<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper on the NPU

OpenAI Whisper (`openai/whisper-small`) speech-to-text on `iron.lm`,
compiled as one `Whisper` graph with three versions sharing a single device
arena:

- `encode`: the 2-layer Conv1d frontend (`conv1`, `GELU`, `conv2`, `GELU`
  and learned `embed_positions`), 12 bidirectional `EncoderLayer` blocks,
  the final `LayerNorm`, and every decoder layer's cross-attention `K` and
  `V` projections written directly into shared `iron.state` buffers;
- `prompt_chunk`: a 64-row decoder prefill chunk over `KVCache`
  self-attention, cross-attention `MHA` over the encoder's `K` and `V`
  states, `MLP`, final `LayerNorm`, `lm_head` and `Sample`;
- `decode_step`: a single-token decoder step with `GEMV` projections,
  packed self-attention and cross-attention `MHA`, `GELU`, `lm_head` (padded
  to 51,968 rows across 8 lanes) and `Sample`.

Audio up to 30 s is transcribed in one window without timestamps. Audio
longer than 30 s (or with `--long-form`) runs OpenAI Whisper's sequential
long-form algorithm with `ApplyTimestampRules`: each 30 s window is decoded
with paired non-decreasing timestamps, advancing the next window to the last
complete timestamp pair.

- `model.py`: `WhisperConfig`, `WhisperEncoder`, `WhisperDecoder`,
  `Whisper`, `TokenPolicy` and the CLI
- `audio.py`: pure-NumPy 16 kHz mono WAV loading and 30 s / long-form
  log-Mel spectrogram extraction
- `hugging_face.py`: Hugging Face's `WhisperForConditionalGeneration` in
  float32, used only when recording goldens or running `--check-reference`
- `profiles/`: per-device operator tunables (`npu1.json`, `npu2.json`)

## Weights and tokenizer

The checkpoint directory holds `model.safetensors`, `config.json`,
`tokenizer.json` and `preprocessor_config.json`. Install
`requirements_examples.txt` as
[Models](../../../docs/models.md#running-testing-and-tuning-a-text-decoder)
describes.

## Running

```bash
python -m iron.applications.whisper.model /path/to/whisper-small --wav clip.wav
```

Pass `--long-form` to force timestamped decoding on clips under 30 s,
`--reference-text transcript.txt` to report word error rate (WER), and
`--check-reference` to compare the encoder output and decoded tokens against
Hugging Face's float32 model.

## Validation on Phoenix (NPU1)

With `mlir-aie` `1.4.5.dev119`, `GELU(approximate="none")` (`gelu_erf`) is
exact (0 of 48,853 normal-output finite `bfloat16` inputs misrounded on
`npu1`), and `LayerNorm` (`layer_norm_eps`) keeps its statistics in 3-limb
`float32` (within 1 `bfloat16` ULP on `npu1`). All projections and attention
matmuls run at `Precision.HIGHEST`.

Measured on Phoenix (`npu1`) across five LibriSpeech clips against the
Hugging Face float32 CPU reference:

| Clip | Audio | Windows | Encoder NRMSE | Encoder Cosine | Tokens / Words vs FP32 | WER | Total Time |
| --- | ---: | ---: | ---: | ---: | --- | ---: | ---: |
| 5.9 s test clip | 5.9 s | 1 | 4.06% | 0.99917 | exact (`23/23`) | 0.0% | 6.8 s |
| `1919-142785-0007` | 26.6 s | 1 | 2.33% | 0.99972 | exact (`85/85`) | 0.0% | 22.1 s |
| `3170-137482-0000` | 28.0 s | 1 | 2.23% | 0.99975 | exact (`84/84`) | 1.5% | 21.9 s |
| `422-122949-0013` | 32.6 s | 2 | | | words exact, window end exact | 6.0% | 43.9 s |
| `2902-9006-0005, -0007, -0015` | 97.0 s | 4 | | | words exact, window end within 0.02 s | 2.3% | 120.9 s |

The float32 CPU reference produces the exact same word error rate on every
clip.

## Testing

```bash
pytest tests/applications/whisper/reference/   # device-free toy graph vs Hugging Face
pytest tests/applications/whisper/             # hardware tests on NPU1 and NPU2
```

Record missing goldens where `torch` and `transformers` are installed with
`pytest <test> --record-goldens -p no:xdist`.
