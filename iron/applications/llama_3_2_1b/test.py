#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import re
import subprocess
import pytest
import os
import sys
from pathlib import Path

from iron.common.harness import record_metric

repo_root = Path(__file__).resolve().parents[3]
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
    not os.environ.get("CI")
    and not (
        (weights_dir / "llama3.2-1b" / "model.safetensors").exists()
        and (weights_dir / "llama3.2-1b" / "tokenizer.model").exists()
    ),
    reason="llama3.2-1b weights not found outside CI",
)


def run_llama_npu(prompt_len, num_tokens, *extra_args, figures):
    """Run the application to completion; record each of ``figures`` it prints."""
    # As a module, so the package's relative imports resolve and nothing
    # needs the repository on sys.path.
    command = [
        sys.executable,
        "-m",
        "iron.applications.llama_3_2_1b.npu",
        str(weights_dir / "llama3.2-1b" / "model.safetensors"),
        str(weights_dir / "llama3.2-1b" / "tokenizer.model"),
        "--num-tokens",
        str(num_tokens),
        "--prompt-len",
        str(prompt_len),
        *extra_args,
    ]
    result = subprocess.run(command, cwd=repo_root, capture_output=True, text=True)

    print(result.stdout)
    print(result.stderr)
    # The harness prints its timings to stderr and the checks to stdout.
    for name, pattern in figures.items():
        match = re.search(pattern, result.stdout + result.stderr)
        if match:
            record_metric(name, float(match.group("value")))

    assert (
        result.returncode == 0
    ), f"Command failed with return code {result.returncode}\nStderr: {result.stderr}"
    return result


PERFORMANCE = {
    "TTFT": r"\[Prefill\]\s*Time to first token:\s*(?P<value>[\d\.e\+-]+) s",
    "TPS": r"\[Decode\]\s*Tokens per second:\s*(?P<value>[\d\.e\+-]+)",
}


@requires_weights
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("prompt_len,num_tokens", params, ids=names)
def test_llama_3_2_1b(prompt_len, num_tokens):
    run_llama_npu(prompt_len, num_tokens, figures=PERFORMANCE)


# KL(fp32 CPU || NPU) of the next-token distribution, teacher-forced over 40
# steps. The graphs measure 0.026 on prefill and at most 0.015 on decode; the
# llama_npu.py they replaced, on the same toolchain, 0.074 and 0.013. Decode
# attention over unmasked KV-cache slots measured 9.2.
MAX_PREFILL_KL = 0.1
MAX_DECODE_KL = 0.05

ACCURACY = {
    "PrefillKL": r"\[Accuracy\] Prefill KL:\s*(?P<value>[\d\.e\+-]+)",
    "DecodeMaxKL": r"\[Accuracy\] Decode max KL:\s*(?P<value>[\d\.e\+-]+)",
    "Top1Mismatches": r"\[Accuracy\] Top-1 mismatches:\s*(?P<value>\d+)",
}


@requires_weights
@pytest.mark.supported_devices("npu2")
def test_llama_3_2_1b_accuracy():
    result = run_llama_npu(1024, 40, "--check-accuracy", figures=ACCURACY)

    prefill_kl = float(re.search(r"Prefill KL:\s*(\S+)", result.stdout).group(1))
    decode_kl = float(re.search(r"Decode max KL:\s*(\S+)", result.stdout).group(1))
    assert prefill_kl <= MAX_PREFILL_KL, f"prefill KL {prefill_kl} > {MAX_PREFILL_KL}"
    assert decode_kl <= MAX_DECODE_KL, f"decode KL {decode_kl} > {MAX_DECODE_KL}"


# Repeated runs must produce bit-identical logits. A prefill KV hand-off that
# was never flushed to the device made 12% of runs diverge. Alternating
# two prompts makes such a missing flush fail every run: 38/38 in each of three
# trials.
DETERMINISM = {
    "DifferingRuns": r"\[Determinism\] Differing runs:\s*(?P<value>\d+)/",
}


@requires_weights
@pytest.mark.supported_devices("npu2")
def test_llama_3_2_1b_determinism():
    result = run_llama_npu(1024, 4, "--check-determinism", "5", figures=DETERMINISM)

    differing = re.search(r"Differing runs:\s*(\d+)/(\d+)", result.stdout)
    assert int(differing.group(1)) == 0, f"{differing.group(0)} (bitwise logits)"
