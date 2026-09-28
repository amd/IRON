# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy between two views: ``Copy(k, keys[i][:, pos])``.

Each side is an access pattern over its buffer (offset, sizes, strides), the
form a DMA takes; the shim channels split its innermost axis, and the
compiler splits a share no one descriptor holds. A per-call value indexing a
view reaches the copy as ``in_offset``/``out_offset``, an element offset.
"""

import dataclasses
from dataclasses import field
from math import gcd, prod
from typing import Any

import aie.utils as aie_utils
import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import ObjectFifo
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, Incompatible, Operator, Out, Scratchpad, auto, param
from iron.common.testing import Case, Testing


def _into_slot(slot, seq=128, num_channels=1) -> dict[str, Any]:
    """Kwargs scattering an (8, 64) block into slot ``slot`` of an (8, seq, 64)
    buffer: each of its rows lands ``seq * 64`` elements after the last.
    """
    return dict(
        src=TensorAccessPattern.from_slice((8, 64), ()),
        dst=TensorAccessPattern.from_slice((8, seq, 64), np.s_[:, slot]),
        input_buffer_size=8 * 64,
        output_buffer_size=8 * seq * 64,
        num_channels=num_channels,
    )


class Copy(Operator):
    """AIE-accelerated copy between two views of two buffers.

    Gathers by ``src`` and scatters by ``dst``, split across
    ``num_channels`` memtile pass-throughs (no cores) on the innermost
    axis. In a graph the patterns come from the operands: ``Copy(k,
    keys[i][:, pos])``, ``Copy(x.transpose(1, 0, 2), y[:, :n])``; a per-call
    index on a view binds ``in_offset`` or ``out_offset``, and a per-call
    bound ``src_bound``/``dst_bound`` with its size. Standalone,
    ``src``/``dst`` are given, or default to the whole of each buffer.

    Each channel's descriptor carries 1/num_channels of the pattern, so the
    fifo object is sized against the per-channel share (``tile_size``). A
    descriptor shorter than the object starves the memtile's S2MM: it never
    completes an object, never releases the lock, and the drain never returns
    (ERT_CMD_STATE_TIMEOUT). An integer multiple is fine; it cycles the buffer.
    Under a bound a call moves any whole number of the bounded axis's rows,
    so the object divides one row's share.
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
    src: TensorAccessPattern = param(
        default=lambda op: TensorAccessPattern.from_slice((op.input_buffer_size,), ())
    )
    output_buffer_size: int = param(default=lambda op: prod(op.src.sizes), repr=False)
    dst: TensorAccessPattern = param(
        default=lambda op: TensorAccessPattern.from_slice((op.output_buffer_size,), ())
    )
    # The axis of each pattern a graph bounds per call (``x[:n]`` on a view):
    # its size is the full extent in the pattern and patched to the call's.
    src_bound: int | None = param(default=None)
    dst_bound: int | None = param(default=None)
    tile_size: int = auto()  # None: the per-channel share of the pattern
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
    # Per-call sizes of the bounded axis of each pattern, in that axis's units.
    src_valid = Scratchpad(np.int32)
    dst_valid = Scratchpad(np.int32)

    def validate(self) -> None:
        if prod(self.src.sizes) != prod(self.dst.sizes):
            raise ValueError(
                f"a copy moves the same element count both ways: src {self.src} "
                f"has {prod(self.src.sizes)} elements, dst {self.dst} has "
                f"{prod(self.dst.sizes)}"
            )

    def resolve(self, dev):
        """The transfer size is the per-channel share of the copy unless
        given, or under a bound the share of one bounded row.
        """
        share = prod(self.src.sizes) // self.num_channels
        tile_size = self.tile_size or gcd(share, *self._row_shares())
        return dataclasses.replace(self, tile_size=tile_size)

    def uses_value(self, name: str) -> bool:
        # An offset or a size is patched only when a graph binds a handle to it.
        return name in self.bound_values

    def array(self, target) -> list:

        for c in range(self.num_channels):
            fifo_in = ObjectFifo(self.x.tile, name=f"fifo_in_{c}", depth=1)
            fifo_out = fifo_in.cons().forward(name=f"fifo_out_{c}", depth=1)
            self.x.lane(c).bind(fifo_in.prod())
            self.y.lane(c).bind(fifo_out.cons())
        return []

    def compatible(self) -> None:
        channels = self.num_channels
        for tap in (self.src, self.dst):
            if tap.sizes[-1] % channels:
                raise Incompatible(
                    f"the innermost axis of {tap} ({tap.sizes[-1]}) must be "
                    f"divisible by num_channels ({channels})"
                )
        per_channel = prod(self.src.sizes) // channels
        if per_channel % self.tile_size:
            raise Incompatible(
                f"tile_size {self.tile_size} must divide the per-channel "
                f"transfer {per_channel} (= {prod(self.src.sizes)} / {channels} "
                f"channels)"
            )
        for row in self._row_shares():
            if row % self.tile_size:
                raise Incompatible(
                    f"tile_size {self.tile_size} must divide the {row} elements "
                    f"per channel one row of the bounded axis moves: a call "
                    f"moves any number of rows"
                )

    def _row_shares(self) -> list[int]:
        """Per bounded pattern, the elements per channel one row of its
        bounded axis moves.
        """
        return [
            prod(tap.sizes) // tap.sizes[bound] // self.num_channels
            for tap, bound in ((self.src, self.src_bound), (self.dst, self.dst_bound))
            if bound is not None
        ]

    def _shares(self, tap: TensorAccessPattern) -> list[TensorAccessPattern]:
        """``tap`` with its innermost axis split among the channels, in order."""
        share = tap.sizes[-1] // self.num_channels
        return [
            TensorAccessPattern(
                tap.tensor_dims,
                tap.offset + c * share * tap.strides[-1],
                [*tap.sizes[:-1], share],
                tap.strides,
            )
            for c in range(self.num_channels)
        ]

    def _taps(
        self, tap: TensorAccessPattern, bound: int | None, dtype
    ) -> list[tuple[TensorAccessPattern, int | None]]:
        """Per channel, its share of ``tap`` and the dimension a bound patches.

        An unbounded share is issued as it is: the compiler splits one no
        descriptor holds. A bounded one must be one descriptor, since its
        size is patched in place, so it is placed exactly, its bounded axis
        on D2 (dimension 1) where the pattern allows: D2 has no wrap, since a
        shim descriptor's length ends it. A bound on the innermost axis, the
        one the channels split, takes one channel.
        """
        if bound is None:
            return [(share, None) for share in self._shares(tap)]
        rank = len(tap.sizes)
        dim = 4 - rank + bound
        if dim == 3 and self.num_channels > 1:
            raise Incompatible(
                f"{tap} is bounded on the axis the {self.num_channels} channels "
                f"split; bound another axis or copy on one channel"
            )
        # At most one axis outside the bound (the iteration slot) and one or
        # two inside it (D1, D0) put the bound on D2.
        on_d2 = bound <= 1 and 1 <= rank - bound - 1 <= 2
        shim = aie_utils.ensure_current_device(required=True).bd_limits(0, 0)
        out = []
        for share in self._shares(tap):
            dims = list(share.transformation_dims)
            if on_d2:
                lead, inner = dims[:bound], dims[bound + 1 :]
                dims = (
                    (lead or [(1, 0)])
                    + [dims[bound]]
                    + [(1, 0)] * (2 - len(inner))
                    + inner
                )
            placed = TensorAccessPattern(
                share.tensor_dims,
                share.offset,
                [n for n, _ in dims],
                [s for _, s in dims],
            )
            if not shim.fits(placed, dtype):
                raise Incompatible(
                    f"{tap} does not fit one descriptor per channel, which a "
                    f"bounded axis needs (its size is patched in place)"
                )
            out.append((placed, 1 if on_d2 else dim))
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

        def at(tap, bound, valid):
            if valid is None:
                return tap
            sizes = list(tap.sizes)
            sizes[bound] = int(valid)
            return TensorAccessPattern(tap.tensor_dims, tap.offset, sizes, tap.strides)

        src = at(self.src, self.src_bound, src_valid)
        dst = at(self.dst, self.dst_bound, dst_valid)
        # Channel by channel, as the design splits the patterns.
        gather = [c.access_indices() + int(in_offset) for c in self._shares(src)]
        scatter = [c.access_indices() + int(out_offset) for c in self._shares(dst)]
        out = (
            np.zeros(self.output_buffer_size, dtype=x.dtype)
            if y is None
            else y.reshape(-1)
        )
        flat = x.reshape(-1)
        for src_c, dst_c in zip(gather, scatter):
            if len(src_c) != len(dst_c):
                raise ValueError(
                    f"pattern element counts differ ({len(src_c)} vs {len(dst_c)}); "
                    "src and dst must move the same number of elements"
                )
            out[dst_c] = flat[src_c]
        return out if y is None else y

    def sequence(self, rt):
        ins = self._taps(self.src, self.src_bound, self.x.dtype)
        outs = self._taps(self.dst, self.dst_bound, self.y.dtype)
        in_off = self.in_offset if self.uses_value("in_offset") else None
        out_off = self.out_offset if self.uses_value("out_offset") else None

        with rt.group() as tg:
            for c in range(self.num_channels):
                tap, dim = ins[c]
                rt.fill(
                    self.x.lane(c),
                    tap,
                    group=tg,
                    offset_by=in_off,
                    size_by=None if dim is None else {dim: self.value("src_valid")},
                )
                tap, dim = outs[c]
                rt.drain(
                    self.y.lane(c),
                    tap,
                    group=tg,
                    wait=True,
                    offset_by=out_off,
                    size_by=None if dim is None else {dim: self.value("dst_valid")},
                )
