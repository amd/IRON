<!--
SPDX-FileCopyrightText: Copyright (C) 2025-2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# 🦾 - IRON: Unlocking the Full Potential of NPUs - 🦾

<a href="https://discord.gg/cW99Ds85e8">
    <img src="https://img.shields.io/badge/Discord-7289DA?logo=discord&logoColor=white" alt="Discord" /></a>
<a href="https://github.com/amd/iron/releases/latest" title="Download the latest release">
   <img src="https://img.shields.io/github/v/release/amd/iron?include_prereleases" alt="Latest Release" /></a>
<a href="https://tooomm.github.io/github-release-stats/?username=amd&repository=iron">
   <img src="https://img.shields.io/github/downloads/amd/iron/total.svg" alt="GitHub downloads" /></a>
<a href="https://github.com/amd/iron/actions" title="Check out our tests">
   <img src="https://github.com/amd/iron/actions/workflows/small.yml/badge.svg" alt="Iron Tests" /></a>
<a href="https://github.com/amd/iron/blob/main/CONTRIBUTING.md" title="Contribution Guide">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
<a href="https://github.com/amd/iron/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache-yellow.svg" alt="license: Apache" /></a>
<a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" /></a>

<p align="center">
   <img src="./images/XDNA2.png" alt="IRON Logo" style="max-width: 100%; height: auto;">
</p>

