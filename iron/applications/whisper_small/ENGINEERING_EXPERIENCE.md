<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Whisper-small Phoenix Encoder Validation

## Overview

This document summarizes the validation of the experimental Whisper-small
encoder application for AMD Phoenix/NPU1 using IRON and mlir-aie.

The validated path covers CPU Whisper audio preprocessing followed by
Phoenix execution of the convolutional frontend, all 12 encoder transformer
blocks, and the final encoder LayerNorm.

The work intentionally stops at the encoder boundary. It does not claim
complete Whisper speech-to-text execution.

## Motivation

The initial goal was to execute Whisper on a Phoenix/XDNA1 NPU.

During the investigation, the higher-level Ryzen AI/Vitis AI model path
presented hardware, release, and toolchain constraints for the tested
Phoenix configuration. IRON/mlir-aie was selected because it exposes the
operator implementations, AIE kernels, data movement, and XRT execution
path required for direct debugging and numerical validation.

This made it possible to inspect and modify individual transformer
operators and to localize numerical differences at intermediate tensor
boundaries.

## Tested configuration

The validated configuration is:

```text
model       OpenAI Whisper-small
device      AMD Phoenix / NPU1
frontend    80 x 128 log-Mel frames
sequence    64 encoder tokens
hidden      768
heads       12
blocks      12
runtime     XRT through mlir-aie
```

The 128-frame geometry is a controlled validation configuration. It should
not be interpreted as validation of Whisper's canonical 3000-frame input
or 1500-token encoder sequence.

## Reference methodology

FP32 reference artifacts are generated independently of the Phoenix
execution path.

Intermediate reference tensors are retained at frontend and encoder block
boundaries so numerical differences can be localized.

The reference path records:

```text
frontend Conv1 / GELU
frontend Conv2 / GELU
Block-0 input

per encoder block:
    input
    after attention
    output

final encoder LayerNorm
```

Real-audio preprocessing was additionally compared against Hugging Face's
`WhisperFeatureExtractor`.

## Whisper audio preprocessing

`whisper_audio.py` implements the tested Whisper audio preprocessing
without requiring Transformers at runtime.

The processing sequence is:

```text
mono 16-kHz PCM16 WAV
        |
        v
float32 waveform
        |
        v
Whisper 30-second pad/crop
        |
        v
400-point centered STFT
hop length = 160
        |
        v
power spectrum
        |
        v
Whisper-small Mel filters
        |
        v
log10 compression
        |
        v
dynamic-range clamp and normalization
        |
        v
requested feature-frame slice
```

Waveform padding/cropping occurs before the centered STFT. The requested
128 feature frames are selected afterward.

### Hugging Face comparison

The preprocessing implementation was independently compared with Hugging
Face's `WhisperFeatureExtractor`.

For the tested preprocessing oracle:

| Metric | Result |
| --- | ---: |
| Shape | 1 x 80 x 128 |
| Max absolute error | 1.19e-7 |
| Mean absolute error | 2.44e-10 |
| RMSE | 5.13e-9 |
| allclose at 1e-6 | True |

This establishes agreement between the standalone preprocessing path and
the independent Hugging Face implementation for the tested input.

## Real-speech validation input

Real-speech validation used:

```text
dataset        hf-internal-testing/librispeech_asr_dummy
configuration  clean
split          validation
sample         1272-128104-0000
sample rate    16000 Hz
channels       mono
duration       approximately 5.855 seconds
```

The reference transcript is:

> MISTER QUILTER IS THE APOSTLE OF THE MIDDLE CLASSES AND WE ARE GLAD TO
> WELCOME HIS GOSPEL

The resulting 128-frame feature tensor was finite with an approximate
range of:

```text
min  -0.80603
max   1.19397
```

The permanent WAV preprocessing path regenerated the previously captured
frontend reference exactly for:

```text
mel
conv1
gelu1
conv2
gelu2
block0_input
```

The maximum and mean differences for those regenerated reference tensors
were zero.

## Phoenix frontend

The Phoenix frontend executes:

```text
80 x 128 Mel input
        |
        v
Conv1 GEMM
        |
        v
GELU1
        |
        v
Conv2 GEMM
        |
        v
GELU2
        |
        v
64 x 768 tokens
        |
        v
positional embedding
        |
        v
Block-0 input
```

