# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""NPU vs torch-bf16 golden tolerances for AIEConv2d (audit-backed).

Semantics live in ROADMAP Track B (tolerance audit). Values are defaults for
``verify_buffer`` / ``torch.allclose`` on hardware paths — not CPU reference
bit-exactness.

Audit (NPU2 / aie2p, float-accum kernels, seed=42 smoke-like matrix including
3→16 k3, depthwise, groups=2, pointwise, strided, 16×16/32×32, 1–2 cols):

- Large-channel groups==1 and pointwise often max |rel| ≪ 1% on non-tiny values.
- Small-IC / grouped cases still show absolute O(0.25–0.5) bf16 MAC-order drift
  vs ``F.conv2d(bf16)``; near-zero outputs need abs floor.
- Policy after audit: tighten default from (0.1, 1.0) → (0.05, 0.5) with
  ``max_error_rate=0.02``. Matrix verified green under that policy on NPU2.
- Tighter abs (0.25) fails groups=2 cases; keep abs_tol=0.5 until kernels improve.
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
    notes: str = ""


# Default smoke / forward / bench NPU path (audit-backed, 2026-08 NPU2).
HW_DEFAULT: Final[Conv2dHWTolerances] = Conv2dHWTolerances(
    rel_tol=0.05,
    abs_tol=0.5,
    max_error_rate=0.02,
    notes="float-accum kernels vs torch bf16; allow 2% outlier rate",
)

# Historical pre-audit defaults (kept for regression comparisons only).
HW_LEGACY_LOOSE: Final[Conv2dHWTolerances] = Conv2dHWTolerances(
    rel_tol=0.1,
    abs_tol=1.0,
    max_error_rate=0.02,
    notes="pre-audit MVP; superseded by HW_DEFAULT",
)

# Stricter profile for large-channel / pointwise-only experiments (not default).
HW_STRICT_EXPERIMENTAL: Final[Conv2dHWTolerances] = Conv2dHWTolerances(
    rel_tol=0.02,
    abs_tol=0.5,
    max_error_rate=0.02,
    notes="experimental; not default — may fail small-IC/grouped",
)


def hw_tolerances() -> Conv2dHWTolerances:
    """Return the product default HW verification tolerances."""
    return HW_DEFAULT
