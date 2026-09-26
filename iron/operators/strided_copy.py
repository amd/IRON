# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from dataclasses import field

import numpy as np
from ml_dtypes import bfloat16

from aie.utils.verify import Tolerance

from iron.common.declare import (
    BoundBuffer,
    In,
    Operator,
    Order,
    Out,
    Overlay,
    Scratchpad,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)
from iron.common.testing import Case, Testing
from iron.common.tiling import legalize


@operator
class StridedCopyOverlay(Overlay):
    """A memtile pass-through, one channel per fifo; no cores.

    Each channel's descriptor carries 1/num_aie_channels of the tensor, so the
    fifo object is sized against the per-channel share (``transfer_size``). A
    descriptor shorter than the object starves the memtile's S2MM: it never
    completes an object, never releases the lock, and the drain never returns
    (ERT_CMD_STATE_TIMEOUT). An integer multiple is fine; it cycles the buffer.
    """

    # Derived from input_sizes by the constructor (per-channel share).
    transfer_size: int | None = tunable(None)
    num_aie_channels: int = tunable(1)
    dtype: object = field(default=bfloat16, repr=False)

    s = StreamIn(transfer_size, dtype=dtype, per=num_aie_channels, depth=1)
    d = StreamOut(transfer_size, dtype=dtype, per=num_aie_channels, depth=1)

    def design(self, target) -> list:
        from aie.iron import ObjectFifo

        for c in range(self.num_aie_channels):
            fifo_in = ObjectFifo(self.s.tile, name=f"fifo_in_{c}", depth=1)
            fifo_out = fifo_in.cons().forward(name=f"fifo_out_{c}", depth=1)
            self.s[c].bind(fifo_in.prod())
            self.d[c].bind(fifo_out.cons())
        return []


# Llama's KV-cache write, shrunk: the cache is (n_kv_groups, seq, head_dim)
# and one token's keys land in slot t of every group. SEQ is 128 rather than
# the real 2048 to keep the output buffer at 128 KB; the full-size arm is
# extensive.
_N_KV, _HEAD_DIM, _SEQ = 8, 64, 128


def _kv_slot(seq, slot, num_aie_channels=1):
    """Kwargs writing one (N_KV, HEAD_DIM) token into cache slot ``slot``."""
    return dict(
        input_sizes=[_N_KV, _HEAD_DIM],
        input_strides=[_HEAD_DIM, 1],
        input_offset=0,
        input_buffer_size=_N_KV * _HEAD_DIM,
        output_sizes=[1, _N_KV, _HEAD_DIM],
        output_strides=[0, seq * _HEAD_DIM, 1],
        output_offset=slot * _HEAD_DIM,
        output_buffer_size=_N_KV * seq * _HEAD_DIM,
        num_aie_channels=num_aie_channels,
    )


def _flat(size, num_aie_channels=1, transfer_size=None):
    """Kwargs for a contiguous copy of ``size`` elements."""
    return dict(
        input_sizes=[size],
        input_strides=[1],
        input_offset=0,
        input_buffer_size=size,
        output_sizes=[size],
        output_strides=[1],
        output_offset=0,
        output_buffer_size=size,
        num_aie_channels=num_aie_channels,
        transfer_size=transfer_size,
    )


def _pad4(sizes, strides):
    """Pad to 4-D: dropping leading dimensions leaves BD registers uninitialised."""
    sizes, strides = list(sizes), list(strides)
    return [1] * (4 - len(sizes)) + sizes, [0] * (4 - len(strides)) + strides


