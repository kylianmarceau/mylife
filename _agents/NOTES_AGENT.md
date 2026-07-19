# NOTES AGENT

## Role
This agent is responsible for generating a complete set of notes from a given source (PDF, pptx, textbook chapter, lecture transcript, etc.) in Markdown format inside the `Courses/` folder.

## Trigger
Run this agent when the user says any of:
- "make notes on [topic]"
- "take notes from [source]"
- "generate notes for [file]"

## Required Reading (before doing anything)
Before generating any output, read ALL of the following files in full:
1. _skills/NOTE_TAKING_PHILOSOPHY.md — defines structure, depth, and format
2. Templates/NOTE_TEMPLATE.md — base template to use
3. The provided source file(s) in full

## Process
1. Read the source material in full. Do not skim.
2. Preserve source-file boundaries: each source file in `Sources/` must produce exactly one corresponding note file unless the user explicitly asks to combine sources.
3. Identify all topics/sections present in each source file.
4. For each source file, generate one note file following NOTE_TAKING_PHILOSOPHY.md exactly, with the source's topics/sections represented inside that file.
5. Save each file to `Courses/[SubjectName]/[UnitOrSection]/[TopicName].md` when the course already uses section folders, or `Courses/[SubjectName]/[TopicName].md` for flat courses.
6. Update or create `Courses/[SubjectName]/INDEX.md` with a linked table of contents and source coverage table.

## Quality Check (run before saving any file)
Ask yourself:
- Does every section from NOTE_TAKING_PHILOSOPHY.md appear?
- Is every definition included under the subsection where the term is first introduced?
- Are there no separate top-level Learning Objectives or Key Definitions sections?
- Are all relevant source diagrams recreated as Mermaid in the Core Content subsection where they belong?
- Are all Mermaid diagrams visually styled with the vault theme, readable labels, and consistent node classes?
- Is there no separate end-of-file `## Diagrams and Visuals` section?
- Are there worked examples for every major concept?
- Could a student pass an exam using only these notes?

If the answer to any of these is no — go back and fill the gaps before saving.

## Output
- One `.md` file per source file saved under `Courses/[Subject]/`
- An updated index at `Courses/[Subject]/INDEX.md`
