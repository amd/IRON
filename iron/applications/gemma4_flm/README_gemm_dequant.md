<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Replace Gemma 4 GEMM and dequant in FastFlowLM

This example replaces two operators in FastFlowLM's Gemma 4 E2B prefill path:

- dequant converts the model's q4nx weights to bfp16;
- GEMM runs the attention and MLP projections with those bfp16 weights.

The rest of the model uses FastFlowLM's operators. This gives two useful
selections to compare: the FastFlowLM engine and the same engine with the IRON
GEMM/dequant pair.

You need an NPU2 device, an IRON environment, the
[FastFlowLM build dependencies](https://github.com/ROCm/FastFlowLM/blob/main/docs/linux-getting-started.md#building-from-source),
and Gemma 4 E2B weights. The commands below run from this directory.

## Build FastFlowLM

Set the paths first. `FLM_MODEL_PATH` names the directory above `models/`, not
the model directory itself.

```bash
export IRON=$(git rev-parse --show-toplevel)
export APP=$IRON/iron/applications/gemma4_flm
export BUILD=$APP/build
export OUTPUT=$BUILD/gemm_dequant
export FLM=$BUILD/FastFlowLM/src
export FLM_MODEL_PATH=/path/to/fastflowlm

git clone https://github.com/ROCm/FastFlowLM $BUILD/FastFlowLM
git -C $BUILD/FastFlowLM checkout 95f455e7ca39a2088b8a457dc44af10ecb3c2b40
git -C $BUILD/FastFlowLM submodule update --init --recursive

cmake -S $FLM -B $BUILD/stock -G Ninja \
    -DFLM_VERSION=1.0.5 -DNPU_VERSION=32.0.203.304 \
    -DFLM_BUILD_GEMMA4E=ON
cmake --build $BUILD/stock --parallel 2
```

If the model is not present, download it with the engine:

```bash
cd $FLM
FLM_MODELINFO_PATH=$FLM/model_info.json \
    $BUILD/stock/flm pull gemma4-it:e2b
```

FastFlowLM reads
`$FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2/model.q4nx`.

## Build the replacement operators

`build_gemm_dequant.py` compiles the Gemma 4 E2B shapes and creates a copy of
FastFlowLM's xclbin directory under `$OUTPUT/xclbins`. It replaces only `mm.xclbin` and
`dequant.xclbin`. The instruction streams go in the adjacent `iron/` directory.

```bash
cd $APP
python3 build_gemm_dequant.py $FLM/xclbins $OUTPUT
```

The script builds the GEMM row counts needed by `--prefill-chunk-len 512`.
Increase `CHUNK` in `build_gemm_dequant.py` to serve larger chunks.

## The override header

[`gemm_dequant_overrides.hpp`](gemm_dequant_overrides.hpp) is a source header,
not a library or a runtime plugin. FastFlowLM includes `flm_override.hpp` at its
operator call sites. The build definition below makes that file include this
header in every Gemma engine translation unit.

FastFlowLM writes a dispatch like this:

```cpp
FLM_OVERRIDE(q_swa_proj, q_swa_proj(out, in, weights), desc, type, shape)
```

Without an override header, `FLM_OVERRIDE` evaluates the second argument. This
header redefines the macro so that the operator name selects another macro:

```cpp
#define FLM_OVERRIDE(name, expr, ...) \
    FLM_OV_##name(expr __VA_OPT__(, ) __VA_ARGS__)

#define FLM_OV_q_swa_proj(expr, desc, type, shape) \
    ::iron::q_proj((desc)->weight_desc(type), shape, bufs, qkv_weights)
```

The replacement macro runs the IRON operator on the buffers at that call site.
The header marks the hooks it replaces. Its generic fallback evaluates `expr`
for every unmarked hook, so unused hooks need no definitions. This header marks
only projection GEMM, dequant, and the setup hooks they require.

GEMM and dequant form one replacement set. IRON dequant writes the bfp16 layout
that IRON GEMM reads, so select both together. To experiment with another
operator, add its `FLM_OV_<name>` macro and preserve the exact result type and
buffer lifetime of the expression it replaces.

## Rebuild the engine

Compile the header into the source-built Gemma engine. The nested quotes make
`FLM_OVERRIDES` a C++ include string.

```bash
OVERRIDE_FLAGS="-I$APP -DFLM_OVERRIDES=\"\\\"gemm_dequant_overrides.hpp\\\"\""
cmake -S $FLM -B $OUTPUT/engine -G Ninja \
    -DFLM_VERSION=1.0.5 -DNPU_VERSION=32.0.203.304 \
    -DFLM_BUILD_GEMMA4E=ON \
    "-DFLM_OVERRIDE_FLAGS=$OVERRIDE_FLAGS"
cmake --build $OUTPUT/engine --target gemma4e_npu --parallel 2
```

Edit the header and rerun the last command to test another implementation.

## Compare the selections

Run the FastFlowLM selection:

```bash
cd $FLM
LD_LIBRARY_PATH=$BUILD/stock/engines FLM_XCLBIN_PATH=$FLM \
    $BUILD/stock/flm serve gemma4-it:e2b \
    --prefill-chunk-len 512 --port 11434
```

Run the IRON GEMM/dequant selection on another port:

```bash
cd $FLM
LD_LIBRARY_PATH=$OUTPUT/engine/engines FLM_XCLBIN_PATH=$OUTPUT \
    $BUILD/stock/flm serve gemma4-it:e2b \
    --prefill-chunk-len 512 --port 11435
```

Send the same request to each port:

```bash
curl -s http://127.0.0.1:11434/api/generate -d \
  '{"model":"gemma4-it:e2b","prompt":"Explain block floating point in two sentences.","stream":false,"max_tokens":64}'
```

Compare `context` for token IDs and `prompt_eval_duration` for prefill time.
The duration is in nanoseconds. Discard the first request, then use the median
of several requests. The IRON pair trades FastFlowLM's shipped implementation
for operator source that you can change and rebuild independently.

The focused test builds both selections and compares their token IDs:

```bash
pytest --iterations 1 iron/applications/gemma4_flm/gemm_dequant
```
