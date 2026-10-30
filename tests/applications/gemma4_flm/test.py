# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Check the IRON engine against FastFlowLM's own engine, greedy over the same prompts.

The same tokens up to their first difference, and there IRON's token at
least as likely as the stock engine's under Gemma 4 in float32 (Hugging
Face's, its logits recorded in the checkpoint's golden.npz), the
reference every model is judged by. After it the two continue from
different tokens and are not compared.

    FLM_MODEL_PATH=<dir> pytest tests/applications/gemma4_flm

The tests run `make engine` first, which builds everything. Each prompt
reports the IRON engine's time to first token and decode rate.
"""

import contextlib
import json
import os
import signal
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
import pytest

from iron.applications.gemma4 import Gemma4
from iron.lm.testing import require, weights_dir
from iron.operators import flm

APP = Path(flm.__file__).with_name("gemma4_engine")
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
    """Run `flm serve` with the engine library in `engine` and the xclbins under `xclbins`."""
    env = dict(
        os.environ, LD_LIBRARY_PATH=f"{engine}:{os.environ.get('LD_LIBRARY_PATH', '')}"
    )
    env["FLM_XCLBIN_PATH"] = str(xclbins)
    env["FLM_MODEL_PATH"] = str(FLM_MODEL_PATH)
    server = subprocess.Popen(
        [
            str(APP / "build" / "stock" / "flm"),
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


def chat(prompt, *, backend=None, max_tokens=128):
    request = {
        "model": "gemma4-it:e2b",
        "stream": False,
        "temperature": 0,
        "top_k": 1,
        "messages": [{"role": "user", "content": prompt}],
        "options": {"num_predict": max_tokens},
    }
    if backend is not None:
        request["backend"] = backend
    return post("/api/chat", request)


def configure_greedy():
    # /api/generate ignores sampling options. /api/chat sets them for the
    # requests that follow.
    chat("Hi", max_tokens=1)


def generate(prompt, *, backend=None, max_tokens=128):
    request = {
        "model": "gemma4-it:e2b",
        "stream": False,
        "prompt": prompt,
        "max_tokens": max_tokens,
    }
    if backend is not None:
        request["backend"] = backend
    return post("/api/generate", request)


def replies(engine, xclbins, prompts):
    """Return the /api/generate responses to prompts, greedy."""
    with serve(engine, xclbins):
        configure_greedy()
        return [generate(prompt) for prompt in prompts]


@pytest.fixture(scope="module")
def build_engines():
    """Build the stock engine and the IRON engine."""
    require(MODEL / "model.q4nx")
    subprocess.run(
        ["make", "engine", f"PYTHON={sys.executable}"],
        cwd=APP,
        env=dict(os.environ, FLM_MODEL_PATH=str(FLM_MODEL_PATH)),
        check=True,
    )


@pytest.fixture(scope="module")
def stock_tokens(build_engines):
    """Return the stock engine's token ids per prompt.

    The stock engine is deterministic, so every iteration compares with
    this one run.
    """
    stock = replies(APP / "build" / "stock" / "engines", FLM, PROMPTS.values())
    return {name: r["context"] for name, r in zip(PROMPTS, stock)}


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "prompt", [pytest.param(name, marks=pytest.mark.bench) for name in PROMPTS]
)
def test_iron_matches_engine(prompt, build_engines, stock_tokens, record_property):
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
    record_property("TTFT", ttft)
    record_property("TPS", tps)
    got, stock = reply["context"], stock_tokens[prompt]
    assert len(got) == len(
        stock
    ), f"IRON gave {len(got)} tokens, the stock engine {len(stock)}"
    at = next((i for i, (a, b) in enumerate(zip(got, stock)) if a != b), None)
    if at is not None:
        directory = weights_dir("gemma-4-e2b-it")
        require(directory / "model.safetensors", directory / "config.json")
        oracle = Gemma4.from_checkpoint(directory).cpu_reference()
        logits = np.asarray(oracle.logits(stock[:at]), np.float64)
        p = np.exp(logits - logits.max())
        p /= p.sum()
        record_property("DivergesAt", at)
        assert p[got[at]] >= p[stock[at]], (
            f"at {at} IRON chose {got[at]} (p {p[got[at]]:.4f} in float32), "
            f"the stock engine {stock[at]} (p {p[stock[at]]:.4f})"
        )


@pytest.mark.extensive
@pytest.mark.supported_devices("npu2")
def test_iron_engine_reload_rebuilds_override_state(build_engines):
    prompt = "Reply with only the word hello."
    with serve(APP / "build" / "engine" / "engines", APP / "build"):
        before = chat(prompt, max_tokens=8)
        # The server initially lets the model catalog select the "flm" backend.
        # Naming that backend explicitly changes the request selector, forcing
        # the same model and override DLL to unload and reload in this process.
        after = chat(prompt, backend="flm", max_tokens=8)
    assert after["message"]["content"] == before["message"]["content"]
