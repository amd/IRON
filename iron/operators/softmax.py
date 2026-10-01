# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


import ml_dtypes
from aie.extras.dialects import arith
from aie.iron.kernels import activation, zero
import numpy as np

from aie.utils.verify import Tolerance

from iron.common.declare import (
    BoundBuffer,
    BoundValue,
    Incompatible,
    In,
    Operator,
    Order,
    Out,
    Overlay,
    Resident,
    Scratchpad,
    StreamIn,
    StreamOut,
    dim,
    operator,
    optional,
    tunable,
)
from iron.common.testing import Case, Testing, device_columns
from iron.common.tiling import encode, split

# softmax_bf16's vector step on both targets (activation.softmax holds a
# row to a multiple of it). Its loops cover only whole steps.
_VECTOR_STEP = 32


@operator
class SoftmaxOverlay(Overlay):
    """The array for row-wise softmax: one core per (column, channel), one row per tile.

    Each row is masked to ``vector_size`` valid elements before the softmax;
    here that is a resident the sequence writes once per build
    (``rtp_vector_size``, default the full row). ``vector_size`` must be at
    least 1.

    The kernels only run over the span: ``vector_size`` rounded up to the
    softmax's 32-element vector step. Past it the masked elements' exponents
    are exact zeros, so leaving them out of the lanes' sums changes no bit;
    the output past the span is zero-filled instead of computed.

    ``causal`` is attention's mask: each row sees one element more than the
    row before it, ``vector_size`` the first row's (default one), counted
    again from the first row of every batch. A core runs ``batches`` runs of
    ``count`` rows, core ``k`` starting each at row ``k * core_offset`` of its
    batch: whole batches with no offset, or a block of every batch's rows.
    A causal row's span changes every row, so it runs over the whole row.
    """

    cols: int = dim()
    num_aie_columns: int = tunable(1)
    num_channels: int = tunable(1)
    rtp_vector_size: int | None = None
    causal: bool = False

    x = StreamIn(cols, per=(num_aie_columns, num_channels))
    y = StreamOut(cols, per=(num_aie_columns, num_channels))
    count = Resident(np.int32)
    vector_size = Resident(np.int32)
    # Causal only: the rows restart their count once per batch, and core k
    # starts it at row k * core_offset.
    batches = Resident(np.int32, optional=True)
    core_offset = Resident(np.int32, optional=True)

    def validate(self) -> None:
        if self.cols % 16 != 0:
            raise ValueError(f"cols ({self.cols}) must be a multiple of 16")

    @property
    def first_vector_size(self) -> int:
        """The valid length of the first row: every row's, unless causal."""
        if self.rtp_vector_size is not None:
            return self.rtp_vector_size
        return 1 if self.causal else self.cols

    def _kernels(self, tile_ty):
        softmax_k = activation.softmax(self.cols)
        # mask_bf16 is exported by the same softmax.cc translation unit.
        mask_k = softmax_k.object_file.bind("mask_bf16", [tile_ty, np.int32, np.int32])
        zero_k = zero(self.cols, ml_dtypes.bfloat16)
        return softmax_k, mask_k, zero_k

    def design(self, target) -> list:
        from aie.iron import Buffer, ObjectFifo, Worker
        from aie.iron.controlflow import range_

        tile_ty = self.x.tile
        cols, chans = self.num_aie_columns, self.num_channels
        n_cores = cols * chans
        softmax_k, mask_k, zero_k = self._kernels(tile_ty)
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
        # Causal: [count, vector_size, batches, core_offset].
        dynamic = isinstance(self.vector_size, BoundValue) and target.image == "elf"
        causal = self.causal
        words = 1 if dynamic else 4 if causal else 2
        rtp_ty = np.ndarray[(words,), np.dtype[np.int32]]
        rtps = [target.rtp(rtp_ty, name=f"rtp_{k}") for k in range(n_cores)]
        barriers = [target.barrier() for _ in range(n_cores)]
        per_tile = self.cols
        param = self.vector_size.param if dynamic else None

        def core_body(
            of_in,
            of_out,
            softmax_kernel,
            mask_kernel,
            zero_kernel,
            rtp,
            barrier,
            vector_size_src=None,
        ):
            barrier.wait_for_value(1)
            n = rtp[0]
            # `dynamic` is a compile-time constant, so only one of these is
            # emitted: a scratchpad parameter read or a write-RTP buffer load.
            vector_size = vector_size_src.read() if dynamic else rtp[1]
            i32 = vector_size.type
            span = arith.minsi(
                arith.andi(
                    arith.addi(vector_size, arith.constant(_VECTOR_STEP - 1, i32)),
                    arith.constant(-_VECTOR_STEP, i32),
                ),
                arith.constant(per_tile, i32),
            )
            for _ in range_(n):
                elem_in = of_in.acquire(1)
                elem_out = of_out.acquire(1)
                zero_kernel(elem_out)
                mask_kernel(elem_in, vector_size, span)
                softmax_kernel(elem_in, elem_out, span)
                of_in.release(1)
                of_out.release(1)

        def causal_body(
            of_in, of_out, softmax_kernel, mask_kernel, rtp, barrier, core, valid
        ):
            barrier.wait_for_value(1)
            n = rtp[0]
            for _ in range_(rtp[2]):
                # This core's first row of the batch.
                valid[0] = rtp[1] + core * rtp[3]
                for _ in range_(n):
                    elem_in = of_in.acquire(1)
                    elem_out = of_out.acquire(1)
                    mask_kernel(elem_in, valid[0], per_tile)
                    softmax_kernel(elem_in, elem_out, per_tile)
                    of_in.release(1)
                    of_out.release(1)
                    valid[0] += 1

        def worker(k):
            args = [of_ins[k].cons(), of_outs[k].prod(), softmax_k, mask_k]
            if causal:
                # The running valid length, as the core counts it.
                valid = Buffer(
                    initial_value=np.zeros(1, dtype=np.int32), name=f"valid_{k}"
                )
                return Worker(causal_body, args + [rtps[k], barriers[k], k, valid])
            args += [zero_k, rtps[k], barriers[k]]
            return Worker(core_body, args + ([param] if dynamic else []))

        workers = [worker(k) for k in range(n_cores)]
        for k in range(n_cores):
            self.x[k].bind(of_ins[k].prod())
            self.y[k].bind(of_outs[k].cons())
        self.count.bind(rtps, 0)
        if not dynamic:
            self.vector_size.bind(rtps, 1)
        if causal:
            self.batches.bind(rtps, 2)
            self.core_offset.bind(rtps, 3)
        return workers


