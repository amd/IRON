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
from iron.common.tiling import Walk, granule_elements, legalize, place


def _into_slot(slot, seq=128, num_channels=1) -> dict[str, Any]:
    """Kwargs scattering an (8, 64) block into slot ``slot`` of an (8, seq, 64)
    buffer: each of its rows lands ``seq * 64`` elements after the last.
    """
    return dict(
        src=Walk.of((8, 64)),
        dst=Walk.slice((8, seq, 64), (slice(None), slot)),
        input_buffer_size=8 * 64,
        output_buffer_size=8 * seq * 64,
        num_channels=num_channels,
    )


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
            Case(dict(input_buffer_size=1024), id="contiguous"),
            Case(dict(input_buffer_size=1024, num_channels=2), id="two_channels"),
            Case(dict(input_buffer_size=1024, num_channels=4), id="four_channels"),
            Case(
                dict(input_buffer_size=1024, num_channels=2, tile_size=256),
                id="two_channels_chunked",
            ),
            Case(dict(input_buffer_size=1024, tile_size=256), id="chunked_transfer"),
            Case(_into_slot(0), id="slot0"),
            Case(_into_slot(5), id="slot5"),
            Case(_into_slot(127), id="slot_last"),
            # The flat cases split a stride-1 run across the channels; these
            # split the rows of a strided scatter.
            Case(_into_slot(5, num_channels=2), id="slot5_two_channels"),
            Case(_into_slot(5, num_channels=4), id="slot5_four_channels"),
            Case(_into_slot(1000, seq=2048), id="slot1000_of_2048", extensive=True),
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
        for walk in (self.src, self.dst):
            if walk.sizes[-1] % channels:
                raise Incompatible(
                    f"the innermost axis of {walk} ({walk.sizes[-1]}) must be "
                    f"divisible by num_channels ({channels})"
                )
        per_channel = self.src.elements // channels
        if per_channel % self.tile_size:
            raise Incompatible(
                f"tile_size {self.tile_size} must divide the per-channel "
                f"transfer {per_channel} (= {self.src.elements} / {channels} channels)"
            )

    def _taps(self, buffer, walk: Walk, offset: int = 0):
        """Per channel, the descriptors of its share of the walk, each with
        the dimension a bound patches (``None`` when none does).

        Each share is legalized for the shim (an axis past its slot's wrap
        is factored or unrolled, order preserved), so a wide reorder lowers
        here instead of failing later in the toolchain. A bounded walk is one
        exact descriptor per channel or an error, its bounded axis on D2
        (dimension 1) where the walk allows: D2 has no wrap, since a shim
        descriptor's length ends it, and it is what a length patch bounds.
        A bound on the innermost axis, the one the channels split, takes one
        channel.
        """
        shares = walk.shares(self.num_channels)
        if walk.bounded is None:
            return [
                [
                    (acc, None)
                    for acc in legalize(
                        buffer.elements,
                        share.offset + offset,
                        share.sizes,
                        share.strides,
                        buffer.dtype,
                    )
                ]
                for share in shares
            ]
        rank, bounded = len(walk.sizes), walk.bounded
        dim = 4 - rank + bounded
        if dim == 3 and self.num_channels > 1:
            raise Incompatible(
                f"{walk} is bounded on the axis the {self.num_channels} channels "
                f"split; bound another axis or copy on one channel"
            )
        # At most one axis outside the bound (the iteration slot) and one or
        # two inside it (D1, D0) put the bound on D2.
        on_d2 = bounded <= 1 and 1 <= rank - bounded - 1 <= 2
        out = []
        for share in shares:
            dims = list(zip(share.sizes, share.strides))
            if on_d2:
                lead, inner = dims[:bounded], dims[bounded + 1 :]
                dims = (
                    (lead or [(1, 0)])
                    + [dims[bounded]]
                    + [(1, 0)] * (2 - len(inner))
                    + inner
                )
            acc = place(
                buffer.elements,
                share.offset + offset,
                dims,
                granule_elements(buffer.dtype),
            )
            if acc is None:
                raise Incompatible(
                    f"{walk} does not fit one descriptor per channel, which a "
                    f"bounded axis needs (its size is patched in place)"
                )
            out.append([(acc, 1 if on_d2 else dim)])
        return out

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

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
        # A DMA pattern: no kernel, so no contract to take it from. The
        # offsets are element counts, not bytes: the firmware multiplies the
        # scratchpad word by the element size before adding it into the BD
        # address register.
        src, dst = self.src, self.dst
        if src_valid is not None:
            src = src.at(int(src_valid))
        if dst_valid is not None:
            dst = dst.at(int(dst_valid))
        # Channel by channel, as the design splits the walks.
        gather = [c.offsets() + int(in_offset) for c in src.shares(self.num_channels)]
        scatter = [c.offsets() + int(out_offset) for c in dst.shares(self.num_channels)]
        out = (
            np.zeros(self.output_buffer_size, dtype=x.dtype)
            if y is None
            else y.reshape(-1)
        )
        flat = x.reshape(-1)
        for src_c, dst_c in zip(gather, scatter):
            if len(src_c) != len(dst_c):
                raise ValueError(
                    f"walk element counts differ ({len(src_c)} vs {len(dst_c)}); "
                    "src and dst must move the same number of elements"
                )
            out[dst_c] = flat[src_c]
        return out if y is None else y

    def sequence(self, rt):
        src, dst = self.src, self.dst
        ins = self._taps(self.x, src)
        outs = self._taps(self.y, dst)
        in_off = self.in_offset if self.uses_value("in_offset") else None
        out_off = self.out_offset if self.uses_value("out_offset") else None

        with rt.group() as tg:
            for c in range(self.num_channels):
                for acc, dim in ins[c]:
                    rt.fill(
                        self.x.lane(c),
                        acc,
                        group=tg,
                        offset_by=in_off,
                        size_by=None if dim is None else {dim: self.value("src_valid")},
                    )
                for acc, dim in outs[c]:
                    rt.drain(
                        self.y.lane(c),
                        acc,
                        group=tg,
                        wait=acc is outs[c][-1][0],
                        offset_by=out_off,
                        size_by=None if dim is None else {dim: self.value("dst_valid")},
                    )
