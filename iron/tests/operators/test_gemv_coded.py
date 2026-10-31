# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""GEMV streaming its weight as coded rows returns plain GEMV's bits, on a device.

Each core decodes a coded tile into the rows plain A gives and runs the
same matvec on them, so at equal tunables the two outputs are one bit
pattern; a tolerance would hide a decode that lost a bit. Real Llama 3.2
1B weights (skipped where absent) carry the exponent spread coding is
built for; drawn rows carry the most exceptions a row holds. A graph whose
weight holds a row past its capacity reads it plain and still matches.
"""

import aie.utils as aie_utils
import numpy as np
import pytest
from aie.utils.verify import Tolerance
from ml_dtypes import bfloat16

import iron
from iron.lm import Checkpoint
from iron.lm.testing import require, weights_dir
from iron.operators.gemv import GEMV

pytestmark = pytest.mark.supported_devices("npu2")

LLAMA = weights_dir("llama3.2-1b") / "model.safetensors"

# (weight, rows, tunables): Llama 3.2 1B's decode GEMVs at its npu2 profile's
# tunables, B on its own stream where a coded tile is too short to carry it.
SHAPES = {
    "gate_proj": (
        "model.layers.0.mlp.gate_proj.weight",
        None,
        dict(tile_size_input=4, tile_size_output=1024),
    ),
    "down_proj": (
        "model.layers.0.mlp.down_proj.weight",
        None,
        dict(tile_size_input=1, tile_size_output=256, feed_b=True),
    ),
    "lm_head": (
        "model.embed_tokens.weight",
        8192,
        dict(tile_size_input=4, tile_size_output=1024),
    ),
}


def _drawn(M: int, K: int) -> np.ndarray:
    """Rows of normal draws, each holding 15 entries far outside its windows."""
    rng = np.random.default_rng(M + K)
    w = rng.standard_normal((M, K)).astype(np.float32)
    w = np.copysign(np.maximum(np.abs(w), np.float32(2**-8)), w)
    for row in w:
        row[rng.choice(K, 15, replace=False)] *= np.exp2(60.0)
    return w.astype(bfloat16)


def _run(op: GEMV, w: np.ndarray, x: np.ndarray) -> np.ndarray:
    tensor = aie_utils.DEFAULT_TENSOR_CLASS
    a, b, c = op.buffers
    buffers = [
        tensor(a.device_form(w)),
        tensor(x),
        tensor(c.host_shape, dtype=c.host_dtype),
    ]
    op(*buffers)
    return buffers[-1].numpy().copy()


@pytest.mark.parametrize("source", ["drawn", *SHAPES])
def test_a_coded_gemv_returns_the_plain_bits(source):
    if source == "drawn":
        w, tunables = _drawn(2048, 2048), dict(tile_size_input=4, tile_size_output=256)
    else:
        require(LLAMA)
        name, rows, tunables = SHAPES[source]
        w = np.asarray(Checkpoint(LLAMA).tensors[name][:rows])
    M, K = w.shape
    x = np.random.default_rng(K).standard_normal(K).astype(bfloat16)
    shape = dict(M=M, K=K, num_aie_columns=8, **tunables)
    plain = _run(GEMV(**shape), w, x)
    coded = _run(GEMV(**shape, coded_a=True), w, x)
    np.testing.assert_array_equal(coded.view(np.uint16), plain.view(np.uint16))
    tolerance = Tolerance.relative(0.04, 1e-3)
    (verdict,) = GEMV(**shape).judge({"A": w, "B": x}, {"C": coded}, tolerance).values()
    assert verdict, verdict.detail


class _Twice(iron.Graph):
    def __init__(self, w, coded_a):
        self.w = iron.param(w)
        self.coded_a = coded_a

    def body(self, x):
        y = GEMV.step(self.w, x, coded_a=self.coded_a, tile_size_input=4)
        return GEMV.step(self.w, y, coded_a=self.coded_a, tile_size_input=4)


@pytest.mark.parametrize("overflow", [False, True], ids=["coded", "past-capacity"])
def test_a_graph_reading_a_weight_coded_returns_the_plain_bits(overflow):
    w = (np.random.default_rng(0).standard_normal((2048, 2048)) * 0.05).astype(bfloat16)
    if overflow:
        w[5, :120] = np.exp2(np.arange(-60.0, 60.0)).astype(bfloat16)
    x = np.random.default_rng(1).standard_normal(2048).astype(bfloat16)
    out = {}
    for coded_a in (False, True):
        graph = _Twice(w, coded_a)
        version = graph.compile(x=(2048,))
        names = sorted(h.name for _, h in version.recording.weights.values())
        assert names == (["w.coded"] if coded_a and not overflow else ["w"])
        out[coded_a] = np.asarray(graph(x).numpy()).copy()
    np.testing.assert_array_equal(out[True].view(np.uint16), out[False].view(np.uint16))
