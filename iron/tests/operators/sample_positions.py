#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sample across positions of one compiled graph, on a device.

Decode samples every position through one graph: the draw row and the
record slot are per-call values, and the select cores' state carries from
one position to the next. The declared cases run position 0 of a fresh
design only, so this drives several positions with a different row each
(greedy, top-1, top-50, top-64, two temperatures) and a logit row chosen to
stress the combine (ties across columns, the max in several columns, all
equal). Every token must be sample_ref's, and every record in its slot.
"""

import numpy as np
import pytest
from aie.iron.kernels.sample import draw_row
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.operators.sample import Sample, reference

# (temperature, top_k) per position; greedy twice, so a greedy row between
# sampled ones leaves nothing behind.
ROWS = [(0.7, 50), (0.0, 50), (1.0, 64), (0.7, 1), (0.0, 1), (1.3, 50)]


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _logits(kind: str, vocab: int, cores: int, rng) -> np.ndarray:
    x = rng.normal(0, 3, vocab).astype(np.float32)
    slice_size = vocab // cores
    if kind == "ties across columns":
        x[rng.choice(vocab, 200, replace=False)] = 12.0
        x[rng.choice(vocab, 10, replace=False)] = 14.0
    elif kind == "max in several columns":
        x[[0, slice_size, vocab - 1]] = 20.0
    elif kind == "column boundary":
        x[[slice_size - 1, slice_size]] = 30.0
    elif kind == "all equal":
        x[:] = 1.5
    return x.astype(bfloat16)


KINDS = ["random", "ties across columns", "max in several columns"]
KINDS += ["column boundary", "all equal", "random"]


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("vocab,cores", [(4096, 4), (128256, 4)], ids=["4k", "llama"])
def test_every_position_draws_and_records_its_token(npu_runtime, vocab, cores):
    steps = len(ROWS)
    rng = np.random.default_rng(vocab)
    draws = iron.state((steps, 4), np.int32, name="draws")
    tokens = iron.state((steps,), np.int32, name="tokens")

    class Step(iron.Graph):
        def body(self, logits, *, position: Scratchpad[np.int32]):
            _, token = Sample(
                logits, draws, tokens, cores=cores, row=position * 4, at=position
            )
            return token

    net = Step().compile(logits=(vocab,))

    rows = np.stack([draw_row(t, k, int(rng.integers(0, 1 << 53))) for t, k in ROWS])
    net.write(draws, rows)
    net.write(tokens, np.full(steps, -1, dtype=np.int32))
    want = []
    for position, kind in enumerate(KINDS):
        logits = _logits(kind, vocab, cores, rng)
        want.append(reference(logits, rows[position]))
        got = int(np.asarray(net(logits, position=position)).reshape(-1)[0])
        assert got == want[-1], f"position {position} ({kind}, {ROWS[position]})"
    recorded = np.asarray(net.read(tokens)).reshape(-1)
    assert recorded.tolist() == want
