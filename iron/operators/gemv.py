# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import math
from typing import Any, ClassVar

import aie.dialects.index as index
import aie.dialects.memref as memref
import numpy as np
from aie.dialects.aie import AIETileType, T
from aie.helpers.taplib import TensorAccessPattern
from aie.helpers.util import np_ndarray_type_to_memref_type
from aie.iron import Buffer, ExternalFunction, In, Out, Worker, ceildiv
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import eltwise, linalg
from aie.utils.compile.jit.params import (
    Select,
    divisors,
    param,
    per_call,
    tunable,
    widths,
)
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.declare.operand import concrete
from iron.common.elementwise import (
    Elementwise,
    FinishStep,
    finish_bound,
    finish_reference,
)
from iron.common.testing import Case, Testing

# Bytes [at, at + n) of B from one head tile of a coded A stream: whole
# 64-byte vectors, as a coded tile and B are.
CODED_HEAD_COPY = """
#include <aie_api/aie.hpp>
#include <stdint.h>

extern "C" void coded_head_copy(const uint8_t *__restrict head,
                                uint8_t *__restrict b, int32_t at, int32_t n) {
  for (int32_t i = 0; i < n; i += 64)
    aie::store_v(b + at + i, aie::load_v<64>(head + i));
}
"""


def _cases(cls, dev: Device):
    # M, K, columns, tile_size_input, tile_size_output
    plain = [
        (128, 128, 1, 32, 128),
        (2048, 8192, 8, 1, 256),
        (8192, 2048, 8, 4, 1024),
        # A single-buffered: Gemma 4's down projection.
        (1536, 12288, 8, 1, 64),
    ]
    # ... and num_batches.
    batched = [
        (256, 128, 1, 1, 256, 4),  # tiny
        (256, 128, 8, 1, 32, 100),  # large num_batches: the size-uncapped dim
        (448, 64, 8, 1, 56, 192),  # a multi-dim run split, and many batches
        (64, 1536, 1, 1, 64, 8),  # large K
        (1026, 64, 1, 1, 2, 2),  # a run that needs an even (granule) split
        (1024, 1024, 1, 1, 64, 2),  # batch stride > 2**20
        (512, 64, 8, 4, 64, 32),  # attention's: several rows, a batch per head
    ]
    # ... and repeat: several batches per matrix of A.
    repeated = [
        (256, 128, 2, 1, 64, 8, 4),  # A re-read for each batch it serves
        (256, 128, 2, 1, 64, 4, 4),  # one matrix for every batch
        (1024, 1024, 1, 1, 64, 4, 2),  # matrix stride > 2**20
        (2048, 64, 8, 4, 256, 32, 4),  # Llama decode's scores: 32 heads, 8 groups
    ]
    # ... and two lanes a column.
    laned = [(8192, 2048, 8, 4, 512)]

    widest = dev.cols

    # A case of 8 columns takes all of a narrower device.
    def case(M, K, cols, tsi, tso, *, bench=False, lower=False, **extra):
        kwargs = dict(M=M, K=K, num_aie_columns=min(cols, widest), tile_size_input=tsi)
        kwargs.update(tile_size_output=tso, **extra)
        return Case(kwargs, bench=bench, lower=lower)

    def bench(M, K, cols, *_):
        return min(cols, widest) == widest and M * K >= 2048 * 8192

    return (
        [case(*p, bench=bench(*p)) for p in plain]
        + [
            case(*p, num_batches=batches, lower=i == 0)
            for i, (*p, batches) in enumerate(batched)
        ]
        + [case(*p, num_batches=batches, repeat=r) for *p, batches, r in repeated]
        + [case(*p, bench=bench(*p), num_channels=2) for p in laned]
        + [
            case(256, 128, 2, 1, 32, num_channels=2, num_batches=8),
            case(2048, 64, 4, 4, 256, num_channels=2, num_batches=32, repeat=4),
        ]
        # ... and B a real stream of its own, broadcast to every lane.
        + [case(2048, 2048, 8, 4, 256, feed_b=True)]
        # ... and A as coded rows: Llama 3.2 1B's decode shapes, B in A's
        # head tile, in two where one coded row is shorter than B (2048x8192
        # at one row a tile), and on its own stream.
        + [
            case(8192, 2048, 8, 4, 1024, coded_a=True, bench=True, lower=True),
            case(2048, 2048, 4, 4, 256, coded_a=True, lower=True),
            case(2048, 8192, 8, 1, 256, coded_a=True, lower=True),
            case(2048, 8192, 8, 1, 256, coded_a=True, feed_b=True),
            case(8192, 2048, 8, 4, 512, coded_a=True, num_channels=2),
            case(128, 128, 1, 32, 128, coded_a=True),
        ]
    )


