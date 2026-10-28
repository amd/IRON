# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import io
import json
import struct

import numpy as np
from ml_dtypes import bfloat16

from iron import server


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
            stream.read(count * next(sizes))
    return found


def test_registry_contains_graph_models():
    assert set(server.MODELS) == {
        "embedding_gemma2",
        "embedding_gemma2_multimodal",
        "gemma4",
        "gemma4_multimodal",
        "llama",
    }


def test_load_model_uses_registry(monkeypatch):
    class Model:
        @classmethod
        def load(cls, path, **options):
            return path, options

    monkeypatch.setitem(server.MODELS, "test", Model)
    assert server.load_model(
        {
            "model": "test",
            "model_path": "/model",
            "context_length": 128,
        }
    ) == ("/model", {"max_seq_len": 128})
    assert server.load_model({"model": "test", "model_path": "/model"}) == (
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
    np.testing.assert_array_equal(server.logits(model, np.asarray([1, 2])), [1, 2])
    server.reset(model)


def test_server_protocol(monkeypatch):
    class Model:
        def logits(self, tokens):
            return np.asarray([tokens[-1], len(tokens)], dtype=bfloat16)

        def forget(self, position):
            assert position == 0

        def embed(self, text, task, dimensions):
            assert task == "query"
            return np.asarray([len(text), dimensions], dtype=np.float32)

    monkeypatch.setattr(server, "load_model", lambda command: Model())
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
    server.serve(io.BytesIO(commands), output)
    assert responses(output.getvalue(), [2, 4]) == [
        {"ok": True},
        {"ok": True, "count": 2},
        {"ok": True},
        {"ok": True, "count": 2},
        {"ok": True},
    ]
