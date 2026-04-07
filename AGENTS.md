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

### Build Directory

Compiled artifacts (`.xclbin`, `.bin`, `.o` files) are stored in `build/` directory by default. The build directory can be customized via `AIEContext(build_dir="path/to/build")`.

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

### C++ (clang-format)

```bash
# Check C++ formatting
python scripts/clang-format-wrapper.py --check

# Show differences
python scripts/clang-format-wrapper.py --diff

# Auto-format all
python scripts/clang-format-wrapper.py --fix

# Format specific directory
python scripts/clang-format-wrapper.py --fix --path aie_kernels/
```

### License Compliance (REUSE)

```bash
# Check all files have proper license headers
reuse lint
```

## Architecture

### Three-Layer Structure

1. **Operators** (`iron/operators/`)
   - Each operator directory contains:
     - `op.py`: Python interface (inherits from `MLIROperator`) - defines operator parameters, compilation artifacts, and runtime argument specs
     - `design.py`: NPU implementation using MLIR-AIE Python API - defines ObjectFIFOs, Workers, and Runtime sequences
     - `reference.py`: CPU reference implementation for validation
     - `test.py`: End-to-end test (build, run, verify against reference)

2. **AIE Kernels** (`aie_kernels/`)
   - Architecture-specific C++ compute kernels:
     - `generic/`: Works on both AIE2 and AIE2P
     - `aie2/`: AIE2-specific (NPU1)
     - `aie2p/`: AIE2P-specific (NPU2)
   - Use AIE API for vectorization (e.g., `aie::mmul`, `aie::add`, `aie::mul`)
   - Compiled to `.o` files and linked into operator `.xclbin`

3. **Common Infrastructure** (`iron/common/`)
   - `base.py`: Base classes (`AIEOperatorBase`, `MLIROperator`, `CompositeOperator`)
   - `compilation/`: Compilation artifact system (MLIR → xclbin)
   - `fusion.py`: Operator fusion framework (`FusedMLIROperator`)
   - `device_manager.py`: XRT device initialization and management (singleton pattern)
   - `context.py`: `AIEContext` for operator compilation/execution
   - `utils.py`: Helper functions (`torch_to_numpy`, `numpy_to_torch`)
   - `test_utils.py`: Test utilities (`verify_buffer`, `nearly_equal`)

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

**Runtime Sequence**: Host-side control flow

- `rt.fill()`: DMA data from host → NPU (shim → L2/L1)
- `rt.drain()`: DMA data from NPU → host
- `rt.start()`: Launch workers
- `rt.task_group()`: Coordinate parallel DMA operations

**Compilation Flow**:

```text
design.py (Python MLIR-AIE API)
    ↓
PythonGeneratedMLIRArtifact
    ↓
MLIR (.mlir file)
    ↓ (aie-opt + aie-translate via Peano toolchain)
xclbin (NPU binary) + insts.bin (instruction sequence)
```

**AIEContext**: Manages compilation and runtime state

- Default build directory: `build/` in current working directory
- Compilation rules: Defines pipeline from Python → MLIR → xclbin
- Device manager: Singleton for XRT resource sharing
- Use `AIEContext(build_dir="...", mlir_verbose=True)` for custom settings

**Device Manager**: Singleton that manages XRT resources

- Automatically initializes `pyxrt.device(0)`
- Caches contexts and kernels per xclbin path
- Shared across all operators to avoid resource conflicts

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

- `size % (num_aie_columns * tile_size) == 0`
- `size % tile_size == 0`

### Memory Hierarchy

- **L3**: Host memory (DDR)
- **L2**: Shared memory tiles (MemTiles in AIE-ML)
- **L1**: Per-core local memory (limited, ~32-64 KB per tile)

Data movement pattern: L3 → Shim DMA → L2 → L1 (tile local) → Compute

## Adding a New Operator

1. Create directory in `iron/operators/<operator_name>/`
2. Implement `op.py`:
   - Subclass `MLIROperator`
   - Implement `get_operator_name()`, `get_mlir_artifact()`, `get_kernel_artifacts()`, `get_arg_spec()`
   - Add validation for dimension constraints (assert statements)
   - Define tile sizes and column counts
3. Implement `design.py`:
   - Import from `aie.iron` (Program, Runtime, Worker, ObjectFifo, Kernel)
   - Define function that builds MLIR-AIE design
   - Use `range_()` for loops (not Python `range`)
   - Handle device-specific logic (NPU1 vs NPU2) if needed
