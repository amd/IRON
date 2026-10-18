<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper on the NPU

OpenAI's Whisper (large-v3-turbo's shape: a 32-layer audio encoder, a
4-layer text decoder) as an `iron.lm.EncoderDecoder`; `model.py`'s
docstrings describe the encoder (`WhisperEncoder`), the decoder (`Whisper`)
and the config. `hugging_face.py`, which only the tests import, is what it
is judged by. The shared library is [AGENTS.md](../../../AGENTS.md#language-models).

## Status

The model runs at a toy shape with tanh GELU on drawn weights
(`tests/applications/whisper/test.py`): device-free, each version's
reference against Hugging Face's logits recorded in
`tests/applications/whisper/goldens/`, and the same checks on the NPU.

The real checkpoint waits on:

- **Exact GELU.** Whisper's `activation_function` is `"gelu"`, which
  `MLP` refuses: no operator computes it.
- **The log-mel features.** Whisper's extractor clamps each clip's log-mel
  to its own maximum less 8 before the affine `(x + 4) / 4`. That needs a
  reduction over the whole clip, which no operator does (`RMSNorm` and
  `Softmax` reduce a row). The rest is `iron.lm.LogMel`'s.
