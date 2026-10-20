# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar

from aie.iron.kernels import activation
from aie.utils.compile.jit.params import param

from iron.common import UnaryElementwise
from iron.common.elementwise import Sweep
from iron.common.testing import Testing


class GELU(UnaryElementwise):
    """AIE-accelerated GELU: by its tanh approximation, or exact
    (``approximate="none"``, ``x * Phi(x)``), as torch's ``approximate``.
    """

    test = Testing(
        [Sweep(), Sweep(approximate="none", bench=None)],
        draw=lambda op: dict(centered=(op.x,)),
    )

    tile_cap: ClassVar[int] = 8192

    approximate: str = param(default="tanh", array=True)

    def validate(self) -> None:
        if self.approximate not in ("tanh", "none"):
            raise ValueError(
                f"GELU: approximate={self.approximate!r} is neither 'tanh' nor 'none'"
            )

    def kernel(self):
        if self.approximate == "none":
            return activation.gelu_erf(self.tile_size)
        # vtanh's error was most of SmolVLM's vision tower's divergence; the table costs nothing.
        return activation.gelu(self.tile_size, use_lut=True)
