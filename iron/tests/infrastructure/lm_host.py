#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A language model's host side: the checkpoint, the weight tree a layout
places it in and sampling (``iron.lm``'s ``Checkpoint``,
``load_weights`` and ``Sampler``), at Llama's layout.

The oracle is the safetensors library itself: tier 1 writes small
checkpoints with ``safetensors.numpy`` to ``tmp_path`` and compares every
view with what ``load_file`` reads; tier 2 reads the actual Llama-3.2-1B
file and skips when it is absent. No NPU.
"""

import dataclasses
import json
import re
import struct
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16
from safetensors.numpy import load_file, save_file

from iron import lm
from iron.lm import Checkpoint, Sampler
from iron.lm.llama3.model import LLAMA_3_2_1B, layout
from iron.lm.testing import weights_dir
from iron.operators import sample


def bitwise_equal(a: np.ndarray, b: np.ndarray) -> bool:
    return (
        a.dtype == b.dtype
        and a.shape == b.shape
        and np.array_equal(a.reshape(-1).view(np.uint8), b.reshape(-1).view(np.uint8))
    )


#: Llama-3.2-1B's proportions at toy size: GQA, a wider FFN, a tied head.
TOY = dataclasses.replace(
    LLAMA_3_2_1B,
    vocab_size=32,
    emb_dim=64,
    n_layers=2,
    n_heads=8,
    n_kv_groups=2,
    head_dim=8,
    hidden_dim=128,
    max_seq_len=16,
    prefill_chunk=8,
)


def load_weights(tensors, config=TOY):
    """``tensors`` in the tree of Llama's layout at ``config``."""
    return lm.load_weights(tensors, layout(config), config.n_layers)


# Each layer field under its Hugging Face name, spelled out here rather
# than read from the runner.
LAYER_NAMES = {
    "norm1": "input_layernorm.weight",
    "q": "self_attn.q_proj.weight",
    "k": "self_attn.k_proj.weight",
    "v": "self_attn.v_proj.weight",
    "o": "self_attn.o_proj.weight",
    "norm2": "post_attention_layernorm.weight",
    "gate": "mlp.gate_proj.weight",
    "up": "mlp.up_proj.weight",
    "down": "mlp.down_proj.weight",
}


def toy_checkpoint(cfg=TOY):
    """A Hugging Face state_dict for ``cfg``, every tensor distinct, bf16."""
    head, kv = cfg.n_heads * cfg.head_dim, cfg.n_kv_groups * cfg.head_dim
    E, F = cfg.emb_dim, cfg.hidden_dim
    shapes = {
        "norm1": (E,),
        "q": (head, E),
        "k": (kv, E),
        "v": (kv, E),
        "o": (E, head),
        "norm2": (E,),
        "gate": (F, E),
        "up": (F, E),
        "down": (E, F),
    }
    rng = np.random.default_rng(0)
    ckpt = {
        "model.embed_tokens.weight": rng.normal(size=(cfg.vocab_size, E)),
        "model.norm.weight": rng.normal(size=E),
    }
    for i in range(cfg.n_layers):
        for f, shape in shapes.items():
            ckpt[f"model.layers.{i}.{LAYER_NAMES[f]}"] = rng.normal(size=shape)
    return {k: v.astype(bfloat16) for k, v in ckpt.items()}


@pytest.fixture
def toy_path(tmp_path):
    path = tmp_path / "toy.safetensors"
    save_file(toy_checkpoint(), path)
    return path


def arrays(weights):
    """Every array of the tree, by a name for it."""
    out = {"embedding": weights.embedding, "norm": weights.norm}
    for i, layer in enumerate(weights.layers):
        out.update({f"layers.{i}.{f}": a for f, a in vars(layer).items()})
    return out


# Tier 1 -- the checkpoint, on files safetensors itself wrote
# ##########################################################################


def test_checkpoint_matches_safetensors_for_every_dtype(tmp_path):
    rng = np.random.default_rng(1)
    tensors = {
        "bf16": rng.normal(size=(3, 5)).astype(bfloat16),
        "f16": rng.normal(size=7).astype(np.float16),
        "f32": rng.normal(size=(2, 3, 4)).astype(np.float32),
        "scalar": np.array(3.5, dtype=np.float32),
        "empty": np.empty((0, 4), dtype=np.float32),
    }
    path = tmp_path / "dtypes.safetensors"
    save_file(tensors, path, metadata={"format": "np"})

    checkpoint = Checkpoint(path)
    expected = load_file(path)
    assert set(checkpoint.tensors) == set(expected)
    for name, t in expected.items():
        assert bitwise_equal(checkpoint.tensors[name], t), name
        assert bitwise_equal(checkpoint.tensors[name], tensors[name]), name


