# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The outputs a tolerance admits, for a test that writes one just past it."""

import numpy as np
from aie.utils.verify import Tolerance, round_to
from ml_dtypes import bfloat16


def rounded(t: np.ndarray, dtype, toward: float, strict: bool) -> np.ndarray:
    """The ``dtype`` value nearest ``t`` on the side of ``toward`` (an
    infinity), past ``t`` where ``strict``, as float64.
    """
    r = t.astype(dtype)
    w = r.astype(np.float64)
    short = (w < t if toward > 0 else w > t) | (strict & (w == t))
    return np.where(short, np.nextafter(r, np.asarray(toward, dtype)), r).astype(
        np.float64
    )


def interval(
    tol: Tolerance, values: list[np.ndarray], args: list[tuple], dtype
) -> tuple[np.ndarray, np.ndarray]:
    """The outputs of ``dtype`` ``tol`` admits for any of ``values``, as
    ``compare`` decides it.

    Args:
        tol: The tolerance an output is held to.
        values: Correctly rounded outputs, as float64.
        args: Each value's reference arguments, for a bound tolerance.
        dtype: The output's element type.

    Returns:
        The least and the greatest admitted output, elementwise.
    """
    lo, hi = [], []
    ulps = tol.kind == "ulps"
    centres = [
        (round_to(v, bfloat16) if ulps else v.astype(np.float32)).astype(np.float64)
        for v in values
    ]
    scale = max(
        float(np.max(np.abs(c), where=np.isfinite(c), initial=0)) for c in centres
    )
    for v, c, a in zip(values, centres, args):
        # Each test compare passes on is an interval around the centre:
        # (radius below, radius above, whether its bound is strict).
        tests = []
        match tol.kind:
            case "bound":
                e = np.broadcast_to(np.ravel(tol.bound(*a)).astype(np.float64), c.shape)
                tests.append((e, e, False))
            case "relative":
                r = tol.rtol or 0.0
                floor = np.finfo(np.float32).tiny if tol.atol is None else tol.atol
                away = np.maximum(floor, 2 * r * np.abs(c) / (1 - r))
                near = np.maximum(floor, 2 * r * np.abs(c) / (1 + r))
                tests.append(
                    (np.where(c < 0, away, near), np.where(c < 0, near, away), True)
                )
            case "ulps":
                if tol.atol is not None:
                    tests.append((tol.atol, tol.atol, True))
            case "exact":
                c = c.astype(dtype).astype(np.float64)
        if tol.range_frac is not None and tol.kind in ("relative", "ulps"):
            tests.append((tol.range_frac * scale, tol.range_frac * scale, False))
        low, high = c, c
        for below, above, strict in tests:
            low = np.minimum(low, rounded(c - below, dtype, np.inf, strict))
            high = np.maximum(high, rounded(c + above, dtype, -np.inf, strict))
        if ulps:
            down = up = c.astype(dtype)
            for _ in range(tol.ulps):
                down = np.nextafter(down, np.asarray(-np.inf, dtype))
                up = np.nextafter(up, np.asarray(np.inf, dtype))
            low = np.minimum(low, down.astype(np.float64))
            high = np.maximum(high, up.astype(np.float64))
        finite = np.isfinite(v)
        lo.append(np.where(finite, low, v))
        hi.append(np.where(finite, high, v))
    return np.minimum.reduce(lo), np.maximum.reduce(hi)
