<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 6 - The Host Reference and Check Mode

Every example so far has checked its device result against numpy. This
section is about the two mechanisms behind that, and when to reach for
each: `graph.reference(...)`, which needs no NPU at all, and
`compile(check=True)`, which does, and tells you which *step* went wrong
rather than only the graph's final answer.

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

`reference` runs the exact same `body` your graph records, but each
`Op.step(...)` calls that operator's own `reference()` on the host instead
of recording a device step. It needs a device only to be *bound* (Section
0), so tunables resolve the same way they would on it; nothing is
dispatched. This is the fast loop: changing `body`, rerunning `reference`,
rather than waiting on a device compile, while you get the computation
right.

### A normal device call

```python
graph.compile(x=(2048,), y=(2048,))
result = graph(x, y)
```

As in every earlier section, this checks the *whole graph's* output against
the reference. If it's outside tolerance, you know something in the chain
is wrong, but not which step.

### `compile(check=True)`: which step

```python
checked = Pipeline()
checked.compile(x=(2048,), y=(2048,), check=True)
checked(x, y)
```

`check=True` dispatches each step of the graph on its own, in NPU1's
natural packaging (an xclbin per step, forced even on NPU2 where a graph
would otherwise share one full ELF — see [Section 7](../section-7/)), and
compares each step's device output to *its own* operator's `reference()`
before the next step runs. The first step outside its `tolerance()` raises
there, naming the operator and the step, rather than only showing a wrong
final answer three operators downstream of the real problem. Reach for it
while bringing up a new graph or a new operator inside one; a graph already
known to work runs its normal, usually faster, packaging.

## <u>Exercises</u>

1. Run `python3 reference_and_check.py` on an attached NPU; it runs all
   three checks and prints each one's max absolute error.
2. Compare `graph.compile(...).plan.full_elf` (ordinary) against
   `checked.compile(..., check=True).plan.full_elf` and read
   `plan.report("Pipeline")` for both — `check=True` is one of the reasons
   `plan()` gives for not choosing a full ELF.
3. In `reference_and_check.py`, replace the `SiLU` import with `GELU` and
   use `GELU.step(x)` in `Pipeline.body`. Update the hand-written reference
   in `main()` too:

   ```python
   gelu = GELU(size=args.size, num_aie_columns=1, tile_size=args.size)
   mul = ElementwiseMul(size=args.size, num_aie_columns=1, tile_size=args.size)
   by_hand = mul.reference(gelu.reference(x), y)
   ```

   Update `Pipeline`'s docstring to say `gelu(x) * y`, then rerun; all three
   checks should still pass. Changing only `body` leaves the manual reference
   computing SiLU, so the first, device-free comparison would fail.
   Print `SiLU`'s and `GELU`'s `.resolved().tolerance()` (import both to compare)
   and read the kernel each is built on (`iron/operators/gelu.py`, `silu.py`)
   for what backs the number.

-----
[Prev](../section-5/) &middot; [Top](..) &middot; [Next](../section-7/)
