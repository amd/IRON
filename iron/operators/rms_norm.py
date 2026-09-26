# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


from typing import ClassVar

import numpy as np
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise, norm
from aie.utils.verify import Tolerance

from iron.common import Elementwise, Extent, In, Out, auto, param
from iron.common.device import bound_device
from iron.common.testing import Case, Testing
from iron.common.tiling import fifo_depth

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


def _cases(cls):
    """Every column and channel split that divides each size within the
    class's shim budget and line cap; the 2048 shape is the default suite.
    """
    dev = bound_device()
    out = []
    for size in [1024, 2048, 4096, 8192]:
        for channels in (1, 2):
            for cols in range(1, cls.shim_columns(dev, channels) + 1):
                tile_size = min(size // (cols * channels), cls.tile_cap)
                if tile_size * cols * channels != size:
                    continue
                out.append(
                    Case(
                        dict(
                            rows=size // tile_size,
                            num_aie_columns=cols,
                            num_channels=channels,
                            tile_size=tile_size,
                        ),
                        extensive=size != 2048,
                    )
                )
    return out


class RMSNorm(Elementwise):
    """AIE-accelerated RMS Normalization layer (unweighted).

    ``rows`` rows of ``tile_size`` elements; :class:`WeightedRMSNorm` is the
    form with a learned weight row, which a graph call with a weight picks.
    ``tile_size`` is the row length and appears in the host shape (``rows x
    tile_size``), so it is a ``param()`` here rather than the knob the base
    declares.
    """

    test = Testing(_cases, tolerance=Tolerance.relative(0.04, 1e-6))

    rows: int = param()
    valid = Extent(rows)  # rows, or fewer per call
    # Required here, though the base defaults it: every field is keyword-only.
    tile_size: int = param()  # pyright: ignore
    # One core by default: a core normalizes whole rows, and the row count is
    # the extent. Call sites with many rows spread them over columns.
    num_aie_columns: int = auto(1)
    # RMSNorm eps; Llama 1e-5 (default), Gemma 1e-6
    epsilon: float = param(default=1e-5, array=True)

    tile_cap: ClassVar[int] = 8192

    x = In(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(num_aie_columns, Elementwise.num_channels),
    )
    y = Out(
        rows,
        tile_size,
        tile=(tile_size,),
        per=(num_aie_columns, Elementwise.num_channels),
    )

    @classmethod
    def resolve_class(cls, n_operands, kwargs):
        # RMSNorm(x, w) in a graph: a bare weight tensor selects the weighted form.
        if cls is RMSNorm and n_operands == 2:
            return WeightedRMSNorm
        return cls

    @property
    def weighted(self) -> bool:
        return False

    @property
    def valid_elements(self) -> int:
        return self.valid * self.tile_size

    def kernel(self, target):
        return norm.rms_norm_eps(self.tile_size)

    def kernel_call(self, kernel, elem_in, elem_out) -> None:
        kernel(elem_in, elem_out, self.tile_size, self.epsilon)

    def reference(self, x, w=None):
        """CPU reference: row-wise RMS normalization, optionally weighted."""
        return reference(x, w=w, weighted=self.weighted, eps=self.epsilon)


class WeightedRMSNorm(RMSNorm):
    """AIE-accelerated RMS Normalization layer with a learned weight row.

    Two cores per (column, channel), pipelined: one normalizes, the next
    multiplies by the weight. The weight fifo is one per channel, shared by
    every column in that channel, and each receives the whole weight row,
    which halves the line a core holds. The pipeline is why this class owns
    its array: the elementwise template places one core per slot.
    """

    tile_cap: ClassVar[int] = 4096

    x = In(
        RMSNorm.rows,
        RMSNorm.tile_size,
        tile=(RMSNorm.tile_size,),
        per=(RMSNorm.num_aie_columns, RMSNorm.num_channels),
    )
    # The weight row is one line, shared by every column of a channel; the
    # shim budget counts a replicate= stream once per channel.
    w = In(
        RMSNorm.tile_size,
        tile=(RMSNorm.tile_size,),
        per=(RMSNorm.num_channels,),
        replicate=True,
    )
    y = Out(
        RMSNorm.rows,
        RMSNorm.tile_size,
        tile=(RMSNorm.tile_size,),
        per=(RMSNorm.num_aie_columns, RMSNorm.num_channels),
    )

    @property
    def weighted(self) -> bool:
        return True

    def array(self, target) -> list:

        tile_ty = self.x.tile
        weights_ty = self.w.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = fifo_depth(self.tile_size, self.x.dtype)
        rms_norm = norm.rms_norm_eps(self.tile_size)
        eltwise_mul = eltwise.mul_sized(self.tile_size)
        of_ins = [
            ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_ws = [
            ObjectFifo(weights_ty, name=f"in2_weights_{j}", depth=depth)
            for j in range(chans)
        ]
        of_mid = [
            ObjectFifo(tile_ty, name=f"out1_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(tile_ty, name=f"out2_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        n_cores = cols * chans
        dynamic = self.uses_value("count") and target.image == "elf"
        counts = (
            [self.count.param] * (2 * n_cores)
            if dynamic
            else [target.rtp(_I32, name=f"count_{k}") for k in range(2 * n_cores)]
        )
        barriers = [target.barrier() for _ in range(2 * n_cores)]
        tile_size, epsilon = self.tile_size, self.epsilon

        def core_norm(of_in, of_out, rms, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rms(elem_in, elem_out, tile_size, epsilon)
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out, tile_size)
                of_in.release(1)
                of_out.release(1)
            of_w.release(1)

        workers = []
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_norm,
                        [
                            of_ins[k].cons(),
                            of_mid[k].prod(),
                            rms_norm,
                            counts[k],
                            barriers[k],
                        ],
                    )
                )
        for i in range(cols):
            for j in range(chans):
                k = i * chans + j
                workers.append(
                    Worker(
                        core_mul,
                        [
                            of_mid[k].cons(),
                            of_ws[j].cons(),
                            of_outs[k].prod(),
                            eltwise_mul,
                            counts[n_cores + k],
                            barriers[n_cores + k],
                        ],
                    )
                )
        for k in range(n_cores):
            self.x.lane(k).bind(of_ins[k].prod())
            self.y.lane(k).bind(of_outs[k].cons())
        for j in range(chans):
            self.w.lane(j).bind(of_ws[j].prod())
        if not dynamic:
            self.count.bind(counts)
        return workers


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x, w=None, weighted=False, eps=1e-5):
    """CPU reference: row-wise RMS normalization, optionally weighted (ground truth).

    Matches the AIE kernel: normalize by 1/sqrt(mean(x^2) + eps).
    """
    f = x.astype(np.float32)
    rms = np.sqrt(np.mean(f**2, axis=-1, keepdims=True) + eps)
    out = (f / rms).astype(x.dtype)
    if weighted:
        out = out * w
    return out
