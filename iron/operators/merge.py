# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction, In, Out, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance
from aie.utils.compile.jit.params import param, per_call

from iron.common import Built, Operator, Rtp
from iron.common.testing import Case, Testing

# EmbeddingGemma 2's placeholders, (id, row), the towers' rows past 2048 text rows.
GEMMA = ((258881, 2048), (258880, 2560))

MERGE = """
#include <stdint.h>

namespace {
const int32_t tokens[PLACEHOLDERS] = TOKENS;
const int32_t at[PLACEHOLDERS] = AT;
int32_t seen[PLACEHOLDERS];
}

#ifdef OFFSET
extern "C" void merge_rows(int32_t *ids, int32_t *before, int32_t *merge, int32_t b) {
#else
extern "C" void merge_rows(int32_t *ids, int32_t *merge, int32_t b) {
#endif
    if (b == 0)
        for (int k = 0; k < PLACEHOLDERS; k++)
#ifdef OFFSET
            seen[k] = before[k];
#else
            seen[k] = 0;
#endif
    for (int r = 0, i = b * BLOCK; r < BLOCK; r++, i++) {
        int32_t id = ids[r], row = i;
        for (int k = 0; k < PLACEHOLDERS; k++)
            if (id == tokens[k]) {
                row = at[k] + seen[k]++;
                break;
            }
        merge[r] = row;
    }
}
"""


class Merge(Operator):
    """The row each position of `ids` takes from the text's embeddings and
    the towers' soft tokens: for each placeholder `(token, at)`, the j-th
    `token` takes row `at + j`; any other id its own position.

    Given `before`, the count of each placeholder before these ids (a
    prompt chunk after others), the j-th takes row `at + before + j`.
    """

    test = Testing(
        [
            Case(dict(rows=2048, placeholders=GEMMA), bench=True),
            Case(dict(rows=192, block=32, placeholders=GEMMA)),
            # One tower's placeholders.
            Case(dict(rows=192, placeholders=((49190, 64),))),
            # The runs of rows overlapping each other and the text's.
            Case(dict(rows=128, placeholders=((0, 0), (1, 40), (2, 20)))),
            # A prompt chunk after others: each count starts where they left it.
            Case(dict(rows=2048, placeholders=GEMMA, offset=True)),
            Case(dict(rows=128, placeholders=((0, 0), (1, 40), (2, 20)), offset=True)),
        ],
        # A third placeholders, scattered: each id's rank is its own; the
        # counts before them as many as a chunk holds.
        draw=lambda op: dict(
            given={
                op.ids: np.where(
                    np.random.default_rng(42).random(op.rows) < 1 / 3,
                    np.random.default_rng(43).choice(
                        [t for t, _ in op.placeholders], op.rows
                    ),
                    np.random.default_rng(44).integers(0, 2**20, op.rows),
                ).astype(np.int32),
                **(
                    {
                        op.before: np.random.default_rng(45)
                        .integers(0, op.rows, op.kinds)
                        .astype(np.int32)
                    }
                    if op.offset
                    else {}
                ),
            }
        ),
    )

    rows: int = param()
    # Each placeholder's (token id, first row of its soft tokens).
    placeholders: tuple[tuple[int, int], ...] = param(array=True)
    block: int = param(default=64)
    offset: bool = param(default=False)
    kinds: int = param(derive=lambda op: len(op.placeholders), repr=False)

    ids = In(rows, dtype=np.int32, obj_shape=(block,))
    before = In(kinds, dtype=np.int32, obj_shape=(kinds,), depth=1, when=offset)
    merge = Out(rows, dtype=np.int32, obj_shape=(block,))

    count = per_call(derive=lambda op: op.rows // op.block)

    def validate(self) -> None:
        tokens = [t for t, _ in self.placeholders]
        if not tokens or len(set(tokens)) != len(tokens):
            raise ValueError(
                f"Merge: placeholders {self.placeholders} are not one or more "
                f"distinct tokens"
            )

    def compatible(self) -> None:
        if self.rows % self.block:
            raise ValueError(
                f"Merge: rows ({self.rows}) are not whole {self.block}-row blocks"
            )

    def ops(self) -> int:
        return 0  # index arithmetic: its figure is latency

    def reference(self, ids, before=None):
        merge = np.arange(ids.size, dtype=np.int32)
        starts = np.zeros(self.kinds, np.int32) if before is None else before
        for (token, at), start in zip(self.placeholders, starts):
            places = np.flatnonzero(ids == token)
            merge[places] = at + start + np.arange(places.size)
        return merge

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def build(self) -> Built:
        tokens, at = zip(*self.placeholders)
        counted = [self.before.obj_type] if self.offset else []
        kernel = ExternalFunction(
            "merge_rows",
            source_string=MERGE,
            arg_types=[self.ids.obj_type, *counted, self.merge.obj_type, np.int32],
            compile_flags=[
                f"-DPLACEHOLDERS={len(tokens)}",
                f"-DTOKENS={{{','.join(map(str, tokens))}}}",
                f"-DAT={{{','.join(map(str, at))}}}",
                f"-DBLOCK={self.block}",
                *(["-DOFFSET"] if self.offset else []),
            ],
            symbol_prefix=(
                f"merge_{'_'.join(map(str, tokens))}_at_"
                f"{'_'.join(map(str, at))}_{self.block}"
                + ("_offset" if self.offset else "")
            ),
        )
        (ids_end,) = self.ids.fifos(self.ids.depth)
        (merge_end,) = self.merge.fifos(self.merge.depth)
        before_end = self.before.fifos(self.before.depth)[0] if self.offset else None
        rtp = Rtp([self.count])

        def core_fn(of_in, of_out, kernel_fn, rtp, of_before):
            n = rtp.read()[self.count]
            before = None if of_before is None else of_before.acquire(1)
            for b in range_(n):
                counts = [] if before is None else [before]
                kernel_fn(of_in.acquire(1), *counts, of_out.acquire(1), b)
                of_in.release(1)
                of_out.release(1)
            if of_before is not None:
                of_before.release(1)

        worker = Worker(
            core_fn,
            [ids_end, merge_end, kernel, rtp, before_end],
        )
        return Built([worker], [rtp])
