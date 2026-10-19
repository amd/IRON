# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Each catalog operator's judgement, device-free: its first default case's
oracle output passes its ``tolerance()``, and an output past it, a NaN or its
halves swapped fail, as a device test, check mode and the tuner judge them."""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.iron.device import from_name

from iron.common import Elementwise
from iron.common.elementwise import _interval
from iron.common.testing import vectors
from iron.tests.support.declared import declared


def _cases():
    first = {}
    for name, cls, case, unresolvable in declared(from_name("npu2", n_cols=8)):
        if unresolvable is None and not case.extensive:
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
        lo, hi = _interval(tolerance, [flat.astype(np.float64)], [args], flat.dtype)
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
        for name, cls, case, unresolvable in declared(dev):
            if unresolvable is not None:
                continue
            tolerance = cls(**case.kwargs).resolved(dev).tolerance()
            if (
                tolerance is not None
                and tolerance.kind != "exact"
                and not tolerance.note
            ):
                unnoted.add(name)
    assert not unnoted, sorted(unnoted)
