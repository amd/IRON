<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 6 - The Host Reference and Check Mode

Every example so far has checked its device result against numpy. IRON
gives you two tools for that:

* `graph.reference(...)` runs the graph on the host. It needs no NPU.
* `compile(check=True)` runs on the NPU and checks each step on its own,
  so a failure names the step that went wrong.

## Walkthrough of [reference_and_check.py](./reference_and_check.py)

```python
class Pipeline(iron.Graph):
    """``silu(x) * y``, two operators as one compiled image."""

    def body(self, x, y):
        return ElementwiseMul.step(SiLU.step(x), y)
```

### `graph.reference(...)`: no NPU

```python
host_reference = graph.reference(x, y)
```

`reference` runs the same `body` your graph records. Each `Op.step(...)`
calls that operator's `reference()` in numpy instead of recording a device
step. A device must be bound (Section 0) so tunables resolve the way they
would on it, but nothing is dispatched. This is the fast loop while you get
a computation right: edit `body`, rerun `reference`, and skip the device
compile.

The example checks `graph.reference` against the same two operators'
`reference()` methods chained by hand. Both sides are the same numpy, so
they must agree exactly.

### A normal device call

```python
graph.compile(x=(2048,), y=(2048,))
result = graph(x, y)
```

This compiles the graph into one image and runs it. Comparing `result`
against a reference tells you whether the whole chain is right, but not
which step is wrong when it isn't.

### `compile(check=True)`: which step

```python
checked = Pipeline()
checked.compile(x=(2048,), y=(2048,), check=True)
checked(x, y)
```

With `check=True`, each step runs as its own dispatch, as an xclbin per
step on NPU1 and NPU2 alike. Before the next step runs, IRON compares the
step's output with its operator's `reference()` on the inputs the device
actually gave it, within that operator's `tolerance()`. The first step
outside its tolerance raises, naming the operator and the step index.

A step whose extent is bounded per call (Section 3) is not checked. IRON
logs a warning for it rather than passing it silently.

Use `check=True` while bringing up a new graph or a new operator inside
one. Once a graph works, compile it normally.

The example ends by comparing the normal call's output with the checked
call's. Both run the same kernels, so they agree exactly.

## <u>Exercises</u>

1. Run `python3 reference_and_check.py` on an attached NPU. It runs all
   three comparisons and prints each one's result.
2. Compare `graph.compile(...).plan.full_elf` with
   `checked.compile(..., check=True).plan.full_elf`, and print
   `plan.report("Pipeline")` for both. On NPU2 the normal compile picks a
   full ELF, and the checked one lists `check=True` as the reason it does
   not.
3. In `reference_and_check.py`, replace the `SiLU` import with `GELU` and
   use `GELU.step(x)` in `Pipeline.body`. Update the hand-written reference
   in `main()` too:

   ```python
   gelu = GELU(size=args.size, num_aie_columns=1, tile_size=args.size)
   mul = ElementwiseMul(size=args.size, num_aie_columns=1, tile_size=args.size)
   by_hand = mul.reference(gelu.reference(x), y)
   ```

   Update `Pipeline`'s docstring to say `gelu(x) * y`, then rerun; all three
   checks should pass. If you change only `body`, the hand-written reference
   still computes SiLU and the first, device-free comparison fails.
   Then print `SiLU`'s and `GELU`'s `.resolved().tolerance()` and read the
   kernel each is built on (`iron/operators/gelu.py`, `silu.py`) to see
   where each number comes from.

-----
[Prev](../section-5/) &middot; [Top](..) &middot; [Next](../section-7/)
