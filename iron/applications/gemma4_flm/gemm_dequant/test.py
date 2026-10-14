# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Tests the focused FastFlowLM GEMM and dequant replacement."""

import contextlib
import json
import os
import re
import signal
import statistics
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import numpy as np
import pytest

from iron.applications.gemma4_flm import dequantize

EXAMPLE = Path(__file__).parent
APP = EXAMPLE.parent
BUILD = APP / "build"
OUTPUT = BUILD / "gemm_dequant"
FLM_ROOT = BUILD / "FastFlowLM"
FLM = FLM_ROOT / "src"
FLM_TAG = "v1.0.8"
SOURCE_FLM_MODEL_PATH = Path(
    os.environ.get(
        "FLM_MODEL_PATH",
        Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv")) / "fastflowlm",
    )
)
SOURCE_MODEL = SOURCE_FLM_MODEL_PATH / "models" / "Gemma4-E2B-IT-NPU2"
FLM_MODEL_PATH = OUTPUT / "weights"
MODEL = FLM_MODEL_PATH / "models" / SOURCE_MODEL.name
SIDECARS = {"model.dq_bf16", "model.dq_bfp", "model.dq_bfp_attn"}
PORT = 18099
URL = f"http://127.0.0.1:{PORT}"
MEASURED_RUNS = 12
PROMPT_TOKENS = 261
PROMPT = """Alice's Adventures in Wonderland ALICE'S ADVENTURES IN WONDERLAND Lewis Carroll
THE MILLENNIUM FULCRUM EDITION 3.0 CHAPTER I Down the Rabbit-Hole Alice was
beginning to get very tired of sitting by her sister on the bank, and of having
nothing to do: once or twice she had peeped into the book her sister was
reading, but it had no pictures or conversations in it, `and what is the use of
a book,' thought Alice `without pictures or conversation?' So she was
considering in her own mind (as well as she could, for the hot day made her feel
very sleepy and stupid), whether the pleasure of making a daisy-chain would be
worth the trouble of getting up and picking the daisies, when suddenly a White
Rabbit with pink eyes ran close by her. There was nothing so VERY remarkable in
that; nor did Alice think it so VERY much out of the way to hear the Rabbit say
to itself, `Oh dear! Oh dear! I shall be late!' (when she thought it over
afterwards, it occurred to her that she ought to have wondered at this, but at
the time it all seemed quite"""

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


def test_offline_dequant_uses_floor_rounding():
    values = np.array([1.0, 1.00390625, -1.0, -1.00390625], dtype=np.float32)
    expected = np.array([0x3F80, 0x3F80, 0xBF80, 0xBF81], dtype=np.uint16)
    np.testing.assert_array_equal(dequantize.f32_to_bf16_floor(values), expected)


def test_offline_dequant_layout_is_a_permutation():
    k_dim, n_dim = 512, 128
    kk, nn = np.meshgrid(np.arange(k_dim), np.arange(n_dim), indexing="ij")
    offsets = dequantize.dequant_offset(kk, nn, k_dim)
    np.testing.assert_array_equal(np.sort(offsets, axis=None), np.arange(k_dim * n_dim))


def test_offline_dequant_writes_a_sidecar(tmp_path):
    first = np.array([1, 2, 3, 4], dtype=np.uint8)
    second = np.array([5, 6], dtype=np.uint8)
    plan = [
        ("first", first.nbytes, "U8", lambda: first),
        ("second", second.nbytes, "U8", lambda: second),
    ]
    output = tmp_path / "weights"
    assert list(dequantize.write_container(output, plan, {"mode": "test"})) == [
        "first",
        "second",
    ]

    header, data_start = dequantize.read_header(output)
    assert header["first"]["data_offsets"] == [0, 4]
    assert header["second"]["data_offsets"] == [4, 6]
    assert header["__metadata__"] == {"mode": "test"}
    assert output.read_bytes()[data_start:] == b"\x01\x02\x03\x04\x05\x06"


def test_plot_contains_all_selections(tmp_path):
    output = tmp_path / "prefill.png"
    run(
        [sys.executable, str(APP / "plot_prefill.py")],
        input=(
            "stock: mean 1000\n"
            "bf16: mean 800\n"
            "dequant: mean 900\n"
            "bfp16: mean 700\n"
        ),
        text=True,
        env=dict(os.environ, IRON_PLOT=str(output)),
    )
    assert output.read_bytes().startswith(b"\x89PNG\r\n\x1a\n")


def checkout_fastflowlm():
    if not FLM_ROOT.exists():
        run(["git", "clone", "https://github.com/ROCm/FastFlowLM", str(FLM_ROOT)])
    run(["git", "-C", str(FLM_ROOT), "checkout", FLM_TAG])
    run(["git", "-C", str(FLM_ROOT), "submodule", "update", "--init", "--recursive"])


