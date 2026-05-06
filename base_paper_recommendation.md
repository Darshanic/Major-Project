# Base Paper Recommendation

## Recommended Base Paper

**Face Anonymization Made Simple** is the best base paper for the project if you want the newest and most relevant reference.

Reason: your project should now prioritize papers published after 2021, and this paper is the latest direct anonymization reference in the set. It aligns better with the privacy-anonymization goal than detector-only or OCR-only papers, while still keeping the older papers as supporting background.

## Ranked Papers

| Rank | Paper                                                                           | Year | Role in Project                  | Why Keep It                                                                                  |
| ---- | ------------------------------------------------------------------------------- | ---- | -------------------------------- | -------------------------------------------------------------------------------------------- |
| 1    | Face Anonymization Made Simple                                                  | 2025 | Base paper                       | Latest direct anonymization paper and the closest fit to the updated priority rule           |
| 2    | G2Face: High-Fidelity Reversible Face Anonymization                             | 2024 | Strong modern base               | Very relevant for realistic privacy-preserving face replacement                              |
| 3    | Ultralytics YOLOv8: Real-Time Object Detection, Segmentation and Classification | 2023 | Core detector reference          | Best recent backbone for real-time detection                                                 |
| 4    | DeepPrivacy2: Towards Realistic Full-Body Anonymization                         | 2023 | Advanced anonymization reference | Strong privacy paper with full-body anonymization                                            |
| 5    | YOLO5Face: Why Reinventing a Face Detector                                      | 2021 | Face detection variant           | Good recent face detector for privacy systems                                                |
| 6    | Large-Scale Privacy Protection in Google Street View                            | 2009 | Historical base                  | Still important as the classic privacy foundation, but lower priority because it is pre-2021 |
| 7    | You Only Look Once: Unified, Real-Time Object Detection                         | 2016 | Core detector reference          | Still useful, but older than YOLOv8                                                          |
| 8    | Joint Face Detection and Alignment Using MTCNN                                  | 2016 | Face detection support           | Useful secondary face detector                                                               |
| 9    | Character Region Awareness (CRAFT)                                              | 2019 | Text detection support           | Strong for scene text and stylized text privacy                                              |
| 10   | EAST: An Efficient and Accurate Scene Text Detector                             | 2017 | Text detection alternative       | Good companion or alternative to CRAFT                                                       |
| 11   | An Overview of the Tesseract OCR Engine                                         | 2007 | OCR baseline                     | Good OCR reference for readable text extraction                                              |
| 12   | CIAGAN: Conditional Identity Anonymization GANs                                 | 2020 | GAN anonymization reference      | Useful, but narrower than the newer anonymization papers                                     |
| 13   | End-to-End Car License Plate Detection and Recognition                          | 2018 | Plate privacy reference          | Good for license plate privacy, but domain-specific                                          |
| 14   | MobileNets: Efficient CNNs for Mobile Vision                                    | 2017 | Deployment reference             | Useful if you emphasize edge/mobile execution                                                |
| 15   | Rapid Object Detection Using a Boosted Cascade of Simple Features               | 2001 | Background only                  | Historical value, but outdated for the project                                               |
| 16   | Why Should I Read the Privacy Policy, I Just Need the Service                   | 2021 | Background only                  | Privacy attitude study, not image anonymization                                              |

## Final Recommendation

Use **Face Anonymization Made Simple** as the base paper if you want the latest publication to lead the project, then build around:

- **YOLOv8** for real-time sensitive object detection
- **MTCNN** as a secondary face detector
- **CRAFT + OCR** for text and PII detection
- **DeepPrivacy2 / G2Face** as the anonymization comparison papers

That combination matches the updated project direction: recent privacy-aware anonymization, context-aware selective anonymization, privacy-risk scoring, and local privacy-first processing.

## Why This Base Paper

I chose **Face Anonymization Made Simple** as the base paper because it is the most recent paper in the set that directly targets face anonymization, which is the core privacy problem in this project. It is a better starting point than pure detector papers because it focuses on the final privacy outcome, not only on finding objects.

It ranks above the older papers for four reasons:

- It is published in 2025, so it satisfies your request to prioritize papers after 2021.
- It is directly about anonymization, while many other papers are only about detection, OCR, or general vision.
- It matches the project’s aim of privacy-preserving output, not just sensitive object localization.
- It is closer to a modern privacy pipeline than older blur-based or detector-only approaches.

## Ranking Logic

The ranking is not only based on year. It also considers how closely each paper matches the project goal.

