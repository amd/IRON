# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One chat request through FastFlowLM, its pipe client and the IRON server."""

import contextlib
import json
import os
import signal
import socket
import subprocess
import sys
import time
import urllib.request
from pathlib import Path

import pytest

from iron import applications
from iron.lm.testing import require, weights_dir

APP = Path(applications.__file__).with_name("fastflowlm_iron")


@pytest.mark.supported_devices("npu2")
def test_chat(tmp_path):
    root = Path(os.environ.get("FLM_MODEL_PATH", weights_dir("fastflowlm")))
    model = root / "models" / "llama3.2-1b-instruct"
    require(
        model / "config.json",
        model / "model.safetensors",
        model / "tokenizer.json",
        model / "tokenizer_config.json",
    )
    env = dict(os.environ, PATH=f"{Path(sys.executable).parent}:{os.environ['PATH']}")
    subprocess.run(["make", "flm"], cwd=APP, env=env, check=True, timeout=1800)

    # Keep FastFlowLM's writable files away from CI's read-only weights mount.
    (tmp_path / "models").mkdir()
    (tmp_path / "models" / model.name).symlink_to(
        model.resolve(), target_is_directory=True
    )
    env["FLM_MODEL_PATH"] = str(tmp_path)
    env["FLM_MODELINFO_PATH"] = str(APP / "build/install/share/flm/model_info.json")
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
                'source "$1" && exec flm serve llama3.2-iron:1b '
                '--ctx-len 2048 --port "$2"',
                "bash",
                str(APP / "build/install/flm_env.sh"),
                str(port),
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
            request = urllib.request.Request(
                url + "/v1/chat/completions",
                headers={"Content-Type": "application/json"},
                data=json.dumps(
                    {
                        "model": "llama3.2-iron:1b",
                        "stream": False,
                        "temperature": 0,
                        "max_tokens": 16,
                        "messages": [
                            {
                                "role": "user",
                                "content": "Name the capital of France in a short sentence.",
                            }
                        ],
                    }
                ).encode(),
            )
            with urllib.request.urlopen(request, timeout=120) as response:
                reply = json.load(response)
            print(reply["choices"][0]["message"]["content"])
            assert "paris" in reply["choices"][0]["message"]["content"].lower()
            assert reply["usage"]["completion_tokens"] > 1
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
