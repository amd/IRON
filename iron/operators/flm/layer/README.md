<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.DecodeLayer`

The operator runs one Gemma 4 decode layer for one token on the whole NPU2
array. It reproduces FastFlowLM's fused decode layer and its runtime sequence.
FastFlowLM's engine can therefore drive it. The kernels come from mlir-aie's
`flm_gemma4_decode_*` factories.

```python
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE
from iron.operators.flm import DecodeLayer

op = DecodeLayer(geometry=FLM_GEMMA4_E2B_DECODE, layer_type="swa", context=ctx)
op.compile()
run = op.get_callable()
run.set_parameters(context_len=37, max_l=4096)
run(x, proj, rms, rope_rms, kv)
```

`geometry` is `FLM_GEMMA4_E2B_DECODE` or `FLM_GEMMA4_E4B_DECODE` from
`aie.iron.kernels`. `layer_type` is one of `global`,
`swa`, `global_skip` and `swa_skip`. A skip layer reads another layer's KV
cache and has no k or v projection.

## One configuration, four sequences

The four layer types configure the device identically. They differ only in
the runtime sequence. FastFlowLM's engine loads one xclbin and switches
between the four sequences from one layer to the next.

## Dispatch parameters

| Parameter | Meaning |
|---|---|
| `context_len` | tokens before this one |
| `max_l` | rows of the KV cache, at most 32768 |

`max_l` sets where V starts in a global layer's cache. A sliding-window
layer's cache is a ring of 512 rows.

## Buffers

The buffers are the engine's, in the order the sequence takes them. The
argument spec gives upper bounds on their sizes.

| Buffer | Holds |
|---|---|
| `x` | the hidden state at offset 0. The layer writes its output over it. The per-layer-input path reads `model_dim` values at `2 * model_dim`. |
| `proj` | the layer's weights, at the offsets that `weight_layout` in `design.py` gives |
| `rms` | the four RMS norm weights |
| `rope_rms` | the RoPE weights (`3 * head_dim`), then the token's per-layer input, its norm weight and `model_dim + 32` values for the up projection |
| `kv` | the K cache, then the V cache. Every layer except a skip layer writes this token's k and v at row `context_len`. |

## Reference

`reference.py` computes the layer in numpy from the five buffers. It
reproduces the kernels' bf16 rounding (toward minus infinity), their fp32
accumulation order, their exp, GELU and reciprocal tables, the fast inverse
square root and the BFP16 attention matmuls. It returns x and the kv cache as
the device leaves them.

FastFlowLM's engine served 20 dispatches as captures: E2B and E4B, all four
layer types, `context_len` 36, 511 and 650. The reference matches the engine
bit for bit on 16 of them. On the other 4, one bf16 output of an RMS norm
differs by 1 ulp, and the MLP spreads the difference over x. The relative L2
error of x is at most 9.8e-4 there. The new K and V rows match bit for bit on
all 20.

## Tests

`test_matches_reference` runs each layer type on synthetic inputs from
`generate_inputs`, on the global layer's xclbin, at `max_l = 1024`. The context
lengths cover a global layer near the start of its cache and deep into it, and
a sliding-window layer before its ring is full, at the wrap and after it. E2B
runs by default. E4B is `extensive`. A dispatch passes when:

- the relative L2 error of x against the reference is at most 1e-2;
- the relative L2 error of the new K and V rows is at most 2e-3;
- the rest of x and of the kv cache equals the input bit for bit.

Synthetic x has no outlier channels. A 1-ulp flip therefore costs more there
than on captured data. Over 80 dispatches per model (8 seeds) the worst error
of x is 5.7e-3 (E2B) and 6.1e-3 (E4B).

`generate_inputs` plants needle rows in the kv cache. A needle key scores 8
with every query head and has its own V row; the other keys score near 0. The
needles sit at the oldest and newest key, at row 0, at the row that the layer
overwrites and at the first row past the keys. A layer that reads a wrong set
of rows therefore changes its output by far more than 1e-2. These bugs, run on
the device, fail the test:

| Bug | Smallest error of x |
|---|---|
| `context_len - 1` or `+ 1` passed to the layer | 0.14 |
| kv rows 0 to 15 read as zero | 0.16 |
| token embedding read as zero | 0.12 |

A non-skip layer that gets a wrong `context_len` also writes a wrong kv row.
The bit-exact check catches that. A sliding-window skip layer with a full ring
(512 or more tokens) reads all 512 rows for any `context_len`. A wrong
`context_len` changes only the order of the rows. Its error stays below 1e-2,
and the test does not catch it.

`test_captured_case` runs captured dispatches when the environment variable
`FLM_LAYER_CASES` names a directory of them. Each dispatch is a directory
with `manifest.json` and the buffers before and after the engine ran it. The
test also requires x and the kv cache to equal the engine's bit for bit.
