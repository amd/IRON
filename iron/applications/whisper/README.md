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

The model runs at a toy shape on drawn weights, with tanh GELU and with
exact (`tests/applications/whisper/test.py`): device-free, each version's
reference against Hugging Face's logits recorded in
`tests/applications/whisper/goldens/`, and the same checks on the NPU.
`Whisper.load` builds large-v3-turbo from its checkpoint (`config.json`,
`model.safetensors`, `tokenizer.json`), held on the NPU to transformers'
logits recorded in `golden.npz` beside it; the tests find it at
`$IRON_EXAMPLE_WEIGHTS_DIR/whisper-large-v3-turbo`. A prompt starts at
`<|startoftranscript|>`, the checkpoint's `decoder_start_token_id`.

`hidden_act` `"gelu"`, Whisper's own, is the exact GELU, `GELU`'s
`approximate="none"` on mlir-aie's `gelu_erf`.

The encoder takes a clip's samples at 16 kHz (`WhisperEncoder.inputs`):
the host pads or cuts them to the clip (30 s at large-v3-turbo's) and
mirrors 200 samples at each end, as `torch.stft` centres its frames, and
the NPU computes the extractor's log-mel features from them,
`iron.lm.LogMel` with Whisper's parameters: the power spectrum through
Slaney's mel filters, then each log10 held to 8 below the clip's largest
(`RowMax` twice), as `(x + 4) / 4` (`Log10Clamp`). On LibriSpeech clips
they are transformers' `WhisperFeatureExtractor`'s rounded to bf16 at all
but 0.05% of features, those one bf16 ulp away
(`iron/tests/lm/test_log_mel.py`).
