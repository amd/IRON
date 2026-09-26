# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Folds on the NPU: a folded graph computes exactly what the unfolded one does.

One graph per kind of fold -- a repeat read by a batched GEMV in another
walk, a copy into a cache written by the projection before it at a
per-call offset, an elementwise step run on the producer's cores -- run
folded and unfolded, as a full ELF and as a chain of xclbins, and compared
bit for bit. iron/tests/common/fold.py checks the same folds without a
device.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import aie.utils as aie_utils
from aie.iron.device import NPU2

import iron
from iron.common.declare import Scratchpad
from iron.common.graph.fold import FoldAll, Kind
from iron.common.image.packaging import each_step
from iron.operators.gemv.op import GEMV
from iron.operators.repeat import Repeat
from iron.operators.silu import SiLU
from iron.operators.strided_copy import StridedCopy

G, REP, L, D, COLS = 2, 4, 256, 64, 2
H = G * REP


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(NPU2())
    yield
    aie_utils.set_current_device(previous)


def _rng():
    return np.random.default_rng(0)


def _scores():
    keys = iron.state((G, L * D), name="keys")
    start = _rng().standard_normal((G, L * D)).astype(bfloat16)

    def fn(q):
        k_all = Repeat(keys, repeat=REP, transfer_size=D)
        return GEMV(
            k_all.reshape(H, L, D),
            q,
            num_aie_columns=COLS,
            tile_size_input=4,
            tile_size_output=L // COLS,
        )

    q = _rng().standard_normal((H, D)).astype(bfloat16)
    return fn, dict(q=(H, D)), (q,), {}, (keys, start)


def _cache_write():
    cache = iron.state((G, L * D), name="cache")
    w = (_rng().standard_normal((G * D, 2 * D)) * 0.1).astype(bfloat16)

    def fn(x, *, pos: Scratchpad[np.int32]):
        v = GEMV(w, x, num_aie_columns=COLS, tile_size_output=D // 2)
        StridedCopy(
            v.reshape(G, D),
            cache,
            out_offset=pos * D,
            input_sizes=(G, D),
            input_strides=(D, 1),
            input_offset=0,
            output_sizes=(1, G, D),
            output_strides=(0, L * D, 1),
            output_offset=0,
        )
        return GEMV(w, x, num_aie_columns=COLS, tile_size_output=D // 2)

    x = _rng().standard_normal(2 * D).astype(bfloat16)
    start = _rng().standard_normal((G, L * D)).astype(bfloat16)
    return fn, dict(x=(2 * D,)), (x,), dict(pos=5), (cache, start)


def _epilogue():
    M, K = 2048, 512
    w = (_rng().standard_normal((M, K)) * 0.05).astype(bfloat16)

    def fn(x):
        h = GEMV(w, x, num_aie_columns=COLS, tile_size_output=M // COLS)
        return SiLU(h, num_aie_columns=COLS, tile_size=M // COLS)

    x = _rng().standard_normal(K).astype(bfloat16)
    return fn, dict(x=(K,)), (x,), {}, None


GRAPHS = {"repeat_read": _scores, "cache_write": _cache_write, "epilogue": _epilogue}
KINDS = {
    "repeat_read": Kind.READ,
    "cache_write": Kind.WRITE,
    "epilogue": Kind.EPILOGUE,
}


def _run(name, fold, boundaries):
    """The graph's output, and its state if it writes one, as raw bits."""
    fn, shapes, inputs, values, state = GRAPHS[name]()
    g = iron.graph(fn)
    version = g.compile(
        fold=FoldAll(kinds=(KINDS[name],)) if fold else None,
        boundaries=boundaries,
        **shapes,
    )
    folded = len(version.traced.steps) < len(g.trace(**shapes).steps)
    assert folded == fold, "the fold under test was not taken"
    version.load()
    if state is not None:
        version.write(state[0], state[1])
    out = np.array(g(*inputs, **values).numpy()).reshape(-1)
    bits = [out.view(np.uint16)]
    if state is not None:
        bits.append(np.array(version.read(state[0])).reshape(-1).view(np.uint16))
    return bits


@pytest.mark.parametrize("boundaries", [None, each_step], ids=["elf", "each_step"])
@pytest.mark.parametrize("name", sorted(GRAPHS))
def test_a_folded_graph_computes_what_the_unfolded_one_does(
    name, boundaries, npu_runtime
):
    unfolded = _run(name, False, boundaries)
    folded = _run(name, True, boundaries)
    for want, got in zip(unfolded, folded):
        assert np.array_equal(want, got)
