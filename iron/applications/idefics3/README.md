<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SmolVLM-256M-Instruct on the NPU

A small vision-language model (Idefics3), its vision tower's projected
patch features spliced into its text backbone's input embedding before
the layers run, over `iron.lm`'s shared decoder. Nothing here needs
torch.

Traced from the real `transformers` source
(`modeling_idefics3.py`) before assuming anything: the model does **not**
cross-attend. `Idefics3Model.text_model` is a plain `AutoModel`-loaded
Llama decoder; the vision connection is a prefix splice
(`masked_scatter` of the connector's projected features into the text
embedding sequence at the `<image>` placeholder positions).

What is SmolVLM's own is in `iron/applications/idefics3/`:

- `model.py`: the text backbone (`SmolVLMText`/`SmolVLMTextOracle`,
  Llama's layer, `iron.lm.Layer`, with an **untied** output head, unlike
  Llama/SmolLM2/Qwen 2.5, its shape read from the checkpoint's nested
  `text_config`, its tunables at 576 wide its profile's), the splice
  (`SmolVLM`/`SmolVLMOracle`, `embed()`'s `pixel_values`), `VLMRunner`
  (the text backbone's and the vision tower's tensors from the one
  checkpoint, read by their own names), and `build_prompt()`, the real
  processor's own token layout at any question text
  (`IMAGE_PREAMBLE`/`IMAGE_TOKENS`, read off the real
  `Idefics3Processor`'s output, not guessed)
- `vision/model.py`: the vision tower (`VisionTower`/`VisionTowerOracle`,
  a 12-layer SigLIP-style ViT -- affine LayerNorm, a learned absolute
  position embedding, bias'd attention, a GELU-tanh MLP, its shape read
  from the checkpoint's nested `vision_config`) and the connector
  (pixel-shuffle, then a bias-free projection into the text model's
  space)

The checkpoint nests the text backbone under `model.text_model`, not
`model` (`CausalLM`'s own assumption): `SmolVLMText.__init__` re-roots
the tree it hands the base class to a fresh namespace aliasing
`model.text_model` as `model`, with no edit to the checkpoint's own
tensors; the untied `lm_head` (a checkpoint sibling of `model`) is kept
separately. That alias goes once `CausalLM` takes its decoder module
explicitly (a library change under review). `SmolVLM.body()` is a full copy of `CausalLM.body()` with one
line changed (`pixel_values` threaded to `embed()`): the base class's
`embed(x)` takes no second argument today, since the generic
`iron.lm.Multimodal` hook (the design's part 2) has not landed; this
override deletes once it does. The same gap is why `generate()` and
`Oracle.logits()` do not thread `pixel_values` through either -- this
port's own tests call `embed()`/`body()` directly instead (see `test.py`).

## Scope: one 512x512 image, no splitting

The real processor's own default (`do_image_splitting=True`) decomposes
a large image into several crops plus a thumbnail, each its own pass
through the vision tower, joined by `<row_x_col_y>` text separators; a
crop's own patch grid can then be partial, needing the real processor's
bucketized, padding-aware position ids. This port takes one whole,
unsplit 512x512 image only (`do_image_splitting=False`): the position-id
simplification (a patch's position is just its raster index) and the
splice's own fixed token position both assume that. The image
decode/resize/normalize step itself is host-side for this first pass
(the library's `Resample`-based on-device resize, `iron.lm.ImagePatches`,
targets arbitrary aspect ratios; this model's image is always exactly
512x512 by construction).

The splice's own position (`IMAGE_PREAMBLE`, `IMAGE_TOKENS`) is a
**compile-time constant**, valid for one image, first in the turn, behind
the fixed `<|im_start|>User:` role preamble (`build_prompt()`'s own
layout) -- not a runtime `masked_scatter` at an arbitrary position. A
prompt that puts the image anywhere else, or that is not built by
`build_prompt()`, is not this port's scope.

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)
- [`tokenizer.json`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct)
- [`config.json`](https://huggingface.co/HuggingFaceTB/SmolVLM-256M-Instruct/blob/main/config.json):
  the model's shape (`SmolVLMTextConfig.from_checkpoint`/
  `VisionConfig.from_checkpoint`), read from beside the checkpoint rather
  than hand-copied

The tests look for all three in
`$IRON_EXAMPLE_WEIGHTS_DIR/smolvlm-256m-instruct/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`).

## Testing

```bash
pytest tests/applications/idefics3/
```

Loads the model once and checks it over three (image, question) pairs
(`build_prompt()` at each question's real tokens, a distinct synthetic
512x512 image each): one forward pass per pair, teacher-forced to the
prompt's last position, device logits against the float32 oracle's.
Measured KL(oracle || device) 0.0061-0.0094 over the three; the gate
holds a generous 0.05.

`--random-weights SEED` runs it on drawn weights and a synthetic image,
on a host without the checkpoint.

There is no `python -m iron.applications.idefics3.model ... --prompt-len ...`-style
command-line generation loop yet: `CausalLM.generate()` does not thread
`pixel_values` through (it is not needed for this port's own accuracy
gate, a single forward pass, so not built -- a real gap, not hidden, that
`iron.lm.Multimodal` is expected to close).