class GEMV(Operator):
    """``C = A @ B`` as row-blocks of A per lane, ``tile_size_input`` rows per mv.cc call.

    By default B rides each lane's A stream ahead of its rows so every input channel of
    a column can carry A; ``feed_b`` instead makes B a real stream of its own, broadcast
    to every lane since each one's dot products read the whole vector, which
    ``B.feed()`` can then take from another operator's output on-chip.
    """

    test = Testing(_cases, draw=lambda op: dict(normal=(op.A, op.B)))

    M: int = param()
    K: int = param()
    # None: a single batch, with no batch dimension.
    num_batches: int | None = param(default=None)
    # Batches per matrix of A (grouped-query scores): no repeated copy.
    repeat: int = param(default=1)
    num_matrices: int | None = param(
        derive=lambda op: (
            None if op.num_batches is None else op.num_batches // op.repeat
        )
    )
    num_aie_columns: int = tunable(domain=widths)
    num_channels: int = tunable(domain=widths)
    # None: two rows where they fit one L1 programmer bank, else one.
    tile_size_input: int = tunable(
        domain=lambda op, dev, t: divisors(
            t,
            of=op.M,
            cap=dev.core_memory_bytes
            // (op.A.depth * op.K * np.dtype(bfloat16).itemsize),
        )
    )
    # At least two rows: the shim moves C in 4-byte granules.
    tile_size_output: int = tunable(
        domain=lambda op, dev, t: divisors(t, of=op.M, step=op.tile_size_input, span=3)
    )
    kernel_vector_size: int = tunable(repr=False)
    # Filled by resolve: A double-buffered where two of its tiles fit a core, else one.
    a_depth: int = tunable(repr=False, init=False)
    # False (the head-tile layout) unless a fed B, or fusion pricing, asks
    # for B's own stream: that costs a shim input channel, so it is not free.
    feed_b: bool = tunable(default=False, domain=(False, True))
    # A, a weight, streams as coded rows (aie.utils.coded): 0.76x the bytes,
    # decoded in each core into the bits plain A gives.
    coded_a: bool = tunable(default=False, domain=(False, True))
    a_capacity: int = param(default=15, array=True)
    # One step folded into these cores, its output C's tile.
    finish: tuple[FinishStep, ...] = param(default=(), array=True)
    # A plain default, not derived: shim_columns() reads it from the class
    # alone (a Testing case), before any instance exists to derive it from.
    uses_extra: bool = param(default=False)
    # feed_b already holds both of a core's input channels; a finish input
    # then rides A's instead of its own (A's own tile re-read, below C's).
    rides: bool = param(default=False, array=True)

    A = In(
        num_matrices,
        M,
        K,
        obj_shape=(tile_size_input, K),
        per=(num_aie_columns, num_channels),
        depth=2,
        coded=coded_a,
        capacity=a_capacity,
    )
    B = In(num_batches, K, obj_shape=Select(feed_b, (K,), None))
    C = Out(
        num_batches,
        M,
        obj_shape=(tile_size_output,),
        per=(num_aie_columns, num_channels),
        depth=2,
    )
    # A finish step's other input, on the channel feed_b would otherwise use,
    # or, riding, no stream of its own (A's tile carries it, re-read).
    finish0 = In(
        num_batches,
        M,
        obj_shape=Select(rides, None, (tile_size_output,)),
        per=(num_aie_columns, num_channels),
        depth=2,
        when=uses_extra,
    )
    valid = per_call(bounds=M)
    tiles = per_call(
        derive=lambda op: ceildiv(
            op.valid, op.num_aie_columns * op.num_channels * op.tile_size_output
        ),
    )
    batches = per_call(derive=lambda op: op.num_batches or 1)

    def extent_unit(self, buffer: str) -> int | None:
        # A in output tiles, so its rows and C's line up under the round-robin split.
        return self.tile_size_output if buffer == "A" else None

    # mv.cc's widths, widest first; narrower than 16 is untested, so refused.
    _KERNEL_VECTOR_SIZES: ClassVar[tuple[int, ...]] = (64, 32, 16)
    # bf16 elements in one of eltwise.passthrough's 64-byte vectors.
    _COPY_ELEMENTS: ClassVar[int] = 32
    # Safe: C's drains go out before the fills feeding them.
    aiecc_flags: ClassVar[tuple[str, ...]] = ("--reclaim-runtime-bds",)

    def validate(self):
        if self.repeat < 1 or (self.num_batches or 1) % self.repeat:
            raise ValueError(
                f"GEMV: repeat ({self.repeat}) must divide num_batches "
                f"({self.num_batches})"
            )
        tso, tsi = self.tile_size_output, self.tile_size_input
        if tso is not None and tsi is not None and not (tso % tsi == 0 and tso >= tsi):
            raise ValueError(
                f"GEMV: tile_size_output ({tso}) must be a multiple of "
                f"tile_size_input ({tsi})"
            )
        self._legal_kernel_vector_size()
        if not self.feed_b and self.K % self._COPY_ELEMENTS:
            raise ValueError(
                f"GEMV: K ({self.K}) must be a multiple of {self._COPY_ELEMENTS}: "
                f"each core copies B out of its A stream in "
                f"{self._COPY_ELEMENTS}-element vectors"
            )
        if self.coded_a:
            self._validate_coded()
        if self.finish:
            if sum(f.binary for f in self.finish) > 1:
                raise ValueError(
                    "GEMV: only one of its finish steps takes another input; "
                    "its one free input channel is already another's"
                )
            if self.feed_b and not self.rides:
                raise ValueError(
                    "GEMV: feed_b already holds both of a core's input "
                    "channels, leaving none for a finish step's other input "
                    "that does not ride A's"
                )
            if self.repeat > 1:
                raise ValueError(
                    f"GEMV: repeat ({self.repeat}) computes its batches out of "
                    f"order, which a finish step's input does not follow"
                )

    def _validate_coded(self):
        if self.K % 64:
            raise ValueError(
                f"GEMV: coded_a needs K ({self.K}) a multiple of 64, the "
                f"coded rows' unit"
            )
        if self.repeat > 1:
            raise ValueError(
                f"GEMV: coded_a codes a weight; repeat ({self.repeat}) re-reads "
                f"an activation A"
            )
        if self.rides:
            raise ValueError(
                "GEMV: coded_a's tiles are coded rows, which a finish input "
                "cannot ride"
            )

    def _head_tiles(self) -> int:
        """Return the tiles of A's stream that carry B to a lane each batch.

        One, or for a coded tile shorter than B's 2K bytes, as many as hold it.
        """
        if not self.coded_a:
            return 1
        return -(-2 * self.K // math.prod(self.A.obj_shape))

    def _legal_kernel_vector_size(self) -> int:
        """Return the vector width the matvec kernel is compiled at.

        mv.cc's static_asserts, ``K % w == 0`` and ``K >= 2 * w``,
        checked here.
        """
        legal = [
            size
            for size in self._KERNEL_VECTOR_SIZES
            if self.K % size == 0 and self.K >= 2 * size
        ]
        if self.kernel_vector_size is None:
            if not legal:
                raise ValueError(
                    f"GEMV: K ({self.K}) has no legal kernel_vector_size: need a "
                    f"width w in {self._KERNEL_VECTOR_SIZES} with K % w == 0 and "
                    "K >= 2*w, so K must be an even multiple of at least 16"
                )
            return legal[0]
        if self.kernel_vector_size not in legal:
            raise ValueError(
                f"GEMV: kernel_vector_size ({self.kernel_vector_size}) is not legal "
                f"for K ({self.K}): the matvec kernel needs K % kernel_vector_size "
                f"== 0 and K >= 2*kernel_vector_size; "
                + (
                    f"legal here: {legal}"
                    if legal
                    else "no width works for this K, which must be an even multiple "
                    "of at least 16"
                )
            )
        return self.kernel_vector_size

    def resolve(self, dev):
        # With no device bound, two rows, unchecked.
        two_rows = 2 * self.K * np.dtype(bfloat16).itemsize
        fits = dev is None or two_rows <= dev.core_memory_bank_bytes
        rows = self.tile_size_input or (2 if fits else 1)
        channels = self.num_channels or 1
        tile = self.tile_size_output or max(rows, 2)
        unit = math.lcm(tile, rows)
        cols = self.resolve_columns(
            dev,
            self.num_aie_columns,
            channels,
            fits=lambda c: self.M % (c * channels * unit) == 0,
        )
        new = self.replace(
            num_aie_columns=cols,
            num_channels=channels,
            tile_size_input=rows,
            tile_size_output=tile,
            kernel_vector_size=self._legal_kernel_vector_size(),
        )
        if dev is None:
            return new.replace(a_depth=self.a_depth or new.A.depth)
        item = np.dtype(bfloat16).itemsize
        line, out = self.K * item, new.tile_size_output * item
        tile_bytes = (
            new.tile_size_input * new.A.shape[-1] * np.dtype(new.A.dtype).itemsize
        )
        rest = line + new.C.depth * out + dev.default_core_stack_bytes
        if new.coded_a:
            # The rows a call decodes into, which the matvec then reads.
            rest += new.tile_size_input * line
        depth = self.a_depth or new.A.depth
        if self.a_depth is None and depth * tile_bytes + rest > dev.core_memory_bytes:
            depth = 1
        held = depth * tile_bytes + rest
        if held > dev.core_memory_bytes:
            raise ValueError(
                f"GEMV: K ({self.K}), tile_size_input ({new.tile_size_input}), "
                f"tile_size_output ({new.tile_size_output}): a core holds {held} "
                f"bytes, past its {dev.core_memory_bytes}"
            )
        return new.replace(a_depth=depth)

    def compatible(self):
        lanes = self.num_aie_columns * self.num_channels
        rows = self.M // lanes
        if self.M % lanes:
            raise ValueError(f"GEMV: M ({self.M}) must divide across {lanes} lanes")
        for name, tile in (
            ("tile_size_output", self.tile_size_output),
            ("tile_size_input", self.tile_size_input),
        ):
            if tile > rows:
                raise ValueError(f"GEMV: {name} ({tile}) exceeds M/lanes ({rows})")
            if rows % tile:
                raise ValueError(f"GEMV: {name} ({tile}) must divide M/lanes ({rows})")

    def fold(self, consumer, at: int):
        if not isinstance(consumer, Elementwise) or self.repeat > 1:
            return None
        others = [i for i in range(len(consumer.inputs)) if i != at]
        if len(others) > 1:
            return None
        binary = bool(others)
        used = sum(b.streamed for b in self.inputs)
        rides = False
        if binary and used + 1 > self.dev.core_dma_channels_in:
            if self.rides or not self._can_ride():
                return None
            rides = True
        dims = tuple(
            sorted(
                (n, vars(consumer)[n])
                for n, p in type(consumer).declaration.params.items()
                if p.init
                and n
                not in (
                    "size",
                    "tile_size",
                    "num_aie_columns",
                    "num_channels",
                    "finish",
                    "uses_extra",
                    "rides",
                )
                and vars(consumer)[n] is not None
            )
        )
        step = FinishStep(type(consumer), dims, at, binary)
        return self.replace(
            finish=self.finish + (step,),
            uses_extra=self.uses_extra or binary,
            rides=self.rides or rides,
        )

    def _can_ride(self) -> bool:
        """Whether A's own tile could carry a finish's other input instead of a stream of its own.

        No batches or per-call bound to walk it by (one tile is this whole call, so one
        extra transfer a lane suffices), A's tile holds a whole number of a finish
        tile's, re-read at most a descriptor's iteration limit, and a lane's extra
        transfer still fits its shim tile's descriptor budget.
        """
        if self.bound_extents or self.num_batches is not None or self.coded_a:
            return False
        try:
            lanes = self.num_aie_columns * self.num_channels
            if self.M != lanes * self.tile_size_output:
                return False
            carried, line = self.tile_size_input * self.K, self.tile_size_output
            if carried % line:
                return False
        except TypeError:  # a tunable not yet resolved: not decidable here
            return False
        dev = self.dev
        if carried // line > (1 << dev.get_dma_bd_iter_bits(0, 0)):
            return False
        shims = sum(
            dev.get_tile_type(col, 0) is AIETileType.ShimNOCTile
            for col in range(dev.cols)
        )
        held = (
            dev.get_num_bds(AIETileType.ShimNOCTile)
            * shims
            // (dev.shim_dma_channels_in + dev.shim_dma_channels_out)
        )
        return 2 <= held

    def build(self) -> Built:
        K, lanes = self.K, self.num_aie_columns * self.num_channels
        tile_size_input, tile_size_output = (
            self.tile_size_input,
            self.tile_size_output,
        )

        # Built here, not at import: CompilableDesign clears earlier ExternalFunctions.
        matvec = linalg.mv(
            tile_size_input,
            K,
            bfloat16,
            bfloat16,
            vectorized=True,
            vec_size=self.kernel_vector_size,
            output_rows=tile_size_output,
            a_coded=self.coded_a,
        )
        # The decoded rows of a coded tile, one buffer a lane: matvec's A.
        decoded = [
            [Buffer(matvec.arg_types()[3])] if self.coded_a else []
            for _ in range(lanes)
        ]

        A_ends = self.A.fifos(self.a_depth)
        C_ends = self.C.fifos(self.C.depth)
        rtps = [Rtp([self.tiles, self.batches]) for _ in range(lanes)]

        if not self.feed_b:
            if self.B.fed_from is not None:
                raise ValueError(
                    "GEMV: B is fed, which needs feed_b=True: unfed, its vector "
                    "rides each lane's A stream, which a fed input cannot take"
                )
            vector = np.ndarray[(K,), np.dtype[bfloat16]]
            if not self.coded_a:
                # A lossless copy of the head tile's first row, B, as 16-bit words.
                copy = eltwise.passthrough(K, np.int16).object_file.bind(
                    "passThroughLine", [self.A.obj_type, vector, np.int32]
                )
                # Per head tile, the copy's arguments past the tile and b.
                head_copies = [(K,)]
            else:
                # B's 2K bytes, from as many coded tiles as hold them. The
                # symbol is the tile type's own, beside a plain GEMV's.
                copy = ExternalFunction(
                    "coded_head_copy",
                    source_string=CODED_HEAD_COPY,
                    arg_types=[self.A.obj_type, vector, np.int32, np.int32],
                    symbol_prefix="coded_head_" + "x".join(map(str, self.A.obj_shape)),
                )
                tile, total = math.prod(self.A.obj_shape), 2 * K
                head_copies = [
                    (h * tile, min(tile, total - h * tile))
                    for h in range(self._head_tiles())
                ]
            vectors = [Buffer(vector) for _ in range(lanes)]

            if not self.finish:

                def core_body(A_fifo, C_fifo, b, matvec, copy, rtp, *decoded):
                    words = rtp.read()
                    n = words[self.tiles]
                    batches = words[self.batches]
                    for _ in range_(batches):
                        # The batch's head tiles carry B.
                        for args in head_copies:
                            head = A_fifo.acquire(1)
                            copy(head, b, *args)
                            A_fifo.release(1)
                        for _ in range_(n):
                            c = C_fifo.acquire(1)
                            for j_idx in range_(tile_size_output // tile_size_input):
                                j_i32: Any = index.casts(T.i32(), j_idx)
                                output_row_offset = j_i32 * tile_size_input
                                a = A_fifo.acquire(1)
                                matvec(
                                    tile_size_input,
                                    output_row_offset,
                                    a,
                                    *decoded,
                                    b,
                                    c,
                                )
                                A_fifo.release(1)
                            C_fifo.release(1)

                workers = [
                    Worker(
                        core_body,
                        [A_ends[i], C_ends[i], vectors[i], matvec, copy, rtps[i]]
                        + decoded[i],
                    )
                    for i in range(lanes)
                ]
                return Built(workers, rtps)

            # The chain of steps folded into these cores: each kernel runs
            # after the one before it, over the tile the previous call
            # wrote in a scratch buffer, ping-ponging between two until the
            # last writes C; at most one step's other input streams in on
            # finish0, or, riding, is A's own tile re-read, cast down to one
            # finish tile's size (A's holds several, identical repeats).
            binary_finish = any(f.binary for f in self.finish)
            of_finish = (
                self.finish0.fifos() if binary_finish and not self.rides else None
            )
            ride_view = (
                np_ndarray_type_to_memref_type(
                    np.ndarray[(tile_size_output,), np.dtype[bfloat16]]
                )
                if binary_finish and self.rides
                else None
            )
            chain_meta = []
            chain_kernels = []
            for step in self.finish:
                consumer = step.consumer_at(tile_size_output, self.dev)
                c_kernel = consumer.layout().kernel()
                c_positions, c_scalars = consumer.arguments(
                    c_kernel, consumer.scalars(), len(consumer.inputs), 1
                )
                c_order = {i: j for j, i in enumerate(c_positions)}
                n_c_args = len(c_positions) + len(c_scalars)
                chain_kernels.append(c_kernel)
                chain_meta.append(
                    (c_positions, c_scalars, c_order, n_c_args, step.at, step.binary)
                )
            scratch_ty = np.ndarray[(tile_size_output,), np.dtype[bfloat16]]
            # A second scratch buffer, to ping-pong, only past one finish
            # step: an L1 line this core otherwise never holds at once.
            scratch_as = [Buffer(scratch_ty) for _ in range(lanes)]
            scratch_bs = (
                [Buffer(scratch_ty) for _ in range(lanes)]
                if len(chain_meta) > 1
                else None
            )

            def core_body_chain(*args):
                A_fifo, C_fifo, b, matvec, copy = args[:5]
                tail = args[5:]
                finish_fifo = tail[0] if of_finish is not None else None
                tail = tail[1:] if of_finish is not None else tail
                chain_fns = tail[: len(chain_meta)]
                tail = tail[len(chain_meta) :]
                lane_decoded = tail[len(tail) - len(decoded[0]) :]
                tail = tail[: len(tail) - len(decoded[0])]
                if scratch_bs is not None:
                    scratch_a, scratch_b, rtp = tail
                else:
                    scratch_a, rtp = tail
                    scratch_b = None
                words = rtp.read()
                n = words[self.tiles]
                batches = words[self.batches]
                for _ in range_(batches):
                    for args in head_copies:
                        head = A_fifo.acquire(1)
                        copy(head, b, *args)
                        A_fifo.release(1)
                    for _ in range_(n):
                        c = C_fifo.acquire(1)
                        for j_idx in range_(tile_size_output // tile_size_input):
                            j_i32: Any = index.casts(T.i32(), j_idx)
                            output_row_offset = j_i32 * tile_size_input
                            a = A_fifo.acquire(1)
                            matvec(
                                tile_size_input,
                                output_row_offset,
                                a,
                                *lane_decoded,
                                b,
                                scratch_a,
                            )
                            A_fifo.release(1)
                        tile = scratch_a
                        for idx, (c_fn, meta) in enumerate(zip(chain_fns, chain_meta)):
                            c_positions, c_scalars, c_order, n_c_args, at, binary = meta
                            last = idx == len(chain_meta) - 1
                            dst = (
                                c
                                if last
                                else (scratch_b if tile is scratch_a else scratch_a)
                            )
                            extra = None
                            if binary and ride_view is not None:
                                ridden = A_fifo.acquire(1)
                                extra = memref.reinterpret_cast(
                                    ride_view,
                                    ridden,
                                    [],
                                    [],
                                    [],
                                    [0],
                                    [tile_size_output],
                                    [1],
                                )
                            elif binary:
                                extra = finish_fifo.acquire(1)
                            c_inputs = [
                                tile if i == at else extra
                                for i in range(len(c_positions) - 1)
                            ]
                            c_elements = c_inputs + [dst]
                            c_fn(
                                *(
                                    (
                                        c_elements[c_order[i]]
                                        if i in c_order
                                        else c_scalars[i]
                                    )
                                    for i in range(n_c_args)
                                )
                            )
                            if binary and ride_view is not None:
                                A_fifo.release(1)
                            elif binary:
                                finish_fifo.release(1)
                            tile = dst
                        C_fifo.release(1)

            workers = [
                Worker(
                    core_body_chain,
                    [A_ends[i], C_ends[i], vectors[i], matvec, copy]
                    + ([of_finish[i]] if of_finish is not None else [])
                    + chain_kernels
                    + [scratch_as[i]]
                    + ([scratch_bs[i]] if scratch_bs is not None else [])
                    + [rtps[i]]
                    + decoded[i],
                )
                for i in range(lanes)
            ]
            return Built(workers, rtps)

        # One fifo, a fresh cons() per core: every lane reads the same
        # vector, not a share of it. Depth 1, as the local buffer it
        # replaces held: resolve()'s memory budget counts one copy. Fed,
        # this gives every core its own reader end of the source's fifo.
        (B_ends,) = self.B.fifos(1, readers=lanes)

        def core_body(A_fifo, B_fifo, C_fifo, matvec, rtp, *decoded):
            words = rtp.read()
            n = words[self.tiles]
            batches = words[self.batches]
            for _ in range_(batches):
                b = B_fifo.acquire(1)
                for _ in range_(n):
                    c = C_fifo.acquire(1)
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32: Any = index.casts(T.i32(), j_idx)
                        output_row_offset = j_i32 * tile_size_input
                        a = A_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, *decoded, b, c)
                        A_fifo.release(1)
                    C_fifo.release(1)
                B_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [A_ends[i], B_ends[i], C_ends[i], matvec, rtps[i]] + decoded[i],
            )
            for i in range(lanes)
        ]
        return Built(workers, rtps)

    def sequence(self, rt):
        """Per batch and lane.

        B's head tile (``feed_b``: one fill to B's own stream instead), then A's rows. C
        drains are issued first: an undrained C would stop A.
        """
        if self.repeat > 1:
            for buf in (self.A, self.C):
                if buf.bounded is not None:
                    raise ValueError(
                        f"GEMV: {buf.name} takes no per-call bound when repeat "
                        f"({self.repeat}) is above 1"
                    )
        M, K, tsi = self.M, self.K, self.tile_size_input
        # A's row as it moves: K elements, or a coded row's bytes.
        width = self.A.shape[-1]
        drains = [
            self.C.drain(
                tap,
                lane=k,
                wait=True,
                length_parameter=word,
                length_unit=unit,
                managed=False,
            )
            for k, tap, word, unit in self.C.transfers()
        ]
        binary_finish = any(f.binary for f in self.finish)
        riding = binary_finish and self.rides
        if binary_finish and not self.rides:
            # finish0's shape matches C's, so the same per-lane walk fills it.
            for k, tap, word, unit in self.finish0.transfers():
                self.finish0.fill(
                    tap, lane=k, length_parameter=word, length_unit=unit, managed=False
                )
        ride_taps = {k: tap for k, tap, _, _ in self.C.transfers()} if riding else {}
        reads = (tsi * K) // self.tile_size_output if riding else 0
        rows = self.A.transfers()
        if (self.num_matrices or 1) > 1 and self.A.bounded is None:
            parts = TensorAccessPattern.full((M, width)).partition(len(rows), 0)
            rows = [
                (
                    k,
                    TensorAccessPattern(
                        self.A.shape, part.offset, part.sizes, part.strides
                    ),
                    None,
                    None,
                )
                for (k, _, _, _), part in zip(rows, parts, strict=True)
            ]
        elif (self.num_matrices or 1) > 1:
            rows = [
                (
                    k,
                    TensorAccessPattern(
                        tap.tensor_dims,
                        tap.offset,
                        [1, *tap.sizes[1:]],
                        [0, *tap.strides[1:]],
                    ),
                    word,
                    unit,
                )
                for k, tap, word, unit in rows
            ]
        for b in range(self.num_batches or 1):
            if self.feed_b:
                self.B.fill(
                    TensorAccessPattern(self.B.shape, b * K, [1, K], [0, 1]),
                    managed=False,
                )
            elif self.coded_a:
                # B, then the rest of its last head tile, unread: A's first
                # bytes, one linear run.
                pad = self._head_tiles() * tsi * width - 2 * K
                heads = [
                    (TensorAccessPattern(self.B.shape, b * K, [1, K], [0, 1]), self.B)
                ]
                if pad:
                    heads.append(
                        (TensorAccessPattern(self.A.shape, 0, [1, pad], [0, 1]), None)
                    )
            else:
                # B's row repeated over an A tile in the iteration dim (stride 0).
                heads = [
                    (
                        TensorAccessPattern(
                            self.B.shape, b * K, [tsi, 1, 1, K], [0, 0, 0, 1]
                        ),
                        self.B,
                    )
                ]
            for k, tap, word, unit in rows:
                if not self.feed_b:
                    for head, source in heads:
                        self.A.fill(head, lane=k, source=source, managed=False)
                (offset,) = concrete((tap.offset,), tap)
                matrix = TensorAccessPattern(
                    tap.tensor_dims,
                    offset + b // self.repeat * M * width,
                    tap.sizes,
                    tap.strides,
                )
                self.A.fill(
                    matrix,
                    lane=k,
                    length_parameter=word,
                    length_unit=unit,
                    managed=False,
                )
                if riding:
                    # The finish's row, re-read to fill one of A's tiles.
                    self.A.fill(
                        ride_taps[k].repeat(reads),
                        lane=k,
                        source=self.finish0,
                        managed=False,
                    )
        for task in drains:
            if task is not None:
                task.await_()

    def ops(self) -> int:
        total = 2 * self.M * self.K * (self.num_batches or 1)
        for step in self.finish:
            consumer = step.consumer_at(self.tile_size_output, self.dev)
            total += (
                consumer.ops()
                * self.M
                * (self.num_batches or 1)
                // self.tile_size_output
            )
        return total

    def reference(self, A, B, finish0=None):
        """``C = A @ B``, one product per batch, then its finish step's."""
        c = self._matvec_reference(A, B)
        if not self.finish:
            return c
        extra = () if finish0 is None else (finish0,)
        return finish_reference(self.finish, c, extra, self.dev, self.tile_size_output)

    def _matvec_reference(self, A, B):
        if self.repeat > 1:
            A = np.repeat(A.reshape(-1, *A.shape[-2:]), self.repeat, axis=0)
        # float32: numpy's bf16 matmul accumulates in bf16, the kernel in f32.
        a, b = A.astype(np.float32), B.astype(np.float32)
        if A.ndim == 3:
            b = b.reshape(A.shape[0], A.shape[2], 1)
            return np.matmul(a, b).reshape(A.shape[0], A.shape[1]).astype(A.dtype)
        return (a @ b.reshape(A.shape[-1])).astype(A.dtype)

    def tolerance(self) -> Tolerance:
        """C accumulates in f32 and rounds once; tighter than linalg.mv's contract, then each finish step's own."""
        own = Tolerance.relative(0.04, 1e-3, note="f32 accumulation, rounded once")
        if not self.finish:
            return own
        return Tolerance.bounded(
            finish_bound(
                self.finish,
                own,
                self._matvec_reference,
                2,
                bfloat16,
                self.dev,
                self.tile_size_output,
            ),
            note="f32 accumulation rounded once, then each finish step's contract",
        )
