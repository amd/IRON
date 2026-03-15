<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
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
<a href="https://github.com/amd/iron/blob/main/docs/contribute.md" title="Contribution Guide">
    <img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome" /></a>
<a href="https://github.com/amd/iron/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/license-Apache-yellow.svg" alt="license: Apache" /></a>
<a href="https://github.com/psf/black">
    <img src="https://img.shields.io/badge/code%20style-black-000000.svg" alt="Code style: black" /></a>

<p align="center">
   <img src="./images/XDNA2.png" alt="IRONCLAD Logo" style="max-width: 100%; height: auto;">
</p>

IRON is an open-source & close-to-metal Python API enabling fast and efficient execution on [AMD Ryzen™ AI NPUs](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html). It relies on language bindings around the [MLIR-AIE](https://github.com/Xilinx/mlir-aie) dialect. 


The IRON Python API for Ryzen™ AI NPUs is described in the following paper:

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.

#### 🎯 Operator Dashboard

| Section | Description | Datatype | AIE2 | AIE2P | Status | Design Example |
|:--------|:------------|:---------|:-----|:------|:-------|:-------------|
| [Element-wise Add](./aie_kernels/generic/add.cc) | Element-wise addition kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/elementwise_add/](./iron/operators/elementwise_add/) |
| [Element-wise Mul](./aie_kernels/generic/mul.cc) | Element-wise multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/elementwise_mul/](./iron/operators/elementwise_mul/) |
| [GEMM](./aie_kernels/aie2p/mm.cc) | General Matrix Multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gemm/](./iron/operators/gemm/) |
| [GEMV](./aie_kernels/generic/mv.cc) | General Matrix-Vector Multiplication kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gemv/](./iron/operators/gemv/) |
| [GQA](./aie_kernels/aie2p/mha.cc) | Grouped Query Attention kernel (Single pipeline) | bfloat16 | | ✓ | 🟢 | [iron/operators/mha/](./iron/operators/mha/) |
| [MHA](./aie_kernels/aie2p/mha.cc) | Multi-Head Attention kernel & Grouped Query Attention | bfloat16 | | ✓ | 🟢 | [iron/operators/mha/](./iron/operators/mha/) |
| [RMSNorm](./aie_kernels/aie2/rms_norm.cc) | RMSNorm kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rms_norm/](./iron/operators/rms_norm/) |
| [RoPE](./aie_kernels/generic/rope.cc) | Rotary Positional Embedding kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rope/](./iron/operators/rope/) |
| [SiLU](./aie_kernels/aie2/silu.cc) | Sigmoid Linear Unit activation kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/silu/](./iron/operators/silu/) |
| [Softmax](./aie_kernels/aie2/softmax.cc) | Softmax kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/softmax/](./iron/operators/softmax/) |
| [Weighted RMSNorm](./aie_kernels/aie2/rms_norm.cc) | Weighted RMSNorm kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/rms_norm/](./iron/operators/rms_norm/) |
| [Copy](./aie_kernels/generic/passThrough.cc) | Copy | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/mem_copy/](./iron/operators/mem_copy/) |
| [Transpose](./aie_kernels/generic/transpose.cc) | Transpose | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/transpose/](./iron/operators/transpose/) |
| [AXPY](./aie_kernels/generic/axpy.cc) | AXPY | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/axpy/](./iron/operators/axpy/) |
| [Reduction](./aie_kernels/aie2/reduction.cc) | Reduction (sum, max, min) | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/reduction/](./iron/operators/reduction/) |
| [Dequant](./aie_kernels/generic/expand.cc) | Dequant Q4NX from [AWQ](https://github.com/mit-han-lab/llm-awq) to bfloat16 | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/dequant/](./iron/operators/dequant/) |
| [RELU](./aie_kernels/aie2/relu.cc) | RELU | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/relu/](./iron/operators/relu/) |
| [Leaky RELU](./aie_kernels/aie2p/leaky_relu.cc) (WIP) | Leaky RELU kernel | bfloat16 | | ✓ | ⚪ | [iron/operators/leaky_relu/](./iron/operators/leaky_relu/) |
| [GELU](./aie_kernels/aie2/gelu.cc) | GELU | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/gelu/](./iron/operators/gelu/) |
| [LayerNorm](./aie_kernels/aie2/layer_norm.cc) | LayerNorm | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/layer_norm/](./iron/operators/layer_norm/) |
| [Convolution](./aie_kernels/aie2/conv2d.cc) | Conv2D (standard, depthwise, pointwise) | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/conv2d/](./iron/operators/conv2d/) |
| [MaxPool]() | MaxPool | bfloat16 | | | ⚪ |  |
| [AveragePool]() | AveragePool | bfloat16 | | | ⚪ |  |
| [Tanh](./aie_kernels/aie2/tanh.cc) | Tanh kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/tanh/](./iron/operators/tanh/) |
| [Sigmoid](./aie_kernels/aie2/sigmoid.cc) | Sigmoid kernel | bfloat16 | ✓ | ✓ | 🟢 | [iron/operators/sigmoid/](./iron/operators/sigmoid/) |

