<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# AGENTS.md

The rules a coding agent or contributor follows in this repository, and the
map of where things live. Each module's docstring is the reference for what
it does; this file does not repeat it.

IRON is a Python library for AMD Ryzen™ AI NPUs (NPU1 is AIE2, NPU2 is
AIE2P) over mlir-aie's `aie.iron`. bfloat16 is its main data type.

Elsewhere:

- [README.md](README.md): installation, the quick start and the models.
- [CONTRIBUTING.md](CONTRIBUTING.md): the pull request workflow, style,
  licence headers, the git hook, and short walkthroughs for adding a model
  or an operator.

## Environment

Install as the README says. XRT must be sourced
(`source /opt/xilinx/xrt/setup.sh`) before anything runs on a device.
`requirements.txt` pins the mlir-aie wheel IRON is tested with, a release
or a nightly (`latest-wheels-4`), which brings the kernel library, and the
llvm-aie (Peano) nightly that mlir-aie commit validated
(`utils/peano-requirements.txt`); pyright types against that wheel too. A
pull request that needs a newer mlir-aie bumps both in the same pull
request (`update-mlir-aie.yml` does it for a release or a nightly).

- Compiled artifacts live in mlir-aie's content-keyed cache,
  `~/.npu/cache/<hash>/` or `$NPU_CACHE_HOME`; nothing is written to the
  working directory.
- `IRON_EXAMPLE_WEIGHTS_DIR` (default `/srv`) is where model tests find
  checkpoints (`iron.lm.testing.weights_dir`).
- `MLIR_AIE_KERNEL_SOURCES=/path/to/mlir-aie` builds kernels from another
  tree; the path is part of the compile key.
- `NPU_RUNTIME` selects the host NPU runtime backend; the programming
  guide's "Getting Set Up" (`programming_guide/section-0`) says more.
- No build context: an operator compiles for the current device and
  nothing else. On a host without an NPU, bind one with
  `aie_utils.set_current_device(from_name("npu2", n_cols=8))`
  (`aie.iron.device.from_name`); the test tree's `npu2` fixture does this.
  Kernels are built with Peano; a kernel that needs xchesscc asks its
  `aie.iron.kernels` factory (`use_chess=True`).

## Commands

```bash
pytest iron/operators/ iron/tests/ -m "not extensive"   # what CI runs on every PR
pytest iron/operators/ iron/tests/                      # the extensive suite
pytest iron/tests/operators/test_catalog.py -k AXPY     # one declared operator
pytest tests/applications/                              # model tests
pytest ... -n auto                                      # in parallel
pytest ... --csv-output=tests_latest.csv                # write benchmark figures
pre-commit run --all-files --hook-stage pre-push        # black, ruff, pyright, ..., as CI's lint
pyright                                                 # types, as CI's Types job
```

Without an NPU, the device-free suite is
`pytest iron/tests/common iron/tests/lm tests/applications iron/tests/operators iron/tests/infrastructure -m "not extensive"`.
Formatting, lint, type and licence checks are in CONTRIBUTING.md
("Formatting and hooks"); docstrings pass ruff's Google-convention
pydocstyle rules, `D205` and `D401` included.

## Where things live

- `iron/operators/`: one operator per module, `relu.py`, or a package with
  `op.py` when it also has a hand-written design, a reference, a README or
  a device test (`flm/gemm/`). `flm/` holds the FastFlowLM ports; its
  operators are also catalogued under dotted names (`"flm.ProjectionGEMM"`),
  which is how a `Profile` names them. `flm.ProjectionGEMM` is not
  `iron.operators.GEMM`.
