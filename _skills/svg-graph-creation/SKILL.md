---
name: svg-graph-creation
description: Create or recreate polished SVG graphs and diagrams from uploaded images, source slides/PDFs, or course notes. Use when Codex needs to turn a graph, chart, resource-allocation graph, process/state diagram, OS/network diagram, or hand-drawn/source visual into a clean, colour-coded dark-theme SVG for this vault.
tags:
  - vault-support
---

# SVG Graph Creation

## Purpose

Create SVG diagrams for study notes by recreating the meaning, structure, labels, arrows, and visual relationships of the source graph. Uploaded images, screenshots, slides, and notes are structural references; convert them into the vault's dark, clean study-diagram style by default. Preserve a source screenshot's original light/exam/printed theme only when the user explicitly asks for the original visual style, exact screenshot styling, or a white/light version.

## Workflow

1. Inspect the source image or source notes first.
2. Identify graph type, nodes, labels, edges, axes, data curve shape, legends, and any special notation.
3. Default to vault-theme restyling. Keep source geometry and technical meaning, but use the vault's dark SVG style. Preserve source colors/background/typography only when explicitly requested.
4. Recreate graphs and diagrams as hand-authored SVG by default. Use another format only when the user explicitly requests it.
5. Preserve semantic relationships over pixel-perfect copying. Keep node placement close to the source when it helps recognition.
6. Add only labels, legends, or captions that clarify the source. Do not invent new technical content.
7. Save SVGs near the note that uses them, or inline the SVG directly in Markdown when the surrounding notes already use inline SVG.
8. Verify the SVG is readable at the target note width before finishing.

## Vault SVG Theme

Use this default palette for generated/recreated graphs unless the user explicitly asks to preserve the source screenshot's original theme or the surrounding note establishes a stronger local theme:

| Element or role | Accent | Suggested dark fill |
|---|---|---|
| Data, perception, inputs, primary route | `#66b3ff` blue | `#20344c` |
| Reasoning, planning, models, commitments | `#b89aff` violet | `#302b46` |
| Learned representations, outputs, successful outcomes, secondary route | `#5ad4b5` teal | `#1b3835` |
| Feedback, control signals, new arrivals, qualifications | `#ffc778` amber | `#3d3326` |
| Failures, warnings, risk, hardness | `#ff939b` coral | `#3f2a33` |
| Infrastructure and neutral objects | `#adb9cb` muted | `#272f3b` |
| Important text | `#f8fafc` | — |
| Muted text | `#adb9cb` | — |
| Background | Transparent; use the note/app background | — |
| Font | `Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, Segoe UI, sans-serif` | — |

## Approved Coloured SVG Style

Use [Introduction I](../../Courses/CSC3044S-AI%20Systems/01_Introduction_I.md) and its SVG assets as the visual reference for new and revised diagrams. This is the vault default, not a one-note experiment.

- Give colour a consistent meaning within each diagram. Match connector and arrowhead colours to their source or signal; use near-white for neutral relationships. Keep labels and arrow direction sufficient to understand the graph without colour.
- Use the palette above as a starting point, not a requirement to use every colour. Keep important labels near-white, use accents for titles and outlines, and use subdued fills for contrast.
- Choose geometry for the concept: parallel lanes for competing controllers, a visible boundary for an agent or subsystem, tree branches for decisions, curved feedback loops, network layers for neural connections, and spatial sketches for routes. Creative layouts must preserve every technical relationship and qualification.
- Use balanced spacing, concise multiline labels, clean curved or orthogonal connectors, and small structural icons only when they clarify the content. Avoid a uniform chain of boxes when the concept has a more useful visual structure.
- Save SVGs under the vault's `diagrams/[Course]/[Optional Unit]/[NoteName]/` folder, embed them with relative Markdown image links, and retain a short italic caption directly underneath. Inline SVG remains appropriate where the note already uses it.
- When styling a note, use a coloured lecture-reference callout and a few coloured callouts for existing key distinctions, warnings, or takeaways. Keep headings and navigation intact, preserve study content, and do not add redundant explanations. Inline coloured spans in callout titles are acceptable when the active Obsidian theme suppresses native accents.

Styling rules:

