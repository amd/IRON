# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Layer-by-layer attention against an independent, stage-rounded reference."""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.dialects.aie import AIEArch
from aie.utils.benchmark import run_iters
from ml_dtypes import bfloat16

from iron.common.declare import Profile
from iron.common.graph.compiled import _step_words
from iron.common.image.packaging import plan
from iron.lm import AttentionPrefillFused, AttentionPrefillProjectedFused
from iron.operators.gemm import GEMM
from iron.operators.softmax import Softmax
from iron.tests.support.lowering import lower
from iron.tests.support.tools import requires


def _profile(dev):
    profile = Profile()
    profile.add(GEMM, tile_m=16, tile_k=64, tile_n=64)
    profile.add(GEMM, N=64, tile_n=16)
    profile.add(GEMM, N=128, tile_n=32 if dev.arch is AIEArch.AIE2 else 16)
    if dev.arch is AIEArch.AIE2p:
        profile.add(GEMM, N=256, tile_n=32)
    for n in (192, 384, 768, 1536, 3072):
        profile.add(GEMM, N=n, tile_n=48)
    profile.add(Softmax, num_channels=4)
    return profile


def _draw(rng, shape, scale=0.5):
    return (rng.standard_normal(shape) * scale).astype(bfloat16)


def _matmul(a, b):
    return (a.astype(np.float32) @ b.astype(np.float32)).astype(bfloat16)


def _attention(q, k, v, causal):
    h, s, d = q.shape
    groups = np.arange(h) // (h // k.shape[0])
    scores = _matmul(q, k[groups].transpose(0, 2, 1))
    scores = (
        (scores.astype(np.float32) / np.sqrt(d)).astype(bfloat16).astype(np.float32)
    )
    if causal:
        scores = np.where(
            np.arange(s)[None, :] > np.arange(s)[:, None], -np.inf, scores
        )
    weights = np.exp(scores - scores.max(axis=-1, keepdims=True))
    weights = (weights / weights.sum(axis=-1, keepdims=True)).astype(bfloat16)
    return _matmul(weights, v[groups])


def _rope(x, angles, heads):
    s, d = angles.shape
    x = x.reshape(s, heads, d).astype(np.float32)
    cos, sin = (angles[:, None, offset::2].astype(np.float32) for offset in (0, 1))
    a, b = np.split(x, 2, axis=-1)
    return np.concatenate((a * cos - b * sin, b * cos + a * sin), axis=-1).astype(
        bfloat16
    )


