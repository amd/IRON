<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper-small Encoder on Phoenix/NPU1

This example runs the Whisper-small encoder on AMD Phoenix/NPU1 using IRON
and mlir-aie.

The validated path performs Whisper log-Mel preprocessing on the CPU and runs
the convolutional frontend, all 12 transformer encoder blocks, and the final
encoder LayerNorm on the NPU.

> [!NOTE]
> This is an encoder example, not a complete speech-to-text implementation.
> The Whisper decoder and autoregressive token generation are not implemented.

## Model path

```text
16-kHz mono PCM16 WAV
        |
        v
CPU log-Mel preprocessing
        |
        v
80 x 128 features
        |
        +---------------- Phoenix/NPU1 ----------------+
        |
        v
Conv1 -> GELU -> Conv2 -> GELU
        |
        v
64 x 768 encoder tokens
        |
        v
12 transformer encoder blocks
        |
        v
final encoder LayerNorm
```

The current validation geometry uses 128 feature frames and produces 64
encoder tokens. Whisper's canonical 3000-frame / 1500-token encoder geometry
is not yet exercised by this example.

## Requirements

Install IRON and activate an environment containing the IRON/mlir-aie runtime
dependencies.

Set `WHISPER_SAFE` to an OpenAI Whisper-small `model.safetensors` checkpoint:

```powershell
$env:WHISPER_SAFE = "C:\path\to\whisper-small\model.safetensors"
```

Reference generation also requires a 16-kHz mono PCM16 WAV. Set
`WHISPER_TEST_WAV` to the validation audio:

```powershell
$env:WHISPER_TEST_WAV = "C:\path\to\validation.wav"
```

Alternatively, pass the WAV explicitly with `--wav`.

Generated validation artifacts are written under `phoenix-whisper-probes` by
default. Set `IRON_WHISPER_ARTIFACT_DIR` to select another location.

## Run the example

Generate real-audio FP32 references:

```text
python iron/applications/whisper_small/whisper_encoder.py --prepare-reference
```

Run the Phoenix encoder against existing references:

```text
python iron/applications/whisper_small/whisper_encoder.py --run
```

Generate references and run the complete validation:

```text
python iron/applications/whisper_small/whisper_encoder.py --all
```

Use `--wav` to override `WHISPER_TEST_WAV`. Use `--help` for optional reference and output paths.

## Implementation

`whisper_frontend.py` implements the NPU convolutional frontend. Whisper's
Conv1D operations are lowered to BF16 GEMMs:

- Conv1 uses logical K=240 padded to K=256.
- Conv2 uses K=2304.
- Conv2's logical 64-row output is executed with physical M=128 and sliced
  back to 64 rows.

`whisper_encoder.py` executes the frontend, all 12 transformer blocks, and
the final LayerNorm in the same Python process. The implementation uses the
LayerNorm, GELU, Softmax, and GEMM operators provided by the current
IRON/mlir-aie stack; no application-specific changes to those generic
operators are required.

The FP32 reference generators are separate from the NPU inference path and
are used only for numerical validation.

## Validation

The 128-frame / 64-token validation uses real audio and completes all frontend
and encoder stages with finite outputs. The FP32 reference uses exact GELU,
matching the Whisper model configuration.

On the validated real-audio sample, the final Phoenix/NPU1 encoder output
measured approximately:

| Stage | NRMSE | RMSE | Cosine similarity |
| --- | ---: | ---: | ---: |
| Final encoder output | 4.706% | 0.06755 | 0.998893 |

The pytest hardware validation enforces a maximum final encoder NRMSE of
`5.0%`. Five consecutive validation iterations reproduced the same final
metrics.

The attention score and value GEMMs use their logical sequence dimensions
rather than relying on the current `SEQ == HEAD_DIM == 64` geometry.

`whisper_audio.py` implements the real-audio preprocessing path:

```text
PCM16 WAV
  -> float32 waveform
  -> Whisper pad/crop
  -> centered STFT
  -> Mel projection
  -> log compression
  -> Whisper normalization
```

The preprocessing implementation was independently compared with Hugging
Face's `WhisperFeatureExtractor`, with approximately `1.19e-7` maximum
absolute error and `5.13e-9` RMSE.

## Current limitations

The following are outside the validated scope of this example:

- canonical 3000-frame / 1500-token encoder execution
- Whisper decoder
- causal decoder self-attention
- encoder-decoder cross-attention
- KV-cache behavior
- autoregressive token generation
- tokenizer/generation integration
- end-to-end speech transcription

The next implementation boundary is the Whisper decoder.
