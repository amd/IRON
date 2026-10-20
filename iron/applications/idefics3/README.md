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

Its vision LayerNorms run at the LayerNorm kernel's epsilon, 1e-5
(`iron.functional.LAYER_NORM_EPS`), not the checkpoint's 1e-6.

## Scope: one image of any size, no splitting

By default (`do_image_splitting=True`), the real processor splits a large
image into crops plus a thumbnail, each its own pass through the tower,
and a crop's patch grid can be partial. This port takes one whole, unsplit
decoded image (`do_image_splitting=False`) of up to 3072x4096 either way
up, uint8, and processes it on the NPU as the processor does: a Lanczos
resize to 2048 on its longest side (`iron.lm.ImageResize`), another to
512x512, then the rescale and normalization (`iron.lm.ImagePatches`), the
pixels bit for bit the processor's in bfloat16.

## Weights and tokenizer

From Hugging Face
([`HuggingFaceTB/SmolVLM-256M-Instruct`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)):
`model.safetensors`, `tokenizer.json` and `config.json`.

## Testing

```bash
pytest tests/applications/idefics3/
```

On the NPU it checks three (image, question) pairs, each a distinct
synthetic 512x512 image, and two images of other sizes: the logits after
the prompt and after one decode step, against transformers' model over its
own processor's pixels, teacher-forced. `--random-weights SEED` runs it on
drawn weights without the checkpoint. `reference/` checks the tower's soft
tokens and the `Multimodal`'s logits across a chunk boundary device-free,
at a toy shape over random weights.

`python -m iron.applications.idefics3.model` runs the text model alone;
the command line takes no image.
