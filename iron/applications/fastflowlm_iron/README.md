<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# IRON models in FastFlowLM

On an NPU2 machine, install [IRON](../../../README.md#installation-linux) and
[the build dependencies](../../../ci/docker-based/Dockerfile)
(the IRON CI container includes them). Run from this directory:

```bash
source /opt/xilinx/xrt/setup.sh
source /path/to/ironenv/bin/activate
make flm
source build/install/flm_env.sh

read -rsp 'Hugging Face token: ' HF_TOKEN; echo
export HF_TOKEN
flm serve llama3.2-iron:1b --ctx-len 2048 --model-extension "$PWD/build/plugin/extension.json"
```

For Llama, first accept the [model license](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
and create a **Read** token in [Hugging Face settings](https://huggingface.co/settings/tokens).
`flm serve` downloads missing weights automatically. IRON reuses compiled
artifacts in `$NPU_CACHE_HOME` (default `~/.npu/cache`).

Replace `llama3.2-iron:1b` with `embeddinggemma-2:740m` to serve embeddings,
or use `flm run` for interactive chat. Models must be registered in both
[IRON](../__init__.py) and the
[plugin catalog](https://github.com/andrej/FastFlowLM/blob/feat/iron-model-extension/extensions/iron/model-list.json).
The plugin reuses FLM's Llama frontend and exchanges tokens/logits or
text/embeddings with the IRON server.

The [integration test](../../../tests/applications/fastflowlm_iron/test.py) checks
Llama chat and EmbeddingGemma-2 through the HTTP API on NPU2. CI needs
`config.json`, `model.safetensors`, `tokenizer.json` and `tokenizer_config.json`
in each of `/srv/fastflowlm/models/llama3.2-1b-instruct/` and
`/srv/fastflowlm/models/embeddinggemma-2/`. Set `FLM_MODEL_PATH` to another directory
containing `models/` to reuse local weights. No token is needed when weights
are already present.
