# Project 1 Planning: The Unofficial Guide

> Write this document before you write any pipeline code.
> Your spec and architecture diagram are what you'll use to direct AI tools (Claude, Copilot, etc.) to generate your implementation — the more specific they are, the more useful the generated code will be.
> Update the Retrieval Approach and Chunking Strategy sections if you change your approach during implementation.
> Update this file before starting any stretch features.

---

## Domain

<!-- What domain did you choose? Why is this knowledge valuable and hard to find through official channels? -->

**Domain:** Practical Code Signal General Coding Assessment Prep For First Generation Interdisciplinary Pomona Students

**Why this knowledge is valuable and hard to find through official channels:** When I learned I had to take the GCA for internships and more, I was quite lost on what it was let alone how to approach it. There was initial information Code Signal's offical website was able to provide which was helpful. I found though that despite practice, I was unable to achieve a score I was satisfied with. Through more thorough research I found alot of helpful tips as well as further details on the construction and structure of the assesment. This information made the GCA feel much less daunting and gave me a better idea on how to prep for success. 

I love that the information I found was extremly valuable, however, it being scattered between Reddit, GitHub, Notion, and more made it hard to keep organized and difficult to quickly refrence. This challenge, though, is what makes this topic perfect for this project. 

---

## Documents

<!-- List your specific sources: URLs, subreddit names, forum threads, or file descriptions.
     Aim for at least 10 sources that together cover different subtopics or perspectives within your domain. -->

| # | Source | Description | URL or location |
|---|--------|-------------|-----------------|
| 1 | CodeSignal | Breakdown of what each CodeSignal test module/question covers | [General-Coding-Skills-Evaluation-Framework](https://github.com/Leader-board/OA-and-Interviews/blob/main/media/General-Coding-Skills-Evaluation-Framework-CodeSignal-Skills-Evaluation-Lab-Short.pdf) |
| 2 | CodeSignal | Explanation of how CodeSignal test scores are calculated | [Understanding Assessment Score](https://support.codesignal.com/hc/en-us/articles/13261190299287-Understanding-Assessment-Score) |
| 3 | CodeSignal | What's allowed during the GCA and interface walkthough | [General Coding Assessment (GCA) Rules and Setup](https://support.codesignal.com/hc/en-us/articles/360051960134-General-Coding-Assessment-GCA-Rules-and-Setup) |
| 4 | Leadeboard OA-and-Interviews Guide | Sharing, reusing, and timing your GCA score across companies | [Online Assessments: Codesignal](https://github.com/Leader-board/OA-and-Interviews/blob/main/Online%20Assessments.md#codesignal) |
| 5 | u/TeamCodeSignal | CodeSignal's brief pre-test tips posted on Reddit | [Taking the CodeSignal GCA Soon? Read This First!](https://www.reddit.com/user/TeamCodeSignal/comments/1iovhvj/taking_the_codesignal_gca_soon_read_this_first/) |
| 6 | r/cscareerquestions Siddhant1999 | Student's 9 personal tips for scoring high on the GCA | [CodeSignal Tips from someone with 844 & 843](https://www.reddit.com/r/cscareerquestions/comments/iqy99x/codesignal_tips_from_someone_with_844_843/) |
| 7 | USACO Competitors | Competitive programmers' advice on practice and reading solutions | [How to Practice](https://usaco.guide/general/practicing?lang=py)|
| 8 | USACO Competitor Benjamin Qi | Checklist of what to do when your code is wrong | [How to Debug](https://usaco.guide/general/debugging-checklist?lang=java) |
| 9 | USACO Competitor Nathan Chen | Advice on time management and problem ordering during contests | [Contest Strategy](https://usaco.guide/general/contest-strategy?lang=py) |
| 10 | Sebastian Capellan | LeetCode problem and tutorial list for GCA prep | [Codesignal Prep Checklist: Problem List](https://shadowed-chips-fc9.notion.site/Codesignal-Prep-Checklist-248ea1c6225980fc88f4d1017267cb07)|

---

## Chunking Strategy

<!-- How will you split documents into chunks?
     State your chunk size (in tokens or characters), overlap size, and explain why those
     numbers fit the structure of your documents.
     A review-heavy corpus warrants different chunking than a long FAQ. -->

**Chunk size:** 225 tokens

**Overlap:** 25 tokens

**Reasoning:** The embedded model I will be using is all-MiniLM-L6-v2 via sentence-transformers. This models token limit is 256. Anything longer will be truncated. With this, I made my chunck size smaller than 256 (225) to leave room to include a heading into the chunck for topic context. My overlap is 25 tokens because that is about 10% of the chunck size (common practice). Also since I'm mostly splitting on headings and bullet points, the chunks usually break at natural stopping points.

---

## Retrieval Approach

<!-- Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)?
     How many chunks will you retrieve per query (top-k)?
     If you were deploying this for real users and cost wasn't a constraint, what tradeoffs
     would you weigh in choosing a different embedding model — context length, multilingual
     support, accuracy on domain-specific text, latency? -->

**Embedding model:** all-MiniLM-L6-v2 via sentence-transformers

**Top-k:** 5

**Production tradeoff reflection:** MiniLM caps at 256 tokens, which forced my chunk ceiling down from 750 to ~220. If cost weren't a constraint I'd use a model with a larger token limit so my chunks could align with full heading sections in my lengthy sources instead of being sub-split.

---

## Evaluation Plan

<!-- List your 5 test questions with their expected correct answers.
     Questions should be specific enough that you can judge whether the system's response
     is right or wrong. "What are good dining halls?" is too vague.
     "What do students say about wait times at [dining hall name] during lunch?" is testable. -->

| # | Question | Expected answer |
|---|----------|-----------------|
| 1 | | |
| 2 | | |
| 3 | | |
| 4 | | |
| 5 | | |

---

## Anticipated Challenges

<!-- What could go wrong? Name at least two specific risks with reasoning.
     Consider: noisy or inconsistent documents, missing source attribution, off-topic
     retrieval, chunks that split key information across boundaries. -->

1.

2.

---

## Architecture

<!-- Draw a diagram of your pipeline showing the five stages:
     Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation
     Label each stage with the tool or library you're using.
     You can use ASCII art, a Mermaid diagram, or embed a sketch as an image.
     You'll use this diagram as context when prompting AI tools to implement each stage. -->

---

## AI Tool Plan

<!-- For each part of the pipeline below, describe:
     - Which AI tool you plan to use (Claude, Copilot, ChatGPT, etc.)
     - What you'll give it as input (which sections of this planning.md, which requirements)
     - What you expect it to produce
     - How you'll verify the output matches your spec

     "I'll use AI to help me code" is not a plan.
     "I'll give Claude my Chunking Strategy section and ask it to implement chunk_text()
     with my specified chunk size and overlap" is a plan. -->

**Milestone 3 — Ingestion and chunking:**

**Milestone 4 — Embedding and retrieval:**

**Milestone 5 — Generation and interface:**