def configure(directory, mode=None):
    command = [
        "cmake",
        "-S",
        str(FLM),
        "-B",
        str(directory),
        "-G",
        "Ninja",
        "-DFLM_VERSION=1.0.8",
        "-DNPU_VERSION=32.0.203.304",
        "-DFLM_BUILD_GEMMA4E=ON",
    ]
    if mode is not None:
        flags = f'-I{APP} -DFLM_OVERRIDES="\\"gemm_dequant_overrides.hpp\\""'
        if mode != "dequant":
            flags += f" -DIRON_OFFLINE_{mode.upper()}"
        command.append(f"-DFLM_OVERRIDE_FLAGS={flags}")
    run(command)


def prepare_model(source_model=SOURCE_MODEL, model=MODEL):
    model.mkdir(parents=True, exist_ok=True)
    for source in source_model.iterdir():
        if source.name in SIDECARS:
            continue
        destination = model / source.name
        if not destination.exists():
            destination.symlink_to(source.resolve())


def test_prepare_model_links_inputs_and_owns_sidecars(tmp_path):
    source_model = tmp_path / "source"
    source_model.mkdir()
    (source_model / "model.q4nx").write_bytes(b"weights")
    (source_model / "model.dq_bf16").write_bytes(b"source sidecar")
    model = tmp_path / "local" / "models" / source_model.name

    prepare_model(source_model, model)

    assert (model / "model.q4nx").is_symlink()
    assert (model / "model.q4nx").read_bytes() == b"weights"
    assert not (model / "model.dq_bf16").exists()
    (model / "model.dq_bf16").write_bytes(b"local sidecar")
    assert (model / "model.dq_bf16").read_bytes() == b"local sidecar"


def build_sidecars():
    commands = {
        "model.dq_bf16": ["--mode", "bf16"],
        "model.dq_bfp": ["--mode", "bfp", "--only", "mlp."],
        "model.dq_bfp_attn": ["--mode", "bfp", "--only", "self_attn."],
    }
    for output, arguments in commands.items():
        output_path = MODEL / output
        if output_path.exists():
            continue
        temporary_path = MODEL / f".{output}.tmp"
        run(
            [
                sys.executable,
                str(APP / "dequantize.py"),
                str(MODEL),
                *arguments,
                "--out",
                temporary_path.name,
            ],
            env=dict(os.environ, IRON_PATH=str(APP.parents[2])),
        )
        temporary_path.replace(output_path)


@pytest.fixture(scope="module")
def build_engines():
    checkout_fastflowlm()
    prepare_model()
    build_sidecars()
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
    for mode in ("dequant", "bf16", "bfp16"):
        directory = OUTPUT / ("engine" if mode == "dequant" else f"engine_{mode}")
        configure(directory, mode=mode)
        run(
            [
                "cmake",
                "--build",
                str(directory),
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


def generate(engine, xclbins, measured_runs=1):
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
        request = {
            "model": "gemma4-it:e2b",
            "stream": False,
            "prompt": PROMPT,
            "max_tokens": 1,
        }
        post("/api/generate", request)
        return [post("/api/generate", request) for _ in range(measured_runs)]


@pytest.mark.supported_devices("npu2")
@pytest.mark.skipif(
    not SOURCE_MODEL.exists(),
    reason="needs $FLM_MODEL_PATH/models/Gemma4-E2B-IT-NPU2",
)
@pytest.mark.metrics(TTFT=r"\[Prefill\] Time to first token: (?P<value>[\d\.e\+-]+) s")
@pytest.mark.bench
def test_all_gemm_dequant_selections(build_engines):
    selections = {
        "stock": (BUILD / "stock" / "engines", FLM),
        "bf16": (OUTPUT / "engine_bf16" / "engines", FLM),
        "dequant": (OUTPUT / "engine" / "engines", OUTPUT),
        "bfp16": (OUTPUT / "engine_bfp16" / "engines", OUTPUT),
    }
    reference = None
    lines = []
    for name, (engine, xclbins) in selections.items():
        responses = generate(engine, xclbins, MEASURED_RUNS)
        assert all(
            response["prompt_eval_count"] == PROMPT_TOKENS for response in responses
        )
        contexts = [response["context"] for response in responses]
        assert all(context == contexts[0] for context in contexts)
        if reference is None:
            reference = contexts[0]
        else:
            assert contexts[0] == reference
        mean_ms = statistics.fmean(
            response["prompt_eval_duration"] / 1e6 for response in responses
        )
        lines.append(f"{name}: mean {mean_ms:.3f}")

    report = "\n".join(lines) + "\n"
    (OUTPUT / "prefill_means.txt").write_text(report)
    print(report, end="")
    iron_mean_ms = float(lines[2].split()[-1])
    print(f"[Prefill] Time to first token: {iron_mean_ms / 1e3:.4f} s")
