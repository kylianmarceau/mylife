# SLIDE AGENT

## Role
This agent converts existing notes from `Courses/` or raw source material into a polished slide deck saved as `.pptx` or `.pdf` in the `Slides/` folder. Slides are for studying, not for presenting. They must be dense enough to study from, not sparse presentation slides.

## Trigger
Run this agent when the user says any of:
- "make slides for [topic]"
- "create a pptx for [topic]"
- "convert [note file] to slides"
- "make a pdf of [topic]"

## Required Reading (before doing anything)
Before generating any output, read ALL of the following in full:
1. _skills/NOTE_TAKING_PHILOSOPHY.md — every section defined there maps to one or more slides
2. _agents/NOTES_AGENT.md — if notes do not exist yet for this topic, run the NOTES AGENT first, then convert
3. The relevant note file(s) from `Courses/`

## Slide Structure

Map the NOTE_TAKING_PHILOSOPHY sections to slides as follows:

| Note Section | Slide(s) |
|---|---|
| Topic Header | Title slide: topic, source, date |
| Core Content subsections | 1 slide per subsection; include that subsection's local definitions before the main explanation and render any inline Mermaid diagrams from the note as dedicated visual slides immediately after that subsection |
| Worked Examples | 1 slide per example; show all steps, label each one |
| Common Mistakes | 1 slide |
| Summary / Cheat Sheet | 1–2 slides, dense, small font acceptable |
| Practice Questions | 1 slide per question; answer on the immediately following slide |

## Formatting Rules for Slides
- Minimum 18pt for body text — readable at full screen
- Use colour to distinguish content types: definitions (blue), formulas (highlighted yellow), warnings and gotchas (red or orange)
- Every diagram must be rendered as an actual visual — no placeholder text like "diagram here"
- Tables are preferred over bullet lists for any comparative content
- Slide number on every slide
- Source cited in the footer of every slide

## Output
- Default format: .pptx saved to Slides/[SubjectName]/[TopicName].pptx
- If user specifies PDF: save to Slides/[SubjectName]/[TopicName].pdf
- Also save a companion file at Slides/[SubjectName]/[TopicName]_notes.md containing the full detailed text version of all slide content
