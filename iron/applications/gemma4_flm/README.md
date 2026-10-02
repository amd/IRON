<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Gemma 4 on IRON operators in FastFlowLM

This example runs the text path of Gemma 4 E2B on IRON operators inside
[FastFlowLM](https://github.com/ROCm/FastFlowLM)'s engine. FastFlowLM
loads the model, tokenizes the prompt and serves the API. Every NPU operator
of the text path is an IRON operator. The engine generates the same tokens as
it does with FastFlowLM's own operators.

## Quick start

You need an NPU2 device (Strix, Krackan) and the IRON environment with an
mlir-aie wheel that contains
[mlir-aie#3818](https://github.com/Xilinx/mlir-aie/pull/3818), the Gemma 4
kernels. FastFlowLM's build needs CMake, Ninja, g++ 13, Rust, Boost, CURL,
FFTW3, FFmpeg, readline and ncurses.

1. Choose the model directory. flm reads the model from
   `$FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2`.

   ```bash
   export FLM_MODEL_PATH=/path/to/flm
   ```

2. Build. `make engine` clones FastFlowLM at a fixed commit, builds the IRON
   operators, and builds flm with an IRON engine and a stock engine.

   ```bash
   make engine
   ```

3. Download the weights, unless the model directory holds them already.

   ```bash
   make weights
   ```

4. Serve the model on the IRON engine, and send it a request.

   ```bash
   make serve
   curl http://127.0.0.1:11434/api/chat -d '{"model": "gemma4-it:e2b", "stream": false,
       "messages": [{"role": "user", "content": "What is 347 + 589?"}]}'
   ```

   The server log names the directory of the IRON operators:

   ```
   [info]  IRON operators from .../build/xclbins/Gemma4-E2B-IT-NPU2/iron
   ```

The test serves a word problem and a 1259-token prompt on both engines. It
checks that the token ids match:

```bash
pytest -m extensive --iterations 1 iron/applications/gemma4_flm
```

The test skips without the model. On a 24-core host, a cold `make engine`
takes about 8 minutes. The IRON build caches its artifacts, and the test then
takes under a minute.

The `Makefile` clones FastFlowLM from
[andrej/FastFlowLM](https://github.com/andrej/FastFlowLM), which adds the
`FLM_OVERRIDE` hooks and the Gemma 4 engine. The pin moves to
[ROCm/FastFlowLM](https://github.com/ROCm/FastFlowLM) once that
repository contains the hooks.

| File | Purpose |
|---|---|
| `build.py` | Builds the IRON operators and stages them for the engine. |
| `pli_weights.py` | Repacks the per-layer-input weights for IRON's GEMM. |
| `overrides.hpp` | Redirects the engine's operator dispatches to the IRON operators. |
| `Makefile` | Builds FastFlowLM's engine with `overrides.hpp` compiled in. |
| `test.py` | Compares the IRON engine's tokens with the stock engine's. |

## IRON operators

An IRON operator is a class in `iron/operators/`. Each operator directory
holds the same files:

- `op.py` defines the operator class, an `MLIROperator`. Its fields describe
  one problem, for example a GEMM's `M`, `K` and `N`. The class declares the
  buffers the operator takes and the artifacts that `op.compile()` builds.
- `design.py` is the IRON program. Workers run kernels on the compute tiles.
  ObjectFifos move data between tiles. The runtime sequence moves data
  between DRAM and the array.
- The kernels are the C++ that runs on one compute tile. These operators take
  their kernels from mlir-aie's kernel factories (`aie.iron.kernels`).
- `reference.py` computes the result on the CPU. `test.py` runs the operator
  on the NPU and compares it with the reference.

`op.compile()` builds two artifacts. The xclbin configures the array: the
tiles, the kernels and the connections. The instruction sequence programs the
data movement of one dispatch. The host loads the xclbin once
and sends the sequence with each dispatch.

A static operator has one fixed instruction sequence, a `.bin` file. A
dynamic operator declares dispatch parameters (`get_dispatch_params()`), for
example the context length. Its sequence depends on their values, so IRON
emits C++ that generates the sequence. The host compiles that generator in
and runs it when the values change.

This example uses six operator classes from `iron/operators/flm/`:

| Operator | Class | Sequence | Engine hooks |
|---|---|---|---|
| [Decode layer](../../operators/flm/layer) | `DecodeLayer` | dynamic: `context_len`, `max_l` | `*_layer_run`, `*_layer`, `*_layer_mv` |
| [Prefill attention](../../operators/flm/prefill_attn) | `PrefillAttention`, `PrefillSlidingAttention` | dynamic: `L_begin`, `L_end`, `max_l` | `global_attn_core`, `swa_attn_core` |
| [LM head](../../operators/flm/lm_head) | `LMHead` | static | `lm_head` |
| [Dequantization](../../operators/flm/dequant) | `DequantBFP` | static, one per (K, N) | `dequant_*` |
| [GEMM](../../operators/flm/gemm) | `GEMM` | static, one per (M, K, N) | `*_proj`, `pli_*_proj` |

- `DecodeLayer` runs one token through one whole layer: norms, projections,
  attention over the KV cache and the MLP. One design spans the whole array.
  Gemma 4 has four layer types. They share one xclbin and differ in the
  instruction sequence.
- `PrefillAttention` and `PrefillSlidingAttention` run causal attention for
  a chunk of prompt tokens. The sliding variant reads only the last 512 keys
  of each query.
- `LMHead` computes the logits of the last token from the 4-bit vocabulary
  weights.
- `DequantBFP` unpacks one layer's 4-bit weights into the block format that
  `GEMM` reads.
- `GEMM` runs every prefill projection: q, k, v, o, the MLP and the
  per-layer-input (PLI) projections. It applies the activation in its output
  stage. All GEMM shapes share one configuration, and therefore one xclbin.

The engine's GEMM converts to bf16 in the floor rounding mode, and rounds
again after each step of gelu. `build.py` constructs every GEMM in one function, `gemm()`, with
`rounding="floor"` and `gelu="bf16_steps"`, which reproduce that arithmetic.

## How FastFlowLM runs the operators

FastFlowLM's Gemma 4 engine marks each operator dispatch with a hook:

```cpp
FLM_OVERRIDE(lm_head, this->lm_head.create_run(this->logits, this->lm_head_weights, this->x))
```

By default the hook expands to its second argument, the engine's own
dispatch. The engine build includes `overrides.hpp`, which redefines
`FLM_OVERRIDE(name, ...)` to expand to `FLM_OV_<name>`. Each `FLM_OV_<name>`
runs the IRON operator on the engine's buffers:

```cpp
#define FLM_OV_lm_head(expr) ::iron::S().lm_head.create_run(this->logits, this->lm_head_weights, this->x)
```

Further arguments after the expression give a hook the values its operator
needs, such as the layer type or the chunk's token range. Three hooks run no
operator. `engine_init` registers the xclbins, `head_weights_loaded` loads
the PLI weights, and `prefill_layer_begin` records the MLP shape of the
layer.

`build.py` writes three things:

- `build/xclbins/Gemma4-E2B-IT-NPU2/` is a copy of the engine's xclbins. The
  IRON xclbins replace `layer`, `attn`, `swa`, `lm_head`, `mm` and `dequant`.
- `build/xclbins/Gemma4-E2B-IT-NPU2/iron/` holds the static instruction
  sequences and the repacked PLI weights. The file names carry the shape, for
  example `gemm_M512_K1536_N2048.bin`.
- `build/gen/` holds the sequence generators of the dynamic operators. The
  engine build compiles them in.

`FLM_XCLBIN_PATH=build` points the engine at the copy. The engine and
`overrides.hpp` register the same xclbin paths, so each IRON operator shares
the engine's hardware context. The device holds 16 hardware contexts, and
the engine registers 10.

The dequantization reads the engine's 4-bit weight buffers in place. The PLI
weights are 16-bit, in the block order of the engine's own GEMM.
`pli_weights.py` reorders them for IRON's GEMM once, at build time.

### Prefill chunks

A GEMM's instruction sequence depends on the number of rows, M. flm splits a
prompt into chunks, and `--prefill-chunk-len 512` limits a chunk to 512
tokens. `build.py` builds a sequence for every row count such a chunk can
have. `CHUNK` in `build.py` sets the limit. A longer limit needs more
sequences and a longer build.
