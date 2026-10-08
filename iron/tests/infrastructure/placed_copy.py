#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A copy into a state folded into its producer's drain, on a device.

Folded, the producer writes the state's slot itself, its drain moved by
the copy's per-call offset, and the copy is gone. Each run checks the
whole state, so a drain that lands in the wrong slot, or past it, cannot
pass.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.harness import verify_buffer
from iron.operators.copy import Copy
from iron.operators.elementwise_add import ElementwiseAdd
from iron.operators.gemv import GEMV

ROWS, K, SLOTS = 512, 2048, 8
IMAGES = {
    "elf": {"image": iron.ELF},
    "xclbin": {"image": iron.XCLBIN, "boundaries": iron.each_step},
}


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


class _Sum(iron.Graph):
    def __init__(self):
        self.cache = iron.state((SLOTS, ROWS))

    def body(self, a, b, *, pos: Scratchpad[np.int32]):
        Copy(ElementwiseAdd(a, b), self.cache[pos])


class _Projection(iron.Graph):
    def __init__(self, w):
        self.w = w
        self.cache = iron.state((SLOTS, ROWS))

    def body(self, x, *, pos: Scratchpad[np.int32]):
        Copy(GEMV(self.w, x), self.cache[pos])


def _compiled(graph, fold, image, **shapes):
    net = graph.compile(fold=fold, **IMAGES[image], **shapes)
    assert net.plan.image == image
    return net


def _cache(net, graph):
    return np.asarray(net.read(graph.cache), dtype=np.float32).reshape(SLOTS, ROWS)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("image", IMAGES)
def test_a_sum_written_into_a_state_lands_in_its_slot(image, npu_runtime):
    graph = _Sum()
    net = _compiled(graph, True, image, a=(ROWS,), b=(ROWS,))
    assert [type(s.op) for s in net.traced.steps] == [ElementwiseAdd]

    rng = np.random.default_rng(0)
    expected = rng.standard_normal((SLOTS, ROWS)).astype(bfloat16).astype(np.float32)
    net.write(graph.cache, expected)
    for slot in (0, 5, SLOTS - 1, 2):
        a, b = (rng.standard_normal(ROWS).astype(bfloat16) for _ in range(2))
        total = a.astype(np.float32) + b.astype(np.float32)
        expected[slot] = total.astype(bfloat16).astype(np.float32)
        net(a, b, pos=slot)
        wrong = np.argwhere(_cache(net, graph) != expected)
        assert wrong.size == 0, f"{slot=}: {len(wrong)} differ, first {wrong[:4]}"


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("image", IMAGES)
def test_a_projection_written_into_a_state_is_the_one_copied(image, npu_runtime):
    rng = np.random.default_rng(1)
    w = (rng.standard_normal((ROWS, K)) / np.sqrt(K)).astype(bfloat16)
    graphs = {fold: _Projection(w) for fold in (True, False)}
    nets = {fold: _compiled(g, fold, image, x=(K,)) for fold, g in graphs.items()}
    assert [type(s.op) for s in nets[True].traced.steps] == [GEMV]
    assert [type(s.op) for s in nets[False].traced.steps] == [GEMV, Copy]
    gemv = nets[True].traced.steps[0].op
    tolerance = gemv.resolved().tolerance()

    expected = rng.standard_normal((SLOTS, ROWS)).astype(bfloat16).astype(np.float32)
    for fold, net in nets.items():
        net.write(graphs[fold].cache, expected)
    for slot in (3, 0, SLOTS - 1):
        x = rng.standard_normal(K).astype(bfloat16)
        got = {}
        for fold, net in nets.items():
            net(x, pos=slot)
            got[fold] = _cache(net, graphs[fold])
        verdict = verify_buffer(
            got[True][slot], "GEMV", gemv.reference(w, x), tolerance
        )
        assert verdict, verdict.detail
        expected[slot] = got[True][slot]
        wrong = np.argwhere(got[True] != expected)
        assert wrong.size == 0, f"{slot=}: {len(wrong)} differ, first {wrong[:4]}"
        assert np.array_equal(got[True], got[False]), f"{slot=}: not the row copied"
