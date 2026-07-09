"""Document ingestion for the Unofficial Guide RAG pipeline (Milestone 3).

Stage 1 of the pipeline (see assets/pipeline-diagram.png): document ingestion.

Every source in documents/ was manually pre-cleaned and converted to Markdown
ahead of time, so ingestion just reads the `.md` files with Python's built-in
open().
"""

from __future__ import annotations

from pathlib import Path
from typing import Union

PathLike = Union[str, Path]


def load_document(path: PathLike) -> str:
    """Load a pre-cleaned Markdown source document.

    All sources live in documents/ as `.md`, so this reads the file with
    Python's built-in open() and returns its text. Accepts either a string
    path or a Path object.

    Raises FileNotFoundError if the path does not exist and ValueError if the
    file is not Markdown.
    """
    path = Path(path)
    if not path.is_file():
        raise FileNotFoundError(f"No such document: {path}")
    if path.suffix.lower() != ".md":
        raise ValueError(
            f"Expected a .md file but got '{path.suffix}' for {path.name}. "
            "All sources should be pre-converted to Markdown."
        )
    with open(path, "r", encoding="utf-8") as f:
        return f.read()
