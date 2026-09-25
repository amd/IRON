#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The llama parameter tree agrees with a Hugging Face checkpoint.

Tier 1 needs no weights file and no NPU: a checkpoint is a dict of tensors, so
a correctly-shaped stand-in exercises the naming and the shapes, which is
precisely what the translation can get wrong. Values are checked by identity
(``is`` / ``data_ptr()``), so a mapping that crosses two weights over is caught
even though both have the same shape, and "2.5 GB is not copied" becomes a
checked fact rather than a claim.

Tier 2 (``test_real_checkpoint_*``) loads the actual 2.47 GB Llama-3.2-1B
safetensors; it is the only test that proves :data:`FROM_HF` matches the real
key spelling, and it skips cleanly when the checkpoint is absent.
"""

import os
from pathlib import Path

import pytest
import safetensors.torch
import torch

from iron.applications.llama_3_2_1b.model import (
    FROM_HF,
    FROM_HF_TOP,
    Llama,
    translate_hf,
)


class Config:
    """Llama-3.2-1B's *shape* at toy dimensions.

    Every proportion the translation depends on is preserved -- grouped-query
    attention (n_kv_groups < n_heads), a wider FFN, a tied output head -- while
    the dimensions are small enough that the whole tier runs in under a second.
    The real geometry is exercised by :class:`RealConfig` in tier 2.
    """

    n_layers = 2
    emb_dim = 64
    hidden_dim = 128
    n_heads = 8
    n_kv_groups = 2
    head_dim = 8
    vocab_size = 32


def hf_checkpoint(cfg=Config):
    """A Hugging Face state_dict for this geometry, every tensor distinct."""
    head = cfg.n_heads * cfg.head_dim
    kv = cfg.n_kv_groups * cfg.head_dim
    shapes = {
        "input_layernorm.weight": (cfg.emb_dim,),
        "self_attn.q_proj.weight": (head, cfg.emb_dim),
        "self_attn.k_proj.weight": (kv, cfg.emb_dim),
        "self_attn.v_proj.weight": (kv, cfg.emb_dim),
        "self_attn.o_proj.weight": (cfg.emb_dim, head),
        "post_attention_layernorm.weight": (cfg.emb_dim,),
        "mlp.gate_proj.weight": (cfg.hidden_dim, cfg.emb_dim),
        "mlp.up_proj.weight": (cfg.hidden_dim, cfg.emb_dim),
        "mlp.down_proj.weight": (cfg.emb_dim, cfg.hidden_dim),
    }
    weights = {
        "model.norm.weight": torch.randn(cfg.emb_dim, dtype=torch.bfloat16),
        "model.embed_tokens.weight": torch.randn(
            cfg.vocab_size, cfg.emb_dim, dtype=torch.bfloat16
        ),
    }
    for i in range(cfg.n_layers):
        for suffix, shape in shapes.items():
            weights[f"model.layers.{i}.{suffix}"] = torch.randn(
                shape, dtype=torch.bfloat16
            )
    return weights


# Tier 1 -- the naming and shapes, ported from the reference
# ##########################################################################


def test_every_declared_parameter_is_filled():
    """load_state_dict is strict, so a missing or misnamed key raises here."""
    model = Llama.from_hf(Config, hf_checkpoint())
    assert len(list(model.named_parameters())) == len(FROM_HF) * Config.n_layers + len(
        FROM_HF_TOP
    )


def test_translation_is_exhaustive_over_the_checkpoint():
    """Nothing in the checkpoint is silently dropped on the way in."""
    weights = hf_checkpoint()
    translated = translate_hf(weights, Config.n_layers)
    assert len(translated) == len(weights), "a checkpoint key went unused"


def test_each_weight_lands_on_the_right_parameter():
    """Identity, not shape: q and k would both 'fit' if the map crossed them."""
    weights = hf_checkpoint()
    translated = translate_hf(weights, Config.n_layers)
    for i in range(Config.n_layers):
        for hf, ours in FROM_HF.items():
            assert (
                translated[f"layers.{i}.{ours}"] is weights[f"model.layers.{i}.{hf}"]
            ), f"layer {i}: {ours} did not come from {hf}"


def test_output_head_is_tied_to_the_token_embedding():
    """Llama 3.2 reads one matrix both to embed a token and to score one."""
    weights = hf_checkpoint()
    model = Llama.from_hf(Config, weights)
    assert torch.equal(model.out_head.weight, weights["model.embed_tokens.weight"])


def test_a_renamed_upstream_key_is_an_error():
    """Silently leaving a weight at its initial value would be far worse."""
    weights = hf_checkpoint()
    weights["model.layers.0.mlp.gate_proj.weight_v2"] = weights.pop(
        "model.layers.0.mlp.gate_proj.weight"
    )
    try:
        Llama.from_hf(Config, weights)
    except KeyError as exc:
        assert "gate_proj" in str(exc)
    else:
        raise AssertionError("a missing checkpoint key should raise")


def test_parameter_names_match_the_checkpoint_shape():
    """Names are the contract with the device buffers, so pin them."""
    with torch.device("meta"):
        model = Llama(Config)
    names = {name for name, _ in model.named_parameters()}
    assert "layers.0.attn.q.weight" in names
    assert "layers.1.ffn.down.weight" in names
    assert "norm.weight" in names and "out_head.weight" in names


# Tier 1 -- the invariants this branch adds
# ##########################################################################


def test_construction_allocates_nothing():
    """Building the tree under meta must not touch 2.5 GB of storage.

    Every parameter is meta -- it has a shape and dtype but no bytes -- until a
    checkpoint is assigned in. This is what lets the tree cost nothing to hold.
    """
    with torch.device("meta"):
        model = Llama(Config)
    for name, param in model.named_parameters():
        assert param.is_meta, f"{name} was materialised before load"


def test_load_shares_storage_with_the_checkpoint():
    """assign=True makes each parameter *be* the checkpoint tensor, not a copy.

    data_ptr() equality is the direct evidence that the 2.5 GB checkpoint is
    not duplicated when the tree is filled.
    """
    weights = hf_checkpoint()
    model = Llama.from_hf(Config, weights)
    assert (
        model.get_parameter("layers.0.attn.q.weight").data_ptr()
        == weights["model.layers.0.self_attn.q_proj.weight"].data_ptr()
    )


def test_out_head_shares_storage_with_embed_tokens():
    """The tie is one matrix -- data_ptr(), not torch.equal.

    torch.equal would pass on two equal copies; at 262 M params the difference
    between one matrix and two is 525 MB, so the identity is what matters.
    """
    weights = hf_checkpoint()
    model = Llama.from_hf(Config, weights)
    assert (
        model.out_head.weight.data_ptr()
        == weights["model.embed_tokens.weight"].data_ptr()
    )


def test_no_parameter_requires_grad():
    """Nothing here trains; grad tracking would only cost memory and surprise."""
    model = Llama.from_hf(Config, hf_checkpoint())
    for name, param in model.named_parameters():
        assert not param.requires_grad, f"{name} still tracks grad"


def test_a_wrong_shape_is_an_error():
    """A weight of the wrong width must fail loudly, naming the parameter.

    assign=True does not reshape: a mismatched tensor would otherwise install a
    parameter of the wrong size and be caught only much later on the device.
    """
    weights = hf_checkpoint()
    good = weights["model.layers.0.self_attn.q_proj.weight"]
    # A real q_proj of the wrong input width.
    weights["model.layers.0.self_attn.q_proj.weight"] = torch.randn(
        good.shape[0], good.shape[1] + 1, dtype=torch.bfloat16
    )
    with pytest.raises(RuntimeError) as exc:
        Llama.from_hf(Config, weights)
    assert "attn.q.weight" in str(exc.value)


# Tier 2 -- the real checkpoint (no NPU), gated on its presence
# ##########################################################################

weights_dir = Path(os.environ.get("IRON_EXAMPLE_WEIGHTS_DIR", "/srv"))
real_checkpoint = weights_dir / "llama3.2-1b" / "model.safetensors"


class RealConfig:
    """The actual Llama-3.2-1B geometry, from LlamaConfig."""

    vocab_size = 128256
    emb_dim = 2048
    n_layers = 16
    n_heads = 32
    n_kv_groups = 8
    head_dim = emb_dim // n_heads  # 64
    hidden_dim = 8192


@pytest.mark.skipif(
    not real_checkpoint.exists(),
    reason=f"llama3.2-1b checkpoint not found at {real_checkpoint}",
)
def test_real_checkpoint_fills_the_tree():
    """FROM_HF matches the real key spelling -- a shaped stand-in cannot show this.

    The parameter-name set the tree exposes must be exactly the set of names
    translate_hf produces from the real checkpoint, and every parameter must be
    materialised (no name left meta because its key never matched).
    """
    weights = safetensors.torch.load_file(real_checkpoint)
    model = Llama.from_hf(RealConfig, weights)

    tree_names = {name for name, _ in model.named_parameters()}
    expected = set(translate_hf(weights, RealConfig.n_layers))
    assert tree_names == expected

    for name, param in model.named_parameters():
        assert not param.is_meta, f"{name} never received a checkpoint tensor"


@pytest.mark.skipif(
    not real_checkpoint.exists(),
    reason=f"llama3.2-1b checkpoint not found at {real_checkpoint}",
)
def test_real_checkpoint_ties_the_output_head():
    """The real checkpoint ties out_head to embed_tokens -- one 262 M matrix."""
    weights = safetensors.torch.load_file(real_checkpoint)
    model = Llama.from_hf(RealConfig, weights)
    assert (
        model.out_head.weight.data_ptr()
        == weights["model.embed_tokens.weight"].data_ptr()
    )
