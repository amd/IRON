# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Which folds the tuner proposes (``iron.tune.fold``), scoped to the ones
that do not split a device array a call site sharing it does not also take.
No device, no toolchain: recording and bookkeeping only.
"""

import aie.utils as aie_utils
import pytest
from aie.iron.device import NPU2

from iron.common.declare import Profile
from iron.common.graph.fold import apply_folds, fold_candidates
from iron.common.image.step import FusionKind
from iron.operators.gemv import GEMV
from iron.tests.support.llama_model import llama_1b
from iron.tune.autotune import Timed
from iron.tune.fold import array_scoped_fold_candidates, fold_profile, propose_folds


def _kinds(recording, fusion) -> tuple[str, ...]:
    return tuple(type(recording.steps[i].op.resolved()).__name__ for i in fusion.steps)


@pytest.fixture(scope="module")
def decode():
    """Llama 3.2 1B's real decode step, device-free, bound for every test
    in this module (``npu2`` is function-scoped, so a module-scoped fixture
    binds its own device rather than taking it).
    """
    with aie_utils.set_current_device(NPU2()):
        model = llama_1b(num_hidden_layers=16)
        decode_shape, _ = model.shapes()
        yield model.record(**decode_shape)


def test_array_scoping_drops_o_proj_and_keeps_down_proj_and_silu(decode):
    """``fold_candidates`` finds 48: o_proj's and down_proj's own residual
    add (32, one ``GEMV`` each), and SwiGLU's gate (16, ``SiLU``). o_proj
    shares its ``GEMV M=2048 K=2048`` array with q_proj, which never folds
    (nothing follows it but RoPE); down_proj's own ``GEMV M=2048 K=8192`` is
    not shared with anything, and every one of SiLU's 16 calls folds alike,
    so only those 32 survive scoping.
    """
    every = fold_candidates(decode)
    assert len(every) == 48

    scoped = array_scoped_fold_candidates(decode)
    kinds = sorted(_kinds(decode, f) for f in scoped)
    gemv_adds = [f for f in scoped if _kinds(decode, f) == ("GEMV", "ElementwiseAdd")]
    assert len(gemv_adds) == 16
    assert kinds.count(("SiLU", "ElementwiseMul")) == 16
    assert len(scoped) == 32

    kept_producers = {decode.steps[f.steps[0]].op.resolved().K for f in gemv_adds}
    assert kept_producers == {8192}, "only down_proj's own K survives, not q/o's 2048"


def test_q_and_o_still_share_one_array_after_the_scoped_folds_apply(decode):
    """Scoping exists so folding never costs an array split: after
    ``propose_folds``'s own candidates apply, q_proj and o_proj (``GEMV
    M=2048 K=2048``) are still one array, exactly as unfolded
    (``iron.tests.lm.test_modules.test_a_decode_steps_q_and_o_share_one_array``).
    """
    proposed = propose_folds(decode)
    assert len(proposed) == 32

    folded = apply_folds(decode, proposed)
    gemvs = [s.op.resolved() for s in folded.steps if isinstance(s.op, GEMV)]
    q_and_o = [g for g in gemvs if (g.M, g.K) == (2048, 2048)]
    assert len(q_and_o) == 32  # 16 layers, q_proj and o_proj each
    assert len({g.array_key() for g in q_and_o}) == 1
    assert not any(g.finish for g in q_and_o), "o_proj's own fold was scoped out"
    # down_proj's own residual add did fold: every one of its finishes is set.
    down = [g for g in gemvs if (g.M, g.K) == (2048, 8192)]
    assert len(down) == 16
    assert all(g.finish for g in down)


def test_propose_folds_excludes_the_fragmenting_candidate(decode):
    """``propose_folds`` on the unscoped candidates never proposes o_proj's
    own residual add: every candidate it returns is one ``array_scoped_fold_
    candidates`` also returns.
    """
    proposed = set(propose_folds(decode))
    scoped = set(array_scoped_fold_candidates(decode))
    assert proposed <= scoped
    all_kinds = [_kinds(decode, f) for f in proposed]
    assert ("GEMV", "ElementwiseAdd") in all_kinds
    assert ("SiLU", "ElementwiseMul") in all_kinds


def test_fold_profile_writes_down_projs_add_and_silus_mul_by_shape(decode):
    """``fold_profile`` adds one fold entry a layer-specific ``down_proj``
    GEMV matches (``K=8192``), none a ``q_proj``/``o_proj`` one (``K=2048``)
    matches, and one for ``SiLU``, each scoped to the one version it was
    found in (``decode``'s own); it leaves ``base``'s own entries alone.
    """
    base = Profile()
    base.add(GEMV, M=2048, K=2048, tile_size_input=4, tile_size_output=256)
    out = fold_profile(base, [Timed(decode)])

    assert list(out) == list(base)  # the one tunable entry survives, unchanged
    fusions = out.fusions()
    kinds = sorted(
        (kind.value, tuple(c.__name__ for c, _, _ in steps))
        for kind, steps, _, _ in fusions
    )
    assert kinds == [
        (FusionKind.FOLD.value, ("GEMV", "ElementwiseAdd")),
        (FusionKind.FOLD.value, ("SiLU", "ElementwiseMul")),
    ]
    assert all(versions == frozenset({decode.version}) for *_, versions in fusions)
    (gemv_fold,) = (
        steps
        for kind, steps, _, _ in fusions
        if kind is FusionKind.FOLD and steps[0][0] is GEMV
    )
    assert gemv_fold[0][1]["K"] == 8192, "down_proj's own K, not q/o's 2048"


def test_fold_profile_is_idempotent_given_its_own_output(decode):
    """Running ``fold_profile`` again over what it just wrote adds nothing
    new: the same 32 candidates propose and dedupe to the same two entries.
    """
    once = fold_profile(Profile(), [Timed(decode)])
    twice = fold_profile(once, [Timed(decode)])
    assert twice.fusions() == once.fusions()