@operator
class StridedCopy(Operator[StridedCopyOverlay]):
    """AIE-accelerated strided copy operator.

    Gathers by the input pattern and scatters by the output pattern, split
    across the overlay's channels on the highest-index non-unit dimension.
    Useful for data layout manipulation such as ``input[0, :, 0] -> output[:, 0, 0]``.
    """

    # StridedCopy moves data and computes nothing, so the gate is exact.
    test = Testing(
        [
            Case(_flat(1024), id="contiguous"),
            Case(_flat(1024, num_aie_channels=2), id="two_channels"),
            Case(_flat(1024, num_aie_channels=4), id="four_channels"),
            Case(
                _flat(1024, num_aie_channels=2, transfer_size=256),
                id="two_channels_chunked",
            ),
            Case(_flat(1024, transfer_size=256), id="chunked_transfer"),
            Case(_kv_slot(_SEQ, 0), id="kv_slot0"),
            Case(_kv_slot(_SEQ, 5), id="kv_slot5"),
            Case(_kv_slot(_SEQ, _SEQ - 1), id="kv_slot_last"),
            # The KV-cache write is what num_aie_channels exists to widen, so
            # it carries the strided arms too: the flat cases split a
            # stride-1 run, these split head_dim.
            Case(_kv_slot(_SEQ, 5, num_aie_channels=2), id="kv_slot5_two_channels"),
            Case(_kv_slot(_SEQ, 5, num_aie_channels=4), id="kv_slot5_four_channels"),
            Case(_kv_slot(2048, 1000), id="kv_llama_full", extensive=True),
        ],
        tolerance=Tolerance.exact(),
    )

    input_buffer_size: int = dim(repr=False)
    output_buffer_size: int = dim(repr=False)
    input_sizes: tuple = ()
    input_strides: tuple = ()
    input_offset: int = 0
    output_sizes: tuple = ()
    output_strides: tuple = ()
    output_offset: int = 0
    x = In(input_buffer_size, dtype=StridedCopyOverlay.dtype, to=StridedCopyOverlay.s)
    y = Out(
        output_buffer_size, dtype=StridedCopyOverlay.dtype, from_=StridedCopyOverlay.d
    )
    # Per-call addends on the two base addresses, patched into the descriptors.
    in_offset = Scratchpad(np.int32)
    out_offset = Scratchpad(np.int32)

    @classmethod
    def overlay_defaults(cls, kwargs):
        """The transfer size is the per-channel share of the copy unless given."""
        if kwargs.get("transfer_size") is None:
            sizes = kwargs.get("input_sizes", ())
            channels = kwargs.get("num_aie_channels", 1)
            kwargs["transfer_size"] = int(np.prod(sizes)) // channels

    def uses_value(self, name: str) -> bool:
        # An offset is patched only when a graph binds a handle to it.
        return name in self.used_values

    @property
    def transfer_size(self) -> int:
        return self.ov.transfer_size

    @property
    def num_aie_channels(self) -> int:
        return self.ov.num_aie_channels

    @property
    def dtype(self):
        return self.ov.dtype

    def validate(self) -> None:
        if len(self.input_sizes) != len(self.input_strides):
            raise ValueError(
                f"input_sizes and input_strides must have the same length "
                f"({len(self.input_sizes)} vs {len(self.input_strides)})"
            )
        if len(self.output_sizes) != len(self.output_strides):
            raise ValueError(
                f"output_sizes and output_strides must have the same length "
                f"({len(self.output_sizes)} vs {len(self.output_strides)})"
            )
        n_in, n_out = int(np.prod(self.input_sizes)), int(np.prod(self.output_sizes))
        if n_in != n_out:
            raise ValueError(
                f"a copy moves the same element count both ways: input_sizes "
                f"{list(self.input_sizes)} has {n_in} elements, output_sizes "
                f"{list(self.output_sizes)} has {n_out}"
            )

    def compatible(self) -> None:
        from iron.common.declare import Incompatible

        channels = self.ov.num_aie_channels
        for label, sizes in (
            ("input_sizes", self.input_sizes),
            ("output_sizes", self.output_sizes),
        ):
            padded, _ = _pad4(sizes, sizes)
            highest = max(i for i, sz in enumerate(padded) if sz >= 1)
            if padded[highest] % channels:
                raise Incompatible(
                    f"Highest dimension of {label} must be divisible by num_aie_channels"
                )
        per_channel = int(np.prod(self.input_sizes)) // channels
        if per_channel % self.ov.transfer_size:
            raise Incompatible(
                f"transfer_size {self.ov.transfer_size} must divide the per-channel transfer "
                f"{per_channel} (= {int(np.prod(self.input_sizes))} / {channels} channels)"
            )

    def _taps(self, buffer, sizes, strides, offset):
        """Per channel, the descriptors of its share of the pattern.

        The highest non-unit dimension is split across the channels; each
        share is then legalized for the shim (a dimension past its slot's
        wrap is factored or unrolled, order preserved), so a reorder as wide
        as a sequence lowers rather than failing three tools down.
        """
        sizes, strides = _pad4(sizes, strides)
        highest = max(i for i, sz in enumerate(sizes) if sz >= 1)
        channels = self.ov.num_aie_channels
        share = sizes[highest] // channels
        split = sizes[:highest] + [share] + sizes[highest + 1 :]
        return [
            legalize(
                buffer.elements,
                offset + c * share * strides[highest],
                split,
                strides,
                buffer.dtype,
            )
            for c in range(channels)
        ]

    def reference(self, x, y=None, *, in_offset=0, out_offset=0):
        """CPU reference: gather by the input tap, scatter by the output tap.

        ``y`` is the output buffer to write into, in place, when given (a
        cache the graph passes as an output keeps everything the copy does
        not touch); otherwise a zeroed buffer of ``output_buffer_size``. The
        offsets are the per-call values, in elements.
        """
        out = reference(
            x.reshape(-1),
            self.input_sizes,
            self.input_strides,
            self.input_offset,
            self.output_buffer_size,
            self.output_sizes,
            self.output_strides,
            self.output_offset,
            self.ov.num_aie_channels,
            input_offset_addend=int(in_offset),
            output_offset_addend=int(out_offset),
            into=None if y is None else y.reshape(-1),
        )
        return out if y is None else y

    def order(self, buffer: BoundBuffer) -> Order:
        """Per channel, its share of the gather (``x``) or the scatter
        (``y``), shifted per call by the offset a graph binds, if any."""
        if buffer is self.x:
            taps = self._taps(
                self.x, self.input_sizes, self.input_strides, self.input_offset
            )
            by = self.in_offset if self.uses_value("in_offset") else None
            return Order(self.ov.s, tuple(map(tuple, taps)), offset_by=by)
        taps = self._taps(
            self.y, self.output_sizes, self.output_strides, self.output_offset
        )
        by = self.out_offset if self.uses_value("out_offset") else None
        return Order(self.ov.d, tuple(map(tuple, taps)), offset_by=by)

    def design(self, rt):
        """One group; per channel its fills, then its drains, the last one waited."""
        src, dst = self.order(self.x), self.order(self.y)
        with rt.group() as tg:
            for c in range(self.ov.num_aie_channels):
                for acc in src[c]:
                    rt.fill(
                        self.ov.s[c], (self.x, acc), group=tg, offset_by=src.offset_by
                    )
                for i, acc in enumerate(dst[c]):
                    rt.drain(
                        self.ov.d[c],
                        (self.y, acc),
                        group=tg,
                        wait=i == len(dst[c]) - 1,
                        offset_by=dst.offset_by,
                    )


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def _pad_to_4d(sizes, strides):
    """design.py pads access patterns to 4D before building the taps; the reference
    has to pad identically or the per-channel split lands on a different dimension."""
    return (
        [1] * (4 - len(sizes)) + list(sizes),
        [0] * (4 - len(strides)) + list(strides),
    )


