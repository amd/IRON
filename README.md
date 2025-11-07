<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# 🦾 - IRON: Unlocking the Full Potential of NPUs - 🦾

<a href="https://discord.gg/Qm6FCD78Xb">
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

| Section | Description | Datatype | Status | Design Example |
|:--------|:------------|:---------|:-------|:-------------|
| [Element-wise Add](./aie_kernels/aie2/add.cc) | Element-wise addition kernel | bfloat16 | 🟢 | [example/elementwise_add/](./example/elementwise_add/) |
| [Element-wise Mul](./aie_kernels/aie2/mul.cc) | Element-wise multiplication kernel | bfloat16 | 🟢 | [example/elementwise_mul/](./example/elementwise_mul/) |
| [GEMM](./aie_kernels/aie2p/mm.cc) | General Matrix Multiplication kernel | bfloat16 | 🟢 | [example/gemm/](./example/gemm/) |
| [GEMV](./aie_kernels/aie2/mv.cc) | General Matrix-Vector Multiplication kernel | bfloat16 | 🟢 | [example/gemv/](./example/gemv/) |
| [GQA](./aie_kernels/aie2p/mha.cc) | Grouped Query Attention kernel (Single pipeline) | bfloat16 | 🟢 | [example/mha/](./example/mha/) |
| [MHA](./aie_kernels/aie2p/mha.cc) | Multi-Head Attention kernel & Grouped Query Attention | bfloat16 | 🟢 | [example/mha/](./example/mha/) |
| [RMSNorm](./aie_kernels/aie2p/rms_norm.cc) | RMSNorm kernel | bfloat16 | 🟢 | [example/rms_norm/](./example/rms_norm/) |
| [RoPE](./aie_kernels/aie2p/rope.cc) | Rotary Positional Embedding kernel | bfloat16 | 🟢 | [example/rope/](./example/rope/) |
| [SiLU](./aie_kernels/aie2p/silu.cc) | Sigmoid Linear Unit activation kernel | bfloat16 | 🟢 | [example/silu/](./example/silu/) |
| [Softmax](./aie_kernels/aie2p/softmax.cc) | Softmax kernel | bfloat16 | 🟢 | [example/softmax/](./example/softmax/) |
| [Weighted RMSNorm](./aie_kernels/aie2p/rms_norm.cc) | Weighted RMSNorm kernel | bfloat16 | 🟢 | [example/rms_norm/](./example/rms_norm/) |
| [Copy](./aie_kernels/generic/passThrough.cc) | Copy | bfloat16 | 🟢 | [example/copy/](./example/copy/) |
| [Transpose](./aie_kernels/aie2p/transpose.cc) | Transpose | bfloat16 | 🟢 | [example/transpose/](./example/transpose/) |
| [AXPY](./aie_kernels/aie2p/axpy.cc) | AXPY | bfloat16 | 🟢 | [example/axpy/](./example/axpy/) |
| [Reduction]() | Reduction | bfloat16 | 🟡 |  |
| [Dequant](./aie_kernels/aie2/expand.cc) | Dequant Q4NX from [AWQ](https://github.com/mit-han-lab/llm-awq) to bfloat16 | bfloat16 | 🟢 | [example/dequant/](./example/dequant/) |
| [RELU](./aie_kernels/aie2p/relu.cc) | RELU | bfloat16 | 🟢 | [example/relu/](./example/relu/) |
| [Leaky RELU](./aie_kernels/aie2p/leaky_relu.cc) | Leaky RELU kernel | bfloat16 | 🟢 | [example/leaky_relu/](./example/leaky_relu/) |
| [GELU](./aie_kernels/aie2p/gelu.cc) | GELU | bfloat16 | 🟢 | [example/gelu/](./example/gelu/) |
| [LayerNorm](./aie_kernels/aie2p/layer_norm.cc) | LayerNorm | bfloat16 | 🟢 | [example/layer_norm/](./example/layer_norm/) |
| [Convolution]() | Convolution | bfloat16 | 🟡 |  |
| [MaxPool]() | MaxPool | bfloat16 | ⚪ |  |
| [AveragePool]() | AveragePool | bfloat16 | ⚪ |  |

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
    build-essential clang clang-14 lld lld-14 cmake ninja-build python3-venv python3-pip
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
   MLIR_PYTHON_EXTRAS_SET_VERSION="0.0.8.3" HOST_MLIR_PYTHON_PACKAGE_PREFIX="aie" pip install -r requirements.txt
   ```

1. To test your installation, you can try to build and run the example below:
   ```bash
   cmake -B build
   cmake --build build --target silu_1_cols_1_channels_2048_tile_2048_run
   ```

Note: On a fresh install, if you get `CMake Error: Could not find CMAKE_ROOT !!!`, just deactivate and reactivate your python environment.

### Building & Testing

> NOTE: Be sure the XRT setup script has been sourced: 
>       `source /opt/xilinx/xrt/setup.sh`

IRON is a CMake-based project. To configure the project, run:
```shell
cmake -B build
```

To build all designs, use: 
```shell
cmake --build build
```

To test all the designs, use the following python script:
``` python
./scripts/run_tests.py --iter 1
``` 
You can select a single test to run using the `--select` flag.

> Targets are listed when running `cmake -B build` with the following syntax:
> ```
> Registering Executable: <TARGET_NAME>
> ```

If you want to build only a specific design, run:
```shell
# Example: cmake --build build --target silu_4_cols_1_channels_2048_tile_512
cmake --build build --target <TARGET_NAME>
```

You can also test an individual (or a selection of multiple) test(s) using the same script:
```shell
./scripts/run_tests.py --select <TARGET_ONE> --select <TARGET_TWO>
```

Additionally a target to build & run is made available under the `<TARGET_NAME>_run` symbol. 
```shell
cmake --build build --target silu_4_cols_1_channels_2048_tile_512_run
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
