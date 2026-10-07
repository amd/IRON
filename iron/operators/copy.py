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
import functools
from collections.abc import Mapping
from dataclasses import field
from math import gcd, isqrt, prod
from typing import Any, ClassVar

import numpy as np
from aie.dialects import aiex
from aie.dialects.aie import DMAChannelDir, WireBundle
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    ExternalFunction,
    Flow,
    ObjectFifo,
    PacketFlow,
    TaskGroup,
    Worker,
    WorkerRuntimeBarrier,
)
from aie.iron.device import Tile
from aie.iron.runtime.dmatask import emit_shim_transfer
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, Operator, Out, Scratchpad, Unresolvable, auto, param
from iron.common.design import BdLimits, ShimChannel
from iron.common.testing import Case, Testing

# kDDRAIEAddrOffset (TxnEncoding.h)
APERTURE = 0x80000000


def _control_header(beats: int, address: int) -> int:
    """A control packet writing ``beats + 1`` words from ``address``, odd parity."""
    header = (beats << 20) | address
    return header | ((1 ^ (bin(header).count("1") & 1)) << 31)


class Gather(Operator):
    """``Copy(table[ids])`` with ``ids`` per call: the rows a call names.

    For ids a graph input the host turns each call's ids into control
    packets (``control_words``); for ids the device made, a
    ``GatherWords`` step writes them into the template (``word_source``).
    The rows go out over ``feeds`` pairs of shims. For feed ``k``, shim
    (2k + 1, 0) streams the packets to shim (2k, 0)'s TileControl: each
    writes a buffer descriptor of (2k, 0), its address the table's on the
    device plus the row's offset, and each batch of ``chain`` descriptors
    is pushed onto (2k, 0)'s MM2S 1 queue. That channel streams the rows to
    (2k + 1, 0)'s S2MM 0, which drains them into ``y``. Each feed streams a
    run of whole pairs of batches, and batch ``j`` runs on set ``j % 2`` of
    its feed's descriptors, so the control words are one layout for every
    feed count and a feed drains one span of ``y``. A set is rewritten only
    after the sequence syncs on the token of the batch that last ran it.
    The descriptors' addresses are physical, so only a full ELF, whose
    table stays put across calls, runs it.
    """

    chain: ClassVar[int] = 8
    # Measured: a fifth pair of shims would gain little over four.
    max_feeds: ClassVar[int] = 4
    control_id: ClassVar[int] = 29
    bd_base: ClassVar[int] = 0x1D000
    # MM2S 1's control register; its task queue is the next word.
    mm2s_1_control: ClassVar[int] = 0x1D218
    # BD words 3 to 6 as the compiler writes a linear shim BD.
    bd_tail: ClassVar[tuple[int, ...]] = (0, 0xC0000000, 0x2000000, 0)
    valid: ClassVar[int] = 1 << 25
    use_next: ClassVar[int] = 1 << 26
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    rows: int = param()
    table_rows: int = param()
    row: int = param()
    dtype: Any = field(default=bfloat16, repr=False)
    words: int = param(
        default=lambda op: 20 * op.chain
        + 3 * (op.rows + len(op.batches))
        + (3 if op.rows % op.chain else 0),
        repr=False,
    )
    feeds: int = auto(array=True)

    table = In(table_rows, row, dtype=dtype)
    control = In(words, dtype=np.uint32)
    y = Out(rows, row, dtype=dtype)

    @property
    def batches(self) -> list[int]:
        """The rows of each batch, ``chain`` at most."""
        return [min(self.chain, self.rows - r) for r in range(0, self.rows, self.chain)]

    @property
    def runs(self) -> list[range]:
        """Per feed, the batches it streams: a run of whole pairs, the last
        feed's ending where the rows do.
        """
        n = len(self.batches)
        pairs = -(-n // 2)
        bounds = [2 * (k * pairs // self.feeds) for k in range(self.feeds + 1)]
        return [range(a, min(b, n)) for a, b in zip(bounds, bounds[1:])]

    def validate(self) -> None:
        if self.rows < 1:
            raise ValueError(f"a gather takes one row at least, not {self.rows}")
        if self.row * np.dtype(self.dtype).itemsize % 4:
            raise ValueError(
                f"a row of {self.row} {np.dtype(self.dtype).name} is not whole "
                f"32-bit words, which a descriptor's length counts"
            )

    def resolve(self, dev):
        """As many feeds as the device's shim columns pair into, up to
        ``max_feeds`` and to one per two batches.
        """
        pairs = -(-len(self.batches) // 2)
        feeds = self.feeds
        if feeds is None:
            feeds = min(self.max_feeds, dev.cols // 2, pairs)
        if not 1 <= feeds <= dev.cols // 2:
            raise Unresolvable(
                f"a gather feeds from 1 to {dev.cols // 2} pairs of shim "
                f"columns on a device of {dev.cols}, not {feeds}"
            )
        return dataclasses.replace(self, feeds=feeds)

    def compatible(self) -> None:
        pairs = -(-len(self.batches) // 2)
        if self.feeds > pairs:
            raise ValueError(
                f"{self.rows} rows are {pairs} pairs of batches of {self.chain}, "
                f"and a feed streams whole pairs, so {self.feeds} feeds leave "
                f"{self.feeds - pairs} idle"
            )

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def array(self, target) -> list:
        routes = []
        for k in range(self.feeds):
            feed, drain = Tile(2 * k, 0), Tile(2 * k + 1, 0)
            routes += [
                PacketFlow(
                    self.control_id - k,
                    drain,
                    feed,
                    dst_port=WireBundle.TileControl,
                    # An explicit False drops the header TileControl reads: the run hangs.
                    keep_pkt_header=True,
                    shim_symbol=f"gather_ctrl{k}",
                ),
                Flow(
                    feed,
                    drain,
                    src_channel=1,
                    dst_channel=0,
                    shim_symbol=f"gather_feed{k}",
                ),
                ShimChannel(f"gather_rows{k}", drain, DMAChannelDir.S2MM, 0),
            ]
        return routes

    def sequence(self, rt) -> None:
        if rt.image != "elf":
            raise ValueError(
                "a gather by a graph input writes physical addresses, which "
                "only a full ELF keeps across calls; package as a full ELF"
            )
        words, y = rt.data(self.control), rt.data(self.y)
        chain, batches, runs = self.chain, self.batches, self.runs
        drained, pending = [], []
        for k, run in enumerate(runs):
            first = run.start * chain * self.row
            last = min(run.stop * chain, self.rows) * self.row
            drained.append(
                emit_shim_transfer(
                    f"gather_rows{k}",
                    y,
                    tap=TensorAccessPattern(
                        (self.rows * self.row,),
                        first,
                        [1, 1, 1, last - first],
                        [0, 0, 0, 1],
                    ),
                    wait=True,
                    managed=False,
                )
            )
            # Every feed's preamble writes the same descriptors, from one copy.
            pending.append(
                [
                    emit_shim_transfer(
                        f"gather_ctrl{k}",
                        words,
                        tap=TensorAccessPattern(
                            (self.words,), 0, [4 * chain, 1, 1, 5], [5, 0, 0, 1]
                        ),
                        packet=(0, self.control_id - k),
                        managed=False,
                    )
                ]
            )
        for i in range(max(len(run) for run in runs)):
            for k, run in enumerate(runs):
                if i >= len(run):
                    continue
                j = run[i]
                if i >= 2:
                    # MM2S 1 finished the feed's batch i - 2: its set and packets are free.
                    aiex.npu_sync(2 * k, 0, DMAChannelDir.MM2S.value, 1)
                    for task in pending[k][:-1]:
                        task.free()
                    pending[k] = pending[k][-1:]
                # A row's packet, the push, and on a short last batch its end.
                packets = batches[j] + 1 + int(batches[j] < chain)
                pending[k].append(
                    emit_shim_transfer(
                        f"gather_ctrl{k}",
                        words,
                        tap=TensorAccessPattern(
                            (self.words,),
                            20 * chain + 3 * (chain + 1) * j,
                            [packets, 1, 1, 3],
                            [3, 0, 0, 1],
                        ),
                        packet=(0, self.control_id - k),
                        managed=False,
                    )
                )
        for k, run in enumerate(runs):
            for _ in run[-2:]:
                aiex.npu_sync(2 * k, 0, DMAChannelDir.MM2S.value, 1)
            for task in pending[k]:
                task.free()
        for task in drained:
            task.await_()

    def word_source(self) -> "GatherWords":
        """The step writing this gather's row addresses into its template on
        a core, for ids the device made.
        """
        return GatherWords(
            rows=self.rows,
            table_rows=self.table_rows,
            row_bytes=self.row * np.dtype(self.dtype).itemsize,
            words=self.words,
        )

    @functools.cached_property
    def template(self) -> tuple[np.ndarray, np.ndarray]:
        """The control words with every row's address zero, and where each
        row's address-low word is.
        """
        chain, words, slots = self.chain, [], []
        for b in range(2 * chain):
            at = self.bd_base + 0x20 * b
            last = b % chain == chain - 1
            word7 = self.valid | (0 if last else self.use_next | ((b + 1) << 27))
            row_words = self.row * np.dtype(self.dtype).itemsize // 4
            words += [_control_header(3, at), row_words, 0, 0, self.bd_tail[0]]
            words += [_control_header(3, at + 16), *self.bd_tail[1:], word7]
        for j, n in enumerate(self.batches):
            sets = (j % 2) * chain
            for k in range(n):
                slots.append(len(words) + 1)
                words += [
                    _control_header(1, self.bd_base + 0x20 * (sets + k) + 4),
                    0,
                    0,
                ]
            if n < chain:
                # The batch's last descriptor ends the chain.
                at = self.bd_base + 0x20 * (sets + n - 1) + 24
                words += [_control_header(1, at), self.bd_tail[3], self.valid]
            words += [
                _control_header(1, self.mm2s_1_control),
                0xF00,
                (1 << 31) | sets,
            ]
        assert len(words) == self.words
        return np.array(words, dtype=np.uint32), np.array(slots)

    def control_words(self, ids, address: int) -> np.ndarray:
        """The control words gathering ``ids`` from a table at ``address``.

        Args:
            ids: The rows, numpy's indices: negative ones count from the end.
            address: The table's XRT buffer address.

        Returns:
            The words ``ids`` takes, ``words`` of them.

        Raises:
            IndexError: An id is past the table, either way.
        """
        ids = np.asarray(ids).astype(np.int64)
        if ids.shape != (self.rows,):
            raise ValueError(
                f"a gather of {self.rows} rows takes {self.rows} ids, got {ids.shape}"
            )
        n = self.table_rows
        if ((ids < -n) | (ids >= n)).any():
            raise IndexError(f"gathering {ids[(ids < -n) | (ids >= n)]} from {n} rows")
        template, slots = self.template
        stride = self.row * np.dtype(self.dtype).itemsize
        rows = (address + APERTURE + (ids % n) * stride).astype(np.uint64)
        words = template.copy()
        words[slots] = (rows & np.uint64(0xFFFFFFFC)).astype(np.uint32)
        words[slots + 1] = ((rows >> np.uint64(32)) & np.uint64(0xFFFF)).astype(
            np.uint32
        )
        return words

    def addressed_inputs(
        self, addresses: Mapping[str, int], rng: np.random.Generator
    ) -> dict[str, np.ndarray]:
        ids = rng.integers(0, self.table_rows, self.rows)
        return {"control": self.control_words(ids, addresses["table"])}


_ROW_ADDRESSES = """
#include <stdint.h>

extern "C" void {symbol}(int32_t *ids, uint32_t *out, int32_t lo, int32_t hi) {{
    uint64_t base = ((uint64_t)(uint32_t)hi << {low_bits}) + (uint32_t)lo + {aperture}ull;
    for (int r = 0; r < {rows}; r++) {{
        int32_t id = ids[r] < -{table_rows} ? -{table_rows} : ids[r];
        id = id > {table_rows} - 1 ? {table_rows} - 1 : id;
        if (id < 0)
            id += {table_rows};
        uint64_t address = base + (uint64_t)id * {row_bytes}u;
        out[2 * r] = (uint32_t)address & 0xFFFFFFFCu;
        out[2 * r + 1] = (uint32_t)(address >> 32) & 0xFFFFu;
    }}
}}
"""


class GatherWords(Operator):
    """A ``Gather``'s control words for ids the device made, in a graph.

    A core turns each id into its row's address words, which drain into
    their slots of ``control``, a buffer holding the gather's template;
    the gather that follows streams it. The table's address reaches the
    core as ``base_lo`` and ``base_hi``, per-call values the graph fills
    in, split at ``low_bits`` since a core reads 30 bits of a value. An id
    past the table is clipped to its first or last row,
    ``table[np.clip(ids, -n, n - 1)]``, so every id reads a row of it.
    """

    low_bits: ClassVar[int] = 29

    rows: int = param(array=True)
    table_rows: int = param(array=True)
    row_bytes: int = param(array=True)
    words: int = param()
    pairs: int = param(default=lambda op: 2 * op.rows, array=True, repr=False)

    ids = In(rows, dtype=np.int32, tile=(rows,), depth=1)
    control = Out(words, dtype=np.uint32, tile=(pairs,), depth=1)
    base_lo = Scratchpad(np.int32)
    base_hi = Scratchpad(np.int32)

    def ops(self) -> int:
        return 0

    def address_words(self, address: int) -> dict[str, int]:
        """``base_lo`` and ``base_hi`` for a table at ``address``."""
        return dict(
            base_lo=address & ((1 << self.low_bits) - 1),
            base_hi=address >> self.low_bits,
        )

    def array(self, target) -> list:
        symbol = f"gather_words_{self.rows}_{self.table_rows}_{self.row_bytes}"
        kernel = ExternalFunction(
            symbol,
            source_string=_ROW_ADDRESSES.format(
                symbol=symbol,
                rows=self.rows,
                table_rows=self.table_rows,
                row_bytes=self.row_bytes,
                low_bits=self.low_bits,
                aperture=APERTURE,
            ),
            arg_types=[self.ids.tile, self.control.tile, np.int32, np.int32],
        )
        ids = ObjectFifo(self.ids.tile, name="gather_ids", depth=1)
        addresses = ObjectFifo(self.control.tile, name="gather_addresses", depth=1)
        self.ids.lane(0).bind(ids.prod())
        self.control.lane(0).bind(addresses.cons())
        barrier = WorkerRuntimeBarrier()

        def core(ids, addresses, kernel, lo, hi, barrier):
            barrier.wait_for_value(1)
            i, a = ids.acquire(1), addresses.acquire(1)
            kernel(i, a, lo.read(), hi.read())
            ids.release(1)
            addresses.release(1)

        worker = Worker(
            core,
            [
                ids.cons(),
                addresses.prod(),
                kernel,
                self.base_lo.param,
                self.base_hi.param,
                barrier,
            ],
        )
        return [worker, barrier]

    def sequence(self, rt) -> None:
        tg = TaskGroup()
        rt.fill(self.ids.lane(0), self.ids, group=tg)
        for tap in self.taps():
            rt.drain(self.control.lane(0), (self.control, tap), group=tg, wait=True)
        tg.finish()

    def taps(self) -> list[TensorAccessPattern]:
        """Where the rows' address words go in ``control``, in row order.

        A row's follow its packet's header, three words to a packet and a
        push after every batch of ``chain``.
        """
        chain, at = Gather.chain, 20 * Gather.chain + 1
        full, short = divmod(self.rows, chain)
        taps = []
        if full:
            taps.append(
                TensorAccessPattern(
                    (self.words,),
                    at,
                    [1, full, chain, 2],
                    [0, 3 * (chain + 1), 3, 1],
                )
            )
        if short:
            taps.append(
                TensorAccessPattern(
                    (self.words,),
                    at + 3 * (chain + 1) * full,
                    [1, 1, short, 2],
                    [0, 0, 3, 1],
                )
            )
        return taps


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

    With ``ids`` a 1-D integer handle (a graph input, a state, an output
    of a step), ``Copy(table[ids])`` is a ``Gather``, the rows each call
    names.

    A side that is a tuple of patterns walks them in turn: ``Copy(table[ids])``
    with ``ids`` an array gathers the rows it names, fixed when the graph is
    traced. Each is
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
    per_call_gather: ClassVar[type[Operator] | None] = Gather

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
    tile_size: int = auto()  # None: the per-channel share, cut to object_bytes
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
        pieces = [prod(p.sizes) // self.num_channels for w in self.walks() for p in w]
        whole = gcd(*pieces, *self._row_shares())
        cap = self.object_bytes // np.dtype(self.dtype).itemsize
        tile_size = self.tile_size or max(
            d
            for i in range(1, isqrt(whole) + 1)
            if whole % i == 0
            for d in (i, whole // i)
            if d <= cap
        )
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
