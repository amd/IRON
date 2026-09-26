#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Sample on adversarial logits, on a device.

sample_select keeps a candidate buffer behind a threshold (cut to the top k
by quickselect when it fills) in its first pass, and in its second emits the
keys above tau in index order and the ties at tau as bitmap bits, 32 lanes
at a time with a scalar tail when a chunk is not a multiple of 32, shifting
the bitmap words when a chunk does not start on a 32-element boundary. The
declared cases draw random logits; this drives the orders and ties those
paths branch on: sorted rows (a cut nearly every vector), all-equal rows
(every key a tie), -0 and +0 at the top (one key), rows of -inf with fewer
finite logits than k, ties straddling words, chunks and columns, the max
once or tied with tau (the argmax from the entries or the bitmap), exactly
k distinct top values.

Each design is compiled once and every pattern is drawn through it with
every draw row (temperature 0, 0.7, 1.0 by top-k 1, 17, 64, and the extreme
uniforms), one position per row. Every token must be sample_ref's; every
mismatch is collected, so a failure lists all of them.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import from_name
from aie.iron.kernels.sample import draw_row

import iron
from iron.common.declare import Scratchpad
from iron.operators.sample import Sample, reference

K_MAX = 64

# (temperature, top_k, n53) per position.
ROWS = [(t, k, None) for t in (0.0, 0.7, 1.0) for k in (1, 17, K_MAX)]
ROWS += [(1.0, K_MAX, (1 << 53) - 1), (0.7, 17, 0), (1.0, 17, 1 << 52)]

DESIGNS = [
    # chunk == slice (1024): one call makes both passes.
    pytest.param(dict(vocab=4096, cores=4), id="resident"),
    pytest.param(dict(vocab=4096, cores=2, chunk=256), id="streamed"),
    # chunk == slice (2000): resident, with a 16-logit scalar tail.
    pytest.param(dict(vocab=4000, cores=2), id="resident_tail"),
    # 40 logits per call: one vector and an 8-logit tail, and every call but
    # every fourth starts off a 32-element word.
    pytest.param(dict(vocab=4000, cores=2, chunk=40), id="streamed_unaligned"),
    # A slice of exactly k_max: every key is a candidate.
    pytest.param(dict(vocab=128, cores=2), id="slice_is_k_max"),
    # chunk 8016 (four per slice, 8016 % 32 == 16).
    pytest.param(dict(vocab=128256, cores=4), id="llama"),
]

KINDS = [
    "random",
    "ascending",
    "descending",
    "sawtooth",
    "all equal",
    "signed zeros",
    "zeros on top",
    "mostly -inf",
    "fewer finite than k",
    "ties straddling below the max",
    "ties straddling at the max",
    "max once over ties",
    "max tied across columns",
    "k distinct top values",
    "k distinct top values in one column",
    "k-th tied past k",
    "few distinct values",
    "subnormals",
]


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _boundaries(vocab: int, slice_size: int, chunk: int) -> np.ndarray:
    """Indices either side of 32-element words, chunks, columns and the end."""
    edges = [32, 64, chunk, 2 * chunk, slice_size, slice_size + chunk, vocab - 32]
    near = [e + d for e in edges for d in (-1, 0, 1)] + [0, vocab - 1]
    return np.unique([i for i in near if 0 <= i < vocab])


