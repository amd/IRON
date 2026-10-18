# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy between two views: ``Copy(k, keys[i][:, pos])``."""

import dataclasses
import functools
from collections.abc import Mapping
from math import gcd, isqrt, prod
from typing import Any, ClassVar

import numpy as np
from aie.dialects.aie import DMAChannelDir, WireBundle
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import (
    CompileTime,
    DmaEndpoint,
    ExternalFunction,
    Flow,
    FlowEndpoint,
    In,
    ObjectFifo,
    Out,
    PacketFlow,
    TaskGroup,
    Worker,
)
from aie.iron.device import Tile
from aie.iron.kernels import datamovement
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import (
    Auto,
    Built,
    Divisors,
    Extent,
    Operand,
    Operator,
    Rtp,
    Unresolvable,
    Value,
    field,
)
from iron.common.declare.operand import slots
from iron.common.testing import Case, Testing

# kDDRAIEAddrOffset (TxnEncoding.h)
APERTURE = 0x80000000

LENGTHS = """
#include <stdint.h>

extern "C" void gather_lengths(uint32_t *lengths, int32_t valid) {
    for (int r = 0; r < ROWS; r++)
        lengths[r] = r < valid ? ROW_WORDS : PAD_WORDS;
}
"""


def _control_header(beats: int, address: int) -> int:
    """A control packet writing ``beats + 1`` words from ``address``, odd parity."""
    header = (beats << 20) | address
    return header | ((1 ^ (bin(header).count("1") & 1)) << 31)


@dataclasses.dataclass(frozen=True, kw_only=True)
class _GatherBuilt(Built):
    """Gather's build, with the control routes ``sequence()`` fills and the
    feed endpoints it waits on."""

    controls: list[PacketFlow]
    pushes: list[FlowEndpoint]