- Papers that are both recent and privacy-anonymization focused rank highest.
- Papers that support the pipeline, such as YOLOv8, G2Face, DeepPrivacy2, and YOLO5Face, come next.
- Older papers like MTCNN, CRAFT, EAST, Tesseract, and Faster R-CNN stay in the list because they are still useful building blocks, but they are not the strongest base references under your updated priority rule.
- Very old background papers remain only for historical context and literature completeness.

## Why Each Paper Is Ranked There

### 1. Face Anonymization Made Simple (2025)

This is ranked first because it is the latest direct anonymization paper in your set. It is different from detector papers because it actually focuses on changing identity while keeping the image usable. That makes it the closest conceptual match to the full project.

### 2. G2Face: High-Fidelity Reversible Face Anonymization (2024)

This ranks second because it is also a modern anonymization paper and is very close to the privacy goal. It is slightly below the first paper because it is more specialized around reversible face anonymization, while the first paper is a simpler lead reference for framing the project.

### 3. Ultralytics YOLOv8: Real-Time Object Detection, Segmentation and Classification (2023)

This ranks third because it is one of the best recent general detection backbones. It is not a base paper for anonymization, but it is highly relevant for detecting faces, plates, documents, and text regions before anonymization.

### 4. DeepPrivacy2: Towards Realistic Full-Body Anonymization (2023)

This is ranked just below YOLOv8 because it is a strong anonymization method, but it is heavier and more specialized. It differs from the top two papers by focusing on realistic synthesis instead of being the broadest project anchor.

### 5. YOLO5Face: Why Reinventing a Face Detector (2021)

This is the strongest 2021-era support paper in your set. It ranks above older detectors because it is more recent and more privacy-relevant than generic face detection methods. It is still below the top anonymization papers because it only detects faces.

### 6. Large-Scale Privacy Protection in Google Street View (2009)

This remains important because it is the classic privacy-protection paper and directly shows the privacy problem. It ranks lower only because it is much older and uses an outdated style of solution compared to the newer anonymization papers.

### 7. You Only Look Once: Unified, Real-Time Object Detection (2016)

This is still a key reference for real-time object detection, but it ranks below YOLOv8 because YOLOv8 is newer and more aligned with current implementation practice. YOLO is more of a foundational detector reference than a current best choice.

### 8. Joint Face Detection and Alignment Using MTCNN (2016)

This ranks as a support paper because it is useful for face detection in difficult scenes. It is below YOLO-based methods because it is older and only covers the face-detection stage.

### 9. Character Region Awareness (CRAFT) (2019)

This ranks high among OCR/text papers because it is strong for stylized and curved scene text, which is important for social media privacy. It differs from Tesseract because it is better at scene text, not just printed text.

### 10. EAST: An Efficient and Accurate Scene Text Detector (2017)

This is a good text detector, but it ranks below CRAFT because CRAFT is usually stronger for arbitrary text shapes. It is still useful as a comparison or fallback detector.

### 11. An Overview of the Tesseract OCR Engine (2007)

This stays in the list because it is a standard OCR reference, but it is lower because it is older and less reliable on stylized social-media text. It is better for baseline OCR than for the project’s hardest cases.

### 12. CIAGAN: Conditional Identity Anonymization GANs (2020)

This is a useful anonymization reference, but it ranks below the newer 2023 to 2025 papers because it is older and narrower. It is still relevant for identity replacement ideas.

### 13. End-to-End Car License Plate Detection and Recognition (2018)

This is included because license plate privacy is part of the project. It ranks lower because it is domain-specific and does not cover the broader privacy pipeline.

### 14. MobileNets: Efficient CNNs for Mobile Vision (2017)

This is a deployment-oriented paper, not a privacy paper. It ranks here because it can support local and lightweight inference, but it does not directly solve the anonymization problem.

### 15. Rapid Object Detection Using a Boosted Cascade of Simple Features (2001)

This is only a background paper. It is historically important, but it is far behind modern detectors and is not a strong choice for the current project.

### 16. Why Should I Read the Privacy Policy, I Just Need the Service (2021)

This is included for privacy context, not image anonymization. It ranks last because it discusses privacy behavior rather than technical privacy protection for images.

## Short Comparison Summary

- The top papers are recent and directly relevant to anonymization.
- The middle papers are supporting methods for detection, OCR, or implementation.
- The bottom papers are included for completeness and background only.

So the base-paper choice is not just about being the newest paper. It is about being the newest paper that also matches the project’s core output: privacy-preserving anonymization with practical detection support.

