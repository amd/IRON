# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""NPU vs torch-bf16 golden tolerances for AIEConv2d.

Defaults for ``verify_buffer`` on hardware paths. bf16 MAC order can differ
from ``F.conv2d(bf16)``; small/grouped shapes need a non-zero abs floor.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Final


@dataclass(frozen=True)
class Conv2dHWTolerances:
    """Hardware verification policy for one compare surface."""

    rel_tol: float
    abs_tol: float
    max_error_rate: float


# Default HW verify policy (NPU vs torch bf16 golden).
HW_DEFAULT: Final = Conv2dHWTolerances(
    rel_tol=0.05,
    abs_tol=0.5,
    max_error_rate=0.02,
)

# Looser alternate for experiments only (not default product path).
HW_LOOSE: Final = Conv2dHWTolerances(
    rel_tol=0.1,
    abs_tol=1.0,
    max_error_rate=0.02,
)

# Tighter alternate for large-channel / pointwise-only experiments.
HW_STRICT_POINTWISE: Final = Conv2dHWTolerances(
    rel_tol=0.05,
    abs_tol=0.25,
    max_error_rate=0.0,
)


def hw_tolerances() -> Conv2dHWTolerances:
    """Return the product default HW verification tolerances."""
    return HW_DEFAULT
