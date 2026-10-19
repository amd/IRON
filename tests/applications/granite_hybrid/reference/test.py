#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.0-H's graph against Hugging Face's GraniteMoeHybrid in float32
over the same random weights at a toy shape, its logits recorded in
``goldens/``, device-free: the shared decoder's tests (``Decoder``), whose
prompts span several of the toy's 64-row chunks, so the Mamba2 layers'
states carry across chunk boundaries and into decode steps.
"""

import dataclasses

import numpy as np
import pytest

from iron.applications.granite_hybrid.model import GraniteHybrid, GraniteHybridConfig
from iron.tests.common.llama_reference import Decoder

#: Granite 4.0-H's proportions at toy size: three Mamba2 layers of two
#: groups and one attention layer without RoPE, a shared MLP, four experts
#: of which a token takes two, and Granite's scalars.
TOY = GraniteHybridConfig(
    vocab_size=1024,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    intermediate_size=256,
    rope_theta=10000.0,
    max_seq_len=256,
    prefill_chunk=64,
    attention_multiplier=0.0625,
    residual_multiplier=0.22,
    embedding_multiplier=12.0,
    logits_scaling=8.0,
    layer_types=("mamba", "attention", "mamba", "mamba"),
    position_embedding_type="nope",
    shared_intermediate_size=512,
    num_local_experts=4,
    num_experts_per_tok=2,
    mamba_n_heads=16,
    mamba_d_head=64,
    mamba_d_state=64,
    mamba_n_groups=2,
)


@pytest.fixture(scope="module")
def golden(golden):
    """The toy's golden, its weights first redrawn in place where the
    shared draw would leave a layer inert: each stacked expert at its own
    matrix's scale, not the whole stack's; the time steps and decays as
    Mamba2 initializes them, so a state lasts many positions; the skip
    ``D`` a tenth of the draw's, so the state carries the scan's output; and
    the convolution's bias ten times the draw's, at its taps' scale.
    """

    def recorded(name, build, config, weights):
        rng = np.random.default_rng(0)
        for layer in weights.model.layers:
            if "block_sparse_moe" in vars(layer):
                moe = layer.block_sparse_moe
                for w in (moe.input_linear.weight, moe.output_linear.weight):
                    w *= np.sqrt(w.shape[1])
            if "mamba" in vars(layer):
                m, H = layer.mamba, config.mamba_n_heads
                m.A_log[:] = np.log(rng.uniform(1, 16, H))
                dt = np.exp(rng.uniform(np.log(1e-3), np.log(1e-1), H))
                m.dt_bias[:] = dt + np.log(-np.expm1(-dt))
                m.D[:] *= 0.1
                m.conv1d.bias[:] *= 10
        return golden(name, build, config, weights)

    return recorded


class TestGraniteHybrid(Decoder):
    model, config, model_type, name = GraniteHybrid, TOY, "granitemoehybrid", "toy"
    json = {"mamba_expand": 2}
    seed = 0

    @classmethod
    def names(cls):
        c = cls.config
        E, D = c.hidden_size, c.head_dim
        S, M = c.shared_intermediate_size, c.intermediate_size
        X, H, N = c.num_local_experts, c.mamba_n_heads, c.mamba_d_state
        I = H * c.mamba_d_head
        channels = I + 2 * c.mamba_n_groups * N
        out = {
            "model.embed_tokens.weight": (c.vocab_size, E),
            "model.norm.weight": (E,),
        }
        for i in range(c.num_hidden_layers):
            p = f"model.layers.{i}"
            out |= {
                f"{p}.input_layernorm.weight": (E,),
                f"{p}.post_attention_layernorm.weight": (E,),
                f"{p}.shared_mlp.input_linear.weight": (2 * S, E),
                f"{p}.shared_mlp.output_linear.weight": (E, S),
                f"{p}.block_sparse_moe.router.layer.weight": (X, E),
                f"{p}.block_sparse_moe.input_linear.weight": (X, 2 * M, E),
                f"{p}.block_sparse_moe.output_linear.weight": (X, E, M),
            }
            if c.attends(i):
                Q, KV = c.num_attention_heads * D, c.num_key_value_heads * D
                out |= {
                    f"{p}.self_attn.q_proj.weight": (Q, E),
                    f"{p}.self_attn.k_proj.weight": (KV, E),
                    f"{p}.self_attn.v_proj.weight": (KV, E),
                    f"{p}.self_attn.o_proj.weight": (E, Q),
                }
            else:
                m = f"{p}.mamba"
                out |= {
                    f"{m}.in_proj.weight": (I + channels + H, E),
                    f"{m}.conv1d.weight": (channels, 1, c.mamba_d_conv),
                    f"{m}.conv1d.bias": (channels,),
                    f"{m}.dt_bias": (H,),
                    f"{m}.A_log": (H,),
                    f"{m}.D": (H,),
                    f"{m}.norm.weight": (I,),
                    f"{m}.out_proj.weight": (E, I),
                }
        return out


class TestGraniteHybridDense(TestGraniteHybrid):
    """Granite 4.0-H 1B's kind: no experts, the shared MLP alone."""

    config, name = dataclasses.replace(TOY, num_local_experts=0), "dense"

    @classmethod
    def names(cls):
        return {k: v for k, v in super().names().items() if "block_sparse_moe" not in k}


def test_layer_types_short_of_the_layers_are_refused():
    with pytest.raises(ValueError, match="3 layer_types for 4 layers"):
        dataclasses.replace(TOY, layer_types=TOY.layer_types[:3])