The convolutional layers are lowered to BF16 GEMMs.

Conv1 has logical K=240 and is padded to K=256 for the Phoenix GEMM.

Conv2 has K=2304. Its logical 64-row result is physically padded to M=128
for GEMM execution and sliced back to 64 rows before bias application.

### Real-speech frontend result

The final Block-0-input comparison against the canonical FP32 reference
measured:

| Metric | Result |
| --- | ---: |
| Max absolute error | 0.0311775 |
| Mean absolute error | 0.00117749 |
| RMSE | 0.00249600 |
| NRMSE | 0.279818% |
| Cosine similarity | 0.999996 |
| Finite | True |

## Complete Phoenix encoder

The real-speech Phoenix frontend output was propagated through all 12
Whisper-small encoder blocks and the final encoder LayerNorm.

Each transformer block executes in a fresh Python subprocess.

This is an intentional runtime-lifetime strategy for the tested
Phoenix/XRT stack. It bounds the number of simultaneously live kernel
handles while preserving the validated execution behavior.

All 12 blocks completed with finite output and normal teardown.

The final encoder LayerNorm comparison against the FP32 encoder oracle
measured approximately:

| Metric | Result |
| --- | ---: |
| NRMSE | 2.554% |
| Cosine similarity | 0.999674 |
| Finite | True |

These values belong specifically to the tested 64-token real-speech
geometry.

### Current-upstream controlled validation

The application was subsequently validated from a clean current-upstream IRON
checkout using the current pinned mlir-aie stack, without the historical
application-development modifications to the generic AIE2 LayerNorm, GELU, or
Softmax kernels.

The deterministic 128-frame frontend and all 12 encoder blocks completed on
Phoenix/NPU1 with finite outputs and normal teardown. The final encoder
LayerNorm comparison against the canonical FP32 reference measured
approximately:

| Metric | Result |
| --- | ---: |
| NRMSE | 7.99% |
| Cosine similarity | 0.9968 |
| Finite | True |

The numerical difference accumulated with encoder depth. Block-output NRMSE
remained approximately 2.20% through Block 8, then increased to approximately
4.97% at Block 9, 6.57% at Block 10, and 8.00% at Block 11.

Additional exact-input checks were used to distinguish individual operator
accuracy from accumulated model-level error. On the investigated Block-9 MLP
inputs, the current stack measured approximately 0.35% NRMSE for LayerNorm,
0.15% for FC1, 0.45% for GELU, and 0.20% for FC2. A same-input comparison of
the complete Block 9 against a CPU BF16-boundary model measured approximately
0.93% output NRMSE.

A CPU model reproducing the application's visible BF16 operator boundaries
finished at approximately 1.73% NRMSE against the FP32 encoder reference.
This indicates that the larger Phoenix-to-FP32 difference is not explained by
the visible BF16 conversion boundaries alone. The current evidence does not
attribute that accumulated difference to a single generic operator.

These measurements are validation observations for the tested Phoenix/NPU1
configuration, not accuracy guarantees for arbitrary inputs or the canonical
3000-frame Whisper encoder geometry.

## Block-6 numerical investigation

Real speech exposed a sparse region of large absolute activations around
encoder Block 6.

The independent FP32 reference exhibited the same large activation
regime, so the activation magnitude itself was not evidence of Phoenix
corruption.

The investigation captured intermediate tensors through attention and the
MLP to determine where the accumulated discrepancy was amplified.

### Error entering Block 6

At the accumulated Block-6 input:

| Metric | Result |
| --- | ---: |
| Max error | 0.446749 |
| Mean error | 0.006956 |
| RMSE | 0.012489 |
| NRMSE | 1.649% |
| Cosine similarity | 0.999868 |

There were no elements with absolute error greater than 0.5.

### After attention

After the Block-6 attention residual:

| Metric | Result |
| --- | ---: |
| Max error | 0.424551 |
| Mean error | 0.006941 |
| RMSE | 0.010911 |
| NRMSE | 1.452% |
| Cosine similarity | 0.999897 |

The maximum and RMS errors were slightly lower than at block input.
Attention therefore did not produce the large amplification.

