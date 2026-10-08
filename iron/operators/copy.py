# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy between two views: ``Copy(k, keys[i][:, pos])``.

Each side is an access pattern over its buffer (offset, sizes, strides), the
form a DMA takes, or patterns walked in turn (a gather, ``table[ids]``); the
shim channels split the innermost run every pattern shares, and the compiler
splits a share no one descriptor holds. A per-call value indexing a view
reaches the copy as ``in_offset``/``out_offset``, an element offset.
"""

import dataclasses
from dataclasses import field
from math import gcd, isqrt, prod
from typing import Any, ClassVar

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import ObjectFifo, TaskGroup
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import CopyRun, Divisors, In, Operator, Out, Scratchpad, auto, param
from iron.common.design import BdLimits
from iron.common.testing import Case, Testing


def _into_slot(slot, seq=128, num_channels=1) -> dict[str, Any]:
    """Kwargs scattering an (8, 64) block into slot ``slot`` of an (8, seq, 64)
    buffer: each of its rows lands ``seq * 64`` elements after the last.
    """
    return dict(
        src=TensorAccessPattern.full((8, 64)),
        dst=TensorAccessPattern.full((8, seq, 64))[:, slot],
        input_buffer_size=8 * 64,
        output_buffer_size=8 * seq * 64,
        num_channels=num_channels,
    )


def _by_head(num_channels: int) -> dict[str, Any]:
    """Kwargs reading a (16, 4, 64) buffer head by head into a flat one."""
    return dict(
        src=TensorAccessPattern.full((16, 4, 64)).permute((1, 0, 2)),
        dst=TensorAccessPattern.full((16 * 4 * 64,)),
        input_buffer_size=16 * 4 * 64,
        num_channels=num_channels,
    )


class Copy(Operator):
    """AIE-accelerated copy between two views of two buffers.

    Gathers by ``src`` and scatters by ``dst``, split across
    ``num_channels`` memtile pass-throughs (no cores) on the innermost
    run every pattern holds a whole number of (the greatest common divisor
    of their innermost sizes), so each channel reads what it writes. In a
    graph the patterns come from the operands: ``Copy(k,
    keys[i][:, pos])``, ``Copy(x.transpose(1, 0, 2), y[:, :n])``; a per-call
    index on a view binds ``in_offset`` or ``out_offset``, and a per-call
    bound ``src_bound``/``dst_bound`` with its size. Standalone,
    ``src``/``dst`` are given, or default to the whole of each buffer.

    A side that is a tuple of patterns walks them in turn: ``Copy(table[ids])``
    gathers the rows ``ids`` names, fixed when the graph is traced. Each is
    its own transfer, with runs of pieces whose offsets step evenly made one
    (consecutive rows, a repeated row, a grid's rows), more than a task group
    holds descriptors for; so they are unmanaged, the compiler metering each
    channel's queue, and the two sides go out in stream order, so that no
    transfer waits on one not yet issued.

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
            # Left to resolve, a share past a memtile is cut to fit one.
            Case(dict(input_buffer_size=1 << 19), id="past_one_memtile"),
            Case(_into_slot(0), id="slot0"),
            Case(_into_slot(5), id="slot5"),
            Case(_into_slot(127), id="slot_last"),
            # The flat cases split a stride-1 run across the channels; these
            # split the rows of a strided scatter.
            Case(_into_slot(5, num_channels=2), id="slot5_two_channels"),
            Case(_into_slot(5, num_channels=4), id="slot5_four_channels"),
            # The sides' innermost axes differ: (16, 4, 64) read by head into
            # a flat buffer, every channel's share of one in step with the other's.
            Case(_by_head(num_channels=2), id="by_head_two_channels"),
            Case(_by_head(num_channels=4), id="by_head_four_channels"),
            Case(_into_slot(1000, seq=2048), id="slot1000_of_2048", extensive=True),
            # Benched: 4 Mi elements, well past the dispatch cost.
            Case(
                dict(input_buffer_size=1 << 22, num_channels=4, tile_size=4096),
                id="bench_flat_4mi",
                bench=True,
            ),
        ],
        tolerance=Tolerance.exact(),
    )

    input_buffer_size: int = param(repr=False)
    src: TensorAccessPattern | tuple[TensorAccessPattern, ...] = param(
        default=lambda op: TensorAccessPattern.full((op.input_buffer_size,))
    )
    output_buffer_size: int = param(
        default=lambda op: sum(
            prod(p.sizes) for p in (op.src if isinstance(op.src, tuple) else (op.src,))
        ),
        repr=False,
    )
    # The output is rows as wide as the source's innermost axis, so the
    # channels split both sides alike.
    dst: TensorAccessPattern | tuple[TensorAccessPattern, ...] = param(
        default=lambda op: TensorAccessPattern.full(
            (op.output_buffer_size // op.src.sizes[-1], op.src.sizes[-1])
            if isinstance(op.src, TensorAccessPattern)
            else (op.output_buffer_size // op.src[0].sizes[-1], op.src[0].sizes[-1])
        )
    )
    # The axis of each pattern a graph bounds per call (``x[:n]`` on a view):
    # its size is the full extent in the pattern and patched to the call's.
    src_bound: int | None = param(default=None)
    dst_bound: int | None = param(default=None)
    # None: the per-channel share, cut to object_bytes.
    tile_size: int = auto(
        domain=Divisors(
            of=lambda op: op.channel_share,
            cap=lambda op: op.object_bytes // np.dtype(op.dtype).itemsize,
            span=3,
        )
    )
    # A memtile holds 512 KiB; the cap leaves room for every channel placed on one.
    object_bytes: ClassVar[int] = 64 * 1024
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

    def walks(self) -> list[tuple[TensorAccessPattern, ...]]:
        """The patterns each side walks in turn, ``[src, dst]``."""
        return [t if isinstance(t, tuple) else (t,) for t in (self.src, self.dst)]

    @property
    def aiecc_flags(self) -> tuple[str, ...]:
        """A gather's pieces outnumber the shim's BD ids, so the compiler
        recycles finished tasks' ids; no task waits on a push issued after
        it, since each channel's drains go out before the fills feeding them.
        """
        gathered = any(isinstance(t, tuple) for t in (self.src, self.dst))
        return ("--reclaim-runtime-bds",) if gathered else ()

    def validate(self) -> None:
        src, dst = (sum(prod(p.sizes) for p in w) for w in self.walks())
        if src != dst:
            raise ValueError(
                f"a copy moves the same element count both ways: src has {src} "
                f"elements, dst {dst}"
            )
        for side, tap, bound in (
            ("src", self.src, self.src_bound),
            ("dst", self.dst, self.dst_bound),
        ):
            if isinstance(tap, tuple) and bound is not None:
                raise ValueError(
                    f"{side} walks {len(tap)} patterns in turn; a per-call bound "
                    f"takes one pattern"
                )

    def resolve(self, dev):
        """The transfer size, unless given, is the largest divisor of the
        per-channel share (under a bound, of one bounded row's share; of a
        gather, of every piece's) whose object fits ``object_bytes``.
        """
        whole = self.channel_share
        cap = self.object_bytes // np.dtype(self.dtype).itemsize
        tile_size = self.tile_size or max(
            d
            for i in range(1, isqrt(whole) + 1)
            if whole % i == 0
            for d in (i, whole // i)
            if d <= cap
        )
        return dataclasses.replace(self, tile_size=tile_size)

    @property
    def channel_share(self) -> int:
        """What each channel's transfers split into: of every pattern's
        share, and of one bounded row's.
        """
        pieces = [prod(p.sizes) // self.num_channels for w in self.walks() for p in w]
        return gcd(*pieces, *self._row_shares())

    def uses_value(self, name: str) -> bool:
        # An offset or a size is patched only when a graph binds a handle to it.
        return name in self.bound_values

    def copies_to(self) -> CopyRun | None:
        """The run ``dst`` writes, where ``src`` reads the whole input in
        order and ``dst`` is one contiguous run, neither bounded.
        """
        src, dst = self.src, self.dst
        # A bounded copy stays: a producer drains whole tiles past the bound.
        if (
            not isinstance(src, TensorAccessPattern)
            or not isinstance(dst, TensorAccessPattern)
            or "in_offset" in self.bound_values
            or self.src_bound is not None
            or self.dst_bound is not None
        ):
            return None
        whole, run = src.coalesce(), dst.coalesce()
        if (
            whole.rank != 1
            or whole.offset != 0
            or whole.sizes[0] != self.input_buffer_size
            or 1 not in (whole.sizes[0], whole.strides[0])
            or run.rank != 1
            or 1 not in (run.sizes[0], run.strides[0])
            or not isinstance(run.offset, (int, np.integer))
        ):
            return None
        return CopyRun(
            self.output_buffer_size,
            int(run.offset),
            "out_offset" if "out_offset" in self.bound_values else None,
        )

    def placed(self, copy: Operator, operand: str) -> None:
        """Never: a copy's sequence moves its transfers itself."""
        return None

    def array(self, target) -> list:

        for c in range(self.num_channels):
            fifo_in = ObjectFifo(self.x.tile, name=f"fifo_in_{c}", depth=1)
            fifo_out = fifo_in.cons().forward(name=f"fifo_out_{c}", depth=1)
            self.x.lane(c).bind(fifo_in.prod())
            self.y.lane(c).bind(fifo_out.cons())
        return []

    def compatible(self) -> None:
        channels = self.num_channels
        step = gcd(*(tap.sizes[-1] for walk in self.walks() for tap in walk))
        if step % channels:
            raise ValueError(
                f"the innermost axes of {self.src} and {self.dst} have a common "
                f"run of {step} elements, which num_channels ({channels}) must divide"
            )
        for walk in self.walks():
            for tap in walk:
                per_channel = prod(tap.sizes) // channels
                if per_channel % self.tile_size:
                    raise ValueError(
                        f"tile_size {self.tile_size} must divide the per-channel "
                        f"transfer {per_channel} (= {prod(tap.sizes)} / {channels} "
                        f"channels)"
                    )
        for row in self._row_shares():
            if row % self.tile_size:
                raise ValueError(
                    f"tile_size {self.tile_size} must divide the {row} elements "
                    f"per channel one row of the bounded axis moves: a call "
                    f"moves any number of rows"
                )

    def _row_shares(self) -> list[int]:
        """Per bounded pattern, the elements per channel one row of its
        bounded axis moves.
        """
        return [
            int(prod(tap.sizes) // tap.sizes[bound]) // self.num_channels
            for tap, bound in ((self.src, self.src_bound), (self.dst, self.dst_bound))
            if bound is not None
        ]

    def _shares(self, tap: TensorAccessPattern) -> list[TensorAccessPattern]:
        """``tap``'s share per channel, in order: every run of the elements
        all patterns' innermost axes, both sides', hold a whole number of,
        split among the channels, so the k-th element a channel reads is the
        k-th it writes.
        """
        step = gcd(*(p.sizes[-1] for walk in self.walks() for p in walk))
        if tap.sizes[-1] != step:
            tap = tap.split(tap.rank - 1, step)
        share = step // self.num_channels
        return [tap[..., c * share : (c + 1) * share] for c in range(self.num_channels)]

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
        shares = self._shares(tap)
        if bound is None:
            return [(share, None) for share in shares]
        if bound == tap.rank - 1 and self.num_channels > 1:
            raise ValueError(
                f"{tap} is bounded on the axis the {self.num_channels} channels "
                f"split; bound another axis or copy on one channel"
            )
        rank = shares[0].rank
        dim = 4 - rank + bound
        # At most one axis outside the bound (the iteration slot) and one or
        # two inside it (D1, D0) put the bound on D2.
        on_d2 = bound <= 1 and 1 <= rank - bound - 1 <= 2
        shim = BdLimits.of(self.dev, 0, 0)
        out = []
        for share in shares:
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
                raise ValueError(
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
            return tap[(*[slice(None)] * bound, slice(int(valid)))]

        src = at(self.src, self.src_bound, src_valid)
        dst = at(self.dst, self.dst_bound, dst_valid)
        gather, scatter = (
            np.concatenate(
                [
                    p.gather(np.arange(prod(p.tensor_dims)))
                    for p in (tap if isinstance(tap, tuple) else (tap,))
                ]
            )
            + int(offset)
            for tap, offset in ((src, in_offset), (dst, out_offset))
        )
        if len(gather) != len(scatter):
            raise ValueError(
                f"pattern element counts differ ({len(gather)} vs {len(scatter)}); "
                "src and dst must move the same number of elements"
            )
        out = (
            np.zeros(self.output_buffer_size, dtype=x.dtype)
            if y is None
            else y.reshape(-1)
        )
        out[scatter] = x.reshape(-1)[gather]
        return out if y is None else y

    @staticmethod
    def _stacked(
        pieces: list[TensorAccessPattern], shim: BdLimits, dtype
    ) -> list[TensorAccessPattern]:
        """``pieces`` with each run of alike ones whose offsets step evenly
        made one pattern with an outer axis, as far as one descriptor holds
        it: twice, so rows make runs and runs make a grid.
        """
        for _ in range(2):
            runs: list[tuple[TensorAccessPattern, int, int]] = []  # first, count, step
            for p in pieces:
                if runs:
                    first, n, step = runs[-1]
                    step = p.offset - first.offset if n == 1 else step
                    if (
                        (p.sizes, p.strides) == (first.sizes, first.strides)
                        and step >= 0
                        and p.offset == first.offset + n * step
                        and shim.fits(
                            TensorAccessPattern(
                                first.tensor_dims,
                                first.offset,
                                [n + 1, *first.sizes],
                                [step, *first.strides],
                            ),
                            dtype,
                        )
                    ):
                        runs[-1] = (first, n + 1, step)
                        continue
                runs.append((p, 1, 0))
            pieces = [
                (
                    first
                    if n == 1
                    else TensorAccessPattern(
                        first.tensor_dims,
                        first.offset,
                        [n, *first.sizes],
                        [step, *first.strides],
                    )
                )
                for first, n, step in runs
            ]
        return pieces

    def sequence(self, rt):
        in_off = self.in_offset if self.uses_value("in_offset") else None
        out_off = self.out_offset if self.uses_value("out_offset") else None
        if isinstance(self.src, tuple) or isinstance(self.dst, tuple):
            shim = BdLimits.of(self.dev, 0, 0)
            # (stream position, channel, is a fill, tap): a drain goes out
            # before the fills that feed it.
            issued = []
            for side, walk in enumerate(self.walks()):
                dtype = (self.x, self.y)[side].dtype
                for c in range(self.num_channels):
                    at = 0
                    shares = [self._shares(p)[c] for p in walk]
                    for tap in self._stacked(shares, shim, dtype):
                        issued.append((at, c, side == 0, tap))
                        at += prod(tap.sizes)
            issued.sort(key=lambda t: t[:3])
            # A channel's drains finish in order, so its last one is the copy's.
            last = {c: i for i, (_, c, fill, _) in enumerate(issued) if not fill}
            tokens = []
            for i, (_, c, fill, tap) in enumerate(issued):
                if fill:
                    rt.fill(self.x.lane(c), tap, offset_by=in_off, managed=False)
                    continue
                task = rt.drain(
                    self.y.lane(c),
                    tap,
                    offset_by=out_off,
                    wait=last[c] == i,
                    managed=False,
                )
                if last[c] == i:
                    tokens.append(task)
            for task in tokens:
                task.await_()
            return

        ins = self._taps(self.src, self.src_bound, self.x.dtype)
        outs = self._taps(self.dst, self.dst_bound, self.y.dtype)
        tg = TaskGroup()
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
        tg.finish()
