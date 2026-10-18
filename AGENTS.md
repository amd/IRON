<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# AGENTS.md

This file provides guidance to AI coding agents when working with code in this repository.

## Overview

IRON is a close-to-metal Python API for AMD Ryzen™ AI NPUs (XDNA architecture). It provides language bindings around the MLIR-AIE dialect to enable fast and efficient execution on NPU hardware.

**Key Technologies:**

- **MLIR-AIE**: Dialect for programming AMD AI Engines (AIE) array architectures
- **XRT (Xilinx Runtime)**: Low-level runtime for interfacing with NPU hardware
- **Target Hardware**: AMD Ryzen AI NPUs (AIE2/AIE2P architectures - NPU1/NPU2)
- **Primary Datatype**: bfloat16

## Environment Setup

```bash
# 1. Source XRT (required for all operations)
source /opt/xilinx/xrt/setup.sh

# 2. Create virtual environment (may already be present)
python3 -m venv ironenv

# 3. Activate virtual environment
source ironenv/bin/activate

# 4. Install dependencies
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt
```

**Note:** `requirements.txt` pins an mlir-aie release wheel, which brings the
kernel library (`aie_kernels/`) and finds the Peano wheel by itself.

**Note:** XRT must be sourced before running any tests or operators.

### Where build outputs go

Compiled artifacts (`.xclbin`, `.bin`, `.o`, the full ELF) live in
mlir-aie's JIT cache, keyed on the content that produced them:
`~/.npu/cache/<hash>/`, or wherever `NPU_CACHE_HOME` points. Nothing is
written to the working directory.

### Environment Variables

- `IRON_EXAMPLE_WEIGHTS_DIR`: Path to language model weights (default: `/srv`)

## Building and Testing

### Run All Operators (non-extensive tests)

```bash
pytest iron/operators/ iron/tests/ -m "not extensive"
```

### Run Extensive Test Suite

```bash
pytest iron/operators/ iron/tests/
```

### Run Single Operator Test

```bash
pytest iron/tests/operators/catalog.py -k AXPY   # a declared Testing
pytest iron/operators/flm/              # an operator with a test of its own
```

### Run Application Tests

```bash
pytest tests/applications/
```

### Run Specific Test Function

```bash
pytest iron/tests/operators/catalog.py -k relu
pytest iron/tests/operators/catalog.py -k GEMM
```

### Parallel Testing (faster)

```bash
pytest iron/operators/ iron/tests/ -n auto -m "not extensive"
```

## Code Style and Linting

### Python (Black)

```bash
# Check formatting
black --check .

# Auto-format
black .
```

### C++ (clang-format)

```bash
python scripts/clang-format-wrapper.py --fix
```

### License Compliance (REUSE)

```bash
# Check all files have proper license headers
reuse lint
```

## Architecture

### Structure

1. **Operators** (`iron/operators/`)
   - One operator is one module: `relu.py` for a small one, a directory with
     `op.py` for one that also has a design, a reference, a README or a
     device test of its own (`flm/gemm/`). `flm/` holds the
     FastFlowLM ports (`flm.GEMM`, `flm.DequantBFP`) and their weight
     packing, exported from its own
     package (`from iron.operators.flm import GEMM`) as well as
     `iron.operators`'s one catalog, dotted (`_OPERATOR_MODULES["flm.GEMM"]`,
     what a `Profile` names it by); flm's GEMM is not `iron.operators.GEMM`.
   - An operator module holds:
     - the operator, one class (`iron/common/declare/`): `Param()` fields for what a host shape
       names, `Auto()` tunables `resolve(dev)` fills from the device and the
       extents (a tunable is an `Auto()` field: the caller or a profile may
       give it, and the library resolves it when neither does), `In`/`Out`
       operands (mlir-aie's `aie.iron.In`/`Out`/`InOut` markers, with a
       declared shape) whose `obj_type=` makes each its own stream into the
       array (`per=` a column count), `Value`
       members the cores read (trip counts, derived from the extents so the
       array never depends on them), a nested `class Array(Operator.Array)`
       whose `build()` builds ObjectFIFOs and Workers and binds each
       operand's lane to a fifo's shim end, and optionally `sequence(rt)`
       when the runtime sequence is not the derived one. The array tier is
       the fields the `Array` reads: what an `obj_type=` names and what is
       declared `array=True`; one array serves every extent. A shipped binary
       is a subclass declared with `image=Xclbin(...)`, its operands pinned
       by its `Array.build()` (`operand.pin([DmaEndpoint(...), ...])`, each lane on a shim channel of the image). Two hooks change what is built: `xclbin_operator()`, the
       operator whose xclbin this one runs (itself by default; flm's GEMM
       returns its shape-free half, so one xclbin serves every shape), and
       `exported_design()`, a callable returning the module (an
       `ir.Module` or its text) for a hand-placed design (flm's
       DecodeLayer, PrefillAttention and LMHead) in place of the derived one.
     - The operator's `reference(*inputs)` is the CPU reference the tests
       and the graph reference run; `vectors(op)` in `iron/common/testing`
       draws random inputs for its declared buffers and takes the outputs
       from it. An `Elementwise` operator has none of its own: its kernel's
       contract is the reference. A composite builds its reference from its
       kernels' contract references where it can, and says why where not.
     - `tolerance()`, what every output is judged by, in tests, a graph's
       check mode (`compile(check=True)`) and autotuning alike: the contract of the kernel it runs unless
       it overrides it (a data mover returns `Tolerance.exact()`: any other
       accepts a wrong permutation). A tolerance with a number names in its
       `note` where the number comes from (`iron/tests/common/judging.py`).
     - `test = Testing(cases, ...)` on the operator class
       (`iron/common/testing.py`): the shapes it is checked at on a device
       and any `draw=` its inputs need. One module,
       `iron/tests/operators/catalog.py`, runs every declaration against
       `reference()`. An operator whose device test is more than that (a
       composite compared step by step, a shipped binary against its own
       accumulator) keeps a `test.py` beside it.

2. **AIE Kernels** ([mlir-aie `aie_kernels/`](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels))
   - C++ compute kernels, sourced from the installed mlir-aie package
     (`aie.utils.config.aie_kernels_dir()`), not from this repo. Operators get
     them from mlir-aie's kernel factories (`aie.iron.kernels`), each of which
     returns an `ExternalFunction` carrying its source, flags, symbol and
     argument types, and in `.contract` the reference it computes, the
     tolerance its output is held to and the scalars it binds
   - Grouped by family (`activation/`, `eltwise/`, `linalg/`, `norm/`,
     `fused/`, `common/`, ...), not by architecture: a kernel's `.cc` includes
     its `*_aie2.h` or `*_aie2p.h` header, chosen by `aie_arch.h`
   - Use AIE API for vectorization (e.g., `aie::mmul`, `aie::add`, `aie::mul`)
   - Compiled to `.o` files and linked into operator `.xclbin`

