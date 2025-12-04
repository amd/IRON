#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import subprocess
import pytest
from pathlib import Path

test_dir = Path(__file__).parent


def generate_test_params():
    prompt_lengths = [64, 2048]
    num_tokens_list = [40]

    params = []
    names = []
    for prompt_len in prompt_lengths:
        for num_tokens in num_tokens_list:
            params.append((prompt_len, num_tokens))
            names.append(f"llama_3.2_1b_prompt_{prompt_len}_tokens_{num_tokens}")
    return params, names


params, names = generate_test_params()


@pytest.mark.metrics(
    TTFT=r"Prefill time: (?P<value>[\d\.e\+-]+) seconds",
    TPS=r"Tokens per second: (?P<value>[\d\.e\+-]+)",
    Num_Tokens=r"Tokens generated: (?P<value>[\d\.e\+-]+)",
)
@pytest.mark.parametrize("prompt_len,num_tokens", params, ids=names)
def test_llama_3_2_1b(prompt_len, num_tokens):
    command = f"python3 {test_dir}/inference.py /srv/llama3.2-1b/model.safetensors /srv/llama3.2-1b/tokenizer.model --prompt_len {prompt_len} --num_tokens {num_tokens}"

    result = subprocess.run(
        command,
        cwd=test_dir,
        shell=True,
        capture_output=True,
        text=True,
        timeout=300,
    )

    assert (
        result.returncode == 0
    ), f"Command failed with return code {result.returncode}\nStderr: {result.stderr}"

    print(result.stdout)
