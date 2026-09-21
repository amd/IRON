# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from typing import ClassVar, Dict

import numpy as np
import torch
from ml_dtypes import bfloat16

from iron.common.declare import (
    BoundValue,
    Incompatible,
    In,
    Operator,
    Out,
    Overlay,
    Resident,
    Scratchpad,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)
from iron.common.device_utils import lut_sources
from iron.common.test_utils import torch_dtype_map


@operator
class SoftmaxOverlay(Overlay):
    """The array for row-wise softmax: one core per (column, channel), one row per tile.

    Each row is masked to ``vector_size`` valid elements before the softmax;
    here that is a resident the sequence writes once per build
    (``rtp_vector_size``, default the full row).
    """

    cols: int = dim()
    num_aie_columns: int = tunable(1)
    num_channels: int = tunable(1)
    rtp_vector_size: int | None = None

    x = StreamIn(cols, per=(num_aie_columns, num_channels))
    y = StreamOut(cols, per=(num_aie_columns, num_channels))
    count = Resident(np.int32)
    vector_size = Resident(np.int32)

    def validate(self) -> None:
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")

    def _kernels(self, target, tile_ty):
        # Both live in softmax.cc, so they name one object: declared separately
        # they would compile that translation unit twice and each copy would
        # define both symbols.
        source = target.kernel_source("softmax")
        bundle = lut_sources(target.dev)
        softmax_k = target.kernel(
            "softmax_bf16",
            [tile_ty, tile_ty, np.int32],
            source=source,
            bundled_sources=bundle,
            object_file_name="softmax.o",
        )
        mask_k = target.kernel(
            "mask_bf16",
            [tile_ty, np.int32, np.int32],
            source=source,
            bundled_sources=bundle,
            object_file_name="softmax.o",
        )
        return softmax_k, mask_k

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_ty = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        softmax_k, mask_k = self._kernels(target, tile_ty)
        of_ins = [
            ObjectFifo(tile_ty, name=f"in1_{i}_{j}")
            for i in range(cols)
            for j in range(chans)
        ]
        of_outs = [
            ObjectFifo(tile_ty, name=f"out_{i}_{j}")
            for i in range(cols)
            for j in range(chans)
        ]
        # [count, vector_size] per core, or [count] when vector_size is a scratchpad value
        dynamic = isinstance(self.vector_size, BoundValue)
        rtp_ty = np.ndarray[(1 if dynamic else 2,), np.dtype[np.int32]]
        rtps = [target.rtp(rtp_ty, name=f"rtp_{k}") for k in range(n_cores)]
        barriers = [target.barrier() for _ in range(n_cores)]
        per_tile = self.cols
        param = self.vector_size.param if dynamic else None

        def core_body(
            of_in,
            of_out,
            softmax_kernel,
            mask_kernel,
            rtp,
            barrier,
            vector_size_src=None,
        ):
            barrier.wait_for_value(1)
            n = rtp[0]
            # `dynamic` is a compile-time constant, so only one of these is
            # emitted: a scratchpad parameter read or a write-RTP buffer load.
            vector_size = vector_size_src.read() if dynamic else rtp[1]
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                mask_kernel(elem_in, vector_size, per_tile)
                softmax_kernel(elem_in, elem_out, per_tile)
                of_in.release(1)
                of_out.release(1)

        workers = [
            Worker(
                core_body,
                [
                    of_ins[k].cons(),
                    of_outs[k].prod(),
                    softmax_k,
                    mask_k,
                    rtps[k],
                    barriers[k],
                ]
                + ([param] if dynamic else []),
            )
            for k in range(n_cores)
        ]
        for k in range(n_cores):
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.count.bind(rtps, 0)
        if not dynamic:
            self.vector_size.bind(rtps, 1)
        return workers


@operator
class DynamicSoftmaxOverlay(SoftmaxOverlay):
    """Softmax whose valid row length is a per-call value (llama's decode mask).

    ``vector_size_symbol`` names the device symbol the host writes, for the
    call sites that still address it by string.
    """

    vector_size_symbol: str | None = None

    vector_size = Scratchpad(np.int32)

    def value_symbol(self, value):
        return self.vector_size_symbol if value.name == "vector_size" else None


@operator
class Softmax(Operator[SoftmaxOverlay]):
    """AIE-accelerated Softmax operation"""

    rows: int = dim()

    x = In(rows, SoftmaxOverlay.cols, to=SoftmaxOverlay.x)
    y = Out(rows, SoftmaxOverlay.cols, from_=SoftmaxOverlay.y)

    @classmethod
    def _classic(cls, kwargs):
        # The legacy spelling picks the dynamic overlay by naming its symbol.
        symbol = kwargs.pop("vector_size_parameter", None)
        if symbol is not None:
            names = {
                f.name for f in SoftmaxOverlay.__dataclass_fields__.values() if f.init
            }
            ov_kwargs = {k: kwargs.pop(k) for k in list(kwargs) if k in names}
            return DynamicSoftmaxOverlay(vector_size_symbol=symbol, **ov_kwargs), kwargs
        return super()._classic(kwargs)

    @property
    def cols(self) -> int:
        return self.ov.cols

    @property
    def size(self) -> int:
        return self.rows * self.ov.cols

    def validate(self) -> None:
        if self.rows % 16 != 0:
            raise ValueError(f"rows ({self.rows}) must be a multiple of 16")

    def compatible(self) -> None:
        ov = self.ov
        if self.rows % ov.num_aie_columns:
            raise Incompatible(
                f"rows ({self.rows}) must be a multiple of num_aie_columns ({ov.num_aie_columns})"
            )
        total = ov.num_aie_columns * ov.num_channels
        if self.rows % total:
            raise Incompatible(
                f"rows ({self.rows}) must be a multiple of the {total} cores"
            )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        out = {"count": self.rows // (ov.num_aie_columns * ov.num_channels)}
        if not isinstance(ov.vector_size, BoundValue):
            out["vector_size"] = (
                ov.rtp_vector_size if ov.rtp_vector_size is not None else ov.cols
            )
        return out

    def reference(self, x):
        """CPU reference: row-wise softmax over ``cols``.

        Note: ignores a per-call ``vector_size`` (if any); the reference
        always softmaxes over the full ``cols``. For decode-style usage with
        a masked tail, the trailing positions will not match the NPU output."""
        return reference(x.reshape(self.rows, self.cols))


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------

"""Golden reference generator for softmax operator."""


def reference(x):
    """CPU reference: row-wise softmax over the last dim (ground truth)."""
    return torch.softmax(x, dim=-1)


def generate_golden_reference(rows: int, cols: int, dtype="bf16", seed=42):
    """
    Generate golden reference data for softmax.

    Returns:
        dict: Dictionary with tensors for inputs and outputs
    """
    torch.manual_seed(seed)
    val_range = 4
    input_tensor = torch.rand(rows, cols, dtype=torch_dtype_map[dtype]) * val_range
    output_tensor = reference(input_tensor)
    return {"input": input_tensor, "output": output_tensor}