- `iron/common/declare/`: IRON's `Operator` over mlir-aie's declaration
  (`aie.utils.compile.jit`'s `param()`, `tunable()`, `per_call()`), and the
  bound operands and `Value`s a build reads. A `Value` is one operator's
  `per_call()` member, `op.value(name)`, which `op.<name>` also returns
  except for an extent, which reads as its number. Also `Xclbin`,
  `Profile` and `Precision`.
- `iron/common/design/`: an operator's MLIR module (`OperatorDesign`) and
  its runtime sequence (`OperatorRuntime`).
- `iron/common/graph/`: `iron.Graph`, recording and `compile`.
- `iron/common/image/`: what a graph lowers onto: the step sequence, the
  buffer allocator, image composition (several designs in one image),
  packaging, and an operator called on its own. All internal.
- `iron/common/feature_map.py`: `Conv2d`, a convolution over a
  channels-last feature map's rows.
- `iron/common/elementwise.py`: the shared elementwise array, its families
  and `Sweep`.
- `iron/common/testing.py`: `Testing`, `Case`, `vectors`, `run_test`,
  `time_call`.
- `iron/common/tracing.py`: `dump_traces` for an operator built with
  `trace=`.
- `iron/tune/`: autotuning, at the edge: nothing in the core imports it.
  `python -m iron.tune.cli GEMV M=2048 K=8192` times one operator;
  `python -m iron.lm.tune <application>` rewrites a model's
  `profiles/<device>.json`.
- `iron/lm/`: what every language model shares (see "Language models").
- `iron/applications/<name>/`: one model each; `tests/applications/<name>/`
  its tests.
- `iron/tests/`: the tests by subsystem, each module `test_<name>.py`.
  What several share is in `iron/tests/support/`; no test module imports
  another.
- Kernels are not here: they are C++ in mlir-aie's
  [`aie_kernels/`](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels),
  reached through the factories in `aie.iron.kernels`, each returning an
  `ExternalFunction` whose `.contract` carries its reference, its tolerance
  and the scalars it binds.

## Hardware

- NPU1 (Phoenix, Hawk Point): 4 rows by 4 usable columns. NPU2 (Strix,
  Strix Halo, Krackan): 4 rows by 8 columns.
- Data moves host (L3) to shim DMA, to memory tiles (L2), to each core's
  local memory (L1, tens of KB), where the kernel runs.
- An operator's size rules are its `compatible()` and its domains; a shape
  it must refuse is in `iron/tests/operators/test_rejected_shapes.py`.

## Adding an operator

CONTRIBUTING.md walks through the common case. The rules:

1. One module, `iron/operators/<name>.py`; a package with `op.py` only when
   it needs more than one module.
2. Declare `class X(Operator)`:
   - Parameters are mlir-aie's `param()`. A host shape's dimension is one
     (`M: int = param()`). A tunable is `tunable()`. Its value comes from
     the call if given, else the profile, else `resolve(dev)`, else its
     default.
     Identity (`array_key`, `design_key`) is taken after resolution.
   - Operands are aie.iron's `In`/`Out`/`InOut`, declared by shape. An
     operand with `obj_shape=` (in the units a core reads; `per=` a column
     count) is its own stream into the array. `when=flag` makes an operand
     exist only where a bool parameter is true.
   - Every trip count a core reads is a `per_call(derive=...)`, so the array
     never depends on an extent. Anything else the array bakes is declared
     `array=True`.
   - A quantity computed from other parameters is:

     | Read by | Declare |
     |---|---|
     | host Python only | `@property` |
     | a compile-time parameter held to its formula | `param(derive=lambda op: ...)` |
     | a compile-time parameter a caller may override | `param(default=lambda op: ...)` |
     | a tunable `resolve(dev)` always fills | `tunable(init=False)` |
     | a core | `per_call(derive=...)` |

   - `build()`, on `layout()`: a copy of the operator holding only the
     parameters its cores read (`declaration.key`) and its members. It makes
     ObjectFIFOs and Workers, uses
     `range_()` (not `range`) for core loops, binds each streamed operand's
     lanes to fifo ends, gives each core an `Rtp` for its values and
     returns `Built(objects, rtps)`.
   - `sequence(rt)` only when the derived runtime sequence is not the one
     wanted (`gemm.py`, `mha.py`).
3. A shipped binary is a subclass declared with its image,
   `class Shipped(X, image=Xclbin(url=, sha256=, filename=))`, whose
   `build()` pins each operand's lanes to the image's shim channels
   (`operand.pin([...])`) and builds no cores. It cannot run inside a graph.
4. The kernel comes from an `aie.iron.kernels` factory. A scalar it takes at
   run time is the operator's `scalars()`, in the kernel's order. A kernel no
   factory covers is an `ExternalFunction` with `symbol_prefix=` naming its
   configuration and a `contract=KernelContract(...)`;
   `iron/tests/toolchain/test_inline_kernel.py` is the example. A new C++ kernel
   goes into mlir-aie with a factory; IRON hosts none.
5. `reference(*inputs)` only where the kernel's contract is not already
   the reference: numpy, upcast to float32, round once. A composite builds
   it from its kernels' contract references where it can, and says why in
   a comment where it cannot. `ops()` where one
   operation per output element is not the count. `tolerance()` where the
   kernel's contract is not what the output is held to (a data mover
   returns `Tolerance.exact()`).
