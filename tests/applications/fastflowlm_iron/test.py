# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Exercise chat and embeddings through the installed FastFlowLM IRON plugin."""

import contextlib
import json
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

import numpy as np
import pytest

from iron import applications
from iron.lm.testing import require, weights_dir

APP = Path(applications.__file__).with_name("fastflowlm_iron")


@pytest.fixture(scope="module")
def installation():
    # An explicit build permits testing a freshly built local FLM/plugin pair.
    if build := os.environ.get("FLM_TEST_BUILD"):
        return Path(build)
    env = dict(os.environ, PATH=f"{Path(sys.executable).parent}:{os.environ['PATH']}")
    subprocess.run(["make", "flm"], cwd=APP, env=env, check=True, timeout=1800)
    return APP / "build"


def post(url, path, body):
    request = urllib.request.Request(
        url + path,
        headers={"Content-Type": "application/json"},
        data=json.dumps(body).encode(),
    )
    with urllib.request.urlopen(request, timeout=180) as response:
        return json.load(response)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize(
    "tag,name",
    [
        ("llama3.2-iron:1b", "llama3.2-1b-instruct"),
        ("embeddinggemma-2:740m", "embeddinggemma-2"),
    ],
)
def test_model(tmp_path, installation, tag, name):
    root = Path(os.environ.get("FLM_MODEL_PATH", weights_dir("fastflowlm")))
    model = root / "models" / name
    require(
        *(
            model / f
            for f in (
                "config.json",
                "model.safetensors",
                "tokenizer.json",
                "tokenizer_config.json",
            )
        )
    )
    env = dict(os.environ, PATH=f"{Path(sys.executable).parent}:{os.environ['PATH']}")
    # Keep FastFlowLM's writable files away from CI's read-only weights mount.
    (tmp_path / "models").mkdir()
    (tmp_path / "models" / model.name).symlink_to(
        model.resolve(), target_is_directory=True
    )
    env["FLM_MODEL_PATH"] = str(tmp_path)
    env["FLM_MODELINFO_PATH"] = str(installation / "install/share/flm/model_info.json")
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    url = f"http://127.0.0.1:{port}"
    log = tmp_path / "server.log"
    with log.open("w") as output:
        server = subprocess.Popen(
            [
                "bash",
                "-c",
                'source "$1" && exec flm serve "$3" '
                '--ctx-len 2048 --port "$2" --model-extension "$4"',
                "bash",
                str(installation / "install/flm_env.sh"),
                str(port),
                "Ollama/" + tag,
                str(installation / "plugin/extension.json"),
            ],
            env=env,
            stdout=output,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            deadline = time.monotonic() + 900
            while True:
                assert server.poll() is None, "FastFlowLM exited during startup"
                try:
                    with urllib.request.urlopen(url + "/api/version", timeout=2):
                        break
                except OSError:
                    assert time.monotonic() < deadline, "FastFlowLM startup timed out"
                    time.sleep(1)
            if name == "embeddinggemma-2":
                texts = [
                    "The capital of France is Paris.",
                    "A dog is playing in the park.",
                ]
                result = post(url, "/v1/embeddings", {"model": tag, "input": texts})
                vectors = np.asarray([r["embedding"] for r in result["data"]])
                assert vectors.shape == (2, 768)
                assert np.isfinite(vectors).all()
                np.testing.assert_allclose(
                    np.linalg.norm(vectors, axis=1), 1, atol=0.02
                )
                assert np.dot(*vectors) < 0.99
                for invalid in ("does-not-exist:1", "llama3.2-iron:1b"):
                    with pytest.raises(urllib.error.HTTPError) as error:
                        post(
                            url, "/v1/embeddings", {"model": invalid, "input": texts[0]}
                        )
                    with error.value as response:
                        assert response.code == 400
                        assert json.load(response)["error"]["message"]
                with pytest.raises(urllib.error.HTTPError) as error:
                    post(
                        url,
                        "/v1/embeddings",
                        {"model": tag, "input": texts[0], "task": "unknown"},
                    )
                with error.value as response:
                    assert response.code == 400
                    assert (
                        "Unsupported EmbeddingGemma task"
                        in json.load(response)["error"]["message"]
                    )
                again = post(
                    url,
                    "/v1/embeddings",
                    {"model": "Ollama/" + tag, "input": texts[0], "task": "query"},
                )
                np.testing.assert_allclose(
                    again["data"][0]["embedding"], vectors[0], atol=1e-5
                )
                custom = post(
                    url,
                    "/v1/embeddings",
                    {"model": tag, "input": texts[0], "task": "QuestionAnswering"},
                )["data"][0]["embedding"]
                assert len(custom) == 768
                np.testing.assert_allclose(np.linalg.norm(custom), 1, atol=0.02)
                short = post(
                    url,
                    "/v1/embeddings",
                    {
                        "model": tag,
                        "input": texts[0],
                        "dimensions": 128,
                    },
                )
                expected = vectors[0, :128] / np.linalg.norm(vectors[0, :128])
                np.testing.assert_allclose(
                    short["data"][0]["embedding"], expected, atol=0.01
                )
                print(
                    "EmbeddingGemma-2: normalized, deterministic 768/128-dimensional embeddings"
                )
            else:
                messages = [
                    {
                        "role": "user",
                        "content": "Name the capital of France in a short sentence.",
                    }
                ]
                body = {
                    "model": tag,
                    "stream": False,
                    "temperature": 0,
                    "max_tokens": 16,
                    "messages": messages,
                }
                reply = post(url, "/v1/chat/completions", body)
                answer = reply["choices"][0]["message"]["content"]
                print(answer)
                assert "paris" in answer.lower()
                assert reply["usage"]["completion_tokens"] > 1
                messages.extend(
                    [
                        {"role": "assistant", "content": answer},
                        {"role": "user", "content": "Which country is that city in?"},
                    ]
                )
                reply = post(url, "/v1/chat/completions", body)
                answer = reply["choices"][0]["message"]["content"]
                print(answer)
                assert "france" in answer.lower()
        except BaseException:
            print(log.read_text())
            raise
        finally:
            with contextlib.suppress(ProcessLookupError):
                os.killpg(server.pid, signal.SIGTERM)
            try:
                server.wait(timeout=10)
            except subprocess.TimeoutExpired:
                os.killpg(server.pid, signal.SIGKILL)
                server.wait()