@operator
class DynamicSoftmaxOverlay(SoftmaxOverlay):
    """Softmax whose valid row length is a per-call value (llama's decode mask)."""

    vector_size = Scratchpad(np.int32)

    def validate(self) -> None:
        super().validate()
        if self.causal:
            raise ValueError("a causal softmax takes its first row's length resident")


def _columns_channels(total_cores):
    """The (columns, channels) split for a core count: 2x2 from four cores up
    (a 4x4 has placement issues on Phoenix), 1x2 for two, 1x1 for one."""
    return {1: (1, 1), 2: (1, 2)}.get(total_cores, (2, 2))


def _row_cases():
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


def _cases():
    """The row cases, and attention's scores, one batch per head: causal at
    the scaled Llama's size, over several whole batches per core, and over a
    longer row than the batch has rows, a causal mask that starts past the
    first column, and batches without a mask; two cores per column, over
    every column, as the Llama graph runs it. Extensive: Llama's heads, and
    fewer heads than cores at its length."""
    out = _row_cases()
    for batches, rows, cols, extra, extensive in [
        (16, 64, 64, dict(causal=True), False),
        (64, 32, 128, dict(causal=True), False),
        (3, 256, 512, dict(causal=True), False),
        (2, 128, 256, dict(causal=True, rtp_vector_size=100), False),
        (4, 128, 256, {}, False),
        (32, 2048, 2048, dict(causal=True), True),
        (4, 2048, 2048, dict(causal=True), True),
    ]:
        out.append(
            Case(
                dict(
                    batches=batches,
                    rows=rows,
                    cols=cols,
                    num_aie_columns=device_columns(),
                    num_channels=2,
                    **extra,
                ),
                extensive=extensive,
            )
        )
    return out


