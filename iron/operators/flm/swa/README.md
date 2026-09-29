<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.PrefillSlidingAttention`

Sliding-window causal prefill attention with a head dim of 256, from a KV
cache. A port of FastFlowLM's sliding-window attention overlay for Gemma 4.

```python
from iron.operators.flm import PrefillSlidingAttention

op = PrefillSlidingAttention(
    max_context=32768, num_heads=8, num_kv_heads=1, window=512, context=ctx
)
op.compile()
run = op.get_callable()
run.set_parameters(L_begin=0, L_end=2048, max_l=4096)
run(o, q, kv)
```

## Dispatch parameters

One build serves every token range. The runtime sequence takes three scalars,
and each call generates the instruction stream for the values that
`set_parameters()` last set:

| Parameter | Meaning |
|---|---|
| `L_begin` | first query token, a multiple of 128 |
| `L_end` | one past the last query token, a multiple of 128 |
| `max_l` | rows of the KV cache, at most `max_context` |

`max_context` sizes the buffers in the argument spec. `max_l` sets where V
starts in the cache, so one build serves a cache of any length up to it.

## Layout

| Buffer | Shape | Rows |
|---|---|---|
| `o` | `(tokens, num_heads, 256)` | token `L_begin` first |
| `q` | `(tokens, num_heads, 256)` | token `L_begin` first |
| `kv` | K `(max_l, num_kv_heads, 256)`, then V of the same shape | token 0 first |

Query head `h` reads KV head `h // (num_heads // num_kv_heads)`. The operator
writes `o` only for `L_end - L_begin` rows.

A query at position `p` sees the keys at positions `p - window + 1` to `p`.
`window` must be a multiple of 128.

The scores carry no `1/sqrt(256)` scale. A caller that needs one scales `q`.

## Numerics

The cores round the scores, the probabilities and the output to bfloat16 and
accumulate in float32. Against the float32 reference in `reference.py`, with
outputs of order 1, the mean absolute error is about 0.008 and the largest is
about 0.1.

## The round-count handshake

Each core reads the token range from its RTPs at the start of each pass. After
a dispatch ends, a core starts its next pass at once, before the next dispatch
writes the RTPs. So each core also takes a count from a lock, `go`, before it
reads them. The sequence sets `go` to the number of passes, 2, after it writes
the RTPs.
