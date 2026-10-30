<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper on the NPU

OpenAI's Whisper (large-v3-turbo's shape by default: a 32-layer audio
encoder, a 4-layer text decoder; small's: 12 and 12) as an
`iron.lm.EncoderDecoder`; `model.py`'s docstrings describe the encoder
(`WhisperEncoder`), the decoder (`Whisper`) and the config. `hugging_face.py`,
which only the tests import, is what it is judged by. The shared library is
[AGENTS.md](../../../AGENTS.md#language-models).

## Status

The model runs at a toy shape on drawn weights, with tanh GELU and with
exact (`tests/applications/whisper/test.py`): device-free, each version's
reference against Hugging Face's logits recorded in
`tests/applications/whisper/goldens/`, and the same checks on the NPU.
`Whisper.load` builds large-v3-turbo or small from its checkpoint
(`config.json`, `model.safetensors`, `tokenizer.json`), held on the NPU to
transformers' logits recorded in `golden.npz` beside it; the tests find
them at `$IRON_EXAMPLE_WEIGHTS_DIR/whisper-large-v3-turbo` and
`whisper-small`. A prompt starts at `<|startoftranscript|>`, the
checkpoint's `decoder_start_token_id`. Small ships 80 mel bins, not
large-v3-turbo's 128; `WhisperEncoderConfig.conv1_channels` and
`LogMel.mel_pad` pad the GEMM tiles their shape would otherwise miss.

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

Every version (the decode step, a prompt chunk, the encode version) compiles
for NPU1 at both checkpoints, device-free: `supported_devices("npu1",
"npu2")` on the device tests.

## Transcription

`Whisper.transcribe(audio)` runs one window (up to 30 s at large-v3-turbo's):
encode, the `<|startoftranscript|> <|language|> <|task|> <|notimestamps|>`
prompt, greedy generation through `Model.generate`, and the decoded text.
`sampled()` adds a suppression bias (-inf at `generation_config.json`'s
`suppress_tokens`, `begin_suppress_tokens` on the prompt's own call, and
every token from the task block on) to the logits `Sample` draws from on
the device, before `Model.generate`'s `logits` is returned; a model's
returned logits themselves stay unsuppressed, so accuracy checks against
Hugging Face's own forward pass are unaffected. `audio.py` loads and saves
mono 16 kHz PCM16 WAV; `wer.py` scores a transcript's word error rate.

```text
python -m iron.applications.whisper.model <path> --wav clip.wav
```

Audio longer than one window raises rather than silently truncating:
long-form transcription (OpenAI Whisper's sequential windowed decoding
with timestamps, `transcribe_long`) is not yet built. This ports the
decoding algorithms of amd/IRON#218 (Giuseppe Capaldo)'s Whisper-small on
Phoenix/NPU1, built on pre-refactor kernel plumbing, onto `iron.lm`'s
`EncoderDecoder`: its token suppression, prompt structure and WER scoring
carry over; its timestamp-pairing rules (`TokenPolicy`) still need a
device-side equivalent of their own, since every draw, timestamps
included, runs on the NPU here.
