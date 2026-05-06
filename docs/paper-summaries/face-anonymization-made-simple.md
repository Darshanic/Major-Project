# Face Anonymization Made Simple

**Paper PDF in this repo:** [`Literature Survey/Face Anonymization Made Simple.pdf`](../../Literature%20Survey/Face%20Anonymization%20Made%20Simple.pdf)

---

## Citation

Han-Wei Kung, Tuomas Varanka, Sanjay Saha, Terence Sim, and Nicu Sebe. "Face Anonymization Made Simple." *arXiv preprint arXiv:2411.00762*, 1 Nov 2024.

---

## 1. Problem Addressed

Protecting people's identity in photos and videos is increasingly important due to privacy laws (e.g., GDPR) and the rise of powerful facial recognition systems. Traditional methods such as blurring and pixelation are vulnerable to reconstruction attacks and destroy useful visual information (expressions, gaze, background). More recent GAN-based methods either produce unnatural results or require extra input data (facial landmarks, masks) and rely on identity loss functions computed by face recognition models — which can themselves be inaccurate.

---

## 2. Key Idea / Method

The paper proposes a **diffusion-based face anonymization** approach that:

- Treats anonymization like a **face-swapping** task (replace the identity while keeping everything else intact).
- Uses **only a single reconstruction loss (MSE)**, removing the need for identity-loss terms derived from face recognition models (e.g., ArcFace).
- Requires **no facial landmarks or segmentation masks** — the full image is generated from scratch via a noise map.
- Offers a single tunable parameter **d** to control the degree of anonymization, and supports diverse results via different random seeds.
- Can optionally accept a second face image to perform **face swapping** (the same model serves both tasks).

---

## 3. Model Architecture / Pipeline

The architecture is built on a **Latent Diffusion Model (Stable Diffusion v2.1)** and consists of three main components:

| Component | Role |
|---|---|
| **Denoising UNet** | Generates the final output image |
| **Source ReferenceNet** | Encodes identity features from the source face |
| **Driving ReferenceNet** | Encodes non-identity features (pose, expression, background) from the driving face |

Each input image is encoded into latent space with a **CLIP image encoder** and passed to its ReferenceNet. Features are injected into the UNet via **self-attention concatenation** and **cross-attention** at every diffusion step.

For **anonymization**, the same image is fed to both ReferenceNets, but the intermediate embedding and ReferenceNet state are modified using the parameter `d`:

- `Z'_img = (1 - d) * Z_img` — scales down the identity embedding.  
- `S' = (1 - d) * S_cond + d * S_uncond` — blends conditional and unconditional states to move away from the original identity.

The model is trained with **classifier-free guidance**: 90% conditional (with source image) and 10% unconditional (without source image). A **curriculum learning** strategy is also used, starting with real and synthetic driving images before fine-tuning on real images only.

---

## 4. Datasets & Experimental Setup

| Dataset | Usage |
|---|---|
| **CelebRef-HQ** | Training |
| **CelebA-HQ** | Training + Evaluation (1,000 test images) |
| **FFHQ** | Training + Evaluation (1,000 test images) |

Training was run for **435,000 steps** on **two NVIDIA A6000 GPUs** at 512×512 resolution using the AdamW optimizer (lr=1e-5, batch size=1 with 8 gradient accumulation steps). Inference uses DDPM with 200 denoising steps and a guidance scale of 4.0.

---

## 5. Main Results and Comparisons

Baselines: **DP2**, **FALCO**, **RiDDLE** (anonymization) and **DiffSwap**, **BlendFace**, **InSwapper** (face swapping).

Metrics: Re-ID rate (↓ better), face shape distance (↑ better), pose/gaze/expression distance (↓ better), and Face IQA score (↑ better).

**Key findings (Table 1):**

- At **d = 1.4**, the model produces the most distinctly shaped faces and achieves the **best pose and gaze preservation** across both datasets.
- At **d = 1.2**, the model best preserves all three attributes (pose, gaze, expression) and still achieves competitive re-ID performance.
- Image quality ranks **second** (behind FALCO, which outputs at 1024×1024).
- The method **outperforms DP2** on every attribute metric and on image quality.

---

## 6. Limitations and Future Work

- **Re-ID rate** does not match FALCO or RiDDLE because they use explicit identity-loss terms; the proposed method relies purely on reconstruction loss.
- **Underrepresented groups** (infants, ethnic minorities) in training data lead to weaker anonymization performance for those subjects — the model shows bias correlated with training set demographics.
- **Resolution** is capped at 512×512 due to GPU memory constraints; larger diffusion models (e.g., SDXL) could improve quality but are not yet affordable at scale.
- Future work could address dataset diversity, higher-resolution generation, and video anonymization.

---

## 7. Practical Takeaways

1. **No landmarks or masks needed** — plug in any face image and get an anonymized result immediately.
2. **One parameter controls privacy vs. utility trade-off** — lower `d` preserves more facial attributes; higher `d` provides stronger anonymization.
3. **Use different seeds for diversity** — the same image can be anonymized into many distinct identities.
4. **Dual-mode versatility** — the same model weights support both anonymization (single image) and face swapping (two images), reducing engineering overhead.
5. **Open source** — code and models are publicly available at <https://github.com/hanweikung/face_anon_simple>.
6. **Watch for bias** — test your deployment on diverse demographics, as the model performs less reliably on underrepresented groups in the training data.
