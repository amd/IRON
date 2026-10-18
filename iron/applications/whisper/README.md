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
  added after them. Then come its `DecoderLayer`s, each a LayerNorm before
  attention and before a plain GELU MLP, with a bias on every projection
  but `k_proj`, and the final LayerNorm. Its rows are the 1500
  positions rounded up to whole 64-row blocks (1536), bounded per call to
  the clip's positions, so neither attention reads the padding.
- `Whisper`: the decoder, its `CrossDecoderLayer`s attending causally and
  over the encoder's output (`encoder_attn`). It adds a learned position table
  after the embedding, and its head is the final LayerNorm and the
  embedding.
- `Reference`: what the model is judged by, Hugging Face's
  `WhisperForConditionalGeneration` in float32 (`HuggingFaceWhisper`), its
  logits after a clip's features and the decoder's tokens recorded once to
  a file (`iron.lm.Golden`).
- `WhisperConfig`: both shapes, read from the checkpoint's own
  `config.json`, and each layer's parts.
- `sanitize()`: renames Whisper's modules (`self_attn_layer_norm`/
  `final_layer_norm`, `out_proj`) at load to the names the shared parts
  read.
- `bf16()`: the checkpoint ships float16; the graphs hold each weight
  rounded once to bf16, and the reference reads the float16 itself.

Nothing rotates (`rope_theta` None).

## Status

The model runs at a toy shape with tanh GELU on drawn weights
(`tests/applications/whisper/test.py`). Device-free, each version's
reference is checked against Hugging Face's logits, recorded in
`tests/applications/whisper/goldens/` (`pytest --record-goldens -p
no:xdist` records them); on the NPU, the same checks run
through the compiled versions. At large-v3-turbo's real shape, with tanh
GELU and a vocabulary of 51872 standing in for the gaps below, every
version's operators resolve on npu2 and npu1.

The real checkpoint waits on:

- **Exact GELU.** Whisper's `activation_function` is `"gelu"`, which
  `MLP` refuses: no operator computes it.
- **`Sample` at a vocabulary of 51866.** It has no even slice per core.
- **The log-mel features.** The encoder takes the feature extractor's
  `input_features`. Whisper's extractor clamps each clip's log-mel to its
  own maximum less 8 before the affine `(x + 4) / 4`. That needs a
  reduction over the whole clip, which no operator does yet (`RMSNorm` and
  `Softmax` reduce a row). The rest is `iron.lm.LogMel`'s, with a power
  spectrum, `log10` and a Slaney filterbank.
