<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 1 - An Operator on Its Own

`iron/operators/` is the operator library: GEMM, GEMV, MHA, RMSNorm, RoPE,
activations and more, each one declared class. Most of the time you'll reach
them through a graph (Section 2), but an operator also stands on its own:
construct it, call it with tensors, and it compiles once and runs on the
device, no `iron.Graph` required.

## Walkthrough of [axpy_example.py](./axpy_example.py)

[`AXPY`](../../iron/operators/axpy.py) computes `scalar_factor * a + b`.

```python
from iron.operators import AXPY

op = AXPY(size=2048, num_aie_columns=1, tile_size=2048, scalar_factor=1.5)
```

Construction is keyword-only, and it never touches the device: it only
declares the shape and tunables.

* `size` is a `param()`: a dimension of the problem, fixed once the operator
  is made.
* `num_aie_columns` and `tile_size` are `tunable()`s: a value for how the
  work is spread across the array. Give one explicitly, as here, or leave it
  out and `Operator.resolve(dev)` picks one for the bound device.
* `scalar_factor` is a `param()` too, baked into the compiled image, not read
  from a tensor at every call.

Every operator's docstring says what it computes; its construction keywords
are the fields `inspect.signature` (or `cls.declaration.params`) shows.

## Calling it

```python
Tensor = aie_utils.DEFAULT_TENSOR_CLASS
a, b = Tensor(a_np), Tensor(b_np)
y = Tensor(a_np.shape, dtype=a_np.dtype)
op(a, b, y)
result = y.numpy()
```

The first call with this shape compiles the design and runs it; a later call
with tensors of the same shape reuses the compiled image. Outside a graph, a
call takes one device tensor per declared buffer, in order — every input,
then every output (`a`, `b`, `y` here; `AXPY.buffers` names them) — not
plain numpy arrays and not only the inputs. `aie_utils.DEFAULT_TENSOR_CLASS`
is the device tensor type the current host runtime uses (`XRTTensor` under
XRT); wrap an existing array to upload it, or give a shape and dtype to
allocate one the device writes into. Calling an operator *inside* a graph
(Section 2) is different: `Op.step(...)` takes handles and plain numpy
weights, and a graph's own output comes back as a plain array — the
device-tensor wrapping here is particular to running one operator alone.

## Checking it against numpy

Every operator defines `reference(*inputs)`, a plain numpy computation of
what the device is meant to produce, and `tolerance()`, how close a real
device run must come to it — neither needs an NPU to call:

```python
from aie.utils.verify import compare

reference = op.reference(a_np, b_np)
verdict = compare(result, reference, op.resolved().tolerance())
assert verdict, verdict.detail
```

`compare(...)` is what checks a result against a reference everywhere in
this guide, never a hand-picked number: `AXPY`'s is "fp32 compute, one bf16
rounding on the store", one ulp — read `op.resolved().tolerance()` yourself
and you'll see the exact `Tolerance` (`aie.utils.verify.Tolerance`) the
kernel's contract declares, with a `note` saying where the bound comes from.
A `Verdict` is truthy when the comparison passed, and `verdict.detail` says
why not when it didn't — `assert verdict, verdict.detail` reads either way.

## <u>Exercises</u>

1. Run `python3 axpy_example.py` on an attached NPU; you should see `PASS!`.
2. Print `op.resolved().tolerance()` and compare it to
   [`ReLU`](../../iron/operators/relu.py)'s (construct one, `op.resolved().tolerance()`
   again) — `ReLU`'s is `Tolerance.exact()`: a selection has nothing to
   round, where `AXPY`'s multiply-add does.
3. Drop `num_aie_columns=1` from the construction (it is still `None` on
   `op`) and print `op.resolved().num_aie_columns`: `resolve(dev)` filled it
   in for the attached device without changing `op` itself.

-----
[Prev](../section-0/) &middot; [Top](..) &middot; [Next](../section-2/)
