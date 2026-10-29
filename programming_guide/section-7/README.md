<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 7 - Profiles and Tunables

So far, each example either left an operator's tunables (`num_aie_columns`,
`tile_size`, ...) to `Operator.resolve(dev)`, or passed them at the
`.step(...)` call. A model with hundreds of steps needs something better.
It keeps its tuned values in a **profile**: a JSON file per device that the
graph applies to every step it records, so `body` never repeats a tunable.

## Walkthrough of [profiles.py](./profiles.py)

```python
class Scaled(iron.Graph):
    """``1.5 * x + y``: one ``AXPY`` step, its tunables left to the profile."""

    def body(self, x, y):
        return AXPY.step(x, y, scalar_factor=1.5)
```

`body` gives only `scalar_factor`. It leaves `tile_size` and
`num_aie_columns` to the profile.

```python
profile = iron.Profile()
# Matches any AXPY built at this size: tile_size and num_aie_columns,
# not scalar_factor or size itself, which a call always gives.
profile.add(AXPY, size=args.size, tile_size=1024, num_aie_columns=2)

graph = Scaled()
graph.profile = profile
```

`Profile.add(cls, **fields)` adds one entry. Its `param()` fields (`size`
here) are what the entry matches: a step uses the entry only if every
dimension the entry names agrees with the step's. A dimension the entry
leaves out matches any value. Its `tunable()` fields (`tile_size`,
`num_aie_columns`) are what the entry sets on each matching step.

Assigning `graph.profile` applies the profile wherever the graph is
recorded, `graph.reference(...)` included. The reference therefore builds
the same operators the device runs.

### Precedence

Each tunable takes its value from the first of these that gives one:

1. **The call's own keyword.**
   `AXPY.step(x, y, scalar_factor=1.5, num_aie_columns=1)` always wins.
2. **The profile.** The most specific matching entry wins, where naming more
   `param()` fields is more specific. Two equally specific entries that
   disagree raise an error.
3. **`Operator.resolve(dev)`**, the operator's own choice for the bound
   device.

[`iron/applications/llama/profiles/`](../../iron/applications/llama/profiles/)
is a full-size example, with one entry per operator shape the decoder
builds. `python -m iron.lm.tune <application> --checkpoint <directory>`
writes it: it times candidate settings of each operator's tunables on the
attached NPU and rewrites `profiles/<device>.json` with the fastest it
finds. Review the change with `git diff` before you commit it.

## <u>Exercises</u>

1. Run `python3 profiles.py` on an attached NPU. It prints the tunables the
   profile chose, then checks the device result against
   `graph.reference(...)`.
2. Add a second entry,
   `profile.add(AXPY, size=1024, tile_size=256, num_aie_columns=1)`, and
   record the graph at `x=(1024,), y=(1024,)`. The different shape picks the
   other entry.
3. Add `num_aie_columns=1` to the `AXPY.step(...)` call itself, keeping the
   profile's `num_aie_columns=2`, and read `op.num_aie_columns` after
   recording. The call's own value wins.

-----
[Prev](../section-6/) &middot; [Top](..) &middot; [Next](../section-8/)
