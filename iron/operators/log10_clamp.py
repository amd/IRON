# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whisper's fused log10, dynamic floor, and affine normalization."""

import numpy as np
from aie.iron import In, Out
from aie.iron.kernels import activation
from aie.utils.compile.jit.params import param
from ml_dtypes import bfloat16

from iron.common import UnaryElementwise
from iron.common.elementwise import CORES, Elementwise, Sweep
from iron.common.testing import Testing


class Log10Clamp(UnaryElementwise):
    """Apply Whisper's log10 floor and affine transform, rounding once to bf16."""

    test = Testing(
        Sweep(lengths=(2048,), channels=(1,), bench=None),
        draw=lambda op: _draw(op),
    )

    mel_floor: float = param(default=1e-10, array=True)
    decades: float = param(default=8.0, array=True)
    shift: float = param(default=4.0, array=True)
    scale: float = param(default=0.25, array=True)

    x = In(
        UnaryElementwise.size,
        dtype=np.float32,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )
    peak = In(
        1,
        dtype=np.float32,
        obj_shape=(1,),
        per=(Elementwise.num_channels,),
        replicate=True,
    )
    y = Out(
        UnaryElementwise.size,
        dtype=bfloat16,
        obj_shape=(Elementwise.tile_size,),
        per=CORES,
    )

    def kernel(self):
        return activation.log10_clamp_f32(self.tile_size)

    def scalars(self) -> tuple:
        return (self.mel_floor, self.decades, self.shift, self.scale)


def _draw(op):
    """Supply positive energies and their clip-wide maximum to the kernel test."""
    rng = np.random.default_rng(42)
    x = np.power(10.0, rng.uniform(-12, 2, op.size)).astype(np.float32)
    return dict(given={op.x: x, op.peak: np.array([x.max()], dtype=np.float32)})
