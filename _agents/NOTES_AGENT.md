---
tags:
  - vault-support
---

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
4. _skills/svg-graph-creation/SKILL.md — required whenever creating or recreating graphs or diagrams

## Process
1. Read the source material in full. Do not skim.
2. Preserve source-file boundaries: each source file in `Sources/` must produce exactly one corresponding note file unless the user explicitly asks to combine sources.
3. Identify all topics/sections present in each source file.
4. For each source file, generate one note file following NOTE_TAKING_PHILOSOPHY.md exactly, with the source's topics/sections represented inside that file.
5. Save each file to `Courses/[SubjectName]/[UnitOrSection]/[TopicName].md` when the course already uses section folders, or `Courses/[SubjectName]/[TopicName].md` for flat courses.
6. Before saving, revise the prose to match the Networks, Operating Systems, and Automated Planning notes: short paragraphs, lists for distinct points, tables for comparisons, and direct explanations without slide/source narration.
7. Recreate source graphs and diagrams with `_skills/svg-graph-creation/SKILL.md` as hand-authored SVGs, save them beside the note in an asset folder, and embed them next to their explanations. Preserve technical relationships and verify each render.
8. Add a clickable Contents list below the topic metadata linking to all main sections and Core Content subsections. Do not include dedicated Summary / Cheat Sheet, Practice Questions, Worked Examples, or Common Mistakes / Gotchas sections.

Do not create or maintain course INDEX files unless explicitly requested by the user.

Add the appropriate course tag to each note's YAML `tags` list, following the Course Navigation table in `VAULT_GUIDE.md`. When using a template, replace its `vault-support` tag with the course tag. Preserve existing metadata and other tags when updating notes.

## Quality Check (run before saving any file)
Ask yourself:
- Does every section from NOTE_TAKING_PHILOSOPHY.md appear?
- Is every definition included under the subsection where the term is first introduced?
- Are there no separate top-level Learning Objectives or Key Definitions sections?
- Was `_skills/svg-graph-creation/SKILL.md` used for every created or recreated graph, with SVGs embedded in the Core Content subsection where they belong?
- Are all SVGs rendered and checked for readable labels, meaningful colours, correct arrows, and no overlaps or clipping?
- Is there no separate end-of-file `## Diagrams and Visuals` section?
- Is there a clickable Contents list near the top, and do all its links target existing headings?
- Are dedicated Summary / Cheat Sheet, Practice Questions, Worked Examples, and Common Mistakes / Gotchas sections absent?
- Are source examples and necessary mechanics explained within the relevant Core Content subsection?
- Does the note read like the existing Networks, Operating Systems, and Automated Planning notes, with no long prose blocks?
- Are processes numbered, properties bulleted, and comparisons or symbol sets placed in tables where useful?
- Is the body free of "the slide says" / "the source shows" phrasing and routine slide-number references?
- Could a student pass an exam using only these notes?

If the answer to any of these is no — go back and fill the gaps before saving.

## Output
- One `.md` file per source file saved under `Courses/[Subject]/`