## Paper Descriptions

### 1. Face Anonymization Made Simple (2025)

This paper is the strongest fit for the project because it directly focuses on face anonymization, which is the privacy outcome your system must deliver. Many other papers in the list stop at detection, but this one is concerned with the actual transformation of identity. That difference matters because your project is not just about identifying sensitive objects; it is about protecting privacy while keeping the image usable. This paper is also the newest in the set, so it matches your priority rule of favoring post-2021 research. It is ranked first because it gives the cleanest conceptual anchor for the whole system. Compared with older blur-based approaches, it reflects a more modern privacy mindset where the result should still look natural and socially shareable.

### 2. G2Face: High-Fidelity Reversible Face Anonymization (2024)

G2Face is ranked just below the base paper because it is also highly aligned with face privacy, but it is more specialized. Its key strength is that it focuses on reversible anonymization, which is useful when authorized access is needed later. That makes it different from simple blur or pixelation methods, which destroy identity but also destroy image quality. For your project, G2Face is valuable as a high-end comparison point because it shows what realistic anonymization can look like when privacy and visual fidelity are both important. It ranks above general detection papers because it speaks directly to the privacy goal, but it stays below the base paper because the project needs a broader framing paper rather than only a sophisticated face-replacement method.

### 3. Ultralytics YOLOv8: Real-Time Object Detection, Segmentation and Classification (2023)

YOLOv8 is ranked high because your system needs a modern detector that can work in real time. Unlike anonymization papers, it does not solve privacy by itself, but it is central to finding the faces, plates, documents, and text regions that must be protected. The reason it ranks above older detectors is that it is newer, lighter to deploy, and more practical for current implementations. It differs from YOLO and Faster R-CNN in that it reflects a newer generation of object detection with better engineering convenience. This makes it a strong pipeline paper, even though it is not the base paper. It belongs near the top because the privacy pipeline cannot work unless the detection stage is fast and reliable.

### 4. DeepPrivacy2: Towards Realistic Full-Body Anonymization (2023)

DeepPrivacy2 is important because it expands privacy beyond the face region and shows how full-body anonymization can be done realistically. That makes it more advanced than simple detectors and more privacy-focused than generic detection models. It ranks below YOLOv8 because its main value is in the anonymization stage rather than the detection stage, and it is more computationally demanding. What makes it different from the base paper is its emphasis on realistic synthesis across larger human regions. For your project, it is useful as a model for how anonymized output can remain visually acceptable, especially if the system ever needs to handle people standing in public scenes rather than only portraits.

### 5. YOLO5Face: Why Reinventing a Face Detector (2021)

YOLO5Face is a useful bridge paper because it sits between older face detectors and newer YOLO-based implementations. It is ranked higher than classic methods because it is more recent and more aligned with the project’s real-time requirements. It differs from MTCNN and Haar cascade approaches by being more in line with modern detection pipelines and by targeting the face-detection problem in a lightweight manner. This paper is not a privacy method by itself, so it cannot serve as the base paper, but it is very relevant for the detection stage. It is especially useful when the system has to detect small or multi-scale faces in social-media images where the subject may not be centered or clearly visible.

### 6. Large-Scale Privacy Protection in Google Street View (2009)

This paper is still essential because it is one of the earliest and most recognizable privacy-protection works. It directly addresses the practical problem of detecting faces and license plates for anonymization, so it remains a strong historical foundation. It ranks lower only because the project now prioritizes papers after 2021, and this work uses an older style of pipeline compared with more recent anonymization research. Its difference from the newer papers is that it is more of a classical privacy-protection system than a modern generative anonymization solution. Even so, it is valuable for showing how the field began and why simple blanket blurring became a problem. In your final report, it is best treated as the foundational historical reference rather than the core modern base.

### 7. You Only Look Once: Unified, Real-Time Object Detection (2016)

YOLO is a foundational paper that still matters because many newer detectors build on its ideas. It ranks below YOLOv8 because the newer version is more practical for present-day deployment, but YOLO remains important as the original real-time object detection reference. It differs from anonymization papers because it only predicts objects and bounding boxes; it does not decide how privacy should be preserved. For your project, its role is to support fast detection of privacy-sensitive regions. It stays in the ranking because every later detection paper must be understood against the backdrop of YOLO’s one-stage detection idea. It is a strong supporting reference, but not the main privacy anchor.

### 8. Joint Face Detection and Alignment Using MTCNN (2016)

