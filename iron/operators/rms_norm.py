# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses

import numpy as np
import torch

from iron.common.declare import (
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)
import aie.utils as aie_utils
from aie.iron.kernels import eltwise, norm

from iron.common.testing import Case, Testing
from iron.common.utils import bank_elements, get_shim_dma_limit

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


def _cases(weighted):
    """Every column and channel split that divides each size within the
    ShimDMA budget; the 2048 shape is the default suite. A weighted norm
    also streams the weight row, one fifo per channel across the columns,
    so its budget is channels * (columns + 1) and its line cap is half."""

    def cases():
        dev = aie_utils.get_current_device()
        limit = get_shim_dma_limit(dev)
        tile_cap = 4096 if weighted else 8192
        out = []
        for size in [1024, 2048, 4096, 8192]:
            for cols in range(1, dev.cols + 1):
                for channels in (1, 2):
                    if cols * channels > limit:
                        continue
                    if weighted and channels * (cols + 1) > limit:
                        continue
                    tile_size = min(size // (cols * channels), tile_cap)
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

    return cases


@operator
class RMSNormOverlay(Overlay):
    """The array for row-wise RMS normalization: one core per (column, channel).

    ``tile_size`` is the row length and is shape-bearing (the host buffers are
    ``rows x tile_size``), so it is a dimension of the overlay, not a tunable.
    """

    tile_size: int = dim()
    # One core by default: a core normalizes whole rows, and how many rows
    # there are is the extent. Call sites with many rows spread them.
    num_aie_columns: int = tunable(1)
    num_channels: int = tunable(1)
    epsilon: float = 1e-5  # RMSNorm eps; Llama 1e-5 (default), Gemma 1e-6
    # The core's tile: min(tile_size, 8192). Filled by tuning.
    per_tile: int | None = tunable(None, repr=False)

    x = StreamIn(per_tile, per=(num_aie_columns, num_channels))
    y = StreamOut(per_tile, per=(num_aie_columns, num_channels))
    count = Resident(np.int32)

    def tuning(self, dev) -> "RMSNormOverlay":
        cols = self.num_aie_columns
        if dev is not None:
            if cols is None:
                cols = self.shim_columns(dev, self.num_channels)
            self.check_shim_columns(dev, cols, self.num_channels)
        elif cols is None:
            raise Untunable("num_aie_columns defaults from the device; none given")
        return dataclasses.replace(
            self, num_aie_columns=cols, per_tile=min(self.tile_size, 8192)
        )

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_ty = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = 1 if self.per_tile > bank_elements(self.x.dtype) else 2
        kernel = norm.rms_norm_eps(self.per_tile)
        of_ins = [
            ObjectFifo(tile_ty, name=f"in1_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(tile_ty, name=f"out_{i}_{j}", depth=depth)
            for i in range(cols)
            for j in range(chans)
        ]
        counts = [target.rtp(_I32, name=f"count_{k}") for k in range(cols * chans)]
        barriers = [target.barrier() for _ in range(cols * chans)]
        per_tile, epsilon = self.per_tile, self.epsilon

        def core_body(of_in, of_out, rms_norm, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rms_norm(elem_in, elem_out, per_tile, epsilon)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_body,
                [of_ins[k].cons(), of_outs[k].prod(), kernel, counts[k], barriers[k]],
            )
            for k in range(cols * chans)
        ]
        for k in range(cols * chans):
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.count.bind(counts)
        return workers


@operator
class WeightedRMSNormOverlay(RMSNormOverlay):
    """RMS normalization followed by an elementwise multiply with a weight row.

    Two cores per (column, channel), pipelined: one normalizes, the next
    multiplies by the weight. The weight fifo is one per channel, shared by
    every column in that channel, and each receives the whole weight row.
    """

    w = StreamIn(
        RMSNormOverlay.per_tile, per=RMSNormOverlay.num_channels, replicate=True
    )

    def tuning(self, dev) -> "WeightedRMSNormOverlay":
        cols = self.num_aie_columns
        if dev is not None:
            # The weight stream is declared replicate=, so the budget already
            # leaves room for its one fill per channel beside the row fills.
            if cols is None:
                cols = self.shim_columns(dev, self.num_channels)
            self.check_shim_columns(dev, cols, self.num_channels)
        elif cols is None:
            raise Untunable("num_aie_columns defaults from the device; none given")
        # The weight is one tile, so the tile is the whole row.
        return dataclasses.replace(self, num_aie_columns=cols, per_tile=self.tile_size)

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_ty = self.x.tile
        weights_ty = self.w.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = 1 if self.per_tile > bank_elements(self.x.dtype) else 2
        rms_norm = norm.rms_norm_eps(self.per_tile)
        eltwise_mul = eltwise.mul_sized(self.per_tile)
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
        counts = [target.rtp(_I32, name=f"count_{k}") for k in range(2 * n_cores)]
        barriers = [target.barrier() for _ in range(2 * n_cores)]
        per_tile, epsilon = self.per_tile, self.epsilon

        def core_norm(of_in, of_out, rms, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rms(elem_in, elem_out, per_tile, epsilon)
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, count, barrier):
            barrier.wait_for_value(1)
            n = count[0]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out, per_tile)
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
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        for j in range(chans):
            self.w[j].bind(of_ws[j].prod())
        self.count.bind(counts)
        return workers


