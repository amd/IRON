# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import ml_dtypes
from aie.iron.kernels import activation
import numpy as np

from aie.utils.verify import Tolerance

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
from iron.common.testing import Case, Testing, device_columns


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

    def _kernels(self, tile_ty):
        softmax_k = activation.softmax(self.cols)
        # mask_bf16 is exported by the same softmax.cc translation unit.
        mask_k = softmax_k.object_file.bind("mask_bf16", [tile_ty, np.int32, np.int32])
        return softmax_k, mask_k

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_ty = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        softmax_k, mask_k = self._kernels(tile_ty)
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
        # [count, vector_size] per core, or [count] when vector_size is a
        # scratchpad value the core reads. On an image without a scratchpad
        # the per-call value is written into [1] by the sequence instead.
        dynamic = isinstance(self.vector_size, BoundValue) and target.image == "elf"
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
    """Softmax whose valid row length is a per-call value (llama's decode mask)."""

    vector_size = Scratchpad(np.int32)


def _columns_channels(total_cores):
    """The (columns, channels) split for a core count: 2x2 from four cores up
    (a 4x4 has placement issues on Phoenix), 1x2 for two, 1x1 for one."""
    return {1: (1, 1), 2: (1, 2)}.get(total_cores, (2, 2))


def _cases():
    out = []
    for size, cols in [(32768, 1024), (32768, 512), (32768, 2048)]:
        columns, channels = _columns_channels(size // cols)
        if columns > device_columns():
            continue
        out.append(
            Case(
                dict(
                    rows=size // cols,
                    cols=cols,
                    num_aie_columns=columns,
                    num_channels=channels,
                )
            )
        )
    return out


@operator
class Softmax(Operator[SoftmaxOverlay]):
    """AIE-accelerated Softmax operation"""

    test = Testing(_cases, tolerance=Tolerance.relative(0.04, 1e-6))

    rows: int = dim()

    x = In(rows, SoftmaxOverlay.cols, to=SoftmaxOverlay.x)
    y = Out(rows, SoftmaxOverlay.cols, from_=SoftmaxOverlay.y)

    @classmethod
    def resolve_class(cls, n_operands, kwargs):
        # Softmax(x, vector_size=<per-call value>) in a graph is the dynamic form.
        v = kwargs.get("vector_size")
        if cls is Softmax and v is not None and not isinstance(v, int):
            return DynamicSoftmax
        return cls

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

    def reference(self, x, vector_size=None):
        """CPU reference: row-wise softmax over the first ``vector_size`` of ``cols``.

        The kernel fills ``[vector_size, cols)`` with the lowest bf16 before
        the softmax, so the masked tail comes out as exact zeros. Without a
        per-call value the resident one applies (``rtp_vector_size``, default
        the full row).
        """
        if vector_size is None:
            ov = self.ov
            vector_size = (
                ov.rtp_vector_size if getattr(ov, "rtp_vector_size", None) else ov.cols
            )
        return reference(x.reshape(self.rows, self.cols), int(vector_size))


@operator
class DynamicSoftmax(Softmax, Operator[DynamicSoftmaxOverlay]):
    """Softmax whose valid row length is a per-call value: ``Softmax(x,
    vector_size=n)`` in a graph with ``n`` a per-call handle."""

    x = In(Softmax.rows, SoftmaxOverlay.cols, to=SoftmaxOverlay.x)
    y = Out(Softmax.rows, SoftmaxOverlay.cols, from_=SoftmaxOverlay.y)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------

"""Golden reference generator for softmax operator."""


def reference(x, vector_size=None):
    """CPU reference: row-wise softmax over the last dim (ground truth).

    ``vector_size`` masks every column from there on to the lowest value of
    the dtype first, as the device kernel does, so those come out as zeros.
    """
    if vector_size is not None and vector_size < x.shape[-1]:
        x = x.copy()
        x[..., vector_size:] = ml_dtypes.finfo(x.dtype).min
    # In float32 and rounded once, as torch does internally for a bf16 input.
    f = x.astype(np.float32)
    e = np.exp(f - f.max(axis=-1, keepdims=True))
    return (e / e.sum(axis=-1, keepdims=True)).astype(x.dtype)
