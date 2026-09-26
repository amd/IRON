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

**Note:** XRT must be sourced before running any tests or operators.

### Where build outputs go

Compiled artifacts (`.xclbin`, `.bin`, `.o`, the full ELF) live in
mlir-aie's JIT cache, keyed on the content that produced them:
`~/.npu/cache/<hash>/`, or wherever `NPU_CACHE_HOME` points. Nothing is
written to the working directory, and `compile(record="disk")` writes the
`Artifacts` record of an image beside it in the cache.

### Environment Variables

- `IRON_EXAMPLE_WEIGHTS_DIR`: Path to model weights for applications (default: `/srv`)

## Building and Testing

### Run All Operators (non-extensive tests)

```bash
pytest iron/operators/ -m "not extensive" --iterations 1
```

### Run Extensive Test Suite

```bash
pytest iron/operators/
```

### Run Single Operator Test

```bash
pytest iron/operators/axpy/
```

### Run Application Tests

```bash
pytest iron/applications/
```

### Run Specific Test Function

```bash
pytest iron/operators/test.py -k relu
pytest iron/operators/gemm/test.py::test_gemm
```

### Parallel Testing (faster)

```bash
pytest iron/operators/ -n auto -m "not extensive"
```

## Code Style and Linting

### Python (Black)

```bash
# Check formatting
black --check .

# Auto-format
black .
```

### Python lint and types (ruff, pyright)

```bash
# Both are scoped by their config (ruff.toml, pyrightconfig.json) to the
# whole `iron` package, after mlir-aie's setup.
ruff check
pyright
```

A declared class is a dataclass to a checker, so a call that names a field it
does not declare, or passes the wrong type, is an error before anything runs.

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
     device test of its own (`gemm/`, `mha/`, `flm/gemm/`).
   - An operator module holds:
     - the operator, one class (`iron/common/declare/`,
       `OPERATOR_API_PLAN.md`): `param()` fields for what a host shape
       names, `auto()` knobs `resolve(dev)` fills from the device and the
       extents, `In`/`Out` operands declared by shape whose `tile=` makes
       each its own stream into the array (`per=` a column count), `Value`
       members the cores read (trip counts, derived from the extents so the
       array never depends on them), `array(target)`, which builds
       ObjectFIFOs and Workers and binds each operand's lane to a fifo's
       shim end, and optionally `sequence(rt)` when the runtime sequence is
       not the derived one. The array tier is what a tile names plus what
       says `array=True`; one array serves every extent. A shipped binary
       is a subclass declared with `image=Xclbin(...)`, its operands pinned
       with `via=`.
     - The operator's `reference(*inputs)` is the CPU reference the tests
       and the graph reference run; `vectors(op)` in `iron/common/harness`
       draws random inputs for its declared buffers and takes the outputs
       from it.
     - `test = Testing(cases, ...)` on the operator class
       (`iron/common/testing.py`): the shapes it is checked at on a device,
       any `draw=` its inputs need, and a `tolerance=` where the contract
       of the kernel it runs is not the gate. One module,
       `iron/operators/test.py`, runs every declaration against
       `reference()`. An operator whose device test is more than that (a
       composite compared step by step, a shipped binary against its own
       accumulator) keeps a `test.py` beside it.

2. **AIE Kernels** ([mlir-aie `aie_kernels/`](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels))
   - Architecture-specific C++ compute kernels, sourced from the installed
     mlir-aie package (`iron.common.kernels.kernels_dir()`), not from this
     repo. Operators get them from mlir-aie's kernel factories
     (`aie.iron.kernels`), each of which returns an `ExternalFunction`
     carrying its source, flags, symbol and argument types, and in
     `.contract` the tolerance its output is held to:
     - `generic/`: Works on both AIE2 and AIE2P
     - `aie2/`: AIE2-specific (NPU1)
     - `aie2p/`: AIE2P-specific (NPU2)
   - Use AIE API for vectorization (e.g., `aie::mmul`, `aie::add`, `aie::mul`)
   - Compiled to `.o` files and linked into operator `.xclbin`

