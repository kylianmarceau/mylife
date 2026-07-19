---
name: codex-marker
description: Mark student scripts by first creating or locating a Markdown memo, extracting the submitted work, comparing the extraction against the memo, and writing a marked-script Markdown file with marks, feedback, and confidence. Use for handwritten or typed exam solutions, partial answers, calculation scripts, algorithm traces, diagrams, and question-by-question feedback in this vault.
---

# Codex Marker

## Overview

Mark submitted answers fairly against a written memo. The normal output is not only a chat response: create a memo Markdown file when one is missing, extract the submitted script, then create a marked-script Markdown file showing the extraction, comparison, marks, feedback, and marking confidence.

## Workflow

1. Identify the script, exam, and memo.
   - Use the user-provided images, scans, PDFs, or files as the submitted script.
   - Use the memo named by the user. If none is named, infer the closest memo from `Courses/**/Exam Prep/*Memo*.md`.
   - Open the exam paper as well as the memo when question wording, mark allocation, or subpart numbering matters.
   - If no suitable memo exists, create a memo Markdown file before marking.
   - If the user asks to mark only a section or question range, create a memo for that section/range rather than the entire exam.
   - If the memo is absent or ambiguous, read the relevant course note before deciding model answers and mark allocation.

2. Create or normalize the memo.
   - Save the memo as Markdown near the exam or script unless the user specifies another location.
   - Include exam title, source file, scope, total marks, question wording, expected answer, mark allocation, and grading notes.
   - If no official memo is available, label the file as an `inferred memo` and list the course notes or calculations used.
   - For algorithm or numeric questions, compute the reference answer independently and include enough trace or method to support marking.

3. Extract the student's work.
   - Inspect every uploaded page or image in order.
   - Transcribe the submitted answer into the marked-script file before assigning marks.
   - Preserve question/subpart labels, final answers, calculations, algorithms, tables, diagrams, and crossed-out work.
   - Treat clearly crossed-out work as not submitted unless the final answer depends on it.
   - Mark unreadable content as `unclear` and state the assumption used. Do not silently turn uncertain handwriting into a conceptual error.

4. Mark against the memo.
   - Allocate marks using the memo's mark total and submark structure where available.
   - If the memo gives only a final answer, split marks reasonably across method, intermediate steps, and final result, then state that split.
   - Award equivalent notation, wording, or reasoning when it is mathematically and conceptually correct.
   - Penalize incorrect reasoning even when the final answer is accidentally correct, unless the memo awards final-answer-only marks.
   - For algorithm traces, check the required policy exactly: queue/stack order, tie handling, reached-list timing, pruning condition, backup rule, and stated assumptions.
   - For numeric work, check formulas, substitution, arithmetic, units/interpretation, and final answer separately.

5. Add marking confidence.
   - Give an overall confidence rating: `high`, `medium`, or `low`.
   - Give per-question confidence when handwriting, missing pages, absent memo, or ambiguous mark allocation affects reliability.
   - Lower confidence when an official memo is missing, handwriting is unclear, the submitted answer is incomplete, or mark splits had to be inferred.
   - State exactly what would increase confidence, such as an official memo, clearer image, or missing page.

6. Write the marked-script Markdown file.
   - Save it near the exam or script unless the user specifies another location.
   - Include links/paths to the memo, exam, and script pages used.
   - Include the extracted student text before the mark table.
   - Include a comparison table that shows expected answer, student answer summary, awarded marks, max marks, confidence, and feedback.
   - Include totals, unclear items, biggest fixes, and coverage notes.

7. Handle uncertainty and fairness.
   - If handwriting is legible enough to infer the intended answer, mark the inferred answer and note the inference.
   - If a key symbol, number, or word is unreadable, assign a provisional mark only when the surrounding working supports it.
   - Do not invent missing steps. Give credit for visible reasoning only.
   - Do not punish minor spelling, layout, or notation differences that do not affect correctness.
   - Keep feedback concise and actionable; focus on what lost marks and how to fix it.

## Output Format

Create a Markdown file with this structure:

```md
# Marked Script: <exam/title/scope>

**Marked against**: <memo path or memo title>  
**Exam**: <exam path>  
**Script pages reviewed**: <count or filenames>  
**Total**: <awarded>/<available>  
**Status**: final | provisional  
**Overall marking confidence**: high | medium | low

## Extracted Student Script

<question-by-question transcription>

## Marking Table

| Question | Awarded | Max | Confidence | Expected | What I read | Feedback |
|---|---:|---:|---|---|---|---|

## Unclear Items

...

## Biggest Fixes

...

## Coverage Notes

...
```

## CSC3041F Search-Specific Checks

When marking the CSC3041F Search mock exam, pay special attention to:

- State-space formulation: states, actions, transition model, initial state, goal test, and cost model must be distinct.
- BFS/UCS/DFS/IDS: order of expansion, reached-list behavior, path cost versus depth, and cutoff meaning.
- Heuristics/A*/beam: admissibility versus consistency, $f(n)=g(n)+h(n)$, Manhattan/misplaced-tile calculations, and beam-pruning guarantees.
- Minimax/max-n/alpha-beta: correct player backup rule, utility scalar versus vector, alpha/beta update node type, and pruned leaves.
- Evaluation functions/MCTS: terminal utility versus cutoff `EVAL`, horizon effect, expected utility, MCTS phases, and UCB exploration term.
