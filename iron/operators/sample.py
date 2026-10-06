# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sample: the next token, drawn on the device from a row of bf16 logits.

Temperature and top-k sampling as ``aie.iron.kernels.sample.sample_ref``
specifies it, bit for bit, so a device draw and a host draw of the same
logits and the same uniform agree exactly. A draw is a four-word row of
``draws`` (temperature, top-k, and the 53-bit uniform, see
``aie.iron.kernels.sample.draw_row``) written by the host ahead of time, one
per position; the token is written to ``token`` (what the next step embeds)
and recorded at its position in ``tokens``.

The logits are split over ``cores`` columns. Each column's core passes its
slice twice through ``sample_select`` (a threshold pass, a collecting pass)
into a summary of its top k -- streamed twice, or once when a chunk is the
whole slice; the summaries join in a memtile into one ``sample_combine``
core, which draws the token.

In a graph, the position is two per-call values: ``row`` is the element
offset of its draw (``4 * position``) and ``at`` the element offset of its
record (``position``):

```python
tokens, token = Sample(logits, draws, tokens, row=position * 4, at=position)
```
"""

import dataclasses

import numpy as np
from aie.helpers.taplib import TensorAccessPattern
from aie.iron import Buffer, ObjectFifo, TaskGroup, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import sample as kernels
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

from iron.common import In, InOut, Operator, Out, Scratchpad, auto, param
from iron.common.design import BdLimits
from iron.common.testing import Case, Testing

# A select core's logits object: no more than this, and even (4-byte DMA).
_CHUNK_LIMIT = 8192


def reference(logits, draw_row, k_max: int | None = None) -> int:
    """The token the device draws from ``logits`` for one four-word draw row.

    The kernels take a top-k below 1 as 1 and one above ``k_max`` as
    ``k_max``: a row of zeros, a buffer the host never wrote, is greedy.
    """
    words = np.asarray(draw_row, dtype=np.int32)
    row = words.view(np.uint32)
    temperature = row[0:1].view(np.float32)[0]
    n53 = int(row[2]) | int(row[3]) << 32
    top_k = max(int(words[1]), 1)
    return kernels.sample_ref(logits, temperature, top_k, n53, k_max=k_max)


def _logits(op: "Sample") -> dict:
    """Logits with a few ties at the top, and one draw row per position."""
    rng = np.random.default_rng(11)
    logits = rng.normal(0, 3, op.vocab).astype(bfloat16)
    logits[rng.choice(op.vocab, 8, replace=False)] = logits.max()
    draws = np.stack(
        [
            kernels.draw_row(t, k, int(rng.integers(0, 1 << 53)))
            for t, k in zip(
                rng.choice([0.0, 0.7, 1.0], op.steps), rng.integers(1, 51, op.steps)
            )
        ]
    )
    return dict(
        logits=logits,
        draws=draws,
        tokens=np.full(op.steps, -1, dtype=np.int32),
    )


class Sample(Operator):
    """Draw the next token from a row of logits (exact temperature/top-k).

    ``cores`` select cores, one slice of the row each, and one combine core.
    """

    # A token id; anything but exact is wrong.
    test = Testing(
        [
            Case(dict(vocab=4096, cores=4, steps=3), id="small"),
            Case(dict(vocab=4096, cores=2, chunk=256), id="two_cores"),
            Case(dict(vocab=128256, cores=4), id="llama", bench=True),
        ],
        tolerance=Tolerance.exact(),
        draw=_logits,
    )

    # The array reads both: the slice each core takes, the summary's size.
    vocab: int = param(array=True)
    k_max: int = param(default=64, array=True)
    # Positions the draws and the record hold; the sequence picks one.
    steps: int = param(default=1)
    cores: int = auto(4)
    # Logits per select call; the largest even divisor of the slice up to
    # 8192 unless given.
    chunk: int = auto()

    logits = In(vocab, tile=(chunk,), per=(cores,), depth=2)
    draws = In(
        steps, kernels.ROW_WORDS, dtype=np.int32, tile=(kernels.ROW_WORDS,), depth=1
    )
    tokens = InOut(steps, dtype=np.int32, tile=(1,), depth=1)
    token = Out(1, dtype=np.int32, tile=(1,), depth=1)
    # Element offsets of this position's draw row and record.
    row = Scratchpad(np.int32)
    at = Scratchpad(np.int32)

    @property
    def slice_size(self) -> int:
        return self.vocab // self.cores

    @property
    def select_streams(self) -> int:
        """How often each select core takes its slice per position."""
        return kernels.select_streams(self.slice_size, self.chunk)

    def validate(self) -> None:
        if self.vocab % self.cores:
            raise ValueError(
                f"vocab ({self.vocab}) must split evenly over {self.cores} cores"
            )

    def resolve(self, dev):
        self.check_shim_columns(dev, self.cores)
        chunk = self.chunk or max(
            c
            for c in range(2, min(self.slice_size, _CHUNK_LIMIT) + 1, 2)
            if self.slice_size % c == 0
        )
        return dataclasses.replace(self, chunk=chunk)

    def compatible(self) -> None:
        # The factories' own checks: chunk divides the slice, k_max fits.
        try:
            self._select()
            self._combine()
        except ValueError as e:
            raise ValueError(str(e)) from e

    def _select(self):
        return kernels.sample_select(
            slice_size=self.slice_size, chunk=self.chunk, k_max=self.k_max
        )

    def _combine(self):
        return kernels.sample_combine(
            columns=self.cores, slice_size=self.slice_size, k_max=self.k_max
        )

    def uses_value(self, name: str) -> bool:
        # A position is patched only when a graph binds a handle to it.
        return name in self.bound_values

    def array(self, target) -> list:
        select, combine = self._select(), self._combine()
        words = kernels.summary_words(self.slice_size, self.k_max)
        calls = self.select_streams * self.slice_size // self.chunk
        # Every core reads the draw row: the select cores their top-k, the
        # combine core the rest.
        of_draw = ObjectFifo(self.draws.tile, name="draw", depth=1)
        self.draws.bind(of_draw.prod())
        of_token = ObjectFifo(self.token.tile, name="token", depth=1)
        self.token.bind(of_token.cons())
        of_record = ObjectFifo(self.tokens.tile, name="record", depth=1)
        self.tokens.bind(of_record.cons())
        # The summaries meet in a memtile, column 0 first.
        of_summaries = ObjectFifo(
            np.ndarray[(self.cores * words,), np.dtype[np.int32]],
            name="summaries",
            depth=1,
        )
        of_summary = of_summaries.prod().join(
            [words * c for c in range(self.cores)],
            obj_types=[np.ndarray[(words,), np.dtype[np.int32]]] * self.cores,
            names=[f"summary_{c}" for c in range(self.cores)],
            depths=[1] * self.cores,
        )

        def select_body(of_x, of_row, of_sum, kernel, state):
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

        workers = []
        for c in range(self.cores):
            of_x = ObjectFifo(self.logits.tile, name=f"logits_{c}", depth=2)
            self.logits.lane(c).bind(of_x.prod())
            state = Buffer(
                np.ndarray[(kernels.SELECT_STATE_WORDS,), np.dtype[np.int32]],
                initial_value=np.zeros(kernels.SELECT_STATE_WORDS, dtype=np.int32),
                name=f"select_state_{c}",
            )
            workers.append(
                Worker(
                    select_body,
                    [of_x.cons(), of_draw.cons(), of_summary[c].prod(), select, state],
                )
            )
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
                stack_size=combine.contract.stack_bytes,
            )
        )
        return workers

    def _slice_taps(self, core: int) -> list[TensorAccessPattern]:
        """Core ``core``'s slice, once per select stream: one descriptor that
        re-reads it (stride 0 in the iteration slot) where the run factors
        into one, else one per stream.
        """
        run, streams = self.slice_size, self.select_streams
        piece = TensorAccessPattern.full((self.vocab,))[core * run : (core + 1) * run]
        shim = BdLimits.of(self.dev, 0, 0)
        halves = shim.factor(run, shim.granule(bfloat16))
        if halves is not None:
            tap = piece.split(0, halves[1]).repeat(streams)
            if shim.fits(tap, bfloat16):
                return [tap]
        return [piece] * streams

    def sequence(self, rt):
        """One group: the draw and the logits in, then the record and the token."""
        row = self.row if self.uses_value("row") else None
        at = self.at if self.uses_value("at") else None
        tg = TaskGroup()
        rt.fill(
            self.draws.lane(),
            TensorAccessPattern.full(self.draws.shape)[0],
            group=tg,
            offset_by=row,
        )
        for c in range(self.cores):
            for tap in self._slice_taps(c):
                rt.fill(self.logits.lane(c), tap, group=tg)
        rt.drain(
            self.tokens.lane(),
            TensorAccessPattern.full(self.tokens.shape)[:1],
            group=tg,
            wait=True,
            offset_by=at,
        )
        rt.drain(self.token.lane(), self.token, group=tg, wait=True)
        tg.finish()

    def ops(self) -> int:
        return 0  # a draw, not arithmetic: its figure is latency

    def reference(self, logits, draws, tokens, *, row=0, at=0):
        """``(tokens, token)``: the draw at ``draws`` row ``row // 4``, recorded at ``at``."""
        token = reference(
            logits,
            np.asarray(draws).reshape(-1)[row : row + kernels.ROW_WORDS],
            self.k_max,
        )
        tokens = np.array(tokens, dtype=np.int32).reshape(-1)
        tokens[at] = token
        return tokens, np.array([token], dtype=np.int32)
