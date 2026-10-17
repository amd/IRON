<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolVLM-256M-Instruct on the NPU

A small vision-language model (Idefics3): a text model and a vision
tower as one `iron.lm.Multimodal`, whose `<image>` placeholders take the
tower's soft tokens. Nothing here needs torch.

In the `transformers` source (`modeling_idefics3.py`), the model does not
cross-attend. `Idefics3Model.text_model` is a plain Llama decoder, and
the connector's projected features replace the text embedding's rows at
the `<image>` placeholders (`masked_scatter`). `Multimodal` places them
the same way.

What is SmolVLM's own is in `iron/applications/idefics3/`:

- `model.py`:
  - `SmolVLMText`/`SmolVLMTextOracle`: the text model, a `CausalLM` on
    `iron.lm.Layer`, with an untied output head (unlike
    Llama/SmolLM2/Qwen 2.5), its shape read from the checkpoint's nested
    `text_config`. The checkpoint nests it under `model.text_model`, which
    `CausalLM` and `Oracle` read through `decoder=`; `lm_head` is a
    sibling of `model`. Its tunables at 576 wide are its profile's.
  - `VLMRunner.npu()`: the text model and the tower as one `Multimodal`,
    keyed by the checkpoint's `image_token_id`.
  - `SmolVLMOracle`: its float32 twin, the tower's soft tokens at the
    placeholders.
  - `build_prompt()`: the real processor's token layout around one image
    and a question's ids, the ids either side read off
    `Idefics3Processor`'s output.
- `vision/model.py`: the vision tower and connector, an `iron.lm.Tower`
  (`VisionTower`) on `iron.lm.Layer`'s SigLIP names (`layer_norm1`/
  `layer_norm2`, biased attention, a GELU-tanh `fc1`/`fc2`; nothing
  rotates), and its float32 twin (`VisionOracle`). It is a 12-layer ViT
  with a learned absolute position embedding, then the connector's
  pixel-shuffle (`pool`, one `Copy`) and its bias-free projection into the
  text model's space (`head`). Its LayerNorms run at the kernel's
  epsilon, 1e-5, until the pinned mlir-aie takes the checkpoint's 1e-6
  (`layer_norm_eps`); the oracle uses 1e-6.

## Scope: one 512x512 image, no splitting

By default (`do_image_splitting=True`), the real processor splits a large
image into several crops plus a thumbnail. Each is its own pass through
the vision tower, joined by `<row_x_col_y>` text separators, and a
crop's patch grid can be partial, which needs the processor's
bucketized, padding-aware position ids. This port takes one whole,
unsplit 512x512 image (`do_image_splitting=False`), so a patch's
position is its raster index. The image is decoded, resized and
normalized on the host.

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)
- [`tokenizer.json`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)
- [`config.json`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct/blob/main/config.json):
  the model's shape (`SmolVLMTextConfig.from_checkpoint`/
  `VisionConfig.from_checkpoint`), read from beside the checkpoint

The tests look for all three in
`$IRON_EXAMPLE_WEIGHTS_DIR/smolvlm-256m-instruct/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`).

## Testing

```bash
pytest tests/applications/idefics3/
```

On the NPU, it loads the model once. It then checks three (image,
question) pairs, each a distinct synthetic 512x512 image: the device's
logits after the prompt and after one decode step, against the float32
oracle's, teacher-forced. `tests/applications/idefics3/reference/` holds
the device-free checks at a toy shape: the tower's reference against
`VisionOracle`, and every version of the `Multimodal` in turn against
`SmolVLMOracle`, the soft tokens crossing a chunk boundary.

`--random-weights SEED` runs it on drawn weights and random questions,
on a host without the checkpoint.

`python -m iron.applications.idefics3.model` runs the text model alone;
the command line takes no image.
