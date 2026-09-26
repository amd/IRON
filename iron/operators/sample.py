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

The logits are split over ``cores`` columns. Each column's core streams its
slice three times through ``sample_select`` (a histogram pass, a refining
pass, a collecting pass) into a summary of its top k; the summaries join in
a memtile into one ``sample_combine`` core, which draws the token.

In a graph, the position is two per-call values: ``row`` is the element
offset of its draw (``4 * position``) and ``at`` the element offset of its
record (``position``)::

    tokens, token = sample(logits, draws, tokens, row=position * 4, at=position)
"""

import numpy as np
from ml_dtypes import bfloat16

from aie.iron import Buffer, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.iron.kernels import sample as kernels
from aie.utils.verify import Tolerance

from iron.common.declare import (
    In,
    InOut,
    Operator,
    Out,
    Overlay,
    Scratchpad,
    StreamIn,
    StreamOut,
    dim,
    operator,
    tunable,
)
from iron.common.testing import Case, Testing
from iron.common.tiling import contiguous, repeated

# A select core's logits object: no more than this, and even (4-byte DMA).
_CHUNK_LIMIT = 8192
# The select kernel's passes over its slice.
_PASSES = 3


@operator
class SampleOverlay(Overlay):
    """``cores`` select cores, one slice each, and one combine core."""

    vocab: int = dim()
    k_max: int = dim(64)
    cores: int = tunable(4)
    # Logits per select call; the largest even divisor of the slice up to
    # 8192 unless given.
    chunk: int | None = tunable(None)

    logits = StreamIn(chunk, per=cores, depth=2)
    draw = StreamIn(kernels.ROW_WORDS, dtype=np.int32, depth=1)
    token = StreamOut(1, dtype=np.int32, depth=1)
    record = StreamOut(1, dtype=np.int32, depth=1)

    @property
    def slice_size(self) -> int:
        return self.vocab // self.cores

    def validate(self) -> None:
        if self.vocab % self.cores:
            raise ValueError(
                f"vocab ({self.vocab}) must split evenly over {self.cores} cores"
            )
        if self.chunk is None:
            self.chunk = max(
                c
                for c in range(2, min(self.slice_size, _CHUNK_LIMIT) + 1, 2)
                if self.slice_size % c == 0
            )
        # The factories check the rest: chunk divides the slice, k_max fits.
        self._select()
        self._combine()

    def _select(self):
        return kernels.sample_select(
            slice_size=self.slice_size, chunk=self.chunk, k_max=self.k_max
        )

    def _combine(self):
        return kernels.sample_combine(
            columns=self.cores, slice_size=self.slice_size, k_max=self.k_max
        )

    def design(self, target) -> list:
        select, combine = self._select(), self._combine()
        words = kernels.summary_words(self.slice_size, self.k_max)
        calls = _PASSES * self.slice_size // self.chunk
        of_draw = ObjectFifo(self.draw.tile, name="draw", depth=1)
        of_token = ObjectFifo(self.token.tile, name="token", depth=1)
        of_record = ObjectFifo(self.record.tile, name="record", depth=1)
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
            self.logits[c].bind(of_x.prod())
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
        self.draw.bind(of_draw.prod())
        self.token.bind(of_token.cons())
        self.record.bind(of_record.cons())
        return workers


def _logits(op: "Sample") -> dict:
    """Logits with a few ties at the top, and one draw row per position."""
    rng = np.random.default_rng(11)
    logits = rng.normal(0, 3, op.ov.vocab).astype(bfloat16)
    logits[rng.choice(op.ov.vocab, 8, replace=False)] = logits.max()
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


@operator
class Sample(Operator[SampleOverlay]):
    """Draw the next token from a row of logits (exact temperature/top-k)."""

    # A token id; anything but exact is wrong.
    test = Testing(
        [
            Case(dict(vocab=4096, cores=4, steps=3), id="small"),
            Case(dict(vocab=4096, cores=2, chunk=256), id="two_cores"),
            Case(dict(vocab=128256, cores=4), id="llama"),
        ],
        tolerance=Tolerance.exact(),
        draw=_logits,
    )

    steps: int = dim(1)
    logits = In(SampleOverlay.vocab, to=SampleOverlay.logits)
    draws = In(steps, kernels.ROW_WORDS, dtype=np.int32, to=SampleOverlay.draw)
    tokens = InOut(steps, dtype=np.int32, from_=SampleOverlay.record)
    token = Out(1, dtype=np.int32, from_=SampleOverlay.token)
    # Element offsets of this position's draw row and record.
    row = Scratchpad(np.int32)
    at = Scratchpad(np.int32)

    def uses_value(self, name: str) -> bool:
        # A position is patched only when a graph binds a handle to it.
        return name in self.used_values

    def reference(self, logits, draws, tokens, *, row=0, at=0):
        """``(tokens, token)``: the draw at ``draws`` row ``row // 4``, recorded at ``at``."""
        token = reference(logits, np.asarray(draws).reshape(-1)[row : row + 4])
        tokens = np.array(tokens, dtype=np.int32).reshape(-1)
        tokens[at] = token
        return tokens, np.array([token], dtype=np.int32)

    def design(self, rt):
        ov = self.ov
        row = self.row if self.uses_value("row") else None
        at = self.at if self.uses_value("at") else None
        with rt.group() as tg:
            rt.fill(
                ov.draw,
                (self.draws, contiguous(self.draws.elements, 0, kernels.ROW_WORDS)),
                group=tg,
                offset_by=row,
            )
            for c in range(ov.cores):
                slice_ = repeated(
                    self.logits.elements,
                    c * ov.slice_size,
                    ov.slice_size,
                    [(_PASSES, 0)],
                    bfloat16,
                )
                rt.fill(ov.logits[c], (self.logits, slice_), group=tg)
            rt.drain(
                ov.record,
                (self.tokens, contiguous(self.tokens.elements, 0, 1)),
                group=tg,
                wait=True,
                offset_by=at,
            )
            rt.drain(ov.token, (self.token, contiguous(1, 0, 1)), group=tg, wait=True)


# --------------------------------------------------------------------------
# The CPU reference this operator is checked against.
# --------------------------------------------------------------------------


def reference(logits, draw_row) -> int:
    """The token the device draws from ``logits`` for one four-word draw row."""
    row = np.asarray(draw_row, dtype=np.int32).view(np.uint32)
    temperature = row[0:1].view(np.float32)[0]
    n53 = int(row[2]) | int(row[3]) << 32
    return kernels.sample_ref(logits, temperature, int(row[1]), n53)
