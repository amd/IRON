# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy between two views: ``Copy(k, keys[i][:, pos])``.

Each side is a walk over its buffer (offset, sizes, strides), the form a DMA
takes; the shim channels split the walk's innermost axis and each share
is legalized for the shim. A per-call value indexing a view
reaches the copy as ``in_offset``/``out_offset``, an element offset.
"""

import dataclasses
from dataclasses import field
from typing import Any

import numpy as np
from aie.iron import ObjectFifo
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, Incompatible, Operator, Out, Scratchpad, auto, param
from iron.common.testing import Case, Testing
from iron.common.tiling import Walk, _pack_exact, granule_elements, legalize

# Llama's KV-cache write, shrunk: the cache is (n_kv_groups, seq, head_dim)
# and one token's keys land in slot t of every group. SEQ is 128 rather than
# the real 2048 to keep the output buffer at 128 KB; the full-size arm is
# extensive.
_N_KV, _HEAD_DIM, _SEQ = 8, 64, 128


def _kv_slot(seq, slot, num_channels=1) -> dict[str, Any]:
    """Kwargs writing one (N_KV, HEAD_DIM) token into cache slot ``slot``."""
    return dict(
        src=Walk.of((_N_KV, _HEAD_DIM)),
        dst=Walk.slice((_N_KV, seq, _HEAD_DIM), (slice(None), slot)),
        input_buffer_size=_N_KV * _HEAD_DIM,
        output_buffer_size=_N_KV * seq * _HEAD_DIM,
        num_channels=num_channels,
    )


def _flat(size, num_channels=1, tile_size=None) -> dict[str, Any]:
    """Kwargs for a contiguous copy of ``size`` elements."""
    return dict(
        input_buffer_size=size,
        output_buffer_size=size,
        num_channels=num_channels,
        tile_size=tile_size,
    )


def _pad4(sizes, strides):
    """Pad to 4-D: dropping leading dimensions leaves BD registers uninitialised."""
    sizes, strides = list(sizes), list(strides)
    return [1] * (4 - len(sizes)) + sizes, [0] * (4 - len(strides)) + strides


def _shares(walk: Walk, num_channels: int) -> list[tuple[int, list[int], list[int]]]:
    """Per channel, the (offset, sizes, strides) of its share of a walk.

    The walk is padded to 4-D and its innermost axis split evenly; channel
    ``c`` starts ``c`` shares along that axis. The one place the split is
    defined: the descriptors, the reference and the check all read it.
    """
    sizes, strides = _pad4(walk.sizes, walk.strides)
    share, remainder = divmod(sizes[-1], num_channels)
    if remainder:
        raise Incompatible(
            f"the innermost axis of {walk} ({sizes[-1]}) must be divisible by "
            f"num_channels ({num_channels})"
        )
    split = sizes[:-1] + [share]
    return [
        (walk.offset + c * share * strides[-1], split, strides)
        for c in range(num_channels)
    ]


class Copy(Operator):
    """AIE-accelerated copy between two views of two buffers.

    Gathers by ``src`` and scatters by ``dst``, split across
    ``num_channels`` memtile pass-throughs (no cores) on the innermost
    axis. In a graph the walks come from the operands: ``Copy(k,
    keys[i][:, pos])``, ``Copy(x.transpose(1, 0, 2), y[:, :n])``; a per-call
    index on a view binds ``in_offset`` or ``out_offset``. Standalone,
    ``src``/``dst`` are given, or default to the whole of each buffer.

    Each channel's descriptor carries 1/num_channels of the walk, so the
    fifo object is sized against the per-channel share (``tile_size``). A
    descriptor shorter than the object starves the memtile's S2MM: it never
    completes an object, never releases the lock, and the drain never returns
    (ERT_CMD_STATE_TIMEOUT). An integer multiple is fine; it cycles the buffer.
    """

    # The params that take an operand's view, and the value its per-call
    # index binds, in operand order.
    accept_views = (("src", "in_offset"), ("dst", "out_offset"))

    # Copy moves data and computes nothing, so the gate is exact.
    test = Testing(
        [
            Case(_flat(1024), id="contiguous"),
            Case(_flat(1024, num_channels=2), id="two_channels"),
            Case(_flat(1024, num_channels=4), id="four_channels"),
            Case(
                _flat(1024, num_channels=2, tile_size=256),
                id="two_channels_chunked",
            ),
            Case(_flat(1024, tile_size=256), id="chunked_transfer"),
            Case(_kv_slot(_SEQ, 0), id="kv_slot0"),
            Case(_kv_slot(_SEQ, 5), id="kv_slot5"),
            Case(_kv_slot(_SEQ, _SEQ - 1), id="kv_slot_last"),
            # num_channels exists to widen the KV-cache write, so the
            # strided arms cover it too: the flat cases split a stride-1
            # run, these split head_dim.
            Case(_kv_slot(_SEQ, 5, num_channels=2), id="kv_slot5_two_channels"),
            Case(_kv_slot(_SEQ, 5, num_channels=4), id="kv_slot5_four_channels"),
            Case(_kv_slot(2048, 1000), id="kv_llama_full", extensive=True),
        ],
        tolerance=Tolerance.exact(),
    )

    input_buffer_size: int = param(repr=False)
    src: Walk = param(default=lambda op: Walk.of((op.input_buffer_size,)))
    output_buffer_size: int = param(default=lambda op: op.src.elements, repr=False)
    dst: Walk = param(default=lambda op: Walk.of((op.output_buffer_size,)))
    tile_size: int = auto()  # None: the per-channel share of the walk
    num_channels: int = auto(1)
    dtype: Any = field(default=bfloat16, repr=False)

    x = In(
        input_buffer_size,
        dtype=dtype,
        tile=(tile_size,),
        per=(num_channels,),
        depth=1,
    )
    y = Out(
        output_buffer_size,
        dtype=dtype,
        tile=(tile_size,),
        per=(num_channels,),
        depth=1,
    )
    # Per-call addends on the two base addresses, in elements.
    in_offset = Scratchpad(np.int32)
    out_offset = Scratchpad(np.int32)
    # Per-call sizes of the bounded axis of each walk (``x[:n]`` on a view),
    # in that axis's units.
    src_valid = Scratchpad(np.int32)
    dst_valid = Scratchpad(np.int32)

    def validate(self) -> None:
        if self.src.elements != self.dst.elements:
            raise ValueError(
                f"a copy moves the same element count both ways: src {self.src} "
                f"has {self.src.elements} elements, dst {self.dst} has "
                f"{self.dst.elements}"
            )

    def resolve(self, dev):
        """The transfer size is the per-channel share of the copy unless given."""
        assert self.src is not None  # validate() filled it
        tile_size = self.tile_size or self.src.elements // self.num_channels
        return dataclasses.replace(self, tile_size=tile_size)

    def uses_value(self, name: str) -> bool:
        # An offset or a size is patched only when a graph binds a handle to it.
        return name in self.used_values

    def array(self, target) -> list:

        for c in range(self.num_channels):
            fifo_in = ObjectFifo(self.x.tile, name=f"fifo_in_{c}", depth=1)
            fifo_out = fifo_in.cons().forward(name=f"fifo_out_{c}", depth=1)
            self.x.lane(c).bind(fifo_in.prod())
            self.y.lane(c).bind(fifo_out.cons())
        return []

    def compatible(self) -> None:
        channels = self.num_channels
        src, dst = self.src, self.dst
        for walk in (src, dst):
            _shares(walk, channels)  # raises when the axis does not split
        per_channel = src.elements // channels
        if per_channel % self.tile_size:
            raise Incompatible(
                f"tile_size {self.tile_size} must divide the per-channel "
                f"transfer {per_channel} (= {src.elements} / {channels} channels)"
            )

    def _taps(self, buffer, walk: Walk, offset: int = 0):
        """Per channel, the descriptors of its share of the walk, each with
        the dimension a bound patches (``None`` when none does).

        Each share is legalized for the shim (an axis past its slot's wrap
        is factored or unrolled, order preserved), so a wide reorder lowers
        here instead of failing later in the toolchain. A bounded axis must
        keep its slot, so a bounded walk is one exact descriptor per channel
        or an error; a bound on the innermost axis, the one the channels
        split, takes one channel.
        """
        shares = _shares(walk, self.num_channels)
        if walk.bounded is None:
            return [
                [
                    (acc, None)
                    for acc in legalize(
                        buffer.elements, start + offset, sizes, strides, buffer.dtype
                    )
                ]
                for start, sizes, strides in shares
            ]
        dim = 4 - len(walk.sizes) + walk.bounded
        if dim == 3 and self.num_channels > 1:
            raise Incompatible(
                f"{walk} is bounded on the axis the {self.num_channels} channels "
                f"split; bound another axis or copy on one channel"
            )
        out = []
        for start, sizes, strides in shares:
            acc = _pack_exact(
                buffer.elements,
                start + offset,
                list(zip(sizes, strides)),
                granule_elements(buffer.dtype),
            )
            if acc is None:
                raise Incompatible(
                    f"{walk} does not fit one descriptor per channel, which a "
                    f"bounded axis needs (its size is patched in place)"
                )
            out.append([(acc, dim)])
        return out

    def reference(
        self, x, y=None, *, in_offset=0, out_offset=0, src_valid=None, dst_valid=None
    ):
        """CPU reference: gather by ``src``, scatter by ``dst``.

        ``x`` is the whole input buffer and ``y`` the whole output buffer,
        written in place when given (a cache the graph passes as an output
        keeps everything the copy does not touch); otherwise a zeroed buffer
        of ``output_buffer_size``. The offsets are the per-call values, in
        elements.
        """
        src, dst = self.src, self.dst
        if src_valid is not None:
            src = _at(src, int(src_valid))
        if dst_valid is not None:
            dst = _at(dst, int(dst_valid))
        out = reference(
            x.reshape(-1),
            src,
            self.output_buffer_size,
            dst,
            self.num_channels,
            input_offset_addend=int(in_offset),
            output_offset_addend=int(out_offset),
            into=None if y is None else y.reshape(-1),
        )
        return out if y is None else y

    def sequence(self, rt):
        src, dst = self.src, self.dst
        ins = self._taps(self.x, src)
        outs = self._taps(self.y, dst)
        in_off = self.in_offset if self.uses_value("in_offset") else None
        out_off = self.out_offset if self.uses_value("out_offset") else None

        def size_by(dim, name):
            return {dim: self.value(name)} if dim is not None else None

        with rt.group() as tg:
            for c in range(self.num_channels):
                for acc, dim in ins[c]:
                    rt.fill(
                        self.x.lane(c),
                        acc,
                        group=tg,
                        offset_by=in_off,
                        size_by=size_by(dim, "src_valid"),
                    )
                for acc, dim in outs[c]:
                    rt.drain(
                        self.y.lane(c),
                        acc,
                        group=tg,
                        wait=acc is outs[c][-1][0],
                        offset_by=out_off,
                        size_by=size_by(dim, "dst_valid"),
                    )


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def _at(walk: Walk, valid: int) -> Walk:
    """The walk with its bounded axis at ``valid``: what one call moves."""
    if walk.bounded is None:
        raise ValueError(f"{walk} has no bounded axis to set to {valid}")
    sizes = list(walk.sizes)
    sizes[walk.bounded] = valid
    return dataclasses.replace(walk, sizes=tuple(sizes), bounded=None)


def _walk_offsets(sizes, strides, offset):
    """Flat element offsets a walk visits, in issue order."""
    grids = np.meshgrid(*[np.arange(s) for s in sizes], indexing="ij")
    flat = np.full(grids[0].shape, offset, dtype=np.int64)
    for grid, stride in zip(grids, strides):
        flat = flat + grid * stride
    return flat.reshape(-1)


def _channel_offsets(walk: Walk, addend: int, num_channels: int):
    """Per channel, the flat offsets of its share, split as the design splits it."""
    return [
        _walk_offsets(sizes, strides, start + addend)
        for start, sizes, strides in _shares(walk, num_channels)
    ]


def reference(
    input_flat,
    src: Walk,
    output_buffer_size,
    dst: Walk,
    num_channels=1,
    input_offset_addend=0,
    output_offset_addend=0,
    into=None,
):
    """Gather by ``src``, scatter by ``dst``, one channel at a time.

    The addends are the per-call offsets. They are element counts, not byte
    offsets: the firmware multiplies the scratchpad word by the element size
    before adding it into the BD address register. ``into`` is an existing
    flat output buffer to scatter into in place; without it the output
    starts zeroed.
    """
    gather = _channel_offsets(src, input_offset_addend, num_channels)
    scatter = _channel_offsets(dst, output_offset_addend, num_channels)
    out = (
        np.zeros(int(output_buffer_size), dtype=input_flat.dtype)
        if into is None
        else into
    )
    for src_c, dst_c in zip(gather, scatter):
        if len(src_c) != len(dst_c):
            raise ValueError(
                f"walk element counts differ ({len(src_c)} vs {len(dst_c)}); "
                "src and dst must move the same number of elements"
            )
        out[dst_c] = input_flat[src_c]
    return out
