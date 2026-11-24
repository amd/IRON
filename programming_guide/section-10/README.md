<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 10 - Tuning a Model

Every profile so far was written by hand: Section 7 gave `AXPY` a
`tile_size` and `num_aie_columns` by eye, and Section 9 named a fusion
itself. A model's profile has an entry for every shape its decoder builds,
too many to pick by hand, so `python -m iron.lm.tune <application>` does it
on the attached NPU: it times each operator's tunables, then prices the
packings and fusions the graph admits, and writes `profiles/<device>.json`
back. This section runs that same search, first on one operator with
`python -m iron.tune.cli`, then on a whole toy graph with
`iron.tune.cli.tune`, the call `iron.lm.tune` itself makes.

## Tuning one operator

```bash
python -m iron.tune.cli GEMV M=128 K=64 \
    num_aie_columns=1 num_channels=1 feed_b=false coded_a=false \
    --rounds 2 --calls 10
```

`GEMV`'s `fields` give its shape (`M`, `K`) and hold four of its tunables at
one setting each, so only `tile_size_input` and `tile_size_output` are
searched, over every value that divides `M`. One run on a Strix Halo NPU2
printed:

```
power mode: turbo
{'tile_size_input': 8, 'tile_size_output': 8}:     -4.87 ± 5.66 us
{'tile_size_input': 4, 'tile_size_output': 16}:     -3.47 ± 3.67 us
{'tile_size_input': 4, 'tile_size_output': 8}:     -2.95 ± 4.29 us
{'tile_size_input': 8, 'tile_size_output': 16}:     -2.23 ± 2.48 us
{'tile_size_input': 4, 'tile_size_output': 4}:     -2.15 ± 3.71 us
{'tile_size_input': 16, 'tile_size_output': 16}:     -1.83 ± 2.76 us
{'tile_size_input': 2, 'tile_size_output': 4}:     -0.71 ± 1.16 us
{'tile_size_input': 2, 'tile_size_output': 8}:     -0.56 ± 1.70 us
{'tile_size_input': 2, 'tile_size_output': 2}:     +0.00 ± 0.00 us  (recorded)
{'tile_size_input': 1, 'tile_size_output': 16}:     +1.32 ± 1.28 us
{'tile_size_input': 2, 'tile_size_output': 16}:     +1.79 ± 4.15 us
{'tile_size_input': 1, 'tile_size_output': 8}:     +2.24 ± 1.73 us
{'tile_size_input': 1, 'tile_size_output': 4}:     +3.35 ± 0.85 us
{'tile_size_input': 1, 'tile_size_output': 2}:     +4.15 ± 2.00 us
```

Each line is one setting of the tunables left open, timed against the
setting `GEMV(M=128, K=64, ...)` itself resolved to without any of them
given (`(recorded)`, always `+0.00`); the number after it is how much
faster (negative) or slower that setting ran, and the `±` figure is its
noise. Sorted fastest first, the top line is the one worth keeping: here,
`tile_size_input=8, tile_size_output=8`, which a profile (Section 7) would
take as
`profile.add(GEMV, M=128, K=64, num_aie_columns=1, num_channels=1, tile_size_input=8, tile_size_output=8)`.

## Walkthrough of [tune_graph.py](./tune_graph.py)

A model's own tune times a decoder's calls this same way, over every shape
its graph builds at once, and then prices packings and fusions across all of
them. `MiniMLP` is Section 9's `SwiGLU` at a width small enough to tune in
about a minute: two `GEMV`s, `SiLU` and a multiply.

```python
class MiniMLP(iron.Graph):
    """``silu(w_gate @ x) * (w_up @ x)``, SwiGLU's shape (Section 9) sized to tune quickly."""

    def __init__(self, w_gate, w_up):
        self.w_gate, self.w_up = iron.param(w_gate), iron.param(w_up)

    def body(self, x):
        gate = GEMV.step(self.w_gate, x)
        up = GEMV.step(self.w_up, x)
        return SiLU.step(gate) * up
```

`record(profile)` is the callable every tune passes around: a model's own
`tune_calls` builds one of these per version (a decode step, a prompt
chunk); a toy graph's is just its one recording, wrapped in a `Timed`.

```python
def record(profile: Profile) -> list[Timed]:
    w_gate, w_up = weights()
    graph = MiniMLP(w_gate, w_up)
    graph.profile = profile
    return [Timed(graph.record(x=(HIDDEN,)))]
```

`main` passes it straight to `iron.tune.cli.tune`, the function
`iron.lm.tune`'s own `main` calls once it has built the same kind of
`record`:

```python
parser = tune_cli.parser("Section 10: tuning a toy graph")
parser.add_argument("--profiles", type=Path, default=None, ...)
args = parser.parse_args(argv)
...
path = tune_cli.tune(args, record, profiles)
```

Run with `--hold GEMV` (so the tunable search spends its time on `SiLU` and
the multiply, `GEMV` left at what the starting profile gives it, here
nothing) and a 90 second `--budget`:

```bash
python programming_guide/section-10/tune_graph.py --rounds 2 --calls 10 --budget 90 --hold GEMV
```

It logs each phase as it finishes, then writes `<device>.json` and its
report. One run's `<device>.report.txt`:

