---
tags:
  - reasoning-in-ai
---

# Video Understanding

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture5_Video_Understanding.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture5_Video_Understanding.pdf), Prof Patrick Marais, slides 1-23 (primary papers: ViViT, Arnab et al. 2021; TimeSformer; Qwen2-VL; Video-MME)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#From image to video|From image to video]]
  - [[#Which frames to sample|Which frames to sample]]
  - [[#Frame tokens versus tubelet tokens|Frame tokens versus tubelet tokens]]
  - [[#Telling the model when each token is|Telling the model when each token is]]
  - [[#Why video breaks quadratic attention|Why video breaks quadratic attention]]
  - [[#Fix 1: factorized space-time attention|Fix 1: factorized space-time attention]]
  - [[#Fix 2: pooling and resampling|Fix 2: pooling and resampling]]
  - [[#Video foundation models versus video-LLMs|Video foundation models versus video-LLMs]]
  - [[#The context wall|The context wall]]
  - [[#Scaling to long video|Scaling to long video]]
  - [[#The cheapest information is not visual|The cheapest information is not visual]]
  - [[#Taxonomy of video tasks|Taxonomy of video tasks]]
  - [[#Temporal grounding|Temporal grounding]]
  - [[#Is the model using time at all?|Is the model using time at all?]]
  - [[#Common video benchmarks|Common video benchmarks]]

---

## Core Content

### From image to video

The image VLM flow is: ViT tokenizes an image → CLIP aligns it with text → a projector feeds an LLM → production VLM answers. A video is "just a sequence of images", so what changes?

| Change | Detail |
|---|---|
| **Scale** | 1 minute at 24 fps = 1,440 frames. Naively $1{,}440 \times 576 \approx 830{,}000$ tokens per minute — impossible with quadratic attention |
| **Time** | Motion, causality, order, before/after — not visible in any single frame |
| **New questions** | "What happened just before the crash?" · "Did she pick up the cup or put it down?" · "When does the goal happen?" |

A practical design must **shrink the token stream**.

![Frame interface](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/frame-interface.svg)

*Raw video → frame sampling → patch or tubelet embedding → space + time positions → LLM answer.*

### Which frames to sample

The common first step is **frame down-sampling**.

| Strategy | How | Trade-off |
|---|---|---|
| Uniform | Every $k$-th frame | Simple and standard, but ignores content: fast events between samples vanish; static scenes waste tokens |
| FPS-based | Fixed frames per second | Token count scales with duration |
| Scene-change / keyframe | Pick frames where content changes | Adapts to content |
| Query-aware | Pick frames relevant to the question | Needs the question up front |

### Frame tokens versus tubelet tokens

#### Definitions

> **Frame tokens**: Patchify each sampled frame independently (as for a single image) and concatenate the frames' tokens in order.

> **Tubelet**: A token spanning a $P \times P$ patch across $\tau$ consecutive frames, embedded with a 3D convolution / linear projection over $t \times h \times w$.

| | Frame tokens | Tubelet tokens |
|---|---|---|
| Time information | Only in sequence order + position encoding (a time/frame embedding is added to each patch's position) | Short-term motion is inside each token |
| Token count | Higher | Fewer for the same clip |
| Used by | Most video-LLMs | ViViT, VideoMAE |

![Tubelet](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/tubelet.svg)

*The same spatial patch from three consecutive frames is flattened across space and time into one tubelet embedding.*

### Telling the model when each token is

Self-attention is permutation-invariant, so position must be injected — now on three axes: height, width, and time.

#### Definitions

> **M-RoPE (Multimodal RoPE)**: Rotary position encoding factorized over $(t, h, w)$, introduced in Qwen2-VL.

> **Absolute timestamps**: Injecting each frame's real time (seconds) so "when" questions can be answered in real units.

How M-RoPE works:

1. **2D RoPE** splits the token embedding in half, applying 1D RoPE by $x$ to one half and by $y$ to the other.
2. **M-RoPE** splits the embedding three ways — $x$, $y$, $t$ — and rotates each part by its own coordinate.
3. Tokens close in space get similar positional encodings, and so do tokens close in time.
4. One scheme handles 1D, 2D, and 2D+T: text tokens have $h = w = 0$ with only $t$ changing; image tokens have $h, w$ with $t = 0$.

Why temporal position matters more than for images:

- For a static image, slightly inaccurate patch positions degrade understanding.
- For video, confusing frame order **destroys causality** ("picked up" vs "put down").

$$
\text{video token} = \text{embed}(\text{patch/tubelet content}) + \text{embed}(\text{where: } h, w;\ \text{when: } t)
$$

The Transformer core is still completely unchanged.

### Why video breaks quadratic attention

For video, sequence length $n = T \cdot S$, with $T$ sampled frames and $S$ tokens per frame (e.g. 256-576). Attention costs $O(n^2) = O((T S)^2)$.

- 32 frames × 256 tokens = 8,192 tokens → $8{,}192^2 \approx 67$ million attention scores per head per layer.
- Doubling the frames → $4\times$ the cost.

Three mitigations:

| Approach | Idea |
|---|---|
| Factorize attention | Never attend over all $T \cdot S$ tokens at once |
| Pool / resample | Shrink $S$ or $T$ with a fixed or learned reducer (Perceiver-style) |
| Sparsify | Attend to a subset (windows, keyframes); useful for long video |

### Fix 1: factorized space-time attention

#### Definitions

> **Factorized space-time attention**: Replacing one attention over all $T \cdot S$ tokens with a temporal attention (each spatial position attends across frames) followed by a spatial attention (tokens attend within their own frame).

1. **Temporal attention**: each patch attends only to the same spatial location in other frames; everything else is masked.
2. **Spatial attention**: take those time-aware tokens and attend across all patches within each frame; other frames are masked.
3. Implement both with tensor reshaping so standard Transformer attention blocks can be reused.

$$
O\big((T \cdot S)^2\big) \;\longrightarrow\; O\big(T^2 \cdot S + T \cdot S^2\big)
$$

![Factorized attention](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/factorized-attention.svg)

*Rows are frames and columns spatial positions. Joint attention connects a query to everything; spatial attention to its frame; temporal attention to its location across frames.*

**Trade-off**: factorization can miss correlations that are jointly spatial and temporal, but it is usually worth it (ViViT, TimeSformer).

### Fix 2: pooling and resampling

Many production video-VLMs reduce the token count before the LLM sees it.

| Method | Reduces | How |
|---|---|---|
| Spatial pooling | $S$ | Reshape ViT tokens to a grid (196 → $14 \times 14$), average $2 \times 2$ blocks → $7 \times 7$ (25% of the tokens) |
| Temporal pooling | $T$ | Average the corresponding token across nearby frames (e.g. sets of 4 consecutive frames) |
| Learned resampling | Whole clip | A Perceiver Resampler / Q-Former maps a clip to a fixed number of tokens regardless of length — learned queries as a bottleneck over space-time. Flamingo's resampler was designed for this: many frames in, 64 tokens out |

> [!warning] <span style="color: #ff939b">Compression loses detail</span>
> Every pool or resample step throws away temporal or spatial detail. Pool too much and you can no longer tell "picked up" from "put down". Video-VLMs differ mostly in **how they compress**, not in the Transformer core.

### Video foundation models versus video-LLMs

| | Video foundation models | Video-LLMs / VLMs (image VLM + time) |
|---|---|---|
| Examples | ViViT, TimeSformer, VideoMAE, VideoMamba | Video-ChatGPT, Video-LLaVA, VideoLLaMA, Qwen2.5-VL, InternVL (video mode) |
| Goal | Strong video representations (classification, retrieval, action recognition) | Open-ended video chat, QA, captioning, grounding |
| Time handling | Tubelets + factorized attention, trained end-to-end | Sample frames → per-frame ViT → compress → LLM reasons over time |
| Relation to images | Extends ViT into 3D | Extends align, bridge, instruction-tune with a temporal front-end |

### The context wall

- Even at 1 fps and only 256 tokens per frame, a 1-hour video needs about **920k tokens** — beyond most context windows.
- But 1 fps already loses most motion; real understanding needs **more** frames, not fewer.

So long-video understanding is fundamentally a **compression and retrieval** problem.

![Context wall](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/context-wall.svg)

*At 1 fps and 256 tokens/frame: 1 s = 256, 10 s = 2,560, 1 min = 15,360, 10 min = 153,600, and 1 hour = 921,600 tokens, crossing a 128k context around 8 minutes.*

### Scaling to long video

| Strategy | Idea | Cost / limitation |
|---|---|---|
| Keyframe selection | Score frames for relevance (to the query or by scene change) and keep the informative ones | A bad selector discards the answer; query-aware selection needs the question first |
| Memory / hierarchical | Summarize chunks into compact memory tokens; reason over summaries ("read the video like chapters") | Lossy; errors compound across chunks |
| Streaming / online | Process video as it arrives with a running state | No global lookback unless stored; "earlier" questions are harder |
| Other modalities | Fuse audio and subtitles, which carry much information at almost no visual-token cost | Not always present or accurate; can leak answers in evaluation |

None of these is solved. Watching a 2-hour film and answering a question about minute 12 is still an open problem.

### The cheapest information is not visual

In lectures, news, and tutorials, most meaning is in the **speech**, not the pixels.

#### Definitions

> **ASR (automatic speech recognition)**: Converting speech audio into a text transcript.

- Subtitles / ASR transcripts are already text: almost free for the LLM and slot straight into the sequence.
- Audio events (doorbell, crash, applause) disambiguate visually ambiguous scenes.
- Design pattern: interleave frame tokens with transcript text on the same timeline, aligned by timestamps.

This reframes many video benchmarks: a model can score well by reading subtitles and barely watching. Production "video understanding" is usually **multimodal** (vision + audio + text); vision-only understanding is much harder.

### Taxonomy of video tasks

| Task | Question form | Temporal reasoning needed |
|---|---|---|
| Action recognition | "What action is this?" (classification) | Low-medium; a few frames often suffice |
| Video captioning | "Describe what happens." | Medium; must order events and describe change |
| Video QA | "Why did X do Y?" "What happened after Z?" | Medium-high; causal, before/after, counting over time |
| Temporal grounding | "When does event E occur?" → time span | High; must localize in time |
| Dense video captioning | Caption every event with its timestamp | High; detect, localize, and describe jointly |

A model can be good at a low-temporal task and weak at a demanding one, which is why benchmarks separate them.

### Temporal grounding

#### Definitions

> **Temporal grounding**: Answering "when in the video?" with a time span — the temporal analogue of spatial grounding's "where in the image?" → box.

![Temporal grounding](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/05_Video_Understanding/temporal-grounding.svg)

*For "When does the player score the goal?" in a 2-minute clip, the model predicts the interval 0:47–0:59.*

- The output is just tokens: the model emits timestamps as text, enabled by absolute-time positions.
- It is hard because "when" cannot be answered from one frame or a global summary. The model must align language to the timeline and inspect frames at fine granularity.

### Is the model using time at all?

| Shortcut | Problem | Diagnostic |
|---|---|---|
| **Single-frame bias** | Many "video" questions are answerable from one good frame ("What sport is this?"); a model ignoring motion can top the leaderboard | Feed a single frame or shuffle frame order; if the score barely drops, the benchmark is not testing time |
| **Subtitle/audio shortcut** | With transcripts, a model can read rather than watch | Evaluate with and without subtitles / with audio muted |

How benchmarks counter this:

- **Video-MME** covers short to long clips and reports results with and without subtitles.
- **TempCompass** and similar suites build questions a single frame or shuffled order cannot answer.

When a video model "wins", ask: would it still win on one frame, on shuffled frames, or with audio muted?

### Common video benchmarks

| Benchmark | Probes | Why it exists |
|---|---|---|
| MSR-VTT / ActivityNet-QA | Open-ended captioning and QA | Classic general-purpose video QA |
| NExT-QA | Causal and temporal QA ("why", "before/after") | Forces reasoning beyond recognition |
| Charades-STA / ActivityNet-Captions | Temporal grounding and dense captioning | Localize events in time |
| Video-MME | Short/medium/long, with and without subtitles | Exposes the subtitle shortcut; tests length |
| TempCompass / Vinoground | Temporal-only skills; frame-order sensitivity | Built so single/shuffled frames fail |
| EgoSchema / LongVideoBench | Long-form understanding (minutes+) | Tests the long-video context wall |

Choose benchmarks that reflect your application's priorities.