def _case(projected, *, h=2, g=1, s=1536, causal=True, seed=0):
    d, e = 64, 256
    rng = np.random.default_rng(seed)
    if not projected:
        inputs = dict(
            queries=_draw(rng, (h, s, d)),
            keys=_draw(rng, (g, s, d)),
            values=_draw(rng, (g, s, d)),
        )
        expected = _attention(*inputs.values(), causal)
        return AttentionPrefillFused(h, g, d, e, s, causal), inputs, expected
    angles = rng.uniform(-np.pi, np.pi, (s, d // 2))
    table = np.empty((s, d), dtype=bfloat16)
    table[:, ::2], table[:, 1::2] = np.cos(angles), np.sin(angles)
    inputs = dict(
        x=_draw(rng, (s, e)),
        rope_angles=table,
        w_query=_draw(rng, (e, h * d), 1 / np.sqrt(e)),
        w_key=_draw(rng, (e, g * d), 1 / np.sqrt(e)),
        w_value=_draw(rng, (e, g * d), 1 / np.sqrt(e)),
        w_output=_draw(rng, (h * d, e), 1 / np.sqrt(h * d)),
    )
    q = _rope(_matmul(inputs["x"], inputs["w_query"]), table, h).transpose(1, 0, 2)
    k = _rope(_matmul(inputs["x"], inputs["w_key"]), table, g).transpose(1, 0, 2)
    v = _matmul(inputs["x"], inputs["w_value"]).reshape(s, g, d).transpose(1, 0, 2)
    context = _attention(q, k, v, causal).transpose(1, 0, 2).reshape(s, h * d)
    expected = _matmul(context, inputs["w_output"])
    return AttentionPrefillProjectedFused(h, g, d, e, s, causal), inputs, expected


def _check(actual, expected, *, device=False):
    actual = np.asarray(actual).reshape(expected.shape).astype(np.float32)
    expected = expected.astype(np.float32)
    assert np.isfinite(actual).all()
    # The original BFP/approximate-softmax path measured up to 0.0352
    # absolute error on these 0.5-scale inputs. Keep its 8% relative
    # allowance, with a tighter absolute bound than the old tests' 2.0.
    # A norm check prevents that absolute allowance hiding small outputs.
    if device:
        assert np.linalg.norm(actual - expected) <= 0.08 * np.linalg.norm(expected)
    np.testing.assert_allclose(
        actual,
        expected,
        atol=0.04 if device else 0.008,
        rtol=0.08 if device else 0.04,
    )


@pytest.mark.parametrize("device", ["npu1", "npu2"])
@pytest.mark.parametrize("projected", [False, True], ids=["core", "projected"])
@pytest.mark.parametrize("causal", [False, True], ids=["unmasked", "causal"])
@pytest.mark.parametrize("g", [1, 2], ids=["gqa", "mha"])
def test_reference(request, device, projected, causal, g):
    request.getfixturevalue(device)
    op, inputs, expected = _case(projected, g=g, causal=causal)
    _check(op.reference(*inputs.values()), expected)


@pytest.mark.parametrize("s", [8192, 32768])
@pytest.mark.parametrize("causal", [False, True])
@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_long_rows_reuse_scratch_and_stream_softmax(request, device, s, causal):
    dev = request.getfixturevalue(device)
    op = AttentionPrefillFused(2, 1, 64, 256, s, causal)
    rec = op.record(queries=(2, s, 64), keys=(1, s, 64), values=(1, s, 64))
    gemms = [step.op for step in rec.steps if isinstance(step.op, GEMM)]
    assert all(gemm.M == op.block_rows for gemm in gemms)
    softmax = [
        step.op.resolved(dev) for step in rec.steps if isinstance(step.op, Softmax)
    ]
    assert softmax[-1].streamed and softmax[-1].cols == s
    assert all(sm.rows // sm.cores <= 48 for sm in softmax if sm.streamed)
    assert rec.pinned["scores"] == 2 * op.num_heads * op.block_rows * s
    # No block leaves a private, pinned score matrix behind. All other
    # pinned tensors are inputs, the output state or shared constants.
    assert set(rec.pinned) == {
        "scores",
        "attn_context",
        "queries",
        "keys",
        "values",
        *(handle.name for _, handle in rec.weights.values()),
    }
    if causal:
        assert op.mask.shape == (op.num_heads, op.block_rows, op.block_rows)
    chosen = plan(dev, rec, step_words=_step_words(rec))
    assert not chosen.commands


@pytest.mark.parametrize(
    "h,g,e", [(32, 8, 2048), (12, 12, 768)], ids=["llama-1b", "gpt2"]
)
def test_projected_model_shapes_resolve(npu2, h, g, e):
    op = AttentionPrefillProjectedFused(h, g, 64, e, 256)
    rec = op.record(
        x=(256, e),
        rope_angles=(256, 64),
        w_query=(e, h * 64),
        w_key=(e, g * 64),
        w_value=(e, g * 64),
        w_output=(h * 64, e),
    )
    assert rec.outputs[0].shape == (256, e)
    chosen = plan(npu2, rec, full_elf=True, step_words=_step_words(rec))
    assert not chosen.commands


@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_profile_reaches_nested_attention(request, device):
    dev = request.getfixturevalue(device)
    op, inputs, _ = _case(True)
    op.profile = Profile()
    op.profile.add(GEMM, tile_m=32, tile_k=64, tile_n=16)
    op.profile.add(Softmax, num_channels=2)
    rec = op.record(**{n: a.shape for n, a in inputs.items()})
    gemms = [s.op.resolved(dev) for s in rec.steps if isinstance(s.op, GEMM)]
    assert all(gemm.tile_m == 32 and gemm.tile_n == 16 for gemm in gemms)
    softmax = [s.op for s in rec.steps if isinstance(s.op, Softmax)]
    assert softmax and all(sm.num_channels == 2 for sm in softmax)


@pytest.mark.parametrize(
    "kwargs,match",
    [
        ({"num_heads": 0}, "num_kv_groups"),
        ({"num_kv_groups": 3}, "num_kv_groups"),
        ({"head_dim": 128}, "head_dim"),
        ({"seq_len": 384}, "seq_len"),
        ({"embedding_dim": 31}, "embedding_dim"),
    ],
)
def test_rejected_dimensions(kwargs, match):
    args = dict(
        num_heads=2, num_kv_groups=1, head_dim=64, embedding_dim=256, seq_len=512
    )
    with pytest.raises(ValueError, match=match):
        AttentionPrefillFused(**(args | kwargs))


def test_input_layout_is_checked(npu2):
    op = AttentionPrefillFused(2, 1, 64, 256, 512)
    with pytest.raises(ValueError, match="expected queries"):
        op.record(queries=(2, 512, 64), keys=(1, 64, 512), values=(1, 512, 64))


@requires("aiecc", "peano", "aiebu")
@pytest.mark.parametrize("projected", [False, True], ids=["core", "projected"])
def test_compiles_to_one_full_elf(npu2, projected):
    op, inputs, _ = _case(projected)
    compiled = op.compile(full_elf=True, **{n: a.shape for n, a in inputs.items()})
    assert compiled.plan.full_elf
    assert not compiled.plan.commands


@requires("aiecc", "peano")
@pytest.mark.parametrize("device", ["npu1", "npu2"])
def test_long_context_stages_lower(request, device, tmp_path):
    dev = request.getfixturevalue(device)
    s = 32768
    op = AttentionPrefillFused(1, 1, 64, 256, s)
    rec = op.record(queries=(1, s, 64), keys=(1, s, 64), values=(1, s, 64))
    # The last query block exercises the widest scores and both strided
    # diagonal-mask copies, as well as streamed softmax and scale.
    last_score = max(
        i
        for i, step in enumerate(rec.steps)
        if isinstance(step.op, GEMM) and step.op.K == 64
    )
    unique = {step.op.design_key(): step.op for step in rec.steps[last_score:]}
    for i, stage in enumerate(unique.values()):
        path = tmp_path / str(i)
        path.mkdir()
        lower(stage.resolved(dev), path)


@pytest.mark.bench
@pytest.mark.parametrize("tuned", [False, True], ids=["defaults", "profile"])
@pytest.mark.parametrize("causal", [False, True], ids=["unmasked", "causal"])
@pytest.mark.parametrize("projected", [False, True], ids=["core", "projected"])
@pytest.mark.parametrize(
    "full_elf",
    [
        pytest.param(False, marks=pytest.mark.supported_devices("npu1", "npu2")),
        pytest.param(True, marks=pytest.mark.supported_devices("npu2")),
    ],
    ids=["separate", "single"],
)
def test_dispatch(projected, full_elf, causal, tuned, record_property):
    op, inputs, expected = _case(projected, causal=causal)
    if tuned:
        op.profile = _profile(aie_utils.get_current_device())
    compiled = op.compile(full_elf=full_elf, **{n: a.shape for n, a in inputs.items()})
    try:
        actual = compiled(*inputs.values())
        _check(actual, expected, device=True)
        # Reusing the scratch on another call must not retain the previous
        # head or block, nor stale host copies from the first dispatch.
        _, again, expected_again = _case(projected, causal=causal, seed=1)
        _check(compiled(*again.values()), expected_again, device=True)
        # Graph.__call__ returns tensors, whereas its loaded callable returns
        # the dispatch timing. Per-step dispatch has no empty-command timing
        # to subtract, so report submit-to-completion in both modes.
        timing = run_iters(compiled.callable, warmup=3, iters=20).dispatch
        assert timing is not None
        record_property("Latency", timing.median_us)
        record_property("Latency MAD", timing.mad_us)
    finally:
        op.release()


@pytest.mark.supported_devices("npu1", "npu2")
def test_long_context_dispatch_without_profile():
    op, inputs, expected = _case(False, h=1, s=4608)
    try:
        _check(op(*inputs.values()), expected, device=True)
    finally:
        op.release()
