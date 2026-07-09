"""Chunking for the Unofficial Guide RAG pipeline (Milestone 3).

Stage 2 of the pipeline (see assets/pipeline-diagram.png): chunking via a
recursive split.

Strategy (from planning.md > Chunking Strategy):
  - chunk size: 225 tokens (leaves room under MiniLM's 256-token limit for a
    heading to be prepended to every chunk)
  - overlap:    25 tokens (~10% of chunk size)
  - recursive split: break on the largest natural boundary that fits
    (paragraph -> line -> sentence -> word), so chunks end at sensible places
  - heading included: each chunk is prefixed with the breadcrumb of the
    Markdown headings it falls under, giving the embedder topic context

Tokens are counted with the same tokenizer the embedder uses
(all-MiniLM-L6-v2), so the 225-token ceiling is measured, not estimated.
"""

from __future__ import annotations

import re
from functools import lru_cache
from typing import List, Tuple

# Separators tried in order by the recursive splitter: paragraph, line,
# sentence, word, then a hard character split as the last resort.
_SEPARATORS = ["\n\n", "\n", ". ", " ", ""]


@lru_cache(maxsize=1)
def _tokenizer():
    """Load and cache the MiniLM tokenizer (downloaded once, then reused)."""
    from transformers import AutoTokenizer

    return AutoTokenizer.from_pretrained("sentence-transformers/all-MiniLM-L6-v2")


def n_tokens(text: str) -> int:
    """Number of MiniLM tokens in `text` (excluding the [CLS]/[SEP] specials)."""
    return len(_tokenizer().encode(text, add_special_tokens=False))


def _split_sections(markdown: str) -> List[Tuple[str, str]]:
    """Split a Markdown document into (heading_breadcrumb, body) sections.

    A new section starts at every `#`..`######` heading line. The breadcrumb is
    the trail of currently-open headings, e.g. "Understanding Assessment Score
    > How Assessment Score is Calculated", so a chunk carries the full topic
    path, not just its nearest subheading.
    """
    heading_re = re.compile(r"^(#{1,6})\s+(.*)$")
    sections: List[Tuple[str, str]] = []
    open_headings: dict = {}  # level -> title
    breadcrumb = ""
    buffer: List[str] = []

    def flush():
        body = "\n".join(buffer).strip()
        if body:
            sections.append((breadcrumb, body))

    for line in markdown.splitlines():
        match = heading_re.match(line)
        if match:
            flush()
            buffer.clear()
            level = len(match.group(1))
            title = match.group(2).strip()
            # A heading closes any deeper or same-level headings above it.
            for lvl in [l for l in open_headings if l >= level]:
                del open_headings[lvl]
            open_headings[level] = title
            breadcrumb = " > ".join(open_headings[l] for l in sorted(open_headings))
        else:
            buffer.append(line)
    flush()
    return sections


def _recursive_split(text: str, max_tokens: int) -> List[str]:
    """Split `text` into atoms that are each <= max_tokens, preferring the
    largest natural boundary (see _SEPARATORS) before falling back to a finer
    one. Concatenating the returned atoms reproduces the original text."""

    def split(segment: str, separators: List[str]) -> List[str]:
        if n_tokens(segment) <= max_tokens:
            return [segment] if segment else []
        sep = separators[0]
        if sep == "":
            return _hard_token_split(segment, max_tokens)
        if sep not in segment:
            return split(segment, separators[1:])
        atoms: List[str] = []
        parts = segment.split(sep)
        for i, part in enumerate(parts):
            # Re-attach the separator to every part except the last so the
            # atoms still concatenate back into the original text.
            piece = part + (sep if i < len(parts) - 1 else "")
            if not piece:
                continue
            if n_tokens(piece) <= max_tokens:
                atoms.append(piece)
            else:
                atoms.extend(split(piece, separators[1:]))
        return atoms

    return split(text, _SEPARATORS)


def _hard_token_split(text: str, max_tokens: int) -> List[str]:
    """Last-resort split of an unbreakable run by decoding fixed token windows."""
    tok = _tokenizer()
    ids = tok.encode(text, add_special_tokens=False)
    pieces = []
    for start in range(0, len(ids), max_tokens):
        window = ids[start : start + max_tokens]
        pieces.append(tok.decode(window))
    return pieces


def _pack_with_overlap(atoms: List[str], budget: int, overlap: int) -> List[str]:
    """Greedily merge atoms into chunk bodies of up to `budget` tokens, seeding
    each new chunk with the trailing ~`overlap` tokens of the previous one."""
    chunks: List[str] = []
    current: List[str] = []
    current_tokens = 0

    for atom in atoms:
        atom_tokens = n_tokens(atom)
        if current and current_tokens + atom_tokens > budget:
            chunks.append("".join(current))
            # Carry the last few atoms forward as overlap.
            seed: List[str] = []
            seed_tokens = 0
            for prev in reversed(current):
                t = n_tokens(prev)
                if seed_tokens + t > overlap:
                    break
                seed.insert(0, prev)
                seed_tokens += t
            current = seed
            current_tokens = seed_tokens
        current.append(atom)
        current_tokens += atom_tokens

    if "".join(current).strip():
        chunks.append("".join(current))
    return chunks


def chunk_text(text: str, chunk_size: int = 225, overlap: int = 25) -> List[str]:
    """Split a Markdown document into overlapping, heading-prefixed chunks.

    Each returned chunk:
      - is at most `chunk_size` MiniLM tokens (heading prefix included),
      - overlaps the previous chunk within the same section by ~`overlap`
        tokens, and
      - begins with the heading breadcrumb of the section it came from.

    Returns a list of chunk strings.
    """
    chunks: List[str] = []
    for breadcrumb, body in _split_sections(text):
        prefix = f"{breadcrumb}\n\n" if breadcrumb else ""
        # Reserve room for the heading so the whole chunk stays within budget.
        budget = max(1, chunk_size - n_tokens(prefix))
        atoms = _recursive_split(body, budget)
        for chunk_body in _pack_with_overlap(atoms, budget, overlap):
            chunks.append(prefix + chunk_body.strip())
    return chunks


if __name__ == "__main__":
    # Milestone 3 inspection: print 5 representative chunks and read them by eye.
    # For each, ask: does this make sense on its own? Could someone answer a
    # question from this chunk alone, without the surrounding text?
    from pathlib import Path

    from ingest import load_document

    docs_dir = Path(__file__).parent / "documents"

    all_chunks = []
    for md_file in sorted(docs_dir.glob("*.md")):
        for chunk in chunk_text(load_document(md_file)):
            all_chunks.append((md_file.name, chunk))

    print(f"{len(all_chunks)} chunks across {len(list(docs_dir.glob('*.md')))} documents\n")

    # Sample 5 chunks spread evenly across the whole corpus, not just one file.
    n = len(all_chunks)
    sample_idx = [round(i * (n - 1) / 4) for i in range(5)] if n >= 5 else range(n)

    for rank, idx in enumerate(sample_idx, 1):
        source, chunk = all_chunks[idx]
        print("=" * 72)
        print(f"[{rank}/5]  chunk #{idx}  from {source}  ({n_tokens(chunk)} tokens)")
        print("-" * 72)
        print(chunk)
        print()
