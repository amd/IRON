# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each catalog operator's judgement, device-free: its first default case's
oracle output passes its ``tolerance()``, and an output past it, a NaN or its
halves swapped fail, as a device test, check mode and the tuner judge them."""

import aie.utils as aie_utils
import ml_dtypes
import numpy as np
import pytest
from aie.iron.device import from_name
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

from iron.common import Elementwise, Unresolvable
from iron.common.testing import vectors
from iron.tests.support.declared import declared, unresolvable
from iron.tests.support.judging import interval


def test_every_declared_case_resolves_on_npu2():
    """A sizing change that leaves a case unresolvable would otherwise only
    skip its device test.
    """
    dev = from_name("npu2", n_cols=8)
    reasons = [(n, c.label, unresolvable(cls, c, dev)) for n, cls, c in declared(dev)]
    assert not [r for r in reasons if r[2]]


def test_npu1_runs_every_case_of_an_operator_it_runs():
    """A case wider than npu1 would only skip there; an operator npu1 cannot
    run at all (an AIE2P-only kernel) refuses every case.
    """
    dev = from_name("npu1", n_cols=4)
    reasons: dict[str, list] = {}
    for name, cls, case in declared(dev):
        reasons.setdefault(name, []).append((case.label, unresolvable(cls, case, dev)))
    partial = {
        name: [r for r in found if r[1]]
        for name, found in reasons.items()
        if any(r for _, r in found) and not all(r for _, r in found)
    }
    assert not partial


def _cases():
    first = {}
    # Every case resolves on npu2 (test_every_declared_case_resolves_on_npu2).
    for name, cls, case in declared(from_name("npu2", n_cols=8)):
        # A bench case's inputs are large on purpose; judging one took 335 s.
        if not case.extensive and not case.bench:
            first.setdefault(name, (cls, case))
    return [
        pytest.param(cls, case, id=f"{name}-{case.label}")
        for name, (cls, case) in first.items()
    ]


CASES = _cases()


def test_the_cases_judge_by_every_kind_of_tolerance(npu2):
    ops = [cls(**case.kwargs).resolved(npu2) for cls, case in (p.values for p in CASES)]
    assert {op.tolerance().kind for op in ops} >= {"exact", "ulps", "relative", "bound"}
    assert any(
        isinstance(op, Elementwise) and len(op.chain()) == 1 for op in ops
    ), "no case is judged by its elementwise kernel's own judge"


@pytest.mark.parametrize("cls,case", CASES)
def test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance(
    npu2, cls, case
):
    op = cls(**case.kwargs).resolved(npu2)
    draw = cls.test.draw
    v = vectors(op, **(draw(op) if draw is not None else {}))
    tolerance = op.tolerance()
    verdicts = op.judge(v.inputs, v.outputs, tolerance)
    assert all(verdicts.values()), {n: x.detail for n, x in verdicts.items() if not x}
    args = tuple(v.inputs[b.name] for b in op.inputs)
    for out in op.outputs:
        want = np.asarray(v.outputs[out.name])
        flat = want.reshape(-1)
        finite = np.flatnonzero(np.isfinite(flat.astype(np.float64)))
        # One element more than the tolerance lets miss.
        n = int(tolerance.max_mismatch_frac * flat.size) + 1
        moved = finite[np.linspace(0, finite.size - 1, n).astype(int)]
        lo, hi = interval(tolerance, [flat.astype(np.float64)], [args], flat.dtype)
        past = flat.copy()
        wrong = {"past its tolerance": past}
        if np.issubdtype(flat.dtype, np.integer):
            top = hi[moved] < np.iinfo(flat.dtype).max
            past[moved] = np.where(top, hi[moved] + 1, lo[moved] - 1)
        else:
            up = np.asarray(np.inf, flat.dtype)
            past[moved] = np.nextafter(hi[moved].astype(flat.dtype), up)
            wrong["a NaN"] = flat.copy()
            wrong["a NaN"][moved[0]] = np.nan
        swapped = np.roll(flat, flat.size // 2)
        # A swap that leaves the output as it was (a word of one repeated value) is no wrong output.
        if not np.array_equal(swapped, flat, equal_nan=True):
            wrong["its halves swapped"] = swapped
        for what, w in wrong.items():
            written = {**v.outputs, out.name: w.reshape(want.shape)}
            verdict = op.judge(v.inputs, written, tolerance)[out.name]
            assert not verdict, f"{out.name} with {what} passed {tolerance}"


@pytest.mark.parametrize("device", [("npu1", 4), ("npu2", 8)], ids=["npu1", "npu2"])
def test_every_tolerance_says_where_its_numbers_come_from(device):
    # An exact one has no number to explain; None is unbounded, and says so.
    dev = from_name(device[0], n_cols=device[1])
    unnoted = set()
    with aie_utils.set_current_device(dev):
        for name, cls, case in declared(dev):
            try:
                op = cls(**case.kwargs).resolved(dev)
            except Unresolvable:
                continue
            tolerance = op.tolerance()
            if (
                tolerance is not None
                and tolerance.kind != "exact"
                and not tolerance.note
            ):
                unnoted.add(name)
    assert not unnoted, sorted(unnoted)


def _bound(x):
    return 0.01 * np.abs(x) + 1e-3


@pytest.mark.parametrize(
    "tol",
    [
        Tolerance.relative(0.04),
        Tolerance.relative(0.04, 1e-3),
        Tolerance.relative(0.04, range_frac=1e-3),
        Tolerance.bf16_ulps(2),
        Tolerance.bf16_ulps(1, atol=float(ml_dtypes.finfo(bfloat16).smallest_normal)),
        Tolerance.bounded(_bound),
        Tolerance.exact(),
    ],
    ids=[
        "relative",
        "relative_atol",
        "relative_range",
        "ulps",
        "ulps_atol",
        "bound",
        "exact",
    ],
)
def test_an_interval_is_what_compare_admits(tol):
    """The outputs a tolerance admits, as an interval: its edges pass
    ``compare``, and the next value past either fails.
    """
    rng = np.random.default_rng(0)
    x = rng.standard_normal(4096) * np.exp(rng.uniform(-8, 8, 4096))
    x = np.concatenate([x, [0.0, 0.0, 1e-40, -1e-39]])
    v = np.concatenate([x[:2048], x[2048:].astype(bfloat16).astype(np.float64)])
    lo, hi = interval(tol, [v], [(x,)], bfloat16)
    bound = dict(bound=_bound(x)) if tol.kind == "bound" else {}
    for edge, away in ((lo, -np.inf), (hi, np.inf)):
        at = edge.astype(bfloat16)
        past = np.nextafter(at, np.asarray(away, bfloat16))
        assert compare(at, v, tol, **bound).n_mismatch == 0
        assert compare(past, v, tol, **bound).n_mismatch == v.size
