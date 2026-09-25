#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import subprocess
import pytest
import os
import re
import sys
from pathlib import Path

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

requires_weights = pytest.mark.skipif(
    not (
        (weights_dir / "llama3.2-1b" / "model.safetensors").exists()
        and (weights_dir / "llama3.2-1b" / "tokenizer.model").exists()
    ),
    reason="llama3.2-1b weights not found",
)


def run_llama_npu(prompt_len, num_tokens, *extra_args):
    command = [
        sys.executable,
        str(test_dir / "llama_npu.py"),
        str(weights_dir / "llama3.2-1b" / "model.safetensors"),
        str(weights_dir / "llama3.2-1b" / "tokenizer.model"),
        "--num-tokens",
        str(num_tokens),
        "--prompt-len",
        str(prompt_len),
        *extra_args,
    ]
    result = subprocess.run(command, cwd=test_dir, capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)

    assert (
        result.returncode == 0
    ), f"Command failed with return code {result.returncode}\nStderr: {result.stderr}"
    return result


@requires_weights
@pytest.mark.supported_devices("npu2")
@pytest.mark.metrics(
    TTFT=r"\[Prefill\]\s*Time to first token:\s*(?P<value>[\d\.e\+-]+) s",
    TPS=r"\[Decode\]\s*Tokens per second:\s*(?P<value>[\d\.e\+-]+)",
)
@pytest.mark.parametrize("prompt_len,num_tokens", params, ids=names)
def test_llama_3_2_1b(prompt_len, num_tokens):
    run_llama_npu(prompt_len, num_tokens)


# KL(fp32 CPU || NPU) of the next-token distribution, teacher-forced over 40
# steps. The NPU measures 0.074 on prefill and at most 0.013 on decode. Decode
# attention over unmasked KV-cache slots measured 9.2.
MAX_PREFILL_KL = 0.1
MAX_DECODE_KL = 0.05


@requires_weights
@pytest.mark.supported_devices("npu2")
@pytest.mark.metrics(
    PrefillKL=r"\[Accuracy\] Prefill KL:\s*(?P<value>[\d\.e\+-]+)",
    DecodeMaxKL=r"\[Accuracy\] Decode max KL:\s*(?P<value>[\d\.e\+-]+)",
    Top1Mismatches=r"\[Accuracy\] Top-1 mismatches:\s*(?P<value>\d+)",
)
def test_llama_3_2_1b_accuracy():
    result = run_llama_npu(1024, 40, "--check-accuracy")

    prefill_kl = float(re.search(r"Prefill KL:\s*(\S+)", result.stdout).group(1))
    decode_kl = float(re.search(r"Decode max KL:\s*(\S+)", result.stdout).group(1))
    assert prefill_kl <= MAX_PREFILL_KL, f"prefill KL {prefill_kl} > {MAX_PREFILL_KL}"
    assert decode_kl <= MAX_DECODE_KL, f"decode KL {decode_kl} > {MAX_DECODE_KL}"


# Repeated runs must produce bit-identical logits. A prefill KV hand-off that
# was never flushed to the device made 12% of runs diverge. Alternating
# two prompts makes such a missing flush fail every run: 38/38 in each of three
# trials.
@requires_weights
@pytest.mark.supported_devices("npu2")
@pytest.mark.metrics(
    DifferingRuns=r"\[Determinism\] Differing runs:\s*(?P<value>\d+)/",
)
def test_llama_3_2_1b_determinism():
    result = run_llama_npu(1024, 4, "--check-determinism", "5")

    differing = re.search(r"Differing runs:\s*(\d+)/(\d+)", result.stdout)
    assert int(differing.group(1)) == 0, f"{differing.group(0)} (bitwise logits)"
