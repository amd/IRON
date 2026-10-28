<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON models in FastFlowLM

This application serves Llama 3.2 1B and EmbeddingGemma 2 through FastFlowLM's
HTTP API. FastFlowLM runs each model in IRON's persistent Python server over a
Unix socket pair. The server compiles the graph versions through the MLIR-AIE
cache on first use, then loads the images and weights.

The Makefile pins the FastFlowLM fork to
[`a84802b8`](https://github.com/andrej/FastFlowLM/commit/a84802b81ee46cdd2aa82daff03e3426fe881701),
which contains the IRON backend and the EmbeddingGemma 2 model entry.

> [Changes to FastFlowLM to add the IRON backend and EmbeddingGemma 2 model](https://github.com/ROCm/FastFlowLM/compare/3b72cd0535ffa82389797491e15e117497cc9f88...andrej:FastFlowLM:iron-backend)

## Prerequisites

Use an NPU2 machine with XRT and the IRON environment installed as described in
the [repository setup](../../../README.md#installation-linux). FastFlowLM also
needs CMake, Ninja, a C++20 compiler, its documented Linux development packages,
and its `tokenizers-cpp` submodule. The Makefile initializes the submodule.

The IRON checkpoint directories must contain:

```text
<models>/llama3.2-1b/config.json
<models>/llama3.2-1b/model*.safetensors*
<models>/llama3.2-1b/tokenizer.json
<models>/embeddinggemma-2/config.json
<models>/embeddinggemma-2/model*.safetensors*
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

2. Clone and build the pinned FastFlowLM engine with `FLM_ENABLE_IRON=ON`.

   ```bash
   make flm IRON_PYTHON=$VIRTUAL_ENV/bin/python
   ```

3. Pull FastFlowLM's serving packages. FastFlowLM uses its Llama package for
   chat metadata and tokenization while the worker reads the BF16 IRON
   checkpoint from `$MODELS/llama3.2-1b`. EmbeddingGemma 2 uses the same public
   checkpoint for FastFlowLM and IRON.

   ```bash
   make pull MODELS=$MODELS
   ```

4. Start Llama 3.2 1B. The first invocation compiles the graph versions, then
   loads the images and uploads the weights. Later invocations reuse the cache.

   ```bash
   make serve-llama MODELS=$MODELS CACHE=$CACHE \
       IRON_PYTHON=$VIRTUAL_ENV/bin/python PORT=52625
   ```

5. Send a chat request from another terminal.

   ```bash
   curl -sS http://127.0.0.1:52625/v1/chat/completions \
       -H 'Content-Type: application/json' \
       -d '{"model":"llama3.2:1b","messages":[{"role":"user","content":"What is 347 + 589?"}],"max_tokens":32}' \
       | python3 -m json.tool
   ```

6. Stop the Llama server with `Ctrl+C`, then start EmbeddingGemma 2.

   ```bash
   make serve-embedding MODELS=$MODELS CACHE=$CACHE \
       IRON_PYTHON=$VIRTUAL_ENV/bin/python PORT=52625
   ```

7. Request a normalized 768-element embedding.

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
The Makefile's server targets instead start `python -m iron.lm_server`; C++
sends token histories or text over the socket, and the worker returns BF16
logits or float32 embeddings.
