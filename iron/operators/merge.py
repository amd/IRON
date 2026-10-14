# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.iron import ExternalFunction, ObjectFifo, Worker
from aie.iron.controlflow import range_
from aie.utils.verify import Tolerance

from iron.common import In, Operator, Out, Value, Param
from iron.common.testing import Case, Testing

# EmbeddingGemma 2's placeholder ids, the towers' rows past 2048 text rows.
GEMMA = dict(audio_token=258881, image_token=258880, audio_at=2048, vision_at=2560)

MERGE = """
#include <stdint.h>

namespace {
int audio, image;
}

extern "C" void merge_rows(int32_t *ids, int32_t *merge, int32_t b) {
    if (b == 0)
        audio = image = 0;
    for (int r = 0, i = b * BLOCK; r < BLOCK; r++, i++) {
        int id = ids[r];
        merge[r] = id == AUDIO_TOKEN   ? AUDIO_AT + audio++
                   : id == IMAGE_TOKEN ? VISION_AT + image++
                                       : i;
    }
}
"""


class Merge(Operator):
    """The row each position of a sequence of token `ids` takes from a table
    of the text's embeddings followed by two towers' soft tokens.

    A position holds its own row, except that the j-th `audio_token` takes
    row `audio_at + j` and the j-th `image_token` row `vision_at + j`. That
    the placeholders are as many as the soft tokens is the caller's check.
    One core reads `block` ids at a time, its counts running over the blocks.
    """

    test = Testing(
        [
            Case(dict(rows=2048, **GEMMA), bench=True),
            Case(dict(rows=192, block=32, **GEMMA)),
            # The two runs of rows overlapping each other and the text's.
            Case(
                dict(rows=128, audio_token=0, image_token=1, audio_at=0, vision_at=40)
            ),
        ],
        # A third placeholders, scattered: each id's rank is its own.
        draw=lambda op: dict(
            given={
                op.ids: np.where(
                    np.random.default_rng(42).random(op.rows) < 1 / 3,
                    np.random.default_rng(43).choice(
                        [op.audio_token, op.image_token], op.rows
                    ),
                    np.random.default_rng(44).integers(0, 2**20, op.rows),
                ).astype(np.int32)
            }
        ),
    )

    rows: int = Param()
    audio_token: int = Param(array=True)
    image_token: int = Param(array=True)
    audio_at: int = Param(array=True)
    vision_at: int = Param(array=True)
    block: int = Param(default=64, array=True)

    ids = In(rows, dtype=np.int32, obj_type=(block,))
    merge = Out(rows, dtype=np.int32, obj_type=(block,))

    count = Value(derive=lambda op: op.rows // op.block)

    def compatible(self) -> None:
        if self.rows % self.block:
            raise ValueError(
                f"Merge: rows ({self.rows}) are not whole {self.block}-row blocks"
            )

    def ops(self) -> int:
        return 0  # index arithmetic: its figure is latency

    def reference(self, ids):
        merge = np.arange(ids.size, dtype=np.int32)
        for token, at in (
            (self.audio_token, self.audio_at),
            (self.image_token, self.vision_at),
        ):
            places = np.flatnonzero(ids == token)
            merge[places] = at + np.arange(places.size)
        return merge

    def tolerance(self) -> Tolerance:
        return Tolerance.exact()

    def array(self) -> list:
        kernel = ExternalFunction(
            "merge_rows",
            source_string=MERGE,
            arg_types=[self.ids.obj_type, self.merge.obj_type, np.int32],
            compile_flags=[
                f"-DAUDIO_TOKEN={self.audio_token}",
                f"-DIMAGE_TOKEN={self.image_token}",
                f"-DAUDIO_AT={self.audio_at}",
                f"-DVISION_AT={self.vision_at}",
                f"-DBLOCK={self.block}",
            ],
            symbol_prefix=(
                f"merge_{self.audio_token}_{self.image_token}_{self.audio_at}_"
                f"{self.vision_at}_{self.block}"
            ),
        )
        of_ids = ObjectFifo(self.ids.obj_type, depth=2)
        of_merge = ObjectFifo(self.merge.obj_type, depth=2)
        (rtp,) = self.rtp([self.count])

        def core_fn(of_in, of_out, kernel_fn, rtp):
            n = rtp.read()[self.count]
            for b in range_(n):
                kernel_fn(of_in.acquire(1), of_out.acquire(1), b)
                of_in.release(1)
                of_out.release(1)

        worker = Worker(core_fn, [of_ids.cons(), of_merge.prod(), kernel, rtp])
        self.ids.bind(of_ids.prod())
        self.merge.bind(of_merge.cons())
        return [worker]
