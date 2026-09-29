<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# `iron.operators.flm.LMHead`

Gemma 4's softcapped logits from a q4nx vocabulary, with the RMS norm folded
in.

```python
from iron.operators.flm import LMHead

op = LMHead(dim=1536, vocab=262144, softcap=30.0, context=ctx)
op.compile()
op.get_callable()(y, w, x)
```

`x` holds the token, then its RMS weight: `2 * dim` bf16. `w` is the
vocabulary as q4nx blocks of 32 out-features by 256 in-features, in the order
`reference.dequantize` documents. `y` receives `vocab` bf16 logits,
`c * tanh(logit / c)` for the softcap `c`.

## Numerics

Against the float64 reference in `reference.py`:

- The cores normalize the token in bf16. They narrow each 32-column dot
  product and the logits to bf16. On the test inputs, the error reaches 1.4%
  of the largest logit.
- AIE2P's `tanh` approximation errs by up to 0.038 absolute, near 0.5. The
  softcap multiplies that error by the cap: up to about 1.1 at Gemma 4's cap of
  30. FastFlowLM's kernel computes the softcap the same way.
