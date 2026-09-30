<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.PrefillAttention`, `iron.operators.flm.PrefillSlidingAttention`

Causal prefill attention from a KV cache. The two operators reproduce
FastFlowLM's prefill attention overlays for Gemma 4:

| Operator | Overlay | Head dim | Keys a query at position `p` sees |
|---|---|---|---|
| `PrefillAttention` | global attention | 512 | `0` to `p` |
| `PrefillSlidingAttention` | sliding-window attention | 256 | `p - window + 1` to `p` |

```python
from iron.operators.flm import PrefillAttention, PrefillSlidingAttention

op = PrefillAttention(max_context=32768, num_heads=8, num_kv_heads=1, context=ctx)
# or
op = PrefillSlidingAttention(
    max_context=32768, num_heads=8, num_kv_heads=1, window=512, context=ctx
)
op.compile()
run = op.get_callable()
run.set_parameters(L_begin=0, L_end=2048, max_l=4096)
run(o, q, kv)
```

`max_context` and `window` must be multiples of 128.

## Dispatch parameters

One build serves every token range. The runtime sequence takes three scalars.
Each call generates the instruction stream for the values of the last
`set_parameters()`:

| Parameter | Meaning |
|---|---|
| `L_begin` | first query token, a multiple of 128 |
| `L_end` | one past the last query token, a multiple of 128 |
| `max_l` | rows of the KV cache, at most `max_context` |

`max_context` sizes the buffers in the argument spec. `max_l` sets where V
starts in the cache, so one build serves a cache of any length up to it.

## Layout

With `dh` the head dim:

| Buffer | Shape | Rows |
|---|---|---|
| `o` | `(tokens, num_heads, dh)` | token `L_begin` first |
| `q` | `(tokens, num_heads, dh)` | token `L_begin` first |
| `kv` | K `(max_l, num_kv_heads, dh)`, then V of the same shape | token 0 first |

Query head `h` reads KV head `h // (num_heads // num_kv_heads)`. The operator
writes `o` only for `L_end - L_begin` rows.

The scores carry no `1/sqrt(dh)` scale. A caller that needs one scales `q`.

## Numerics

The cores round the scores, the probabilities and the output to bfloat16 and
accumulate in float32. Against the float32 reference in `reference.py`, with
outputs of order 1:

| Operator | Mean absolute error | Largest |
|---|---|---|
| `PrefillAttention` | about 0.009 | about 0.15 |
| `PrefillSlidingAttention` | about 0.008 | about 0.1 |
