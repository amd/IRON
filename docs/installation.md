<!--
SPDX-FileCopyrightText: Copyright (C) 2025-2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Installation (Linux)

These instructions take a fresh **Ubuntu 24.04** or **Ubuntu 24.10** install
to building and running programs on the Ryzen™ AI NPU.

!!! note "BIOS"
    Ensure your system has the latest BIOS version that enables NPU support.
    Check your laptop or mini-PC manufacturer's support website for BIOS
    updates.

## 1. Kernel, driver and XRT

On Ubuntu 24.04 you may need Linux 6.11 or later, from the Hardware
Enablement (HWE) stack:

```bash
sudo apt update
sudo apt install --install-recommends linux-generic-hwe-24.04
sudo reboot
```

Then install the XDNA™ driver and XRT as
[mlir-aie's instructions](https://github.com/Xilinx/mlir-aie?tab=readme-ov-file#build-and-install-the-xdna-driver-and-xrt)
describe.

## 2. The driver's command timeout

Give the driver a command timeout IRON's longest commands fit in. The amdxdna
driver ends a command after about two periods of its `tdr_timeout_ms` in which
no command on the device starts or finishes (2000 ms by default, so about
4 s), and the run reports `ERT_CMD_STATE_TIMEOUT`. IRON needs
`tdr_timeout_ms=150000`, so a command may run about 300 s. Set it, then
reload the driver or reboot:

```bash
echo "options amdxdna tdr_timeout_ms=150000" | sudo tee /etc/modprobe.d/amdxdna-tdr.conf
sudo modprobe -r amdxdna && sudo modprobe amdxdna
```

The amdxdna 2.21 driver (XRT 2.21) names it `timeout_in_sec`, in seconds
(2 by default); `ls /sys/module/amdxdna/parameters` shows which one yours
has. There, write `options amdxdna timeout_in_sec=150` instead, or set it
until the next reboot without reloading:

```bash
echo 150 | sudo tee /sys/module/amdxdna/parameters/timeout_in_sec
```

On NPU2 a model's prompt chunk is one command, and the deepest chunk, at the
model's native context, is the longest. The timeout must cover it, with room
to spare on a slower device. CI's nightly times a whole prompt at the native
context, which bounds its deepest chunk from above: `long_context`'s TTFT on
the [Benchmarks page](https://amd.github.io/IRON/benchmarks/#bench=long_context&suite=nightly&metric=TTFT).
On NPU1 a command is one operator, the longest an attention layer of the
deepest chunk.

## 3. System packages

IRON needs Python 3.11 to 3.14, the versions the mlir-aie wheels are built
for:

```bash
sudo apt install build-essential clang clang-14 lld lld-14 python3-venv python3-pip
```

## 4. IRON and its Python packages

Clone IRON, set up a virtual environment and source XRT:

```bash
git clone https://github.com/amd/IRON.git
cd IRON
python3 -m venv ironenv
source ironenv/bin/activate
python3 -m pip install --upgrade pip
source /opt/xilinx/xrt/setup.sh
```

Install the pinned packages. The mlir-aie wheel `requirements.txt` pins is a
nightly ([AGENTS.md](../AGENTS.md#environment) says how the pins move), and it
installs this checkout in editable mode:

```bash
pip install -r requirements.txt
```

Loading a model needs the `models` extra (huggingface_hub, tokenizers and
jinja2); the model tests also read images and audio:

```bash
pip install -e '.[models]'               # to load and run models
pip install -r requirements_examples.txt # the extra and the model tests' packages
```

## 5. Check the installation

Build and run one operator on the NPU:

```bash
pytest iron/tests/operators/test_catalog.py -k AXPY
```

## Next steps

- Run a model: [Models](models.md).
- Write your own operators and graphs: the
  [programming guide](programming_guide/README.md).
- The commands that run the operator and model tests:
  [AGENTS.md](../AGENTS.md#commands).