def test_checkpoint_views_the_mapping_without_copying(toy_path):
    a = Checkpoint(toy_path).tensors["model.norm.weight"]
    assert not a.flags.writeable and not a.flags.owndata
    with pytest.raises(ValueError):
        a[0] = 0


def _resident_bytes(path: Path) -> int:
    """This process's resident bytes of its mappings of ``path``, per the kernel."""
    total, inside = 0, False
    for line in Path("/proc/self/smaps").read_text().splitlines():
        fields = line.split()
        if re.match(r"[0-9a-f]+-[0-9a-f]+ ", line):
            inside = fields[-1] == str(path.resolve())
        elif inside and fields[0] == "Rss:":
            total += int(fields[1]) * 1024
    return total


def test_release_drops_the_pages_and_keeps_the_bytes(toy_path):
    checkpoint = Checkpoint(toy_path)
    weights = arrays(load_weights(checkpoint.tensors))
    before = {name: np.array(a) for name, a in weights.items()}
    assert _resident_bytes(toy_path) > 0
    for a in weights.values():
        checkpoint.release(a)
    # The tensors cover the whole file, header page included.
    assert _resident_bytes(toy_path) == 0
    # Read again, each faults back in from the file, unchanged.
    for name, a in weights.items():
        assert bitwise_equal(a, before[name]), name
    assert _resident_bytes(toy_path) > 0


def test_release_leaves_anything_else_alone(toy_path):
    checkpoint = Checkpoint(toy_path)
    elsewhere = np.zeros(8, dtype=bfloat16)
    checkpoint.release(elsewhere)
    checkpoint.release(checkpoint.tensors["model.embed_tokens.weight"][:, ::2])
    assert not elsewhere.any() and _resident_bytes(toy_path) > 0


@pytest.mark.parametrize(
    "end, data", [(12, 12), (16, 8)], ids=["range-not-the-shape", "range-past-the-end"]
)
def test_checkpoint_rejects_a_malformed_file(tmp_path, end, data):
    """A byte range that is not the shape's is refused on open."""
    header = {"x": {"dtype": "F32", "shape": [4], "data_offsets": [0, end]}}
    blob = json.dumps(header).encode()
    path = tmp_path / "bad.safetensors"
    path.write_bytes(struct.pack("<Q", len(blob)) + blob + bytes(data))
    with pytest.raises(ValueError):
        Checkpoint(path)


def test_checkpoint_rejects_an_unsupported_dtype(tmp_path):
    """One safetensors knows and a model's weights never are: complex64."""
    header = {"x": {"dtype": "C64", "shape": [4], "data_offsets": [0, 32]}}
    blob = json.dumps(header).encode()
    path = tmp_path / "c64.safetensors"
    path.write_bytes(struct.pack("<Q", len(blob)) + blob + bytes(32))
    with pytest.raises(ValueError, match="C64"):
        Checkpoint(path)


# Tier 1 -- the tree
# ##########################################################################


def test_each_checkpoint_tensor_lands_on_its_field_bitwise(toy_path):
    """Every tensor is distinct, so a mapping that crosses two same-shaped
    weights over (k and v, gate and up) is caught.
    """
    weights = load_weights(Checkpoint(toy_path).tensors)
    ckpt = load_file(toy_path)
    assert len(weights.layers) == TOY.n_layers
    assert bitwise_equal(weights.embedding, ckpt["model.embed_tokens.weight"])
    assert bitwise_equal(weights.norm, ckpt["model.norm.weight"])
    for i, layer in enumerate(weights.layers):
        assert list(vars(layer)) == list(LAYER_NAMES)
        for f, hf in LAYER_NAMES.items():
            expected = ckpt[f"model.layers.{i}.{hf}"]
            assert bitwise_equal(getattr(layer, f), expected), (i, f)


def test_tree_arrays_are_the_checkpoints(toy_path):
    """The tracer names a weight by id(), so each is one array, as read."""
    tensors = Checkpoint(toy_path).tensors
    weights = load_weights(tensors)
    assert weights.layers[1].v is tensors["model.layers.1.self_attn.v_proj.weight"]
    ids = [id(a) for a in arrays(weights).values()]
    assert len(set(ids)) == len(ids)


def test_tree_rejects_a_missing_key():
    ckpt = toy_checkpoint()
    del ckpt["model.layers.1.mlp.up_proj.weight"]
    with pytest.raises(ValueError, match=r"model\.layers\.1\.mlp\.up_proj\.weight"):
        load_weights(ckpt)


def test_tree_rejects_a_missing_layer():
    """Layer 0 gone and layer 1 whole: the tree is still two layers, one
    of them missing, not one layer renumbered.
    """
    ckpt = {
        k: v for k, v in toy_checkpoint().items() if not k.startswith("model.layers.0.")
    }
    with pytest.raises(ValueError, match=r"model\.layers\.0\.input_layernorm\.weight"):
        load_weights(ckpt)