def _tap_offsets(sizes, strides, offset):
    """Flat element offsets a TensorAccessPattern visits, in issue order."""
    grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
    flat = np.full(grids[0].shape, offset, dtype=np.int64)
    for grid, stride in zip(grids, strides):
        flat = flat + grid * stride
    return flat.reshape(-1)


def _channel_offsets(sizes, strides, offset, num_aie_channels):
    sizes, strides = _pad_to_4d(sizes, strides)
    highest = max(idx for idx, sz in enumerate(sizes) if sz >= 1)
    per_channel = sizes[highest] // num_aie_channels
    split = sizes[:highest] + [per_channel] + sizes[highest + 1 :]
    return [
        _tap_offsets(split, strides, offset + c * per_channel * strides[highest])
        for c in range(num_aie_channels)
    ]


def reference(
    input_flat,
    input_sizes,
    input_strides,
    input_offset,
    output_buffer_size,
    output_sizes,
    output_strides,
    output_offset,
    num_aie_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
    into=None,
):
    """Gather by the input tap, scatter by the output tap, one channel at a time.

    The addends are the *_offset_parameter values. They are element counts, not byte
    offsets: the firmware multiplies the scratchpad word by the element size before
    adding it into the BD address register. ``into`` is an existing flat output
    buffer to scatter into in place; without it the output starts zeroed.
    """
    src = _channel_offsets(
        input_sizes, input_strides, input_offset + input_offset_addend, num_aie_channels
    )
    dst = _channel_offsets(
        output_sizes,
        output_strides,
        output_offset + output_offset_addend,
        num_aie_channels,
    )

    out = (
        np.zeros(int(output_buffer_size), dtype=input_flat.dtype)
        if into is None
        else into
    )
    for src_c, dst_c in zip(src, dst):
        if len(src_c) != len(dst_c):
            raise ValueError(
                f"tap element counts differ ({len(src_c)} vs {len(dst_c)}); "
                "the input and output access patterns must move the same number "
                "of elements"
            )
        out[dst_c] = input_flat[src_c]
    return out
