# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing on the NPU: a graph's designs measured into a fresh cost
table, the graph compiled through ``Graph.compile`` with the tuner, and the
tuned image run against the untuned one, bit for bit. The model and the
search are checked without a device (``iron/tests/toolchain/narrowing.py``).
"""

import re

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common.graph.narrowing import CostTable, JointNarrowing, cost_key, variants
from iron.common.graph.probe import Timing, calibrate, measure_steps
from iron.common.image import Fusion
from iron.operators import ElementwiseAdd, ElementwiseMul, SiLU

SIZE = 8192
TILE = 256

pytestmark = pytest.mark.usefixtures("npu_runtime")


class Chain(iron.Graph):
    """add, silu, mul, add, silu, each at the full array's width."""

    def __init__(self):
        super().__init__()
        wide = dict(size=SIZE, tile_size=TILE)
        self.add = ElementwiseAdd(**wide)
        self.silu = SiLU(**wide)
        self.mul = ElementwiseMul(**wide)

    def body(self, a, b):
        x = self.mul(self.silu(self.add(a, b)), b)
        return self.silu(self.add(x, b))


@pytest.mark.supported_devices("npu2")
def test_tuned_graph_is_bit_identical_and_packed(tmp_path):
    table = CostTable(tmp_path / "costs.json")
    traced = Chain().trace(a=(SIZE,), b=(SIZE,))
    first = {}
    for s in traced.steps:
        first.setdefault(cost_key(s.op), s.op)
    timing = Timing(rounds=2, calls=10)
    dev = aie_utils.ensure_current_device()
    for op in first.values():
        costs = measure_steps(table, variants(op, dev), timing)
        assert all(c.exact for c in costs.values())
    add, silu = (variants(op, dev)[-1].op for op in list(first.values())[:2])
    calibrate(table, add, silu, timing)

    tuned = Chain().compile(
        image=iron.ELF,
        coresident=JointNarrowing(table, fit_cache=tmp_path / "fits"),
        a=(SIZE,),
        b=(SIZE,),
    )
    plain = Chain().compile(image=iron.ELF, a=(SIZE,), b=(SIZE,))
    assert tuned.tuning is not None and plain.tuning is None
    assert [len(g) for g in tuned.tuning.groups] == [3]
    text = Fusion(tuned.sequence).text()
    assert len(re.findall(r"aiex\.configure", text)) == tuned.tuning.configures == 2

    rng = np.random.default_rng(0)
    a = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    b = (rng.random(SIZE) * 4 - 2).astype(bfloat16)
    want = np.array(plain(a, b).numpy()[:SIZE])
    got = np.array(tuned(a, b).numpy()[:SIZE])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()
