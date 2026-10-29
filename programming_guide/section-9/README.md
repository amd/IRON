<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Section 9 - Fusing Steps On-Chip

Every graph so far compiled each step as its own device configuration: a
step's cores read their inputs from host memory and write their output
back to it, and the next step reads it from there again. For a decode step,
where each operator's compute is small, that round trip through host memory
and the change of configuration between steps are a real share of its time.

A **fusion** runs several of a graph's steps as one device configuration.
`body` does not change: a profile (Section 7) names which steps fuse, and
`compile` builds them together.

## Walkthrough of [swiglu_fusion.py](./swiglu_fusion.py)

```python
class SwiGLU(iron.Graph):
    """``silu(w_gate @ x) * (w_up @ x)``, against weights this graph holds."""

    def __init__(self, w_gate, w_up):
        self.w_gate, self.w_up = iron.param(w_gate), iron.param(w_up)

    def body(self, x):
        gate = GEMV.step(self.w_gate, x)
        up = GEMV.step(self.w_up, x)
        return SiLU.step(gate) * up
```

This is Llama 3.2 1B's gated MLP for one token, up to its down projection
(`GatedMLP` in [`iron/lm/blocks.py`](../../iron/lm/blocks.py)): four steps,
`gate`, `up`, `SiLU` and the multiply, with three intermediates between
them.

### What a recording admits

```python
recording = fused.record(x=(HIDDEN,))
for fusion in candidates(recording):
    ...
```

`iron.common.graph.fusion.candidates(recording)` lists every run of
consecutive steps that could stream on-chip. For `SwiGLU` it prints:

```
candidate stream: steps (0, 1, 2, 3) (GEMV, GEMV, SiLU, ElementwiseMul)
candidate stream: steps (1, 2, 3) (GEMV, SiLU, ElementwiseMul)
candidate stream: steps (2, 3) (SiLU, ElementwiseMul)
```

A candidate is only what the recording allows: each intermediate one step
in the run writes, later steps in the run read whole, and no host step or
graph output reads. The second run is the up projection, SiLU and the
multiply, the gate projection's output still coming from host memory.
Whether a candidate fits on the array, and whether it is faster, depends on
the tunables its members run at, so nothing fuses until a profile names it.

### Naming the fusion in a profile

```python
MLP_EDGES = [(0, "C", 2, "x"), (1, "C", 3, "b"), (2, "y", 3, "a")]

profile = tuned_profile()
gemv = (GEMV, {"M": INTERMEDIATE, "K": HIDDEN})
profile.add_fusion(
    iron.FusionKind.STREAM,
    [
        gemv,
        gemv,
        (SiLU, {"size": INTERMEDIATE}),
        (ElementwiseMul, {"size": INTERMEDIATE}),
    ],
    MLP_EDGES,
)
```

`Profile.add_fusion(kind, steps, edges)` adds one fusion entry. `steps` are
matched like `Profile.add`'s entries, by class and the dimensions named, in
the order `body` records them. Each edge is `(producer, output, consumer,
input)`, indices into `steps` and the operators' own operand names: the gate
projection's `C` feeds SiLU's `x`, the up projection's `C` feeds the
multiply's `b`, and SiLU's `y` feeds its `a`. A step may also give tunables
it takes only inside this fusion, as a third element; this example keeps
the ones `tuned_profile()` gives every step.

`iron.common.graph.fusion.fusions(recording, profile)` is the pick: the
candidates a profile names, a step in at most one. The example prints it:

```
the profile fuses steps (0, 1, 2, 3) as one stream
```

`Graph.compile` makes the same pick and builds each fusion as one device
configuration. In a full ELF (NPU2's default) the fused steps are one part
of the one call; per step (NPU1's default) the fusion is one xclbin and one
dispatch.

### The kinds of fusion

`FusionKind` names how a fusion's steps share the device:

| Kind | What runs together |
|---|---|
| `STREAM` | An edge's producer streams its output straight into the consumer's cores; one output may feed several consumers. This example. |
| `STAGED` | As `STREAM`, where the two sides' lanes differ in count, tile or order and are rejoined through memory tiles. |
| `FOLD` | The consumer's kernel runs in its producer's own cores, after the producer's (SiLU's cores finishing with the multiply). |
| `PACK` | Independent steps placed side by side and issued at once (the q, k and v projections). |
| `MERGE` | Consecutive steps that share one configuration, run back to back. |

### Checking and timing it

```python
versions = {
    "unfused": apart.compile(x=(HIDDEN,)),
    "fused": fused.compile(x=(HIDDEN,)),
}
```

`apart` is the same graph under `tuned_profile()` alone. Both versions are
held to `graph.reference(x)` (Section 6), and to each other bit for bit: a
fusion changes where intermediates live, not what any kernel computes, so
fused and unfused outputs must be identical. `compile(check=True)` checks
each step on its own dispatch, so it compiles the steps unfused whatever
the profile names; check the steps that way, then compare the fused version
against them, as this example does.

Each version's loaded image (`version.callable`) is then timed with
mlir-aie's `run_interleaved`: `--rounds` rounds of `--calls` calls each,
the two versions taking turns, each figure the NPU's own time for a call.
On a Strix NPU2 (Ryzen AI 9 HX 370):

```
unfused: 1685.2 us min, 1720.6 us median
fused: 1296.0 us min, 1324.9 us median
```

The fusion's three intermediates (two of 8192 elements from the
projections, one from SiLU) stay on-chip, and the four steps run as one
configuration.

### Letting the tuner choose

Writing a fusion entry by hand is how to try one. For a whole model,
`python -m iron.lm.tune <application> --fusions-only` prices every
candidate in the model's recordings against its profile, confirms that a
fused version is bit-identical to the steps apart, and writes the fusions
that gain into the application's `profiles/<device>.json`.

## <u>Exercises</u>

1. Run `python3 swiglu_fusion.py` on an attached NPU2. It lists the
   candidates, checks both versions and prints their NPU times.
2. Drop the edge `(1, "C", 3, "b")` from `MLP_EDGES` and compile again.
   The entry no longer matches the recording's candidate, so the graph
   compiles unfused.
3. Give `body` a second input `y` in place of the `up` projection,
   `return SiLU.step(GEMV.step(self.w_gate, x)) * y`. Which stream
   candidates does the recording admit now? `candidates` leaves folds out;
   `iron.common.graph.fold.fold_candidates(recording)` lists those, among
   them steps `(1, 2)`: the multiply run in SiLU's own cores.

-----
[Prev](../section-8/) &middot; [Top](..)
