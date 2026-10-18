# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``DecoderConfig``'s partial rotary (``rotary_dim``) and RoPE amplitude
scale (``rope_attention_scaling``), device-free, and a ``max_seq_len`` no
prompt chunk divides.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.graph.handle import Affine
import iron.functional as F
from iron.lm import rope_angles
from iron.applications.llama.model import Llama
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint, small

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


class _PartialRotaryLlama(Llama):
    """Llama's shape, but only ``q``'s rotary prefix goes through RoPE."""

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, D, A = c.num_attention_heads, c.head_dim, c.rope_width
        h = RMSNorm.step(x, weight=w.input_layernorm.weight)
        q = w.self_attn.q_proj.weight
        q_rot_weight = q.reshape(H, D, c.hidden_size)[:, :A, :].reshape(
            H * A, c.hidden_size
        )
        q_rot = F.linear(h, q_rot_weight)
        RoPE.step(q_rot.reshape(n * H, A), step.angles)
        return x


def _partial_rotary_small(**config):
    cfg = dataclasses.replace(SMALL, **config)
    model = _PartialRotaryLlama(cfg, checkpoint(cfg).tree("random"))
    model.profile = PROFILE
    return model


def test_rope_width_is_the_rotary_dim_when_given():
    model = small(rotary_dim=32)
    cfg = model.config
    assert cfg.rope_width == 32
    assert cfg.angles().shape == (cfg.max_seq_len, 32)
    # Every other weight keeps the full head_dim: only the angle table narrows.
    q = model.layers[0].self_attn.q_proj.weight
    assert q.shape == (cfg.num_attention_heads * cfg.head_dim, cfg.hidden_size)


def test_angles_are_the_unscaled_table_at_rope_width():
    cfg = small(rotary_dim=32).config
    expected = rope_angles(32, cfg.max_seq_len, cfg.rope_theta, cfg.rope_scaling)
    np.testing.assert_array_equal(cfg.angles(), expected.astype(np.float32))


def test_attention_scaling_multiplies_the_whole_table_once():
    cfg = small(rotary_dim=32, rope_attention_scaling=1.25).config
    unscaled = rope_angles(32, cfg.max_seq_len, cfg.rope_theta, cfg.rope_scaling)
    np.testing.assert_allclose(cfg.angles(), unscaled * np.float32(1.25), rtol=1e-6)


def test_by_default_the_table_is_rope_angles_at_head_dim():
    cfg = small().config
    assert cfg.rotary_dim is None and cfg.rope_width == cfg.head_dim
    assert cfg.rope_attention_scaling == 1.0
    np.testing.assert_array_equal(
        cfg.angles(),
        rope_angles(cfg.head_dim, cfg.max_seq_len, cfg.rope_theta, cfg.rope_scaling),
    )


def test_decode_step_reads_the_rope_table_at_its_own_width():
    model = _partial_rotary_small(rotary_dim=32)
    cfg = model.config
    t = model.trace(**model.shapes()[0])
    by_op = {id(b.op): b for b in t.bindings}
    angles = t.steps[1].op
    assert by_op[id(angles)].expression == Affine(t.values[1], 32)
    assert (
        t.pinned["rotary_emb.table"]
        == cfg.max_seq_len * 32 * np.dtype(bfloat16).itemsize
    )


def test_prompt_chunk_reads_the_rope_table_at_its_own_width():
    model = _partial_rotary_small(rotary_dim=32, max_seq_len=256, prefill_chunk=256)
    t = model.trace(**model.shapes()[1])
    copies = [s.op for s in t.steps if type(s.op).__name__ == "Copy"]
    angle_copy = next(c for c in copies if c.dst.sizes[-1] == 32)
    assert list(angle_copy.dst.sizes) == [256, 32]
    assert t.pinned["rotary_emb.table"] == 256 * 32 * np.dtype(bfloat16).itemsize


def test_a_context_no_chunk_divides_is_allocated_exactly():
    """LFM2's 128000 positions in 2048-row chunks, small: the caches, the
    angle table and the draws hold a row a position, and no call goes past
    the last position.
    """
    model = small(max_seq_len=300)
    cfg = model.config
    assert cfg.angles().shape == (300, cfg.head_dim)
    t = model.trace(**model.shapes()[1])
    row = cfg.num_key_value_heads * cfg.head_dim * np.dtype(bfloat16).itemsize
    layers = "model.layers.0.cache.keys", "model.layers.1.cache.values"
    assert t.pinned[layers[0]] == t.pinned[layers[1]] == 300 * row
    assert t.pinned["drawn"] == 300 * np.dtype(np.int32).itemsize
    with pytest.raises(ValueError, match="301 tokens do not fit 300 rows"):
        model.logits(np.zeros(301, np.int64))


@pytest.mark.parametrize(
    "chunk,rows,inside", [(1, 44, True), (1, 45, False), (0, 256, True), (2, 1, False)]
)
def test_a_prompt_chunk_past_the_last_position_is_refused(chunk, rows, inside):
    """Every limit a prompt chunk's trace records holds where its rows end
    by position 300, and one fails where they pass it, so the call is
    refused before it is dispatched.
    """
    model = small(max_seq_len=300)
    t = model.trace(**model.shapes()[1])
    values = dict(
        start=chunk * 256,
        rope_start=chunk * 256,
        rows=rows,
        position=chunk * 256 + rows - 1,
        token=0,
    )
    held = [limit.lo <= limit.evaluate(values) < limit.hi for limit in t.limits]
    assert all(held) == inside
    joint = [str(limit) for limit in t.limits if limit.plus is not None]
    assert joint and all(s == "start + rows" for s in joint)
