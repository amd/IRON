<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper on the NPU

OpenAI's Whisper (large-v3-turbo's shape: a 32-layer audio encoder, a
4-layer text decoder), an `iron.lm.EncoderDecoder`. Everything is in
`model.py`:

- `WhisperEncoder`: an `iron.lm.Tower` over a clip's log-mel features.
  Two convolutions run first (`iron.lm.Conv1d`, kernel 3, the second at
  stride 2), each followed by a GELU, and the fixed position table is
  added after them. Then come its `Layer`s on Whisper's names
  (`self_attn_layer_norm`/`final_layer_norm`, `fc1`/`fc2`, a bias on every
  projection but `k_proj`) and the final LayerNorm. Its rows are the 1500
  positions rounded up to whole 64-row blocks (1536), bounded per call to
  the clip's positions, so neither attention reads the padding.
- `Whisper`: the decoder, its `Layer`s attending causally and over the
  encoder's output (`encoder_attn`). It adds a learned position table
  after the embedding, and its head is the final LayerNorm and the
  embedding.
- `WhisperOracle`/`WhisperEncoderOracle`: the float32 twins.
- `WhisperConfig`: both shapes, read from the checkpoint's own
  `config.json`.

Nothing rotates (`rope_base` None).

## Status

The model runs at a toy shape with tanh GELU on drawn weights
(`tests/applications/whisper/test.py`). Device-free, each version's
reference is checked against the oracle; on the NPU, the same checks run
through the compiled versions. At large-v3-turbo's real shape, with tanh
GELU and a vocabulary of 51872 standing in for the gaps below, every
version's operators resolve on npu2 and npu1.

The real checkpoint waits on:

- **Exact GELU.** Whisper's `activation_function` is `"gelu"`. `Layer`
  and `WhisperEncoder` refuse it until mlir-aie's exact GELU arrives with
  the pin bump.
- **`Sample` at a vocabulary of 51866.** It has no even slice per core.
- **An fp16 checkpoint.** `Checkpoint` reads F16 tensors as float16, not
  bf16.
- **The log-mel features.** The encoder takes the feature extractor's
  `input_features`. Whisper's extractor clamps each clip's log-mel to its
  own maximum less 8 before the affine `(x + 4) / 4`. That needs a
  reduction over the whole clip, which no operator does yet (`RMSNorm` and
  `Softmax` reduce a row). The rest is `iron.lm.LogMel`'s, with a power
  spectrum, `log10` and a Slaney filterbank.
