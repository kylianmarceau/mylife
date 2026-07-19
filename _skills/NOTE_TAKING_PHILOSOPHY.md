# NOTE TAKING PHILOSOPHY

## Purpose
This skill defines the exact standard for all notes generated in this vault. Any agent producing notes MUST read and follow this file before generating any output. Notes exist for one purpose: to allow the student to study entirely from them, with zero need to return to the source material.

## Core Principle
Notes are NOT summaries. They are structured reconstructions of the source material — complete enough to replace the source for study purposes. Every concept that can be examined must appear in the notes.

For source-driven lecture notes, preserve source-file boundaries. Each file in `Sources/` must map to one generated note file, unless the user explicitly asks for sources to be combined. A note may contain many topics/sections from that source, but multiple source files must not be silently merged into one note.

## Required Sections (in order)

Every note file or slide deck MUST contain all of the following sections, in this order:

### 1. Topic Header
- Full topic name
- Subject/course it belongs to
- Source(s) used (title, author, page range or slide numbers)
- Date generated

### 2. Core Content (Main Body)
- Broken into subsections matching the source material's structure
- Every subsection must begin with any definitions needed for that subsection, under a local `#### Definitions` heading
- Define terms where they are first used, not in a separate top-level glossary
- Definition format:
  > **Term**: [Exact or near-exact definition from source]. *In plain language: [one-sentence plain English explanation].*
- If a subsection introduces no new technical terms, omit the local `#### Definitions` heading for that subsection
- Do not skip terms even if they seem obvious — the student may not know them
- Each concept must be explained fully — do not truncate or summarise away the mechanics
- For mathematical or algorithmic content: include the full formula or pseudocode, then a worked example
- All math-related notes, variables, equations, recurrence relations, asymptotic complexity expressions, probability expressions, update rules, and formulas MUST be written in LaTeX. Use inline math with `$...$` and display math with `$$...$$`. Do not write mathematical formulas as plain ASCII text or fenced `text` code blocks. If pseudocode needs formula-like logic, keep the pseudocode as pseudocode and repeat the formal mathematical statement in LaTeX nearby.
- For process-based content: include a numbered step-by-step walkthrough
- For comparative content (e.g. Algorithm A vs B): include a side-by-side comparison table
- Use the source's own examples where they exist; supplement with clear invented examples only where the source has none
- Every relevant diagram, graph, architecture, flow, state machine, queue, tree, timeline, grid, table-shaped visual, or figure from the source must be recreated in the appropriate Core Content subsection where that concept is explained.
- Markdown notes must use Mermaid for diagrams wherever Mermaid can reasonably represent the visual. Use `flowchart`, `sequenceDiagram`, `stateDiagram-v2`, `classDiagram`, `erDiagram`, `graph`, `journey`, or Mermaid-compatible Markdown tables as appropriate.
- Do not collect diagrams in a separate end-of-file `## Diagrams and Visuals` section. A diagram belongs next to the explanation it supports.
- If Mermaid cannot faithfully represent a graph or chart, include a concise Markdown table plus a short caption in the relevant subsection, and state what the source visual shows.
- Every diagram must have a short caption directly below it explaining what it shows and why it matters.
- Mermaid diagrams must be visually polished: use the vault Mermaid theme directive, rounded readable node labels, curved connectors for flowcharts, and consistent class styling for focus, normal, outcome, and warning nodes.

### 3. Worked Examples
- At minimum one worked example per major concept
- Show all steps — do not skip algebra, logic steps, or intermediate states
- Label each step
- If the source provides an example, use it. If not, construct a minimal clear one.

### 4. Common Mistakes / Gotchas
- A bullet list of misconceptions, edge cases, or errors students commonly make on this topic
- Infer these from warning callouts in the source, exam-style questions, or known difficulty areas

### 5. Summary / Cheat Sheet
- A compact revision block at the end
- Contains: key terms (one line each), key formulas, key relationships, and one-sentence takeaways
- Should be usable as a quick-reference on its own

### 6. Practice Questions
- Minimum 3 questions per topic, ranging from recall to application
- Include answers or answer sketches beneath each question using the format: > Answer: ...

## Formatting Rules
- Use clear heading hierarchy: H1 for topic, H2 for required sections, H3 for source subsections, H4 for local definition blocks
- Bold all technical terms on first use
- Use tables for comparisons — never prose comparisons
- Use numbered lists for processes/steps, bullet lists for properties/features
- Code blocks for pseudocode and actual code only. Formal mathematical notation must use LaTeX, not fenced code blocks.
- Use fenced `mermaid` code blocks for source diagrams in Markdown notes. Do not use fenced `text` blocks for diagrams unless the visual cannot be expressed in Mermaid and a table is not suitable.
- Mermaid node labels should be concise, readable, and line-broken with `<br/>` when needed. Avoid fragile syntax in labels: prefer plain ASCII words, and avoid raw parentheses, slashes, pipes, and mathematical notation inside node labels.
- Mermaid blocks should use this visual theme unless there is a clear reason not to:
  ```text
  %%{init: {"theme":"base","themeVariables":{"primaryColor":"#e0f2fe","primaryTextColor":"#0f172a","primaryBorderColor":"#0284c7","lineColor":"#64748b","secondaryColor":"#f8fafc","tertiaryColor":"#dcfce7","fontFamily":"Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif"},"flowchart":{"curve":"basis","htmlLabels":true,"padding":12}}}%%
  ```
- Never write a section as "See source" or "Refer to textbook" — if it belongs in the notes, it must be written out

## Tone
- Write as a knowledgeable peer explaining to another student, not as a textbook author
- Precise but not unnecessarily formal
- No filler phrases like "it is important to note that" or "as we can see"
