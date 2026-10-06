# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
import numpy as np
from aie.iron import Buffer, ObjectFifo, Worker, WorkerRuntimeBarrier
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise, norm
from aie.utils.verify import Tolerance

from iron.common import In, Out, Rowwise, param
from iron.common.testing import Sweep, Testing

# The longest weighted row: the multiplying core holds the weight row beside
# each line, which halves the line a core holds.
WEIGHTED_TILE_CAP = 4096


class RMSNorm(Rowwise):
    """AIE-accelerated RMS Normalization of each row, optionally times a
    learned weight row.

    Unweighted, one core per (column, channel) runs the norm, as any
    elementwise operator. Weighted (``RMSNorm(x, weight=w)`` in a graph,
    or ``weighted=True``), two cores per (column, channel) are pipelined: one
    normalizes, the next multiplies by the weight. The weight fifo is one
    per channel, shared by every column in that channel, and each receives
    the whole weight row, which halves the line a core holds.
    """

    test = Testing(
        [Sweep(rows=True), Sweep(rows=True, tile_cap=WEIGHTED_TILE_CAP, weighted=True)]
    )

    # The epsilon under the root: 1e-5 by default; a model states its own.
    epsilon: float = param(default=1e-5, array=True)
    weighted: bool = param(default=False, array=True)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    # The weight row is one line, shared by every column of a channel; the
    # shim budget counts a replicate= stream once per channel.
    weight = In(
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_channels,),
        replicate=True,
        when=weighted,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        tile=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        if self.weighted and self.tile_size > WEIGHTED_TILE_CAP:
            raise ValueError(
                f"tile_size={self.tile_size}: a weighted row is at most "
                f"{WEIGHTED_TILE_CAP} elements, since the multiplying core holds "
                f"the weight row beside each line"
            )

    def kernel(self):
        return norm.rms_norm_eps(self.tile_size)

    def scalars(self) -> tuple:
        return (self.epsilon,)

    def reference(self, x, weight=None):
        """The kernels' references in turn: the normalized row rounded to
        bf16, as the first core stores it, then times the weight.
        """
        normed = super().reference(x)
        if weight is None:
            return normed
        y = eltwise.mul_sized(self.tile_size).contract.reference(normed, weight)
        return y.astype(normed.dtype)

    def tolerance(self) -> Tolerance | None:
        if not self.weighted:
            return super().tolerance()
        # Each kernel is within one ulp of its reference; the product of a
        # row one ulp off is itself up to one ulp off before its own rounding.
        return Tolerance.bf16_ulps(
            2,
            atol=2.0**-126,
            note="rms_norm_eps then mul_sized, one ulp each; atol is the "
            "smallest normal bf16",
        )

    def array(self, target) -> list:
        if not self.weighted:
            return super().array(target)
        tile_ty = self.x.tile
        weights_ty = self.weight.tile
        cols, chans = self.num_aie_columns, self.num_channels
        depth = target.fifo_depth(self.tile_size, self.x.dtype)
        rms_norm = self.kernel()
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
            else [
                Buffer(
                    np.ndarray[(1,), np.dtype[np.int32]],
                    name=f"count_{k}",
                    use_write_rtp=True,
                )
                for k in range(2 * n_cores)
            ]
        )
        barriers = [WorkerRuntimeBarrier() for _ in range(2 * n_cores)]

        def core_norm(of_in, of_out, rms, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                rms(elem_in, elem_out, self.tile_size, self.epsilon)
                of_in.release(1)
                of_out.release(1)

        def core_mul(of_in, of_w, of_out, mul, count, barrier):
            barrier.wait_for_value(1)
            n = count.read() if dynamic else count[0]
            elem_w = of_w.acquire(1)
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mul(elem_in, elem_w, elem_out, self.tile_size)
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
            self.weight.lane(j).bind(of_ws[j].prod())
        if not dynamic:
            self.count.bind(counts)
        return workers + barriers
