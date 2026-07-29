<!--
SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# SwiGLU prefill (stream-dse codegen)

The whole SwiGLU-prefill block, `(SiLU(x @ gate) * (x @ up)) @ down`, deployed as one
full ELF. Unlike the hand-written operators the MLIR is generated at build time by 
[`stream-dse`](https://github.com/KULeuven-MICAS/stream),
which solves where every layer runs and emits the AIE design.

## What IRON provides and what stream-dse returns

stream-dse needs two inputs, and IRON writes both from one source.

| | Source | Built by |
| --- | --- | --- |
| Workload (ONNX) | [`reference.py`](./reference.py), the `SwiGLU` `nn.Module` | `torch.export` via [`iron/common/stream/workload.py`](../../common/stream/workload.py) |
| Mapping (YAML) | the placement in [`stream_design.py`](./stream_design.py) | [`iron/common/stream/mapping.py`](../../common/stream/mapping.py) |
| Kernels (`.cc`) | IRON's `aie_kernels` library | the registry in [`iron/common/stream/ops.py`](../../common/stream/ops.py) |

`reference.py` is the single source of truth. Running it produces the golden output the
test compares against; exporting it produces the workload the design is generated from.
The mapping reads its layer names back from the exported graph rather than restating
them, so workload and mapping cannot disagree. Both files are written into the
experiment's output directory at build time; nothing is committed.

stream-dse returns one MLIR design per fusion group. IRON takes it from there:
`iron/common/sequence.py` fuses the designs into a single module and compiles it with
`aiecc` into one full ELF.

Nothing crosses the boundary except those files, which is why stream-dse can be an
optional dependency: a checkout without it imports and tests everything else.

## Fusion granularity: the `k` modes

`k` is how many fused groups the block is split into, and so how many designs the ELF
holds. The groups are `stream_design.GROUP_LAYERS`.

| `k` | Groups | Shape on the array |
| --- | --- | --- |
| 1 | `gate, up, silu, mul, down` | the whole block at once, layers on disjoint columns, pipelined |
| 2 | `gate, up, silu, mul` + `down` | as above, split after the multiply |
| 5 | one per layer | layer by layer, each taking the whole array in turn |

k=1 and k=2 fuse several layers onto each core, so intermediates stay on chip. k=5 is
the shape [`swiglu_prefill`](../swiglu_prefill) uses, every layer its own design.

A core holds the operands of every layer in its group, so the kernel tile a group can
afford shrinks as more layers fuse onto it. That is why the tile is chosen per `k`
(`stream_design.FUSED_TILES` and `LAYER_TILES`). A tile that does not fit is rejected at
build time by stream-dse, naming the core and the shortfall.

The tile also bounds the problem sizes: `seq_len` must be a multiple of the array rows,
and `embedding_dim` and `hidden_dim` multiples of their tile times the column split.
`stream_design._check_shapes` enforces this and names the offending dimension.

Designs that come out byte-identical are built and configured once: at k=5 the gate and
up projections are the same design, so the ELF holds four rather than five. Set
`share_designs=False` on the operator to switch that off.

## Expected performance

Warm dispatch on one callable, 20 dispatches, seq 256 / embedding 512 / hidden 2048, on
an idle NPU2. `swiglu_prefill` is the hand-written operator at the same shape.

| Design | Median (us) | Relative |
| --- | --- | --- |
| `swiglu_prefill` | 1348 | 1.00x |
| `k=1` | 1165 | 0.86x |
| `k=2` | 1452 | 1.08x |
| `k=5` | 1399 | 1.04x |

k=1 is fastest: fusing the whole block keeps the intermediates on chip instead of
returning them to memory between layers.

Medians from one machine, so treat them as orders of magnitude rather than exact.
Accuracy tracks the hand-written operator: 0.139 of output elements more than 8 percent
from the golden reference, against 0.139 to 0.144 here.

## Runtime buffers

Named by the reference module: `input`, `w_gate`, `w_up`, `w_down`, `output`.

```python
run = operator.get_callable()
run.get_buffer("w_gate").torch_view()[:] = weights.flatten()
```

## Installing

stream-dse is an optional, separately installed dependency and is not in IRON's
`requirements.txt`.

```bash
pip install -r requirements_stream.txt
stream-setup-aie          # required: installs stream-dse's AIE codegen dialects
```

`stream-setup-aie` installs the pure-Python codegen dialects (`xdsl-aie`, `snax-mlir`)
that cannot be plain PyPI dependencies because they are direct git installs. It does not
install `mlir_aie` / `llvm-aie`: IRON's `requirements.txt` pins those, and the codegen
only emits text MLIR through xdsl. Solving uses the licence-free OR-Tools GSCIP backend,
so no Gurobi licence is needed.

Importing the operator does not require stream-dse; only building it does.

## Build and run

```bash
source /opt/xilinx/xrt/setup.sh
pytest iron/operators/swiglu_prefill_stream/test.py
```

## Adding another operator

One `StreamKernel` plus one `TORCH_OPS` entry in `iron/common/stream/ops.py`, pointing
at IRON's `aie_kernels/<dir>/<name>.cc`, plus that operator's own placement. The
kernel entry carries both the compile flags and the operand layouts, so the layout the
generated DMAs produce and the layout the compiled object expects come from one place.

## Notes

The hardware description (`whole_array_strix.yaml`) is resolved from the installed
`stream` package, where it ships as package data; nothing is vendored here.

Node names are set explicitly, naming the role each layer plays rather than the ATen
op the exporter captured (`matmul`, `matmul_1`, ...). The mapping and the generated
design are both read by those names.
