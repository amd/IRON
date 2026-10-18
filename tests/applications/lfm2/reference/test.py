#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2's graph against Hugging Face's LFM2 in float32 over the same random
weights, its logits recorded in ``goldens/``, device-free (no checkpoint,
no NPU): the short convolution's rows before a call, carried as a
``Checkpoints`` state across prompt chunks, decode steps and a chat turn
from a boundary a decode step crossed.
"""

import aie.utils as aie_utils
import numpy as np
import pytest

from iron.applications.lfm2.model import Lfm2, Lfm2Config
from iron.lm import OnHost as Host
from iron.lm.testing import assert_close
from iron.tests.common.llama_reference import Decoder
from iron.tests.toolchain.tools import DEVICES

pytestmark = pytest.mark.usefixtures("npu2")

#: LFM2-1.2B's proportions at toy size: two conv layers, two attending.
TOY = Lfm2Config(
    vocab_size=512,
    hidden_size=512,
    num_hidden_layers=4,
    num_attention_heads=8,
    num_key_value_heads=2,
    head_dim=64,
    rope_theta=1e6,
    max_seq_len=1024,
    prefill_chunk=256,
    block_ff_dim=1024,
    full_attn_idxs=(1, 3),
)
# Two chunks, the second short, then decode steps across the next boundary.
PROMPT, LAST = 500, 514


def names(c: Lfm2Config) -> dict[str, tuple[int, ...]]:
    """Each tensor of an LFM2 checkpoint of ``c``'s shape, by name."""
    E, F, D, K = c.hidden_size, c.intermediate_size, c.head_dim, c.conv_kernel
    Q, KV = c.num_attention_heads * D, c.num_key_value_heads * D
    out = {
        "model.embed_tokens.weight": (c.vocab_size, E),
        "model.embedding_norm.weight": (E,),
    }
    for i in range(c.num_hidden_layers):
        p = f"model.layers.{i}"
        out |= {
            f"{p}.operator_norm.weight": (E,),
            f"{p}.ffn_norm.weight": (E,),
            f"{p}.feed_forward.w1.weight": (F, E),
            f"{p}.feed_forward.w3.weight": (F, E),
            f"{p}.feed_forward.w2.weight": (E, F),
        }
        if i in c.full_attn_idxs:
            out |= {
                f"{p}.self_attn.q_proj.weight": (Q, E),
                f"{p}.self_attn.k_proj.weight": (KV, E),
                f"{p}.self_attn.v_proj.weight": (KV, E),
                f"{p}.self_attn.out_proj.weight": (E, Q),
                f"{p}.self_attn.q_layernorm.weight": (D,),
                f"{p}.self_attn.k_layernorm.weight": (D,),
            }
        else:
            out |= {
                f"{p}.conv.in_proj.weight": (3 * E, E),
                f"{p}.conv.conv.weight": (E, 1, K),
                f"{p}.conv.out_proj.weight": (E, E),
            }
    return out


class TestLfm2(Decoder):
    model, config, model_type, name = Lfm2, TOY, "lfm2", "toy"

    @classmethod
    def names(cls):
        return names(cls.config)


class OnHost(Host, Lfm2):
    profile = None


def _assert_close(model, reference, tokens):
    """The model's logits after ``tokens`` against the reference's
    (``assert_close``; this toy measures at most 2.2%, a turn reading a
    stale slot 124%): the reference's.
    """
    want = reference.logits(tokens)
    assert_close(model.logits(tokens), want, f"{len(tokens)} tokens")
    return want


@pytest.fixture(scope="module")
def toy(golden):
    """The toy's random weights and their golden logits."""
    case = TestLfm2.case(golden)
    return case.weights, case.golden


@pytest.fixture(scope="module")
def ran(toy):
    """The model after a prompt of two chunks and decode steps across the
    next boundary, each call held to the reference, and the tokens it ran.
    It binds the device itself, being set up before the tests' ``npu2``.
    """
    weights, reference = toy
    model = OnHost(TOY, weights)
    # No greedy step of this prompt has a top-2 gap within bf16's resolution.
    tokens = list(np.random.default_rng(27).integers(0, TOY.vocab_size, PROMPT))
    with aie_utils.set_current_device(DEVICES["npu2"]()):
        while len(tokens) <= LAST:
            tokens.append(int(_assert_close(model, reference, tokens).argmax()))
    return model, reference, tokens


def test_attention_layers_hold_caches_and_conv_layers_a_checkpointed_tail(ran):
    model, _, _ = ran
    C, K, E = TOY.prefill_chunk, TOY.conv_kernel, TOY.hidden_size
    assert list(model.caches) == [1, 3]
    assert list(model.recurrent) == [0, 2]
    slots = (TOY.max_seq_len - 1) // C + 2
    for states in model.recurrent.values():
        assert states["conv"].slots.shape == (slots, K - 1, E)


def test_a_turn_resumes_from_a_boundary(ran):
    """A one-token turn from a boundary, whose first position convolves over
    the rows before it, then a decode step: first from the slot the decode
    step crossing 512 wrote, then from the one the prompt's first chunk
    wrote.
    """
    model, reference, tokens = ran
    for boundary in (512, 256):
        turn = tokens[:boundary] + [int(np.random.default_rng(boundary).integers(512))]
        turn.append(int(_assert_close(model, reference, turn).argmax()))
        _assert_close(model, reference, turn)


def test_a_turn_resumes_where_its_state_is_held(toy):
    """Decision 50 with recurrent state: an appended turn resumes at its
    first new token, the state where the last call ended; a turn changing
    a token mid-chunk resumes at the boundary before it. A call never
    crosses a boundary, so each writes its slot; every turn is the
    reference's.
    """
    weights, reference = toy
    model = OnHost(TOY, weights)
    rng = np.random.default_rng(3)
    tokens = list(rng.integers(0, TOY.vocab_size, 500))
    _assert_close(model, reference, tokens)
    for turn, start, calls in (
        (tokens + list(rng.integers(0, 512, 30)), 500, [(500, 12), (512, 18)]),
        (tokens[:280] + list(rng.integers(0, 512, 1)), 256, [(256, 25)]),
        (tokens[:280] + list(rng.integers(0, 512, 300)), 256, [(256, 256), (512, 68)]),
    ):
        turn = np.array(turn)
        assert model.resume(model._held(turn)) == start
        got = [(v["start"], v["rows"]) for _, v in model._chunks(turn, start)]
        assert got == calls
        _assert_close(model, reference, list(turn))
