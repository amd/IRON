#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A language model's host side: the checkpoint, its tree by its own names
and sampling (``iron.lm``'s ``Checkpoint``, ``Checkpoint.tree`` and
``Sampler``), on a checkpoint of Llama's names.

The oracle is the safetensors library itself: tier 1 writes small
checkpoints with ``safetensors.numpy`` to ``tmp_path`` and compares every
view with what ``load_file`` reads; tier 2 reads the actual Llama-3.2-1B
file and skips when it is absent. No NPU.
"""

import base64
import dataclasses
import hashlib
import json
import os
import re
import struct
import subprocess
import sys
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16
from safetensors.numpy import load_file, save_file

from iron.lm import Checkpoint, Sampler
from iron.applications.llama.model import LLAMA_3_2_1B, SPECIAL_TOKENS, tokenizer
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


# Each layer's tensors under its Hugging Face name, spelled out here rather
# than read from the model.
def layer_shapes(cfg) -> dict[str, tuple[int, ...]]:
    head, kv = cfg.n_heads * cfg.head_dim, cfg.n_kv_groups * cfg.head_dim
    E, F = cfg.emb_dim, cfg.hidden_dim
    return {
        "input_layernorm.weight": (E,),
        "self_attn.q_proj.weight": (head, E),
        "self_attn.k_proj.weight": (kv, E),
        "self_attn.v_proj.weight": (kv, E),
        "self_attn.o_proj.weight": (E, head),
        "post_attention_layernorm.weight": (E,),
        "mlp.gate_proj.weight": (F, E),
        "mlp.up_proj.weight": (F, E),
        "mlp.down_proj.weight": (E, F),
    }


def toy_checkpoint(cfg=TOY):
    """A Hugging Face state_dict for ``cfg``, every tensor distinct, bf16."""
    rng = np.random.default_rng(0)
    ckpt = {
        "model.embed_tokens.weight": rng.normal(size=(cfg.vocab_size, cfg.emb_dim)),
        "model.norm.weight": rng.normal(size=cfg.emb_dim),
    }
    for i in range(cfg.n_layers):
        for name, shape in layer_shapes(cfg).items():
            ckpt[f"model.layers.{i}.{name}"] = rng.normal(size=shape)
    return {k: v.astype(bfloat16) for k, v in ckpt.items()}


@pytest.fixture
def toy_path(tmp_path):
    path = tmp_path / "toy.safetensors"
    save_file(toy_checkpoint(), path)
    return path


def at(tree, name: str):
    """The node of ``tree`` at the dotted checkpoint ``name``."""
    for key in name.split("."):
        tree = tree[int(key)] if isinstance(tree, list) else vars(tree)[key]
    return tree


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
    tree = checkpoint.tree()
    weights = {name: at(tree, name) for name in checkpoint.tensors}
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


# Tier 1 -- a sharded checkpoint (Qwen3's own: two files and an index)
# ##########################################################################


def shard(tensors: dict, tmp_path: Path, split: int) -> Path:
    """``tensors`` written as two ``.safetensors`` shards and the index
    naming each tensor's shard, as Hugging Face's ``save_pretrained``
    splits a checkpoint past its size cap. Returns the index's path.
    """
    names = list(tensors)
    shards = {
        "model-00001-of-00002.safetensors": names[:split],
        "model-00002-of-00002.safetensors": names[split:],
    }
    weight_map = {}
    for filename, keys in shards.items():
        save_file({k: tensors[k] for k in keys}, tmp_path / filename)
        weight_map.update({k: filename for k in keys})
    index = tmp_path / "toy.safetensors.index.json"
    index.write_text(json.dumps({"metadata": {}, "weight_map": weight_map}))
    return index


@pytest.fixture
def sharded_toy_path(tmp_path):
    return shard(toy_checkpoint(), tmp_path, split=5)


def test_checkpoint_reads_a_sharded_index(sharded_toy_path):
    tensors = Checkpoint(sharded_toy_path).tensors
    expected = {
        **load_file(sharded_toy_path.parent / "model-00001-of-00002.safetensors"),
        **load_file(sharded_toy_path.parent / "model-00002-of-00002.safetensors"),
    }
    assert set(tensors) == set(expected)
    for name, t in expected.items():
        assert bitwise_equal(tensors[name], t), name


def test_checkpoint_rejects_a_tensor_named_in_two_shards(tmp_path):
    """Both files on disk hold every tensor (a malformed split): the index
    names each shard once, but ``name`` is in both files' own headers.
    """
    tensors = toy_checkpoint()
    name = next(iter(tensors))
    save_file(tensors, tmp_path / "a.safetensors")
    save_file(tensors, tmp_path / "b.safetensors")
    weight_map = {k: "a.safetensors" for k in tensors}
    weight_map[name] = "b.safetensors"
    index = tmp_path / "both.safetensors.index.json"
    index.write_text(json.dumps({"weight_map": weight_map}))
    with pytest.raises(ValueError, match=re.escape(name)):
        Checkpoint(index)


def test_checkpoint_rejects_a_shard_that_disagrees_with_the_index(tmp_path):
    """The index's own partition and a shard's real header disagree, with no
    tensor duplicated across shards: a stale or hand-edited index, not the
    two-shards-claim-the-same-name corruption above.
    """
    tensors = toy_checkpoint()
    names = list(tensors)
    weight_map = {n: "a.safetensors" for n in names[:-1]}
    weight_map[names[-1]] = "b.safetensors"
    save_file({n: tensors[n] for n in names[:-1]}, tmp_path / "a.safetensors")
    save_file({}, tmp_path / "b.safetensors")  # b's real header holds nothing
    index = tmp_path / "mismatched.safetensors.index.json"
    index.write_text(json.dumps({"weight_map": weight_map}))
    with pytest.raises(ValueError, match=re.escape(names[-1])):
        Checkpoint(index)


def test_checkpoint_release_drops_the_right_shard(sharded_toy_path):
    first_shard = sharded_toy_path.parent / "model-00001-of-00002.safetensors"
    second_shard = sharded_toy_path.parent / "model-00002-of-00002.safetensors"
    checkpoint = Checkpoint(sharded_toy_path)
    tree = checkpoint.tree()
    weights = {name: at(tree, name) for name in checkpoint.tensors}
    assert _resident_bytes(first_shard) > 0 and _resident_bytes(second_shard) > 0
    for a in weights.values():
        checkpoint.release(a)
    assert _resident_bytes(first_shard) == 0
    assert _resident_bytes(second_shard) == 0


# Tier 1 -- the tree
# ##########################################################################


def test_each_checkpoint_tensor_lands_on_its_name_bitwise(toy_path):
    """Every tensor is distinct, so a mapping that crosses two same-shaped
    weights over (k and v, gate and up) is caught.
    """
    tree = Checkpoint(toy_path).tree()
    ckpt = load_file(toy_path)
    assert len(tree.model.layers) == TOY.n_layers
    assert list(vars(tree)) == ["model"]
    for name, expected in ckpt.items():
        assert bitwise_equal(at(tree, name), expected), name


def test_tree_arrays_are_the_checkpoints(toy_path):
    """The tracer names a weight by id(), so each is one array, as read."""
    checkpoint = Checkpoint(toy_path)
    tree = checkpoint.tree()
    name = "model.layers.1.self_attn.v_proj.weight"
    assert tree.model.layers[1].self_attn.v_proj.weight is checkpoint.tensors[name]
    ids = [id(at(tree, name)) for name in checkpoint.tensors]
    assert len(set(ids)) == len(ids)


def test_tree_rejects_a_skipped_layer(tmp_path):
    """Layer 0 gone and layer 1 whole: refused, not one layer renumbered."""
    ckpt = {
        k: v for k, v in toy_checkpoint().items() if not k.startswith("model.layers.0.")
    }
    save_file(ckpt, tmp_path / "skipped.safetensors")
    with pytest.raises(ValueError, match=re.escape("[1] skip [0]")):
        Checkpoint(tmp_path / "skipped.safetensors").tree()


@pytest.mark.parametrize("fill", ["random", "unread"])
def test_a_filled_tree_has_the_checkpoints_names_shapes_and_dtypes(toy_path, fill):
    """Neither reads a tensor: each array is the process's own."""
    checkpoint = Checkpoint(toy_path)
    tree = checkpoint.tree(fill)
    for name, tensor in checkpoint.tensors.items():
        a = at(tree, name)
        assert (a.shape, a.dtype) == (tensor.shape, tensor.dtype), name
        assert a.flags.owndata and a is not tensor, name


