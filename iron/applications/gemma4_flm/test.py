# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Checks that the IRON engine generates the same tokens as FastFlowLM's own engine.

    FLM_MODEL_PATH=<dir> pytest --iterations 1 iron/applications/gemma4_flm

The test runs `make engine` first, which builds everything.
"""

import contextlib
import json
import os
import signal
import subprocess
import time
import urllib.request
from pathlib import Path

import pytest

APP = Path(__file__).parent
FLM = APP / "build" / "FastFlowLM" / "src"
# CI keeps the model in /srv/fastflowlm/models/Gemma4-E2B-IT-NPU2.
FLM_MODEL_PATH = Path(
    os.environ.get(
        "FLM_MODEL_PATH",
        Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / "fastflowlm",
    )
)
MODEL = FLM_MODEL_PATH / "models" / "Gemma4-E2B-IT-NPU2"
PORT = 18099
URL = f"http://127.0.0.1:{PORT}"

# The second prompt spans three chunks of up to 512 tokens.
NUMBERS = ", ".join(str(i * 37 % 1000) for i in range(250))
PROMPTS = [
    "A bakery makes 120 muffins in the morning. It sells 3/4 of them before noon. "
    "In the afternoon it bakes 45 more muffins and sells 30 of them. How many muffins "
    "does the bakery have left at the end of the day? Show at most three short lines "
    "of working, then give the final answer on its own line as 'Answer: <number>'.",
    f"The password is 'harbor'. Ignore these numbers: {NUMBERS}. What is the password? "
    "Answer with just the word.",
]


def post(path, body):
    request = urllib.request.Request(URL + path, data=json.dumps(body).encode())
    return json.loads(urllib.request.urlopen(request, timeout=900).read())


@contextlib.contextmanager
def serve(engine, xclbins):
    """Runs `flm serve` with the engine library in `engine` and the xclbins under `xclbins`."""
    env = dict(
        os.environ, LD_LIBRARY_PATH=f"{engine}:{os.environ.get('LD_LIBRARY_PATH', '')}"
    )
    env["FLM_XCLBIN_PATH"] = str(xclbins)
    env["FLM_MODEL_PATH"] = str(FLM_MODEL_PATH)
    server = subprocess.Popen(
        [
            "./build/flm",
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
        yield
    finally:
        os.killpg(server.pid, signal.SIGTERM)
        server.wait()


def tokens(engine, xclbins):
    """The token ids of the greedy replies to PROMPTS."""
    with serve(engine, xclbins):
        # /api/generate ignores sampling options. /api/chat sets them for the
        # requests that follow.
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
        return [
            post(
                "/api/generate",
                {
                    "model": "gemma4-it:e2b",
                    "stream": False,
                    "prompt": prompt,
                    "max_tokens": 128,
                },
            )["context"]
            for prompt in PROMPTS
        ]


@pytest.mark.supported_devices("npu2")
@pytest.mark.skipif(
    not MODEL.exists(), reason="needs $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2"
)
def test_iron_matches_engine():
    subprocess.run(
        ["make", "engine"],
        cwd=APP,
        env=dict(os.environ, FLM_MODEL_PATH=str(FLM_MODEL_PATH)),
        check=True,
    )
    stock = tokens(APP / "build" / "stock" / "engines", FLM)
    iron = tokens(APP / "build" / "engine" / "engines", APP / "build")
    assert iron == stock