4. Implement C++ kernel in `aie_kernels/<arch>/` if needed
   - Choose appropriate directory: `generic/`, `aie2/`, or `aie2p/`
   - Use AIE API for portable vectorization when possible
   - Add `event0()` and `event1()` for performance profiling
5. Implement `reference.py` with CPU reference
6. Implement `test.py` with pytest tests
   - Use `@pytest.mark.extensive` for slower/larger tests
   - Use `verify_buffer()` from `iron.common.test_utils`
7. Register operator in `iron/operators/__init__.py`

## Operator Fusion

IRON supports fusing multiple operators into a single ELF file. This improves performance enabling a single runtime dispatch for a chain of operators. This works only with the "full ELF" flow, which uses ELF files at runtime. The ELF files take the place of `xclbin`s:

```python
from iron.common.fusion import FusedMLIROperator

# Define individual operators
gemm1 = AIEGEMM(...)
relu = AIERELU(...)
gemm2 = AIEGEMM(...)

# Create fused operator with runlist
# Intermediate buffers are automatically managed
fused_op = FusedMLIROperator(
    name="fused_gemm_relu_gemm",
    runlist=[
        (gemm1, "in", "temp1"),      # (operator, input_buffers, output_buffers)
        (relu, "temp1", "temp2"),
        (gemm2, "temp2", "out"),
    ],
    input_args={"in": size_in},
    output_args={"out": size_out},
    context=ctx
)
```

Benefits of fusion:

- Reduces host ↔ NPU data transfers
- Runs a chain of operators using a single host-side dispatch (one CPU/host interrupt after fusion vs. one interrupt per operator without fusion)

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
from iron.common.test_utils import verify_buffer

# Compare NPU output against CPU reference
errors = verify_buffer(
    output=npu_output,
    buf_name="output",
    reference=cpu_reference,
    rel_tol=0.04,      # 4% relative tolerance
    abs_tol=1e-6,      # Absolute tolerance for small values
    max_error_rate=0.0 # 0% of elements can fail (strict)
)
assert len(errors) == 0, f"Found {len(errors)} mismatches"
```

### Datatype Conversion Helpers

```python
from iron.common.utils import torch_to_numpy, numpy_to_torch

# Convert torch tensor to numpy (preserves bfloat16)
np_array = torch_to_numpy(torch_tensor)

# Convert numpy array to torch (preserves bfloat16)
torch_tensor = numpy_to_torch(np_array)
```

These utilities handle bfloat16 conversion correctly (avoiding float32 intermediate).

## Debugging and Performance

### Debug Mode

Disable XRT runlist for easier debugging (executes kernels individually):

```python
context = AIEContext(use_runlist=False)
```

This sacrifices performance but makes it easier to identify which kernel fails.

### Verbose MLIR Output

Enable verbose MLIR compilation output:

```python
context = AIEContext(mlir_verbose=True)
```

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

- Verify kernel `.cc` file is in correct `aie_kernels/<arch>/` directory
- Check `get_kernel_artifacts()` in `op.py` references correct kernel path
- Ensure kernel function signature matches `Kernel()` declaration in `design.py`

**Compilation hangs or fails**

- Check MLIR-AIE is installed: `python -c "import aie.iron"`
- Verify `llvm-aie` is available: `which aie-opt`
- Look for syntax errors in `design.py` (common: using `range` instead of `range_()`)

**Test failures with numerical differences**

- Check datatype consistency (bfloat16 has limited precision)
- Verify reference implementation matches NPU kernel exactly
- Look for memory alignment issues in C++ kernel
- Adjust tolerances in `verify_buffer()` if needed (`rel_tol`, `abs_tol`)

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

Full LLM inference example at `iron/applications/llama_3.2_1b/`:

- **Required files**: `model.safetensors`, `tokenizer.model` from Hugging Face
- **Default location**: `/srv/llama3.2-1b/` (configurable via `IRON_EXAMPLE_WEIGHTS_DIR`)
- **Additional deps**: `pip install -r requirements_examples.txt`
- **Run**: `pytest iron/applications/llama_3.2_1b/`

### AIE Kernel Reference

See `aie_kernels/README.md` for catalog of available kernels:

- Element-wise ops (add, mul, scale)
- Matrix operations (mm, mv)
- Reductions (add, max, min)
- ML ops (conv2d, relu, exp)
- Vision ops (rgba2gray, filter2d)

Kernels are organized by coding style:

- **AIE API**: Portable C++ template library (recommended)
- **Intrinsics**: Architecture-specific low-level intrinsics (max performance)
- **Generic C**: Works on any AIE family (basic functionality)
