<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Replace Gemma 4 GEMM and dequant in FastFlowLM engine

This example replaces two operators in the FastFlowLM engine's Gemma 4 E2B
prefill path:

- dequant converts the model's q4nx weights to bfp16;
- GEMM runs the attention and MLP projections with those bfp16 weights.

The rest of the model uses the original FastFlowLM operators.

You need an NPU2 device, an IRON environment, the
[FastFlowLM build dependencies],
and Gemma 4 E2B weights. The commands below run from this directory.

[FastFlowLM build dependencies]: https://github.com/ROCm/FastFlowLM/blob/main/docs/linux-getting-started.md#building-from-source

## Build the FastFlowLM inference engine

We will be using the following paths throughout:

```bash
export IRON=$(git rev-parse --show-toplevel)
export APP=$IRON/iron/applications/gemma4_flm
export BUILD=$APP/build
export OUTPUT=$BUILD/gemm_dequant
export FLM=$BUILD/FastFlowLM/src
export FLM_MODEL_PATH=/path/to/fastflowlm-models-dir
```

`FLM_MODEL_PATH` must point to the parent of the `models` directory that
contains the Gemma 4 weights. FastFlowLM appends `/models` to the path. The
steps below explain how to download the weights if you do not have them.

Pull and build the unmodified ("stock") FastFlowLM engine for comparison:

```bash
git clone https://github.com/ROCm/FastFlowLM $BUILD/FastFlowLM
git -C $BUILD/FastFlowLM checkout v1.0.8
git -C $BUILD/FastFlowLM submodule update --init --recursive

cmake -S $FLM -B $BUILD/stock -G Ninja \
    -DFLM_VERSION=1.0.8 -DNPU_VERSION=32.0.203.304 \
    -DFLM_BUILD_GEMMA4E=ON
cmake --build $BUILD/stock --parallel 2
```

If the weights are absent from `$FLM_MODEL_PATH/models`, download them with the
engine you just built:

```bash
cd $FLM
FLM_MODELINFO_PATH=$FLM/model_info.json \
    $BUILD/stock/flm pull gemma4-it:e2b
```

## Build the replacement IRON operators

Now build the NPU programs for the operators you want to replace.
`build_gemm_dequant.py` compiles the Gemma 4 E2B shapes and creates a copy of
FastFlowLM's xclbin directory under `$OUTPUT/xclbins`. It replaces only
`mm.xclbin` and `dequant.xclbin`. The instruction streams go in the adjacent
`iron/` directory.

```bash
cd $APP
python3 build_gemm_dequant.py $FLM/xclbins $OUTPUT
```

The script builds the GEMM row counts needed by `--prefill-chunk-len 512`.
Increase `CHUNK` in `build_gemm_dequant.py` to serve larger chunks.

## The override header

Next, build a modified FastFlowLM engine that runs the IRON operators instead
of the built-in stock operators.
[`gemm_dequant_overrides.hpp`](gemm_dequant_overrides.hpp) is the source header
that defines these replacements.

In the FastFlowLM source code, dispatches use `FLM_OVERRIDE` like this:

```cpp
FLM_OVERRIDE(q_swa_proj, q_swa_proj(out, in, weights), desc, type, shape)
```

This makes each dispatch overridable. Without an override header,
`FLM_OVERRIDE` evaluates the second argument. This example's header redefines
the macro so that the operator name selects another macro:

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
that IRON GEMM reads, so select both together.

To experiment with another operator, add its `FLM_OV_<name>` macro and preserve
the exact result type and buffer lifetime of the expression it replaces.

## Rebuild the engine

Recompile the FastFlowLM engine with the overrides. The nested quotes make
`FLM_OVERRIDES` a C++ include string.

```bash
OVERRIDE_FLAGS="-I$APP -DFLM_OVERRIDES=\"\\\"gemm_dequant_overrides.hpp\\\"\""
cmake -S $FLM -B $OUTPUT/engine -G Ninja \
    -DFLM_VERSION=1.0.8 -DNPU_VERSION=32.0.203.304 \
    -DFLM_BUILD_GEMMA4E=ON \
    "-DFLM_OVERRIDE_FLAGS=$OVERRIDE_FLAGS"
cmake --build $OUTPUT/engine --target gemma4e_npu --parallel 2
```

Edit the header and rerun the last command to test another implementation.

## Compare the selections

Run the stock FastFlowLM engine:

```bash
cd $FLM
LD_LIBRARY_PATH=$BUILD/stock/engines FLM_XCLBIN_PATH=$FLM \
    $BUILD/stock/flm serve gemma4-it:e2b \
    --prefill-chunk-len 512 --port 11434
```

Run the engine with IRON-replaced GEMM/dequant on another port:

```bash
cd $FLM
LD_LIBRARY_PATH=$OUTPUT/engine/engines FLM_XCLBIN_PATH=$OUTPUT \
    $BUILD/stock/flm serve gemma4-it:e2b \
    --prefill-chunk-len 512 --port 11435
```

Send the same request to each port:

```bash
# Test stock:
REQUEST='{
  "model": "gemma4-it:e2b",
  "prompt": "Explain block floating point in two sentences.",
  "stream": false,
  "max_tokens": 64
}'
curl -s http://127.0.0.1:11434/api/generate -d \
    "$REQUEST"

# Test IRON-overridden:
curl -s http://127.0.0.1:11435/api/generate -d \
    "$REQUEST"
```

Compare `context` for token IDs and `prompt_eval_duration` for prefill time.
The duration is in nanoseconds. Discard the first request as a warm-up, then
use the median of several requests.

The Python test performs these steps. Run it from the repository root. It
builds both selections and compares their token IDs:

```bash
pytest --iterations 1 iron/applications/gemma4_flm/gemm_dequant
```
