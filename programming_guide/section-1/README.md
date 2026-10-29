<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 1 - An Operator on Its Own

`iron/operators/` is the operator library: GEMM, GEMV, MHA, RMSNorm, RoPE,
activations and more, each a declared class. You will usually use them
inside a graph (Section 2), but an operator also works on its own: construct
it, call it with tensors, and it compiles once and runs on the device.

## Walkthrough of [axpy_example.py](./axpy_example.py)

[`AXPY`](../../iron/operators/axpy.py) computes `scalar_factor * a + b`.

```python
from iron.operators import AXPY

op = AXPY(size=2048, num_aie_columns=1, tile_size=2048, scalar_factor=1.5)
```

Construction is keyword-only and does not touch the device. It only
declares the shape and tunables.

* `size` is a `param()`: a dimension of the problem, fixed once the operator
  is made.
* `num_aie_columns` and `tile_size` are `tunable()`s: choices about how the
  work is spread across the array. Set them, as here, or leave them out and
  the operator's `resolve(dev)` picks values for the device.
* `scalar_factor` is also a `param()`. It is compiled into the image rather
  than read from a tensor on each call.

Each operator's docstring says what it computes. Its construction keywords
are what `inspect.signature` (or `cls.declaration.params`) shows.

## Calling it

```python
Tensor = aie_utils.DEFAULT_TENSOR_CLASS
a, b = Tensor(a_np), Tensor(b_np)
y = Tensor(a_np.shape, dtype=a_np.dtype)
op(a, b, y)
result = y.numpy()
```

The first call compiles the design and runs it. Later calls with the same
shape reuse the compiled image.

Called on its own, an operator takes one device tensor per declared buffer,
in order: every input, then every output (`a`, `b`, `y` here; `op.buffers`
lists them). `aie_utils.DEFAULT_TENSOR_CLASS` is the device tensor type of
the current host runtime (`XRTTensor` under XRT). Wrap a numpy array to
upload it, or give a shape and dtype to allocate a buffer for the device to
write. Inside a graph (Section 2) this is different: `Op.step(...)` takes
handles and weights, and the graph returns plain numpy arrays.

## Checking it against numpy

Every operator has `reference(*inputs)`, a numpy computation of what the
device should produce, and `tolerance()`, how close a device run must come
to it. Neither needs an NPU:

```python
from aie.utils.verify import compare

reference = op.reference(a_np, b_np)
verdict = compare(result, reference, op.resolved().tolerance())
assert verdict, verdict.detail
```

Every example in this guide checks its result with `compare(...)`. The
tolerance comes from the kernel's contract, an `aie.utils.verify.Tolerance`
whose `note` explains the bound. For `AXPY` it is one bf16 ulp: the kernel
computes in fp32 and rounds once to bf16 on the store. A `Verdict` is truthy
when the check passes, and `verdict.detail` describes the result either way.

## <u>Exercises</u>

1. Run `python3 axpy_example.py` on an NPU. You should see `PASS!`.
2. Print `op.resolved().tolerance()`, then do the same for a
   [`ReLU`](../../iron/operators/relu.py). `ReLU`'s is `Tolerance.exact()`:
   `max(x, 0)` has nothing to round, while `AXPY`'s multiply-add does.
3. Leave out `num_aie_columns=1` when constructing `op`. `op.num_aie_columns`
   is then `None`, and `op.resolved().num_aie_columns` shows the value
   `resolve(dev)` chose for your device. `op` itself is unchanged.

-----
[Prev](../section-0/) &middot; [Top](..) &middot; [Next](../section-2/)
