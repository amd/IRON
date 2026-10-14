# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Every catalog case's judgement, device-free: its own oracle output passes
its ``tolerance()``, and an output past it, a NaN or its halves swapped fail,
as a device test, check mode and the tuner judge them."""

import numpy as np
import pytest
from aie.iron.device import from_name

from iron.common.elementwise import _interval
from iron.common.harness import vectors
from iron.tests.common.declared import declared

DEVICES = {"npu2": 8, "npu1": 4}


def _cases():
    return [
        pytest.param(device, cls, case, id=f"{device}-{name}-{case.label}")
        for device, n_cols in DEVICES.items()
        for name, cls, case, unresolvable in declared(from_name(device, n_cols=n_cols))
        if unresolvable is None and not case.extensive
    ]


@pytest.mark.parametrize("device,cls,case", _cases())
def test_a_case_passes_its_oracle_and_fails_an_output_past_its_tolerance(
    request, device, cls, case
):
    op = cls(**case.kwargs).resolved(request.getfixturevalue(device))
    draw = cls.test.draw
    v = vectors(op, **(draw(op) if callable(draw) else draw or {}))
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
        if flat.size > 1:
            wrong["its halves swapped"] = np.roll(flat, flat.size // 2)
        for what, w in wrong.items():
            written = {**v.outputs, out.name: w.reshape(want.shape)}
            verdict = op.judge(v.inputs, written, tolerance)[out.name]
            assert not verdict, f"{out.name} with {what} passed {tolerance}"
