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

- An operator library (GEMM, MHA, RMSNorm, RoPE, activations, ...) over mlir-aie's `aie.iron`, each operator one declared class
- Graphs: a model's operators recorded once per input shape and compiled into one image, so intermediate values stay on the device
- Autotuning of each operator's tunables into a per-device profile
- End-to-end models on the NPU, from Llama 3.2 1B to a vision-language model (see [Models](#models))

## Quick start

After [installing](#installation-linux) IRON with its `models` extra, and given a Hugging Face token for meta-llama's gated repository:

```python
from iron.applications.llama import Llama

model = Llama.load("meta-llama/Llama-3.2-1B")   # downloads, fits, compiles once
print(model.generate("The capital of France is", 8))   # greedy; pass an iron.lm.Sampler to sample
```

`Llama.load` also takes a local directory holding `config.json`, the checkpoint and `tokenizer.json`.

The IRON Python API for Ryzen™ AI NPUs is described in the following paper:

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.

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
    # IRON needs Python 3.11 or later; our wheels support 3.12 and 3.13
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

1. Install required Python packages (from requirements.txt), the mlir-aie
   release wheel it pins among them:
   ```bash
   pip install -r requirements.txt
   ```

   Loading a model needs the `models` extra (huggingface_hub, tokenizers and
   jinja2); the model tests also read images and audio. From this checkout:
   ```bash
   pip install -e '.[models]'               # to load and run models
   pip install -r requirements_examples.txt # the extra and the model tests' packages
   ```

1. To test your installation, you can try to build and run the example below:
   ```bash
   pytest iron/tests/operators/test_catalog.py -k AXPY
   ```

The commands that run the operator and model tests are in [AGENTS.md](./AGENTS.md#commands).

## Models

Each model is a package under [iron/applications/](./iron/applications/) over [iron/lm/](./iron/lm/), the library every model shares ([AGENTS.md](./AGENTS.md#language-models) describes it); its README says what is its own and where its files come from. The tests find a checkpoint at `$IRON_EXAMPLE_WEIGHTS_DIR/<checkpoint>`, default `/srv` (`iron.lm.testing.weights_dir`).

| Model | Application | Checkpoint |
|---|---|---|
| Llama 3.2 1B, 3B | [llama](./iron/applications/llama/) | `llama3.2-1b`, `llama3.2-3b` |
| Qwen3 1.7B, 0.6B | [qwen3](./iron/applications/qwen3/) | `qwen3-1.7b`, `qwen3-0.6b` |
| Qwen3-Reranker 0.6B (`score`) | [qwen3_reranker](./iron/applications/qwen3_reranker/) | `qwen3-reranker-0.6b` |
| Qwen3-Embedding 0.6B (`embed`) | [qwen3_embedding](./iron/applications/qwen3_embedding/) | `qwen3-embedding-0.6b` |
| Qwen 2.5 1.5B Instruct | [qwen2](./iron/applications/qwen2/) | `qwen2.5-1.5b-instruct` |
| SmolLM2 1.7B Instruct | [smollm2](./iron/applications/smollm2/) | `smollm2-1.7b-instruct` |
| Phi-4-mini-instruct | [phi3](./iron/applications/phi3/) | `phi-4-mini-instruct` |
| Granite 4.2 3B | [granite](./iron/applications/granite/) | `granite-4.2-3b` |
| SmolLM3 3B | [smollm3](./iron/applications/smollm3/) | `smollm3-3b` |
| Gemma 3 1B | [gemma3](./iron/applications/gemma3/) | `gemma-3-1b-it` |
| Gemma 4 E2B text decoder | [gemma4](./iron/applications/gemma4/) | `gemma-4-e2b-it` |
| Qwen3.5 0.8B text decoder | [qwen3_5](./iron/applications/qwen3_5/) | `qwen3.5-0.8b` |
| Qwen3-30B-A3B (reference only) | [qwen3_moe](./iron/applications/qwen3_moe/) | `qwen3-30b-a3b` |
| Granite 4.0-H (reference only) | [granite_hybrid](./iron/applications/granite_hybrid/) | none yet |
| Ministral 3 text decoder (drawn weights) | [ministral3](./iron/applications/ministral3/) | none yet |
| LFM2-1.2B | [lfm2](./iron/applications/lfm2/) | `lfm2-1.2b` |
| SmolVLM-256M-Instruct | [idefics3](./iron/applications/idefics3/) | `smolvlm-256m-instruct` |
| EmbeddingGemma 2 | [embedding_gemma2](./iron/applications/embedding_gemma2/) | `embeddinggemma-2` |
| ResNet-50 | [resnet](./iron/applications/resnet/) | `resnet-50` |
| YOLOX-Nano | [yolox](./iron/applications/yolox/) | `yolox-nano` |
| Whisper (toy shape) | [whisper](./iron/applications/whisper/) | none: drawn weights |
| Gemma 4 E2B in FastFlowLM | [gemma4_engine](./iron/operators/flm/gemma4_engine/) | `$FLM_MODEL_PATH` (the tests default to `fastflowlm`) |

What the text decoders (Llama to LFM2 above) share:

- **Setup**: `requirements_examples.txt`, as [installing](#installation-linux) says. XRT maps every device buffer locked, and a model's weights and caches are banks of at most 3.5 GiB (`iron.common.image.allocator.BANK`), so `ulimit -l` must cover one bank.

- **Run**: `python -m iron.applications.<application>.model <directory or repository id> [--prompt TEXT]`, the directory holding `config.json`, the checkpoint and the tokenizer; `-v` logs each compile; `--help` lists the options, and [Llama's README](./iron/applications/llama/README.md#running) explains them.
- **Test**: `pytest tests/applications/<application>/` (or `tests/applications/decoders/ -k <application>` for the decoders that share one test) loads the model once and checks throughput, accuracy against transformers' logits recorded in `golden.npz` beside the checkpoint, and determinism. `pytest <test> --record-goldens -p no:xdist` records missing logits where torch and transformers are installed; they are not IRON's requirements.
- **Tune**: `python -m iron.lm.tune <application> --checkpoint <directory>/model.safetensors` times each operator at every setting of its tunables and rewrites the application's `profiles/<device>.json`; review it with `git diff` and commit it.

## Architecture

1. **Operators** (`iron/operators/`): each operator is one class, imported in [iron/operators/\_\_init\_\_.py](./iron/operators/__init__.py); its docstring says what it computes. Its parameters are declared with mlir-aie's `param()` (a tunable with `tunable()`, a per-call value with `per_call()`); its operands are aie.iron's `In`/`Out`/`InOut`, declared by shape. Its `build()` builds the array with ObjectFIFOs and Workers around a kernel; the library derives the runtime sequence unless the operator writes it. Its `reference()` and `test = Testing(...)` are what `iron/tests/operators/test_catalog.py` checks it by.
2. **Kernels** ([mlir-aie `aie_kernels/`](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)): C++ compute kernels, vectorized with the AIE API, reached through mlir-aie's kernel factories (`aie.iron.kernels`), which also carry each kernel's reference and tolerance. IRON hosts no kernels of its own, apart from the FastFlowLM Gemma 4 engine's overrides (`iron/operators/flm/gemma4_engine/`).
3. **Graphs and images** (`iron/common/`): a graph is recorded on handles and lowered onto an image: its buffers placed in one arena, and on NPU2 its operators' designs composed into one full ELF that runs them in turn (on NPU1, an xclbin per step), run through XRT.
4. **Models** (`iron/lm/`, `iron/applications/`): see [Models](#models).

## Community and Support

- 💬 **Discord**: Join our [Discord server](https://discord.gg/cW99Ds85e8) for discussions and support
- 🐛 **Issues**: Report bugs and request features via [GitHub Issues](https://github.com/amd/iron/issues)
- 📖 **Contributing**: See [CONTRIBUTING.md](./CONTRIBUTING.md) for development guidelines
- 📚 **Documentation**: [AGENTS.md](./AGENTS.md) for the rules and the map of the code, operator docstrings in `iron/operators/`, kernel docs in the [mlir-aie kernel library](https://github.com/Xilinx/mlir-aie/tree/main/aie_kernels)

## License

IRON is licensed under the Apache License 2.0. See [LICENSE](./LICENSE) for details.

-----

<p align="center">Copyright&copy; 2025-2026 Advanced Micro Devices, Inc</p>