> Use this dashboard to quickly check the status of each kernel and locate relevant setup, build, and usage information.

## Model Conversion Tools

For converting HuggingFace models (Llama, Mistral, Qwen, Gemma, etc.) to IRON NPU format:

| Tool | Platform | Purpose |
|------|----------|---------|
| [`iron.model_analysis`](./iron/model_analysis/README.md) | Windows, macOS, Linux | **Analysis** - Scan models, detect features, gap analysis |
| [`iron.model_convert`](./iron/model_convert/README.md) | Linux (NPU only) | **Conversion** - Full model conversion to NPU format |

**Quick workflow:**
```bash
# 1. Analyze any model (works on any platform)
python -m iron.model_analysis check meta-llama/Llama-2-7b-hf
python -m iron.model_analysis scan Qwen/Qwen3.5-27B -o scan.json
python -m iron.model_analysis analyze Qwen/Qwen3.5-27B -o report.json

# 2. Convert (Linux with NPU only)
python -m iron.model_convert convert meta-llama/Llama-2-7b-hf -o ./iron_model
```

**Creating custom operators for new architectures?** See the complete guide: [`CREATING_OPERATORS.md`](./iron/model_analysis/CREATING_OPERATORS.md)

#### 📌 Legend

| Status | Meaning            |
|--------|--------------------|
| 🟢     | **Done**           |
| 🟡     | **In Development** |
| ⚪     | **Not Assigned**   |


## Installation (Linux)

These instructions will guide you through everything required for building and executing a program on the Ryzen™ AI NPU, starting from a fresh bare-bones **Ubuntu 24.04** or **Ubuntu 24.10** install.

### Initial Setup

  > Be sure you have the latest BIOS on your laptop or mini-PC that enables the NPU. See [here](#update-bios).

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

1. Install required Python packages (from requirements.txt):
   ```bash
   pip install -r requirements.txt
   ```

1. To test your installation, you can try to build and run the example below:
   ```bash
   ./iron/operators/axpy/test.py
   ```

### Building/Using & Testing Operators

All available operators can be found in `iron/operators`. These each contain:

* `op.py`: The Python operator interface -- an easy access point to integrate operators into your project that prescribes how to compile the operator (build artifacts) and how to call it at runtime (buffer sizes, etc.)
* `design.py`: The implementation of the operator's NPU code. Often references a kernel in `aie_kernels` for the compute core code and describes the data movement using ObjectFIFOs.
* `reference.py`: A reference CPU implementation to validate the correctness of the NPU implementation.
* `test.py`: An end-to-end test that instantiates and builds the operator, runs it and verifies its outputs against the reference.

> NOTE: Be sure the XRT setup script has been sourced and the Python environment is activated: 
>       `source /opt/xilinx/xrt/setup.sh`
>       `source /path/to/ironenv/bin/activate`

To build and test all the operators:
``` bash
pytest iron/operators/ -m "not extensive"
``` 

To run the extensive test suite:
``` bash
pytest iron/operators/
```

To run a specific operator's tests:
``` bash
pytest iron/operators/axpy/
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

-----

<p align="center">Copyright&copy; 2025 Advanced Micro Devices, Inc</p>
