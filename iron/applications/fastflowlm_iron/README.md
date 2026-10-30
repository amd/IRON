<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON models in FastFlowLM

This application serves Llama 3.2 1B and EmbeddingGemma 2 through FastFlowLM's
HTTP API. FastFlowLM runs each model in IRON's persistent Python server over a
pair of standard input and output pipes. The server compiles the graph versions
through the MLIR-AIE cache on first use, then loads the images and weights.
The Llama entry uses Meta's base checkpoint, intended for text continuation.

The Makefile pins the FastFlowLM fork to
[`ea31ca5a`](https://github.com/andrej/FastFlowLM/commit/ea31ca5a6f8738e691e5f323a0c99f01e676f0d8),
which contains the IRON backend and its BF16 Llama and EmbeddingGemma 2 model
entries.

> [Changes to FastFlowLM to add the IRON backend and EmbeddingGemma 2 model](https://github.com/ROCm/FastFlowLM/compare/3b72cd0535ffa82389797491e15e117497cc9f88...andrej:FastFlowLM:iron-backend)

## Prerequisites

Use an NPU2 machine with XRT and the IRON environment installed as described in
the [repository setup](../../../README.md#installation-linux). FastFlowLM also
needs CMake, Ninja, a C++20 compiler, its documented Linux development packages,
and its `tokenizers-cpp` submodule. The Makefile initializes the submodule.

The `pull` target downloads these IRON checkpoint directories:

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

3. Accept the license for `meta-llama/Llama-3.2-1B`, then provide a Hugging Face
   token through `HF_TOKEN`, `HUGGING_FACE_HUB_TOKEN` or `HF_TOKEN_PATH`. Pull
   the BF16 Llama and EmbeddingGemma 2 checkpoints used by IRON.

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
          -d '{"model":"llama3.2-iron:1b","messages":[{"role":"user","content":"What is 347 + 589?"}],"max_tokens":32}' \
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
[Llama guide](../llama/README.md) and
[EmbeddingGemma 2 guide](../embedding_gemma2/README.md) run the same graph
classes in the command's Python process. They do not use the FastFlowLM worker.
The Makefile's server targets instead start `python -m iron.lm_server`; C++
sends token histories or text through pipes, and the worker returns BF16
logits or float32 embeddings.

## Adding a model

Add the model's lazy import to `MODELS` in `iron/applications/__init__.py`.
The server uses the standard `load`, `logits` (whole token history), `forget`
and `embed` methods; model computation stays in IRON.

In FastFlowLM, a decoder registers `flm::iron::causal_factory("<registry-name>")`
with `causal_traits()` for its frontend's family, following
`common/models/llama3/iron/` and `common/AutoModel/builtin_backends.cpp`.
An embedding model uses `flm::iron::Embedding` in
`include/AutoEmbeddingModel/all_embedding_model.hpp`. Add its checkpoint files
to `model_list.json` and `model_info.json`, using an `-iron` family suffix for
a decoder. These adapters share the C++ pipe client; no Python model code is
needed in FastFlowLM.
