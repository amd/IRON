# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Section-8 example: a toy decoder, no checkpoint download.

``TOY`` is Llama's shape with one layer, and its weights are drawn at a
seed rather than read from a file. The model is the real ``Llama`` class,
compiled as a decode step and a prompt chunk, checked against its host
reference and with ``compile(check=True)``.
"""

import argparse
import json
import math
import struct
import tempfile
from pathlib import Path

import numpy as np
from ml_dtypes import bfloat16

from iron.applications.llama.model import Llama, LlamaConfig
from iron.lm import Checkpoint

# Llama's shape, one layer: small enough to compile quickly, still every
# operator a real decoder builds (RoPE, grouped-query MHA, a gated MLP).
# rope_theta and eps are Llama 3.2 1B's own; the rest is shrunk.
TOY = LlamaConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=1,
    num_attention_heads=16,
    num_key_value_heads=4,
    head_dim=64,
    intermediate_size=2048,
    rope_theta=500000.0,
    max_seq_len=256,
    prefill_chunk=256,
)


def toy_shapes(config: LlamaConfig) -> dict[str, tuple[int, ...]]:
    """Every tensor of a Hugging Face Llama checkpoint of ``config``'s
    shape, by name: the model's own, then each layer's.
    """
    E, F, V = config.hidden_size, config.intermediate_size, config.vocab_size
    Q = config.num_attention_heads * config.head_dim
    KV = config.num_key_value_heads * config.head_dim
    named = {"model.embed_tokens.weight": (V, E), "model.norm.weight": (E,)}
    for i in range(config.num_hidden_layers):
        layer = f"model.layers.{i}"
        named |= {
            f"{layer}.input_layernorm.weight": (E,),
            f"{layer}.self_attn.q_proj.weight": (Q, E),
            f"{layer}.self_attn.k_proj.weight": (KV, E),
            f"{layer}.self_attn.v_proj.weight": (KV, E),
            f"{layer}.self_attn.o_proj.weight": (E, Q),
            f"{layer}.post_attention_layernorm.weight": (E,),
            f"{layer}.mlp.gate_proj.weight": (F, E),
            f"{layer}.mlp.up_proj.weight": (F, E),
            f"{layer}.mlp.down_proj.weight": (E, F),
        }
    return named


def toy_checkpoint(config: LlamaConfig, directory) -> Checkpoint:
    """A sparse ``.safetensors`` file of ``config``'s shape: its header and
    a hole, which ``Checkpoint.tree("random", seed)`` never reads.
    """
    named = toy_shapes(config)
    path = Path(directory) / "toy.safetensors"
    header, end = {}, 0
    for name, shape in named.items():
        size = math.prod(shape) * np.dtype(bfloat16).itemsize
        header[name] = {
            "dtype": "BF16",
            "shape": shape,
            "data_offsets": [end, end + size],
        }
        end += size
    blob = json.dumps(header).encode()
    blob += b" " * (-len(blob) % 8)
    with open(path, "wb") as f:
        f.write(struct.pack("<Q", len(blob)) + blob)
        f.truncate(8 + len(blob) + end)
    return Checkpoint(path)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Section 8: a toy decoder")
    parser.add_argument("--prompt-tokens", type=int, default=8)
    parser.add_argument("--decode-steps", type=int, default=3)
    args = parser.parse_args(argv)

    with tempfile.TemporaryDirectory() as directory:
        checkpoint = toy_checkpoint(TOY, directory)
        model = Llama(TOY, checkpoint.tree("random", seed=0))

        rng = np.random.default_rng(1)
        tokens = rng.integers(0, TOY.vocab_size, args.prompt_tokens).astype(np.int64)
        ids = np.zeros(TOY.prefill_chunk, dtype=np.int32)
        ids[: tokens.size] = tokens
        values = dict(
            token=int(tokens[-1]),
            position=tokens.size - 1,
            start=0,
            rows=tokens.size,
            rope_start=0,
        )

        # feeds= lets the prompt chunk hand its carried values to the decode step.
        decode = model.compile(**model.shapes()[0])
        prompt = model.compile(feeds=decode, **model.shapes()[1])

        _, carry = prompt(ids, **values)
        device_tokens = [int(carry["token"])]
        for _ in range(args.decode_steps):
            _, carry = decode(**carry)
            device_tokens.append(int(carry["token"]))
        print(f"device drew: {device_tokens}")

        # The greedy draw is deterministic, so the device must match exactly.
        _, ref_carry = model.reference(ids, **values)
        host_tokens = [int(ref_carry["token"])]
        for _ in range(args.decode_steps):
            _, ref_carry = model.reference(**ref_carry)
            host_tokens.append(int(ref_carry["token"]))
        print(f"host reference drew: {host_tokens}")
        assert device_tokens == host_tokens, (device_tokens, host_tokens)

        checked = Llama(TOY, checkpoint.tree("random", seed=0))
        checked_decode = checked.compile(**checked.shapes()[0], check=True)
        checked_prompt = checked.compile(**checked.shapes()[1], check=True)
        _, checked_carry = checked_prompt(ids, **values)
        checked_decode(**checked_carry)
        print("PASS!")


if __name__ == "__main__":
    main()
