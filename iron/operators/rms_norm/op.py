# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import dataclasses
from typing import ClassVar, Dict

import numpy as np
import torch
from ml_dtypes import bfloat16

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
from iron.common.utils import device_columns, get_shim_dma_limit
from iron.common.test_utils import torch_dtype_map

_I32 = np.ndarray[(1,), np.dtype[np.int32]]  # type: ignore[misc]


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

    _name_aliases: ClassVar[Dict[str, str]] = {"epsilon": "eps"}

    def tuning(self, dev) -> "RMSNormOverlay":
        cols = self.num_aie_columns
        if dev is not None:
            limit = get_shim_dma_limit(dev)
            if cols is None:
                cols = min(device_columns(dev), limit // (2 * self.num_channels))
            if cols * self.num_channels > limit:
                raise Untunable(
                    f"num_aie_columns * num_channels ({cols * self.num_channels}) "
                    f"exceeds ShimDMA limit of {limit} for this device"
                )
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
        depth = 1 if self.tile_size > 4096 else 2
        kernel = target.kernel(
            "rms_norm_eps",
            [tile_ty, tile_ty, np.int32, np.float32],
            source=target.kernel_source("rms_norm"),
        )
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
            limit = get_shim_dma_limit(dev)
            if cols is None:
                # Room for the weight fill beside the row fills.
                cols = min(device_columns(dev), limit // self.num_channels - 1)
            # (cols * chans) in-fills + chans weight-fills must fit the shim's
            # host->array channels.
            usage = self.num_channels * (cols + 1)
            if usage > limit:
                raise Untunable(
                    f"weighted RMSNorm with num_aie_columns={cols}, "
                    f"num_channels={self.num_channels} requires {usage} ShimDMA "
                    f"output channels but device only has {limit}"
                )
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
        depth = 1 if self.tile_size > 4096 else 2
        rms_norm = target.kernel(
            "rms_norm_eps",
            [tile_ty, tile_ty, np.int32, np.float32],
            source=target.kernel_source("rms_norm"),
        )
        eltwise_mul = target.kernel(
            "eltwise_mul_bf16_vector_size",
            [tile_ty, weights_ty, tile_ty, np.int32],
            source=target.kernel_source("mul"),
        )
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

    ``RMSNorm(..., weighted=True)`` constructs a :class:`WeightedRMSNorm`; the
    legacy ``size=`` spelling is ``rows * tile_size``.
    """

    rows: int = dim()

    x = In(rows, RMSNormOverlay.tile_size, to=RMSNormOverlay.x)
    y = Out(rows, RMSNormOverlay.tile_size, from_=RMSNormOverlay.y)

    def __new__(cls, *args, **kwargs):
        if cls is RMSNorm and kwargs.pop("weighted", False):
            return WeightedRMSNorm(*args, **kwargs)
        return super().__new__(cls)

    @classmethod
    def resolve_class(cls, n_operands, kwargs):
        # RMSNorm(x, w) in a graph: a bare weight tensor selects the weighted form.
        if cls is RMSNorm and (n_operands == 2 or kwargs.pop("weighted", False)):
            return WeightedRMSNorm
        return cls

    @classmethod
    def _classic(cls, kwargs):
        kwargs.pop("weighted", None)
        if "size" in kwargs:
            size = kwargs.pop("size")
            tile = kwargs.get("tile_size")
            if tile is None or size % tile:
                raise ValueError(
                    f"size ({size}) must be a multiple of tile_size ({tile})"
                )
            kwargs["rows"] = size // tile
        return super()._classic(kwargs)

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


def generate_golden_reference(
    rows: int, cols: int, dtype="bf16", seed=42, weighted=False, eps=1e-5
):
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    if weighted:
        weights = torch.rand(cols, dtype=torch_dtype_map[dtype]) * val_range
        output_tensor = reference(input_tensor, weights, weighted=True, eps=eps)
        return {"input": input_tensor, "weight": weights, "output": output_tensor}
    else:
        output_tensor = reference(input_tensor, eps=eps)
        return {"input": input_tensor, "output": output_tensor}
