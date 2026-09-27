<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Llama 3.2 1B on the NPU

Prefill and decode of Llama 3.2 1B as one IRON graph function, compiled to
one image per input shape (`npu.py`) and run from a numpy host loop
(`runner.py`). The weights are the safetensors checkpoint mapped into numpy
(`weights.py`), and the accuracy check compares the NPU's logits with a
float32 numpy forward pass (`cpu.py`); nothing here needs torch.

## Weights and tokenizer

From Hugging Face:

- [`model.safetensors`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- [`tokenizer.model`](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original)

The tests look for them in `$IRON_EXAMPLE_WEIGHTS_DIR/llama3.2-1b/`
(`IRON_EXAMPLE_WEIGHTS_DIR` defaults to `/srv`); on the command line they
can be anywhere.

## Setup

Set up IRON as the repository root describes, then:

```bash
python3 -m pip install -r requirements_examples.txt
```

## Running

From the repository root:

```bash
python -m iron.applications.llama_3_2_1b.runner \
    /path/to/model.safetensors /path/to/tokenizer.model \
    --prompt-len 2048 --num-tokens 40
```

- `--prompt-len`: characters of `prompt.txt` to use as the prompt (default 2048)
- `--num-tokens`: tokens to generate (default 40)
- `--check-accuracy`: instead of sampling, compare each step's logits with a
  float32 numpy forward pass (`cpu.Reference`) and print the KL divergence
  and top-1 agreement
- `--check-determinism ROUNDS`: instead of sampling, run two prompts
  `ROUNDS` times each and count the runs whose logits differ bitwise

`pytest iron/applications/llama_3_2_1b/` runs all three and records the
throughput and accuracy figures.
