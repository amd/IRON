# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Tests the focused FastFlowLM GEMM and dequant replacement."""

import contextlib
import json
import os
import re
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest

EXAMPLE = Path(__file__).parent
APP = EXAMPLE.parent
BUILD = APP / "build"
OUTPUT = BUILD / "gemm_dequant"
FLM_ROOT = BUILD / "FastFlowLM"
FLM = FLM_ROOT / "src"
FLM_COMMIT = "95f455e7ca39a2088b8a457dc44af10ecb3c2b40"
FLM_MODEL_PATH = Path(
    os.environ.get(
        "FLM_MODEL_PATH",
        Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / "fastflowlm",
    )
)
MODEL = FLM_MODEL_PATH / "models" / "Gemma4-E2B-IT-NPU2"
PORT = 18099
URL = f"http://127.0.0.1:{PORT}"

OVERRIDDEN = {
    "engine_init",
    "prefill_layer_begin",
    "dequant_qkv",
    "dequant_o",
    "dequant_up",
    "dequant_gate",
    "dequant_down",
    "q_swa_proj",
    "q_global_proj",
    "k_swa_proj",
    "k_global_proj",
    "v_swa_proj",
    "v_global_proj",
    "o_swa_proj",
    "o_global_proj",
    "gate_proj",
    "up_proj",
    "down_proj",
}


def run(command, **kwargs):
    subprocess.run(command, check=True, **kwargs)


def test_example_overrides_only_gemm_and_dequant():
    header = (APP / "gemm_dequant_overrides.hpp").read_text()
    overrides = set(re.findall(r"^#define FLM_OV_(\w+)", header, re.MULTILINE))
    markers = set(re.findall(r"^#define FLM_HAS_OVERRIDE_(\w+)", header, re.MULTILINE))
    assert overrides == OVERRIDDEN
    assert markers == OVERRIDDEN

    build_source = (APP / "build_gemm_dequant.py").read_text()
    assert "from iron.operators.flm import GEMM, DequantBFP" in build_source
    for operator in ("DecodeLayer", "LMHead", "PrefillAttention"):
        assert operator not in build_source


def checkout_fastflowlm():
    if not FLM_ROOT.exists():
        run(["git", "clone", "https://github.com/ROCm/FastFlowLM", str(FLM_ROOT)])
    run(["git", "-C", str(FLM_ROOT), "checkout", FLM_COMMIT])
    run(["git", "-C", str(FLM_ROOT), "submodule", "update", "--init", "--recursive"])


def configure(directory, override=False):
    command = [
        "cmake",
        "-S",
        str(FLM),
        "-B",
        str(directory),
        "-G",
        "Ninja",
        "-DFLM_VERSION=1.0.5",
        "-DNPU_VERSION=32.0.203.304",
        "-DFLM_BUILD_GEMMA4E=ON",
    ]
    if override:
        flags = f'-I{APP} -DFLM_OVERRIDES="\\"gemm_dequant_overrides.hpp\\""'
        command.append(f"-DFLM_OVERRIDE_FLAGS={flags}")
    run(command)


@pytest.fixture(scope="module")
def build_engines():
    checkout_fastflowlm()
    configure(BUILD / "stock")
    run(["cmake", "--build", str(BUILD / "stock"), "--parallel", "2"])
    run(
        [
            sys.executable,
            str(APP / "build_gemm_dequant.py"),
            str(FLM / "xclbins"),
            str(OUTPUT),
        ],
        env=dict(os.environ, FLM_MODEL_PATH=str(FLM_MODEL_PATH)),
    )
    configure(OUTPUT / "engine", override=True)
    run(
        [
            "cmake",
            "--build",
            str(OUTPUT / "engine"),
            "--target",
            "gemma4e_npu",
            "--parallel",
            "2",
        ]
    )


def post(path, body):
    request = urllib.request.Request(URL + path, data=json.dumps(body).encode())
    return json.loads(urllib.request.urlopen(request, timeout=900).read())


@contextlib.contextmanager
def serve(engine, xclbins):
    env = dict(
        os.environ,
        FLM_MODEL_PATH=str(FLM_MODEL_PATH),
        FLM_XCLBIN_PATH=str(xclbins),
        LD_LIBRARY_PATH=f"{engine}:{os.environ.get('LD_LIBRARY_PATH', '')}",
    )
    server = subprocess.Popen(
        [
            str(BUILD / "stock" / "flm"),
            "serve",
            "gemma4-it:e2b",
            "--prefill-chunk-len",
            "512",
            "--port",
            str(PORT),
        ],
        cwd=FLM,
        env=env,
        start_new_session=True,
    )
    try:
        for _ in range(120):
            with contextlib.suppress(OSError):
                urllib.request.urlopen(URL + "/api/version")
                break
            time.sleep(1)
        else:
            raise RuntimeError("FastFlowLM server did not start")
        yield
    finally:
        os.killpg(server.pid, signal.SIGTERM)
        server.wait()


def generate(engine, xclbins):
    with serve(engine, xclbins):
        post(
            "/api/chat",
            {
                "model": "gemma4-it:e2b",
                "stream": False,
                "temperature": 0,
                "top_k": 1,
                "messages": [{"role": "user", "content": "Hi"}],
                "options": {"num_predict": 1},
            },
        )
        return post(
            "/api/generate",
            {
                "model": "gemma4-it:e2b",
                "stream": False,
                "prompt": "Explain block floating point in two sentences.",
                "max_tokens": 64,
            },
        )


@pytest.mark.supported_devices("npu2")
@pytest.mark.skipif(
    not MODEL.exists(), reason="needs $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2"
)
@pytest.mark.metrics(TTFT=r"\[Prefill\] Time to first token: (?P<value>[\d\.e\+-]+) s")
@pytest.mark.bench
def test_iron_gemm_dequant_matches_fastflowlm(build_engines):
    stock = generate(BUILD / "stock" / "engines", FLM)
    iron = generate(OUTPUT / "engine" / "engines", OUTPUT)
    print(f"[Prefill] Time to first token: {iron['prompt_eval_duration'] / 1e9:.4f} s")
    assert iron["context"] == stock["context"]
