#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import re
import subprocess
import pytest
import os
import sys
from pathlib import Path

from iron.common.test_utils import record_metric

test_dir = Path(__file__).parent
weights_dir = Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv"))


def generate_test_params():
    prompt_lengths = [1024, 13]
    num_tokens_list = [40, 1]

    params = []
    names = []
    for prompt_len in prompt_lengths:
        for num_tokens in num_tokens_list:
            params.append((prompt_len, num_tokens))
            names.append(f"llama_3.2_1b_prompt_{prompt_len}_tokens_{num_tokens}")
    return params, names


params, names = generate_test_params()


FIGURES = {
    "TTFT": r"\[Prefill\]\s*Time to first token:\s*(?P<value>[\d\.e\+-]+) s",
    "TPS": r"\[Decode\]\s*Tokens per second:\s*(?P<value>[\d\.e\+-]+)",
}


@pytest.mark.skipif(
    not (
        (weights_dir / "llama3.2-1b" / "model.safetensors").exists()
        and (weights_dir / "llama3.2-1b" / "tokenizer.model").exists()
    ),
    reason="llama3.2-1b weights not found",
)
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("prompt_len,num_tokens", params, ids=names)
def test_llama_3_2_1b(prompt_len, num_tokens):
    command = f"{sys.executable} {test_dir}/llama_npu.py {weights_dir}/llama3.2-1b/model.safetensors {weights_dir}/llama3.2-1b/tokenizer.model --num-tokens {num_tokens} --prompt-len {prompt_len}"

    result = subprocess.run(
        command,
        cwd=test_dir,
        shell=True,
        capture_output=True,
        text=True,
    )

    print(result.stdout)
    print(result.stderr)
    # The figures the application prints, for the CSV.
    for name, pattern in FIGURES.items():
        match = re.search(pattern, result.stdout)
        if match:
            record_metric(name, float(match.group("value")))

    assert result.returncode == 0, (
        f"Command failed with return code {result.returncode}\nStderr: {result.stderr}"
    )
