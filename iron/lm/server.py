# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Serve graph models to a length-prefixed binary client."""

import json
import inspect
import struct
import sys

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import from_name
from ml_dtypes import bfloat16

from iron.applications.embedding_gemma2 import EmbeddingGemma
from iron.applications.embedding_gemma2 import Multimodal as EmbeddingGemmaMultimodal
from iron.applications.gemma4 import Gemma4, Gemma4Multimodal
from iron.applications.llama import Llama

MODELS = {
    "embedding_gemma2": EmbeddingGemma,
    "embedding_gemma2_multimodal": EmbeddingGemmaMultimodal,
    "gemma4": Gemma4,
    "gemma4_multimodal": Gemma4Multimodal,
    "llama": Llama,
}


def read_exact(stream, size):
    data = bytearray()
    while len(data) < size:
        chunk = stream.read(size - len(data))
        if not chunk:
            raise EOFError
        data.extend(chunk)
    return bytes(data)


def receive(stream):
    size = struct.unpack("=I", read_exact(stream, 4))[0]
    return json.loads(read_exact(stream, size))


def send(stream, header, payload=b""):
    data = json.dumps(header, separators=(",", ":")).encode()
    stream.write(struct.pack("=I", len(data)))
    stream.write(data)
    stream.write(payload)
    stream.flush()


def load_model(command):
    model_class = MODELS[command["model"]]
    options = {}
    if "context_length" in command:
        options["max_seq_len"] = command["context_length"]
    return model_class.load(command["model_path"], **options)


def logits(model, tokens):
    parameters = inspect.signature(model.logits).parameters
    return model.logits(tokens, {}) if "raw" in parameters else model.logits(tokens)


def reset(model):
    target = getattr(model, "text", model)
    target.forget(0)


def serve(input_stream, output_stream):
    model = None
    while True:
        command = receive(input_stream)
        try:
            name = command["command"]
            if name == "load_model":
                model = load_model(command)
                send(output_stream, {"ok": True})
            elif name == "logits":
                tokens = np.frombuffer(
                    read_exact(input_stream, command["count"] * 4), np.int32
                )
                values = np.asarray(logits(model, tokens), dtype=bfloat16)
                words = values.view(np.uint16).astype("<u2", copy=False)
                send(output_stream, {"ok": True, "count": words.size}, words.tobytes())
            elif name == "reset":
                reset(model)
                send(output_stream, {"ok": True})
            elif name == "embed":
                text = read_exact(input_stream, command["size"]).decode()
                value = np.asarray(
                    model.embed(text, command["task"], command["dimensions"]),
                    dtype="<f4",
                )
                send(output_stream, {"ok": True, "count": value.size}, value.tobytes())
            elif name == "close":
                send(output_stream, {"ok": True})
                return
            else:
                raise ValueError(f"unknown command: {name}")
        except Exception as error:
            send(output_stream, {"ok": False, "error": str(error)})


def main():
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    serve(sys.stdin.buffer, sys.stdout.buffer)


if __name__ == "__main__":
    main()
