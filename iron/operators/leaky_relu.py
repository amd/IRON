# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron.kernels import activation

from iron.common import UnaryElementwise, param
from iron.common.testing import Case, Testing, channeled_unary_cases


class LeakyReLU(UnaryElementwise):
    """AIE-accelerated Leaky ReLU operator: the elementwise design with
    ``alpha`` as a kernel argument.
    """

    test = Testing(
        # The shape sweep at the default alpha, then two more alphas on one
        # small shape in the default suite, so alpha is seen to reach the
        # kernel.
        lambda cls: (
            channeled_unary_cases(alpha=0.01)(cls)
            + [
                Case(
                    dict(
                        size=2048,
                        num_aie_columns=1,
                        num_channels=1,
                        tile_size=2048,
                        alpha=a,
                    )
                )
                for a in (0.1, 0.25)
            ]
        ),
        draw=dict(centered=("x",)),
    )

    alpha: float = param(default=0.01, array=True)

    def kernel(self, target):
        # The factory holds what the line length must satisfy: a whole
        # number of the architecture's vectors (16 on aie2, 32 on aie2p).
        return activation.leaky_relu(self.tile_size)

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        kernel(elem_in, elem_out, self.tile_size, self.alpha)

    def reference(self, x):
        """CPU reference: ``x`` where positive, ``alpha * x`` where not."""
        f = x.astype(np.float32)
        return np.where(f > 0, f, np.float32(self.alpha) * f).astype(x.dtype)