### MLP localization

The discrepancy increased in the MLP path:

| Stage | Max error | RMSE |
| --- | ---: | ---: |
| MLP LayerNorm | 0.420604 | 0.031947 |
| FC1 / MLP up | 1.917938 | 0.033527 |
| GELU | 1.690414 | 0.013182 |
| FC2 / MLP down | 11.911743 | 0.107814 |
| Block output | 11.987274 | 0.110622 |

The largest output discrepancies were sparse. The dominant coordinates
were concentrated primarily at tokens 8 and 22 and channels 2 and 452.

For example, FC2 produced values in the hundreds at those coordinates in
both the FP32 reference and Phoenix execution.

The issue was therefore not a broad instability across the tensor.

### Exact-input Block-6 control

To distinguish intrinsic Block-6 error from amplification of upstream
perturbation, Block 6 was rerun independently using the exact canonical
FP32 `block6.input` tensor.

The same Phoenix Block-6 implementation then measured:

| Metric | Accumulated input | Exact FP32 input |
| --- | ---: | ---: |
| Max error | ~11.99 | 0.693359 |
| RMSE | ~0.1106 | 0.005211 |

Supplying the exact input reduced maximum error by roughly 17x and RMSE
by roughly 21x.

This control supports the interpretation that Block 6 is numerically
sensitive and amplifies perturbation already present in its input, rather
than the observed approximately 12-unit absolute discrepancy being caused
by an intrinsic Block-6 implementation failure.

## XRT Python runtime observation

During validation, the native device path and the Python execution path
could fail independently.

`xrt-smi validate` successfully exercised the native XRT/driver/device
path while mlir-aie initially could not create its Python NPU runtime
because the selected `pyxrt` binding was incompatible with the active
Python interpreter.

A compatible XRT Python binding restored:

```text
pyxrt import
    |
    v
mlir-aie XRT runtime
    |
    v
XRTTensor
    |
    v
CachedXRTRuntime
    |
    v
NPU1 / npu1
```

This distinction is useful when debugging the application:

- successful `xrt-smi` validation proves the native driver/device path;
- successful `pyxrt` import and mlir-aie device resolution additionally
  prove the Python/IRON runtime path.

The public application does not contain machine-specific XRT installation
paths.

## Current upstream operator support

The Whisper encoder uses the LayerNorm, GELU, Softmax, and GEMM operators
provided by the current IRON/mlir-aie stack.

Earlier application development required experimental Phoenix/AIE2 changes
while bringing up transformer LayerNorm, signed GELU activations, and stable
attention Softmax behavior. These historical changes are not part of the
current application contribution.

The current upstream stack was independently validated at Whisper-relevant
geometries before running the complete encoder. The tested LayerNorm, GELU,
and Softmax paths completed with finite outputs, including signed GELU
activations and Whisper-sized attention Softmax inputs.

The complete 12-block encoder subsequently executed on the clean current
upstream stack without application-specific modifications to those generic
operators.

## Evidence handling

During development, intermediate FP32 and Phoenix tensors were retained
for stage-level comparison.

Generated compiler products and large research artifacts are not required
in the source tree and are not part of the application contribution.

The public source and documentation intentionally avoid machine-specific
user paths and Hugging Face snapshot identifiers.

## Validated scope

The following are established by this work for the tested Phoenix/NPU1
configuration:

- Whisper-compatible real-WAV preprocessing for the tested input;
- independent Hugging Face preprocessing agreement;
- Phoenix Conv1/GELU/Conv2/GELU frontend execution;
- 64 x 768 real-speech encoder token representation;
- all 12 Whisper-small encoder transformer blocks;
- final encoder LayerNorm;
- finite real-speech encoder outputs;
- stage-level numerical localization of the Block-6 sensitivity.

## Outside the validated scope

The following are not established by this work:

- canonical 3000-frame Whisper execution on Phoenix;
- 1500-token full-length encoder execution;
- Whisper decoder execution;
- decoder causal self-attention;
- encoder-decoder cross-attention;
- KV-cache behavior;
- autoregressive token generation;
- tokenizer/generation integration;
- end-to-end speech transcription;
- arbitrary transformer architectures.

The next implementation boundary is the Whisper decoder.