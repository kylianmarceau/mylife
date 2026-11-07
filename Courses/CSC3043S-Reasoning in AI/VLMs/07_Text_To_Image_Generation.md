---
tags:
  - reasoning-in-ai
---

# Text-to-Image Generation

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture7_Text_to_Image_Generation.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture7_Text_to_Image_Generation.pdf), Prof Patrick Marais, slides 1-17 (primary papers: Rombach et al. 2022; Ho and Salimans 2022; Peebles and Xie 2023)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#The cost of diffusion in pixel space|The cost of diffusion in pixel space]]
  - [[#Latent diffusion|Latent diffusion]]
  - [[#The control problem: conditioning on text|The control problem: conditioning on text]]
  - [[#Text conditioning with cross-attention|Text conditioning with cross-attention]]
  - [[#Classifier-free guidance|Classifier-free guidance]]
  - [[#The Stable Diffusion pipeline|The Stable Diffusion pipeline]]
  - [[#Diffusion Transformers (DiT)|Diffusion Transformers (DiT)]]
  - [[#Evaluation: two separate questions|Evaluation: two separate questions]]
  - [[#FID|FID]]
  - [[#CLIPScore|CLIPScore]]

---

## Core Content

### The cost of diffusion in pixel space

Standard (DDPM) diffusion generates every pixel directly. For a $512 \times 512$ image:

$$
512 \times 512 \times 3 = 786{,}432 \text{ numbers per image, per denoising step}
$$

- The denoiser reads and rewrites all 786k numbers for each of its ~1000 timesteps, for every image generated.
- The cost is not amortized: training **and** inference both pay it repeatedly.
- Pixel-space diffusion works, but at scale it needs a cluster, not a laptop or single GPU.

Can the same diffusion process run more economically? Yes — in a low-dimensional latent space.

### Latent diffusion

#### Definitions

> **Latent diffusion**: Running the whole diffusion process (forward noising and reverse denoising) inside a VAE's compressed latent space, then decoding once at the end (Rombach et al., 2022).

![Latent diffusion](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/latent-cost.svg)

*A frozen VAE encodes $512 \times 512 \times 3$ pixels (786,432 numbers) into a $64 \times 64 \times 4$ latent (16,384), diffusion runs there, and the VAE decoder maps back.*

$$
\frac{512 \times 512 \times 3}{64 \times 64 \times 4} = \frac{786{,}432}{16{,}384} = 48\times \text{ fewer numbers}
$$

- The VAE encoder/decoder is **trained once, separately, then frozen**. It handles accurate, efficient encoding of image characteristics (perception); diffusion handles generation.
- **Inference**: choose a random seed in latent space, run denoising there, and decode the final latent to an image with the VAE decoder.

This is cheap and the basis of **Stable Diffusion**.

### The control problem: conditioning on text

The diffusion denoiser maps (noisy latent, timestep) → predicted noise. There is **no text anywhere**, so it can only produce *some* plausible image, never one dictated by a prompt.

The prompt must condition **every** one of the ~50 denoising steps, not just influence the start. Two sub-problems:

1. **Encode the words**: use CLIP's text encoder, which already maps prompts into a space aligned with image content. Use **all** CLIP text tokens (usually 77), not just the pooled output.
2. **Condition the denoiser**: use cross-attention, with the latent supplying queries and the text supplying keys and values.

### Text conditioning with cross-attention

![Text conditioning](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/cross-attention-conditioning.svg)

*Prompt tokens from the CLIP text encoder supply keys and values; noisy-latent patches supply queries; cross-attention appears at many layers at every step.*

$$
Q = \text{latent features} \cdot W^Q, \qquad K = \text{text tokens} \cdot W^K, \qquad V = \text{text tokens} \cdot W^V
$$

$$
\text{CrossAttn}(Q, K, V) = \text{softmax}\!\left(\frac{QK^\top}{\sqrt{d_k}}\right) V
$$

- Each patch of the noisy latent "asks" the prompt what it should depict.
- Cross-attention is injected at **many layers** of the denoiser, at **every step**, so guidance persists throughout denoising.

### Classifier-free guidance

#### Definitions

> **Classifier-free guidance (CFG)**: Steering generation by extrapolating from the model's unconditioned noise prediction towards its prompt-conditioned prediction, controlled by a guidance scale (Ho and Salimans, 2022).

> **Guidance scale $w$**: How strongly to follow the direction the prompt pulls the image.

$$
\hat{\epsilon} = \epsilon_\theta(z_t, t, \varnothing) + w \cdot \big[\epsilon_\theta(z_t, t, c) - \epsilon_\theta(z_t, t, \varnothing)\big]
$$

The bracket is **"what the prompt changed"**; the scale amplifies it. The result is a modified noise prediction, which is then subtracted from the current latent to get a less noisy latent.

![Classifier-free guidance](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/cfg.svg)

*The guided prediction starts at the unconditional prediction and moves $w$ times along the direction the prompt pulls it.*

| Scale | Effect |
|---|---|
| $w = 0$ | Prompt ignored (unconditional) |
| $w = 1$ | Ordinary conditioning |
| $w = 7.5$ | Follow the prompt direction $7.5\times$ as hard (Stable Diffusion default) |
| Well above typical range | Over-saturation and artifacts |

Example: "An oil painting of a collie in a top hat" with the same model, prompt, and seed. As the scale rises, prompt adherence improves, but contrast increases too.

- **Why "classifier-free"**: earlier methods steered with a separate image classifier; CFG uses only the model's own with/without-prompt predictions.
- **Cost**: two denoiser passes per step, roughly doubling generation time. A very common, worthwhile trade.
- **Training**: the prompt is randomly dropped during training, so one model learns both the conditioned and unconditioned predictions.

### The Stable Diffusion pipeline

![Stable Diffusion pipeline](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/stable-diffusion.svg)

*The prompt is encoded by CLIP; random latent noise is denoised by a guided U-Net or DiT for $T$ steps; the VAE decoder makes the image.*

1. **Encode the prompt** with the CLIP text encoder into token embeddings.
2. **Sample** a random latent $z_T$ (e.g. $64 \times 64 \times 4$).
3. **For each step** $t = T, \dots, 1$:
   1. Predict the noise with and without the prompt (cross-attention to text tokens).
   2. Combine them with classifier-free guidance.
   3. The **scheduler** uses the guided prediction to compute a less noisy latent $z_{t-1}$.
4. **Decode** the final latent $z_0$ with the VAE decoder into pixels.

### Diffusion Transformers (DiT)

#### Definitions

> **U-Net**: The convolutional encoder-decoder architecture used as the denoiser in the original Stable Diffusion.

> **Diffusion Transformer (DiT)**: A denoiser that cuts the latent into patches like a ViT and uses a Transformer to predict the noise over those patch tokens (Peebles and Xie, 2023).

![Diffusion Transformer](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/dit.svg)

*DiT patchifies the noisy latent like a ViT and uses Transformer blocks to predict the noise.*

| | U-Net denoiser | DiT denoiser |
|---|---|---|
| Architecture | Convolutional | Transformer over latent patch tokens (ViT-style tokenization) |
| Text conditioning | Cross-attention | Cross-attention or conditioning tokens |
| Guidance | CFG | Unchanged |
| Scaling | Works well | Scales better with data and compute |

DiTs are behind most current top-tier image and video generators — the ViT from lecture 1, now used for generation.

### Evaluation: two separate questions

A good generation must be both **realistic** and **faithful to the prompt**. These fail independently: an amazing photo of the wrong thing, or an on-prompt but ugly mess. So they are measured separately.

| Question | Metric |
|---|---|
| Is it realistic? | FID |
| Does it match the prompt? | CLIPScore |

### FID

#### Definitions

> **Fréchet Inception Distance (FID)**: The distance between the feature distributions of real and generated images, as seen by a pretrained Inception network (Heusel et al., 2017). Lower is better.

1. Extract Inception features for a set of real images and a set of generated images.
2. Fit a Gaussian (mean and covariance) to each set.
3. Measure the distance between the two Gaussians.

The standard Fréchet distance between the fitted Gaussians $(\mu_r, \Sigma_r)$ and $(\mu_g, \Sigma_g)$ is:

$$
\text{FID} = \|\mu_r - \mu_g\|^2 + \text{Tr}\!\left(\Sigma_r + \Sigma_g - 2\big(\Sigma_r \Sigma_g\big)^{1/2}\right)
$$

![FID and CLIPScore](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/07_Text_To_Image_Generation/fid-clipscore.svg)

*FID compares the feature distributions of real and generated sets; CLIPScore checks each image against its prompt (0.82 on-prompt vs 0.24 off-prompt).*

| Measures | Does not measure | Limits |
|---|---|---|
| Realism and diversity of the generated **set** | Whether any single image matches the prompt; a model can have excellent FID while ignoring prompts | Needs a fairly large sample; sensitive to the reference set |

### CLIPScore

#### Definitions

> **CLIPScore**: The cosine similarity between CLIP embeddings of the generated image and its prompt (Hessel et al., 2021).

$$
\text{CLIPScore}(I, c) \propto \cos\big(E_{\text{img}}(I), E_{\text{txt}}(c)\big)
$$

A high value means image and text sit close together in CLIP's shared space, so the image is on-prompt. It is the same similarity used for zero-shot classification, pointed at generation.

> [!warning] <span style="color: #ff939b">Use both metrics</span>
> A model can have good FID while ignoring the prompt (realistic but wrong), or good CLIPScore while producing a garbled mess that contains the right concepts. They catch different failures. Neither replaces a human judging the image; they are cheap automatic proxies used at scale during development.
