# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron.common import Link, UnaryElementwise, auto
from iron.common.testing import Case, Sweep, Testing
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gelu import GELU


class SiLU(UnaryElementwise):
    """AIE-accelerated SiLU activation function."""

    # SwiGLU's product finished in silu's cores, its other factor streamed
    # beside silu's input.
    test = Testing(
        [
            Sweep(channels=None),
            *(
                Case(dict(size=2048, num_aie_columns=4, finish=chain), id=name)
                for name, chain in [
                    ("finish_ElementwiseMul", (Link(ElementwiseMul(size=2048)),)),
                    (
                        "finish_ElementwiseMul_at1",
                        (Link(ElementwiseMul(size=2048), 1),),
                    ),
                    (
                        "finish_ElementwiseMul_at1GELU",
                        (Link(ElementwiseMul(size=2048), 1), Link(GELU(size=2048))),
                    ),
                ]
            ),
        ]
    )

    # One channel per column: the LUT-based kernel is sized for it.
    num_channels: int = auto(1, repr=False, init=False)

    def kernel(self):
        return activation.silu_sized(self.tile_size)
