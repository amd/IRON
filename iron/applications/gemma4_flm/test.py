# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Checks that the IRON engine generates the same tokens as FastFlowLM's own engine.

    FLM_MODEL_PATH=<dir> pytest --iterations 1 iron/applications/gemma4_flm

The tests run `make engine` first, which builds everything. Each prompt reports
the IRON engine's time to first token and decode rate.
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

# The long prompt spans three chunks of up to 512 tokens.
NUMBERS = ", ".join(str(i * 37 % 1000) for i in range(250))
PROMPTS = {
    "word_problem": "A bakery makes 120 muffins in the morning. It sells 3/4 of them before noon. "
    "In the afternoon it bakes 45 more muffins and sells 30 of them. How many muffins "
    "does the bakery have left at the end of the day? Show at most three short lines "
    "of working, then give the final answer on its own line as 'Answer: <number>'.",
    "long_prompt": f"The password is 'harbor'. Ignore these numbers: {NUMBERS}. "
    "What is the password? Answer with just the word.",
}


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


def replies(engine, xclbins, prompts):
    """The /api/generate responses to prompts, greedy."""
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
            )
            for prompt in prompts
        ]


@pytest.fixture(scope="module")
def stock_tokens():
    """Builds both engines, then returns the stock engine's token ids per prompt.

    The stock engine is deterministic, so every iteration compares with this
    one run.
    """
    subprocess.run(
        ["make", "engine"],
        cwd=APP,
        env=dict(os.environ, FLM_MODEL_PATH=str(FLM_MODEL_PATH)),
        check=True,
    )
    stock = replies(APP / "build" / "stock" / "engines", FLM, PROMPTS.values())
    return {name: r["context"] for name, r in zip(PROMPTS, stock)}


@pytest.mark.supported_devices("npu2")
@pytest.mark.skipif(
    not MODEL.exists(), reason="needs $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2"
)
@pytest.mark.metrics(
    TTFT=r"\[Prefill\]\s*Time to first token:\s*(?P<value>[\d\.e\+-]+) s",
    TPS=r"\[Decode\]\s*Tokens per second:\s*(?P<value>[\d\.e\+-]+)",
)
@pytest.mark.parametrize(
    "prompt", [pytest.param(name, marks=pytest.mark.bench) for name in PROMPTS]
)
def test_iron_matches_engine(prompt, stock_tokens):
    (reply,) = replies(
        APP / "build" / "engine" / "engines", APP / "build", [PROMPTS[prompt]]
    )
    # flm reports durations in nanoseconds.
    ttft = reply["prompt_eval_duration"] / 1e9
    tps = reply["eval_count"] / (reply["eval_duration"] / 1e9)
    print(f"[Prefill] {reply['prompt_eval_count']} prompt tokens")
    print(f"[Prefill] Time to first token: {ttft:.4f} s")
    print(f"[Decode] {reply['eval_count']} tokens")
    print(f"[Decode] Tokens per second: {tps:.2f}")
    assert reply["context"] == stock_tokens[prompt]
