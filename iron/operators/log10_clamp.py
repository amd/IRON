# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import In, Out
from aie.iron.kernels import activation
from aie.utils.compile.jit.params import param

from iron.common import UnaryElementwise
from iron.common.elementwise import CORES, Elementwise, Sweep
from iron.common.testing import Case, Testing


def draw(op):
    """Mel energies over seventeen decades, an eighth of them zero, and
    their largest as the peak.
    """
    rng = np.random.default_rng(42)
    x = 10.0 ** rng.uniform(-14, 3, op.size) * (rng.uniform(size=op.size) >= 0.125)
    x = x.astype(np.float32)
    return dict(given={op.x: x, op.peak: x.max(keepdims=True)})


class Log10Clamp(UnaryElementwise):
    """`log10(max(x, mel_floor))` of float32 held to `decades` below that of
    `peak`, then `(y + shift) * scale`, rounded once to bf16: Whisper's
    log-mel features from mel energies and the clip's largest.
    """

    test = Testing(
        [
            Sweep(),
            # Whisper's clip: 3000 frames of 128 mels.
            Case(dict(size=384000, num_aie_columns=8, tile_size=1600), id="whisper"),
        ],
        draw=draw,
    )

    mel_floor: float = param(default=1e-10, array=True)
    decades: float = param(default=8.0, array=True)
    shift: float = param(default=4.0, array=True)
    scale: float = param(default=0.25, array=True)

    x = In(
        UnaryElementwise.size,
        dtype=np.float32,
        obj_shape=(UnaryElementwise.tile_size,),
        per=CORES,
    )
    # One float32 every core holds for the call.
    peak = In(
        1,
        dtype=np.float32,
        obj_shape=(1,),
        per=(Elementwise.num_channels,),
        replicate=True,
    )
    y = Out(
        UnaryElementwise.size,
        obj_shape=(UnaryElementwise.tile_size,),
        per=CORES,
    )

    def compatible(self) -> None:
        super().compatible()
        if self.tile_size % 32:
            raise ValueError(
                f"Log10Clamp: tile_size ({self.tile_size}) is not whole 32-lane "
                f"vectors"
            )

    def kernel(self):
        return activation.log10_clamp_f32(self.tile_size)

    def scalars(self) -> tuple:
        return (self.mel_floor, self.decades, self.shift, self.scale)