3. **Common Infrastructure** (`iron/common/`)
   - `declare/`: the declaration layer (`Operator`, its `Param`/`Auto` fields (`Param()`/`Auto()` return the plain `dataclasses.Field`, its `ParamSpec`/`AutoSpec` in the field's metadata and read back with `ParamSpec.of(f)`; each field is its own dimension reference, `GEMV.K` in a shape and `vars(op)["K"]` on an instance),
     operands (`Operand`: `op.x` is the declared operand bound to the
     instance, its shape and lanes resolved), the `Value` member and its
     `DispatchTime`/`Extent` specializations (`op.value(name)` is the value
     bound to the instance, its device parameter once built),
     `Xclbin` and its
     `fetch()`, inference; `cls.declaration`, a `Declaration`, is what a
     class declares, read once as its body finishes: its members and which
     fields are parameters, tunables, array-tier or probed). A domain's
     bound (`Divisors(of=, step=, cap=)`) is an integer or a callable of the
     operator and the device, as is `when=`; a fixed tuple is a domain too,
     and an `Auto` field annotated with an `Enum` and given no domain is
     searched over that `Enum`'s members. An operator's shim budget, `shim_columns`, is
     the bound device's `shim_dma_channels_in`/`out`; its `residents` the
     derived values the preamble writes once per build
   - `design/`: the library-owned build: `OperatorDesign(op, image)`,
     whose `module()` is the MLIR module for one operator and which
     mlir-aie's `CompilableDesign` compiles and caches; `OperatorRuntime`,
     the operator's sequence as an aie.iron `Runtime` subclass (what
     `sequence(rt)` receives; the derived sequence, each operand's
     `transfers()`, a pinned lane's shim DMA tasks)
   - `graph/`: graphs (`iron.Graph`, `iron.state`) and
     `compile(dev=, full_elf=, coresident=, profile=, precision=)`
   - `image/`: what a graph lowers onto, all of it internal:
     `OperatorSequence(traced)`, what a `TracedGraph` becomes (its steps
     as `SequenceStep(op, buffers)`, each buffer a `BufferRef(root, start,
     nbytes)` a handle's `ref()` gives: a whole buffer of the image, or
     `nbytes` of it from byte `start`), the buffer allocator (`LiveRange`,
     `Pool`, `ArenaPlan`), `Fusion` (the designs of a sequence as one
     module, a `DeviceConfiguration` per array or pack composed by
     mlir-aie's `Program.compose`),
     `FusedImage`/`XclbinChain` (the full ELF or the chain of xclbins it
     links; a design whose `xclbin_operator()` is another operator, or a
     shipped image, runs that xclbin rather than a link of its own), an
     operator's own image (what an operator called outside a graph runs,
     the one-step sequence `TracedGraph.of_step(op)` as an xclbin chain:
     `op(*tensors)` compiles it once and runs it, `op.compile()` builds it
     and returns its `Artifacts`), the runtime callables (a buffer read
     back by its `BufferRef`) and the record of what a compiled image
     consists of
   - `elementwise.py`: the shared elementwise array and its operand shapes
     (flat, binary, rowwise), and `Sweep`, the cases of an elementwise
     operator
   - `testing.py`: how an operator declares the shapes it is tested at
     (`Testing`, `Case`), and the device test harness: `vectors` draws an
     operator's inputs and its reference's outputs; `run_test` compiles,
     dispatches, judges and times it, `time_call` the timing alone, for a
     graph test that needs no judgement; a single buffer is judged with
     mlir-aie's `aie.utils.verify.compare`. A test's figures go to
     pytest's `record_property`, which the root conftest writes to the CSV.
     The reference and the judgement are the operator's own:
     `op._call_reference(inputs, outputs, values)` runs `reference()` on
     buffers by name, `op.judge(inputs, written, tolerance)` returns a
     `Verdict` per written buffer
   - `tracing.py`: `dump_traces(run, trace_file)`, for a sequence holding an
     operator built with `trace=` (mlir-aie's `TraceConfig`); the workers
     traced are those its `Array.build()` gives `Worker(trace=)`, else its first.
     A test that traces builds its own `TraceConfig`

4. **Tuning** (`iron/tune/`), at the edge: it depends on the graph core
   and nothing in the core imports it
   - `measure.py` times settings of one design on the NPU, interleaved
     round by round with the traced setting, and caches each time by its
     build, per-call values and inputs (`Cache`); `judge` admits a setting
     whose output differs only within both its own and the traced
     setting's `tolerance()`
   - `autotune.py` times every setting of each operator shape a model's
     calls run (coordinate descent past 32) and writes the fastest that
     beats the traced one by two standard errors as a `Profile` entry. It
     does not build a GEMM setting whose matmul kernel alone, at the cycles
     per call mlir-aie's nightly published for its `recipe_key` and the
     core's clock (`CORE_MHZ`), is slower than the fastest setting timed
   - `cli.py` times one operator at every setting it tunes to
     (`python -m iron.tune.cli GEMV M=2048 K=8192`) and holds the parser
     `python -m iron.lm.tune <application>` builds on, which rewrites the
     application's `profiles/<device>.json`

### Key Concepts

**ObjectFIFO**: Data movement primitive in MLIR-AIE

- Connects producers and consumers (shim DMA ↔ compute tiles)
- Uses `acquire()` to get buffer access, `release()` to free it
- Pattern: always pair acquire with release in loops

**Worker**: Compute tile task

- Wraps a Python function that runs on AIE compute core
- Function uses `range_()` for loops (not Python `range`)
- Calls compiled C++ kernels via `Kernel` objects

**TensorAccessPattern (TAP)**: Describes how data is sliced and distributed

- Used to parallelize work across multiple columns
- Format: `(tensor_shape, offset, dimensions, strides)`

**Runtime Sequence**: Host-side control flow, an aie.iron `Runtime`
(`OperatorRuntime`). The library derives it from the operator's declaration
(each buffer split over its stream's slots); an operator that needs a
different order overrides `sequence(rt)`:

- `self.A.fill(tap, lane=i, group=tg)`: DMA data from host → NPU (shim →
  L2/L1), mlir-aie's `ObjectFifoHandle.fill` on the operand's lane `i`
  (left out of a one-lane operand only); `source=` moves another operand's
  data through this one's lane
- `self.C.drain(tap, lane=i, group=tg, wait=True)`: DMA data from NPU →
  host; `wait=False` is the default, as upstream's
- `tg = TaskGroup()` ... `tg.finish()` (mlir-aie's): awaits and frees a
  group's transfers; `TaskGroup.pipelined(n)` keeps a step's in flight
  while the next is issued
- `tap` is a slice of the operand (`self.A[:, r0:r1, :]`) or any
  `TensorAccessPattern` over it, all of it when left out; the compiler
  splits a constant pattern no one descriptor holds
- per-call words are a `Value` of the operator, under upstream's names:
  `offset_parameter=`, `length_parameter=` (with `length_unit=`, the
  elements one unit counts) and `repeat_parameter=`

**Per-call values**: `Value()` members (`dtype=np.int32` by default) are
patched into descriptors or read by cores without a rebuild; `DispatchTime()`
members regenerate the sequence per call (xclbin only). A graph binds them to
keyword-only parameters annotated `iron.Scratchpad[T]`, `iron.Carried[T]` or
`aie.iron.DispatchTime[T]`. The parameter scratchpad exists on a full ELF only
(XRT's `get_ctrl_scratchpad_bo` serves a module run), so on an xclbin image a
scratchpad value lowers to a dispatch-time scalar: an offset use regenerates
the stream, a core-read use is a write of the scalar into the core's
runtime parameters. Arithmetic on a value is an expression of it; a view's
index may floor by a power of two (`slots[position // 2048]`), be held
to a range (`rows[iron.clamp(position - 512, lo=0)]`) and wrap by a power
of two after it (`ring[position % 4096]`), which the host, the reference
and a device loop's Emit all compute, while a bound (`x[:n]`), which
patches a length, stays linear. A run of fixed width from a per-call
start, `x[s : s + W]`, then bounded, `[:n]`, is a view any axis one
descriptor walks takes; every call is checked to keep `s + n` (or, not
bounded, `s + W`) inside the axis, so `W` may pass its end.

**Compilation Flow**:

```text
op.py (X.array + X.sequence or the derived sequence)
    ↓
iron.common.design.OperatorDesign.module (library-owned Runtime/Program)
    ↓
MLIR (.mlir file)
    ↓ (aie-opt + aie-translate via Peano toolchain)
xclbin (NPU binary) + insts.bin (instruction sequence)
```

**No build context.** An operator takes the device that is current and
nothing else. Everything else is a fixed path (`aie.utils.config.aie_kernels_dir()`), an
environment choice (`MLIR_AIE_KERNEL_SOURCES`), or a keyword on the build
itself (`compile(full_elf=False)`). On a host without an NPU, bind one to
resolve and compile against: `aie_utils.set_current_device(from_name("npu2",
n_cols=8))` (`aie.iron.device.from_name`); the test tree's `npu2` fixture
does that and restores the previous device. Kernels are built with Peano; IRON has
no xchesscc path, and a kernel that needs one asks the `aie.iron.kernels`
factory for it (`use_chess=True`) rather than IRON carrying a global flag.

**Runtime**: `aie.utils.DefaultNPURuntime` loads an image and runs it,
shared across operators. A device test is one marked
`@pytest.mark.supported_devices(...)`; conftest.py releases the runtime
after it (`aie.utils.cleanup_npu_runtime()`), or after its module's last
test when a module- or class-scoped fixture may hold an image its tests share.

## Hardware Constraints

### NPU Architecture Limits

- **NPU1 (AIE2)**: 4 rows × 4 columns (AMD Ryzen AI Phoenix/Hawk Point)
  - It has 5 columns, but only 4 are accessible.
- **NPU2 (AIE2P)**: 4 rows × 8 columns (AMD Ryzen AI 300 Series "Strix Point", Ryzen AI 9 HX 370 "Strix Halo", Krackan)

### Tile and Dimension Constraints

Common operator parameters and their constraints:

- `tile_size`: Typically 64, 128, 256, or 4096 (depends on operator and data type)
- `num_aie_columns`: Must match hardware (1-4 for NPU1, up to 8 for NPU2)

**GEMM-specific**:

- `tile_m`, `tile_k`, `tile_n`: Matrix tile dimensions (typically 64)
- Minimum tile sizes depend on `precision` (`iron.Precision`):
  - `MEDIUM` (default, bfp16 macs): 8×8×8 minimum
  - `HIGH` and `HIGHEST`: 4×8×8 minimum
- Matrix dimensions must be multiples of `tile × num_rows/columns`
  - `M % (tile_m * n_aie_rows) == 0`, the rows the bound device's
    `core_rows` names (4 on NPU1 and NPU2)
  - `K % tile_k == 0`
  - `N % (tile_n * num_aie_columns) == 0`

**Element-wise ops** (add, mul, relu, gelu, etc.):

- `size % (num_aie_columns * num_channels * tile_size) == 0`, with `tile_size` at most the class's `tile_cap` (4096 elements unless it says otherwise); left out, the column count is the most that divide

### Memory Hierarchy

- **L3**: Host memory (DDR)
- **L2**: Shared memory tiles (MemTiles in AIE-ML)
- **L1**: Per-core local memory (limited, ~32-64 KB per tile)

Data movement pattern: L3 → Shim DMA → L2 → L1 (tile local) → Compute

## Adding a New Operator

1. Create `iron/operators/<operator_name>.py` (a directory with `op.py` only
   if it needs more than one module: a hand-written design, its own
   reference, a README, a device test of its own)
2. Declare the operator (`class X(Operator)`):
   - `Param()` fields for what a host shape names; `Auto()` tunables, filled
     by `resolve(dev)` from the device and the extents
   - `In`/`Out` operands by shape, each with its `obj_type=` in the units a
     core reads (`per=` a column count): an operand with an `obj_type=` is
     its own stream of `op.x.lanes` lanes, `op.x.obj_type` the fifo type;
     `when=flag`, a bool `Param()`, makes an operand (and its stream) exist
     only where the flag is true; a call gives it by keyword, its name,
     which sets the flag (`RMSNorm.step(x, weight=w)` is `weighted=True`)
   - a `Value(derive=...)` for every trip count the core reads, so the
     array never depends on the extent; what else the array bakes is a
     field declared `Param(array=True)` (or `Auto(array=True)`)
   - which of these computes a quantity from other fields depends on who
     reads it:

     | Reads it | Declare |
     |---|---|
     | Host Python, never a field itself | `@property` |
     | A compile-time field a caller may still override (`check_derived` catches disagreement) | `Param(derive=lambda op: ...)` |
     | A tunable `resolve(dev)` always fills, never a caller's | `Auto(init=False)`, given by `resolve`'s `self.replace(...)` |
     | A core, as a trip count or scalar | `Value(derive=lambda op: ...)` |
   - `class Array(Operator.Array)`: the array tier, a frozen dataclass the
     class generates with every field a stream names, every field declared
     `array=True` and every operand and value; it annotates only the
     library's views it reads (`dev: Any`, `buffers: list[Operand]`), and
     `op.array_config()` makes it from the operator. `build() -> Built` builds ObjectFIFOs and Workers
     (`self.kernel()` or a factory's `ExternalFunction`), `range_()` for
     loops, and `self.x.bind([f.prod() for f in fifos])` (a handle per lane)
     for every streamed operand. The values the cores read are their
     runtime parameters, `rtps = [Rtp([self.count, ...]) for _ in
     range(n)]`, one per core given as a Worker argument; in the core,
     `words = rtp.read()`
     waits for the sequence and returns each word keyed by its value
     (`words[self.count]`), whether the build wrote it into the core's
     buffer or made it a scratchpad word (`self.count.in_scratchpad`, a
     per-call value on a full ELF). `self.count.per_call` says whether a
     call gives it, and `self.x.l1_depth` is the depth a core-side fifo of
     `x`'s tiles can have. The device is `self.dev`. It returns
     `Built(objects, rtps)`: its Workers and any `Flow`, `Lock`, `TileDma`
     or `Buffer` only the sequence reaches, so each is in the design
     whatever a shape's sequence touches, and every core's `Rtp`. What the
     sequence programs beyond those rides a `Built` subclass of its own,
     read back as `rt.built`. It sees the array tier alone: an extent is no
     field of it
   - `compatible()` for divisibility against the resolved tunables
   - `sequence(rt)` only if the derived sequence is not the one you want:
     `self.A.fill(tap, lane=i)`, `self.C.drain(tap, lane=i, wait=True)`
   - see `iron/common/elementwise.py` for the elementwise families, and
     `gemm.py` or `mha.py` for hand-written sequences
3. A shipped binary is a subclass declared with the image, `class
   Shipped(X, image=Xclbin(url=, sha256=, filename=))`: it pins the tunables,
   and its `Array.build()` builds no cores: it pins each operand's lanes to the
   image's shim channels (`operand.pin([DmaEndpoint(Tile(c, 0), MM2S, ch),
   ...])`, returning the endpoints), places the image's parameter block in each core,
   `Buffer(address=)`, which holds its derived `Value`s' words in
   declaration order (`Value(words=)` for a block of several), and returns
   the `Lock(lock_id=)` the sequence releases it with, on its own `Built`
   (`rt.built`). It takes no per-call
   value. `Xclbin` is mlir-aie's `NPUKernel`, fetched on first read of
   `xclbin_path`; a build runs its `with_instructions(insts)`
4. Name the kernel with a factory from `aie.iron.kernels`
   (`eltwise.relu_sized(line)`, `norm.rms_norm_eps(tile)`, ...): it carries
   the symbol, the source, the argument types, aie2's LUT tables and the
   contract: the reference, the tolerance and the scalar bindings. The
   factory binds the line length; a scalar the kernel takes at run time is
   its `Array`'s `scalars()`, in the kernel's order (`AXPY` returns
   `(self.scalar_factor,)`, `RMSNorm` `(self.epsilon,)`; the factories take
   no `a=` or `epsilon=`),
   so the operator declares no `kernel_call` or `reference` of its own; a
   field it passes is declared `array=True`. An elementwise operator
   whose core makes more than one call over a line lists them in `chain()`,
   each a `KernelCall(kernel, scalars, operands)` naming its input tiles by
   operand (`(self.x,)`, or `None` for the line the call before it wrote).
   Bind a further symbol of the same object with
   `fn.object_file.bind(symbol, arg_types)`. A kernel the factories do not
   cover is an `ExternalFunction` of mlir-aie's whose `symbol_prefix=`
   names its configuration (the compile flags that are the operator's
   own, as `merge.py` does), so two configurations of it link into one
   image; a factory prefixes its symbols with the digest of its source
   and flags itself. With `source_string=` it is one written in the
   operator's own file (the hello-world in
   `iron/tests/toolchain/inline_kernel.py`: a `vadd` in C++ text, the
   argument types the operands' tiles). Give such a kernel its
   `contract=KernelContract(roles=, parameter_bindings=, reference=,
   tolerance=)` and it is used like a factory's: `KernelContract` and the
   `Param` role come from `aie.iron.kernels`, the `In`/`Out` roles from
   `aie.utils.compile.jit.markers` (`In`, `Out`, `Param` and
   `DispatchTime` each name one thing in aie.iron and another in
   `iron.common`, so a module using both imports aie.iron's qualified:
   `markers.In`, `kernels.Param`, `aie.iron.DispatchTime[T]`), and `tolerance=` is what its output is
   judged by on the device (`Tolerance.bf16_ulps(1, atol=2**-126)` for a
   bf16 result rounded once, as `eltwise`'s factories give); without it
   the catalog refuses to judge the operator. An operator running one kernel
   reports its contract from `tolerance()` (`Elementwise` does this
   from `kernel()`); both, like `ops()`, are asked of the resolved
   operator, `op.resolved().tolerance()`. If a new C++ compute kernel is needed, add it
   to the
   [mlir-aie kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)
   with a factory in `aie.iron.kernels`; IRON hosts no kernels
   - Choose the family directory (`activation/`, `eltwise/`, `linalg/`, ...);
     put architecture-specific code in `*_aie2.h` / `*_aie2p.h` headers
   - Use AIE API for portable vectorization when possible
   - Add `event0()` and `event1()` for performance profiling
5. Give the operator a `reference(*inputs)` only where its kernel's contract
   is not already it (numpy, on the declared shapes: upcast to float32,
   compute, round once; from the contract references of the kernels it
   runs where it can), and an `ops()` where one operation per output
   element is not its count (`2 * M * K * N` for GEMM, 0 for a data mover):
   `run_test(..., record=record_property)` records throughput from it.
   Override `tolerance()` where the contract of the kernel it runs is not
   what its output is held to, returning an `aie.utils.verify.Tolerance`
   (`Tolerance.exact()` for a data mover)
6. Declare how it is tested: `test = Testing(cases)` on the operator class,
   from `iron.common.testing`
   - the cases are `Case(kwargs, extensive=...)`, plain kwarg dicts, and
     callables of the class returning them when they follow the device's
     width: `Sweep(...)` is the elementwise one (at the regular length one
     core and the widest grid the shim budget allows, at the others the
     smallest and the largest tile; `channels=None` for a binary operator,
     `rows=True` for a rowwise one, further keywords given to every case)
   - `extensive=True` keeps a case out of the default suite
   - `bench=True` marks the cases CI tracks over time (`pytest.mark.bench`).
     Every operator needs at least one, in the default suite. Pick an input
     large enough that dispatch overhead (~160 us) does not dominate the
     measurement; a case that finishes near that floor measures little, so
     an operator no input takes past it gets its least noisy case. `Sweep`
     adds one at `BENCH_ELEMENTS`
   - `lower=True` adds a case to the device-free lowering gate
     (`iron/tests/toolchain/lowering.py`), which lowers each operator's
     first default case on every device: flag one for each layout or dtype
     that case does not reach (`Sweep(lower=True)` flags its first)
   - `draw=`, a callable of the operator, returns `vectors()`'s arguments
     keyed by its operands: `normal=(op.A,)`, `centered=(op.x,)`, and
     `given={op.angles: table}` for a tensor or a shape an input with
     preconditions needs (a packed quantization, an angle table)
   - `iron/tests/operators/catalog.py` runs it; a test with a body of its own goes
     beside the operator and calls `run_test(op, vectors(op), ...,
     record=record_property)`, and gives pytest's `record_property` any
     figure beyond latency, bandwidth and throughput
   - a shape the operator must *refuse* goes in
     `iron/tests/operators/rejected_shapes.py`, which needs no device
7. Register operator in `iron/operators/__init__.py` (`_OPERATOR_MODULES`:
   the name, and the module that defines it; an flm port's own name and
   module go in `_FLM_OPERATOR_MODULES` beside it, the one place both its
   package and the dotted catalog entry read) and in `__init__.pyi`, so a
   type checker sees the lazily-loaded name too

### What an operator overrides

| Hook | Required | Runs |
|---|---|---|
| `Array.build()` | yes, unless an `Elementwise` base builds it from `kernel()`/`chain()` | once per build, to generate the array |
| `reference(*inputs)` | yes, unless a kernel's contract already is one | by `run_test`/the graph's own reference, on host tensors |
| `resolve(dev)` | yes, if the class declares an `Auto()` tunable | once, the first time the operator meets a device |
| `validate()` | no (a no-op) | at construction, before `array_key`/`design_key` can be taken |
| `compatible()` | no (a no-op) | once every tunable is resolved, device-free |
| `sequence(rt)` | no (the derived one serves most operators) | building the array's runtime sequence |
| `tolerance()` | no (the kernel's contract, else `None`) | judging a device run or a check-mode step |
| `ops()` | no (one op per output element) | a device test's throughput figure |
| `extent_unit(buffer)` | no (`None`: the stream tile's own rows) | splitting a bounded call's rows across a round-robin stream |
| `array_device()` | no (the bound device) | building the array, when it covers only part of the bound device (GEMM's row subset) |
| `xclbin_operator()` | no (itself) | locating the xclbin a shipped subclass runs (flm's GEMM, one image for every shape) |
| `exported_design()` | no (`None`: the derived module) | compiling, in place of the generated MLIR (flm's hand-placed designs) |

Inside a graph's `body()`, a step is spelled `GEMV.step(w, h, **kw)`: a
classmethod that records a step on the active tracer and returns a handle,
never an instance; outside a body it raises. Calling an already-constructed
instance inside a body is `op.apply(*operands, **values)`; `op(*npu_tensors)`
still runs the operator on the device. Construction is keyword-only
(`GEMV(M=..., K=...)`, as written above) and never traces, with or without a
body around it. A graph's own `profile` reaches every step its tracer
constructs without the body passing one explicitly (`Tracer(name, profile)` makes each step
with `profile.make(cls, **given)`); standalone use of the same profile
calls it explicitly, `profile.make(Cls, **kw)`.

## Graphs

Operators compose into a graph: a subclass of `iron.Graph` whose `body()`
is called on handles, traced once per input shape, compiled to one image
per shape (a version) and called per token. Inputs are `body`'s positional
parameters, outputs its return values, per-call values its keyword-only
parameters annotated `Scratchpad[T]`, and weights and `iron.state(...)`
device-resident state what the instance holds, named by attribute path
(`self.layers[3].q` is `layers.3.q`):

```python
import iron
import iron.functional as F
from iron import Scratchpad
from iron.operators import Copy

class Decode(iron.Graph):
    def __init__(self, weights, angles):
        self.weights = weights                   # a namespace of arrays: weights
        self.rope = iron.weight(angles)          # (max_len, head_dim)
        self.k = iron.state((max_len, head_dim)) # positions first, as iron.lm's caches

    def body(self, x, *, pos: Scratchpad[np.int32]):
        w = self.weights
        h = F.rms_norm(x, (emb,), w.norm)        # each function infers the extents
        angles = Copy.step(self.rope[pos]).reshape(1, head_dim)  # gathered on the NPU
        self.k[pos] = F.rope(F.linear(h, w.wk), angles)  # a copy into the state
        return x + F.linear(h, w.wo)             # + - * / @ on handles are steps too

graph = Decode(weights, angles)
graph.compile(x=(1, emb))                        # or on the first call
y = graph(x_tok, pos=n)
```

A body reads a held array where it is held, with no alias: a numpy slice,
reshape or transpose of it (`w.wk[:E]`) is a view of its buffer, under its
own path. A per-call gather wraps it where it gathers,
`iron.weight(w.embed)[ids]`; one input's ids may gather from any number of
tables, each table once, the host encoding each table's words into the
input's buffer after the last's.

A graph is also how operators compose into a reusable block. Called in
another graph's body, on its handles and per-call values
(`self.log_mel(wave, self.features[1:F + 1], frames=frames)`), a graph's
body traces into the caller's: its steps are the caller's, its weights
and states are named by the caller's path to it (`log_mel.dft`), the
values it is given bound its steps, and the caller's one compile covers
it. It may take an output to write as an input defaulting to None (a
state's rows), and carries no values of its own. On its own it compiles
and runs like any graph, which is how its device test runs it. A caller
that names a part's values itself, carried ones included, traces any of
the part's methods into its body under the part's profile with
`part.inline(part.method, ...)`.

A graph's inputs and per-call values are its `body`'s parameters, checked
as the class is made; a graph whose inputs follow what it holds names them
in `signature()` instead (`iron.lm.Multimodal`'s are its parts'). A
compiled version takes the values it reads (`TracedGraph.reads`) and
ignores the graph's others.

So a capability a model needs is an operator when it is new compute: a
kernel, an array, a data movement no operator has (`iron/operators/`, as
"Adding a New Operator" says). It is a graph when it composes operators
the library has (`iron.lm.blocks`: `LogMel`, `Conv2d`, `ImagePatches`);
a model calls the graph rather than writing its
operators into its own body.

The versions of one graph share its weights and states: a full ELF
version is placed in the graph's one scratch arena. `graph.reference(...)` runs the body through each operator's
`reference()` on host tensors, per-call values and state modelled.

The tunables a graph's operators run with can be a `Profile` rather than
keywords at every call: entries keyed by operator class and shape, the
graph's `profile` attribute (`compile(profile=)` overrides it for one
compile); a directory there holds one per device, `<device>.json`. A call
that leaves a tunable open takes the most specific entry's value; a call that
gives one keeps it. An entry matches on the fields the operator is
constructed with, the call's keywords and the extents inferred from its
operands: key MHA by `seq_pad`, which its shape gives, not `seq_len`, which
follows from it later. A profile is a JSON file, `Profile.load(path)` and
`profile.save(path)`, one entry to a line naming the class in
`iron.operators` (an flm port dotted, `"flm.GEMM"`), then its dimensions
and tunables:

```json
{"entries": [
  {"operator": "GEMV", "M": 2048, "K": 8192, "tile_size_input": 1},
  {"operator": "MHA", "num_heads": 32, "seq_pad": 2048, "num_pipelines": 8},
  {"operator": "MHA", "num_heads": 32, "seq_pad": 1, "num_pipelines": 4}
]}
```

`iron/applications/llama/profiles/<device>.json` is the worked
example (a test at the small shape loads
`iron/tests/common/llama_small_profile.json`), and
`test_llama_names_only_the_tunables_that_matter` checks that each keyword the
graph still passes is one the profile could not have given.

Operators with equal `array_key()` share one array; with equal
`design_key()` they are one build. `compile(dev=, full_elf=, **shapes)`
packages it as mlir-aie's `full_elf` says: one full ELF, or with `False`
an xclbin per step; left `None`, a full ELF on NPU2 and xclbins on NPU1,
and `verbose=True` prints why. `check=True` debugs a graph a step at a
time: each step is its own dispatch, held to its reference on the inputs
the NPU gave it by its `tolerance()`, and the first step outside it raises,
naming the step and its buffers. `coresident=AdjacentPacking()` packs
designs into shared device configurations. `precision=` (`iron.Precision`,
torch's matmul precision levels) is the most any step may round: a step
whose own `precision` rounds more is raised to it. It links the image (`version.image`) and stops
there: the runtime that loads it is made on the first call, so a host with
the toolchain and no NPU can compile ahead of time.
`iron/applications/llama/model.py` is the worked example
(`Llama`, a `CausalLM` from `iron.lm`, called through
`logits(tokens)`, judged by transformers' logits);
`iron/tests/common/graph.py` traces it device-free,
`iron/tests/common/llama_reference.py` runs its reference against
transformers' recorded logits and `iron/tests/toolchain/` builds it.

## Design rationale and known limits

Why the pieces are shaped as they are, and what is not built. Check the
code before relying on a line here; it is the authority.

### Rationale

- **One class per operator, tiers by declaration.** The array tier is
  the fields the operator's `Array` reads, at least what an
  `obj_type=`/`per=` names; `Array.build()` sees that tier alone, so an
  extent cannot leak into a core program. Trip
  counts are `Value`s the sequence writes, so one array serves every
  extent and one build serves many shapes.
  `iron/tests/toolchain/array_identity.py` compiles operators at two
  extents and compares the core ELFs byte for byte.
- **Tunable precedence.** A call site's value, then the graph's profile, then
  `resolve(dev)`, then the `Auto()` default. Identity (`array_key`,
  `design_key`) is taken after resolution, so two calls that resolve alike
  share a build.
- **Packaging is one switch, mlir-aie's `full_elf`**, derived where it is
  left `None` (`iron/common/image/packaging.py`, reported with
  `verbose=True`): a `DispatchTime` value, NPU1 or `check=True` forces
  xclbin; otherwise the image is one full ELF. Full-ELF streams have DDR
  address folding off, so a sequence cannot move between images.
- **Length-free extents.** `Extent(field)` and `x[:n]` bounds are carried
  through reshape and transpose; under a bound a buffer is split
  round-robin by tile. GEMM bounds its compute (M, and on a full ELF K),
  not its DMA; MHA's K and V move only the blocks up to the bound, so
  attention over a cache costs the context, not the cache. A per-call size
  is mlir-aie's runtime transfer length, `fill/drain(length_parameter=,
  length_unit=)`: whole 16-byte units, so a bounded tile is at least 16
  bytes.
- **One compile, any context.** A decoder is two versions, a decode step
  and a `prefill_chunk`-row prompt chunk, both compiled once; `max_seq_len`
  sizes the caches and the RoPE table alone, a row a position, a chunk a
  run of them (`cache[s : s + C][:rows]`, which may pass the buffer's end
  where each call's bound is checked to keep inside it). It is the
  checkpoint's native context where the model fits the host (`Runner.fit`
  logs what it chose), else the longest whole number of chunks that does,
  and a caller may ask for any up to the native one. A prompt runs chunk by chunk
  against the caches, and decode is MHA of one query (a KV group's heads
  packed into the narrowest query block that holds them, over 64-key
  blocks, since the cores compute every row of it; a pipeline's own K and
  V lanes; a group that does
  not divide a block is two overlapping runs of its first and last
  `width` heads, `width` the largest power of two in it). The caches are
  `(max_seq_len, num_key_value_heads, head_dim)`, so a call's write is contiguous
  and no descriptor steps by the context: a `(groups, positions)` cache
  would step `max_seq_len * head_dim` between groups, past a descriptor's
  2^20-granule stride from 32768 rows on.
  `test_llama_does_not_grow_with_the_context` checks that no activation
  or array follows `max_seq_len`, and `tests/applications/long_context/`
  holds every decoder application to it, and to its deepest decode step
  and prompt chunk on the NPU, at its native context.
- **DMA descriptors** (mlir-aie's `verifyStridesWraps`, asked of a pattern
  by `dev.dma_bd_fits(col, row, tap, dtype)`, and of an operand's lane by
  `operand.fits(tap)` and `operand.split(elements)`): the innermost
  dimension holds at most 1023 granules unless the transfer is linear, the
  next at most 1023 elements, the third has no wrap field, and the
  outermost is the iteration count (at most 64) and the only one whose
  stride may be 0. A pattern past them is split by the compiler
  (`aie-decompose-large-dma-bd`), a per-call offset patched into every
  piece; one whose size a call bounds must fit one descriptor, since the
  patch lands in its length.
- **Placement.** Operator order is the final tiebreak for shim tile and
  channel, so a per-column stream is not guaranteed to sit in physical
  column `c`; where that matters, an `Array.build()` pins its lanes
  (`operand.pin`) to shim channels a route of its own reaches. Where the
  tiles an `Array.build()` names are a choice, the choice can be a tunable:
  `gemm.py` declares its own `Enum` of named placements (`GEMMPlacement`)
  and a field `placement: GEMMPlacement = Auto(default=GEMMPlacement.SHIMS)`
  its `Array` reads, left out of a domain since an `Enum`-annotated tunable
  is searched over its own members. `Array.build()` writes mlir-aie's
  `Tile(c, r)`, `Tile(col=c)` or `Any*Tile` (`AnyComputeTile`, `AnyMemTile`,
  `AnyShimTile`) by the resolved member, the hand-found one the default.
  Autotuning times each member the placer takes, like any other tunable.
  GEMM's shim tiles stay pinned regardless of the member: unpinned, a wide
  b_col_maj shape still piles more buffer descriptors onto one shim tile
  than it holds, checked against mlir-aie #3921's placer fixes (533e0c121).
  `mha.py` pins nothing but the two P*V cores a split head shares L1
  between (`pv_cores > 1`, a physical invariant no placer can infer); every
  other MHA tile is left to the placer, checked the same way across its
  catalog, Llama's and EmbeddingGemma 2's shapes.
- **`Elementwise` is not upstream's `transform_parallel`.** They differ in
  the trip count (a `Value` here, folded into the core there), in who
  owns the sequence (the library here, so operators fuse into one image),
  and in the column budget. Splitting upstream's
  `_transform_parallel_gen` would let IRON reuse it.

### Not built, or limited

- A fused sequence in an xclbin (several steps in one dispatch) is refused;
  so are modules. An xclbin image is therefore one dispatch per step.
- A prompt chunk's attention grows with the context: on npu2 (218, Strix
  Halo) a 2048-row chunk takes about 0.83 s plus 0.606 s per 2048 rows
  before it. amdxdna's watchdog stops a command that runs about 4 s past the
  device's last progress (two `tdr_timeout_ms` periods of 2000 ms on kernels
  from 6.17, xdna 2.25; 4 to 6 s on xdna 2.21's `timeout_in_sec` timer). As
  one command a chunk crossed it at about 12.7k tokens, so a full ELF ends
  a command after each step a carried value bounds (`Plan.commands`): a
  prompt chunk is a command per attention layer, the longest one layer, 0.62
  s at 32768 and 2.4 s at 131072. Each command still grows with the context;
  a window of keys per command (attention with a log-sum-exp combine) would
  bound it. At 131072 a decode step takes 0.674 s; the whole 131k prompt's
  time to first token is unmeasured.
- Tuning times each operator alone, not inside the fused image it runs
  in. Kernel cycles skip only GEMM settings, since only GEMM's calls per
  core are known here, and only on npu2, the one NPU whose core clock was
  measured. A GEMM with a column-major B (`b_col_maj`) is never skipped:
  the nightly times no such tile.
- Open upstream asks in mlir-aie: an accessor for L1 banking. aiecc's split memory (a whole-module clone per split item) is
  mlir-aie #3689's, which shares one clone per split.

## Common Patterns

### Multi-Column Parallelism

Distribute work across NPU columns using TensorAccessPattern:

```python
num_columns = 4
parts = TensorAccessPattern.full((total_elements,)).partition(num_columns)
taps = [parts[i] for i in range(num_columns)]  # column i's contiguous chunk
```

### ObjectFIFO Acquire/Release Pattern

```python
def core_body(of_in, of_out, kernel_fn):
    for _ in range_(num_iterations):
        elem_in = of_in.acquire(1)
        elem_out = of_out.acquire(1)
        kernel_fn(elem_in, elem_out, size)
        of_in.release(1)
        of_out.release(1)
```

### Using `range_()` vs `range`

- **Always use `range_()`** in Worker functions (NPU-side code)
- Use Python `range` only in Runtime sequences (host-side code)

### Vectorized Kernel Template

```cpp
#include <aie_api/aie.hpp>

void my_kernel(bfloat16* in, bfloat16* out, int32_t size) {
    event0();  // Start performance counter
    aie::vector<bfloat16, 32> vec_in = aie::load_v<32>(in);
    // ... vectorized operations ...
    aie::store_v(out, vec_out);
    event1();  // Stop performance counter
}
```

**Note**: `event0()` and `event1()` are performance profiling markers.

### Test Verification Pattern

```python
from aie.utils.verify import Tolerance
from iron.common.testing import run_test, vectors
from iron.operators import Tanh

op = Tanh(size=2048, num_aie_columns=1, num_channels=1, tile_size=2048)

# Dispatch, and compare every output with op.reference() on the drawn inputs
# under the tolerance contract of the kernel the operator runs; in a test,
# record=record_property puts its latency and bandwidth in the CSV ...
errors = run_test(op, vectors(op), tolerance=op.resolved().tolerance())
assert not errors, errors

# ... or under an explicit one.
errors = run_test(op, vectors(op), tolerance=Tolerance.relative(0.04, 1e-6))
```

`op.judge()` holds a step's buffers to its reference the same way, for
tests that dispatch by hand, and mlir-aie's `aie.utils.verify.compare` a
single buffer.

A test that dispatches is marked `@pytest.mark.supported_devices("npu1",
"npu2")`, and nothing else: the mark skips it where no listed NPU is, and
conftest.py releases the runtime after it.

### bfloat16 and runtime tensors

IRON is numpy only; nothing in it needs torch. numpy has no bfloat16 of its
own, so use `ml_dtypes.bfloat16`. A reference upcasts to float32, computes,
and rounds to bfloat16 once per tensor it names:

```python
import numpy as np
from ml_dtypes import bfloat16

x = (rng.standard_normal((M, K)) * 4).astype(bfloat16)
y = (x.astype(np.float32) @ w.astype(np.float32)).astype(bfloat16)
```

Runtime tensors (`aie.utils.DEFAULT_TENSOR_CLASS`) are built from a numpy
array, written through `numpy_view()` (no device sync; the buffer is
marked for upload) and read with `numpy()` (synced from the device first).
An operator called outside a graph takes one per declared buffer, in
declaration order:

```python
tensor = aie_utils.DEFAULT_TENSOR_CLASS
x_t, out_t = tensor(x.reshape(-1)), tensor(np.zeros(size, dtype=bfloat16))
op(x_t, out_t)          # compiles once, then runs
out = out_t.numpy()
```

## Debugging and Performance

### Building against a local kernel tree

```bash
MLIR_AIE_KERNEL_SOURCES=/path/to/mlir-aie pytest ...
```

The path reaches the compile key, so pointing IRON at another tree rebuilds
rather than reusing the cache.

### Performance Profiling

C++ kernels use `event0()` and `event1()` markers for performance profiling. These can be analyzed with AIE trace tools to measure cycle counts.

### Logging

The codebase uses Python's standard `logging` module. Enable debug logging:

```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## CI and PR Workflow

### GitHub Actions Workflows

- **phoenix-small.yml**, **krackan-small.yml**: Operator and library tests, `iron/operators/` and `iron/tests/` (non-extensive, runs on every PR), on NPU1 and NPU2
- **phoenix-extensive.yml**, **krackan-extensive.yml**: Full test suite (the same, with extensive tests), nightly and on pushes to `main` and `devel`
- **phoenix-test-examples.yml**, **krackan-examples.yml**: Application tests, `tests/applications/`
- **ci-lint.yml**: Linting checks (black, clang-format, reuse)
- **pr-comment.yml**: Posts the performance trends of a PR as a comment
- **publish-pages.yml**: Rebuilds the benchmark history site on GitHub Pages

### Benchmark Results

Each CI run writes `tests_latest.csv` (`--csv-output`; a run without it
writes no CSV), which `.github/actions/commit_results`
merges into `{arch}/{suite}/all.csv` on the `ci` branch. The scripts under
`ci/scripts/` consume those CSVs:

- `merge_all.py`: appends a run and drops results older than a year
- `pretty_trends.py`: the performance changes of one run, as markdown
- `pr_comment.py`: assembles those reports into the PR comment
- `build_pages.py`: the per-operator charts published to GitHub Pages

The trend report and the charts cover only parametrizations marked
`@pytest.mark.bench`: a catalog case declared with `bench=True`, or a test
of its own that carries the mark.

### Workflow Requirements

- **Target Branch**: Always submit PRs to `devel`
- **CI Tests**: Run on self-hosted runners with NPU hardware
- **All CI must pass**: Including linting and formatting checks
- **Pre-Push Hook** (optional but recommended):

  ```bash
  cp scripts/hooks/pre-push .git/hooks/pre-push
  chmod +x .git/hooks/pre-push
  ```

- **PR Prefixes**: Use "DRAFT:" for work-in-progress, "REFACTOR:" for refactoring

## Troubleshooting

### Common Issues

**Compilation hangs or fails**

- Check MLIR-AIE is installed: `python -c "import aie.iron"`
- Look for errors in the operator's `Array.build()` (common: using `range` instead of `range_()`)

**Test failures with numerical differences**

- Check datatype consistency (bfloat16 has limited precision)
- Verify reference implementation matches NPU kernel exactly
- Look for memory alignment issues in C++ kernel
- Check which tolerance the test judges by: the kernel's contract
  (`op.resolved().tolerance()`) unless the test passes `tolerance=`

**Dimension mismatch errors**

- Check operator constraints (e.g., `M % (tile_m * 4) == 0` for GEMM)
- Verify `tile_size`, `num_aie_columns`, and total size are compatible
- Ensure tensor dimensions are multiples of required alignment

**Kernel compilation failures**

- Check the kernel's `.cc` includes the right `*_aie2.h` / `*_aie2p.h` header for the target
- Verify `#include <aie_api/aie.hpp>` for AIE API kernels
- Ensure template parameters match function signature
- Check for syntax errors in vectorization code

## Language models (`iron/lm/`)

### The shared library

`iron/lm/` is what every language model shares; each model is an
application over it, a package under `iron/applications/`. How to add one
is "Add a model" in [CONTRIBUTING.md](CONTRIBUTING.md). Nothing in the
library imports a model. The modules:

- `base.py`: `Config` and `DecoderConfig`, a model's shape read from the
  checkpoint's `config.json` (a field with no `metadata={"json": ...}` is
  IRON's choice and keeps its default), whose `attention(i)` and
  `layer(i)` give layer `i`'s parts; `rope_angles`; `Checkpoint`, the
  mapped `.safetensors` (sharded, or a PyTorch checkpoint read without
  torch), whose `tree(fill=)` is the weights by the checkpoint's own names
  (`weights.model.layers[3].self_attn.q_proj.weight`): `"read"`, views of
  the file; `"random"`, drawn at a seed; `"unread"`, allocated and never
  written, for tracing and building; `Derived`, weights a model computes
  from that tree; `Model`, a graph whose versions `load()` compiles before
  the first call, with `sanitize(w)`, which renames one layer's modules to
  the names the parts read; `OnHost`, a model mixin that runs the graph's
  own reference (`Graph.reference`) in place of the device; and `Runner`
  and `main`, a checkpoint, tokenizer and model and the command line.
  `Runner.reference()` is what a model is judged by: transformers' logits
  recorded beside the checkpoint, or with `--random-weights SEED` the
  graph's own reference over the drawn weights
- `blocks.py`: the parts a layer is composed from, each a frozen
  dataclass called inside a graph's body: `Norm` (RMS, or affine LayerNorm
  with `bias=True`), `Attention` (heads, groups, q/k/v norms, scale,
  window, partial rotary), `MLP` (gated or plain, SiLU or GELU-tanh),
  `DecoderLayer` (pre-norm attention and MLP with residuals, a residual
  scale where one is set) and `CrossDecoderLayer` (adds attention over an
  encoder's output). Also the front-end graphs `LogMel`, `Conv1d`,
  `Conv2d`, `MaxPool2d`, `ConcatChannels` and `ImagePatches`
- `golden.py`: `Golden`, transformers' logits stored by token hash in an
  `.npz` and computed on a miss only while recording
  (`--record-goldens`), and `HuggingFace`, transformers' model built over
  IRON's config and weights (`build`) or a checkpoint (`load`)
- `causal.py`: `CausalLM`, a decoder as one graph, a prompt chunk and a
  decode step (`DecodeStep`), the key and value caches (`keys`, `values`,
  by layer index), and `logits(tokens)`. A subclass gives `head(x)`;
  `embed()` and `positions()` (identity by default) scale the embedded
  rows and add an absolute position table. `decoder=` names a decoder
  nested in the checkpoint. `Checkpoints` is state carried position to
  position (LFM2's short convolutions), a slot per prompt-chunk boundary,
  held in `recurrent` (`iron/tests/lm/checkpoints.py`)
- `encoder.py`: `Encoder`, bidirectional, compiled once at `max_tokens`
  rows with the length bound per call; `Tower`, an encoder whose rows come
  from a front end (`front`) and whose output is soft tokens in a text
  model's space
- `encoder_decoder.py`: `EncoderDecoder`, a `CausalLM` whose layers also
  attend over an encoder's output; `encode()` runs the encoder and writes
  each layer's cross keys and values once
- `multimodal.py`: `Multimodal(text, towers)`, a text model and its towers
  keyed by placeholder token as one graph, the soft tokens merged in at
  the placeholders

`generation.py` (sampling, the generation loop, the accuracy and
determinism checks) and `testing.py` (a device test's checks, the files
under `$IRON_EXAMPLE_WEIGHTS_DIR/<name>`) need only `logits(tokens)`. Their
dependencies are in `requirements_examples.txt`; transformers and torch
are needed only to record goldens.

### Llama 3.2 1B Inference

Full LLM inference example at `iron/applications/llama/`: `model.py`
(Llama 3's head, Llama 3.2 1B's shape,
the tokenizer), `profiles/` (tunables), its test and README:

- **Required files**: `config.json`, `model.safetensors`, `tokenizer.model` from Hugging Face
- **Default location**: `/srv/llama3.2-1b/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Additional deps**: `pip install -r requirements_examples.txt`
- **Run**: `pytest tests/applications/llama/`, or
  `python -m iron.applications.llama.model model.safetensors tokenizer.model`
  (`--max-seq-len` sets the longest context served, up to the checkpoint's
  `max_position_embeddings`, by default that where the model fits the host:
  131072 for Llama 3.2 1B, 4 GiB of caches; one compile serves every
  context up to it). XRT maps
  every device buffer locked and `ulimit -l` binds each mapping; the
  weights and the caches are banks of at most 3.76 GB, a buffer object
  each (`allocator.BANK`), so the limit must cover one bank

### EmbeddingGemma 2

Its text encoder, audio and vision towers at
`iron/applications/embedding_gemma2/`, one package and one test, an
`Encoder` rather than a `CausalLM`: one graph compiled once at `max_tokens`
rows (2048 by default), the prompt's length bound per call, each tower a
`Tower` and the multimodal model an `iron.lm.Multimodal`:

- **Required files**: `model.safetensors`, `tokenizer.json`
- **Default location**: `/srv/embeddinggemma-2/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Run**: `pytest tests/applications/embedding_gemma2/`, or
  `python -m iron.applications.embedding_gemma2.model <dir> --query ... --document ...`

A model's device test goes in `tests/applications/<name>/test.py`, and
imports its application as `iron.applications.<name>`: CI's example suite
runs `tests/applications/`, and the benchmark history names a row by that
directory.

### AIE Kernel Reference

See the [mlir-aie kernel library README](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/README.md) for the catalog of available kernels:

- Element-wise ops (add, mul, scale)
- Matrix operations (mm, mv)
- Reductions (add, max, min)
- ML ops (conv2d, relu, exp)
- Vision ops (rgba2gray, filter2d)

Kernels are organized by coding style:

- **AIE API**: Portable C++ template library (recommended)
- **Intrinsics**: Architecture-specific low-level intrinsics (max performance)
- **Generic C**: Works on any AIE family (basic functionality)
