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
from iron.operators.flm import DecodeLayer

op = DecodeLayer(model="GEMMA4_E2B", layer_type="swa", context=ctx)
op.compile()
run = op.get_callable()
run.set_parameters(context_len=37, max_l=4096)
run(x, proj, rms, rope_rms, kv)
```

`model` is `GEMMA4_E2B` or `GEMMA4_E4B`. `layer_type` is one of `global`,
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
