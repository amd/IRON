# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Runs of steps the fusion tests fuse, their recordings, and the fusions over them."""

from iron.common.graph.record import Recording
from iron.common.image.step import Edge, Fusion, FusionKind
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU
from iron.tests.support import sequences


def stream(producer: int, output: str, input: str) -> Fusion:
    """Return the two-step stream fusion of ``producer``'s ``output`` into the next step's ``input``."""
    return Fusion(
        FusionKind.STREAM,
        (producer, producer + 1),
        (Edge(producer, output, producer + 1, input),),
    )


def three_step() -> Fusion:
    """Return ``gemv_silu_mul``'s stream fusion: GEMV's ``C`` into SiLU, SiLU's ``y`` into the multiply."""
    return Fusion(
        FusionKind.STREAM, (0, 1, 2), (Edge(0, "C", 1, "x"), Edge(1, "y", 2, "a"))
    )


def silu_mul(size, tile, **extra):
    """Return a SwiGLU gate's SiLU and multiply."""
    silu = SiLU(size=size, tile_size=tile, **extra)
    mul = ElementwiseMul(size=size, tile_size=tile, **extra)
    return silu, mul


def silu_mul_recording(name, silu, mul):
    """Return ``silu`` then ``mul``, SiLU's ``y`` and the multiply's ``a`` both ``mid``."""
    steps = sequences.steps((silu, "x", "mid"), (mul, "mid", "up", "out"))
    return Recording.of_steps(name, steps, ["x", "up"], ["out"])


def gemv_add(M, K, tile_size_input=4, tile_size_output=256, **extra):
    """Return a projection and its residual add; the defaults are Llama decode's profile tunables at 2048 by 2048."""
    gemv = GEMV(
        M=M,
        K=K,
        tile_size_input=tile_size_input,
        tile_size_output=tile_size_output,
        **extra,
    )
    add = ElementwiseAdd(size=M, tile_size=tile_size_output, **extra)
    return gemv, add


def gemv_add_recording(name, gemv, add):
    """Return ``gemv`` then ``add``, GEMV's ``C`` and the add's ``b`` both ``mid``."""
    steps = sequences.steps((gemv, "A", "B", "mid"), (add, "r", "mid", "out"))
    return Recording.of_steps(name, steps, ["A", "B", "r"], ["out"])


def gemv_silu_mul(M, cols, tile, **extra):
    """Return a square projection, then ``silu_mul`` on ``cols`` columns."""
    gemv = GEMV(M=M, K=M, tile_size_input=4, tile_size_output=tile, **extra)
    silu, mul = silu_mul(M, tile, num_aie_columns=cols, **extra)
    return gemv, silu, mul


def gemv_silu_mul_recording(name, gemv, silu, mul):
    """Return the three steps, GEMV's ``C`` into SiLU's ``x`` and SiLU's ``y`` into the multiply's ``a``."""
    steps = sequences.steps(
        (gemv, "A", "B", "mid1"), (silu, "mid1", "mid2"), (mul, "mid2", "up", "out")
    )
    return Recording.of_steps(name, steps, ["A", "B", "up"], ["out"])


def kinds(recording, fusion) -> tuple[str, ...]:
    """Return the class name of each of ``fusion``'s steps in ``recording``, resolved."""
    return tuple(type(recording.steps[i].op.resolved()).__name__ for i in fusion.steps)