@operator
class Softmax(Operator[SoftmaxOverlay]):
    """AIE-accelerated Softmax operation"""

    test = Testing(_cases, tolerance=Tolerance.relative(0.04, 1e-6))

    rows: int = dim()
    # Independent (rows, cols) softmaxes: a causal mask restarts per batch.
    # A single batch carries no batch dimension at all.
    batches: int = dim(1)

    x = In(optional(batches), rows, SoftmaxOverlay.cols, to=SoftmaxOverlay.x)
    y = Out(optional(batches), rows, SoftmaxOverlay.cols, from_=SoftmaxOverlay.y)

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

    @property
    def cores(self) -> int:
        return self.ov.num_aie_columns * self.ov.num_channels

    @property
    def whole_batches(self) -> bool:
        """Each core takes a contiguous run of the rows of every batch at
        once: its share of whole batches, or with no mask any rows at all.
        Otherwise it takes a block of each batch's rows, a descriptor per
        batch, which the shim's sixteen hold only a few batches of."""
        return not self.ov.causal or self.batches % self.cores == 0

    def compatible(self) -> None:
        total = self.cores
        if self.whole_batches:
            if self.batches * self.rows % total:
                raise Incompatible(
                    f"{self.batches} batches of {self.rows} rows do not divide "
                    f"across the {total} cores"
                )
        elif self.rows % total:
            raise Incompatible(
                f"rows ({self.rows}) must be a multiple of the {total} cores, "
                f"or the batches ({self.batches}) of them"
            )

    def order(self, buffer: BoundBuffer) -> Order:
        """Whole batches: each slot a contiguous block of every batch's rows,
        one descriptor. Otherwise the derived block of each batch's rows."""
        if not self.whole_batches:
            return super().order(buffer)
        stream = buffer.stream(self.ov)
        blocks = split((self.batches * self.rows, self.cols), stream.count, 0)
        return Order(
            stream,
            tuple(tuple(encode(b, buffer.elements, buffer.dtype)) for b in blocks),
        )

    def residents(self) -> dict[str, int]:
        ov = self.ov
        total = self.batches * self.rows // self.cores
        if not ov.causal:
            # The mask does not restart, so a core's rows are one run.
            out = {"count": total}
        elif self.whole_batches:
            batches = total // self.rows
            out = {"count": self.rows, "batches": batches, "core_offset": 0}
        else:
            count = self.rows // self.cores
            out = {"count": count, "batches": self.batches, "core_offset": count}
        if not isinstance(ov.vector_size, BoundValue):
            out["vector_size"] = ov.first_vector_size
        return out

    def reference(self, x, vector_size=None):
        """CPU reference: row-wise softmax over the first ``vector_size`` of ``cols``.

        The kernel fills ``[vector_size, cols)`` with the lowest bf16 before
        the softmax, so the masked tail comes out as exact zeros. Without a
        per-call value the resident one applies (``rtp_vector_size``, default
        the full row, or one for a causal mask's first row).
        """
        if vector_size is None:
            vector_size = self.ov.first_vector_size
        shape = (self.batches, self.rows, self.cols)
        y = reference(x.reshape(shape), int(vector_size), causal=self.ov.causal)
        return y.reshape(self.y.shape)


@operator
class DynamicSoftmax(Softmax, Operator[DynamicSoftmaxOverlay]):
    """Softmax whose valid row length is a per-call value: ``Softmax(x,
    vector_size=n)`` in a graph with ``n`` a per-call handle."""

    # Not causal, which takes its first row's length resident.
    test = Testing(_row_cases, tolerance=Tolerance.relative(0.04, 1e-6))

    x = In(
        optional(Softmax.batches),
        Softmax.rows,
        SoftmaxOverlay.cols,
        to=SoftmaxOverlay.x,
    )
    y = Out(
        optional(Softmax.batches),
        Softmax.rows,
        SoftmaxOverlay.cols,
        from_=SoftmaxOverlay.y,
    )


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------

"""Golden reference generator for softmax operator."""


def reference(x, vector_size=None, causal=False):
    """CPU reference: row-wise softmax over the last dim (ground truth).

    ``vector_size`` masks every column from there on to the lowest value of
    the dtype first, as the device kernel does, so those come out as zeros.
    ``causal`` masks row ``r`` of the last two dims from ``vector_size + r``
    on instead (``vector_size`` defaulting to one).
    """
    if causal:
        first = 1 if vector_size is None else vector_size
        rows, cols = x.shape[-2:]
        valid = first + np.arange(rows)[:, None]
        lowest = np.asarray(ml_dtypes.finfo(x.dtype).min, dtype=x.dtype)
        x = np.where(np.arange(cols)[None, :] < valid, x, lowest)
    elif vector_size is not None and vector_size < x.shape[-1]:
        x = x.copy()
        x[..., vector_size:] = ml_dtypes.finfo(x.dtype).min
    # In float32 and rounded once, as torch does internally for a bf16 input.
    f = x.astype(np.float32)
    e = np.exp(f - f.max(axis=-1, keepdims=True))
    return (e / e.sum(axis=-1, keepdims=True)).astype(x.dtype)
