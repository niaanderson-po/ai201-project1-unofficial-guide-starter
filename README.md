# The Unofficial Guide — Project 1

> **How to use this template:**
> Complete each section *after* you've built and tested the corresponding part of your system.
> Do not write placeholder text — if a section isn't done yet, leave it blank and come back.
> Every section below is required for submission. One-liners will not receive full credit.

---

## Domain

<!-- What topic or category of knowledge does your system cover?
     Why is this knowledge valuable, and why is it hard to find through official channels?
     Example: "Student reviews of CS professors at [university] — useful because official
     course descriptions don't reflect teaching style, exam difficulty, or workload." -->

---

## Document Sources

<!-- List every source you collected documents from.
     Be specific: include URLs, subreddit names, forum thread titles, or file names.
     Aim for variety — sources that together cover different subtopics or perspectives. -->

| # | Source | Type | URL or file path |
|---|--------|------|-----------------|
| 1 | | | |
| 2 | | | |
| 3 | | | |
| 4 | | | |
| 5 | | | |
| 6 | | | |
| 7 | | | |
| 8 | | | |
| 9 | | | |
| 10 | | | |

---

## Chunking Strategy

<!-- Describe your chunking approach with enough specificity that someone else could reproduce it.
     Include:
     - Chunk size (characters or tokens) and why that size fits your documents
     - Overlap size and why (or why not) you used overlap
     - Any preprocessing you did before chunking (e.g., stripping HTML, removing headers)
     - What your final chunk count was across all documents -->

**Chunk size:**

**Overlap:**

**Why these choices fit your documents:**

**Final chunk count:** 123 chunks across 10 documents

**Sample Chuncks:**

*[1/5]  chunk #0  from codesignal-prep-checklist-problem-list.md  (209 tokens)*

Codesignal Prep Checklist 🖥️ > Problem List