6. `test = Testing(cases, draw=...)` on the class. A tolerance that is not
   exact says where its number comes from in `note=`. Every operator
   without a `test.py` of its own has at least one `bench=True` case in
   the default suite, large enough that
   dispatch overhead (about 160 us) does not dominate, and a `lower=True`
   case for each layout or dtype its first default case does not reach.
   `iron/tests/operators/test_catalog.py` runs every declaration; a test with a
   body of its own goes beside the operator as `test.py`.
7. Import it in `iron/operators/__init__.py` (an flm port in
   `iron/operators/flm/__init__.py`).

### What an operator overrides

| Hook | Required | Runs |
|---|---|---|
| `build()` | yes, unless an `Elementwise` base builds it from `kernel()`/`chain()` | once per build |
| `reference(*inputs)` | unless a kernel's contract already is one | in tests and the graph reference |
| `resolve(dev)` | if the class declares a `tunable()` | the first time it meets a device |
| `validate()` | no | at construction |
| `compatible()` | no | once every tunable is resolved |
| `sequence(rt)` | no | building the runtime sequence |
| `tolerance()` | no (the kernel's contract) | judging a device run or a check-mode step |
| `ops()` | no (one per output element) | a test's throughput figure |
| `extent_unit(buffer)` | no | splitting a bounded call's rows over a round-robin stream |
| `array_device()` | no (the bound device) | when the array covers part of the device (GEMM) |
| `xclbin_operator()` | no (itself) | locating the xclbin a shipped subclass runs |
| `exported_design()` | no (the derived module) | compiling a hand-placed design in its place |

Construction is keyword-only (`GEMV(M=..., K=...)`) and never records.
Inside a graph's `body()`, `GEMV.step(w, h, **kw)` records a step and
returns a handle, as calling an instance, `op(h, **values)`, does. Outside
a graph, `op(*tensors)` compiles once and runs on the device.

## Graphs

A graph is a subclass of `iron.Graph` whose `body()` is recorded on handles,
once per input shape, compiled to one image per shape (a version) and
called per token. Its docstring and `compile`'s say how inputs, per-call
values, weights, state and profiles are named. The rules:

- A capability a model needs is an operator when it is new compute, and a
  graph when it composes operators the library has (`iron.lm`'s
  `LogMel`, `Conv2d`, `ImagePatches`). A model calls such a graph in its
  body rather than copying its steps.
- Tunables come from the graph's `profile`, not keywords at every call: a
  JSON file per device, one entry per operator class and shape, matched on
  the fields the operator is constructed with (key MHA by `seq_pad`, not
  `seq_len`). `iron/applications/llama/profiles/` is the worked example;
  the nightly trends, not a test, say whether a profile pays off.
- `compile(full_elf=None)` picks one full ELF on NPU2 and an xclbin per
  step on NPU1 (`iron/common/image/packaging.py`; `Graph.compile` logs
  why at INFO). `check=True` runs each step on its own dispatch against its
  reference and raises at the first step outside its tolerance.
- `graph.reference(...)` runs the body through each operator's
  `reference()` on the host.

`iron/applications/llama/model.py` is the worked example;
`iron/tests/common/test_graph.py` records it device-free and
`iron/tests/toolchain/` builds it.

## Design rationale and known limits

Check the code before relying on a line here; it is the authority.

### Rationale

- **One array, every extent.** `build()` sees only the key's parameters, and
  trip counts are per-call values the sequence writes, so one build serves many
  shapes. `iron/tests/toolchain/test_array_identity.py` compares core ELFs built
  at two extents.
- **Length-free extents.** A per-call bound (`x[:n]`) is mlir-aie's runtime
  transfer length, in whole 16-byte units. GEMM bounds its compute, not its
  DMA; MHA moves only the key and value blocks up to the bound, so attention
  over a cache costs the context, not the cache.
- **One compile, any context.** A decoder is two versions, a decode step
  and a prompt chunk; `max_seq_len` sizes only the caches and the RoPE
  table. Caches are `(max_seq_len, num_key_value_heads, head_dim)` so a
  call's write is contiguous and no descriptor strides by the context.
  `tests/applications/long_context/`'s
  `test_nothing_grows_with_the_context` holds every decoder to this.
- **DMA descriptors.** A pattern past one buffer descriptor's limits is
  split by the compiler; one whose size a call bounds must fit a single
  descriptor (`operand.fits`, `operand.split`).
- **Placement.** Tile placement is left to aiecc's placer unless a physical
  invariant needs a pin (MHA's shared-L1 P*V cores) or the placer fails
  (GEMM's shim tiles; `GEMMPlacement`). A placement choice can be an
  `Enum`-annotated tunable, searched over its members.
- **`Elementwise` is not upstream's `transform_parallel`**: its trip count is
  a `Value`, the library owns its sequence, and it has its own column
  budget.

### Not built, or limited

- An xclbin image is one dispatch per step; several steps in one xclbin
  dispatch are refused.
- A full ELF call is one command however long it runs: a prompt chunk's
  attention grows with the context, and a tower's with its image. The
  driver's command timeout must cover the longest, as the README's
  [installation](README.md#installation-linux) sets it.
- Tuning times each operator alone, not inside the image it runs in.
  Kernel cycle counts skip only GEMM settings, only on npu2, and never with
  a column-major B.

## Tests

```python
from aie.utils.verify import Tolerance
from iron.common.testing import run_test, vectors
from iron.operators import Tanh

op = Tanh(size=2048, num_aie_columns=1, num_channels=1, tile_size=2048)
errors = run_test(op, vectors(op), tolerance=op.resolved().tolerance())
assert not errors, errors
```

- A test that dispatches is marked `@pytest.mark.supported_devices(...)`
  and nothing else; conftest.py releases the runtime after it.
- `run_test(..., record=record_property)` writes latency, bandwidth and
  throughput to the CSV; any other figure goes to `record_property`.
- IRON is numpy only: `ml_dtypes.bfloat16` for bf16. torch and
  transformers are needed only to record goldens (`pytest <test> --record-goldens -p no:xdist`).
- A bug fix comes with a test that fails without it.

## CI

Each hardware workflow runs one job per runner, Phoenix (NPU1) and Krackan
(NPU2):

- `small.yml`: `iron/operators/` and `iron/tests/`, non-extensive, on
  every PR.
- `extensive.yml`: the same with extensive tests, nightly and on pushes to
  `main` and `devel`.
- `examples.yml`: `tests/applications/`, non-extensive, on every PR: each
  model loaded once for its shortest call (a 13-token prompt, one token
  drawn; an embedding model's or a toy's own checks) and the device-free
  reference tests.
- `nightly.yml`: every `tests/applications/`
  test, extensive ones too, each night: the depth a model's checks have
  (accuracy, determinism, sampling, chat turns, long generations, the
  each-step form, long_context's deep checks); a benched
  TTFT, TPS or Latency 10% worse than the night before's fails it
  (`pretty_trends.py --fail-on`).
- `ci-lint.yml`: `reuse lint` and every pre-commit hook (black, ruff,
  clang-format, actionlint, hygiene) over the repository, and pyright over
  `[tool.pyright]`'s paths in `pyproject.toml` on Python 3.11 to 3.14.
- `pr-comment.yml` and `publish-pages.yml`: the performance trends of a PR
  and the benchmark history site.

On `main` and `devel`, `publish-results.yml`, the only job that can push,
merges each run's `tests_latest.csv` into `{arch}/{suite}/all.csv` on the
`ci` branch (`ci/scripts/merge_results.sh`); `ci/scripts/` turns those into
the PR comment and the charts. Only cases marked `@pytest.mark.bench` (a
`Case(bench=True)`) are tracked, and a metric's unit and direction are named
in `ci/scripts/pretty_common.py`'s `METRICS`.

A run publishes what it got through. `examples.yml` and `nightly.yml` run
each `tests/applications/<name>/` in its own pytest process, so a crash
ends only that model's tests, and conftest.py rewrites the CSV as each test
starts, counting the running test a failed check until it ends: a process
that dies keeps every result before it and names the test it died in. Every
process of one run stamps the run's one date (`--csv-date`), which is how the
reports tell one run from the next.

## Language models

`iron/lm/` is what every language model shares; each model is a package
under `iron/applications/` over it, and nothing in the library imports a
model. This is the one description of that structure; the model READMEs
link here.

The model layer is JAX-shaped and torch-named. A model is a pure function,
recorded into a graph, over an explicit tree of weights; it keeps torch's and
transformers' names so checkpoints load and references compare by name.
`iron.functional` gets a function only once a kernel computes it. Per-tile
programs and their autotuning live at the operator and kernel layer, where
tunables and profiles already do that job.

- `config.py`: `DecoderConfig`, a model's shape from the checkpoint's
  `config.json`.
- `checkpoint.py`: `Checkpoint`, a mapped `.safetensors` (sharded through
  its index, or a PyTorch checkpoint read without torch);
  `tree("read" | "random" | "unread")` is the weights by the checkpoint's
  own names.
- `blocks.py`: the leaf modules that declare their weights with
  `iron.param` (`Linear`, `Embedding`, `RMSNorm`, `LayerNorm`), the blocks
  a layer is made of (`Attention`, `GatedMLP`, `MLP`, `DecoderLayer`,
  `EncoderLayer`, `SandwichLayer`, `PleLayer`), the memory a layer owns
  (`KVCache`, `NoCache`) and the model's `Rope`; and the front-end graphs.
- `model.py`: `Model`, which loads from a checkpoint's directory or
  repository id (`Model.load`, its context fitted to the host by
  `Model.fit`) and generates (`generate(prompt, max_tokens, sampler=None)`,
  `stream`, timings on `model.stats`); its `renames` maps a checkpoint's
  module names to the parts'. `Model.cpu_reference()` is what
  a model is judged by: transformers' logits recorded in `golden.npz`
  beside the checkpoint (`golden.py`), or with drawn weights the graph's
  own reference on the host (`OnHost`, which runs it in place of the
  device).
- `causal.py`: `CausalLM`, a decoder as one graph of a prompt chunk and a
  decode step, its modules a `Decoder` of `layer_class` layers.
- `session.py`: `Session`, one conversation over a decoder's loaded
  versions (the tokens its caches hold, `logits` and the draws); a model's
  `session` is the one `logits` and `generate` run in, and several share
  one model.
- `encoder.py`, `multimodal.py`: `Encoder` and `Tower`, and
  `Multimodal`.
- `cli.py`: `main`, the command line every model shares (`--help` lists
  its options, `-v` logs iron's INFO lines), and `exports`, a model
  package's lazy `__getattr__`.
- `generation.py`, `testing.py`: sampling and the device tests' checks;
  they need only `logits(tokens)`. `tune.py`: `python -m iron.lm.tune`.

A model's device test is `tests/applications/<name>/test.py` and imports
its application as `iron.applications.<name>`: CI's example suite runs
`tests/applications/`, and the benchmark history names a row by that
directory. A decoder's device-free test is
`tests/applications/<name>/reference/test.py`.