3. **Common Infrastructure** (`iron/common/`)
   - `declare/`: the declaration layer (`Operator`, `param`/`auto`,
     operands, `Value`, `Scratchpad`/`DispatchTime`, `Xclbin`, inference)
   - `design/`, `tiling.py`, `external.py`: the library-owned build: the
     `Target` a design declares kernels against, the derived runtime
     sequence, legal DMA descriptors, the shipped-image path
   - `graph/`: graph functions (`iron.graph`, `iron.state`) and
     `compile(dev, boundaries=, image=)`
   - `image/`: what a graph lowers onto: `OperatorSequence`, the buffer
     allocator, fusion, the seam onto mlir-aie's `CompilableDesign`, the
     runtime callables and the record of what a compiled image consists of
   - `elementwise.py`: the shared elementwise array and its two operand shapes
   - `kernels.py`: `kernels_dir()` and `declare_kernel`, for a kernel the
     factories do not cover
   - `harness.py`: the device test harness (`vectors`; `run_test`, timed with
     `aie.utils.benchmark.run_iters`; `verify_buffer`, a wrapper over
     mlir-aie's `aie.utils.verify.compare`; `record_metric`)
   - `testing.py`: how an operator declares the shapes it is tested at (`Testing`, `Case`)
   - `tracing.py`: `dump_traces`, for a sequence compiled with `trace_size=`

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

- `rt.fill(slot, view)`: DMA data from host → NPU (shim → L2/L1)
- `rt.drain(slot, view)`: DMA data from NPU → host
- `rt.group()`: Coordinate parallel DMA operations
- views are slices of the declared buffers (`self.A[:, r0:r1, :]`) or
  explicit `Access` descriptors; `tiling.legalize` makes them legal

**Per-call values**: `Scratchpad(T)` members are patched into descriptors
or read by cores without a rebuild; `DispatchTime(T)` regenerates the
sequence per call (xclbin only). A graph binds them to keyword-only
parameters.

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
nothing else. Everything else is a fixed path (`iron.common.kernels.kernels_dir()`), an
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
- `num_aie_rows`: Always 4 for current NPU architectures

**GEMM-specific**:

- `tile_m`, `tile_k`, `tile_n`: Matrix tile dimensions (typically 64)
- Minimum tile sizes depend on `emulate_bf16_mmul_with_bfp16` flag:
  - `True` (default): 8×8×8 minimum
  - `False`: 4×8×8 minimum
- Matrix dimensions must be multiples of `tile × num_rows/columns`
  - `M % (tile_m * 4) == 0`
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
   - `param()` fields for what a host shape names; `auto()` knobs, filled
     by `resolve(dev)` from the device and the extents
   - `In`/`Out` operands by shape, each with its `tile=` in the units a
     core reads (`per=` a column count): an operand with a tile is its own
     stream, `op.x.lane(i)` a shim endpoint, `op.x.tile` the fifo type
   - a `Value(derive=...)` for every trip count the core reads, so the
     array never depends on the extent; what else the array bakes is
     `param(..., array=True)`
   - `array(target)`: build ObjectFIFOs and Workers (`target.kernel(...)`,
     `target.rtp(...)`, `target.barrier()`), `range_()` for loops, and
     `self.x.lane(i).bind(fifo.prod())` / `self.count.bind(rtps)` for every
     member. It sees the array tier alone: reading an extent raises
   - `compatible()` for divisibility against the resolved knobs
   - `sequence(rt)` only if the derived sequence is not the one you want:
     `rt.fill(self.A.lane(i), access)`, `rt.drain(self.C.lane(i), access)`
   - see `iron/common/elementwise.py` for the elementwise families, and
     `gemm/op.py` or `mha/op.py` for hand-written sequences
3. A shipped binary is a subclass declared with the image, `class
   Shipped(X, image=Xclbin(url=, sha256=, filename=))`: it pins the knobs,
   redeclares the operands with `via=` and lays the image's parameter block
   out as a `Value(address=, lock=)`; nothing builds its array
4. Name the kernel with a factory from `aie.iron.kernels`
   (`eltwise.relu_sized(line)`, `norm.rms_norm_eps(tile)`, ...): it carries
   the symbol, the source, the argument types, aie2's LUT tables and the
   tolerance contract. Bind a further symbol of the same object with
   `fn.object_file.bind(symbol, arg_types)`. `target.kernel(...)` declares
   a kernel the factories do not cover (one whose compile flags are the
   operator's own, like flm's `mm_fused.cc`) and, with `source_text=`, one
   written in the operator's own file (the hello-world in
   `iron/tests/toolchain/inline_kernel.py`: a `vadd` in C++ text, the
   argument types the operands' tiles). An operator running one kernel
   reports its contract from `tolerance(target)` (`Elementwise` does this
   from `kernel(target)`). If a new C++ compute kernel is needed, add it
   to the
   [mlir-aie kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)
   with a factory in `aie.iron.kernels`; IRON hosts no kernels
   - Choose appropriate directory: `generic/`, `aie2/`, or `aie2p/`
   - Use AIE API for portable vectorization when possible
   - Add `event0()` and `event1()` for performance profiling
5. Give the operator a `reference(*inputs)` (numpy, on the declared shapes:
   upcast to float32, compute, round once)
6. Declare how it is tested: `test = Testing(cases, tolerance=)` on the
   operator class, from `iron.common.testing`
   - leave `tolerance` out to be judged by the contract of the kernel the
     operator runs (`Operator.reference_tolerance()`); give an
     `aie.utils.verify.Tolerance` where that is not the right gate
   - the cases are `Case(kwargs, extensive=...)` or plain kwarg dicts, or a
     callable returning them when they follow the device's width;
     `channeled_unary_cases`/`binary_elementwise_cases` build the
     elementwise sweeps
   - `extensive=True` keeps a case out of the default suite
   - `draw=` passes `vectors()` its arguments (`normal=`, `centered=`, a given
     tensor or shape per input), or a callable of the operator for an input
     with preconditions (a packed quantization, an angle table)
   - `iron/operators/test.py` runs it; a test with a body of its own goes
     beside the operator and calls `run_test(op, vectors(op), ...)`, with
     `record_metric()` for any figure beyond latency and bandwidth
   - a shape the operator must *refuse* goes in
     `iron/tests/operators/rejected_shapes.py`, which needs no device
7. Register operator in `iron/operators/__init__.py` (`_OPERATOR_MODULES`:
   the name, and the module that defines it)

## Graph Functions

Operators compose into a graph function: a Python function called on
handles, traced once for its shapes, compiled to one image and called per
token. Inputs are its positional parameters, outputs its return values,
weights whatever tensors it closes over, `iron.state(...)` device-resident
state it closes over, and keyword-only parameters annotated
`Scratchpad[T]` per-call values:

```python
import iron
from iron.common import Scratchpad

kv = iron.state((n_kv_groups, max_len, head_dim))

@iron.graph(names_from=model)
def decode(x, angles, *, pos: Scratchpad[np.int32]):
    h = RMSNorm(x, model.norm.weight)             # a bare tensor is a weight
    k = RoPE(GEMV(model.wk, h), angles)          # class calls infer the extents
    Copy(k, kv[:, pos])                          # a state passed as an output is written
    return GEMV(model.wo, h)

net = decode.compile(dev, x=(1, emb), angles=(1, head_dim))
logits = net(x_tok, ang_tok, pos=n)
```

The knobs a graph's operators run with can be a `Profile` rather than
keywords at every call: entries keyed by operator class and shape, given to
`iron.graph(profile=...)` (or applied in a `with profile:` scope). A call
that leaves a knob open takes the most specific entry's value; a call that
gives one keeps it. `iron/applications/llama_3_2_1b/graphs.py::profile` is
the worked example, and `test_llama_names_only_the_knobs_that_matter`
checks that each keyword the graph still passes is one the profile could
not have given.

Operators with equal `array_key()` share one array; with equal
`design_key()` they are one build; `op.explain()` prints which fields are
which and how each value reaches the device. `compile(dev, boundaries=, image=)` derives the image (a
fused ELF on NPU2, per-step xclbins with `boundaries=iron.each_step`) and
`verbose=True` prints why. It links the image (`net.image`) and stops
there: the runtime that loads it is made on the first call, so a host with
the toolchain and no NPU can compile ahead of time.
`iron/applications/llama_3_2_1b/graphs.py` is the worked example;
`iron/tests/common/graph.py` traces it device-free and
`iron/tests/toolchain/` builds it.

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
# under the tolerance contract of the kernel the operator runs ...
run = run_test(op, vectors(op), tolerance=op.reference_tolerance())
assert not run.errors, run.errors

# ... or under an explicit one.
run = run_test(op, vectors(op), tolerance=Tolerance.relative(0.04, 1e-6))
```

`verify_buffer()` compares a single buffer the same way, for tests that
dispatch by hand.

### bfloat16 between torch and numpy

numpy has no bfloat16 of its own; use `ml_dtypes.bfloat16` and move the bits,
never going through float32:

```python
import ml_dtypes, torch

np_array = torch_tensor.view(torch.uint16).numpy().view(ml_dtypes.bfloat16)
torch_tensor = torch.from_numpy(np_array.view("uint16")).view(torch.bfloat16)
```

Runtime tensors take and return torch tensors directly
(`aie.utils.DEFAULT_TENSOR_CLASS.from_torch()`, `.to_torch()`).

## Debugging and Performance

### Building against a local kernel tree

```bash
MLIR_AIE_KERNEL_SOURCES=/path/to/mlir-aie/aie_kernels pytest ...
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

- **small.yml**: Fast operator tests (non-extensive, runs on every PR)
- **extensive.yml**: Full test suite (all operators with extensive tests)
- **test-examples.yml**: Application tests (e.g., Llama inference)
- **ci-lint.yml**: Linting checks (black, clang-format, reuse)

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
  `include/aie_kernels/<arch>/` (`iron.common.kernels.kernels_dir()`,
  overridden by `MLIR_AIE_KERNEL_SOURCES`)
- Ensure the kernel's C++ signature matches the factory from
  `aie.iron.kernels` (or `bind()`'s argument types), or the
  `target.kernel(...)` declaration, that the operator's `array()` names

**Compilation hangs or fails**

- Check MLIR-AIE is installed: `python -c "import aie.iron"`
- Verify `llvm-aie` is available: `which aie-opt`
- Look for errors in the operator's `array()` (common: using `range` instead of `range_()`)

**Test failures with numerical differences**

- Check datatype consistency (bfloat16 has limited precision)
- Verify reference implementation matches NPU kernel exactly
- Look for memory alignment issues in C++ kernel
- Check which tolerance the test judges by: the kernel's contract
  (`op.reference_tolerance()`) unless the test passes `tolerance=`

**Dimension mismatch errors**

- Check operator constraints (e.g., `M % (tile_m * 4) == 0` for GEMM)
- Verify `tile_size`, `num_aie_columns`, and total size are compatible
- Ensure tensor dimensions are multiples of required alignment

**"Invalid configuration: NPU2 has 8 columns"**

- NPU1 supports 1-4 columns only
- NPU2 supports up to 8 columns
- Device type is auto-detected via XRT

**Kernel compilation failures**

- Check kernel is in correct architecture directory (`generic/`, `aie2/`, `aie2p/`)
- Verify `#include <aie_api/aie.hpp>` for AIE API kernels
- Ensure template parameters match function signature
- Check for syntax errors in vectorization code

## Applications

### Llama 3.2 1B Inference

Full LLM inference example at `iron/applications/llama_3_2_1b/`:

- **Required files**: `model.safetensors`, `tokenizer.model` from Hugging Face
- **Default location**: `/srv/llama3.2-1b/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Additional deps**: `pip install -r requirements_examples.txt`
- **Run**: `pytest iron/applications/llama_3_2_1b/`

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
