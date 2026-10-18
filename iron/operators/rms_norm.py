# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from aie.iron import ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import eltwise, norm
from aie.utils.verify import Tolerance

from iron.common import Built, In, KernelCall, Out, Param, Rowwise, Rtp
from iron.common.elementwise import Sweep
from iron.common.testing import Testing

# The longest weighted row: the weight row beside each line halves it.
WEIGHTED_TILE_CAP = 4096


class RMSNorm(Rowwise):
    """AIE-accelerated RMS Normalization of each row, optionally times a
    learned weight row.

    Weighted, two cores per (column, channel) are pipelined: one normalizes,
    the next multiplies by the weight row, which halves the line a core holds.
    """

    test = Testing(
        [
            Sweep(rows=True),
            Sweep(rows=True, tile_cap=WEIGHTED_TILE_CAP, lower=True, weighted=True),
        ]
    )

    # The epsilon under the root: 1e-5 by default; a model states its own.
    epsilon: float = Param(default=1e-5, array=True)
    weighted: bool = Param(default=False)

    x = In(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )
    # Shared by every column of a channel: counted once per channel.
    weight = In(
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_channels,),
        replicate=True,
        when=weighted,
    )
    y = Out(
        Rowwise.rows,
        Rowwise.tile_size,
        obj_type=(Rowwise.tile_size,),
        per=(Rowwise.num_aie_columns, Rowwise.num_channels),
    )

    def validate(self) -> None:
        if self.weighted and self.tile_size > WEIGHTED_TILE_CAP:
            raise ValueError(
                f"RMSNorm: tile_size ({self.tile_size}) must be at most "
                f"{WEIGHTED_TILE_CAP} when weighted, since the multiplying core "
                f"holds the weight row beside each line"
            )

    def chain(self) -> tuple[KernelCall, ...]:
        if not self.weighted:
            return super().chain()
        config = self.array_config()
        return (
            KernelCall(config.kernel(), config.scalars(), (self.x,)),
            KernelCall(eltwise.mul_sized(self.tile_size), (), (None, self.weight)),
        )

    def reference(self, x, weight=None):
        """The kernels' references in turn, the normalized row rounded to bf16."""
        normed = super().reference(x)
        if weight is None:
            return normed
        y = eltwise.mul_sized(self.tile_size).contract.reference(normed, weight)
        return y.astype(normed.dtype)

    def tolerance(self) -> Tolerance | None:
        if not self.weighted:
            return super().tolerance()
        # Each kernel's ulp, and the product's of a row one ulp off.
        return Tolerance.bf16_ulps(
            2,
            atol=2.0**-126,
            note="rms_norm_eps then mul_sized, one ulp each; atol is the "
            "smallest normal bf16",
        )

    class Array(Rowwise.Array):
        def kernel(self):
            return norm.rms_norm_eps(self.tile_size)

        def scalars(self) -> tuple:
            return (self.epsilon,)

        def build(self) -> Built:
            if not self.weighted:
                return super().build()
            tile_ty = self.x.obj_type
            weights_ty = self.weight.obj_type
            cols, chans = self.num_aie_columns, self.num_channels
            depth = self.x.l1_depth
            rms_norm = self.kernel()
            eltwise_mul = eltwise.mul_sized(self.tile_size)
            of_ins = [
                ObjectFifo(tile_ty, depth=depth)
                for i in range(cols)
                for j in range(chans)
            ]
            of_ws = [ObjectFifo(weights_ty, depth=depth) for j in range(chans)]
            of_mid = [
                ObjectFifo(tile_ty, depth=depth)
                for i in range(cols)
                for j in range(chans)
            ]
            of_outs = [
                ObjectFifo(tile_ty, depth=depth)
                for i in range(cols)
                for j in range(chans)
            ]
            n_cores = cols * chans
            rtps = [Rtp([self.count]) for _ in range(2 * n_cores)]

            def core_norm(of_in, of_out, rms, rtp):
                n = rtp.read()[self.count]
                for _ in range_(n):
                    elem_in = of_in.acquire(1)
                    elem_out = of_out.acquire(1)
                    rms(elem_in, elem_out, self.tile_size, self.epsilon)
                    of_in.release(1)
                    of_out.release(1)

            def core_mul(of_in, of_w, of_out, mul, rtp):
                n = rtp.read()[self.count]
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
                                rtps[k],
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
                                rtps[n_cores + k],
                            ],
                        )
                    )
            self.x.bind([f.prod() for f in of_ins])
            self.y.bind([f.cons() for f in of_outs])
            self.weight.bind([f.prod() for f in of_ws])
            return Built(workers, rtps)
