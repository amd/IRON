<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON models in FastFlowLM

This application explicitly compiles the IRON graphs for Llama 3.2 1B and
EmbeddingGemma 2, then serves them through FastFlowLM's HTTP API. FastFlowLM
runs each model in a persistent Python worker over a Unix socket pair. The
worker retrieves the compiled images from the shared MLIR-AIE cache, loads the
images and weights, and dispatches inference on the NPU.

The Makefile pins the FastFlowLM fork to
[`afbbd18d`](https://github.com/andrej/FastFlowLM/commit/afbbd18d3fb73c71b1eb3b3ea655da0ee7396faf),
which contains the IRON backend and the EmbeddingGemma 2 model entry.

> [Changes to FastFlowLM to add the IRON backend and EmbeddingGemma 2 model](https://github.com/ROCm/FastFlowLM/compare/8d6768dab2fd8616ea3b814f611ff01a0758681f...andrej:FastFlowLM:iron-backend)

## Prerequisites

Use an NPU2 machine with XRT and the IRON environment installed as described in
the [repository setup](../../../README.md#installation-linux). FastFlowLM also
needs CMake, Ninja, a C++20 compiler, its documented Linux development packages,
and its `tokenizers-cpp` submodule. The Makefile initializes the submodule.

The IRON checkpoint directories must contain:

```text
<models>/llama3.2-1b/model.safetensors
<models>/llama3.2-1b/tokenizer.model
<models>/embeddinggemma-2/model.safetensors
<models>/embeddinggemma-2/tokenizer.json
```

Run these steps from `iron/applications/fastflowlm_iron`.

1. Activate IRON and XRT, then select the model and compilation-cache paths.

   ```bash
   source /opt/xilinx/xrt/setup.sh
   source ../../../.venv/bin/activate
   export MODELS=/path/to/models
   export CACHE=$PWD/build/cache
   ```

2. Compile all required graph versions. Llama builds its decode and 2048-row
   prompt versions. EmbeddingGemma 2 builds 64-, 128-, 256- and 512-row
   versions. The scripts compile and link the images but do not load them or
   upload weights.

   ```bash
   make compile MODELS=$MODELS CACHE=$CACHE IRON_PYTHON=$VIRTUAL_ENV/bin/python
   ```

   `compile_llama.py --max-seq-len` accepts another multiple of 2048.
   `compile_embeddinggemma2.py --max-tokens` accepts another multiple of 64 and
   builds doubling versions from 64 rows, then the requested maximum. Each
   script prints the image and `artifacts.json` paths under `$CACHE`.

3. Clone and build the pinned FastFlowLM engine with `FLM_ENABLE_IRON=ON`.

   ```bash
   make flm IRON_PYTHON=$VIRTUAL_ENV/bin/python
   ```

4. Pull FastFlowLM's serving packages. FastFlowLM uses its Llama package for
   chat metadata and tokenization while the worker reads the BF16 IRON
   checkpoint from `$MODELS/llama3.2-1b`. EmbeddingGemma 2 uses the same public
   checkpoint for FastFlowLM and IRON.

   ```bash
   make pull MODELS=$MODELS
   ```

5. Start Llama 3.2 1B. This command uses the same cache as step 2, then loads
   the images and uploads the weights.

   ```bash
   make serve-llama MODELS=$MODELS CACHE=$CACHE \
       IRON_PYTHON=$VIRTUAL_ENV/bin/python PORT=52625
   ```

6. Send a chat request from another terminal.

   ```bash
   curl -sS http://127.0.0.1:52625/v1/chat/completions \
       -H 'Content-Type: application/json' \
       -d '{"model":"llama3.2:1b","messages":[{"role":"user","content":"What is 347 + 589?"}],"max_tokens":32}' \
       | python3 -m json.tool
   ```

7. Stop the Llama server with `Ctrl+C`, then start EmbeddingGemma 2.

   ```bash
   make serve-embedding MODELS=$MODELS CACHE=$CACHE \
       IRON_PYTHON=$VIRTUAL_ENV/bin/python PORT=52625
   ```

8. Request a normalized 768-element embedding.

   ```bash
   curl -sS http://127.0.0.1:52625/v1/embeddings \
       -H 'Content-Type: application/json' \
       -d '{"model":"embeddinggemma-2","input":"What causes the northern lights?"}' \
       | python3 -m json.tool
   ```

The direct model commands in the
[Llama guide](../llama_3.2_1b/README.md) and
[EmbeddingGemma 2 guide](../embeddinggemma_2/README.md) run the same graph
classes in the command's Python process. They do not use the FastFlowLM worker.
The Makefile's server targets instead start `python -m flm_iron.worker`; C++
sends token histories or text over the socket, and the worker returns BF16
logits or float32 embeddings.
