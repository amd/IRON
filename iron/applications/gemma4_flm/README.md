<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Gemma 4 on IRON operators in FastFlowLM

This example application demonstrates how to use IRON operators inside the
[FastFlowLM inference engine](https://github.com/ROCm/FastFlowLM) by overriding
its dispatches to the NPU. The FastFlowLM infrastructure loads the model,
tokenizes the prompt and serves the API; every operator on the text path of
Gemma 4 E2B that runs on the NPU is overridden with its open-source IRON
counterpart. The engine generates the same tokens as FastFlowLM without
overrides.

## Quick start

You need an NPU2 device (Strix, Krackan) and the IRON environment.
FastFlowLM's build needs CMake, Ninja, g++ 13, Rust, Boost, CURL, FFTW3,
FFmpeg, readline and ncurses.

1. Choose the model directory. flm reads the model from
   `$FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2`.

   ```bash
   export FLM_MODEL_PATH=/path/to/flm
   ```

2. Download the weights. `make weights` clones FastFlowLM at a fixed commit,
   builds flm and pulls the model. It skips the pull if the model directory
   holds `model.q4nx`.

   ```bash
   make weights
   ```

3. Build. `make engine` builds the IRON operators from the downloaded model,
   and then FastFlowLM's Gemma 4 engine with `overrides.hpp` compiled in.

   ```bash
   make engine
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

The `Makefile` clones FastFlowLM from
[andrej/FastFlowLM](https://github.com/andrej/FastFlowLM), which adds the
`FLM_OVERRIDE` hooks and the Gemma 4 engine.

| File | Purpose |
|---|---|
| `build.py` | Builds the IRON operators and stages them for the engine. |
| `pli_weights.py` | Repacks the per-layer-input weights for IRON's GEMM. |
| `overrides.hpp` | Redirects the engine's operator dispatches to the IRON operators. |
| `Makefile` | Builds FastFlowLM's engine with `overrides.hpp` compiled in. |
| `test.py` | Compares the IRON engine's tokens with the stock engine's. |

## IRON operators

This example uses six operator classes from `iron/operators/flm/`:

| Operator | Class | Abstraction level | Sequence | Engine hooks |
|---|---|---|---|---|
| [GEMM](../../operators/flm/gemm) | `GEMM` | high | static, one per (M, K, N) | `*_proj`, `pli_*_proj` |
| [Dequantization](../../operators/flm/dequant) | `DequantBFP` | high | static, one per (K, N) | `dequant_*` |
| [LM head](../../operators/flm/lm_head) | `LMHead` | high | static | `lm_head` |
| [Prefill attention](../../operators/flm/prefill_attn) | `PrefillAttention`, `PrefillSlidingAttention` | low | dynamic: `L_begin`, `L_end`, `max_l` | `global_attn_core`, `swa_attn_core` |
| [Decode layer](../../operators/flm/layer) | `DecodeLayer` | low | dynamic: `context_len`, `max_l` | `*_layer_run`, `*_layer`, `*_layer_mv` |

The high-level operators describe their dataflow with IRON's Workers,
ObjectFifos and runtime sequence:

- `GEMM` runs every prefill projection: q, k, v, o, the MLP and the
  per-layer-input (PLI) projections. It applies the activation in its output
  stage. All GEMM shapes share one configuration, and therefore one xclbin.
- `DequantBFP` unpacks one layer's 4-bit weights into the block format that
  `GEMM` reads.
- `LMHead` computes the logits of the last token from the 4-bit vocabulary
  weights.

The low-level operators are ports of FastFlowLM's designs. Their designs
also place locks, tile DMAs, flows and shim buffer descriptors by hand. They
are not yet fully ported to IRON's high-level abstractions:

- `PrefillAttention` and `PrefillSlidingAttention` run causal attention for
  a chunk of prompt tokens. The sliding variant reads only the last 512 keys
  of each query.
- `DecodeLayer` runs one token through one whole layer: norms, projections,
  attention over the KV cache and the MLP. One design spans the whole array.
  Gemma 4 has four layer types. They share one xclbin and differ in the
  instruction sequence.

Each of these operators is an IRON operator. Its directory holds these files:

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

`op.compile()` generates the operator's artifacts: an xclbin and an
instruction sequence. `build.py` overwrites the engine's xclbins with IRON's
xclbins, and the override hooks dispatch IRON's instruction sequences.

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

`build.py` writes four things:

- `build/ops/` holds IRON's build artifacts of every operator.
- `build/xclbins/Gemma4-E2B-IT-NPU2/` is the engine's xclbin directory, with
  six xclbins replaced by IRON's builds: `layer`, `attn`, `swa`, `lm_head`,
  `mm` and `dequant`. The server log line
  `IRON operators from .../build/xclbins/Gemma4-E2B-IT-NPU2/iron` confirms
  that the engine loads its xclbins from this directory.
- `build/xclbins/Gemma4-E2B-IT-NPU2/iron/` holds the static instruction
  sequences and the repacked PLI weights. The file names carry the shape, for
  example `gemm_M512_K1536_N2048.bin`.
- `build/gen/` holds the sequence generators of the dynamic operators. The
  engine build compiles them in.

`FLM_XCLBIN_PATH=build` points the engine at the IRON-compiled operators.
