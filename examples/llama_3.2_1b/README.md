<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Golden Model Inference

## Model and Tokenizer Download Instructions

To download the necessary files for the model, please follow the links below:

- **Model File**: [model.safetensors](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- **Tokenizer File**: [tokenizer.model](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original)

Make sure to place these files in the appropriate directory for your project.

## Installation Instructions

Before running `inference.py`, ensure you have the proper environment. To build the environment from scratch, follow the instructions below:

1. Create and activate a Python virtual environment:
     ```bash
     python3 -m venv ironenv
     source ironenv/bin/activate
     python3 -m pip install --upgrade pip
     ```

2. Install prerequisites:
     ```bash
     source ./scripts/install_prereqs.sh --env <name of your virtual env>
     source ./script/env_setup.sh --env <name of your virtual env>
     python3 -m pip install -r requirements_llama.txt
     ```

You can skip passing the `--env` option if you named your virtual environment `ironenv`.

## Running Inference

Inference with Llama-3.2-1B can be run by specifying a number of tokens to generate based on a prompt. This is done with `inference.py`:  
```bash  
cd golden_model
python inference.py model.safetensors tokenizer.model --num_tokens <NUM_TOKENS> --prompt <PROMPT>
```

`inference.py` has the following command format:  
```bash
python inference.py <weights_file_path> <tokenizer_file_path> [--num_tokens NUM_TOKENS] [--prompt PROMPT] [--use_prompt_template] [--save_outputs]
```

### Arguments:
- `weights_file_path`: Path to the weights file (e.g., `model.safetensors`).
- `tokenizer_file_path`: Path to the tokenizer file (e.g., `tokenizer.model`).
- `--num_tokens`: (Optional) Number of tokens to predict. Default is `1`.
- `--prompt`: (Optional) Prompt for the model to generate text from. Default is the text in `prompts.txt`.
- `--use_prompt_template`: (Optional) Use a prompt template for the model. Should be passed in when using Instruct weights.
- `--save_outputs`: (Optional) Enable hooks to save outputs of at each layer of the model.