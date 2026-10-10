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

**Note:** `requirements.txt` pins an mlir-aie nightly wheel, which brings the
kernel library (`aie_kernels/`) and finds the Peano wheel by itself.

**Note:** XRT must be sourced before running any tests or operators.

### Where build outputs go

Compiled artifacts (`.xclbin`, `.bin`, `.o`, the full ELF) live in
mlir-aie's JIT cache, keyed on the content that produced them:
`~/.npu/cache/<hash>/`, or wherever `NPU_CACHE_HOME` points. Nothing is
written to the working directory, and `compile(record="disk")` (on a graph
or an `OperatorImage`) writes the `Artifacts` record of an image beside it
in the cache.

### Environment Variables

- `IRON_EXAMPLE_WEIGHTS_DIR`: Path to language model weights (default: `/srv`)

## Building and Testing

### Run All Operators (non-extensive tests)

```bash
pytest iron/operators/ iron/tests/ -m "not extensive" --iterations 1
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
pytest iron/applications/
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
# Check C++ formatting
python scripts/clang-format-wrapper.py --check

# Show differences
python scripts/clang-format-wrapper.py --diff

# Auto-format all
python scripts/clang-format-wrapper.py --fix

# Format specific directory
python scripts/clang-format-wrapper.py --fix --path iron/
```

### License Compliance (REUSE)

```bash
# Check all files have proper license headers
reuse lint
```

## Architecture

### Three-Layer Structure

