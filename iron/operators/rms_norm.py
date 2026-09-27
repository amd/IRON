# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
from typing import ClassVar

import numpy as np
from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise, norm
from aie.utils.verify import Tolerance

from iron.common import In, Out, Rowwise, param
from iron.common.tiling import fifo_depth

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


class RMSNorm(Rowwise):
    """AIE-accelerated RMS Normalization of each row (unweighted).

    :class:`WeightedRMSNorm` is the form with a learned weight row, which a
    graph call with a weight picks.
    """

    # RMSNorm eps; Llama 1e-5 (default), Gemma 1e-6
    epsilon: float = param(default=1e-5, array=True)

    @classmethod
    def resolve_class(cls, n_operands, kwargs):
        # RMSNorm(x, w) in a graph: a bare weight tensor selects the weighted form.
        if cls is RMSNorm and n_operands == 2:
            return WeightedRMSNorm
        return cls

    def kernel(self, target):
        return norm.rms_norm_eps(self.tile_size, epsilon=self.epsilon)


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

    def reference(self, x, w):
        """The two kernels' references in turn: the normalized row rounded to
        bf16, as the first core stores it, then times the weight.
        """
        normed = super().reference(x)
        y = eltwise.mul_sized(self.tile_size).contract.reference(normed, w)
        return y.astype(normed.dtype)

    def tolerance(self, target) -> Tolerance:
        # Each kernel is within one ulp of its reference; the product of a
        # row one ulp off is itself up to one ulp off before its own rounding.
        return Tolerance.bf16_ulps(
            2,
            atol=2.0**-126,
            note="rms_norm_eps then mul_sized, one ulp each; atol is the "
            "smallest normal bf16",
        )

    def array(self, target) -> list:
        tile_ty = self.x.tile
        weights_ty = self.w.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = fifo_depth(self.tile_size, self.x.dtype)
        rms_norm = self.kernel(target)
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

        def core_norm(of_in, of_out, rms, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rms(elem_in, elem_out)
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out)
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
