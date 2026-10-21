<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper-small on Phoenix/NPU1

This example runs Whisper-small on AMD Phoenix/NPU1 using IRON and mlir-aie.

- `whisper_pipeline.py` transcribes audio end to end: WAV in, text out, with
  the frontend, encoder and decoder matrix products on the NPU. Audio longer
  than 30 s is decoded window by window.
- `whisper_encoder.py` is the original short-geometry encoder validation
  (128 Mel frames, 64 encoder tokens).

## End-to-end transcription

`whisper_pipeline.py` uses Whisper's canonical geometry (3000 Mel frames,
1500 encoder tokens) and greedy decoding.

| Stage | NPU | CPU |
| --- | --- | --- |
| Preprocessing | | log-Mel features |
| Frontend | conv1 and conv2 as GEMMs, GELU | im2col |
| Encoder (12 blocks) | Q/K/V/out, score, value, fc1, fc2 GEMMs; LayerNorm, masked softmax, GELU, fc1 bias | head split/merge, other biases, FP32 residual stream |
| Cross-attention K/V | 768x768 GEMM for all decoder blocks | |
| Decoder (prompt, then 1 token per step) | fused Q/K/V, output, fc1, fc2 GEMVs | LayerNorm, attention, GELU |
| Token selection | | vocabulary projection, suppression, timestamp rules, argmax |

The encoder GEMMs use all four Phoenix columns, except the value GEMM: its
N=64 is not a multiple of 4 x `tile_n`. The NPU LayerNorm has no scale or
shift, so each LayerNorm's affine parameters fold into the GEMM weights that
follow it, and the softmax scale folds into Q. The encoder's nine kernels are
built as two chained xclbins (GEMMs, and LayerNorm/softmax/GELU/add), so the
encoder holds two NPU contexts: in one xclbin with all nine, the first
kernels time out on NPU1 (only the last eight ran in testing). The host
still splits and merges the attention heads, adds the biases whose results
pass through it anyway, and accumulates the residual stream in FP32; a BF16
residual stream, rounded at each of the 24 residual adds, about doubled the
encoder error in a CPU emulation.

The decoder processes the prompt and
every generated token one at a time with four-column GEMVs, with the decoder
weights resident in NPU-visible BF16 buffers, which avoids padding a single
token to a 64-row GEMM. All NPU weights are converted to resident BF16 buffers
once at startup, and the encoder GEMMs and decoder GEMVs reuse their input and
output buffers and one XRT run object across calls: allocating buffers or runs
per call costs more than most of these kernels' NPU work. Each phase stays
within the NPU1 context budget and releases its contexts before the next phase
starts.

Run it with:

```text
python iron/applications/whisper_small/whisper_pipeline.py --wav clip.wav
```

Audio up to 30 s is decoded as one window without timestamps. Longer audio
(or any audio with `--long-form`) follows OpenAI Whisper's sequential
long-form algorithm: each 30 s window is decoded with timestamps, and the next
window starts at the last complete timestamp pair. Decoding is greedy, without
temperature fallback and without conditioning on the previous window's text;
this reproduces the text of Hugging Face `generate(return_timestamps=True,
condition_on_prev_tokens=False)` on the CPU. The segments are printed with
their start and end times.

The script also runs a Hugging Face FP32 CPU reference on the same log-Mel
features, after the NPU run. For one window it requires an exact token match.
For long-form audio, the reference decodes the same windows the NPU chose; the
text tokens must match exactly and each timestamp within two steps (0.04 s),
since adjacent timestamps are often near-ties in BF16. The script exits
non-zero on a mismatch or when a window produces no end-of-text token.
`--reference-text transcript.txt` reports the word error rate against a
transcript; `--no-reference` skips the CPU reference. `transformers` is
required for the tokenizer in either case.

Compiled kernels go to `--build-dir`, `$IRON_WHISPER_BUILD_DIR`, or
`<artifact dir>/pipeline-build`. On Windows, use a short path such as
`C:\iw` to stay below path-length limits. The first run compiles all kernels
(several minutes).

Validation on Phoenix (warm kernel cache, LibriSpeech clips, mlir-aie
`1.4.4.dev73` as pinned in `requirements.txt`):

| Clip | Audio | Windows | Encoder NRMSE | Tokens | WER | Encoder | Compute | Decode |
| --- | ---: | ---: | ---: | --- | ---: | ---: | ---: | ---: |
| 1919-142785-0007 | 26.6 s | 1 | 2.71% | exact | 0.0% | 1.4 s | 8.9 s | 13.0 tok/s |
| 3170-137482-0000 | 28.0 s | 1 | 2.74% | exact | 1.5% | 1.3 s | 8.5 s | 13.6 tok/s |
| 5.9 s test clip | 5.9 s | 1 | 4.14% | exact | 0.0% | 1.4 s | 4.4 s | 11.8 tok/s |
| 422-122949-0013 | 32.6 s | 2 | | text exact, timestamps exact | 6.0% | 2.7 s | 14.6 s | 12.3 tok/s |
| 2902-9006-0005, -0007, -0015 joined | 97.0 s | 4 | | text exact, timestamps within 0.02 s | 2.3% | 5.5 s | 36.4 s | 13.4 tok/s |

The CPU FP32 reference has the same word error rate on every clip. Timings
vary by up to 2x between identical runs on Windows; the table shows typical
values. Before the encoder's LayerNorm, softmax and GELU moved to the NPU,
the encoder took about 2.4 s per window, with an encoder NRMSE of
1.9-2.7%.

> [!WARNING]
> **Accuracy of the NPU LayerNorm, softmax and GELU kernels.** These kernels
> are the largest remaining source of encoder error. With the previous
> mlir-aie (`1.4.4.dev53`) the encoder NRMSE was 3.6-5.3%; replacing all
> three with exact CPU functions (still BF16 outputs) brought it to 2.2% on
> 1919-142785-0007, and each kernel contributed. The NPU GELU uses the tanh
> approximation, while Whisper uses the exact erf form.
>
> With `1.4.4.dev53`, the 97 s clip did not match the CPU reference: in its
> first window, after "...swim with the stream", the CPU FP32 model prefers
> "." over "," by only 0.054 logits (35.880 vs 35.827), and the NPU picked
> ",". With `1.4.4.dev73` it matches. Near-ties like this one are decided by
> BF16 rounding as a whole, so other audio may still produce such
> mismatches; the pipeline reports them and exits non-zero.

## Encoder-only validation

> [!NOTE]
> The rest of this document describes the short-geometry encoder validation in
> `whisper_encoder.py`.

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
| Final encoder output | 2.730% | 0.03920 | 0.999628 |

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

- Greedy decoding only, without beam search, temperature fallback,
  no-speech detection or conditioning on the previous window's text.
  Timestamps are produced only in long-form mode.
- Attention softmax, LayerNorm and GELU in the decode step, and the
  vocabulary projection, still run on the CPU. The fused `mha` operator
  targets NPU2 only, so encoder attention is built from per-head GEMMs and
  softmax.
- The encoder's NPU LayerNorm, softmax and GELU kernels cost accuracy; see the
  warning under the validation table.
- Only one process can use the NPU at a time; a second process fails to
  create its hardware context.
