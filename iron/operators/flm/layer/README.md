<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.DecodeLayer`

> Note: This operator uses hand-placed and hand-allocated components.
> As a result it is less portable and less idiomatic than most of the other operators 
> in this repository. If your goal is to learn IRON operator programming,
> other operators are likely better examples.

The operator runs one Gemma 4 decoder layer for one token on the whole NPU2
array. It reproduces FastFlowLM's fused decode layer and its runtime sequence.
The kernels come from mlir-aie's `flm_gemma4_decode_*` factories.

```python
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE
from iron.common.image import OperatorImage
from iron.operators.flm import DecodeLayer

image = OperatorImage(DecodeLayer(geometry=FLM_GEMMA4_E2B_DECODE, layer_type="swa"))
image(x, proj, rms, rope_rms, kv, context_len=37, max_l=4096)
```

`geometry` is `FLM_GEMMA4_E2B_DECODE` or `FLM_GEMMA4_E4B_DECODE` from
`aie.iron.kernels`. `layer_type` is one of `global`, `swa`, `global_skip` and
`swa_skip`.

## Layer types

Gemma 4 has two kinds of attention layer:

- A `global` layer attends to every earlier token. Its KV cache holds
  `max_l` rows. Its head dim is `geometry.dh`.
- An `swa` layer (sliding-window attention) attends to the last 512 tokens
  only. Its KV cache is a ring of 512 rows. Its head dim is
  `geometry.swa_dh`.

Gemma 4 shares KV caches between layers. A skip layer, `global_skip` or
`swa_skip`, reads the KV cache of an earlier layer of the same kind. It has
no k or v projection and writes no cache row. If `geometry.double_wide_mlp`
is set, a skip layer has twice the intermediate size.

The four layer types configure the device identically. They differ only in
the runtime sequence. One xclbin, the `global` layer's, therefore runs all
four.

## What the layer computes

The operator computes one decoder layer of one decode step: the layer's
output hidden state for one token. It does not compute the embedding lookup,
the final norm or the LM head.

1. Attention. The layer applies an RMS norm to the hidden state h and
   projects it to q, k and v. It applies a per-head RMS norm and RoPE to q
   and k, and an RMS norm without weight to v. A non-skip layer writes k and
   v into the KV cache. q attends to the cached keys. The o projection and an
   RMS norm follow. A residual adds the result to h.
2. MLP. An RMS norm, the up and gate projections, `GELU(gate) * up`, the
   down projection and an RMS norm follow. A residual adds the result.
3. Per-layer input. The layer projects the token embedding to `pli_d`
   values and scales them. It applies an RMS norm, adds the token's
   per-layer embedding and scales the sum. GELU of a projection of the hidden state multiplies the
   result. An up projection and an RMS norm follow. A residual adds the
   result.
4. The layer multiplies the hidden state by the layer scale.

The weights of the attention and the MLP are q4nx. The per-layer-input
weights are bf16. The activations are bf16. The cores accumulate in fp32.
The attention matmuls run on bfp16 operands.

## Dispatch parameters

| Parameter | Meaning |
|---|---|
| `context_len` | tokens before this one |
| `max_l` | rows of the KV cache, at most 32768 |

`max_l` sets where V starts in a global layer's cache. A sliding-window
layer's cache is a ring of 512 rows. The host refuses a dispatch with a
negative `context_len`, a `max_l` above 32768 or, in a global layer, a
`context_len` of `max_l` or more.

## Buffers

The design expects these buffers, in this order. The operator's buffer sizes
(`arg_sizes` in `design.py`) are upper bounds on what a layer reads.

| Buffer | Holds |
|---|---|
| `x` | the hidden state at offset 0. The layer writes its output over it. The per-layer-input path reads the token embedding, `model_dim` values at `2 * model_dim`. |
| `proj` | the layer's weights, at the offsets that `weight_layout` in `design.py` gives |
| `rms` | the four RMS norm weights |
| `rope_rms` | the cos and sin of the token's position and the q and k norm weights (`3 * head_dim`), then the token's per-layer embedding, its norm weight and `model_dim + 32` values for the up projection |
| `kv` | the K cache, then the V cache. Every layer except a skip layer writes this token's k and v at row `context_len`. |

## Reference

`reference.py` computes the same output in numpy from the five buffers. It
models the kernels' rounding, accumulation order and lookup tables with
`aie2p_math_emulation.py`. It returns x and the kv cache as the device leaves
them.

## Tests

The tests run the layer on synthetic inputs and compare x and the kv cache
with the reference. Uniformly random inputs lack the features of real
inputs: a few channels with large values, and attention that puts most of
its weight on a few keys. On uniformly random inputs, the error of a layer
that reads the wrong cache rows stays close to the rounding error. A
comparison cannot separate such a bug from rounding error.

`generate_inputs` therefore plants needles in the KV cache. A needle is a
cache row whose key scores high against the query and whose value row is
distinct. The needles sit at the oldest and the newest key, at row 0, at the
row that the layer writes and at the first row past the keys. A layer that reads one row too many, one too
few or a wrong row changes its attention output by a large fraction.
A sliding-window skip layer with a full ring reads all 512 rows for any
`context_len`. A wrong `context_len` changes only the order of the rows, and
the test does not detect it.

`test_captured_case` runs dispatches captured from FastFlowLM's engine when
the environment variable `FLM_LAYER_CASES` names a directory of them. It
also requires x and the kv cache to equal the engine's bit for bit.
