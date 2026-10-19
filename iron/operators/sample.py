# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sample: the next token, drawn on the device from a row of bf16 logits.

Temperature and top-k sampling bit for bit as
``aie.iron.kernels.sample.sample_ref``, from a four-word draw row the host
writes ahead of time per position. Each column's core reduces its slice of
the logits to a top-k summary; one combine core draws the token from them.
"""

from functools import cache

import numpy as np
from aie.dialects.aie import WireBundle, get_target_model
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, In, InOut, ObjectFifo, Out, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import sample
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import divisors, param, per_call, tunable, widths
from ml_dtypes import bfloat16

from iron.common import Built, Operator, Unresolvable
from iron.common.testing import Case, Testing

# A select core's logits object: no more than this, and even (4-byte DMA).
_CHUNK_LIMIT = 8192


def _largest_chunk(run: int, calls: int) -> int | None:
    """The largest legal chunk of `run` logits that takes at most `calls` calls."""
    for n in range(-(-run // _CHUNK_LIMIT), calls + 1):
        if run % n == 0 and run // n % 2 == 0:
            return run // n
    return None


@cache
def slices(vocab: int, cores: int, k_max: int) -> tuple[int, int]:
    """`(slice, last)`: the logits each select core but the last reads, and the last's.

    An even split where there is one, else the smallest slice of the fewest calls.
    """
    if vocab % cores == 0 and vocab // cores % 2 == 0 and vocab // cores >= k_max:
        return vocab // cores, vocab // cores
    least = -(-vocab // cores)
    least += least % 2
    best, fewest = None, -(-least // _CHUNK_LIMIT)
    for size in range(least, (vocab - k_max) // max(cores - 1, 1) + 1, 2):
        last = vocab - (cores - 1) * size
        calls = best[0] - 1 if best else size // 2
        chunk = _largest_chunk(size, calls)
        tail = chunk and _largest_chunk(last, calls)
        if tail:
            best = (max(size // chunk, last // tail), size, last)
            if best[0] == fewest:
                break
    if best is None:
        raise ValueError(
            f"Sample: vocab ({vocab}) does not split over {cores} cores into even "
            f"slices (4-byte DMA) of at least k_max ({k_max})"
        )
    return best[1], best[2]


def reference(logits, draw_row, k_max: int | None = None) -> int:
    """The token the device draws for one draw row; an all-zero row is greedy."""
    words = np.asarray(draw_row, dtype=np.int32)
    row = words.view(np.uint32)
    temperature = row[0:1].view(np.float32)[0]
    n53 = int(row[2]) | int(row[3]) << 32
    top_k = max(int(words[1]), 1)
    return sample.sample_ref(logits, temperature, top_k, n53, k_max=k_max)


def _logits(op: "Sample") -> dict:
    """Logits with a few ties at the top, and one draw row per position."""
    rng = np.random.default_rng(11)
    logits = rng.normal(0, 3, op.vocab).astype(bfloat16)
    logits[rng.choice(op.vocab, 8, replace=False)] = logits.max()
    draws = np.stack(
        [
            sample.draw_row(t, k, int(rng.integers(0, 1 << 53)))
            for t, k in zip(
                rng.choice([0.0, 0.7, 1.0], op.steps), rng.integers(1, 51, op.steps)
            )
        ]
    )
    return dict(
        given={
            op.logits: logits,
            op.draws: draws,
            op.tokens: np.full(op.steps, -1, dtype=np.int32),
        }
    )


class Sample(Operator):
    """Draw the next token from a row of logits (exact temperature/top-k)."""

    # A token id; anything but exact is wrong.
    test = Testing(
        [
            Case(dict(vocab=4096, cores=4, steps=3), id="small"),
            Case(dict(vocab=4096, cores=2, chunk=256), id="two_cores"),
            Case(dict(vocab=128256, cores=4), id="llama", bench=True),
            # No even split: three slices of 14560, and 8186 left for the last.
            Case(dict(vocab=51866, cores=4), id="uneven", lower=True),
        ],
        draw=_logits,
    )

    vocab: int = param(array=True)
    k_max: int = param(default=64, array=True)
    # Positions the draws and the record hold; the sequence picks one.
    steps: int = param(default=1)
    cores: int = tunable(default=4, domain=widths)
    # Logits per select call.
    chunk: int = tunable(
        domain=lambda op, dev, t: divisors(
            t, of=op.slice_size, step=2, cap=_CHUNK_LIMIT
        )
    )

    logits = In(vocab, obj_shape=(chunk,), per=(cores,))
    draws = In(
        steps, sample.ROW_WORDS, dtype=np.int32, obj_shape=(sample.ROW_WORDS,), depth=1
    )
    tokens = InOut(steps, dtype=np.int32, obj_shape=(1,), depth=1)
    token = Out(1, dtype=np.int32, obj_shape=(1,), depth=1)
    # Element offsets of this position's draw row and record.
    row = per_call(derive=lambda op: 0)
    at = per_call(derive=lambda op: 0)

    @property
    def slice_size(self) -> int:
        return slices(self.vocab, self.cores, self.k_max)[0]

    def validate(self) -> None:
        if self.vocab % 2:
            raise ValueError(
                f"Sample: vocab ({self.vocab}) must be even: the logits move in 4-byte words"
            )

    def resolve(self, dev):
        self.check_shim_columns(dev, self.cores)
        tm = get_target_model(dev.resolve())
        row = next(r for r in range(tm.rows()) if tm.is_mem_tile(0, r))
        joined = tm.get_num_dest_switchbox_connections(0, row, WireBundle.DMA)
        if self.cores > joined:
            raise Unresolvable(
                f"Sample's {self.cores} summaries join in one memtile, which "
                f"takes {joined}"
            )
        chunk = self.chunk or _largest_chunk(self.slice_size, self.slice_size // 2)
        return self.replace(chunk=chunk)

    def compatible(self) -> None:
        # The factories' own checks: chunk divides the slice, k_max fits.
        config = self.layout()
        for run in config.runs:
            config.select(*run)
        config.combine()

    @property
    def runs(self) -> list[tuple[int, int]]:
        """Each select core's `(logits, chunk)`: the last reads what is left."""
        size, last = slices(self.vocab, self.cores, self.k_max)
        tail = self.chunk if last == size else _largest_chunk(last, last // 2)
        return [(size, self.chunk)] * (self.cores - 1) + [(last, tail)]

    def select(self, run: int, chunk: int):
        return sample.sample_select(slice_size=run, chunk=chunk, k_max=self.k_max)

    def combine(self):
        return sample.sample_combine(
            columns=self.cores, slice_size=self.slice_size, k_max=self.k_max
        )

    def build(self) -> Built:
        runs, combine = self.runs, self.combine()
        selects = {run: self.select(*run) for run in set(runs)}
        words = sample.summary_words(self.slice_size, self.k_max)
        # Every core reads the draw row.
        of_draw = ObjectFifo(self.draws.obj_type, depth=self.draws.depth)
        self.draws.bind(of_draw.prod())
        of_token = ObjectFifo(self.token.obj_type, depth=self.token.depth)
        self.token.bind(of_token.cons())
        of_record = ObjectFifo(self.tokens.obj_type, depth=self.tokens.depth)
        self.tokens.bind(of_record.cons())
        # The summaries meet in a memtile, column 0 first; combine reads a
        # shorter last one's ties no further than its count.
        of_summaries = ObjectFifo(
            np.ndarray[(self.cores * words,), np.dtype[np.int32]],
            depth=1,
        )
        of_summary = of_summaries.prod().join(
            [words * c for c in range(self.cores)],
            obj_types=[
                np.ndarray[(sample.summary_words(run, self.k_max),), np.dtype[np.int32]]
                for run, _ in runs
            ],
            depths=[1] * self.cores,
        )

        def select_body(of_x, of_row, of_sum, kernel, state, calls):
            row = of_row.acquire(1)
            summary = of_sum.acquire(1)
            for _ in range_(calls):
                x = of_x.acquire(1)
                kernel(x, row, state, summary)
                of_x.release(1)
            of_sum.release(1)
            of_row.release(1)

        def combine_body(of_sums, of_row, of_tok, of_rec, kernel):
            summaries = of_sums.acquire(1)
            row = of_row.acquire(1)
            token = of_tok.acquire(1)
            record = of_rec.acquire(1)
            kernel(summaries, row, token, record)
            of_sums.release(1)
            of_row.release(1)
            of_tok.release(1)
            of_rec.release(1)

        workers, logits = [], []
        for c, (run, chunk) in enumerate(runs):
            of_x = ObjectFifo(
                np.ndarray[(chunk,), np.dtype[self.logits.dtype]],
                depth=self.logits.depth,
            )
            logits.append(of_x.prod())
            state = Buffer(
                np.ndarray[(sample.SELECT_STATE_WORDS,), np.dtype[np.int32]],
                initial_value=np.zeros(sample.SELECT_STATE_WORDS, dtype=np.int32),
            )
            workers.append(
                Worker(
                    select_body,
                    [
                        of_x.cons(),
                        of_draw.cons(),
                        of_summary[c].prod(),
                        selects[run, chunk],
                        state,
                        sample.select_streams(run, chunk) * run // chunk,
                    ],
                )
            )
        self.logits.bind(logits)
        workers.append(
            Worker(
                combine_body,
                [
                    of_summaries.cons(),
                    of_draw.cons(),
                    of_token.prod(),
                    of_record.prod(),
                    combine,
                ],
            )
        )
        return Built(workers)

    def sequence(self, rt):
        """One group: the draw and the logits in, then the record and the token."""
        row = self.row if self.row.per_call else None
        at = self.at if self.at.per_call else None
        tg = TaskGroup()
        self.draws.fill(self.draws[0], group=tg, offset_parameter=row)
        for c, (run, chunk) in enumerate(self.layout().runs):
            # Core c's slice, once per select stream.
            streams = sample.select_streams(run, chunk)
            start = c * self.slice_size
            piece = TensorAccessPattern.full((self.vocab,))[start : start + run]
            halves = self.logits.split(run)
            tap = halves and piece.split(0, halves[1]).repeat(streams)
            taps = [tap] if tap and self.logits.fits(tap) else [piece] * streams
            for tap in taps:
                self.logits.fill(tap, lane=c, group=tg)
        self.tokens.drain(self.tokens[:1], group=tg, wait=True, offset_parameter=at)
        self.token.drain(group=tg, wait=True)
        tg.finish()

    def ops(self) -> int:
        return 0  # a draw, not arithmetic: its figure is latency

    def reference(self, logits, draws, tokens, *, row=0, at=0):
        """``(tokens, token)``: the draw at ``draws`` row ``row // 4``, recorded at ``at``."""
        token = reference(
            logits,
            np.asarray(draws).reshape(-1)[row : row + sample.ROW_WORDS],
            self.k_max,
        )
        tokens = np.array(tokens, dtype=np.int32).reshape(-1)
        tokens[at] = token
        return tokens, np.array([token], dtype=np.int32)

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()
