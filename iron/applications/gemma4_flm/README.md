<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Gemma 4 on IRON operators in FastFlowLM

This example application demonstrates how to use IRON operators inside the
[FastFlowLM inference engine](https://github.com/ROCm/FastFlowLM) to build the
Gemma 4 model from open source code. The FastFlowLM infrastructure loads the
model, tokenizes the prompt and serves the API; this repository provides the
operators that run on the NPU on the text path of Gemma 4 E2B.

## Quick start

You need an NPU2 device (Strix, Krackan) and the IRON environment, see the
[IRON installation instructions](../../../README.md#installation-linux) (in
short, `pip install -r requirements.txt`). The `Makefile` pulls and builds the
FastFlowLM engine, with its operators replaced by their open-source
implementations from this repository. The build needs FastFlowLM's
[documented prerequisites](https://github.com/ROCm/FastFlowLM/blob/main/docs/linux-getting-started.md#building-from-source),
and in addition Boost, CURL, FFTW3, readline, ncurses and Rust 1.80 or newer.
On Ubuntu 24.04, whose default Rust is 1.75, install them with:

```bash
sudo apt install cmake ninja-build pkg-config uuid-dev libdrm-dev libxrt-dev \
    libavformat-dev libavcodec-dev libavutil-dev libswscale-dev libswresample-dev \
    libboost-dev libboost-filesystem-dev libboost-program-options-dev \
    libcurl4-openssl-dev libfftw3-dev libreadline-dev libncurses-dev \
    cargo-1.85 rustc-1.85
export PATH=/usr/lib/rust-1.85/bin:$PATH
```

Run the steps below from this directory, `iron/applications/gemma4_flm`.

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

4. Serve the model on the IRON engine.
   `--prefill-chunk-len 512` is required: the IRON operators are built for
   prompt chunks of up to 512 tokens.

   ```bash
   cd build/FastFlowLM/src
   LD_LIBRARY_PATH=../../engine/engines FLM_XCLBIN_PATH=../.. \
       ./build/flm serve gemma4-it:e2b --prefill-chunk-len 512 --port 11434
   ```

   Send it a request from another terminal:

   ```bash
   curl http://127.0.0.1:11434/api/chat -d '{"model": "gemma4-it:e2b", "stream": false,
       "messages": [{"role": "user", "content": "What is 347 + 589?"}]}'
   ```

   Check the server log to confirm you are using the IRON operators:

   ```
   [info]  IRON operators from .../build/xclbins/Gemma4-E2B-IT-NPU2/iron
   ```

   Alternatively, for an interactive chatbot in your command line:

   ```bash
   cd build/FastFlowLM/src
   LD_LIBRARY_PATH=../../engine/engines FLM_XCLBIN_PATH=../.. \
       ./build/flm run gemma4-it:e2b --prefill-chunk-len 512
   ```

The test serves a word problem and a 1259-token prompt on both engines. It
checks that the token ids match. Run it from the repository root:

```bash
pytest --iterations 1 iron/applications/gemma4_flm
```

The `Makefile` clones FastFlowLM at the commit of
[ROCm/FastFlowLM#763](https://github.com/ROCm/FastFlowLM/pull/763), which adds
the `FLM_OVERRIDE` hooks and the Gemma 4 engine.

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
ObjectFifos and runtime sequence. Alongside the other operators in IRON, these
are good examples of idiomatic IRON code:

- `GEMM` runs every prefill projection: q, k, v, o, the MLP and the
  per-layer-input (PLI) projections. It applies the activation in its output
  stage. All GEMM shapes share one configuration, and therefore one xclbin.
- `DequantBFP` unpacks one layer's 4-bit weights into the block format that
  `GEMM` reads.
- `LMHead` computes the logits of the last token from the 4-bit vocabulary
  weights.

The low-level operators are less portable and less idiomatic than the
operators above. These low-level designs place locks, tile DMAs, flows and shim
buffer descriptors by hand:

- `PrefillAttention` and `PrefillSlidingAttention` run causal attention for
  a chunk of prompt tokens.
- `DecodeLayer` runs one token through one whole layer: norms, projections,
  attention over the KV cache and the MLP.

Each of these operators is an IRON operator. Each operator consists of:

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