class Gather(Operator):
    """``Copy(table[ids])`` with ``ids`` per call: the rows a call names.

    Over each of ``feeds`` pairs of shims, shim (2k + 1, 0) streams control
    packets to shim (2k, 0)'s TileControl, each writing a buffer descriptor
    whose address is a row's; batches of ``chain`` alternate between two
    descriptor sets, and (2k, 0)'s MM2S 1 streams the rows back to
    (2k + 1, 0)'s S2MM 0. Under a bound each row past it moves
    ``pad_bytes``: a descriptor moves one 16-byte unit at least.
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
    pad_bytes: ClassVar[int] = 16

    rows: CompileTime[int] = field()
    table_rows: CompileTime[int] = field()
    row: CompileTime[int] = field()
    dtype: CompileTime[Any] = field(bfloat16, repr=False)
    words: CompileTime[int] = field(
        derive=lambda op: 20 * op.chain
        + 6 * op.rows
        + 3 * len(op.batches)
        + (3 if op.rows % op.chain else 0),
        repr=False,
    )
    feeds: CompileTime[int] = Auto()

    table = In(table_rows, row, dtype=dtype)
    control = In(words, dtype=np.uint32)
    y = Out(rows, row, dtype=dtype, obj_shape=(row,), per=(feeds,))
    valid_rows = Extent(rows)
    # Per feed, the 16-byte units it drains under a bound.
    drained0 = Value(derive=lambda op: op.drained(0))
    drained1 = Value(derive=lambda op: op.drained(1))
    drained2 = Value(derive=lambda op: op.drained(2))
    drained3 = Value(derive=lambda op: op.drained(3))

    @property
    def batches(self) -> list[int]:
        """The rows of each batch, ``chain`` at most."""
        return [min(self.chain, self.rows - r) for r in range(0, self.rows, self.chain)]

    @property
    def runs(self) -> list[range]:
        """Per feed, the batches it streams: a run of whole pairs."""
        n = len(self.batches)
        pairs = -(-n // 2)
        bounds = [2 * (k * pairs // self.feeds) for k in range(self.feeds + 1)]
        return [range(a, min(b, n)) for a, b in zip(bounds, bounds[1:])]

    def drained(self, feed: int) -> int:
        """The 16-byte units feed ``feed`` drains with ``valid_rows`` rows valid."""
        valid = self.valid_rows
        if feed >= self.feeds:
            return 0
        run = self.runs[feed]
        first = run.start * self.chain
        count = min(run.stop * self.chain, self.rows) - first
        kept = min(max(valid - first, 0), count)
        row_bytes = self.row * np.dtype(self.dtype).itemsize
        return (kept * row_bytes + (count - kept) * self.pad_bytes) // 16

    def validate(self) -> None:
        if self.rows < 1:
            raise ValueError(f"Gather: rows ({self.rows}) must be at least 1")
        if self.row * np.dtype(self.dtype).itemsize % 4:
            raise ValueError(
                f"Gather: a row of {self.row} {np.dtype(self.dtype).name} is not whole "
                f"32-bit words, which a descriptor's length counts"
            )

    def resolve(self, dev):
        pairs = -(-len(self.batches) // 2)
        feeds = self.feeds
        if feeds is None:
            feeds = min(self.max_feeds, dev.cols // 2, pairs)
        if not 1 <= feeds <= dev.cols // 2:
            raise Unresolvable(
                f"Gather: a gather feeds from 1 to {dev.cols // 2} pairs of shim "
                f"columns on a device of {dev.cols}, not {feeds}"
            )
        return dataclasses.replace(self, feeds=feeds)

    def compatible(self) -> None:
        if (
            "valid_rows" in self.bound_extents
            and self.row * np.dtype(self.dtype).itemsize % 16
        ):
            raise ValueError(
                f"Gather: a row of {self.row} {np.dtype(self.dtype).name} is not whole "
                f"16-byte units, which a bounded drain's length counts"
            )
        pairs = -(-len(self.batches) // 2)
        if self.feeds > pairs:
            raise ValueError(
                f"Gather: {self.rows} rows are {pairs} pairs of batches of {self.chain}, "
                f"and a feed streams whole pairs, so {self.feeds} feeds leave "
                f"{self.feeds - pairs} idle"
            )

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def extent_unit(self, buffer: str) -> int:
        return 0  # a bound shortens y's drains by the drained words, not by tiles

    class Array(Operator.Array):
        def build(self) -> Built:
            shims = [(Tile(2 * k, 0), Tile(2 * k + 1, 0)) for k in range(self.feeds)]
            drains = [DmaEndpoint(drain, DMAChannelDir.S2MM, 0) for _, drain in shims]
            self.y.pin(drains)
            # Per feed, the control packets from the drain shim into the feed
            # shim's TileControl.
            controls = [
                PacketFlow(
                    Gather.control_id - k,
                    drain,
                    feed,
                    dst_port=WireBundle.TileControl,
                    # An explicit False drops the header TileControl reads: the run hangs.
                    keep_pkt_header=True,
                )
                for k, (feed, drain) in enumerate(shims)
            ]
            feeds = [
                Flow(feed, drain, src_channel=1, dst_channel=0) for feed, drain in shims
            ]
            return _GatherBuilt(
                [*controls, *feeds, *drains],
                controls=controls,
                # The feed shim's MM2S 1, which runs the descriptors the packets push.
                pushes=[flow.endpoint(feed) for flow, (feed, _) in zip(feeds, shims)],
            )

    def sequence(self, rt) -> None:
        words = rt.data(self.control)
        controls, pushes = rt.built.controls, rt.built.pushes
        chain, batches, runs = self.chain, self.batches, self.runs
        bounded = "valid_rows" in self.bound_extents
        unit = 16 // np.dtype(self.dtype).itemsize
        drained, pending = [], []
        for k, run in enumerate(runs):
            first = run.start * chain * self.row
            size = min(run.stop * chain, self.rows) * self.row - first
            drained.append(
                self.y.drain(
                    TensorAccessPattern(
                        (self.rows * self.row,), first, [1, 1, 1, size], [0, 0, 0, 1]
                    ),
                    lane=k,
                    wait=True,
                    managed=False,
                    length_parameter=self.value(f"drained{k}") if bounded else None,
                    length_unit=unit if bounded else None,
                )
            )
            # Every feed's preamble writes the same descriptors, from one copy.
            pending.append(
                [
                    controls[k].fill(
                        words,
                        tap=TensorAccessPattern(
                            (self.words,), 0, [4 * chain, 1, 1, 5], [5, 0, 0, 1]
                        ),
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
                    pushes[k].sync()
                    for task in pending[k][:-1]:
                        task.free()
                    pending[k] = pending[k][-1:]
                # A row's two packets, the push, and on a short last batch its end.
                packets = 2 * batches[j] + 1 + int(batches[j] < chain)
                pending[k].append(
                    controls[k].fill(
                        words,
                        tap=TensorAccessPattern(
                            (self.words,),
                            20 * chain + (6 * chain + 3) * j,
                            [packets, 1, 1, 3],
                            [3, 0, 0, 1],
                        ),
                        managed=False,
                    )
                )
        for k, run in enumerate(runs):
            for _ in run[-2:]:
                pushes[k].sync()
            for task in pending[k]:
                task.free()
        for task in drained:
            task.await_()

    def word_source(self) -> "GatherWords":
        """The step writing row addresses into the template, for ids the device made."""
        return GatherWords(
            rows=self.rows,
            table_rows=self.table_rows,
            row_bytes=self.row * np.dtype(self.dtype).itemsize,
            words=self.words,
            bounded="valid_rows" in self.bound_extents,
        )

    @functools.cached_property
    def template(self) -> tuple[np.ndarray, np.ndarray]:
        """The control words with every row's address zero, and where each
        row's address-low word is (its length one before, its high word two after).
        """
        chain, words, slots = self.chain, [], []
        row_words = self.row * np.dtype(self.dtype).itemsize // 4
        for b in range(2 * chain):
            at = self.bd_base + 0x20 * b
            last = b % chain == chain - 1
            word7 = self.valid | (0 if last else self.use_next | ((b + 1) << 27))
            words += [_control_header(3, at), row_words, 0, 0, self.bd_tail[0]]
            words += [_control_header(3, at + 16), *self.bd_tail[1:], word7]
        for j, n in enumerate(self.batches):
            sets = (j % 2) * chain
            for k in range(n):
                at = self.bd_base + 0x20 * (sets + k)
                slots.append(len(words) + 2)
                words += [_control_header(1, at), row_words, 0]
                words += [_control_header(1, at + 8), 0, self.bd_tail[0]]
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

    def control_words(self, ids, address: int, valid: int | None = None) -> np.ndarray:
        """The control words gathering ``ids`` from a table at ``address``.

        Args:
            ids: The rows, numpy's indices: negative ones count from the end.
            address: The table's XRT buffer address.
            valid: The rows a bounded call moves, the first ``valid`` of
                ``ids``; each other moves ``pad_bytes`` of the table's first
                row. ``None`` moves every row.

        Returns:
            The words ``ids`` takes, ``words`` of them.

        Raises:
            IndexError: An id is past the table, either way, or ``valid`` is
                outside ``[0, rows]``.
        """
        ids = np.asarray(ids).astype(np.int64)
        if ids.shape != (self.rows,):
            raise ValueError(
                f"Gather: a gather of {self.rows} rows takes {self.rows} ids, got {ids.shape}"
            )
        valid = self.rows if valid is None else int(valid)
        if not 0 <= valid <= self.rows:
            raise IndexError(f"Gather: {valid} valid rows of a gather of {self.rows}")
        ids = ids[:valid]
        n = self.table_rows
        if ((ids < -n) | (ids >= n)).any():
            raise IndexError(
                f"Gather: gathering {ids[(ids < -n) | (ids >= n)]} from {n} rows"
            )
        template, slots = self.template
        stride = self.row * np.dtype(self.dtype).itemsize
        rows = np.full(self.rows, address + APERTURE, dtype=np.uint64)
        rows[:valid] += ((ids % n) * stride).astype(np.uint64)
        words = template.copy()
        words[slots[valid:] - 1] = self.pad_bytes // 4
        words[slots] = (rows & np.uint64(0xFFFFFFFC)).astype(np.uint32)
        words[slots + 2] = ((rows >> np.uint64(32)) & np.uint64(0xFFFF)).astype(
            np.uint32
        )
        return words

    def addressed_inputs(
        self, addresses: Mapping[str, int], rng: np.random.Generator
    ) -> dict[str, np.ndarray]:
        ids = rng.integers(0, self.table_rows, self.rows)
        return {"control": self.control_words(ids, addresses["table"])}

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()


class GatherWords(Operator):
    """A ``Gather``'s control words for ids the device made, in a graph.

    A core turns each id, clipped to the table, into its row's address
    words in their slots of ``control``. The table's address is split at
    ``low_bits`` (a core reads 30 bits of a value). ``bounded``, the ids bounded per call to their
    first ``valid_rows``, it also writes each row's length: a whole row's
    for those, ``Gather.pad_bytes`` for the rest, as a bounded ``Gather``
    drains them.
    """

    low_bits: ClassVar[int] = 29

    rows: CompileTime[int] = field()
    table_rows: CompileTime[int] = field(array=True)
    row_bytes: CompileTime[int] = field(array=True)
    words: CompileTime[int] = field()
    pairs: CompileTime[int] = field(
        derive=lambda op: 2 * op.rows, repr=False, array=True
    )
    bounded: CompileTime[bool] = field(False, array=True)
    # The words a call writes: the address pairs, then if bounded the lengths.
    record: CompileTime[int] = field(
        derive=lambda op: op.pairs + (op.rows if op.bounded else 0), repr=False
    )

    ids = In(rows, dtype=np.int32, obj_shape=(rows,), depth=1)
    control = Out(words, dtype=np.uint32, obj_shape=(record,), depth=1)
    base_lo = Value()
    base_hi = Value()
    valid_rows = Extent(rows)
    valid = Value(derive=lambda op: op.valid_rows)

    def ops(self) -> int:
        return 0

    def address_words(self, address: int) -> dict[str, int]:
        """``base_lo`` and ``base_hi`` for a table at ``address``."""
        return dict(
            base_lo=address & ((1 << self.low_bits) - 1),
            base_hi=address >> self.low_bits,
        )

    class Array(Operator.Array):
        def build(self) -> Built:
            kernel = datamovement.row_addresses(
                self.rows,
                self.table_rows,
                self.row_bytes,
                low_bits=GatherWords.low_bits,
                aperture=APERTURE,
            )
            ids = ObjectFifo(self.ids.obj_type, depth=self.ids.depth)
            self.ids.bind(ids.prod())
            lengths = lengths_kernel = None
            if self.bounded:
                lengths_ty = np.ndarray[(self.rows,), np.dtype[np.uint32]]
                pad = Gather.pad_bytes // 4
                lengths_kernel = ExternalFunction(
                    "gather_lengths",
                    source_string=LENGTHS,
                    arg_types=[lengths_ty, np.int32],
                    compile_flags=[
                        f"-DROWS={self.rows}",
                        f"-DROW_WORDS={self.row_bytes // 4}",
                        f"-DPAD_WORDS={pad}",
                    ],
                    symbol_prefix=(
                        f"gather_lengths_{self.rows}_{self.row_bytes // 4}_{pad}"
                    ),
                )
                # A core has two output channels: a memtile joins its two records.
                control = ObjectFifo(self.control.obj_type, depth=self.control.depth)
                addresses, lengths = control.prod().join(
                    [0, self.pairs],
                    obj_types=[
                        np.ndarray[(self.pairs,), np.dtype[np.uint32]],
                        lengths_ty,
                    ],
                    depths=[1, 1],
                )
                self.control.bind(control.cons())
            else:
                addresses = ObjectFifo(self.control.obj_type, depth=self.control.depth)
                self.control.bind(addresses.cons())
            read = [self.base_lo, self.base_hi]
            rtp = Rtp(read + ([self.valid] if self.bounded else []))

            def core(ids, addresses, kernel, rtp, lengths, lengths_kernel):
                words = rtp.read()
                i, a = ids.acquire(1), addresses.acquire(1)
                kernel(i, a, words[self.base_lo], words[self.base_hi])
                ids.release(1)
                addresses.release(1)
                if lengths is not None:
                    lengths_kernel(lengths.acquire(1), words[self.valid])
                    lengths.release(1)

            worker = Worker(
                core,
                [
                    ids.cons(),
                    addresses.prod(),
                    kernel,
                    rtp,
                    None if lengths is None else lengths.prod(),
                    lengths_kernel,
                ],
            )
            return Built([worker], [rtp])

    def sequence(self, rt) -> None:
        tg = TaskGroup()
        self.ids.fill(group=tg)
        for tap in self.taps():
            self.control.drain(tap, group=tg, wait=True)
        tg.finish()

    def taps(self) -> list[TensorAccessPattern]:
        """Where the rows' address words go in ``control``, in row order,
        then if ``bounded`` their lengths, the word before each address.
        """
        chain, at = Gather.chain, 20 * Gather.chain + 2
        full, short = divmod(self.rows, chain)
        taps = []
        for start, width in [(at, 2)] + ([(at - 1, 1)] if self.bounded else []):
            if full:
                taps.append(
                    TensorAccessPattern(
                        (self.words,),
                        start,
                        [1, full, chain, width],
                        [0, 6 * chain + 3, 6, 2],
                    )
                )
            if short:
                taps.append(
                    TensorAccessPattern(
                        (self.words,),
                        start + (6 * chain + 3) * full,
                        [1, 1, short, width],
                        [0, 0, 6, 2],
                    )
                )
        return taps

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()


def _into_slot(slot, seq=128, num_channels=1) -> dict[str, Any]:
    """Kwargs scattering an (8, 64) block into slot ``slot`` of an (8, seq, 64) one."""
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

    Gathers by ``src`` and scatters by ``dst`` through ``num_channels``
    memtile pass-throughs, split on the innermost run every pattern holds
    whole, so each channel reads what it writes. ``tile_size`` divides each
    channel's share: a descriptor shorter than the object never completes
    it, and the drain hangs (ERT_CMD_STATE_TIMEOUT).
    """

    accept_views = (("src", "in_offset"), ("dst", "out_offset"))
    per_call_gather: ClassVar[type[Operator] | None] = Gather

    test = Testing(
        [
            Case(dict(input_buffer_size=1024), id="contiguous"),
            Case(
                dict(input_buffer_size=1024, dtype=np.float32), id="float32", lower=True
            ),
            Case(dict(input_buffer_size=1024, num_channels=2), id="two_channels"),
            Case(dict(input_buffer_size=1024, tile_size=256), id="chunked_transfer"),
            # Left to resolve, a share past a memtile is cut to fit one.
            Case(dict(input_buffer_size=1 << 19), id="past_one_memtile"),
            Case(_into_slot(5), id="slot5", lower=True),
            Case(_into_slot(127), id="slot_last"),
            # The rows of a strided scatter split across the channels.
            Case(_into_slot(5, num_channels=2), id="slot5_two_channels"),
            # The sides' innermost axes differ.
            Case(_by_head(num_channels=2), id="by_head_two_channels", lower=True),
            Case(
                dict(input_buffer_size=1 << 22, num_channels=4, tile_size=4096),
                id="bench_flat_4mi",
                bench=True,
            ),
        ],
    )

    input_buffer_size: CompileTime[int] = field(repr=False)
    src: CompileTime[TensorAccessPattern | tuple[TensorAccessPattern, ...]] = field(
        derive=lambda op: TensorAccessPattern.full((op.input_buffer_size,)), held=False
    )
    # A repeated source's walk is its capacity: the destination's rows are the copy's.
    output_buffer_size: CompileTime[int] = field(
        derive=lambda op: sum(
            prod(p.sizes)
            for p in (
                (op.dst,)
                if op.src_repeat
                else op.src if isinstance(op.src, tuple) else (op.src,)
            )
        ),
        held=False,
        repr=False,
    )
    # Rows as wide as the source's innermost axis: the channels split both alike.
    dst: CompileTime[TensorAccessPattern | tuple[TensorAccessPattern, ...]] = field(
        derive=lambda op: TensorAccessPattern.full(
            (op.output_buffer_size // op.src.sizes[-1], op.src.sizes[-1])
            if isinstance(op.src, TensorAccessPattern)
            else (op.output_buffer_size // op.src[0].sizes[-1], op.src[0].sizes[-1])
        ),
        held=False,
    )
    # The axis of each pattern a graph bounds per call.
    src_bound: CompileTime[int | None] = field(None)
    dst_bound: CompileTime[int | None] = field(None)
    # The source's first axis runs a per-call count of times (Handle.at's repeat).
    src_repeat: CompileTime[bool] = field(False)
    tile_size: CompileTime[int] = Auto(
        domain=Divisors(
            of=lambda op, dev: op.channel_share,
            cap=lambda op, dev: op.object_bytes // np.dtype(op.dtype).itemsize,
            span=3,
        )
    )
    # A memtile holds 512 KiB; the cap leaves room for every channel placed on one.
    object_bytes: ClassVar[int] = 64 * 1024
    # The patterns a repeated source walks in turn: a repeat word each.
    max_walks: ClassVar[int] = 8
    num_channels: CompileTime[int] = Auto(1)
    dtype: CompileTime[Any] = field(bfloat16, repr=False)

    x = In(
        input_buffer_size,
        dtype=dtype,
        obj_shape=(tile_size,),
        per=(num_channels,),
        depth=1,
    )
    y = Out(
        output_buffer_size,
        dtype=dtype,
        obj_shape=(tile_size,),
        per=(num_channels,),
        depth=1,
    )
    # In elements.
    in_offset = Value(derive=lambda op: 0)
    out_offset = Value(derive=lambda op: 0)
    src_valid = Value(derive=lambda op: op.src_bound)
    dst_valid = Value(derive=lambda op: op.dst_bound)
    # Each walk's runs past the first, as a task queue's repeat count counts them.
    src_repeats0 = Value(derive=lambda op: 0)
    src_repeats1 = Value(derive=lambda op: 0)
    src_repeats2 = Value(derive=lambda op: 0)
    src_repeats3 = Value(derive=lambda op: 0)
    src_repeats4 = Value(derive=lambda op: 0)
    src_repeats5 = Value(derive=lambda op: 0)
    src_repeats6 = Value(derive=lambda op: 0)
    src_repeats7 = Value(derive=lambda op: 0)

    def walks(self) -> list[tuple[TensorAccessPattern, ...]]:
        """The patterns each side walks in turn, ``[src, dst]``."""
        return [t if isinstance(t, tuple) else (t,) for t in (self.src, self.dst)]

    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    def validate(self) -> None:
        walks = len(self.walks()[0])
        if self.src_repeat and (
            walks > self.max_walks
            or self.num_channels not in (None, 1)
            or isinstance(self.dst, tuple)
        ):
            raise ValueError(
                f"Copy: a repeated source walks at most {self.max_walks} patterns, a "
                f"descriptor each, on one channel into one pattern; got {walks}"
            )
        src, dst = (sum(prod(p.sizes) for p in w) for w in self.walks())
        if src != dst and not self.src_repeat:
            raise ValueError(
                f"Copy: a copy moves the same element count both ways: src has {src} "
                f"elements, dst {dst}"
            )
        for side, tap, bound in (
            ("src", self.src, self.src_bound),
            ("dst", self.dst, self.dst_bound),
        ):
            if isinstance(tap, tuple) and bound is not None and not self.src_repeat:
                raise ValueError(
                    f"Copy: {side} walks {len(tap)} patterns in turn; a per-call bound "
                    f"takes one pattern"
                )

    def resolve(self, dev):
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
        """What each channel's transfers split into."""
        pieces = [prod(p.sizes) // self.num_channels for w in self.walks() for p in w]
        return gcd(*pieces, *self._row_shares())

    class Array(Operator.Array):
        def build(self) -> Built:
            ins, outs = [], []
            for c in range(self.num_channels):
                fifo_in = ObjectFifo(self.x.obj_type, depth=self.x.depth)
                fifo_out = fifo_in.cons().forward(depth=self.y.depth)
                ins.append(fifo_in.prod())
                outs.append(fifo_out.cons())
            self.x.bind(ins)
            self.y.bind(outs)
            return Built([])

    def compatible(self) -> None:
        channels = self.num_channels
        step = gcd(*(tap.sizes[-1] for walk in self.walks() for tap in walk))
        if step % channels:
            raise ValueError(
                f"Copy: the innermost axes of {self.src} and {self.dst} have a common "
                f"run of {step} elements, which num_channels ({channels}) must divide"
            )
        for walk in self.walks():
            for tap in walk:
                per_channel = prod(tap.sizes) // channels
                if per_channel % self.tile_size:
                    raise ValueError(
                        f"Copy: tile_size ({self.tile_size}) must divide the per-channel "
                        f"transfer {per_channel} (= {prod(tap.sizes)} / {channels} "
                        f"channels)"
                    )
        for row in self._row_shares():
            if row % self.tile_size:
                raise ValueError(
                    f"Copy: tile_size ({self.tile_size}) must divide the {row} elements "
                    f"per channel one row of the bounded axis moves: a call "
                    f"moves any number of rows"
                )

    def _row_shares(self) -> list[int]:
        """Per bounded pattern, the elements per channel one bounded row moves."""
        src, dst = self.walks()
        return [
            int(
                prod(tap.sizes[bound + 1 :])
                if repeated
                else prod(tap.sizes) // tap.sizes[bound]
            )
            // self.num_channels
            for walk, bound, repeated in (
                (src, self.src_bound, self.src_repeat),
                (dst, self.dst_bound, False),
            )
            if bound is not None
            for tap in walk
        ]

    def _shares(self, tap: TensorAccessPattern) -> list[TensorAccessPattern]:
        """``tap``'s share per channel, in order."""
        step = gcd(*(p.sizes[-1] for walk in self.walks() for p in walk))
        if tap.sizes[-1] != step:
            tap = tap.split(tap.rank - 1, step)
        share = step // self.num_channels
        return [tap[..., c * share : (c + 1) * share] for c in range(self.num_channels)]

    def _taps(
        self, tap: TensorAccessPattern, bound: int | None, operand: Operand
    ) -> list[tuple[TensorAccessPattern, int | None]]:
        """Per channel, its share of ``tap`` and the elements of one unit of
        the dimension a bound patches. A bounded share is one descriptor, its
        bounded axis on D2 where it fits: D2 has no wrap.
        """
        shares = self._shares(tap)
        if bound is None:
            return [(share, None) for share in shares]
        if bound == tap.rank - 1 and self.num_channels > 1:
            raise ValueError(
                f"Copy: {tap} is bounded on the axis the {self.num_channels} channels "
                f"split; bound another axis or copy on one channel"
            )
        rank = shares[0].rank
        dim = 4 - rank + bound
        on_d2 = bound <= 1 and 1 <= rank - bound - 1 <= 2
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
            (run, step), half = dims[-1], dims[-1][0] // 2
            if on_d2 and dims[-2][0] == 1 and step == 1 and run % 2 == 0:
                # A size-1 D1 is dropped, so the bound would take D1's 1023
                # wrap: past it, the run's halves fill D1 instead.
                halves = TensorAccessPattern(
                    share.tensor_dims,
                    share.offset,
                    [*placed.sizes[:2], 2, half],
                    [*placed.strides[:2], half, 1],
                )
                if not operand.fits(placed) and operand.fits(halves):
                    placed = halves
            if not operand.fits(placed):
                raise ValueError(
                    f"Copy: {tap} does not fit one descriptor per channel, which a "
                    f"bounded axis needs (its size is patched in place)"
                )
            sizes, _ = slots(placed.sizes, placed.strides)
            out.append((placed, prod(sizes[(1 if on_d2 else dim) + 1 :])))
        return out

    def ops(self) -> int:
        return 0  # a data mover: its figure is bandwidth

    def reference(
        self,
        x,
        y=None,
        *,
        in_offset=0,
        out_offset=0,
        src_valid=None,
        dst_valid=None,
        src_repeats0=None,
        src_repeats1=None,
        src_repeats2=None,
        src_repeats3=None,
        src_repeats4=None,
        src_repeats5=None,
        src_repeats6=None,
        src_repeats7=None,
    ):
        """Gather by ``src``, scatter by ``dst``, into ``y`` in place if given."""

        # Offsets count elements: the firmware scales the word by the element size.
        def at(tap, bound, valid):
            if valid is None:
                return tap
            return tap[(*[slice(None)] * bound, slice(int(valid)))]

        src, dst = self.walks()
        if self.src_repeat:
            repeats = (
                src_repeats0,
                src_repeats1,
                src_repeats2,
                src_repeats3,
                src_repeats4,
                src_repeats5,
                src_repeats6,
                src_repeats7,
            )
            src = [w if r is None else w[: int(r) + 1] for w, r in zip(src, repeats)]
        src = tuple(at(tap, self.src_bound, src_valid) for tap in src)
        dst = tuple(at(tap, self.dst_bound, dst_valid) for tap in dst)
        gather, scatter = (
            np.concatenate([p.gather(np.arange(prod(p.tensor_dims))) for p in tap])
            + int(offset)
            for tap, offset in ((src, in_offset), (dst, out_offset))
        )
        if len(gather) != len(scatter):
            raise ValueError(
                f"Copy: pattern element counts differ ({len(gather)} vs {len(scatter)}); "
                "src and dst must move the same number of elements"
            )
        out = (
            np.zeros(self.output_buffer_size, dtype=x.dtype)
            if y is None
            else y.reshape(-1)
        )
        out[scatter] = x.reshape(-1)[gather]
        if y is None:
            return out
        # A strided y reshapes to a copy, so the result is written back through it.
        y[...] = out.reshape(y.shape)
        return y

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    @staticmethod
    def _stacked(
        pieces: list[TensorAccessPattern], operand: Operand
    ) -> list[TensorAccessPattern]:
        """``pieces`` with each evenly stepped run made one pattern: twice, so
        rows make runs and runs make a grid.
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
                        and operand.fits(
                            TensorAccessPattern(
                                first.tensor_dims,
                                first.offset,
                                [n + 1, *first.sizes],
                                [step, *first.strides],
                            )
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
        in_off = self.in_offset if self.in_offset.per_call else None
        out_off = self.out_offset if self.out_offset.per_call else None
        if self.src_repeat:
            # The drain first, so the walks' fills queue behind a consumer.
            tg = TaskGroup()
            ((tap, unit),) = self._taps(self.dst, self.dst_bound, self.y)
            self.y.drain(
                tap,
                group=tg,
                wait=True,
                offset_parameter=out_off,
                length_parameter=None if unit is None else self.dst_valid,
                length_unit=unit,
            )
            for k, walk in enumerate(self.walks()[0]):
                ((tap, unit),) = self._taps(walk, self.src_bound, self.x)
                self.x.fill(
                    tap,
                    group=tg,
                    offset_parameter=in_off,
                    length_parameter=None if unit is None else self.src_valid,
                    length_unit=unit,
                    repeat_parameter=self.value(f"src_repeats{k}"),
                )
            tg.finish()
            return
        if isinstance(self.src, tuple) or isinstance(self.dst, tuple):
            # A drain goes out before the fills that feed it.
            issued = []
            for side, walk in enumerate(self.walks()):
                operand = (self.x, self.y)[side]
                for c in range(self.num_channels):
                    at = 0
                    shares = [self._shares(p)[c] for p in walk]
                    for tap in self._stacked(shares, operand):
                        issued.append((at, c, side == 0, tap))
                        at += prod(tap.sizes)
            issued.sort(key=lambda t: t[:3])
            # A channel's drains finish in order, so its last one is the copy's.
            last = {c: i for i, (_, c, fill, _) in enumerate(issued) if not fill}
            tokens = []
            for i, (_, c, fill, tap) in enumerate(issued):
                if fill:
                    self.x.fill(tap, lane=c, offset_parameter=in_off, managed=False)
                    continue
                task = self.y.drain(
                    tap,
                    lane=c,
                    offset_parameter=out_off,
                    wait=last[c] == i,
                    managed=False,
                )
                if last[c] == i:
                    tokens.append(task)
            for task in tokens:
                task.await_()
            return

        ins = self._taps(self.src, self.src_bound, self.x)
        outs = self._taps(self.dst, self.dst_bound, self.y)
        tg = TaskGroup()
        for c in range(self.num_channels):
            tap, unit = ins[c]
            self.x.fill(
                tap,
                lane=c,
                group=tg,
                offset_parameter=in_off,
                length_parameter=None if unit is None else self.src_valid,
                length_unit=unit,
            )
            tap, unit = outs[c]
            self.y.drain(
                tap,
                lane=c,
                group=tg,
                wait=True,
                offset_parameter=out_off,
                length_parameter=None if unit is None else self.dst_valid,
                length_unit=unit,
            )
        tg.finish()
