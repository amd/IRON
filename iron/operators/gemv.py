# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import math
from typing import Any, ClassVar

import aie.dialects.index as index
import numpy as np
from aie.dialects.aie import T
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, Out, Worker, ceildiv
from aie.iron.controlflow import range_
from aie.iron.device import Device
from aie.iron.kernels import eltwise, linalg
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import divisors, param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing


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

    def case(M, K, cols, tsi, tso, *, bench=False, lower=False, **extra):
        kwargs = dict(M=M, K=K, num_aie_columns=cols, tile_size_input=tsi)
        kwargs.update(tile_size_output=tso, **extra)
        return Case(kwargs, bench=bench, lower=lower)

    widest = dev.cols

    def bench(M, K, cols, *_):
        return cols == widest and M * K >= 2048 * 8192

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
    )


class GEMV(Operator):
    """``C = A @ B`` as row-blocks of A per lane, ``tile_size_input`` rows per
    mv.cc call; B rides each lane's A stream ahead of its rows so every
    input channel of a column can carry A.
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

    A = In(
        num_matrices,
        M,
        K,
        obj_shape=(tile_size_input, K),
        per=(num_aie_columns, num_channels),
        depth=2,
    )
    B = In(num_batches, K)
    C = Out(
        num_batches,
        M,
        obj_shape=(tile_size_output,),
        per=(num_aie_columns, num_channels),
        depth=2,
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
        if self.K % self._COPY_ELEMENTS:
            raise ValueError(
                f"GEMV: K ({self.K}) must be a multiple of {self._COPY_ELEMENTS}: "
                f"each core copies B out of its A stream in "
                f"{self._COPY_ELEMENTS}-element vectors"
            )

    def _legal_kernel_vector_size(self) -> int:
        """The vector width the matvec kernel is compiled at: mv.cc's
        static_asserts, ``K % w == 0`` and ``K >= 2 * w``, checked here.
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
        tile_bytes = new.tile_size_input * line
        rest = line + new.C.depth * out + dev.default_core_stack_bytes
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
        )
        vector = np.ndarray[(K,), np.dtype[bfloat16]]
        # A lossless copy of the head tile's first row, B, as 16-bit words.
        copy = eltwise.passthrough(K, np.int16).object_file.bind(
            "passThroughLine", [self.A.obj_type, vector, np.int32]
        )

        A_ends = self.A.fifos(self.a_depth)
        C_ends = self.C.fifos(self.C.depth)
        vectors = [Buffer(vector) for _ in range(lanes)]
        rtps = [Rtp([self.tiles, self.batches]) for _ in range(lanes)]

        def core_body(A_fifo, C_fifo, b, matvec, copy, rtp):
            words = rtp.read()
            n = words[self.tiles]
            batches = words[self.batches]
            for _ in range_(batches):
                # The batch's head tile carries B.
                head = A_fifo.acquire(1)
                copy(head, b, K)
                A_fifo.release(1)
                for _ in range_(n):
                    c = C_fifo.acquire(1)
                    for j_idx in range_(tile_size_output // tile_size_input):
                        j_i32: Any = index.casts(T.i32(), j_idx)
                        output_row_offset = j_i32 * tile_size_input
                        a = A_fifo.acquire(1)
                        matvec(tile_size_input, output_row_offset, a, b, c)
                        A_fifo.release(1)
                    C_fifo.release(1)

        workers = [
            Worker(
                core_body,
                [
                    A_ends[i],
                    C_ends[i],
                    vectors[i],
                    matvec,
                    copy,
                    rtps[i],
                ],
            )
            for i in range(lanes)
        ]
        return Built(workers, rtps)

    def sequence(self, rt):
        """Per batch and lane: B's head tile, then A's rows. C drains are
        issued first: an undrained C would stop A.
        """
        if self.repeat > 1:
            for buf in (self.A, self.C):
                if buf.bounded is not None:
                    raise ValueError(
                        f"GEMV: {buf.name} takes no per-call bound when repeat "
                        f"({self.repeat}) is above 1"
                    )
        M, K, tsi = self.M, self.K, self.tile_size_input
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
        rows = self.A.transfers()
        if (self.num_matrices or 1) > 1 and self.A.bounded is None:
            parts = TensorAccessPattern.full((M, K)).partition(len(rows), 0)
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
            # B's row repeated over an A tile in the iteration dim (stride 0).
            head = TensorAccessPattern(
                self.B.shape, b * K, [tsi, 1, 1, K], [0, 0, 0, 1]
            )
            for k, tap, word, unit in rows:
                self.A.fill(head, lane=k, source=self.B, managed=False)
                matrix = TensorAccessPattern(
                    tap.tensor_dims,
                    tap.offset + b // self.repeat * M * K,
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
        for task in drains:
            if task is not None:
                task.await_()

    def ops(self) -> int:
        return 2 * self.M * self.K * (self.num_batches or 1)

    def reference(self, A, B):
        """``C = A @ B``, one product per batch."""
        if self.repeat > 1:
            A = np.repeat(A.reshape(-1, *A.shape[-2:]), self.repeat, axis=0)
        # float32: numpy's bf16 matmul accumulates in bf16, the kernel in f32.
        a, b = A.astype(np.float32), B.astype(np.float32)
        if A.ndim == 3:
            b = b.reshape(A.shape[0], A.shape[2], 1)
            return np.matmul(a, b).reshape(A.shape[0], A.shape[1]).astype(A.dtype)
        return (a @ b.reshape(A.shape[-1])).astype(A.dtype)

    def tolerance(self) -> Tolerance:
        """C accumulates in f32 and rounds once; tighter than linalg.mv's contract."""
        return Tolerance.relative(0.04, 1e-3, note="f32 accumulation, rounded once")
