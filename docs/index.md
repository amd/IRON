---
hide:
  - toc
  - navigation
---

<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON: Unlocking the Full Potential of NPUs

**A close-to-metal Python API for AMD Ryzen™ AI NPUs.**

IRON is an open-source & close-to-metal Python API enabling fast and
efficient execution on [AMD Ryzen™ AI NPUs](https://www.amd.com/en/products/processors/consumer/ryzen-ai.html).
It relies on language bindings around the [MLIR-AIE](https://github.com/Xilinx/mlir-aie)
dialect.

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

<a class="iron-card" href="benchmarks/" markdown>
<span class="iron-card-icon">📊</span>
<span class="iron-card-title">Benchmarks</span>
<span class="iron-card-desc">Operator and model performance, as measured by CI.</span>
</a>

</div>

**Key Features:**

- An operator library (GEMM, MHA, RMSNorm, RoPE, activations, ...) over mlir-aie's `aie.iron`, each operator one declared class
- Graphs: a model's operators recorded once per input shape and compiled into one image, so intermediate values stay on the device
- Autotuning of each operator's tunables into a per-device profile
- Language models compiled for the NPU, from Llama 3.2 1B to a vision-language model; tokenization stays on the host (see [Models](models.md))

## Quick start

After [installing](installation.md) IRON with its `models` extra, and given a
Hugging Face token for meta-llama's gated repository:

```python
from iron.applications.llama import Llama

model = Llama.load("meta-llama/Llama-3.2-1B")   # downloads, fits, compiles once
print(model.generate("The capital of France is", 8))   # greedy; pass an iron.lm.Sampler to sample
```

`Llama.load` also takes a local directory holding `config.json`, the
checkpoint and `tokenizer.json`.

The IRON Python API for Ryzen™ AI NPUs is described in the following paper:

> E. Hunhoff, J. Melber, K. Denolf, A. Bisca, S. Bayliss, S. Neuendorffer, J. Fifield, J. Lo, P. Vasireddy, P. James-Roxby, E. Keller. "[Efficiency, Expressivity, and Extensibility in a Close-to-Metal NPU Programming Interface](https://arxiv.org/abs/2504.18430)". In 33rd IEEE International Symposium On Field-Programmable Custom Computing Machines, May 2025.
