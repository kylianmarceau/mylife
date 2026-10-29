---
tags:
  - vault-support
---

# NOTE TAKING PHILOSOPHY

## Purpose
This skill defines the exact standard for all notes generated in this vault. Any agent producing notes MUST read and follow this file before generating any output. Notes exist for one purpose: to allow the student to study entirely from them, with zero need to return to the source material.

## Core Principle
Notes are NOT summaries. They are structured reconstructions of the source material — complete enough to replace the source for study purposes. Every concept that can be examined must appear in the notes.

For source-driven lecture notes, preserve source-file boundaries. Each file in `Sources/` must map to one generated note file, unless the user explicitly asks for sources to be combined. A note may contain many topics/sections from that source, but multiple source files must not be silently merged into one note.

## Required Writing Style For All Future Notes

Every new or revised study note in `Courses/` must match the readable style of the existing CSC3001F Networks, CSC3002F Operating Systems, and CSC3041F Automated Planning notes. This is a required rule, not an optional preference.

- Explain one idea at a time in short paragraphs, usually one to three sentences. Break up dense paragraphs before they become walls of text.
- Use a brief explanation followed by a table or list when several distinct facts need to be learned. Use numbered steps for processes, bullet lists for properties, and tables for comparisons or symbol meanings.
- Keep the heading hierarchy and local `#### Definitions` blocks used in those course notes. Place formulas, diagrams, and examples directly beside the concept they explain.
- Write the explanation directly as study material. Do not narrate the source with phrases such as “the slide says,” “the source shows,” “the lecture explains,” or routine slide-number callouts. Keep source identification in the topic header.
- Preserve complete examinable content while improving scanability. Do not turn the note into a shallow summary just to shorten paragraphs.
- Before saving, read the note as a student would. Split long prose blocks, replace enumerations with lists or tables, and make sure the result reads naturally without the source open.

Use these existing notes as style references: `Courses/CSC3001F-networks/Lecture_Notes/Transport_Layer.md`, `Courses/CSC3002F-Operating Systems/MICHEL/02_Process_Scheduling.md`, and `Courses/CSC3041F-Automated Planning/Search/04_Heuristic_Search_Astar_And_Beam.md`.

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
  > **Term**: [Exact or near-exact definition from source].
- If a subsection introduces no new technical terms, omit the local `#### Definitions` heading for that subsection
- Do not skip terms even if they seem obvious — the student may not know them
- Each concept must be explained fully — do not truncate or summarise away the mechanics
- For mathematical or algorithmic content: include the full formula or pseudocode and explain its mechanics within the relevant subsection
- All math-related notes, variables, equations, recurrence relations, asymptotic complexity expressions, probability expressions, update rules, and formulas MUST be written in LaTeX. Use inline math with `$...$` and display math with `$$...$$`. Do not write mathematical formulas as plain ASCII text or fenced `text` code blocks. If pseudocode needs formula-like logic, keep the pseudocode as pseudocode and repeat the formal mathematical statement in LaTeX nearby.
- For process-based content: include a numbered step-by-step walkthrough
- For comparative content (e.g. Algorithm A vs B): include a side-by-side comparison table
- Use the source's own examples where they exist; supplement with clear invented examples only where the source has none
- Every relevant diagram, graph, architecture, flow, state machine, queue, tree, timeline, grid, table-shaped visual, or figure from the source must be recreated in the appropriate Core Content subsection where that concept is explained.
- For every graph or diagram created or recreated from source material or existing notes, read and apply `_skills/svg-graph-creation/SKILL.md`. Use hand-authored SVG as the default, including flowcharts, architectures, state diagrams, trees, graphs, and charts. Use another format only when the user explicitly requests it.
- Do not collect diagrams in a separate end-of-file `## Diagrams and Visuals` section. A diagram belongs next to the explanation it supports.
- Preserve the source's technical meaning, labels, arrow directions, and qualifications. Use Markdown tables for tabular information; do not substitute a table for a graph that the SVG skill can recreate.
- Every diagram must have a short caption directly below it explaining what it shows and why it matters.
- SVG diagrams must follow the approved coloured style in `_skills/svg-graph-creation/SKILL.md`, using Introduction I as the visual reference: transparent dark-theme assets, meaningful blue/violet/teal/amber/coral accents, subdued fills, readable labels, balanced spacing, and concept-appropriate layouts. Verify every render at the embedded note width and preserve the relationships being taught.

## Formatting Rules
- Include a clickable Contents list below the topic metadata, before Core Content. Link to every main section and Core Content subsection using same-note heading links.
- Do not include dedicated Summary / Cheat Sheet, Practice Questions, Worked Examples, or Common Mistakes / Gotchas sections. Preserve source examples and essential qualifications within the relevant Core Content subsection instead.
- Use clear heading hierarchy: H1 for topic, H2 for required sections, H3 for source subsections, H4 for local definition blocks
- Bold all technical terms on first use
- Use tables for comparisons — never prose comparisons
- Use numbered lists for processes/steps, bullet lists for properties/features
- Code blocks for pseudocode and actual code only. Formal mathematical notation must use LaTeX, not fenced code blocks.
- Save SVG files in an asset folder near their note and embed them using filesystem-relative Markdown image links. Inline SVG is appropriate when the note already uses it.
- Keep diagram labels concise and readable; explain formal mathematical notation in the surrounding LaTeX.
- Parse and render every new or revised SVG before finishing; check contrast, arrow direction, clipping, and label overlap.
- Never write a section as "See source" or "Refer to textbook" — if it belongs in the notes, it must be written out

## Tone
- Write as a knowledgeable peer explaining to another student, not as a textbook author
- Precise but not unnecessarily formal
- No filler phrases like "it is important to note that" or "as we can see"
- Follow the short-paragraph, list, and table style in **Required Writing Style For All Future Notes** above
