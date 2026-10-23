<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolVLM-256M-Instruct on the NPU

A small vision-language model (Idefics3): its text model and vision tower
as one `iron.lm.Multimodal`, `SmolVLM`, whose `<image>` placeholders take the tower's
soft tokens, as transformers' `masked_scatter` places them; the model does
not cross-attend. `model.py` and `vision/model.py` say what is its own.
The shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Images: split as the processor splits them

The checkpoint's processor splits an image (`do_image_splitting=True`), and
so does this port: one decoded image of up to 3072x4096 either way up,
uint8, processed on the NPU as the processor does. A Lanczos resize to 2048
on its longest side (`iron.lm.ImageResize`), another to whole 512x512
squares at its aspect (up to 2048x2048), then each square and the whole
resized to 512x512 is a frame: rescaled and normalized
(`iron.lm.ImagePatches`), the pixels bit for bit the processor's in
bfloat16, and through the tower, 64 soft tokens each. An image gives up to
16 squares and the whole, 1088 soft tokens. `VisionConfig.do_image_splitting`
false takes the whole alone, as `do_image_splitting=False` does.

The tower is one version, called once a frame; each call resizes the image
anew, since a version's steps all run.

## Precision

The tower's patch embedding and connector run at `Precision.HIGHEST`, its
layers' projections and the text model's at their configs' precision.
Measured on npu2 over the tests' four photos, eight steps each,
KL(float32 transformers || device) averages 0.0031 to 0.016 a photo, 0.080
at the worst step, with no top-1 mismatch.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolVLM-256M-Instruct`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)):
`model.safetensors`, `tokenizer.json` and `config.json`.

## Testing

```bash
pytest tests/applications/idefics3/
```

On the NPU it checks four COCO val2017 photos of different sizes and
aspects, each with a question, one compile serving them all: the
next-token distribution after the prompt and after seven decode steps,
teacher-forced, against transformers' model over its own processor's
pixels, split as the checkpoint's processor splits them. The photos are
fetched from COCO's own host by URL and sha256 into IRON's cache. `--random-weights SEED` runs it on
drawn weights without the checkpoint. `reference/` checks the tower's soft
tokens, every frame's, and the `Multimodal`'s logits across a chunk
boundary device-free, at a toy shape over random weights.

`python -m iron.applications.idefics3.model` runs the text model alone;
the command line takes no image.
