#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama's host side without torch: checkpoint reader, weight tree, RoPE
table, embedding and sampling (``weights.py``, ``sampling.py``).

torch appears only here, as the oracle: the checkpoint files are written by
``safetensors.torch`` and every value is compared with what torch produces.
Tier 1 writes small real checkpoints to ``tmp_path``; tier 2 reads the
actual Llama-3.2-1B file and skips when it is absent. No NPU.
"""

import json
import math
import os
import re
import struct
from pathlib import Path

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.applications.llama_3_2_1b.sampling import Sampler
from iron.applications.llama_3_2_1b.weights import (
    Llama3RopeScaling,
    LlamaWeights,
    SafetensorsFile,
    rope_angles,
)

torch = pytest.importorskip("torch")
safetensors_torch = pytest.importorskip("safetensors.torch")
model = pytest.importorskip("iron.applications.llama_3_2_1b.model")


def as_numpy(t):
    """A torch tensor as numpy, bf16 preserved (the oracle side's converter)."""
    if t.dtype is torch.bfloat16:
        return t.view(torch.uint16).numpy().view(bfloat16)
    return t.numpy()


def bitwise_equal(a: np.ndarray, b: np.ndarray) -> bool:
    return (
        a.dtype == b.dtype
        and a.shape == b.shape
        and np.array_equal(a.reshape(-1).view(np.uint8), b.reshape(-1).view(np.uint8))
    )


class ToyConfig:
    """Llama-3.2-1B's proportions at toy size: GQA, a wider FFN, a tied head."""

    n_layers = 2
    emb_dim = 64
    hidden_dim = 128
    n_heads = 8
    n_kv_groups = 2
    head_dim = 8
    vocab_size = 32


def toy_checkpoint(cfg=ToyConfig):
    """A Hugging Face state_dict for ``cfg``, every tensor distinct, bf16."""
    head, kv = cfg.n_heads * cfg.head_dim, cfg.n_kv_groups * cfg.head_dim
    E, F = cfg.emb_dim, cfg.hidden_dim
    shapes = {
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
    gen = torch.Generator().manual_seed(0)
    ckpt = {
        "model.embed_tokens.weight": torch.randn(cfg.vocab_size, E, generator=gen),
        "model.norm.weight": torch.randn(E, generator=gen),
    }
    for i in range(cfg.n_layers):
        for suffix, shape in shapes.items():
            ckpt[f"model.layers.{i}.{suffix}"] = torch.randn(*shape, generator=gen)
    return {k: v.to(torch.bfloat16) for k, v in ckpt.items()}


@pytest.fixture
def toy_path(tmp_path):
    path = tmp_path / "toy.safetensors"
    safetensors_torch.save_file(toy_checkpoint(), path)
    return path


# Tier 1 -- the reader, on files safetensors itself wrote
# ##########################################################################


def test_reader_matches_safetensors_for_every_dtype(tmp_path):
    gen = torch.Generator().manual_seed(1)
    tensors = {
        "bf16": torch.randn(3, 5, generator=gen).to(torch.bfloat16),
        "f16": torch.randn(7, generator=gen).to(torch.float16),
        "f32": torch.randn(2, 3, 4, generator=gen),
        "f64": torch.randn(4, generator=gen).double(),
        "i64": torch.arange(-5, 6, dtype=torch.int64),
        "i32": torch.arange(9, dtype=torch.int32).reshape(3, 3),
        "i16": torch.tensor([-2, 7], dtype=torch.int16),
        "i8": torch.tensor([-128, 0, 127], dtype=torch.int8),
        "u8": torch.tensor([0, 255], dtype=torch.uint8),
        "bool": torch.tensor([True, False, True]),
        "scalar": torch.tensor(3.5),
        "empty": torch.empty(0, 4),
    }
    path = tmp_path / "dtypes.safetensors"
    safetensors_torch.save_file(tensors, path, metadata={"format": "pt"})

    file = SafetensorsFile(path)
    expected = safetensors_torch.load_file(path)
    assert set(file.keys()) == set(expected)
    assert file.metadata == {"format": "pt"}
    for name, t in expected.items():
        assert bitwise_equal(file[name], as_numpy(t)), name


def test_reader_views_the_mapping_without_copying(toy_path):
    file = SafetensorsFile(toy_path)
    a = file["model.norm.weight"]
    b = file["model.norm.weight"]
    assert a is not b and np.shares_memory(a, b)
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
    tree = LlamaWeights.load(toy_path)
    before = {name: np.array(a) for name, a in tree.named_parameters()}
    assert _resident_bytes(toy_path) > 0
    for _, a in tree.named_parameters():
        tree.release(a)
    # The tensors cover the whole file, header page included.
    assert _resident_bytes(toy_path) == 0
    # Read again, each faults back in from the file, unchanged.
    for name, a in tree.named_parameters():
        assert bitwise_equal(a, before[name]), name
    assert _resident_bytes(toy_path) > 0


def test_release_is_only_for_views_of_the_mapping(toy_path):
    file = SafetensorsFile(toy_path)
    tree = LlamaWeights.from_file(file)
    elsewhere = np.zeros(8, dtype=bfloat16)
    assert not file.holds(elsewhere)
    with pytest.raises(ValueError, match="not a contiguous view"):
        file.release(elsewhere)
    with pytest.raises(ValueError, match="not a contiguous view"):
        file.release(tree.embedding[:, ::2])
    # The tree releases what is its file's and leaves anything else alone.
    tree.release(elsewhere)
    assert not elsewhere.any()


def test_reader_rejects_a_range_that_disagrees_with_the_shape(tmp_path):
    header = {"x": {"dtype": "F32", "shape": [4], "data_offsets": [0, 12]}}
    blob = json.dumps(header).encode()
    path = tmp_path / "bad.safetensors"
    path.write_bytes(struct.pack("<Q", len(blob)) + blob + bytes(12))
    with pytest.raises(ValueError, match="claims bytes"):
        SafetensorsFile(path)


def test_reader_rejects_a_range_past_the_end(tmp_path):
    header = {"x": {"dtype": "F32", "shape": [4], "data_offsets": [0, 16]}}
    blob = json.dumps(header).encode()
    path = tmp_path / "short.safetensors"
    path.write_bytes(struct.pack("<Q", len(blob)) + blob + bytes(8))
    with pytest.raises(ValueError, match="8-byte data section"):
        SafetensorsFile(path)


# Tier 1 -- the tree
# ##########################################################################


def test_tree_holds_each_checkpoint_tensor_bitwise(toy_path):
    weights = LlamaWeights.load(toy_path)
    ckpt = safetensors_torch.load_file(toy_path)
    assert len(weights.layers) == ToyConfig.n_layers
    assert bitwise_equal(weights.embedding, as_numpy(ckpt["model.embed_tokens.weight"]))
    assert bitwise_equal(weights.norm, as_numpy(ckpt["model.norm.weight"]))
    blk = weights.layers[1]
    assert bitwise_equal(
        blk.q, as_numpy(ckpt["model.layers.1.self_attn.q_proj.weight"])
    )
    assert bitwise_equal(
        blk.down, as_numpy(ckpt["model.layers.1.mlp.down_proj.weight"])
    )
    assert bitwise_equal(
        blk.norm2, as_numpy(ckpt["model.layers.1.post_attention_layernorm.weight"])
    )


def test_tree_names_are_the_module_trees(toy_path):
    """named_parameters() is model.Llama's, name for name and value for value:
    it replaces Weights(module) as the graphs' names_from.
    """
    weights = LlamaWeights.load(toy_path)
    ckpt = safetensors_torch.load_file(toy_path)
    torch_tree = model.Llama.from_hf(ToyConfig, ckpt)
    ours = dict(weights.named_parameters())
    theirs = dict(torch_tree.named_parameters())
    assert list(ours) == list(theirs)
    for name, p in theirs.items():
        assert bitwise_equal(ours[name], as_numpy(p)), name


def test_the_reference_tree_is_built_from_the_tree_bitwise(toy_path):
    """model.Llama.from_weights, the CPU reference's constructor, holds the
    tree's values exactly as from_hf holds the checkpoint's.
    """
    weights = LlamaWeights.load(toy_path)
    ckpt = safetensors_torch.load_file(toy_path)
    ours = dict(model.Llama.from_weights(ToyConfig, weights).named_parameters())
    theirs = dict(model.Llama.from_hf(ToyConfig, ckpt).named_parameters())
    assert list(ours) == list(theirs)
    for name, p in theirs.items():
        assert ours[name].dtype is torch.bfloat16, name
        assert bitwise_equal(as_numpy(ours[name]), as_numpy(p)), name
    assert not any(p.requires_grad for p in ours.values())


def test_tree_arrays_keep_their_identity(toy_path):
    """The tracer names a weight by id(); a fresh array per read would unname it."""
    weights = LlamaWeights.load(toy_path)
    first = [id(a) for _, a in weights.named_parameters()]
    again = [id(a) for _, a in weights.named_parameters()]
    assert first == again and len(set(first)) == len(first)
    assert weights.out_head is weights.embedding
    assert weights.layers[0].q is weights.layers[0].q


def test_tree_rejects_a_missing_key(tmp_path):
    ckpt = toy_checkpoint()
    del ckpt["model.layers.1.mlp.up_proj.weight"]
    path = tmp_path / "missing.safetensors"
    safetensors_torch.save_file(ckpt, path)
    with pytest.raises(ValueError, match=r"model\.layers\.1\.mlp\.up_proj\.weight"):
        LlamaWeights.load(path)


def test_tree_rejects_an_untied_head(tmp_path):
    ckpt = toy_checkpoint()
    ckpt["lm_head.weight"] = ckpt["model.embed_tokens.weight"].clone()
    path = tmp_path / "untied.safetensors"
    safetensors_torch.save_file(ckpt, path)
    with pytest.raises(ValueError, match="lm_head.weight"):
        LlamaWeights.load(path)


def test_tree_rejects_a_misshapen_layer(tmp_path):
    ckpt = toy_checkpoint()
    good = ckpt["model.layers.1.self_attn.k_proj.weight"]
    ckpt["model.layers.1.self_attn.k_proj.weight"] = torch.zeros(
        good.shape[0], good.shape[1] + 1, dtype=torch.bfloat16
    )
    path = tmp_path / "misshapen.safetensors"
    safetensors_torch.save_file(ckpt, path)
    with pytest.raises(ValueError, match="layer 1 k"):
        LlamaWeights.load(path)


def test_embed_is_torch_embedding(toy_path):
    weights = LlamaWeights.load(toy_path)
    ckpt = safetensors_torch.load_file(toy_path)
    ids = [[0, 31, 7, 7, 12]]
    expected = torch.nn.functional.embedding(
        torch.tensor(ids), ckpt["model.embed_tokens.weight"]
    )
    got = weights.embed(ids)
    assert bitwise_equal(got, as_numpy(expected))
    assert got.flags.writeable  # a copy, not a view of the read-only map


# Tier 1 -- RoPE
# ##########################################################################


def test_rope_is_nearer_exact_than_torch_and_agrees_in_bf16():
    """Not bitwise: torch's pow/cos/sin are not correctly rounded, ours are.

    Against the formula evaluated in float64 throughout, ours is the nearer
    table, at the worst entry and on average. Over the 2048 positions a
    prompt can reach, the bf16 tables the device reads differ in 0.28% of
    entries (365), by at most 2**-8 -- one bf16 step at magnitude 1.
    """
    D, L, base = 64, 2048, 500000.0
    ours = rope_angles(D, L, base)
    theirs = model.rope_angles(D, L, base).numpy()
    assert ours.dtype == np.float32 and ours.shape == (L, D)

    freqs = np.outer(np.arange(L), 1.0 / base ** (np.arange(0, D, 2) / D))
    exact = np.empty((L, D))
    exact[:, ::2], exact[:, 1::2] = np.cos(freqs), np.sin(freqs)
    ours_err, theirs_err = np.abs(ours - exact), np.abs(theirs - exact)
    assert ours_err.max() < theirs_err.max()
    assert ours_err.mean() < theirs_err.mean()

    a = ours.astype(bfloat16).astype(np.float32)
    b = theirs.astype(bfloat16).astype(np.float32)
    assert np.abs(a - b).max() <= 2.0**-8
    assert np.count_nonzero(a != b) / a.size < 0.005


def test_rope_is_correctly_rounded_at_position_zero_and_one():
    """Row 0 is exactly (1, 0) per frequency; row 1 is cos/sin of inv_freq."""
    D, base = 64, 500000.0
    angles = rope_angles(D, 2, base)
    assert np.array_equal(angles[0, ::2], np.ones(D // 2, np.float32))
    assert np.array_equal(angles[0, 1::2], np.zeros(D // 2, np.float32))
    inv = (1.0 / base ** (np.arange(0, D, 2, dtype=np.float32) / np.float32(D))).astype(
        np.float32
    )
    assert np.array_equal(
        angles[1, ::2], np.cos(inv.astype(np.float64)).astype(np.float32)
    )


LLAMA_3_2 = Llama3RopeScaling(
    factor=32.0,
    low_freq_factor=1.0,
    high_freq_factor=4.0,
    original_max_position_embeddings=8192,
)


def _published_llama3_scaling(freqs, factor, low, high, original):
    """``apply_scaling`` from Meta's llama-models reference, as published:
    one frequency at a time, in float64.
    """
    low_wavelen, high_wavelen = original / low, original / high
    scaled = []
    for freq in freqs:
        wavelen = 2 * math.pi / freq
        if wavelen < high_wavelen:
            scaled.append(freq)
        elif wavelen > low_wavelen:
            scaled.append(freq / factor)
        else:
            smooth = (original / wavelen - low) / (high - low)
            scaled.append((1 - smooth) * freq / factor + smooth * freq)
    return np.array(scaled)


def test_llama3_scaling_is_the_published_formula():
    """Every frequency of Llama 3.2 1B's (head_dim 64, base 500000) matches
    Meta's reference, and all three bands are exercised: the fastest fifteen
    kept, three interpolated, the slowest fourteen divided by 32.
    """
    D, base = 64, 500000.0
    inv_freq = 1.0 / base ** (np.arange(0, D, 2) / D)
    ours = LLAMA_3_2(inv_freq)
    published = _published_llama3_scaling(inv_freq, 32.0, 1.0, 4.0, 8192)
    np.testing.assert_allclose(ours, published, rtol=1e-15, atol=0)

    kept = ours == inv_freq
    divided = np.isclose(ours, inv_freq / 32.0, rtol=1e-15, atol=0)
    between = ~kept & ~divided
    assert (kept.sum(), between.sum(), divided.sum()) == (15, 3, 14)
    # The bands are contiguous, fastest to slowest, and the interpolation
    # moves each frequency part of the way to its divided value.
    assert list(np.flatnonzero(kept)) == list(range(15))
    assert list(np.flatnonzero(between)) == [15, 16, 17]
    assert np.all(inv_freq[between] / 32.0 < ours[between])
    assert np.all(ours[between] < inv_freq[between])


def test_scaled_rope_table_rotates_by_the_scaled_frequencies():
    """The scaled table is the unscaled table's formula over the scaled
    frequencies, rounded once; the kept band is the unscaled table's.
    """
    D, L, base = 64, 2048, 500000.0
    exponents = np.arange(0, D, 2, dtype=np.float32) / np.float32(D)
    inv_freq = 1.0 / base ** exponents.astype(np.float64)
    scaled = LLAMA_3_2(inv_freq).astype(np.float32)
    freqs = np.outer(np.arange(L, dtype=np.float32), scaled).astype(np.float64)

    angles = rope_angles(D, L, base, LLAMA_3_2)
    assert angles.dtype == np.float32 and angles.shape == (L, D)
    assert np.array_equal(angles[:, ::2], np.cos(freqs).astype(np.float32))
    assert np.array_equal(angles[:, 1::2], np.sin(freqs).astype(np.float32))

    unscaled = rope_angles(D, L, base)
    assert np.array_equal(angles[:, :30], unscaled[:, :30]), "the kept band moved"
    assert not np.array_equal(angles[:, 30:], unscaled[:, 30:])


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


def test_probabilities_are_the_harness_pipeline():
    """Temperature, top-k and softmax as the torch pipeline Sampler replaced
    computed them, here in float32 on both sides. bf16 logits tie often, so more than k
    survive: both sides keep every tie with the k-th.
    """
    logits = random_logits(128256, seed=4)
    sampler = Sampler(0.7, 50, np.random.default_rng(0))
    t = torch.from_numpy(logits.astype(np.float32)) / 0.7
    kth = torch.topk(t, 50).values[-1]
    t = torch.where(t < kth, torch.tensor(float("-inf")), t)
    expected = torch.softmax(t, dim=-1).double().numpy()
    got = sampler.probabilities(logits)
    assert np.array_equal(got > 0, expected > 0)
    assert np.count_nonzero(got) >= 50
    np.testing.assert_allclose(got, expected, rtol=1e-6, atol=0)


def test_draws_follow_the_distribution():
    logits = np.log(np.array([0.5, 0.3, 0.2], dtype=np.float32))
    sampler = Sampler(1.0, None, np.random.default_rng(5))
    counts = np.bincount([sampler(logits) for _ in range(20000)], minlength=3)
    np.testing.assert_allclose(counts / counts.sum(), [0.5, 0.3, 0.2], atol=0.015)


# Tier 2 -- the real checkpoint (no NPU), gated on its presence
# ##########################################################################

weights_dir = Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv"))
real_checkpoint = weights_dir / "llama3.2-1b" / "model.safetensors"
requires_checkpoint = pytest.mark.skipif(
    not real_checkpoint.exists(),
    reason=f"llama3.2-1b checkpoint not found at {real_checkpoint}",
)


class RealConfig:
    vocab_size = 128256
    emb_dim = 2048
    n_layers = 16
    n_heads = 32
    n_kv_groups = 8
    head_dim = 64
    hidden_dim = 8192


@requires_checkpoint
def test_real_checkpoint_every_tensor_bitwise():
    file = SafetensorsFile(real_checkpoint)
    expected = safetensors_torch.load_file(real_checkpoint)
    assert set(file.keys()) == set(expected)
    for name, t in expected.items():
        assert bitwise_equal(file[name], as_numpy(t)), name


@requires_checkpoint
def test_real_checkpoint_tree():
    weights = LlamaWeights.load(real_checkpoint)
    c = RealConfig
    head, kv = c.n_heads * c.head_dim, c.n_kv_groups * c.head_dim
    assert weights.embedding.shape == (c.vocab_size, c.emb_dim)
    assert weights.embedding.dtype == bfloat16
    assert weights.norm.shape == (c.emb_dim,)
    assert len(weights.layers) == c.n_layers
    for layer in weights.layers:
        assert layer.norm1.shape == layer.norm2.shape == (c.emb_dim,)
        assert layer.q.shape == (head, c.emb_dim)
        assert layer.k.shape == layer.v.shape == (kv, c.emb_dim)
        assert layer.o.shape == (c.emb_dim, head)
        assert layer.gate.shape == layer.up.shape == (c.hidden_dim, c.emb_dim)
        assert layer.down.shape == (c.emb_dim, c.hidden_dim)
    expected_names = set(
        model.translate_hf(safetensors_torch.load_file(real_checkpoint), c.n_layers)
    )
    assert {n for n, _ in weights.named_parameters()} == expected_names


@requires_checkpoint
def test_real_checkpoint_embedding():
    weights = LlamaWeights.load(real_checkpoint)
    table = safetensors_torch.load_file(real_checkpoint)["model.embed_tokens.weight"]
    ids = [[128000, 791, 6864, 315, 9822, 374, 220, 128255, 0]]
    expected = torch.nn.functional.embedding(torch.tensor(ids), table)
    assert bitwise_equal(weights.embed(ids), as_numpy(expected))