def test_random_fill_draws_at_its_seed(toy_path):
    """Each matrix at a deviation of 1/sqrt(in), every norm one."""
    checkpoint = Checkpoint(toy_path)
    a, b, c = (checkpoint.tree("random", seed) for seed in (3, 3, 4))
    for name in checkpoint.tensors:
        assert bitwise_equal(at(a, name), at(b, name)), name
    q = "model.layers.0.self_attn.q_proj.weight"
    assert not np.array_equal(at(a, q), at(c, q))
    for name, tensor in checkpoint.tensors.items():
        x = at(a, name).astype(np.float32)
        if tensor.ndim == 1:
            assert (x == 1).all(), name
        else:
            assert abs(x.std() * np.sqrt(tensor.shape[1]) - 1) < 0.1, name


def test_unread_fill_zeroes_a_scalar(tmp_path):
    """A graph may read a scalar as it is built: a clamp's bounds."""
    save_file({"bound": np.array(3.5, dtype=np.float32)}, tmp_path / "s.safetensors")
    tree = Checkpoint(tmp_path / "s.safetensors").tree("unread")
    assert tree.bound.shape == () and tree.bound == 0


def test_tree_refuses_an_unknown_fill(toy_path):
    with pytest.raises(ValueError, match="'zeros'"):
        Checkpoint(toy_path).tree("zeros")


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


