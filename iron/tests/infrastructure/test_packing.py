# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A profile's packing on the device: a graph whose designs share one
device configuration computes what it does with each design configured
apart, bit for bit, and its reference.
"""

import re

import numpy as np
import pytest
from aie.utils.verify import Tolerance, compare
from ml_dtypes import bfloat16

import iron
from iron import Profile
from iron.operators.elementwise_mul import ElementwiseMul
from iron.operators.gemv import GEMV
from iron.operators.silu import SiLU


class Projection(iron.Graph):
    """``ElementwiseMul(SiLU(W @ x), up)``: three designs, a decode MLP's."""

    def body(self, w, x, up):
        y = GEMV.step(w, x)
        gate = SiLU.step(y, tile_size=256)
        return ElementwiseMul.step(gate, up, tile_size=256)


@pytest.mark.supported_devices("npu2")
def test_a_packed_graph_matches_its_designs_apart():
    packing = Profile()
    packing.add_packing(
        [
            (GEMV, {}, {"num_aie_columns": 2, "num_channels": 2}),
            (SiLU, {}, {"num_aie_columns": 1}),
            (ElementwiseMul, {}, {"num_aie_columns": 1}),
        ]
    )
    packed_graph = Projection()
    packed_graph.profile = packing
    shapes = dict(w=(2048, 2048), x=(2048,), up=(2048,))
    packed = packed_graph.compile(**shapes)
    composition = packed.sequence.packaging.composition
    devices = re.findall(r"^  aie\.device\(\w+\) @(\w+) \{$", composition.text(), re.M)
    assert len(devices) == 1, f"the three designs took {devices}"
    apart = Projection().compile(**shapes)

    rng = np.random.default_rng(0)
    w = (rng.standard_normal((2048, 2048)) / 32).astype(bfloat16)
    x = rng.standard_normal(2048).astype(bfloat16)
    up = rng.standard_normal(2048).astype(bfloat16)
    out = np.asarray(packed(w, x, up))
    assert np.array_equal(
        out.view(np.uint16), np.asarray(apart(w, x, up)).view(np.uint16)
    ), "packed and apart differ"
    verdict = compare(
        out,
        np.asarray(packed_graph.reference(w, x, up)),
        Tolerance.bf16_ulps(
            4,
            atol=1e-6,
            note="GEMV's float32 sum rounded once, SiLU's 1 ulp through the "
            "multiply, and each rounding",
        ),
    )
    assert verdict, verdict.detail