| **Problem** | **Tutorial** |
| --- | --- |
| Find Occurrences of an Element in an Array | [YouTube](https://www.youtube.com/watch?v=4sQL7R5ySUU) |
| Spiral Matrix | [YouTube](https://www.youtube.com/watch?v=BJnMZNwUk1M) |
| Longest Consecutive Sequence | [YouTube](https://www.youtube.com/watch?v=P6RZZMu_maU) |
| Spiral Matrix II | [YouTube](https://www.youtube.com/watch?v=RvLrWFBJ9fM) |
| 4Sum II | [YouTube](https://www.youtube.com/watch?v=3usKZSZC2No&t=188s) |

*[2/5]  chunk #30  from general-coding-skills-evaluation-framework.md  (212 tokens)*

General Coding Skills Evaluation Framework > Framework Specifications

To balance the breadth and depth of the evaluation content with the goals of fostering a positive candidate experience, the maximum allowed time for this framework is 70 minutes (for 4 code writing questions). Longer evaluations allow for increased measurement precision and improve the quality of signal–however, the more time-intensive evaluations become, the more reluctant candidates are to complete them. Moreover, solving the questions in the given timeframe is an important indicator of skill and a key factor in differentiating between candidate skill levels. This time-constrained process simulates on-the-job demands, as software engineers often balance multiple tasks simultaneously. Additionally, offering a limited, 70-minute timeframe helps prevent candidates from engaging in behaviors such as spending time searching for answers online, further promoting the validity of evaluations powered by the framework.

The following sections outline specifications for each module within the General Coding Framework at a high level. These specifications can be used to create variations of questions while ensuring evaluation results are comparable across candidates.

*[3/5]  chunk #61  from general-coding-skills-evaluation-framework.md  (217 tokens)*

General Coding Skills Evaluation Framework > Framework Example Content > Module 4 – Problem Solving

- There is one pair of indices where the sum of the elements is `2^0 = 1`: `(1, 2)`: `numbers[1] + numbers[2] = -1 + 2 = 1`
- There are two pairs of indices where the sum of the elements is `2^1 = 2`: `(0, 0)` and `(1, 3)`
- There are two pairs of indices where the sum of the elements is `2^2 = 4`: `(0, 3)` and `(2, 2)`
- In total, there are `1 + 2 + 2 = 5` pairs summing to powers of 2.

For `numbers = [2]`, the output should be `solution(numbers) = 1`.

- The only pair of indices is `(0, 0)` and the sum is equal to `2^2 = 4`. So, the answer is 1.

*[4/5]  chunk #92  from online-assessments-codesignal.md  (85 tokens)*

CodeSignal

- It is possible to submit a test result to multiple companies. This
    goes both ways – if you do well once, you won’t have to retake the
    test for a good period of time as you can simply share the result
    for other companies. Similarly, if you do poorly and several
    companies request that score (and you do not have a better one to
    share), you can run into trouble.

*[5/5]  chunk #122  from understanding-assessment-score.md  (157 tokens)*

Understanding Assessment Score > Skill Proficiency

Although the skill proficiency feedback is positively correlated to the Assessment Score overall score (i.e., a test-taker that earns more "Expert" level classifications will have a higher overall score than a test-taker that earns primarily "Developing" level classifications), their intended purpose is developmental for test-takers. Skill proficiency levels are calculated independently from Assessment Score, not directly connected to the overall score, and have not been validated for use in making hiring decisions. Because of this, CodeSignal strongly recommends all selection or administrative decisions to be based on test-takers' Assessment Score, which serves as a holistic snapshot of the test-taker's ability, without consideration of individual skill proficiency feedback.

---

## Embedding Model

<!-- Name the embedding model you used and explain your choice.
     Then answer: if you were deploying this system for real users and cost wasn't a constraint,
     what tradeoffs would you weigh in choosing a different model?
     Consider: context length limits, multilingual support, accuracy on domain-specific text,
     latency, and local vs. API-hosted. -->

**Model used:**

**Production tradeoff reflection:**

---

## Grounded Generation

<!-- Explain how your system enforces grounding — how does it prevent the LLM from answering
     beyond the retrieved documents?
     Describe both your system prompt (what instruction you gave the model) and any structural
     choices (e.g., how you formatted the context, whether you filtered low-relevance chunks).
     Do not just say "I told it to use the documents" — show the actual instruction or explain
     the mechanism. -->

**System prompt grounding instruction:**

**How source attribution is surfaced in the response:**

---

## Evaluation Report

<!-- Run your 5 test questions from planning.md through your system and record the results.
     Be honest — a partially accurate or inaccurate result that you explain well is more
     valuable than a suspiciously perfect result. -->

| # | Question | Expected answer | System response (summarized) | Retrieval quality | Response accuracy |
|---|----------|-----------------|------------------------------|-------------------|-------------------|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |
| 4 | | | | | |
| 5 | | | | | |

**Retrieval quality:** Relevant / Partially relevant / Off-target  
**Response accuracy:** Accurate / Partially accurate / Inaccurate

---

## Failure Case Analysis

<!-- Identify at least one question where retrieval or generation did not work as expected.
     Write a specific explanation of *why* it failed, tied to a part of the pipeline.

     "The answer was wrong" is not an explanation.

     "The relevant information was split across a chunk boundary, so retrieval returned
     only half the context — the model didn't have enough to answer correctly" is an explanation.

     "The embedding model treated the professor's nickname as out-of-vocabulary and returned
     results from an unrelated review" is an explanation. -->

**Question that failed:**

**What the system returned:**

**Root cause (tied to a specific pipeline stage):**

**What you would change to fix it:**

---

## Spec Reflection

<!-- Reflect on how planning.md shaped your implementation.
     Answer both questions with at least 2–3 sentences each. -->

**One way the spec helped you during implementation:**

**One way your implementation diverged from the spec, and why:**

---

## AI Usage

<!-- Describe at least 2 specific instances where you used an AI tool during this project.
     For each: what did you give the AI as input, what did it produce, and what did you
     change, override, or direct differently?

     "I used Claude to help me code" is not sufficient.
     "I gave Claude my Chunking Strategy section from planning.md and asked it to implement
     chunk_text(). It returned a function using a fixed character split. I overrode the
     chunk size from 500 to 200 because my documents are short reviews, not long guides." -->

**Instance 1**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*

**Instance 2**

- *What I gave the AI:*
- *What it produced:*
- *What I changed or overrode:*
