<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.PrefillAttention`, `iron.operators.flm.PrefillSlidingAttention`

> Note: This operator uses hand-placed and hand-allocated components.
> As a result it is less portable and less idiomatic than most of the other operators
> in this repository. If your goal is to learn IRON operator programming,
> other operators in this repository are likely better examples.

Causal prefill attention from a KV cache. The two operators reproduce
FastFlowLM's prefill attention overlays for Gemma 4:

| Operator | Overlay | Head dim | Keys of the query at position `p` |
|---|---|---|---|
| `PrefillAttention` | global attention | 512 | `0` to `p` |
| `PrefillSlidingAttention` | sliding-window attention | 256 | `p - window + 1` to `p` |

```python
from iron.common.image import OperatorImage
from iron.operators.flm import PrefillAttention, PrefillSlidingAttention

op = PrefillAttention(max_context=32768, num_heads=8, num_kv_heads=1)
# or
op = PrefillSlidingAttention(max_context=32768, num_heads=8, num_kv_heads=1, window=512)
image = OperatorImage(op)
image(o, q, kv, L_begin=0, L_end=2048, max_l=4096)
```

`max_context` and `window` must be multiples of 128.

## Dispatch parameters

One build serves every token range and every cache length up to `max_context`.
The runtime sequence takes three scalars. Each call passes them by keyword, and
the instruction stream is generated for those values:

| Parameter | Meaning |
|---|---|
| `L_begin` | first query token, a multiple of 128 |
| `L_end` | one past the last query token, a multiple of 128 |
| `max_l` | rows of the KV cache, at most `max_context` |

The host refuses a dispatch whose values break these bounds or whose query
range runs past `max_l`, before the array runs.

`max_context` sets the buffer sizes. `max_l` sets the
first row of V in the cache.

## Layout

With `dh` the head dim:

| Buffer | Shape | Rows |
|---|---|---|
| `o` | `(tokens, num_heads, dh)` | token `L_begin` first |
| `q` | `(tokens, num_heads, dh)` | token `L_begin` first |
| `kv` | K `(max_l, num_kv_heads, dh)`, then V of the same shape | token 0 first |

Query head `h` reads KV head `h // (num_heads // num_kv_heads)`. The operator
writes `o` only for `L_end - L_begin` rows.

The scores carry no `1/sqrt(dh)` scale. To apply the scale, multiply `q` by it.

## Numerics

The cores round the scores, the probabilities and the output to bfloat16 and
accumulate in float32. `test.py` compares the output with the float32 reference
in `reference.py`.