def test_every_special_token_decodes_once(tmp_path):
    """Each id from 128000 to 128255 is one special token, as Meta's
    llama-models numbers them, over a byte-level toy ``tokenizer.model``.
    """
    path = tmp_path / "tokenizer.model"
    path.write_text(
        "".join(f"{base64.b64encode(bytes([b])).decode()} {b}\n" for b in range(256))
    )
    enc = tokenizer(path)
    assert sorted(SPECIAL_TOKENS.values()) == list(range(128000, 128256))
    names = [enc.decode([i]) for i in range(128000, 128256)]
    assert names == list(SPECIAL_TOKENS)
    for name, token in [("<|eom_id|>", 128008), ("<|eot_id|>", 128009)]:
        assert enc.encode(name, allowed_special="all") == [token]
        assert enc.decode([token]) == name


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
    c = LLAMA_3_2_1B
    model = Checkpoint(real_checkpoint).tree().model
    assert model.embed_tokens.weight.shape == (c.vocab_size, c.emb_dim)
    assert model.embed_tokens.weight.dtype == bfloat16
    assert len(model.layers) == c.n_layers
    for layer in model.layers:
        for name, shape in layer_shapes(c).items():
            assert at(layer, name).shape == shape, name
    assert sorted(vars(Checkpoint(real_checkpoint).tree())) == ["model"]


# Tier 2 -- Qwen3's real, sharded checkpoint (no NPU), gated on its presence
# ##########################################################################

real_qwen3_index = weights_dir("qwen3-1.7b") / "model.safetensors.index.json"
requires_qwen3_checkpoint = pytest.mark.skipif(
    not real_qwen3_index.exists(),
    reason=f"qwen3-1.7b checkpoint not found at {real_qwen3_index}",
)


@requires_qwen3_checkpoint
def test_real_qwen3_checkpoint_every_tensor_bitwise():
    """Every tensor the index names, read from whichever of its two shard
    files holds it, bitwise the shard's own.
    """
    tensors = Checkpoint(real_qwen3_index).tensors
    index = json.loads(real_qwen3_index.read_text())
    by_shard: dict[str, list[str]] = {}
    for name, filename in index["weight_map"].items():
        by_shard.setdefault(filename, []).append(name)
    assert set(tensors) == set(index["weight_map"])
    for filename, names in by_shard.items():
        expected = load_file(real_qwen3_index.parent / filename)
        for name in names:
            assert bitwise_equal(tensors[name], expected[name]), name


# Tier 1 -- Download, a test input cached in NPU_CACHE_HOME
# ##########################################################################

# A small, stable public file over real HTTPS: no IRON asset of its own, so
# this gate costs one tiny download rather than a checkpoint-sized one.
PINNED_URL = "https://raw.githubusercontent.com/octocat/Hello-World/master/README"
PINNED_SHA256 = "03ba204e50d126e4674c005e04d82e84c21366780af1f43bd54a37816b6ab340"


def fetch_in(cache_home: Path, weights_home: Path, url: str, sha256: str):
    """``Download(url, sha256).fetch()``, in a subprocess with
    ``NPU_CACHE_HOME`` and ``IRON_EXAMPLE_WEIGHTS_DIR`` set to `cache_home`
    and `weights_home`: both constants are read once at import, which an
    in-process ``os.environ`` write would not reach.
    """
    script = f"from iron.lm.testing import Download; print(Download({url!r}, {sha256!r}).fetch())"
    return subprocess.run(
        [sys.executable, "-c", script],
        env=os.environ
        | {
            "NPU_CACHE_HOME": str(cache_home),
            "IRON_EXAMPLE_WEIGHTS_DIR": str(weights_home),
        },
        capture_output=True,
        text=True,
    )


def test_download_fetches_into_the_cache_not_the_read_only_weights_dir(tmp_path):
    """A `Download` never touches the weights directory (CI mounts it
    read-only), and a repeat of the same pin is served from the cache
    without a second trip over the network.
    """
    cache_home, weights = tmp_path / "cache", tmp_path / "weights"
    weights.mkdir()
    weights.chmod(0o555)
    try:
        first = fetch_in(cache_home, weights, PINNED_URL, PINNED_SHA256)
        assert first.returncode == 0, first.stderr
        fetched = Path(first.stdout.strip())
        assert fetched.is_relative_to(cache_home)
        assert not fetched.is_relative_to(weights)
        assert hashlib.sha256(fetched.read_bytes()).hexdigest() == PINNED_SHA256

        # The same pin, its host now unreachable (a reserved, never-resolving
        # TLD, RFC 2606): this succeeds only by reading the cached file.
        unreachable = "https://host.invalid/README"
        second = fetch_in(cache_home, weights, unreachable, PINNED_SHA256)
        assert second.returncode == 0, second.stderr
        assert Path(second.stdout.strip()) == fetched
    finally:
        weights.chmod(0o755)
