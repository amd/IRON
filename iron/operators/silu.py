# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron.kernels import activation

from iron import operators as catalog
from iron.common import Chain, Link, UnaryElementwise, Auto
from iron.common.elementwise import Sweep
from iron.common.testing import Case, Testing


class SiLU(UnaryElementwise):
    """AIE-accelerated SiLU activation function."""

    # SwiGLU's product finished in silu's cores.
    test = Testing(
        [
            Sweep(channels=None),
            lambda cls, dev: [
                Case(dict(size=2048, num_aie_columns=4, finish=chain), id=name)
                for name, chain in [
                    (
                        "finish_ElementwiseMul",
                        Chain((Link(catalog.ElementwiseMul(size=2048)),)),
                    ),
                    (
                        "finish_ElementwiseMul_at1",
                        Chain((Link(catalog.ElementwiseMul(size=2048), 1),)),
                    ),
                    (
                        "finish_ElementwiseMul_at1GELU",
                        Chain(
                            (
                                Link(catalog.ElementwiseMul(size=2048), 1),
                                Link(catalog.GELU(size=2048)),
                            )
                        ),
                    ),
                ]
            ],
        ]
    )

    # One channel per column: the LUT-based kernel is sized for it.
    num_channels: int = Auto(default=1, repr=False, init=False)

    def kernel(self):
        # vtanh's error was most of Llama 3.2 3B's divergence; the table costs nothing.
        return activation.silu_sized(self.tile_size, use_lut=True)
