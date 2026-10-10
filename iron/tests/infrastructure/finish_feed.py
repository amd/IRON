# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A finish's input riding its producer's feed, on the NPU.

A GEMV's lanes take both of its cores' input channels for A, with B
riding it, so the residual a folded add takes rides A too: each tile of it
follows the rows of A that make the output tile it is added to. A folded graph is judged
against numpy and, bit for bit, against the graph run unfolded.
"""

import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.harness import run_test, vectors
from iron.lm.layers import SwiGLU
from iron.operators import GEMV, ElementwiseAdd, ElementwiseMul, SiLU

pytestmark = pytest.mark.usefixtures("npu_runtime")


class Residual(iron.Graph):
    def __init__(self, w):
        self.w = w

    def body(self, x, r):
        return ElementwiseAdd(GEMV(self.w, x, num_aie_columns=8), r)


@pytest.mark.supported_devices("npu2")
@pytest.mark.parametrize("M,K", [(2048, 2048), (2048, 8192), (512, 2048)])
def test_a_residual_rides_the_matrix_into_a_folded_matvec(M, K):
    rng = np.random.default_rng(0)
    w = (rng.standard_normal((M, K)) / np.sqrt(K)).astype(bfloat16)
    x = rng.standard_normal((1, K)).astype(bfloat16)
    r = rng.standard_normal((1, M)).astype(bfloat16)

    folded = Residual(w).compile(image=iron.ELF, fold=True, x=(1, K), r=(1, M))
    (step,) = folded.traced.steps
    assert [b.name for b in step.op.inputs] == ["A", "B", "finish0_b"]
    assert not any(b.streamed for b in step.op.finish_inputs)
    plain = Residual(w).compile(image=iron.ELF, x=(1, K), r=(1, M))
    assert len(plain.traced.steps) == 2

    got = np.array(folded(x, r).numpy()[:M])
    want = (w.astype(np.float32) @ x.astype(np.float32).reshape(-1)).astype(bfloat16)
    want = (want.astype(np.float32) + r.astype(np.float32).reshape(-1)).astype(bfloat16)
    (out,) = (b.name for b in step.op.outputs)
    (verdict,) = step.op.judge(
        {b.name: t for b, t in zip(step.op.inputs, (w, x, r))},
        {out: got},
        step.op.gate(),
        {out: want},
    ).values()
    assert verdict, verdict.detail
    unfolded = np.array(plain(x, r).numpy()[:M])
    assert got.view(np.uint16).tolist() == unfolded.view(np.uint16).tolist()


@pytest.mark.supported_devices("npu2")
def test_each_batch_of_a_matvec_takes_its_own_residual():
    op = GEMV(M=256, K=128, num_batches=2).fold(ElementwiseAdd(size=2 * 256), 0)
    run = run_test(op, vectors(op), tolerance=op.gate())
    assert not run.errors, run.errors


@pytest.mark.supported_devices("npu2")
def test_the_up_projection_rides_the_gate_into_its_product():
    E, H = 2048, 8192
    rng = np.random.default_rng(0)
    shapes = [(H, E), (H, E), (E, H)]
    weights = [
        (rng.standard_normal(s) / np.sqrt(s[1])).astype(bfloat16) for s in shapes
    ]
    x = rng.standard_normal((1, E)).astype(bfloat16)

    folded = SwiGLU(*weights).compile(image=iron.ELF, fold=True, x=(1, E))
    up, gate, down = folded.traced.steps
    assert [type(link.op) for link in gate.op.finish] == [SiLU, ElementwiseMul]
    plain = SwiGLU(*weights).compile(image=iron.ELF, x=(1, E))

    got = np.array(folded(x).numpy()[:E])
    op = gate.op.resolved()
    held = {b.name: folded.read(h) for b, h in zip(op.buffers, gate.slots)}
    (verdict,) = op.judge(
        {b.name: held[b.name] for b in op.inputs},
        {b.name: held[b.name] for b in op.outputs},
        op.tolerance(),
    ).values()
    assert verdict, verdict.detail
    unfolded = np.array(plain(x).numpy()[:E])
    assert got.view(np.uint16).tolist() == unfolded.view(np.uint16).tolist()
