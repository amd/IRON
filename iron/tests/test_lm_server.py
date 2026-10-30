# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import io
import json
import struct
import subprocess
import sys

import numpy as np
from ml_dtypes import bfloat16

from iron import lm_server
from iron.applications import MODELS, model_class


def request(header, payload=b""):
    data = json.dumps(header).encode()
    return struct.pack("=I", len(data)) + data + payload


def responses(data, word_sizes):
    stream = io.BytesIO(data)
    found = []
    sizes = iter(word_sizes)
    while stream.tell() < len(data):
        size = struct.unpack("=I", stream.read(4))[0]
        found.append(json.loads(stream.read(size)))
        count = found[-1].get("count", 0)
        if count:
            found.append(stream.read(count * next(sizes)))
    return found


def test_registry_contains_graph_models():
    assert set(MODELS) == {
        "embedding_gemma2",
        "embedding_gemma2_multimodal",
        "gemma4",
        "gemma4_multimodal",
        "llama",
    }


def test_registry_resolves_model_class(monkeypatch):
    class Model:
        pass

    monkeypatch.setitem(MODELS, "test", (__name__, "Model"))
    monkeypatch.setattr(sys.modules[__name__], "Model", Model, raising=False)
    assert model_class("test") is Model


def test_load_model_uses_registry(monkeypatch):
    class Model:
        @classmethod
        def load(cls, path, **options):
            return path, options

    monkeypatch.setattr(lm_server, "model_class", lambda name: Model)
    assert lm_server.load_model(
        {
            "model": "test",
            "model_path": "/model",
            "context_length": 128,
        }
    ) == ("/model", {"max_seq_len": 128})
    assert lm_server.load_model({"model": "test", "model_path": "/model"}) == (
        "/model",
        {},
    )


def test_multimodal_dispatch_uses_text_only_inputs():
    class Text:
        def forget(self, position):
            assert position == 0

    class Model:
        text = Text()

        def logits(self, tokens, raw):
            assert raw == {}
            return tokens

    model = Model()
    np.testing.assert_array_equal(lm_server.logits(model, np.asarray([1, 2])), [1, 2])
    lm_server.reset(model)


def test_server_protocol(monkeypatch):
    class Model:
        def logits(self, tokens):
            return np.asarray([tokens[-1], len(tokens)], dtype=bfloat16)

        def forget(self, position):
            assert position == 0

        def embed(self, text, task, dimensions):
            assert task == "query"
            return np.asarray([len(text), dimensions], dtype=np.float32)

    monkeypatch.setattr(lm_server, "load_model", lambda command: Model())
    commands = b"".join(
        [
            request({"command": "load_model", "model": "test", "model_path": "/m"}),
            request(
                {"command": "logits", "count": 3},
                np.asarray([4, 7, 9], dtype=np.int32).tobytes(),
            ),
            request({"command": "reset"}),
            request(
                {"command": "embed", "size": 5, "task": "query", "dimensions": 128},
                b"hello",
            ),
            request({"command": "close"}),
        ]
    )
    output = io.BytesIO()
    lm_server.serve(io.BytesIO(commands), output)
    assert responses(output.getvalue(), [2, 4]) == [
        {"ok": True},
        {"ok": True, "count": 2},
        np.asarray([9, 3], dtype=bfloat16).tobytes(),
        {"ok": True},
        {"ok": True, "count": 2},
        np.asarray([5, 128], dtype="<f4").tobytes(),
        {"ok": True},
    ]


def test_server_disconnect():
    lm_server.serve(io.BytesIO(), io.BytesIO())


def test_server_keeps_diagnostics_off_the_pipe():
    result = subprocess.run(
        [
            sys.executable,
            "-c",
            "from iron import lm_server; import os; "
            "lm_server.load_model = lambda command: "
            "(print('loading', flush=True), os.write(1, b'native output\\n')); "
            "lm_server.main()",
        ],
        input=request({"command": "load_model"}) + request({"command": "close"}),
        capture_output=True,
        check=True,
        timeout=30,
    )
    assert responses(result.stdout, []) == [{"ok": True}, {"ok": True}]
    assert b"loading" in result.stderr
    assert b"native output" in result.stderr
