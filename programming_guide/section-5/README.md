<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 5 - Carried Values and Device Loops

Section 3's per-call values come from the host on every call. A
**carried** value comes from the *previous call* instead: the host sets it
for the first call, and from then on the graph computes its next value
itself. A decoder carries its position and its last sampled token this
way (see [Section 8](../section-8/)).

## Walkthrough of [carried_loop.py](./carried_loop.py)

```python
class Walk(iron.Graph):
    """One step of a linked list walk: the next node gathered from
    ``successor`` and recorded in ``trail`` at the step count, the step
    count one more than the last."""

    def __init__(self, successor, steps: int):
        self.successor = iron.weight(successor)
        self.trail = iron.state((steps,), np.int32, name="trail")

    def body(self, *, node: Carried[np.int32], steps: Carried[np.int32]):
        nxt = Copy.step(self.successor[node], dtype=np.int32)
        Copy.step(nxt, self.trail[steps], dtype=np.int32)
        return iron.carry(node=nxt, steps=steps + 1)
```

A keyword-only parameter annotated `Carried[T]` (rather than
`Scratchpad[T]`) is a carried value. The body returns `iron.carry(...)`
last, giving the next value of each carried parameter. A next value can be
a one-element handle the graph computed (`node=nxt`) or a linear
expression of the current values (`steps=steps + 1`).

`iron.weight(table)` holds a table that the body indexes per call, as in
`self.successor[node]`. Compare `iron.param` (Section 4), which a step
reads whole. `trail` is a state, as in Section 4, and indexing it by the
carried `steps` works just like indexing `total` by `pos`: each call writes
one more entry.

## Calling it from the host, one step at a time

```python
nxt = walk.reference(node=node, steps=steps)   # or walk(node=node, steps=steps)
node, steps = int(nxt["node"]), int(nxt["steps"])
```

Called like any other graph, a carried graph returns the next values as a
`Carry`, a mapping by name. Nothing changes in place: you pass them into
the next call yourself. This works on any device, and `graph.reference(...)`
works the same way, so you can check a carried design against numpy one
step at a time.

## Looping entirely on the device

On NPU2 a graph normally compiles to one full ELF (Section 2). A full-ELF version
with carried values ends in an extra **Emit** step, which writes the next
call's scratchpad from the values it just carried, so the next call needs
nothing from the host. [`CarriedLoop`](../../iron/common/graph/carried.py)
runs that loop: a `first` version is started once from the host, and then
a `body` version that takes no tensor is run repeatedly, with `depth` runs
queued so the device does not wait on the host between them.

```python
walk = Walk(successor, args.steps + 1)
body = walk.compile()
loop = iron.CarriedLoop(body, body, depth=2)
got = list(loop.run(args.steps, node=start, steps=0))
```

`loop.run` yields `0, 1, 2, ...` as each step completes on the device.
`Walk` takes no tensor, so one compiled version serves as both `first`
and `body`. A graph whose first call does take a tensor (a decoder's
prompt chunk, which starts the decode loop) compiles that version with
`feeds=body` and passes it as `first`.

Because `first` is itself a full step here, `loop.run(args.steps, ...)`
makes `args.steps + 1` transitions in total, which is why `trail` holds
`args.steps + 1` entries. The example reads `trail` back with
`body.read(walk.trail)` and compares it exactly to a numpy walk. A gather
does no arithmetic, so the match is exact.

## <u>Exercises</u>

1. Run `python3 carried_loop.py` on an attached NPU2. It checks the
   host-driven path against a numpy walk, then runs the same walk as a
   device loop and checks the device's `trail` against it.
2. Bind an NPU1 device
   (`aie_utils.set_current_device(from_name("npu1", n_cols=4))`) and read
   `Walk(successor, 1).compile().plan.full_elf`. NPU1 has no full ELF, so
   there is no device loop there; only the host-driven path applies.
3. Run `CarriedLoop(body, body, depth=1)`, which keeps one step in flight
   at a time, then raise `depth` and time `loop.run` again to see what
   queuing steps on the device buys.

-----
[Prev](../section-4/) &middot; [Top](..) &middot; [Next](../section-6/)
