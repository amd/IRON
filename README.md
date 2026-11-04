<!--
SPDX-FileCopyrightText: Copyright (C) 2025-2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# 🦾 - IRON: Unlocking the Full Potential of NPUs - 🦾

<p align="center">
  <strong>A close-to-metal Python API for AMD Ryzen™ AI NPUs</strong>
</p>

<p align="center">
  <a href="https://amd.github.io/IRON/"><img src="https://img.shields.io/badge/docs-amd.github.io%2FIRON-1565d8" alt="Documentation"></a>
  <a href="https://github.com/amd/IRON/actions/workflows/small.yml?query=branch%3Adevel"><img src="https://github.com/amd/IRON/actions/workflows/small.yml/badge.svg?branch=devel" alt="Tests"></a>
  <a href="./LICENSE"><img src="https://img.shields.io/badge/license-Apache%202.0-blue" alt="License: Apache 2.0"></a>
  <a href="https://discord.gg/UbXzGdXsR5"><img src="https://img.shields.io/badge/Discord-%23ROCm--NPU-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
</p>

<p align="center">
  <a href="https://amd.github.io/IRON/installation/">Install</a> ·
  <a href="./programming_guide/">Programming guide</a> ·
  <a href="https://amd.github.io/IRON/api/">API reference</a> ·
  <a href="https://amd.github.io/IRON/models/">Models</a> ·
  <a href="https://amd.github.io/IRON/performance-checks/">Performance Checks</a>
</p>

<p align="center">
  <img src="./images/XDNA2.png" alt="The AMD XDNA 2 NPU: a grid of AI tiles over memory tiles, DMAs and the Infinity Fabric" width="100%">
</p>

IRON is an open-source Python library for programming the AI Engine array in
[AMD Ryzen™ AI NPUs](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html),
from a single operator up to a whole language model. It is built on the
[MLIR-AIE](https://github.com/Xilinx/mlir-aie) compiler and its `aie.iron`
bindings, and runs on NPU1 (Phoenix, Hawk Point) and NPU2 (Strix, Strix
Halo, Krackan).

- **Operators**: GEMM, GEMV, attention, normalization, RoPE, activations and
  more, each one declared Python class, tested against a numpy reference.
- **Graphs**: a model's operators are recorded once per input shape and
  compiled into one image, so intermediate values stay on the device.
- **Autotuning**: each operator's tunables, and which steps run fused,
  packed into one device configuration or on coded weights, are searched and
  saved in a per-device profile; a model's tune keeps only what leaves it
  bit-identical and faster end to end.
- **Models on the NPU**: Llama 3.2, Granite 4, Gemma 4 (text, vision and
  audio) and EmbeddingGemma 2, every step of the model's graph on the NPU,
  measured nightly by CI.

## Quick start

On Ubuntu 24.04 or 24.10 with the XDNA driver and XRT installed (the
[installation guide](https://amd.github.io/IRON/installation/) covers every
step, including the driver timeout IRON needs):

```bash
git clone https://github.com/amd/IRON.git && cd IRON
python3 -m venv ironenv && source ironenv/bin/activate
source /opt/xilinx/xrt/setup.sh
pip install -r requirements.txt
pip install -e '.[models]'
```

Then, with a Hugging Face token for meta-llama's gated repository:

```python
from iron.applications.llama import Llama

model = Llama.load("meta-llama/Llama-3.2-1B")   # downloads, fits, compiles once
print(model.generate("The capital of France is", 8))   # greedy; pass an iron.lm.Sampler to sample
```

`Llama.load` also takes a local directory holding `config.json`, the
checkpoint and `tokenizer.json`. To write operators and graphs of your own,
start with the [programming guide](./programming_guide/).

## Models

| Model | NPU1 (Phoenix, Hawk Point) | NPU2 (Strix, Strix Halo, Krackan) |
|---|:---:|:---:|
| [Llama 3.2 1B, 3B](./iron/applications/llama/) | ✓ | ✓ |
| [Granite 4.2 3B](./iron/applications/granite/) | ✓ | ✓ |
| [Granite 4.0-H 1B](./iron/applications/granite_hybrid/) | ✓ | ✓ |
| [Gemma 4 E2B](./iron/applications/gemma4/): text, vision and audio | ✓ | ✓ |
| [EmbeddingGemma 2](./iron/applications/embedding_gemma2/) | ✓ | ✓ |
| [Gemma 4 E2B in FastFlowLM](./iron/operators/flm/gemma4_engine/) | | ✓ |

How to run, test and tune each one is on the
[Models](https://amd.github.io/IRON/models/) page; their time to first token
and tokens per second, and every operator's performance, are tracked on
[Performance Checks](https://amd.github.io/IRON/performance-checks/).

## How it works

1. **Operators** (`iron/operators/`): one class each, whose `build()` lays
   out ObjectFIFOs and Workers around a kernel on the AIE tile array.
2. **Kernels**: C++ AIE API kernels from mlir-aie's
   [kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels),
   each carrying its own reference and tolerance.
3. **Graphs and images** (`iron/common/`): a graph's operators share one
   buffer arena; on NPU2 they compose into one full ELF, on NPU1 an xclbin
   per step.
4. **Models** (`iron/lm/`, `iron/applications/`): torch-named, pure-function
   models over a checkpoint's weights, recorded into graphs.

[AGENTS.md](./AGENTS.md) maps the code and its rules, and
[CONTRIBUTING.md](./CONTRIBUTING.md) walks through adding an operator or a
model.

## Community

- 💬 [ROCm Discord](https://discord.gg/UbXzGdXsR5), **#ROCm-NPU** channel, for questions and discussion
- 🐛 [GitHub Issues](https://github.com/amd/IRON/issues) for bugs and feature requests

## Citing IRON

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.

## Acknowledgements

The operators in [`iron/operators/flm/`](./iron/operators/flm/) are ports of
the NPU overlays of [FastFlowLM](https://github.com/ROCm/FastFlowLM)'s Gemma 4
engine, and [`gemma4_engine`](./iron/operators/flm/gemma4_engine/) runs them
inside that engine. FastFlowLM's runtime is MIT-licensed; its NPU binaries,
which the engine example and the `Shipped` test reference fetch from
FastFlowLM, are under its own binary license and are not redistributed here.

## License

IRON is licensed under the [Apache License 2.0](./LICENSE).

-----

<p align="center">Copyright&copy; 2025-2026 Advanced Micro Devices, Inc</p>
