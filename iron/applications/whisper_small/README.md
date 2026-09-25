<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper-small Encoder on Phoenix/NPU1

This application provides experimental Whisper-small encoder support for
AMD Phoenix/NPU1 using IRON and mlir-aie.

The validated path derives Whisper log-Mel features from real audio on the
CPU, then executes the convolutional frontend, all 12 encoder transformer
blocks, and the final encoder LayerNorm on the Phoenix NPU.

> [!NOTE]
> This is currently an encoder validation application, not a complete
> speech-to-text implementation. The Whisper decoder and autoregressive
> generation are not yet implemented.

## Implemented path

```text
16-kHz mono PCM16 WAV
        |
        v
CPU Whisper log-Mel preprocessing
        |
        v
80 x 128 feature frames
        |
        +---------------- Phoenix/NPU1 ----------------+
        |
        v
Conv1 -> GELU
        |
        v
Conv2 -> GELU
        |
        v
64 x 768 encoder tokens
        |
        v
12 Whisper-small encoder blocks
        |
        v
final encoder LayerNorm
```

The current Phoenix validation geometry intentionally uses 128 feature
frames, producing 64 encoder tokens. It does not yet exercise Whisper's
canonical 3000-frame / 1500-token encoder geometry.

## Requirements

Install IRON and activate an environment containing the IRON/mlir-aie
runtime dependencies.

The reference utilities additionally require PyTorch and NumPy.

Set `WHISPER_SAFE` to an OpenAI Whisper-small `model.safetensors` file:

```powershell
$env:WHISPER_SAFE = "C:\path\to\whisper-small\model.safetensors"
```

Generated validation artifacts are written under `phoenix-whisper-probes`
by default. Set `IRON_WHISPER_ARTIFACT_DIR` to select another location.

## Controlled validation

Generate deterministic FP32 references:

```text
python iron/applications/whisper_small/whisper_encoder.py --prepare-reference
```

Run the Phoenix frontend and complete 12-block encoder:

```text
python iron/applications/whisper_small/whisper_encoder.py --run
```

Generate references and run the complete validation:

```text
python iron/applications/whisper_small/whisper_encoder.py --all
```

The encoder driver also accepts explicit frontend/reference/output artifact
paths; use `--help` for the complete command-line interface.

## Real-audio validation

`whisper_audio.py` implements the Whisper audio preprocessing used by the
real-speech validation path:

```text
PCM16 WAV
  -> float32 waveform
  -> Whisper pad/crop
  -> centered STFT
  -> Mel projection
  -> log compression
  -> Whisper normalization
```

The implementation was independently compared with Hugging Face's
`WhisperFeatureExtractor`. For the preprocessing oracle, the maximum
absolute error was approximately `1.19e-7` with RMSE approximately
`5.13e-9`.

Real-speech validation used the LibriSpeech dummy validation sample
`1272-128104-0000` from
`hf-internal-testing/librispeech_asr_dummy`.

For that input, the Phoenix frontend Block-0 input comparison against the
FP32 reference measured approximately:

| Metric | Result |
| --- | ---: |
| Max absolute error | 0.03118 |
| Mean absolute error | 0.001177 |
| RMSE | 0.002496 |
| NRMSE | 0.280% |
| Cosine similarity | 0.999996 |

All 12 encoder blocks and the final encoder LayerNorm completed with finite
outputs in the original real-speech validation. That validation measured
approximately `2.554%` NRMSE and `0.999674` cosine similarity at the final
encoder output.

A subsequent validation against the current upstream IRON/mlir-aie stack used
the deterministic 128-frame / 64-token configuration. The complete encoder
executed successfully with finite outputs and normal teardown. Its final
encoder comparison against the FP32 reference measured approximately `7.99%`
NRMSE with `0.9968` cosine similarity.

Exact-input operator checks on the current stack remained substantially closer
to their mathematical references. The observed late-encoder difference
accumulates and is amplified across encoder depth; the current validation did
not identify a single LayerNorm, GELU, Softmax, or GEMM operation as its sole
cause.

See [ENGINEERING_EXPERIENCE.md](ENGINEERING_EXPERIENCE.md) for validation
methodology and numerical investigation details.

## Phoenix implementation notes

The frontend lowers Whisper's Conv1D operations to Phoenix BF16 GEMMs.
Conv1 uses logical K=240 padded to K=256. Conv2 uses K=2304, and its
logical 64-row result is physically padded to M=128 for the Phoenix GEMM
before slicing back to 64 rows.

Encoder blocks intentionally execute in fresh Python subprocesses. This
keeps the number of simultaneously live XRT kernel handles bounded on the
tested Phoenix/XRT configuration.

The encoder uses the LayerNorm, GELU, Softmax, and GEMM operators provided by
the current IRON/mlir-aie stack; no application-specific modifications to
those generic operators are required by this validation path.

## Current limitations

The following are outside the validated scope of this application:

- canonical 3000-frame / 1500-token Whisper encoder execution
- Whisper decoder
- causal decoder self-attention
- encoder-decoder cross-attention
- KV-cache behavior
- autoregressive token generation
- tokenizer/generation integration
- end-to-end speech transcription
- complete 12-block controlled encoder execution on the clean current-upstream
  IRON/mlir-aie stack without application-specific generic operator patches;
- current-upstream stage-level numerical characterization through the final
  encoder LayerNorm.

The next implementation boundary is the Whisper decoder.