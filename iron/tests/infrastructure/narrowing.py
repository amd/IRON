# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing on the NPU: a graph's designs measured into a fresh cost
table, the graph compiled through ``Graph.compile`` with the tuner, and the
tuned image run against the untuned one, bit for bit. The model and the
search are checked without a device (``iron/tests/toolchain/narrowing.py``).
"""

import os
import re
import subprocess
import sys

import aie.utils as aie_utils
import numpy as np
import pytest
from ml_dtypes import bfloat16

import iron
from iron.common import Scratchpad
from iron.common.graph.costcache import CostCache, Measurement
from iron.common.graph.fold import replaced
from iron.common.graph.narrowing import CostTable, JointNarrowing, cost_key, variants
from iron.common.graph.probe import (
    CONTEXTS,
    Call,
    Timing,
    calibrate,
    measure_graph,
    measure_steps,
    platform,
    search,
)
from iron.common.image import Fusion
from iron.lm.layers import SwiGLU
from iron.operators import GEMM, MHA, ElementwiseAdd, ElementwiseMul, SiLU, Softmax

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


class Project(iron.Graph):
    """The first `n` rows of `x` projected by `w`."""

    def body(self, x, w, *, n: Scratchpad[np.int32]):
        return GEMM(x[:n], w, b_col_maj=True)


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
def test_a_value_derived_from_a_tunable_is_measured_at_its_resolution(tmp_path):
    # GEMM's tile count reads its auto() tile shape as well as the row bound.
    # Its DMAs move every row under the bound, so its time does not follow it.
    traced = Project().trace(x=(2048, 2048), w=(2048, 2048))
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    table = CostTable(tmp_path / "costs.json")
    call = Call(traced, dict(n=256))
    measure_graph(table, [call], [], Timing(rounds=2, calls=10), cache=cache)
    [key] = {cost_key(s.op) for s in traced.steps}
    assert table.steps[key].t_step_us > 0, table.steps[key]


@pytest.mark.supported_devices("npu2")
def test_widths_are_compared_on_the_rows_under_the_bound(tmp_path):
    # GEMM drains every row; past the bound they hold what each width's L1 held.
    traced = Project().trace(x=(1024, 1024), w=(1024, 1024))
    [step] = traced.steps
    found = variants(step.op, aie_utils.ensure_current_device())
    assert len(found) > 1
    costs = measure_steps(
        CostTable(tmp_path / "costs.json"),
        found,
        Timing(rounds=1, calls=5),
        values=Call(traced, dict(n=256)).op_values(step.op),
    )
    assert all(c.exact for c in costs.values()), costs


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
def test_one_operator_is_measured_from_the_command_line(tmp_path):
    table = tmp_path / "costs.json"
    run = subprocess.run(
        [
            sys.executable,
            "-m",
            "iron.common.graph.tune",
            "ElementwiseAdd",
            f"size={SIZE}",
            f"tile_size={TILE}",
            "--rounds=1",
            "--calls=5",
            f"--table={table}",
        ],
        env=os.environ | {"NPU_CACHE_HOME": str(tmp_path / "cache")},
        capture_output=True,
        text=True,
    )
    assert run.returncode == 0, run.stderr
    found = variants(
        ElementwiseAdd(size=SIZE, tile_size=TILE), aie_utils.ensure_current_device()
    )
    assert CostTable(table).steps.keys() == {v.key for v in found}
    printed = [line for line in run.stdout.splitlines() if "t_step" in line]
    assert len(printed) == len(found)
    assert sum("(default)" in line for line in printed) == 1


@pytest.mark.supported_devices("npu2")
def test_descent_measures_every_line_through_the_default(tmp_path):
    found = variants(
        ElementwiseAdd(size=SIZE, tile_size=TILE), aie_utils.ensure_current_device()
    )
    default = dict(found[0].tunables)
    costs = search(
        CostTable(tmp_path / "costs.json"),
        found,
        Timing(rounds=1, calls=5),
        exhaustive=1,
    )
    lines = {
        v.key
        for v in found
        if sum(dict(v.tunables)[n] != x for n, x in default.items()) <= 1
    }
    assert lines <= costs.keys() <= {v.key for v in found}
    assert all(c.exact for c in costs.values()), costs


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
def test_a_fold_the_tuner_takes_runs_as_the_forced_fold_does(tmp_path):
    # Measured as traced and folded, the tuner decides; either way its
    # image is the untuned one folded alike, bit for bit.
    rng = np.random.default_rng(0)
    E = 2048
    weights = [
        (rng.standard_normal((E, E)) / np.sqrt(E)).astype(bfloat16) for _ in range(3)
    ]
    dev = aie_utils.ensure_current_device()
    traced = SwiGLU(*weights).trace(x=(1, E))
    calls = Call.admitted(traced, dev)
    folds = calls[1].traced
    report = platform()
    table = CostTable(tmp_path / "costs.json")
    measure_graph(
        table,
        calls,
        [("SiLU", "ElementwiseMul")],
        Timing(rounds=1, calls=5),
        cache=CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c"),
    )
    assert {cost_key(s.op) for s in traced.steps + folds.steps} <= table.steps.keys()

    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    tuned = SwiGLU(*weights).compile(image=iron.ELF, coresident=tuner, x=(1, E))
    fold = bool(tuned.tuning.folds)
    assert any(isinstance(s.op, SiLU) for s in tuned.traced.steps) != fold
    plain = SwiGLU(*weights).compile(image=iron.ELF, fold=fold, x=(1, E))
    x = rng.standard_normal((1, E)).astype(bfloat16)
    want = np.array(plain(x).numpy()[:E])
    got = np.array(tuned(x).numpy()[:E])
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()


@pytest.mark.supported_devices("npu2")
def test_a_folded_design_is_priced_beside_the_one_it_replaces(tmp_path):
    E = 2048
    weights = [np.zeros((E, E), bfloat16) for _ in range(3)]
    traced = SwiGLU(*weights).trace(x=(1, E))
    calls = Call.admitted(traced, aie_utils.ensure_current_device())
    folds = calls[1].traced
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    timing = Timing(rounds=1, calls=5)
    table = CostTable(tmp_path / "costs.json")
    measure_graph(table, calls, [], timing, cache=cache)

    gate, fused = replaced(traced, folds)[0]
    entry = cache.key(fused.resolved())
    raw = cache.get(entry, Measurement)
    near = cache.get(cache.beside_key(cache.key(gate.resolved()), entry), Measurement)
    paired = table.steps[cost_key(gate)].t_step_us + raw.t_step_us - near.t_step_us
    assert table.steps[cost_key(fused)].t_step_us == pytest.approx(paired)

    again = CostTable(tmp_path / "again.json")
    assert measure_graph(again, calls, [], timing, cache=cache) == []
    assert again.steps == table.steps


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