MTCNN is still widely respected because it handles face detection and alignment together, which can be helpful in difficult or angled images. It ranks below YOLO-based methods because it is older and narrower, but it remains very useful as a second detector for face recall. Its difference from YOLOv8 is that it is more specialized for faces, while YOLOv8 covers a wider detection set. That specialization makes MTCNN valuable in a privacy pipeline where faces need to be found reliably, even when lighting or pose is difficult. It is not a base paper because it stops at detection and alignment, but it is strong supporting evidence for a hybrid detector strategy.

### 9. Character Region Awareness (CRAFT) (2019)

CRAFT is ranked high among the text papers because it solves a problem that ordinary OCR methods often miss: text with unusual shapes, curved layouts, stylized fonts, and complex backgrounds. That makes it particularly relevant for social-media images where sensitive information may appear on signs, clothing, posters, and packaging. It differs from Tesseract because it is focused on locating text regions in the scene, not just reading clean printed words. It also differs from EAST by being especially strong for arbitrary-shaped text. In your project, CRAFT is important because text privacy is not a side issue; it is one of the most common sources of accidental data leakage. That is why it ranks above older OCR baselines.

### 10. EAST: An Efficient and Accurate Scene Text Detector (2017)

EAST is another valuable scene-text detector, and it ranks close to CRAFT because it addresses the same privacy-relevant problem. Its advantage is speed and simplicity, which can matter in a system that needs to process images quickly. It is ranked below CRAFT because CRAFT is generally a better fit for highly irregular or stylized text, which is common in real social-media content. EAST differs from Tesseract in that it is about detecting text regions rather than recognizing text characters. It is still a useful companion paper because it gives you a strong alternative detection method for comparison and fallback. Including it strengthens the literature review by showing that text privacy has more than one technical approach.

### 11. An Overview of the Tesseract OCR Engine (2007)

Tesseract is a classic OCR reference, and it remains useful because it is one of the most widely known open-source OCR engines. It ranks lower because its strengths are mostly in reading clearer printed text, while your project needs to handle noisy, stylized, curved, and scene-based text on social media. That difference is important: Tesseract is a recognition baseline, not a full modern scene-text privacy solution. Still, it is useful to include because any serious privacy system must show that it considered OCR foundations before moving to more specialized methods. It is best used as a baseline or comparison paper rather than a direct architectural pillar.

### 12. CIAGAN: Conditional Identity Anonymization GANs (2020)

CIAGAN is relevant because it explores identity anonymization using generative methods instead of simple blur or masking. It ranks below the newer anonymization papers because it is older and more focused on face identity replacement than on a full privacy pipeline. What makes it different is its GAN-based approach, which can preserve more visual realism than basic anonymization. That realism is valuable, but the paper is not as current as G2Face or Face Anonymization Made Simple. For your project, CIAGAN is worth keeping as a methodological bridge between classical blur-based systems and more advanced generative privacy techniques. It is a supporting anonymization paper, not the primary one.

### 13. End-to-End Car License Plate Detection and Recognition (2018)

This paper is included because license plates are one of the privacy-sensitive objects that your system may need to protect. It ranks below the broader papers because it solves a very specific problem: plate detection and recognition. That narrowness is useful in a privacy pipeline, but it also means the paper does not cover the rest of the system. It differs from the face and anonymization papers because it is domain-specific and not centered on human identity protection. Still, it is a good supporting reference when you justify why the system should detect plates separately from faces and text. It helps make the literature review more complete by showing that privacy threats are not limited to people.

### 14. MobileNets: Efficient CNNs for Mobile Vision (2017)

MobileNets is not a privacy paper, but it matters because your project emphasizes local processing and efficient on-device execution. It ranks below the main vision and privacy papers because it is mainly about model efficiency rather than the privacy task itself. Its difference from the rest of the list is that it gives an engineering strategy, not a privacy algorithm. That makes it valuable if you want the final system to run on a modest laptop, mobile device, or edge environment. In the context of your project, MobileNets is best cited when you discuss deployment constraints and why lightweight models matter for privacy-first processing.

### 15. Rapid Object Detection Using a Boosted Cascade of Simple Features (2001)

This is a historically important paper because it helped establish real-time object detection on constrained hardware. It ranks near the bottom because modern detection and anonymization methods are far more suitable for your project. The paper differs from all recent works because it belongs to the classical computer vision era, before deep learning became dominant. Still, it is useful for background because it shows how face detection evolved from simple cascades to modern CNN-based systems. In a literature review, this paper mainly helps you explain the progression of detection technology, but it should not be treated as a technical base for the current project.

