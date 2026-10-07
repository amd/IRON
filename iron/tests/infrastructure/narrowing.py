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
from iron.common import Scratchpad
from iron.common.graph.costcache import CostCache
from iron.common.graph.narrowing import CostTable, JointNarrowing, cost_key, variants
from iron.common.graph.probe import (
    CONTEXTS,
    Call,
    Timing,
    calibrate,
    measure_graph,
    measure_steps,
    platform,
)
from iron.common.image import Fusion
from iron.operators import MHA, ElementwiseAdd, ElementwiseMul, SiLU, Softmax

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


class AddSilu(iron.Graph):
    """silu of a sum: two of `Chain`'s designs."""

    def body(self, a, b):
        return SiLU(ElementwiseAdd(a, b, tile_size=TILE), tile_size=TILE)


class Masked(iron.Graph):
    """A softmax over each row's first `n` entries, `n` given per call."""

    def body(self, x, *, n: Scratchpad[np.int32]):
        return Softmax(x[:, :n])


class Attend(iron.Graph):
    """One query's heads over the first `n` rows of a key and value cache."""

    def body(self, q, k, v, *, n: Scratchpad[np.int32]):
        return MHA(q, k[:n], v[:n], heads_interleaved=True, kv_interleaved=True)


@pytest.mark.supported_devices("npu2")
def test_a_value_derived_from_a_bound_extent_follows_the_call(tmp_path):
    # MHA's KV block count follows the context, which the call gives alone.
    traced = Attend().trace(q=(1, 32, 64), k=(2048, 8, 64), v=(2048, 8, 64))
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    t_step = {}
    for n in (64, 2048):
        table = CostTable(tmp_path / f"costs{n}.json")
        call = Call(traced, dict(n=n))
        measure_graph(table, [call], [], Timing(rounds=2, calls=10), cache=cache)
        [key] = {cost_key(s.op) for s in traced.steps}
        t_step[n] = table.steps[key].t_step_us
    assert t_step[2048] > 3 * t_step[64], t_step


@pytest.mark.supported_devices("npu2")
def test_measures_more_widths_than_one_batch_of_contexts(tmp_path):
    # A probe that writes a per-call value loads its context when it is built.
    op = Masked().trace(x=(256, 256)).steps[0].op
    found = variants(op, aie_utils.ensure_current_device())
    assert len(found) > CONTEXTS // 2
    costs = measure_steps(
        CostTable(tmp_path / "costs.json"),
        found,
        Timing(rounds=1, calls=5),
        values={"length": 200, "valid_cols": 200},
    )
    assert len(costs) == len(found) and all(c.exact for c in costs.values())


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


@pytest.mark.supported_devices("npu2")
def test_a_graph_sharing_measured_designs_measures_nothing(tmp_path):
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "costs")
    pairs = [("ElementwiseAdd", "SiLU")]
    timing = Timing(rounds=1, calls=5)
    chain = CostTable(tmp_path / "chain.json")
    shapes = dict(a=(SIZE,), b=(SIZE,))
    ran = measure_graph(
        chain, [Call(Chain().trace(**shapes))], pairs, timing, cache=cache
    )
    assert len(ran) == len(chain.steps) + 1
    assert len(list(cache.directory.iterdir())) == len(ran)

    table = CostTable(tmp_path / "add_silu.json")
    ran = measure_graph(
        table, [Call(AddSilu().trace(**shapes))], pairs, timing, cache=cache
    )
    assert ran == []
    assert table.steps and table.steps.items() <= chain.steps.items()
    assert table.calibrations == chain.calibrations