def test_tree_rejects_an_untied_head():
    ckpt = toy_checkpoint()
    ckpt["lm_head.weight"] = ckpt["model.embed_tokens.weight"].copy()
    with pytest.raises(ValueError, match="lm_head.weight"):
        load_weights(ckpt)


def test_tree_rejects_a_misshapen_layer():
    ckpt = toy_checkpoint()
    name = "model.layers.1.self_attn.k_proj.weight"
    good = ckpt[name]
    ckpt[name] = np.zeros((good.shape[0], good.shape[1] + 1), dtype=bfloat16)
    with pytest.raises(ValueError, match=re.escape(f"{name} is (16, 65)")):
        load_weights(ckpt)


# Tier 1 -- sampling
# ##########################################################################


def random_logits(n=1000, seed=0):
    return np.random.default_rng(seed).normal(size=n).astype(bfloat16)


def test_greedy_is_argmax():
    logits = random_logits()
    sampler = Sampler(0.0, top_k=50, rng=np.random.default_rng(0))
    assert sampler(logits) == int(np.argmax(logits.astype(np.float32)))


def test_seeded_sampling_is_reproducible():
    logits = random_logits()
    a = Sampler(0.7, 50, np.random.default_rng(1608560892))
    b = Sampler(0.7, 50, np.random.default_rng(1608560892))
    draws = [a(logits) for _ in range(200)]
    assert draws == [b(logits) for _ in range(200)]
    assert len(set(draws)) > 1  # it does sample


def test_top_k_never_leaves_the_top_k():
    logits = random_logits()
    k = 5
    x = logits.astype(np.float32)
    top = set(np.flatnonzero(x >= np.sort(x)[-k]).tolist())
    sampler = Sampler(1.0, k, np.random.default_rng(3))
    assert {sampler(logits) for _ in range(2000)} == top


def test_top_k_keeps_ties_with_the_kth():
    logits = np.array([5.0, 3.0, 3.0, 3.0, 1.0], dtype=np.float32)
    probs = Sampler(1.0, 2, np.random.default_rng(0)).probabilities(logits)
    assert np.all(probs[:4] > 0) and probs[4] == 0


def test_device_rows_are_the_host_draws():
    """rows() takes the uniforms the host draws would, greedy steps included,
    so the device's tokens are the host's for the same seed.
    """
    logits = random_logits(4096, seed=6)
    for temperature in (0.7, 0.0):
        host = Sampler(temperature, 50, np.random.default_rng(9))
        device = Sampler(temperature, 50, np.random.default_rng(9))
        rows = device.rows(8, k_max=64)
        want = [host(logits) for _ in range(8)]
        assert [sample.reference(logits, r) for r in rows] == want
        assert host.rng.random() == device.rng.random()


def test_device_rows_refuse_an_unbounded_top_k():
    rng = np.random.default_rng(0)
    with pytest.raises(ValueError, match="device draws"):
        Sampler(0.7, None, rng).rows(1, k_max=64)
    with pytest.raises(ValueError, match="device draws"):
        Sampler(0.7, 65, rng).rows(1, k_max=64)


def test_draws_follow_the_distribution():
    logits = np.log(np.array([0.5, 0.3, 0.2], dtype=np.float32))
    sampler = Sampler(1.0, None, np.random.default_rng(5))
    counts = np.bincount([sampler(logits) for _ in range(20000)], minlength=3)
    np.testing.assert_allclose(counts / counts.sum(), [0.5, 0.3, 0.2], atol=0.015)


# Tier 2 -- the real checkpoint (no NPU), gated on its presence
# ##########################################################################

real_checkpoint = weights_dir("llama3.2-1b") / "model.safetensors"
requires_checkpoint = pytest.mark.skipif(
    not real_checkpoint.exists(),
    reason=f"llama3.2-1b checkpoint not found at {real_checkpoint}",
)


@requires_checkpoint
def test_real_checkpoint_every_tensor_bitwise():
    tensors = Checkpoint(real_checkpoint).tensors
    expected = load_file(real_checkpoint)
    assert set(tensors) == set(expected)
    for name, t in expected.items():
        assert bitwise_equal(tensors[name], t), name


@requires_checkpoint
def test_real_checkpoint_is_llama_3_2_1b():
    """The real key spelling and shapes are the default config's, and
    nothing is left over.
    """
    weights = load_weights(Checkpoint(real_checkpoint).tensors, LLAMA_3_2_1B)
    assert weights.embedding.dtype == bfloat16
    assert len(weights.layers) == LLAMA_3_2_1B.n_layers
