<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 5 - Carried Values and Device Loops

Section 3's per-call values came from the host, one call at a time. A
**carried** value instead comes from the *previous call*: the host seeds it
once, and after that the graph itself says what it is next. A decoder's
token position and its last sampled token are carried this way — see
[Section 8](../section-8/).

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

A keyword-only parameter annotated `Carried[T]` (rather than `Scratchpad[T]`)
is a carried value. `body` must then return `iron.carry(...)` last, naming
the next value of every carried parameter: `node`'s is `nxt`, a handle the
step computed; `steps`' is `steps + 1`, a plain expression of the current
value. Either form is allowed — a carried value's next value is either an
expression of the current per-call values, or one element the graph itself
computed.

`iron.weight(table)` wraps `successor` for per-call indexing
(`self.successor[node]`, read differently each call), distinct from
`iron.param` (Section 4): a weight is read through a per-call index, a
param's whole tensor is an operand. `trail` is Section 4's `iron.state`
again, indexed by the carried `steps` the same way `Accumulate` indexed by
a scratchpad `pos` — a carried value and a per-call value reach a state the
same way, each call writing one more of its rows.

## Calling it from the host, one step at a time

```python
nxt = walk.reference(node=node, steps=steps)   # or walk(node=node, steps=steps)
node, steps = int(nxt["node"]), int(nxt["steps"])
```

Called like any other graph, a carried graph returns the *next* values as a
`Carry` (a mapping, `dict(nxt)` if you want a plain one) instead of mutating
anything in place — you feed them back into the next call yourself. This
form works on any device and needs no special setup; it is also what
`graph.reference(...)` gives you to check a carried design against numpy,
one step reproducing what a device call would carry forward.

## Looping entirely on the device

A full-ELF version (NPU2; Section 7 says more about full ELF vs. xclbin)
with carried values compiles an extra step, an **Emit**, that writes its own
next scratchpad from what it just carried — so a second call never needs
the host to hand it anything. [`CarriedLoop`](../../iron/common/graph/carried.py)
drives that: `first` seeds the carried values from the host once, and
`body` (no tensor) is looped, `depth` runs kept in flight so the device
never idles waiting for the host between them.

```python
walk = Walk(successor, steps + 1)
body = walk.compile()
loop = iron.CarriedLoop(body, body, depth=2)
for index in loop.run(steps, node=start, steps=0):
    ...  # index is 0, 1, 2, ... as each step on the device completes
```

`Walk` takes no tensor at all, so one compiled version serves both roles —
`first` and `body` are the same `CompiledGraph`. A graph whose body also
takes a tensor (a decoder's prompt chunk feeding its first decode step,
for instance) compiles two versions and passes the tensor-taking one as
`feeds=` so its Emit is sized to start the other
(`iron/tests/infrastructure/test_carried_loop.py`'s `Trail` is that case).

Because `first` here is this same `body` — it always looks the next node
up, with no separate "just seed `node`" branch the way `Trail`'s own `jump`
does — `loop.run(steps, node=start, ...)` performs `steps + 1` transitions
in total, not `steps`: one from `first`, then `steps` more from `body`, so
`trail` is sized `steps + 1` to hold every one of them.
`carried_loop.py` reads `trail` back with `body.read(walk.trail)` — a
public state, the way any other section's device run is checked — and
compares it to the numpy walk, exactly: a gather has nothing to round.

## <u>Exercises</u>

1. Run `python3 carried_loop.py` on an attached NPU2; it checks the
   host-driven path against a plain numpy walk, then runs the same walk as
   a device loop and checks the device's own recorded `trail` against the
   numpy walk.
2. Read `Walk(successor, 1).compile().plan.full_elf` for an NPU1-bound
   device (`aie_utils.set_current_device(from_name("npu1", n_cols=4))`) — a
   carried value with no full ELF has no device loop; only the host-driven
   path applies.
3. `CarriedLoop(body, body, depth=1)` runs one step at a time, in lockstep
   with the host; raise `depth` and compare how many steps land between two
   calls to `next(iterator)` — this is the pipelining `depth` buys.

-----
[Prev](../section-4/) &middot; [Top](..) &middot; [Next](../section-6/)