def _logits(kind: str, vocab: int, slice_size: int, chunk: int, rng) -> np.ndarray:
    x = rng.normal(0, 3, vocab).astype(np.float32)
    if kind == "ascending":
        x = np.sort(x)
    elif kind == "descending":
        x = np.sort(x)[::-1].copy()
    elif kind == "sawtooth":
        # Ascending across vectors, descending within each.
        x = np.sort(x)
        whole = vocab - vocab % 32
        x[:whole] = x[:whole].reshape(-1, 32)[:, ::-1].reshape(-1)
    elif kind == "all equal":
        x[:] = 1.5
    elif kind == "signed zeros":
        x = np.where(rng.random(vocab) < 0.5, np.float32(-0.0), np.float32(0.0))
    elif kind == "zeros on top":
        # -0 first, then both signs, in every column: one key.
        x = -np.abs(x) - 0.5
        at = np.unique(np.concatenate([_boundaries(vocab, slice_size, chunk), [5]]))
        x[at] = np.where(np.arange(at.size) % 2, np.float32(0.0), np.float32(-0.0))
    elif kind == "mostly -inf":
        x[rng.random(vocab) < 0.95] = -np.inf
    elif kind == "fewer finite than k":
        # Column 0 and the last logit only; tau is -inf for top-k 17 and 64.
        finite = [1, 33, min(slice_size - 1, 60), vocab - 1]
        keep = x[finite]
        x[:] = -np.inf
        x[finite] = keep
    elif kind == "ties straddling below the max":
        x = np.clip(rng.normal(0, 1, vocab), -4, 4).astype(np.float32)
        x[_boundaries(vocab, slice_size, chunk)] = 8.0
        x[rng.choice(vocab, 3, replace=False)] = [9.0, 9.5, 10.0]
    elif kind == "ties straddling at the max":
        x = np.clip(rng.normal(0, 1, vocab), -4, 4).astype(np.float32)
        x[_boundaries(vocab, slice_size, chunk)] = 8.0
    elif kind == "max once over ties":
        x = np.clip(x, -10, 9)
        x[rng.choice(vocab, min(100, vocab // 2), replace=False)] = 10.0
        x[vocab - 3] = 20.0
    elif kind == "max tied across columns":
        x = np.clip(x, -10, 9)
        x[[31, 32, slice_size - 1, slice_size, vocab - 1]] = 20.0
    elif kind == "k distinct top values":
        x = np.clip(rng.normal(0, 1, vocab), -4, 4).astype(np.float32)
        x[rng.choice(vocab, K_MAX, replace=False)] = 10 + 0.125 * np.arange(K_MAX)
    elif kind == "k distinct top values in one column":
        x = np.clip(rng.normal(0, 1, vocab), -4, 4).astype(np.float32)
        last = vocab - slice_size
        at = last + rng.choice(slice_size, K_MAX, replace=False)
        x[at] = 10 + 0.125 * rng.permutation(K_MAX)
    elif kind == "k-th tied past k":
        # 63 distinct values above five copies of the 64th.
        x = np.clip(rng.normal(0, 1, vocab), -4, 4).astype(np.float32)
        at = rng.choice(vocab, K_MAX + 4, replace=False)
        x[at[: K_MAX - 1]] = 10.125 + 0.125 * np.arange(K_MAX - 1)
        x[at[K_MAX - 1 :]] = 10.0
    elif kind == "few distinct values":
        x = rng.integers(0, 4, vocab).astype(np.float32)
    elif kind == "subnormals":
        tiny = np.float32(2.0**-130)
        x = (rng.integers(-64, 65, vocab) * tiny).astype(np.float32)
    else:
        assert kind == "random", kind
    return x.astype(bfloat16)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("kwargs", DESIGNS)
def test_adversarial_logits_draw_the_reference_token(npu_runtime, kwargs):
    steps = len(ROWS)
    rng = np.random.default_rng(kwargs["vocab"] + kwargs.get("chunk", 0))
    draws = iron.state((steps, 4), np.int32, name="draws")
    tokens = iron.state((steps,), np.int32, name="tokens")
    sample = Sample(**kwargs, k_max=K_MAX, steps=steps)
    sample.use_value("row")
    sample.use_value("at")
    ov = sample.ov
    vocab, slice_size, chunk = ov.vocab, ov.slice_size, ov.chunk

    @iron.graph
    def step(logits, *, position: Scratchpad[np.int32]):
        _, token = sample(logits, draws, tokens, row=position * 4, at=position)
        return token

    net = step.compile(logits=((vocab,), bfloat16))
    rows = np.stack(
        [
            draw_row(t, k, int(rng.integers(0, 1 << 53)) if n53 is None else n53)
            for t, k, n53 in ROWS
        ]
    )
    net.write(draws, rows)

    failures = []
    for kind in KINDS:
        logits = _logits(kind, vocab, slice_size, chunk, rng)
        for position, (t, k, _) in enumerate(ROWS):
            want = reference(logits, rows[position])
            got = int(np.asarray(step(logits, position=position)).reshape(-1)[0])
            if got != want:
                n53 = int(rows[position, 2].view(np.uint32))
                n53 |= int(rows[position, 3].view(np.uint32)) << 32
                failures.append(
                    f"{kind}: T={t} top_k={k} n53={n53}: device {got}, "
                    f"reference {want}"
                )
    assert not failures, (
        f"{len(failures)} of {len(KINDS) * steps} draws differ "
        f"(slice {slice_size}, chunk {chunk}):\n" + "\n".join(failures)
    )