```
tune of npu2.json

added:
  fold SiLU size=256 + ElementwiseMul size=256 in x[64]
  packing GEMV M=256 K=64 {"feed_b": true, "num_aie_columns": 1, "num_channels": 4, "tile_size_input": 4, "tile_size_output": 16} + SiLU uses_extra=True size=256 in x[64]
  tunables ElementwiseMul size=256 {"num_aie_columns": 1, "num_channels": 1, "tile_size": 64}
  tunables SiLU size=256 {"num_aie_columns": 1, "tile_size": 256}
dropped:
  nothing
end to end against the starting profile:
  MiniMLP (x[64]): -116.6 ± 2.6 us
phases, each version against the phase before:
  seed: 1 s (build 1, timing 0), check 0 s; no version changed
  survey: 0 s (build 0, timing 0), check 0 s; no version changed
  autotune of 2 shape(s): 5 s (build 4, timing 1), check 1 s; MiniMLP (x[64]) -17.8 ± 11.6 us
  folds and packing: 13 s (build 7, timing 5), check 0 s; MiniMLP (x[64]) -115.6 ± 8.5 us
  fusions: 7 s (build 5, timing 1), check 0 s; no version changed
  verify: 0 s (build 0, timing 0), check 0 s; no version changed
  validate: 0 s (build 0, timing 0), check 0 s; no version changed
```

`added` is what changed: `SiLU` and the multiply (`ElementwiseMul`) each got
a tunable entry at their shape (`size=256`, `INTERMEDIATE`); `SiLU` and the
multiply folded into one step; and one `GEMV` (`M=256, K=64` is
`INTERMEDIATE, HIDDEN`) packed with `SiLU` into one shared configuration,
both scoped to this call's one version (`x[64]`). `phases` is the same tune
broken into the stages
[AGENTS.md](../../AGENTS.md)'s "Graphs" section describes: `autotune` found `SiLU` and
the multiply's own settings, `folds and packing` found the fold and the
packing (most of the gain), and `fusions` tried streaming a `GEMV` straight
into `SiLU` on top of that and dropped it: the packing already removes the
same switch, so streaming on top gains nothing more.

### Checking the result

`tune` already checks what it saves against the profile it started from
(the report's `end to end against the starting profile` line) and drops
anything that doesn't gain; `main` still checks the written profile
against a numpy reference itself, as any device run must:

```python
tuned = Profile.load(path)
graph = MiniMLP(w_gate, w_up)
graph.profile = tuned
reference = graph.reference(x)
graph.compile(x=(HIDDEN,))
result = graph(x)
verdict = compare(np.asarray(result), reference, op.resolved().tolerance())
```

which printed `tuned profile vs. graph.reference(): ok`: the fold and the
packing changed where `SiLU`'s and the multiply's work runs and how the
device is configured between steps, not what either computes.

## Packings scoped to a version

The packing entry above carries `"versions": [{"x": [[64], "bfloat16"]}]`:
it names the call's one input shape. A decoder's decode step and its prompt
chunk run the same arrays at very different extents, so a grouping timed
on one is scoped to it; `Profile.add_packing(members, versions=...)` takes
the same scope by hand, and `python -m iron.lm.tune <application>
--packings-only` finds and scopes it for every version a model's graph
builds.

## Coded weights

A `GEMV` whose profile entry sets `"coded_a": true` reads its weight as
mlir-aie's coded rows, about 0.76x the bytes, bit-identical output: a
decode step whose time is mostly its weight reads gets faster for it.
`tune_graph.py`'s own survey names the same lever, `coded: up to 0 us
(read-bound GEMVs' time times the bytes coding saves)` - zero here, because
`MiniMLP`'s weight is a few dozen kilobytes, nowhere near large enough for
the read to dominate the way a real decoder's does. Checking a checkpoint
fits and setting it is [AGENTS.md](../../AGENTS.md)'s "Coded weights" walkthrough; from a
profile with it set, `python -m iron.lm.tune <application> --packings-only`
re-groups around the smaller weight and `python -m iron.lm.validate
<application> --checkpoint DIR --candidate PROFILE_DIR` checks the result
bit-identical on real weights.

## One compile for many runs

`tune` and `iron.lm.tune` both spend their time before a single call: once
`<device>.json` is written, `graph.compile(...)` (Section 3) builds against
it once and every later call, at any shape that version covers, runs
without tuning or compiling again. A model loads its tuned profile the same
way at startup; `tune_graph.py`'s own `graph.compile(x=(HIDDEN,))` after the
search is the same call, on the profile the search just wrote.

## <u>Exercises</u>

1. Run `python -m iron.tune.cli GEMV M=128 K=64 num_aie_columns=1
   num_channels=1 feed_b=false coded_a=false --rounds 2 --calls 10` on an
   attached NPU2. Drop `feed_b=false` and compare: `feed_b=true` opens a
   wider search, including settings a shim channel must be spent on.
2. Run `python3 tune_graph.py` without `--hold GEMV`. `GEMV`'s own
   tunables are searched too: the tune takes longer, and where a setting
   wins, its report's `added` gains a `tunables GEMV M=256 K=64 ...` line
   (gate and up share that one shape).
3. Pass `--profiles ./my-profile` and re-run. `my-profile/npu2.json` is
   kept after the run; open it and find the `"packings"` entry this section
   walks through, by eye this time.

-----
[Prev](../section-9/) &middot; [Top](..)
