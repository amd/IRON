---
hide:
  - toc
  - navigation
---

<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# 🦾 IRON: Unlocking the Full Potential of NPUs 🦾

**A close-to-metal Python API for AMD Ryzen™ AI NPUs.**

IRON is an open-source Python library for programming the AI Engine array in
[AMD Ryzen™ AI NPUs](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html),
from a single operator up to a whole language model. It is built on the
[MLIR-AIE](https://github.com/Xilinx/mlir-aie) compiler and its `aie.iron`
bindings, and runs on NPU1 (Phoenix, Hawk Point) and NPU2 (Strix, Strix
Halo, Krackan).

![The AMD XDNA 2 NPU: a grid of AI tiles over memory tiles, DMAs and the Infinity Fabric](assets/images/XDNA2.png)

<div class="iron-cards" markdown>

<a class="iron-card" href="installation/" markdown>
<span class="iron-card-icon">🚀</span>
<span class="iron-card-title">Installation</span>
<span class="iron-card-desc">Set up the XDNA driver, XRT, and IRON itself on Ubuntu.</span>
</a>

<a class="iron-card" href="programming_guide/" markdown>
<span class="iron-card-icon">📖</span>
<span class="iron-card-title">Programming Guide</span>
<span class="iron-card-desc">Declare an operator, record a graph of operators, compile it and run it on the NPU.</span>
</a>

<a class="iron-card" href="models/" markdown>
<span class="iron-card-icon">🤖</span>
<span class="iron-card-title">Models</span>
<span class="iron-card-desc">Language models compiled for the NPU, from Llama to Gemma 4.</span>
</a>

<a class="iron-card" href="performance-checks/" markdown>
<span class="iron-card-icon">📊</span>
<span class="iron-card-title">Performance Checks</span>
<span class="iron-card-desc">Operator and model performance, as measured by CI.</span>
</a>

</div>

## Highlights

- **Operators**: GEMM, GEMV, attention, normalization, RoPE, activations and
  more, each one declared Python class, tested against a numpy reference.
- **Graphs**: a model's operators are recorded once per input shape and
  compiled into one image, so intermediate values stay on the device.
- **Autotuning**: each operator's tunables, and which steps run fused,
  packed into one device configuration or on coded weights, are searched and
  saved in a per-device profile; a model's tune keeps only what leaves it
  bit-identical and faster end to end.
- **Models on the NPU**: Llama 3.2, Granite 4, Gemma 4 (text, vision and
  audio) and EmbeddingGemma 2, every step of the model's graph on the NPU.
  See [Models](models.md).

## Quick start

After [installing](installation.md) IRON with its `models` extra
(`pip install -e '.[models]'`), and given a Hugging Face token for
meta-llama's gated repository:

```python
from iron.applications.llama import Llama

model = Llama.load("meta-llama/Llama-3.2-1B")   # downloads, fits, compiles once
print(model.generate("The capital of France is", 8))   # greedy; pass an iron.lm.Sampler to sample
```

`Llama.load` also takes a local directory holding `config.json`, the
checkpoint and `tokenizer.json`.

## Citing IRON

The IRON Python API for Ryzen™ AI NPUs is described in the following paper:

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.
