<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 7 - Profiles and Tunables

Every example so far either left an operator's tunables (`num_aie_columns`,
`tile_size`, ...) out entirely, letting `Operator.resolve(dev)` pick sane
defaults, or gave them explicitly at the `.step(...)` call site. A real
model does neither at scale: it autotunes each operator's tunables once per
device and keeps the result in a **profile**, a JSON file the graph applies
without `body` repeating a tunable at every call.

## Walkthrough of [profiles.py](./profiles.py)

```python
class Scaled(iron.Graph):
    """``1.5 * x + y``: one ``AXPY`` step, its tunables left to the profile."""

    def body(self, x, y):
        return AXPY.step(x, y, scalar_factor=1.5)
```

`body` names only what makes `AXPY` *this* operator — `scalar_factor` — and
leaves `tile_size` and `num_aie_columns` to whatever resolves them.

```python
profile = iron.Profile()
profile.add(AXPY, size=2048, tile_size=1024, num_aie_columns=2)

graph = Scaled()
graph.profile = profile
```

`Profile.add(cls, **fields)` records one entry: the `param()` fields given
(`size` here) are what an entry *matches* — a graph's step is only shaped
by this entry if every dimension it names agrees; a dimension left out
matches any value. The `tunable()` fields given (`tile_size`,
`num_aie_columns`) are what the entry *sets*, for every step whose shape
matches. Assigning `profile` to `graph.profile` makes it apply to `body`
wherever the graph is recorded — including `graph.reference(...)`, which
constructs the same operators under the same profile, so a check reflects
what the device actually runs.

### Precedence

A value for one tunable can come from three places, in this order:

1. **The call's own keyword** — `AXPY.step(x, y, scalar_factor=1.5, num_aie_columns=1)`
   always wins, profile or not.
2. **The profile** — the most specific matching entry (more `param()` fields
   named is more specific; two equally specific entries that disagree raise).
3. **`Operator.resolve(dev)`** — the operator's own default for the bound
   device, when neither of the above gave a value.

[`iron/applications/llama/profiles/`](../../iron/applications/llama/profiles/)
is the worked example at model scale: one entry per operator shape a real
decoder builds, written by `python -m iron.lm.tune <application> --checkpoint
<directory>`, which times every setting of every operator's tunables and
rewrites the profile. Review a regenerated profile with `git diff` before
committing it — a tunable moving is a performance change worth seeing, not
just a file diff.

## <u>Exercises</u>

1. Run `python3 profiles.py`; it prints the tunables the profile chose and
   checks the graph against numpy, same as earlier sections.
2. Add a second `profile.add(AXPY, size=1024, tile_size=256, num_aie_columns=1)`
   entry and record the graph at `x=(1024,), y=(1024,)` — a different shape
   picks the other entry.
3. Add `num_aie_columns=1` to the `AXPY.step(...)` call itself (keeping the
   profile's `num_aie_columns=2`) and reread `op.num_aie_columns` after
   recording: the call's own value wins.

-----
[Prev](../section-6/) &middot; [Top](..) &middot; [Next](../section-8/)