### 16. Why Should I Read the Privacy Policy, I Just Need the Service (2021)

This paper is included because it reflects privacy attitudes and user behavior, which gives context to why automated privacy tools are necessary. It ranks last because it is not a technical image-anonymization paper. Its value is conceptual rather than algorithmic: it helps explain the gap between what users should understand and what they actually do when sharing data online. That makes it useful in the introduction or motivation section, but not in the core method section. It differs from the rest of the list because it studies privacy perception rather than building a privacy-protection model. For that reason, it should be cited as supporting motivation rather than as a direct technical reference.

## Real-Time Video and Live Stream Adaptation

Since the project now includes **live video and live streaming** capabilities, the paper ranking must be reconsidered with latency and processing efficiency as top priorities. Real-time streaming has different constraints than static image processing.

### Critical Papers for Live Streaming (High Priority)

**1. Ultralytics YOLOv8 (Rank 3)**
This becomes even more critical for live streaming than static images. YOLOv8 is optimized for real-time performance with minimal latency, which is essential for processing video frames at 30+ FPS. It is faster and more efficient than older YOLO versions and can be quantized for edge deployment. This paper should be your primary detection reference for streaming.

**2. YOLO5Face (Rank 5)**
For live face detection in streaming, YOLO5Face is a strong match because it combines face-specific detection with real-time capability. Unlike MTCNN which may introduce lag in multi-scale processing, YOLO5Face maintains consistent per-frame latency suitable for continuous video. This is more suitable for streams than pure MTCNN.

**3. MobileNets (Rank 14 → Should Move Higher)**
For live streaming, MobileNets becomes much more important than its current ranking suggests. It provides a framework for deploying detection and anonymization models on edge devices with limited compute, which is critical for real-time processing without server offloading. It should be re-prioritized to Rank 8-9 for streaming implementations.

### Papers Needing Caution for Live Streaming (Latency Concerns)

**DeepPrivacy2 (Rank 4)**
While useful for high-quality results, DeepPrivacy2 may be too computationally demanding for live streaming at high frame rates. Synthesizing full-body anonymization in real time can introduce noticeable latency. It is better suited for post-processing or recording, not live streams.

**G2Face (Rank 2)**
Similarly, G2Face's focus on reversible and high-fidelity anonymization adds compute overhead. For live streams where latency is critical, simpler anonymization methods may be preferred. Keep G2Face as a reference for static images but consider lightweight alternatives for streaming.

### Papers Suitable for Both Static and Streaming

**Face Anonymization Made Simple (Rank 1 - Base Paper)**
This paper remains the best base because its methods should be lighter than DeepPrivacy2 and G2Face, making it applicable to both static and streaming scenarios. However, you will need to validate that its anonymization techniques can process frames fast enough for your target FPS.

**CRAFT (Rank 9) and EAST (Rank 10)**
For text detection in streams, EAST is actually preferable to CRAFT for live use because it prioritizes speed over maximum accuracy. CRAFT is better for static images where processing time is not constrained. For streaming, EAST should move up in priority.

### Recommended Paper Stack for Live Streaming

For **live video and streaming implementation**, use this modified order:

1. **YOLOv8** (detection backbone for frames)
2. **Face Anonymization Made Simple** (base anonymization method)
3. **YOLO5Face** (face-specific detection if needed)
4. **MobileNets** (model efficiency and edge deployment)
5. **EAST** (fast text detection for streams)
6. **MTCNN** (fallback face detector if YOLOv8 misses angled faces)
7. **CRAFT** (for reference on advanced text detection, use only if stream FPS allows)

De-prioritize in streaming scenarios:
- **DeepPrivacy2** (too slow for real-time)
- **G2Face** (high latency for streaming)
- **Tesseract** (character-level OCR can be deferred to post-processing)

### Key Considerations for Your Project

- **Frame rate target:** Determine whether you aim for 24 FPS, 30 FPS, or higher. This determines which papers' methods are practical.
- **Edge vs. cloud:** If processing on-device (privacy-first), MobileNets becomes critical. If cloud-based, latency is less of a concern but bandwidth and privacy become trade-offs.
- **Anonymization quality:** For live streams, users may tolerate faster but simpler anonymization (blur, masking) instead of realistic synthesis.
- **Per-frame vs. temporal consistency:** Streaming requires frame-to-frame consistency to avoid flickering. Check if Face Anonymization Made Simple provides temporal stability guidance or if you need additional papers on video-level coherence.
