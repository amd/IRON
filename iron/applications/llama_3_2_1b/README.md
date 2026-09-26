<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Golden Model Inference

## Model and Tokenizer Download Instructions

To download the necessary files for the model, please follow the links below:

- **Model File**: [model.safetensors](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main)
- **Tokenizer File**: [tokenizer.model](https://huggingface.co/meta-llama/Llama-3.2-1B/tree/main/original)

The CI tests expect these files to be placed in the directory `/srv/llama3.2-1b`;
when calling `inference.py`, you will supply the paths to those two files on the command line, so you can place them anywhere.

## Installation Instructions

Before running `inference.py`, ensure you have the proper environment. To build the environment from scratch, follow the instructions below:

1. Follow the IRON installation instructions in the repository root fist.
   After this, you should have an `ironenv` environment set up and activated.

2. Install the following additional requirements:
   ```
   python3 -m pip install -r requirements_examples.txt
   ```

## Running Inference

Inference with Llama-3.2-1B can be run by specifying a number of tokens to generate based on a prompt. This is done with `inference.py`:  
```bash  
cd golden_model
python inference.py /path/to/model.safetensors /path/to/tokenizer.model --num_tokens <NUM_TOKENS> --prompt <PROMPT>
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