#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import subprocess
import pytest
import sys
import os
import resource
from pathlib import Path
import os

test_dir = Path(__file__).parent
weights_dir = Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv"))


def generate_test_params():
    prompt_lengths = [
        1024,  # 13
    ]
    num_tokens_list = [
        40,
        # 1
    ]

    params = []
    names = []
    for prompt_len in prompt_lengths:
        for num_tokens in num_tokens_list:
            params.append((prompt_len, num_tokens))
            names.append(f"llama_3.2_1b_prompt_{prompt_len}_tokens_{num_tokens}")
    return params, names


params, names = generate_test_params()


@pytest.mark.metrics(
    TTFT=r"\[Prefill\]\s*Time to first token:\s*(?P<value>[\d\.e\+-]+) s",
    TPS=r"\[Decode\]\s*Tokens per second: (?P<value>[\d\.e\+-]+)",
)
@pytest.mark.parametrize("prompt_len,num_tokens", params, ids=names)
def test_llama_3_2_1b(prompt_len, num_tokens):
    # Print debug info about resource limits
    print("\n=== Debug: Resource Limits ===")
    print(f"TTY stdin: {os.isatty(0)}, stdout: {os.isatty(1)}, stderr: {os.isatty(2)}")
    try:
        stack_soft, stack_hard = resource.getrlimit(resource.RLIMIT_STACK)
        print(f"Stack limit: soft={stack_soft}, hard={stack_hard}")
        as_soft, as_hard = resource.getrlimit(resource.RLIMIT_AS)
        print(f"Address space limit: soft={as_soft}, hard={as_hard}")
    except Exception as e:
        print(f"Error getting limits: {e}")
    print("=" * 40)

    command = f"python3 {test_dir}/llama_npu.py {weights_dir}/llama3.2-1b/model.safetensors {weights_dir}/llama3.2-1b/tokenizer.model --num-tokens {num_tokens} --prompt-len {prompt_len}"

    result = subprocess.run(
        command,
        cwd=test_dir,
        shell=True,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)

    assert (
        result.returncode == 0
    ), f"Command failed with return code {result.returncode}\nStderr: {result.stderr}"