@operator
class RMSNorm(Operator[RMSNormOverlay]):
    """AIE-accelerated RMS Normalization layer (unweighted).

    ``rows`` rows of ``tile_size`` elements; :class:`WeightedRMSNorm` is the
    form with a learned weight row, which a graph call with a weight picks.
    """

    test = Testing(_cases(weighted=False))

    rows: int = dim()

    x = In(rows, RMSNormOverlay.tile_size, to=RMSNormOverlay.x)
    y = Out(rows, RMSNormOverlay.tile_size, from_=RMSNormOverlay.y)

    @classmethod
    def resolve_class(cls, n_operands, kwargs):
        # RMSNorm(x, w) in a graph: a bare weight tensor selects the weighted form.
        if cls is RMSNorm and n_operands == 2:
            return WeightedRMSNorm
        return cls

    @property
    def size(self) -> int:
        return self.rows * self.ov.tile_size

    @property
    def weighted(self) -> bool:
        return False

    @property
    def epsilon(self) -> float:
        return self.ov.epsilon

    def compatible(self) -> None:
        ov = self.ov
        unit = ov.num_aie_columns * ov.num_channels * ov.tile_size
        if self.size % unit:
            raise Incompatible(
                f"size ({self.size}) must be a multiple of "
                f"num_aie_columns * num_channels * tile_size ({unit})"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        return {
            "count": self.size // (ov.num_aie_columns * ov.num_channels) // ov.per_tile
        }

    def reference(self, x, w=None):
        """CPU reference: row-wise RMS normalization, optionally weighted."""
        return reference(x, w=w, weighted=self.weighted, eps=self.epsilon)


@operator
class WeightedRMSNorm(RMSNorm, Operator[WeightedRMSNormOverlay]):
    """AIE-accelerated RMS Normalization layer with a learned weight row."""

    test = Testing(_cases(weighted=True))

    x = In(RMSNorm.rows, RMSNormOverlay.tile_size, to=RMSNormOverlay.x)
    w = In(RMSNormOverlay.tile_size, to=WeightedRMSNormOverlay.w)
    y = Out(RMSNorm.rows, RMSNormOverlay.tile_size, from_=RMSNormOverlay.y)

    @property
    def weighted(self) -> bool:
        return True

    @property
    def weight_length(self) -> int:
        """Length of the weight vector, which here is one tile."""
        return self.ov.tile_size


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(x, w=None, weighted=False, eps=1e-5):
    """CPU reference: row-wise RMS normalization, optionally weighted (ground truth).

    Matches the AIE kernel: normalize by 1/sqrt(mean(x^2) + eps).
    """
    rms = torch.sqrt(torch.mean(x**2, dim=-1, keepdim=True) + eps)
    out = x / rms
    if weighted:
        out = out * w
    return out
