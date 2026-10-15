# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``DecoderConfig``'s partial rotary (``rotary_dim``) and global RoPE amplitude
scale (``rope_attention_scaling``), device-free: the angle table's own
shape and values, and that a traced decoder reads it at that width rather
than ``head_dim`` -- Phi-4-mini-instruct's need, exercised here without a
model of its own.
"""

import dataclasses

import numpy as np
import pytest
from ml_dtypes import bfloat16

from iron.common.graph.handle import Affine
from iron.lm import project, rope_angles
from iron.applications.llama.model import Llama
from iron.operators.rms_norm import RMSNorm
from iron.operators.rope import RoPE
from iron.tests.common.llama_model import PROFILE, SMALL, checkpoint, small

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


class _PartialRotaryLlama(Llama):
    """Llama's shape, but ``q``'s rotary prefix alone goes through RoPE: a
    plain numpy weight slice (free at trace time) stands in for the real
    per-head ``q_rot``/``q_pass`` split a partial-rotary model's own layer
    makes, enough to exercise the shared decoder's narrower angle table
    without a whole model package of its own.
    """

    def layer(self, step, i, w, x):
        c, n = self.config, x.shape[0]
        H, D, A = c.n_heads, c.head_dim, c.rope_width
        h = RMSNorm.step(x, weight=w.input_layernorm.weight)
        q = w.self_attn.q_proj.weight
        q_rot_weight = q.reshape(H, D, c.emb_dim)[:, :A, :].reshape(H * A, c.emb_dim)
        q_rot = project(h, q_rot_weight)
        RoPE.step(q_rot.reshape(n * H, A), step.angles)
        return x


def _partial_rotary_small(**config):
    cfg = dataclasses.replace(SMALL, **config)
    model = _PartialRotaryLlama(cfg, checkpoint(cfg).tree("random"))
    model.profile = PROFILE
    return model


def test_rope_width_defaults_to_head_dim():
    cfg = small().config
    assert cfg.rotary_dim is None
    assert cfg.rope_width == cfg.head_dim
    assert cfg.angles().shape == (cfg.max_seq_len, cfg.head_dim)


def test_rope_width_is_the_rotary_dim_when_given():
    model = small(rotary_dim=32)
    cfg = model.config
    assert cfg.rope_width == 32
    assert cfg.angles().shape == (cfg.max_seq_len, 32)
    # Every other weight keeps the full head_dim: only the angle table narrows.
    q = model.layers[0].self_attn.q_proj.weight
    assert q.shape == (cfg.n_heads * cfg.head_dim, cfg.emb_dim)


def test_angles_are_the_unscaled_table_at_rope_width():
    cfg = small(rotary_dim=32).config
    expected = rope_angles(32, cfg.max_seq_len, cfg.rope_base, cfg.rope_scaling)
    np.testing.assert_array_equal(cfg.angles(), expected.astype(np.float32))


def test_attention_scaling_multiplies_the_whole_table_once():
    cfg = small(rotary_dim=32, rope_attention_scaling=1.25).config
    unscaled = rope_angles(32, cfg.max_seq_len, cfg.rope_base, cfg.rope_scaling)
    np.testing.assert_allclose(cfg.angles(), unscaled * np.float32(1.25), rtol=1e-6)


def test_attention_scaling_of_one_leaves_llama_unchanged():
    # Every existing full-rotary model takes this path: rope_width ==
    # head_dim and the table is bitwise what rope_angles alone gives.
    cfg = small().config
    assert cfg.rope_attention_scaling == 1.0
    np.testing.assert_array_equal(
        cfg.angles(),
        rope_angles(cfg.head_dim, cfg.max_seq_len, cfg.rope_base, cfg.rope_scaling),
    )


def test_decode_step_reads_the_rope_table_at_its_own_width():
    model = _partial_rotary_small(rotary_dim=32)
    cfg = model.config
    t = model.trace(**model.shapes()[0])
    by_op = {id(b.op): b for b in t.bindings}
    angles = t.steps[1].op
    assert by_op[id(angles)].expression == Affine(t.values[1], 32)
    assert t.pinned["rope"] == cfg.max_seq_len * 32 * np.dtype(bfloat16).itemsize


def test_prompt_chunk_reads_the_rope_table_at_its_own_width():
    model = _partial_rotary_small(rotary_dim=32, max_seq_len=256, prefill_chunk=256)
    t = model.trace(**model.shapes()[1])
    copies = [s.op for s in t.steps if type(s.op).__name__ == "Copy"]
    angle_copy = next(c for c in copies if c.dst.sizes[-1] == 32)
    assert list(angle_copy.dst.sizes) == [256, 32]
    assert t.pinned["rope"] == 256 * 32 * np.dtype(bfloat16).itemsize