IRON is an open-source & close-to-metal Python API enabling fast and efficient execution on [AMD Ryzen™ AI NPUs](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html). It relies on language bindings around the [MLIR-AIE](https://github.com/Xilinx/mlir-aie) dialect.

**Key Features:**

- Close-to-metal NPU programming via MLIR-AIE Python bindings
- Pre-built operator library (GEMM, MHA, RMSNorm, RoPE, activations, etc.)
- Operator fusion for optimal performance
- Extensible architecture for custom operators
- End-to-end LLM inference (Llama 3.2 1B example included)

The IRON Python API for Ryzen™ AI NPUs is described in the following paper:

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.

#### 🎯 Operator Dashboard

| Section | Description | Datatype | AIE2 | AIE2P | Status | Design Example |
|:--------|:------------|:---------|:-----|:------|:-------|:-------------|
| [Element-wise Add](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/eltwise/add.cc) | Element-wise addition kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/elementwise_add.py](./iron/operators/elementwise_add.py) |
| [Element-wise Mul](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/eltwise/mul.cc) | Element-wise multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/elementwise_mul.py](./iron/operators/elementwise_mul.py) |
| [GEMM](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/linalg/mm.cc) | General Matrix Multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gemm.py](./iron/operators/gemm.py) |
| [Alternative GEMM](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/fused/mm_fused.h) | General Matrix Multiplication with a fused activation epilogue, specialised for transformer projection shapes. M, K and N are runtime parameters, so one xclbin serves every shape. B is stored as bfp16 on AIE2P | bfloat16, bfp16 | ✓ | ✓ | 🟢 | [iron/operators/flm/gemm/](./iron/operators/flm/gemm/) |
| [GEMV](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/linalg/mv_bf16.cc) | General Matrix-Vector Multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gemv.py](./iron/operators/gemv.py) |
| [GQA](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/linalg/mha.cc) | Grouped Query Attention kernel (Single pipeline) | bfloat16 | | ✓ | 🟢 | [iron/operators/mha.py](./iron/operators/mha.py) |
| [MHA](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/linalg/mha.cc) | Multi-Head Attention kernel & Grouped Query Attention | bfloat16 | | ✓ | 🟢 | [iron/operators/mha.py](./iron/operators/mha.py) |
| [RMSNorm](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/norm/rms_norm.cc) | RMSNorm kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rms_norm.py](./iron/operators/rms_norm.py) |
| [RoPE](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/datamovement/rope.cc) | Rotary Positional Embedding kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rope.py](./iron/operators/rope.py) |
| [SiLU](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/silu.cc) | Sigmoid Linear Unit activation kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/silu.py](./iron/operators/silu.py) |
| [Softmax](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/softmax.cc) | Softmax kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/softmax.py](./iron/operators/softmax.py) |
| SwiGLU | The gated feed-forward block, a graph of GEMV or GEMM (by row count), SiLU and element-wise multiplication | bfloat16 | | ✓ | 🟢 | [iron/lm/layers.py](./iron/lm/layers.py) |
| [Weighted RMSNorm](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/norm/rms_norm.cc) | Weighted RMSNorm kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rms_norm.py](./iron/operators/rms_norm.py) |
| Copy | A copy between two views, moved by the DMAs alone (no kernel) | any | ✓ | ✓ | 🟢 | [iron/operators/copy.py](./iron/operators/copy.py) |
| [Transpose](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/datamovement/transpose.cc) | Transpose | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/transpose.py](./iron/operators/transpose.py) |
| [AXPY](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/datamovement/axpy.cc) | AXPY | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/axpy.py](./iron/operators/axpy.py) |
| [Reduction]() | Reduction | bfloat16 | | | 🟡 |  |
| [Dequant](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/datamovement/expand.cc) | Dequant Q4NX from [AWQ](https://github.com/mit-han-lab/llm-awq) to bfloat16 | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/dequant.py](./iron/operators/dequant.py) |
| [Dequant to bfp16](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/quant/q4nx_dequant.cc) | Dequant Q4NX to bfp16, laid out for the B operand of the [alternative GEMM](./iron/operators/flm/gemm/) | q4nx → bfp16 | | ✓ | 🟢 | [iron/operators/flm/dequant/](./iron/operators/flm/dequant/) |
| [RELU](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/eltwise/relu.cc) | RELU | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/relu.py](./iron/operators/relu.py) |
| [Leaky RELU](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/leaky_relu.cc) | Leaky RELU | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/leaky_relu.py](./iron/operators/leaky_relu.py) |
| [GELU](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/gelu.cc) | GELU | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gelu.py](./iron/operators/gelu.py) |
| [LayerNorm](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/norm/layer_norm.cc) | LayerNorm | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/layer_norm.py](./iron/operators/layer_norm.py) |
| [Convolution]() | Convolution | bfloat16 | | | 🟡 |  |
| [MaxPool]() | MaxPool | bfloat16 | | | ⚪ |  |
| [AveragePool]() | AveragePool | bfloat16 | | | ⚪ |  |
| [Tanh](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/tanh.cc) | Tanh kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/tanh.py](./iron/operators/tanh.py) |
| [Sigmoid](https://github.com/Xilinx/mlir-aie/blob/main/aie_kernels/activation/sigmoid.cc) | Sigmoid kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/sigmoid.py](./iron/operators/sigmoid.py) |

> Use this dashboard to quickly check the status of each kernel and locate relevant setup, build, and usage information.

#### 📌 Legend

| Status | Meaning            |
|--------|--------------------|
| 🟢     | **Done**           |
| 🟡     | **In Development** |
| ⚪     | **Not Assigned**   |


## Installation (Linux)

These instructions will guide you through everything required for building and executing a program on the Ryzen™ AI NPU, starting from a fresh bare-bones **Ubuntu 24.04** or **Ubuntu 24.10** install.

### Initial Setup

  > **Important**: Ensure your system has the latest BIOS version that enables NPU support. Check your laptop/mini-PC manufacturer's support website for BIOS updates.

If starting from `Ubuntu 24.04` you may need to update the Linux kernel to 6.11+ by installing the Hardware Enablement (HWE) stack:

  ```bash
  sudo apt update
  sudo apt install --install-recommends linux-generic-hwe-24.04
  sudo reboot
  ```

1. Install XDNA™ Driver and XRT:

    > [Instructions from mlir-aie repository](https://github.com/Xilinx/mlir-aie?tab=readme-ov-file#build-and-install-the-xdna-driver-and-xrt)

1. Install the packages needed for IRON and MLIR-AIE:

    ```bash
    # Python versions 3.10, 3.12 and 3.13 are currently supported by our wheels
    sudo apt install \
    build-essential clang clang-14 lld lld-14 python3-venv python3-pip
    ```

1. Setup a virtual environment and activate it:
   ```bash
   python3 -m venv ironenv
   source ironenv/bin/activate
   python3 -m pip install --upgrade pip
   ```

1. Source XRT (installed in step 1):
   ```bash
   source /opt/xilinx/xrt/setup.sh
   ```

1. Install required Python packages (from requirements.txt), mlir-aie's
   nightly wheel among them:
   ```bash
   pip install -r requirements.txt
   ```

1. To test your installation, you can try to build and run the example below:
   ```bash
   pytest iron/tests/operators/catalog.py -k AXPY
   ```

### Building/Using & Testing Operators

All available operators can be found in `iron/operators`. These each contain:

- `op.py` (or `<name>.py` for a small operator): The operator, one declared class (see `iron/common/declare/` and the Architecture section of `AGENTS.md`): its tunables, its operands declared by shape with the tile each streams into the array in, the values the cores read, and `array()`, which builds the array with ObjectFIFOs and Workers around a C++ kernel from the [mlir-aie kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels). The library derives the runtime sequence from that declaration, or the operator writes it by hand. One array serves every extent, so one build of it serves many shapes.
- The operator's `reference()` method: the CPU implementation the NPU result is checked against, on the declared shapes.
- `test = Testing(cases, ...)` on the operator class: the shapes it is checked at on a device. `iron/tests/operators/catalog.py` runs every operator's declaration, building it, running `vectors(op)` through it and verifying against the reference. An operator with a device test of its own keeps a `test.py` beside it.

Operators compose into graphs: a subclass of `iron.Graph` whose `body()` is called on handles, traced once per input shape, compiled to one image per shape and called per token (see `iron/common/graph/`; `iron/lm/llama3/model.py` is the worked example, its tunables a `Profile` the graph carries rather than keywords at every call).

> NOTE: Be sure the XRT setup script has been sourced and the Python environment is activated:
>       `source /opt/xilinx/xrt/setup.sh`
>       `source /path/to/ironenv/bin/activate`

To build and test all the operators:

``` bash
pytest iron/operators/ iron/tests/ -m "not extensive"
```

To run the extensive test suite:

``` bash
pytest iron/operators/ iron/tests/
```

To run a specific operator's tests:

``` bash
pytest iron/tests/operators/catalog.py -k AXPY
```

### Git Hooks (Optional but Recommended)

To ensure your code passes CI linting checks before pushing, install the pre-push hook:

```bash
cp scripts/hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
```

The hook will run the same linting checks as CI:

- License checks (reuse)
- Python formatting (black)
- C++ formatting (clang-format)

To bypass the hook if needed: `git push --no-verify`

## Language Models

### Llama 3.2 1B Inference

IRON includes a complete LLM inference example demonstrating NPU acceleration:

- **Location**: `iron/applications/llama_3.2_1b/`, over the model package `iron/lm/llama3/` and the decoder every model shares (`iron/lm/`)
- **Model**: Meta Llama 3.2 1B
- **Features**: Multi-head attention, fused operators, bfloat16 quantization

See [iron/applications/llama_3.2_1b/README.md](./iron/applications/llama_3.2_1b/README.md) for setup and usage instructions.

### EmbeddingGemma 2

- **Location**: `iron/applications/embeddinggemma_2/`, over the model package `iron/lm/embeddinggemma2/`
- **Model**: EmbeddingGemma 2's text encoder, text to a unit-length embedding

See [iron/applications/embeddinggemma_2/README.md](./iron/applications/embeddinggemma_2/README.md) for setup and usage instructions.

## Architecture

IRON uses a three-layer architecture:

1. **Operators** (`iron/operators/`): High-level Python API for NPU operations
   - Each operator is one declared class with its array and its CPU reference (a file at the root, or `op.py` in a package), and a `test = Testing(...)` that `iron/tests/operators/catalog.py` runs; a few keep a `test.py` beside them for a device test of their own

2. **AIE Kernels** ([mlir-aie `aie_kernels/`](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)): Low-level C++ compute kernels
   - Organized by family (`activation/`, `eltwise/`, `linalg/`, `norm/`, ...); architecture-specific
     code lives in `*_aie2.h` / `*_aie2p.h` headers the family's `.cc` selects between
   - Vectorized using AIE API for optimal performance

3. **Common Infrastructure** (`iron/common/`): Compilation, device management, and utilities
   - The declaration layer (`declare/`), the design and its runtime sequence (`design/`), the images (`image/`) and graphs (`graph/`)
   - MLIR-AIE compilation pipeline
   - XRT runtime integration

## Performance

IRON operators are designed for maximum NPU utilization:

- Parallel execution across multiple AIE columns
- Optimized data movement via ObjectFIFOs
- Fused operations to minimize host-NPU transfers
- Vectorized kernels using AIE intrinsics

Run benchmarks:

```bash
# Run all operators with performance metrics stored in tests_latest.csv
pytest iron/operators/ iron/tests/ -m "not extensive" -v
```

## Community and Support

- 💬 **Discord**: Join our [Discord server](https://discord.gg/cW99Ds85e8) for discussions and support
- 🐛 **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/amd/iron/issues)
- 📖 **Contributing**: See [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines
- 📚 **Documentation**: Operator examples in `iron/operators/`, kernel docs in the [mlir-aie kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)

## License

IRON is licensed under the Apache License 2.0. See [LICENSE](./LICENSE) for details.

-----

<p align="center">Copyright&copy; 2025-2026 Advanced Micro Devices, Inc</p>