- Use no gradients, shadows, decorative blobs, or ornamental backgrounds.
- For Markdown/Obsidian raw SVG blocks, do not insert blank lines inside `<svg>...</svg>`.
- Prefer inline SVG attributes over a `<style>` block because Obsidian renders inline attributes more reliably.
- Do not draw a full background rectangle for embedded note diagrams unless explicitly requested. Never add a white background for normal vault-style output.
- Keep labels short and close to the visual element they describe.
- Use rounded rectangles only for graph objects such as resources, callouts, or legend boxes.
- Use crisp strokes, usually `1.4` to `2.4` px.
- Use `vector-effect="non-scaling-stroke"` on important strokes.
- Use a responsive root such as `<svg width="100%" viewBox="0 0 900 520" role="img">`.
- Include `<title>` and, when useful, `<desc>` for accessibility.
- Use explicit marker colours matching their connector strokes for reliable Obsidian rendering. Keep the SVG transparent over the dark note background; do not depend on `context-stroke` or inherited CSS variables for essential colours.

## Common Graph Patterns

### Resource-allocation graphs

Use for OS deadlock/resource allocation diagrams.

- Processes: circles with blue stroke, muted process labels such as `P1`, `P2`.
- Resource types: rounded rectangles with gray stroke and no fill.
- Resource instances: small gray filled dots inside resource rectangles.
- Request edge: white arrow from process to resource.
- Assignment edge: white arrow from resource to process.
- Use a compact legend only when the notation is not obvious.
- Multiple instances must be drawn as multiple dots, not a number label unless the source uses a number.
- A cycle should be visually traceable by arrow direction.
- Use the source's node labels (`P`, `T`, `R`, subscripts) but style them like the vault example: gray sans-serif text, blue process outlines, gray resource outlines, and white relationship edges.

### Curves and charts

Use for conceptual curves such as CPU utilization versus degree of multiprogramming.

- Axes: white or near-white arrowed axes.
- Axis labels: white, concise, centered along the axis; rotate vertical labels.
- Curves: blue stroke, no fill, smooth Bezier paths.
- Threshold/callout arrows: white line with simple arrowhead and short label.
- Do not over-grid conceptual charts; use no grid unless the source has one.
- Preserve the qualitative shape, especially peaks, drops, and asymptotes.

### Flow and state diagrams

- Use simple circles, rounded rectangles, and arrowed connectors.
- Keep connector crossings minimal.
- Use meaningful accents from the approved palette for active/process/state elements and muted strokes for infrastructure/resources.
- Preserve source order and direction where possible.

## SVG Construction Rules

Start from this Obsidian-safe skeleton. Keep it as one continuous raw HTML block with no blank lines inside the SVG:

```svg
<svg width="100%" viewBox="0 0 680 380" role="img" xmlns="http://www.w3.org/2000/svg">
<title>Diagram title</title>
  <defs>
    <marker id="arrow" viewBox="0 0 10 10" refX="8" refY="5"
            markerWidth="6" markerHeight="6" orient="auto-start-reverse">
      <path d="M2 1L8 5L2 9" fill="none" stroke="#ffffff"
            stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
    </marker>
  </defs>
  <line x1="80" y1="310" x2="640" y2="310" stroke="#ffffff" stroke-width="1.5" marker-end="url(#arrow)"/>
</svg>
```

Implementation guidance:

- Prefer explicit SVG geometry over generated raster images.
- Put `fill`, `stroke`, `font-size`, `font-family`, and `marker-end` directly on elements.
- Use `<path>` for curved relationships and conceptual curves.
- Use marker arrowheads instead of manually drawing arrow triangles repeatedly.
- Use grouped elements (`<g>`) for repeated nodes.
- Avoid raw mathematical notation inside tiny labels; put formulas in surrounding Markdown when they need to be studied.
- Keep all text within the `viewBox`; test long labels manually.

## Verification Checklist

Before finishing, check:

- The SVG opens or renders without XML errors.
- Every source node, label, axis, edge, legend item, and key visual relation is represented.
- Arrow direction is correct.
- Render every SVG at the target note width on a dark background. Text must be readable and must not overlap graph elements; inspect every render, not just a sample.
- Accent colours, connector strokes, and arrowheads follow the approved style; source nodes and edges are all accounted for.
- Multi-instance resources show the correct number of dots.
- Conceptual curves preserve the source shape and callout placement.
- The output is useful in notes without needing the original source image.
