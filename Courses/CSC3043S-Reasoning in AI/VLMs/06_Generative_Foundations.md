---
tags:
  - reasoning-in-ai
---

# Generative Foundations: VAEs, GANs, and Diffusion

> [!abstract] <span style="color: #b89aff">Lecture reference</span>
> **Subject**: CSC3043S Reasoning in AI: Vision-Language Models  
> **Source**: [Lecture6_Generative_Foundations.pdf](../../../Sources/CSC3043S%20-%20Reasoning%20in%20AI/VLM%27s/Lecture6_Generative_Foundations.pdf), Prof Patrick Marais, slides 1-25 (primary papers: Kingma and Welling 2014; Goodfellow et al. 2014; Ho et al. 2020)  
> **Generated**: 2026-10-29  

---

## Contents

- [[#Core Content|Core Content]]
  - [[#From understanding to generating|From understanding to generating]]
  - [[#Recap: the autoencoder|Recap: the autoencoder]]
  - [[#Why a plain autoencoder cannot generate|Why a plain autoencoder cannot generate]]
  - [[#Variational autoencoders|Variational autoencoders]]
  - [[#The reparameterization trick|The reparameterization trick]]
  - [[#KL divergence|KL divergence]]
  - [[#The VAE objective|The VAE objective]]
  - [[#VAE strengths and weaknesses|VAE strengths and weaknesses]]
  - [[#GANs: a forger versus a detective|GANs: a forger versus a detective]]
  - [[#The GAN objective|The GAN objective]]
  - [[#GAN strengths and weaknesses|GAN strengths and weaknesses]]
  - [[#Diffusion: the core idea|Diffusion: the core idea]]
  - [[#Why many small steps|Why many small steps]]
  - [[#Training: predict the noise|Training: predict the noise]]
  - [[#The noise schedule and ᾱₜ|The noise schedule and ᾱₜ]]
  - [[#The diffusion loss|The diffusion loss]]
  - [[#Generating an image step by step|Generating an image step by step]]
  - [[#Comparison of image generators|Comparison of image generators]]

---

## Core Content

### From understanding to generating

Everything so far was **understanding**: image/video in → text out (describe, answer, ground, locate). Now the direction flips: something in → a **new image** out.

#### Definitions

> **Generation**: Producing new samples that look as if they came from the training distribution, rather than copying training images (which is memorization).

Example: train on 10,000 face photos and produce a realistic face of someone who never existed.

The core question: how do you learn the "look" (distribution) of a whole category of images well enough to synthesize convincing new members?

The lecture has three parts: autoencoders → VAEs (make the latent space sampleable); GANs (learn to generate by competition); diffusion (add noise, then learn to remove it).

### Recap: the autoencoder

#### Definitions

> **Autoencoder (AE)**: An encoder that maps input $x$ to a small latent code $z$, and a decoder that maps $z$ back to a reconstruction $\hat{x} \approx x$.

> **Bottleneck**: The small latent code, which forces the network to keep only what matters.

![Autoencoder](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/autoencoder.svg)

*An image is compressed to a small latent code $z$ and decoded back to $\hat{x} \approx x$.*

The AE is self-supervised. Its loss is reconstruction error, e.g. mean-squared error:

$$
\mathcal{L}_{\text{AE}} = \|x - \hat{x}\|^2
$$

### Why a plain autoencoder cannot generate

In theory, pick a random $z$ and decode it. In practice this **fails**:

- The AE only learned to decode the specific codes its training images mapped to.
- The space between and around those codes was never trained. If $(1, 1)$ and $(10, 10)$ are encoded training examples, what does $(5, 5)$ decode to?
- So a random $z$ usually decodes to noise or garbage.

![Latent gaps](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/latent-gaps.svg)

*Plain autoencoder codes are scattered with gaps, so a random code decodes to garbage; VAE codes fill a region around $\mathcal{N}(0, I)$ that is safe to sample.*

### Variational autoencoders

#### Definitions

> **Variational autoencoder (VAE)**: An autoencoder whose encoder outputs a probability distribution over codes rather than a single code, regularized towards a fixed prior so the latent space can be sampled (Kingma and Welling, 2014).

> **Approximate posterior $q(z \mid x)$**: The encoder's Gaussian $\mathcal{N}(\mu(x), \sigma(x)^2 I)$ — given this image, where could its code plausibly lie?

> **Prior $p(z)$**: The fixed target distribution $\mathcal{N}(0, I)$ shared by every image.

1. For each image $x$, the encoder predicts a mean $\mu(x)$ and standard deviation $\sigma(x)$, defining $q(z \mid x) = \mathcal{N}(\mu, \sigma^2 I)$.
2. During training, sample $z \sim q(z \mid x)$ and decode it. The decoder must handle a **region** of latent space, not an isolated point.
3. Pull every posterior towards the same prior $p(z) = \mathcal{N}(0, I)$. The posteriors then overlap and together cover the region sampled later. Without this pull, the encoder could place posteriors anywhere and the gaps return.

![Variational autoencoder](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/vae.svg)

*The encoder outputs $\mu$ and $\sigma$ defining $q(z \mid x)$; a sample is decoded; the KL term pulls $q$ towards the prior.*

**Generation** is cheap: keep only the decoder, draw $z \sim \mathcal{N}(0, I)$, and decode it into a new image.

### The reparameterization trick

**Problem**: training needs $\partial \mathcal{L}/\partial \mu$ and $\partial \mathcal{L}/\partial \sigma$, but "draw a random sample" is not differentiable. With sampling inside the network, no gradient reaches the encoder.

**Fix**: sample parameter-free noise and build $z$ from it.

$$
\epsilon \sim \mathcal{N}(0, I), \qquad z = \mu + \sigma \odot \epsilon
$$

The distribution of $z$ is unchanged, but $z$ is now a differentiable function of $\mu$ and $\sigma$, so gradients flow to the encoder. This makes the VAE trainable end-to-end.

![Reparameterization trick](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/reparameterization.svg)

*Sampling inside the network blocks gradients; drawing $\epsilon$ from outside and setting $z = \mu + \sigma \odot \epsilon$ lets gradients reach the encoder.*

### KL divergence

#### Definitions

> **KL divergence $\text{KL}(q \,\|\, p)$**: A measure of the gap between a distribution $q$ and a reference $p$. It is never negative, is zero only when $q = p$, and is **not symmetric**.

Here we always measure the encoder's posterior against the prior. Per latent dimension, for $q = \mathcal{N}(\mu, \sigma^2)$ and $p = \mathcal{N}(0, 1)$:

$$
\text{KL} = \tfrac{1}{2}\left(\mu^2 + \sigma^2 - 1 - \ln \sigma^2\right)
$$

| Term | Penalizes |
|---|---|
| $\mu^2$ | Being off-centre |
| $\sigma^2 - 1 - \ln \sigma^2$ | Being too wide or too narrow; zero exactly at $\sigma = 1$ |

![Gaussian KL](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/gaussian-kl.svg)

*A matched posterior has KL $0.02$; a shifted mean gives $2.43$; a posterior that is too wide gives $1.51$.*

The KL term is the **only** thing tying each image's posterior to the distribution sampled at generation time.

### The VAE objective

#### Definitions

> **ELBO (evidence lower bound)**: A lower bound on the data log-likelihood. The VAE loss is the negative ELBO; maximizing the ELBO and minimizing the negative ELBO are the same.

> **Posterior collapse**: When $q(z \mid x) = \mathcal{N}(0, I)$ for every image, so the code carries no information about $x$.

$$
\mathcal{L}_{\text{VAE}} = \underbrace{\mathbb{E}_{q(z \mid x)}\big[\text{reconstruction error}\big]}_{\text{rebuild } x \text{ from a sampled code}} + \underbrace{\text{KL}\big(q(z \mid x) \,\|\, p(z)\big)}_{\text{keep the posterior near the prior}}
$$

- For images, the reconstruction term usually reduces to a simple MSE between generated and input images.
- **β-VAE** weights the KL term by $\beta$ for more control.

The two terms pull in opposite directions:

| Regime | Result |
|---|---|
| Reconstruction only | $\sigma \rightarrow 0$ and posteriors drift apart: back to a plain AE with gaps |
| KL only | Posterior collapse: perfect prior match, useless reconstruction |
| Balanced | Posteriors close enough to the prior to sample from, distinct enough to rebuild each image |

### VAE strengths and weaknesses

A VAE is an autoencoder whose encoder outputs a distribution, regularized so the posteriors together match a sampleable prior.

| Strengths | Weakness |
|---|---|
| Stable, simple training (one network pair, one clear objective) | Samples tend to be **blurry**: the reconstruction term averages over everything the posterior could encode, smoothing fine detail |
| Smooth, structured latent space; nearby codes decode to similar images, enabling interpolation and editing | |

VAEs rarely generate final images today, but the **VAE encoder is a core part of Stable Diffusion**, compressing images so diffusion runs cheaply.

### GANs: a forger versus a detective

#### Definitions

> **Generative adversarial network (GAN)**: Two networks trained together with opposing objectives — a generator and a discriminator (Goodfellow et al., 2014).

> **Generator $G$**: Takes random noise $z$ and tries to produce a realistic fake image (the forger).

> **Discriminator $D$**: Takes one image and outputs the probability that it is real rather than generated (the detective).

![GAN](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/gan.svg)

*The generator turns noise into a fake image; the discriminator judges real versus fake, and its feedback trains both.*

- Noise is the seed for **diversity**; a fixed input would always map to the same output.
- The discriminator is trained to catch fakes; the generator is trained to fool it. As one improves, the other must too — an **arms race**.
- At the end, keep only the generator.

### The GAN objective

$$
\min_G \max_D \; \mathbb{E}_{x \sim p_{\text{data}}}\big[\log D(x)\big] + \mathbb{E}_{z \sim p(z)}\big[\log\big(1 - D(G(z))\big)\big]
$$

- $D$ is trained to **maximize** its output on real data (and minimize it on fakes).
- $G$ is simultaneously trained to **minimize** $\log(1 - D(G(z)))$.
- This is a two-player **minimax** game, a well-studied optimization problem.

Intuition:

1. The discriminator sees a real photo and says 0.9 "real" (correct), then sees a fake and says 0.8 "real" (fooled). It adjusts to score that fake lower.
2. The generator is told "the discriminator still flagged 30% of your fakes" and adjusts to push those towards "real".
3. Repeat millions of times until fakes are indistinguishable from real.

Why training is notoriously hard:

- It is a **moving target**: both networks change at once (in practice they often alternate).
- If the discriminator gets too good too fast, the generator gets no useful signal ("you're always wrong" teaches nothing).
- Balancing them is the whole art; failures include **mode collapse** and instability.

### GAN strengths and weaknesses

| Strengths | Weaknesses |
|---|---|
| **Sharp**, detailed images — competition rewards crisp detail, no blurry averaging | Unstable, finicky training |
| **Fast** sampling: one generator forward pass per image | **Mode collapse**: producing only a few kinds of image |
| | No well-structured latent space or likelihood; harder to control and evaluate |

GANs dominated image generation around 2016-2021, with many variants (conditional GANs, CycleGAN, style control). Diffusion then matched their sharpness with far more stable training and greater diversity. GANs are still used for fast generation, and the discriminator idea appears in other networks.

### Diffusion: the core idea

#### Definitions

> **Diffusion model**: A generator that learns to reverse a fixed process which gradually adds noise to images (Ho et al., 2020, DDPM).

> **Forward process**: Repeatedly add a little random noise to a real image until only noise remains. It is fixed — no learning.

> **Reverse process**: A trained network that undoes one noise step, run many times starting from pure noise.

![Diffusion forward and reverse](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/diffusion-forward-reverse.svg)

*The fixed forward process adds noise until only noise remains; the learned reverse process removes it step by step to produce a new image.*

### Why many small steps

- Generating a whole image from pure noise in one shot is extremely hard; that is essentially the GAN's difficulty.
- Diffusion solves a small, easy problem instead: "this image is slightly noisy; make it slightly less noisy".
- Each denoising step is a small, well-behaved **regression** the network can learn reliably.
- Chaining hundreds of easy steps accomplishes what one giant leap cannot.

Analogy: you cannot sculpt a statue in one strike, but you can remove one chip at a time.

"Many easy steps beat one hard step" is why diffusion trains stably where GANs struggle, and why its images are both sharp and diverse.

### Training: predict the noise

The network is **never asked to make an image**. It is asked to guess the noise that was added — a plain regression.

1. Take a clean image $x_0$.
2. Pick a random step $t$ and random noise $\epsilon \sim \mathcal{N}(0, I)$.
3. Construct the noisy image directly with the fixed schedule:

$$
x_t = \sqrt{\bar{\alpha}_t}\,x_0 + \sqrt{1 - \bar{\alpha}_t}\,\epsilon
$$

4. The network predicts the noise: $\hat{\epsilon} = \epsilon_\theta(x_t, t)$.
5. Loss $= \|\epsilon - \hat{\epsilon}\|^2$; backpropagate to update $\theta$.

![Diffusion training](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/noise-prediction.svg)

*Pick a clean image, a random step and noise, build $x_t$ directly, predict the noise, and minimize the squared error.*

No likelihood, no adversary — one clean regression.

### The noise schedule and ᾱₜ

#### Definitions

> **$\bar{\alpha}_t$ ("alpha-bar at step $t$")**: A number between 0 and 1 giving how much of the clean image survives at step $t$. It is the cumulative product of a **fixed noise schedule** chosen in advance; the network never learns it.

- $\bar{\alpha}_t \approx 1$ early (mostly clean image); $\bar{\alpha}_t \approx 0$ late (almost pure noise).
- So $\sqrt{\bar{\alpha}_t}\,x_0$ fades out while $\sqrt{1 - \bar{\alpha}_t}\,\epsilon$ fades in, smoothly turning an image into noise.

![Noise schedule](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/alpha-bar.svg)

*$\bar{\alpha}_t$ falls from 1 to 0 while $1 - \bar{\alpha}_t$ rises, so $x_t$ turns smoothly from image into noise.*

### The diffusion loss

$$
\mathcal{L} = \big\|\,\epsilon - \epsilon_\theta(x_t, t)\,\big\|^2
$$

| Symbol | Meaning |
|---|---|
| $\epsilon$ | The random noise added to the clean image; known exactly because we chose it |
| $x_t$ | The noisy image at step $t$, built with $\bar{\alpha}_t$; the network's input |
| $\epsilon_\theta(x_t, t)$ | The network's noise prediction given the noisy image and step $t$ ($\theta$ = weights) |
| $\|\cdot\|^2$ | Squared difference: standard regression error |

| Model | What its loss asks |
|---|---|
| VAE | Reconstruct accurately **and** keep the latent space sampleable |
| GAN | Fool an adversary — a complicated, often unstable moving target |
| Diffusion | Predict the noise — a simple regression |

### Generating an image step by step

1. Start from pure random noise (like the VAE, generation begins with noise).
2. Ask the network "what noise is in this?" and subtract a bit of it → a slightly cleaner image.
3. Repeat 50-1000 times → a fully formed, novel image emerges.

![Sampling loop](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/sampling-loop.svg)

*Start from pure noise, predict the noise, subtract a little, and repeat many times.*

| Pros | Cons |
|---|---|
| Excellent quality and diversity — why diffusion won | **Slow**: VAEs and GANs need one pass; diffusion needs many. Fast samplers (e.g. DDIM) cut 1000 steps to about 4 |

For high-resolution images, pixel-space diffusion is too expensive. Running diffusion in a VAE's compressed latent space gives **Stable Diffusion** (next lecture).

### Comparison of image generators

| | VAE | GAN | Diffusion |
|---|---|---|---|
| Machinery | Encoder → $z \sim \mathcal{N}(\mu, \sigma)$ → decoder → $\hat{x}$ | Generator: noise → $\hat{x}$; discriminator: real or fake? | Add noise (fixed); network removes noise, $\times T$ |
| Loss | Reconstruct + KL | The two networks compete | Predict the noise (MSE) |
| Training | One network pair, stable | Tricky | Stable |
| Samples | Smooth latent, blurry images | Sharp, one-pass | Best quality and diversity, slow |

Many GAN variants exist, but all suffer from diversity or stability issues. Diffusion is now the dominant image-generation approach, and the basis of every modern generator: it turned a very complex problem into many easy steps.

![Generator comparison](../../../diagrams/CSC3043S-Reasoning%20in%20AI/VLMs/06_Generative_Foundations/generator-comparison.svg)

*VAE, GAN, and diffusion side by side: their machinery, losses, and characteristic strengths.*