1. **Operators** (`iron/operators/`)
   - One operator is one module: `relu.py` for a small one, a directory with
     `op.py` for one that also has a design, a reference, a README or a
     device test of its own (`swiglu_prefill_stream/`). `flm/` is a catalog of its
     own: the FastFlowLM ports (`flm.GEMM`, `flm.DequantBFP`), the binary they
     are measured against and their weight packing; its GEMM is not
     `iron.operators.GEMM`.
   - An operator module holds:
     - the operator, one class (`iron/common/declare/`): `param()` fields for what a host shape
       names, `auto()` tunables `resolve(dev)` fills from the device and the
       extents (a tunable is an `auto()` field: the caller or a profile may
       give it, and the library resolves it when neither does), `In`/`Out` operands declared by shape whose `tile=` makes
       each its own stream into the array (`per=` a column count), `Value`
       members the cores read (trip counts, derived from the extents so the
       array never depends on them), `array(target)`, which builds
       ObjectFIFOs and Workers and binds each operand's lane to a fifo's
       shim end, and optionally `sequence(rt)` when the runtime sequence is
       not the derived one. The array tier is what a tile names plus what
       says `array=True`; one array serves every extent. A shipped binary
       is a subclass declared with `image=Xclbin(...)`, its operands pinned
       with `via=`. Two hooks change what is built: `configuration()`, the
       operator whose xclbin this one runs (itself by default; flm's GEMM
       returns its shape-free half, so one xclbin serves every shape), and
       `exported_design(image)`, a callable returning the module (an
       `ir.Module` or its text) for a design another tool exports
       (stream-dse's SwiGLU groups) in place of the derived one.
     - The operator's `reference(*inputs)` is the CPU reference the tests
       and the graph reference run; `vectors(op)` in `iron/common/harness`
       draws random inputs for its declared buffers and takes the outputs
       from it. An `Elementwise` operator has none of its own: its kernel's
       contract is the reference. A composite builds its reference from its
       kernels' contract references where it can, and says why where not.
     - `test = Testing(cases, ...)` on the operator class
       (`iron/common/testing.py`): the shapes it is checked at on a device,
       any `draw=` its inputs need, and a `tolerance=` where the contract
       of the kernel it runs is not the gate. One module,
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
   - `declare/`: the declaration layer (`Operator`, `param`/`auto`,
     operands, `Value`, `Scratchpad`/`DispatchTime`, `Xclbin` and its
     `fetch()`, inference). An operator's shim budget, `shim_columns`, is
     the bound device's `shim_dma_channels_in`/`out`; its `residents` the
     derived values the preamble writes once per build
   - `design/`: the library-owned build: the `Target` an
     array is built against (its device and image),
     `build_design(op, image)` (the module for one operator),
     `OperatorDesign` (that module as mlir-aie's `CompilableDesign`
     compiles and caches it), the derived runtime sequence (`Sequence`,
     its `split`/`round_robin`), `ExternalSequence` (the sequence
     against a shipped image: `Lock.set` releases its parameter block)
   - `graph/`: graphs (`iron.Graph`, `iron.state`) and
     `compile(dev=, boundaries=, image=)`
   - `image/`: what a graph lowers onto: `OperatorSequence`, the buffer
     allocator (`LiveRange`, `Pool`, `ArenaPlan`), `Fusion` (the designs of
     a sequence as one module), `FusedImage`/`XclbinChain` (the full ELF
     or the chain of xclbins it links), `OperatorImage` (one operator built
     and called on its own, outside a graph: `OperatorImage(op).compile()`,
     then `image(*tensors)`, `image.artifacts`), the runtime callables and
     the record of what a compiled image consists of
   - `elementwise.py`: the shared elementwise array and its operand shapes (flat, binary, rowwise)
   - `harness.py`: the device test harness (`vectors`; `run_test`, timed with
     `aie.utils.benchmark.run_iters`, every buffer paired by name; and
     `verify_buffer`, mlir-aie's `aie.utils.verify.compare` on one buffer
     of the reference's size); a test's figures go to
     pytest's `record_property`, which the root conftest writes to the CSV.
     The reference and the judgement are the operator's own:
     `op.call_reference(inputs, outputs, values)` runs `reference()` on
     buffers by name, `op.judge(inputs, written, tolerance)` returns a
     `Verdict` per written buffer
   - `testing.py`: how an operator declares the shapes it is tested at
     (`Testing`, `Case`, and `Sweep`, the elementwise sweep)
   - `tracing.py`: `dump_traces(run, trace_file)`, for a sequence holding an
     operator built with `trace=` (mlir-aie's `TraceConfig`); the workers
     traced are those its `array()` gives `Worker(trace=)`, else its first.
     The root conftest's `trace` fixture is the one reader of
     `IRON_TRACE_SIZE`/`IRON_TRACE_DIR`

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

**Runtime Sequence**: Host-side control flow. The library derives it from
the operator's declaration (each buffer split over its stream's slots); an
operator that needs a different order overrides `sequence(rt)`:

- `rt.fill(slot, view, group=tg)`: DMA data from host → NPU (shim → L2/L1)
- `rt.drain(slot, view, group=tg)`: DMA data from NPU → host
- `tg = TaskGroup()` ... `tg.finish()` (mlir-aie's): awaits and frees a
  group's transfers; `TaskGroup.pipelined(n)` keeps a step's in flight
  while the next is issued
- views are slices of the declared buffers (`self.A[:, r0:r1, :]`) or
  mlir-aie's `TensorAccessPattern`s over one (`(self.A, tap)`); the
  compiler splits a constant pattern no one descriptor holds

**Per-call values**: `Scratchpad(T)` members are patched into descriptors
or read by cores without a rebuild; `DispatchTime(T)` regenerates the
sequence per call (xclbin only). A graph binds them to keyword-only
parameters. The parameter scratchpad exists on a full ELF only (XRT's
`get_ctrl_scratchpad_bo` serves a module run), so on an xclbin image a
`Scratchpad` value lowers to a dispatch-time scalar: an offset use
regenerates the stream, a core-read use is an `rtp_write` of the scalar.

**Compilation Flow**:

```text
op.py (X.array + X.sequence or the derived sequence)
    ↓
iron.common.design.build_design (library-owned Runtime/Program)
    ↓
MLIR (.mlir file)
    ↓ (aie-opt + aie-translate via Peano toolchain)
xclbin (NPU binary) + insts.bin (instruction sequence)
```

**No build context.** An operator takes the device that is current and
nothing else. Everything else is a fixed path (`aie.utils.config.aie_kernels_dir()`), an
environment choice (`MLIR_AIE_KERNEL_SOURCES`), or a keyword on the build
itself (`compile(record="disk")`). On a host without an NPU, bind one to
resolve and compile against: `aie_utils.set_current_device(from_name("npu2",
n_cols=8))` (`aie.iron.device.from_name`); the test tree's `npu2` fixture
does that and restores the previous device. Kernels are built with Peano; IRON has
no xchesscc path, and a kernel that needs one asks the `aie.iron.kernels`
factory for it (`use_chess=True`) rather than IRON carrying a global flag.

**Runtime**: `aie.utils.DefaultNPURuntime` loads an image and runs it,
shared across operators. A test that ran on hardware takes the
`npu_runtime` fixture, which releases it afterwards.

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
- Minimum tile sizes depend on `emulate_bf16_mmul_with_bfp16` flag:
  - `True` (default): 8×8×8 minimum
  - `False`: 4×8×8 minimum
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
   - `param()` fields for what a host shape names; `auto()` tunables, filled
     by `resolve(dev)` from the device and the extents
   - `In`/`Out` operands by shape, each with its `tile=` in the units a
     core reads (`per=` a column count): an operand with a tile is its own
     stream, `op.x.lane(i)` a shim endpoint, `op.x.tile` the fifo type;
     `when=flag`, a bool `param()`, makes an operand (and its stream) exist
     only where the flag is true; a call gives it by keyword, its name,
     which sets the flag (`RMSNorm(x, weight=w)` is `weighted=True`)
   - a `Value(derive=...)` for every trip count the core reads, so the
     array never depends on the extent; what else the array bakes is
     `param(..., array=True)`
   - `array(target)`: build ObjectFIFOs and Workers (`self.kernel()` or a
     factory's `ExternalFunction`, `Buffer(..., use_write_rtp=True)` for a
     runtime parameter, `WorkerRuntimeBarrier()`), `range_()` for loops, and
     `self.x.lane(i).bind(fifo.prod())` / `self.count.bind(rtps)` for every
     member. It returns what it built: its Workers, its barriers and any
     `Flow`, `Lock` or `TileDma` only the sequence reaches. It sees the
     array tier alone: reading an extent raises
   - `compatible()` for divisibility against the resolved tunables
   - `sequence(rt)` only if the derived sequence is not the one you want:
     `rt.fill(self.A.lane(i), access)`, `rt.drain(self.C.lane(i), access)`
   - see `iron/common/elementwise.py` for the elementwise families, and
     `gemm.py` or `mha.py` for hand-written sequences
3. A shipped binary is a subclass declared with the image, `class
   Shipped(X, image=Xclbin(url=, sha256=, filename=))`: it pins the tunables,
   redeclares the operands with `via=` and lays the image's parameter block
   out as a `Value(address=, lock=)`; nothing builds its array
4. Name the kernel with a factory from `aie.iron.kernels`
   (`eltwise.relu_sized(line)`, `norm.rms_norm_eps(tile)`, ...): it carries
   the symbol, the source, the argument types, aie2's LUT tables and the
   contract: the reference, the tolerance and the scalar bindings. The
   factory binds the line length and any scalar the operator gives it
   (`activation.leaky_relu(tile, alpha=)`, `datamovement.axpy(tile, a=)`,
   `norm.rms_norm_eps(tile, epsilon=)`), so a core calls the kernel with
   its elements alone and the operator declares no `kernel_call` or
   `reference` of its own; a field it passes is `param(..., array=True)`.
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
   `contract=KernelContract(roles=, parameter_bindings=, reference=)` and
   it is used like a factory's. An operator running one kernel
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
   `run_test(..., record=record_property)` records throughput from it
6. Declare how it is tested: `test = Testing(cases, tolerance=)` on the
   operator class, from `iron.common.testing`
   - leave `tolerance` out to be judged by the contract of the kernel the
     operator runs (`Operator.tolerance()`); give an
     `aie.utils.verify.Tolerance` where that is not the right gate
   - the cases are `Case(kwargs, extensive=...)`, plain kwarg dicts, and
     callables of the class returning them when they follow the device's
     width: `Sweep(...)` is the elementwise one (every column and channel
     count the shim budget allows at each length; `channels=None` for a
     binary operator, `rows=True` for a rowwise one, further keywords given
     to every case)
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
   - `draw=` passes `vectors()` its arguments (`normal=`, `centered=`, a given
     tensor or shape per input), or a callable of the operator for an input
     with preconditions (a packed quantization, an angle table)
   - `iron/tests/operators/catalog.py` runs it; a test with a body of its own goes
     beside the operator and calls `run_test(op, vectors(op), ...,
     record=record_property)`, and gives pytest's `record_property` any
     figure beyond latency, bandwidth and throughput
   - a shape the operator must *refuse* goes in
     `iron/tests/operators/rejected_shapes.py`, which needs no device
7. Register operator in `iron/operators/__init__.py` (`_OPERATOR_MODULES`:
   the name, and the module that defines it)

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
from iron.common import Scratchpad

class Decode(iron.Graph):
    def __init__(self, weights, angles):
        self.weights = weights                   # a namespace of arrays: weights
        self.rope = iron.weight(angles)          # (max_len, head_dim)
        self.kv = iron.state((n_kv_groups, max_len, head_dim))

    def body(self, x, *, pos: Scratchpad[np.int32]):
        w = self.weights
        h = RMSNorm(x, weight=w.norm)            # class calls infer the extents
        k = RoPE(GEMV(w.wk, h), Copy(self.rope[pos]).reshape(1, head_dim))  # gathered on the NPU
        Copy(k, self.kv[:, pos])                 # a state passed as an output is written
        return GEMV(w.wo, h)

graph = Decode(weights, angles)
graph.compile(x=(1, emb))                        # or on the first call
logits = graph(x_tok, pos=n)
```

The versions of one graph share its weights and states: a full ELF
version is placed in the graph's one scratch arena. `graph.reference(...)` runs the body through each operator's
`reference()` on host tensors, per-call values and state modelled.

The tunables a graph's operators run with can be a `Profile` rather than
keywords at every call: entries keyed by operator class and shape, the
graph's `profile` attribute (or applied in a `with profile:` scope); a
directory there holds one per device, `<device>.json`. A call
that leaves a tunable open takes the most specific entry's value; a call that
gives one keeps it. An entry matches on the fields the operator is
constructed with, the call's keywords and the extents inferred from its
operands: key MHA by `seq_pad`, which its shape gives, not `seq_len`, which
follows from it later. A profile is a JSON file, `Profile.load(path)` and
`profile.save(path)`, one entry to a line naming the class in
`iron.operators`, then its dimensions and tunables:

```json
{"entries": [
  {"operator": "GEMV", "M": 2048, "K": 8192, "tile_size_input": 1},
  {"operator": "MHA", "num_heads": 32, "seq_pad": 2048, "num_pipelines": 8},
  {"operator": "MHA", "num_heads": 32, "seq_pad": 1, "num_pipelines": 4}
]}
```

`iron/lm/llama3/profiles/<device>.json` is the worked
example (a test at the small shape loads
`iron/tests/common/llama_small_profile.json`), and
`test_llama_names_only_the_tunables_that_matter` checks that each keyword the
graph still passes is one the profile could not have given.

Operators with equal `array_key()` share one array; with equal
`design_key()` they are one build. `compile(dev=, boundaries=,
image=, **shapes)` derives the image (a fused ELF on NPU2, per-step
xclbins with `boundaries=iron.each_step`) and `verbose=True` prints why.
It links the image (`version.image`) and stops
there: the runtime that loads it is made on the first call, so a host with
the toolchain and no NPU can compile ahead of time.
`iron/lm/llama3/model.py` is the worked example
(`Llama`, a `CausalLM` from `iron.lm`, called through
`logits(tokens)`, and `LlamaOracle`, its float32 forward pass on the host;
its `Runner` builds both and checks one against the other);
`iron/tests/common/graph.py` traces it device-free,
`iron/tests/common/llama_reference.py` runs its reference against the CPU
one and `iron/tests/toolchain/` builds it.

## Design rationale and known limits

Why the pieces are shaped as they are, and what is not built. Check the
code before relying on a line here; it is the authority.

### Rationale

- **One class per operator, tiers by declaration.** The array tier is
  what a `tile=`/`per=` names plus what says `array=True`; `array()` sees
  that tier alone, so an extent cannot leak into a core program. Trip
  counts are `Value`s the sequence writes, so one array serves every
  extent and one build serves many shapes.
  `iron/tests/toolchain/array_identity.py` compiles operators at two
  extents and compares the core ELFs byte for byte.
- **Tunable precedence.** A call site's value, then the graph's profile, then
  `resolve(dev)`, then the `auto()` default. Identity (`array_key`,
  `design_key`) is taken after resolution, so two calls that resolve alike
  share a build.
- **Packaging is derived** (`iron/common/image/packaging.py`, reported with
  `verbose=True`): a `DispatchTime` value, NPU1, or more than one boundary
  each force xclbin; otherwise the image is one full ELF. Full-ELF streams
  have DDR address folding off, so a sequence cannot move between images.
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
  sizes the caches and the RoPE table alone. A prompt runs chunk by chunk
  against the caches, and decode is MHA of one query (a KV group's heads
  packed into a block, a pipeline's own K and V lanes), or where MHA does
  not fit `GQAScores`, `Softmax` and `GQAContext` over the same caches. The caches are
  `(max_seq_len, n_kv_groups, head_dim)`, so a call's write is contiguous
  and no descriptor steps by the context: a `(groups, positions)` cache
  would step `max_seq_len * head_dim` between groups, past a descriptor's
  2^20-granule stride from 32768 rows on.
  `test_llama_does_not_grow_with_the_context` checks that no activation
  or array follows `max_seq_len`.
- **DMA descriptors** (mlir-aie's `verifyStridesWraps`, restated over a
  pattern by `BdLimits.fits`, `BdLimits.of(dev, col, row)`): the innermost
  dimension holds at most 1023 granules unless the transfer is linear, the
  next at most 1023 elements, the third has no wrap field, and the
  outermost is the iteration count (at most 64) and the only one whose
  stride may be 0. A pattern past them is split by the compiler
  (`aie-decompose-large-dma-bd`), a per-call offset patched into every
  piece; one whose size a call bounds must fit one descriptor, since the
  patch lands in its length.
- **Placement.** Operator order is the final tiebreak for shim tile and
  channel, so a per-column stream is not guaranteed to sit in physical
  column `c`; pin it with `via=` where that matters. Where the tiles an
  `array()` names are a choice, the choice is a tunable:
  `placement: str = auto("...", array=True, domain=Placement({...}))`, each
  name a `Pins` holding cores, memtiles and shims at a `Level` (the tile,
  its column, or the placer's), the hand-found one the default
  (`iron/common/declare/placement.py`; MHA and GEMM). The tuner measures
  each name the placer takes, like any other tunable.
- **`Elementwise` is not upstream's `transform_parallel`.** They differ in
  the trip count (a `Value` here, folded into the core there), in who
  owns the sequence (the library here, so operators fuse into one image),
  and in the column budget. Splitting upstream's
  `_transform_parallel_gen` would let IRON reuse it.

### Not built, or limited

- A fused sequence in an xclbin (several steps in one dispatch) is refused;
  so are modules. NPU1 therefore needs `boundaries=iron.each_step`.
- A prompt chunk is one dispatch, and its attention grows with the
  context (about 1.2 s plus 0.12 s per 2048 rows before it; MHA streams
  every K and V block for each Q block, valid or not). amdxdna's watchdog
  (`tdr_timeout_ms`, 2000 by default; a stall is two ticks with no job
  run or completed) stops a dispatch between 4 and 6 s, so past about
  48k tokens a prompt needs `tdr_timeout_ms` raised (`options amdxdna
  tdr_timeout_ms=10000` in `/etc/modprobe.d/`, read at module load). At
  10000 a 131008-token prompt runs, in 315 s, and decodes at 5.0 tok/s
  (198 ms a step).
- Tuning: there is no search over a tunable's legal values, and no
  per-kernel L1 budget.
- Open upstream asks in mlir-aie: a builder for `aiex.configure` /
  `aiex.run`; an accessor for L1 banking. aiecc's split memory (a whole-module clone per split item) is
  mlir-aie #3689's, which shares one clone per split.

## Common Patterns

### Multi-Column Parallelism

Distribute work across NPU columns using TensorAccessPattern:

```python
num_columns = 4
chunk = total_elements // num_columns

taps = [
    TensorAccessPattern(
        (1, total_elements),
        chunk * i,  # offset for column i
        [1, 1, 1, chunk], # sizes
        [0, 0, 0, 1], # strides
    )
    for i in range(num_columns)
]
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
from iron.common.harness import run_test, vectors
from iron.operators import Tanh

op = Tanh(size=2048, num_aie_columns=1, num_channels=1, tile_size=2048)

# Dispatch, and compare every output with op.reference() on the drawn inputs
# under the tolerance contract of the kernel the operator runs; in a test,
# record=record_property puts its latency and bandwidth in the CSV ...
run = run_test(op, vectors(op), tolerance=op.resolved().tolerance())
assert not run.errors, run.errors

# ... or under an explicit one.
run = run_test(op, vectors(op), tolerance=Tolerance.relative(0.04, 1e-6))
```

`op.judge()` holds a step's buffers to its reference the same way, for
tests that dispatch by hand, and `verify_buffer()` a single buffer.

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
marked for upload) and read with `numpy()` (synced from the device first):

```python
run.get_buffer("x").numpy_view()[:] = x.reshape(-1)
run()
out = run.get_buffer("out").numpy()
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

- **small.yml**: Operator and library tests, `iron/operators/` and `iron/tests/` (non-extensive, runs on every PR)
- **extensive.yml**: Full test suite (the same, with extensive tests)
- **test-examples.yml**: Application tests (Llama inference, EmbeddingGemma 2, Gemma 4 on FastFlowLM)
- **ci-lint.yml**: Linting checks (black, clang-format, reuse)
- **pr-comment.yml**: Posts the performance trends of a PR as a comment
- **publish-pages.yml**: Rebuilds the benchmark history site on GitHub Pages

### Benchmark Results

Each run writes `tests_latest.csv`, which `.github/actions/commit_results`
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

**"No XRT device found"**

- Ensure `source /opt/xilinx/xrt/setup.sh` was run
- Check XDNA driver is installed: `lsmod | grep amdxdna`

**"Kernel not found" or "Symbol not defined"**

- Verify the kernel `.cc` exists under the installed mlir-aie package's
  `include/aie_kernels/<family>/` (`aie.utils.config.aie_kernels_dir()`,
  overridden by `MLIR_AIE_KERNEL_SOURCES`)
- Ensure the kernel's C++ signature matches the factory from
  `aie.iron.kernels` (or `bind()`'s argument types), or the
  `ExternalFunction` declaration, that the operator's `array()` names

**Compilation hangs or fails**

- Check MLIR-AIE is installed: `python -c "import aie.iron"`
- Verify `llvm-aie` is available: `which aie-opt`
- Look for errors in the operator's `array()` (common: using `range` instead of `range_()`)

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

**"Invalid configuration: NPU2 has 8 columns"**

- NPU1 supports 1-4 columns only
- NPU2 supports up to 8 columns
- Device type is auto-detected via XRT

**Kernel compilation failures**

- Check the kernel's `.cc` includes the right `*_aie2.h` / `*_aie2p.h` header for the target
- Verify `#include <aie_api/aie.hpp>` for AIE API kernels
- Ensure template parameters match function signature
- Check for syntax errors in vectorization code

## Language models (`iron/lm/`)

### The shared decoder

`iron/lm/` is what every language model shares, and each model is a
package under it (`iron/lm/llama3/`). A model is five things over the
shared layer, plus its tokenizer and profiles:

- `Config` (`decoder.py`): the shape
- `CausalLM` (`decoder.py`): a decoder as one graph, a prompt chunk and a
  decode step, the key and value caches, attention over them (`attend`) and
  `logits(tokens)`. A model subclasses it with `layer(step, i, weights,
  x)` and `head(x)`, built from `layers.py`: `project(x, w)`, a weight's
  projection at either row count (GEMV for one row, GEMM for more), and
  `swiglu`, the SwiGLU feed-forward (`SwiGLU` is it as a graph of its own,
  device-tested by `iron/operators/swiglu/test.py`). `rope_angles`
  (`decoder.py`) is the RoPE table a `Config` names the base and scaling of
- `Oracle` (`decoder.py`): the same decoder's float32 forward pass on the
  host, the reference the model is judged by, as an operator's is its
  `reference()` (not composed from the operators' references, so it catches
  a wiring mistake the graph's own reference repeats). A model subclasses it
  with a numpy `layer(angles, weights, x)` and `head(x)` and names it as
  its `CausalLM`'s `oracle`; the pass, RoPE and attention are shared. Its
  float32 weights are twice the checkpoint, so it is built to check with
- a checkpoint `Layout` (`checkpoint.py`): each weight's place in the
  model, its name in the checkpoint and its shape, which `load_weights`
  checks strictly against the mapped `.safetensors`
- `Runner` and `main` (`runner.py`): the checkpoint, the tokenizer, the
  model and its oracle, and the command line. A model's runner names
  its `config`, `layout`, `model`, `open_tokenizer` and `bos`. With
  `--random-weights SEED` (and pytest's option of that name) the weights
  are drawn (`random_weights`) and the prompts random: speed, accuracy
  against the oracle and determinism on a host without the files

Nothing of a model's own is needed by `generation.py` (sampling, the
generation loop and the accuracy and determinism checks over any model
with `logits(tokens)`) or `testing.py` (what a model's device test checks
with them, and where it finds the files,
`$IRON_EXAMPLE_WEIGHTS_DIR/<name>`; pytest's `--max-seq-len` runs a
model's test at another context). Nothing in the library imports a
model.

Their dependencies (safetensors, tiktoken, ...) are in
`requirements_examples.txt`.

### Llama 3.2 1B Inference

Full LLM inference example at `iron/applications/llama_3.2_1b/` (its test
and README), over the model package `iron/lm/llama3/`: `model.py` (Llama 3's
layer and head on the NPU and in numpy, Llama 3.2 1B's shape, the layout, the
tokenizer), `profiles/` (tunables):

- **Required files**: `model.safetensors`, `tokenizer.model` from Hugging Face
- **Default location**: `/srv/llama3.2-1b/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Additional deps**: `pip install -r requirements_examples.txt`
- **Run**: `pytest iron/applications/llama_3.2_1b/`, or
  `python -m iron.lm.llama3.model model.safetensors tokenizer.model`
  (`--max-seq-len`, a multiple of 2048, sizes the caches: 32768 by default,
  1 GB of them; one compile serves every context up to it). XRT locks
  every device buffer, so `ulimit -l` must cover the weights and the
  caches: about 3.7 GB at 32768, 7 GB at 131072

### EmbeddingGemma 2

Its text encoder at `iron/applications/embeddinggemma_2/` (its test and
README), over the model package `iron/lm/embeddinggemma2/`, which is not a
`CausalLM`: one graph compiled once at `max_tokens` rows (2048 by default),
the prompt's length bound per call, and `EmbeddingGemmaOracle`, its float32
encoder on the host:

- **Required files**: `model.safetensors`, `tokenizer.json`
- **Default location**: `/srv/embeddinggemma-2/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Run**: `pytest iron/applications/embeddinggemma_2/`, or
  `python -m iron.lm.embeddinggemma2.encoder <dir> --query ... --document ...`

A model's device test goes in `iron/applications/<name>/test.py`: CI's
example suite runs `iron/applications/`, and the benchmark history names a
row by that directory.

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
