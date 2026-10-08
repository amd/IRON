# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Joint narrowing on the NPU: a graph's designs measured into a fresh cost
table, the graph compiled through ``Graph.compile`` with the tuner, and the
tuned image run against the untuned one, bit for bit. The model and the
search are checked without a device (``iron/tests/toolchain/narrowing.py``).
"""

import dataclasses
import math
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
from iron.common.graph.costcache import Accuracy, CostCache, Measurement
from iron.common.graph.fold import replaced
from iron.common.graph.narrowing import (
    CostTable,
    JointNarrowing,
    Variant,
    cost_key,
    fitting,
    variants,
)
from iron.common.graph.probe import (
    CONTEXTS,
    Call,
    Timing,
    calibrate,
    check_model,
    measure_graph,
    measure_steps,
    platform,
    search,
)
from iron.common.image import Fusion
from iron.lm.layers import SwiGLU
from iron.operators import (
    GEMM,
    GEMV,
    MHA,
    Copy,
    ElementwiseAdd,
    ElementwiseMul,
    SiLU,
    Softmax,
)

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


class Gather(iron.Graph):
    """Row `pos` of `rows`, gathered and added to `x`."""

    def body(self, x, rows, *, pos: Scratchpad[np.int32]):
        return ElementwiseAdd(x, Copy(rows[pos]), tile_size=TILE)


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
        table = CostTable(tmp_path / f"costs{n}.json", "npu2", "fused")
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
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
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
        CostTable(tmp_path / "costs.json", "npu2", "fused"),
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
        CostTable(tmp_path / "costs.json", "npu2", "fused"),
        found,
        Timing(rounds=1, calls=5),
        values={"length": 200, "valid_cols": 200},
    )
    assert len(costs) == len(found) and all(c.exact for c in costs.values())


@pytest.mark.supported_devices("npu2")
def test_a_setting_far_behind_the_fastest_is_timed_no_further(tmp_path):
    # GEMV at one column is several times its widest's step.
    found = variants(GEMV(M=2048, K=2048), aie_utils.ensure_current_device())
    timing = Timing(rounds=4, calls=10, settle=1)
    cut = CostTable(tmp_path / "cut.json", "npu2", "fused")
    measure_steps(cut, found, timing)
    full = CostTable(tmp_path / "full.json", "npu2", "fused")
    measure_steps(full, found, dataclasses.replace(timing, cutoff=math.inf))
    assert all(full.steps[v.key].rounds == timing.rounds for v in found)
    stopped = {v.key for v in found if cut.steps[v.key].rounds < timing.rounds}
    assert stopped and found[0].key not in stopped
    # Timed in full, what was stopped is still well behind the fastest.
    best = min(full.steps[v.key].t_step_us for v in found)
    assert all(full.steps[key].t_step_us > 1.2 * best for key in stopped)


@pytest.mark.supported_devices("npu2")
def test_a_batch_whose_every_setting_is_stopped_is_measured(tmp_path):
    # At cutoff 0 all but the default stop after settling; a later batch has no default.
    op = Masked().trace(x=(256, 256)).steps[0].op
    found = variants(op, aie_utils.ensure_current_device())
    assert len(found) > CONTEXTS // 2
    timing = Timing(rounds=2, calls=5, settle=1, cutoff=0.0)
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
    measure_steps(table, found, timing, values={"length": 200, "valid_cols": 200})
    rounds = [table.steps[v.key].rounds for v in found]
    assert rounds == [timing.rounds] + [timing.settle] * (len(found) - 1)


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
        CostTable(tmp_path / "costs.json", "npu2", "fused"),
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
def test_a_setting_that_does_not_build_is_left_out(tmp_path):
    # 128x128 B tiles double-buffered beside A and C are past a core's memory.
    dev = aie_utils.ensure_current_device()
    gemm = GEMM(M=2048, K=2048, N=2048)
    found = [
        Variant.of(gemm, dev),
        Variant.of(gemm.with_tunables(tile_k=128, tile_n=128), dev),
    ]
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
    logged = []
    costs = search(
        table,
        found,
        Timing(rounds=1, calls=5),
        exhaustive=1,
        fit_cache=tmp_path / "fits",
        log=logged.append,
    )
    assert costs.keys() == table.steps.keys() == {found[0].key}
    assert len(logged) == 1 and "does not build" in logged[0], logged
    # The build's verdict is kept, not the placer's.
    kept, refused = fitting(found, tmp_path / "fits")
    assert kept == found[:1]
    assert refused[found[1].key].startswith("[aiecc] Compilation failed")


@pytest.mark.supported_devices("npu2")
def test_tuned_graph_is_bit_identical_and_packed(tmp_path):
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
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
def test_the_model_predicts_the_tuned_graph_and_the_graph_as_traced(tmp_path):
    # Strix Halo at 8 rounds of 50: tuned within -6.8% to +2.6%; as traced
    # the model held 618-634 us while runs measured 626-738 us.
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
    shapes = dict(a=(SIZE,), b=(SIZE,))
    timing = Timing(rounds=8, calls=50)
    calls = Call.admitted(Chain().trace(**shapes), aie_utils.ensure_current_device())
    measure_graph(table, calls, [("ElementwiseAdd", "SiLU")], timing, cache=cache)

    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    tuned = Chain().compile(image=iron.ELF, coresident=tuner, **shapes)
    untuned = Chain().compile(image=iron.ELF, **shapes)
    rng = np.random.default_rng(0)
    tensors = [(rng.random(SIZE) * 4 - 2).astype(bfloat16) for _ in range(2)]
    check = check_model(tuned, untuned, tensors, timing=timing)
    # A failure's traceback would hold their contexts from the next test.
    del tuned, untuned
    assert check.predicted_us == pytest.approx(
        check.measured_us, rel=0.1
    ), check.report()
    assert check.baseline_us == pytest.approx(
        check.baseline_measured_us, rel=0.2
    ), check.report()


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
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
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
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
    measure_graph(table, calls, [], timing, cache=cache)

    gate, fused = replaced(traced, folds)[0]
    entry = cache.key(fused.resolved())
    raw = cache.get(entry, Measurement)
    near = cache.get(cache.beside_key(cache.key(gate.resolved()), entry), Measurement)
    paired = table.steps[cost_key(gate)].t_step_us + raw.t_step_us - near.t_step_us
    assert table.steps[cost_key(fused)].t_step_us == pytest.approx(paired)

    again = CostTable(tmp_path / "again.json", "npu2", "fused")
    assert measure_graph(again, calls, [], timing, cache=cache) == []
    assert again.steps == table.steps


@pytest.mark.supported_devices("npu2")
def test_an_inexact_width_within_its_gates_is_accurate_and_cached(tmp_path):
    # tile_k=16 rounds C's bf16 accumulator after every 16 of K, the default every 64.
    dev = aie_utils.ensure_current_device()
    default = GEMM(M=256, K=256, N=256)
    found = [Variant.of(op, dev) for op in (default, default.with_tunables(tile_k=16))]
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    timing = Timing(rounds=1, calls=5)
    table = CostTable(tmp_path / "costs.json", "npu2", "fused")
    measure_steps(table, found, timing, cache=cache)
    narrow = table.steps[found[1].key]
    assert not narrow.exact and narrow.accurate, narrow
    entries = [cache.key(v.resolved) for v in found]
    for entry in entries:
        assert cache.get(cache.judged_key(entries[0], entry), Accuracy).within

    stamps = {p: p.stat().st_mtime_ns for p in cache.directory.iterdir()}
    again = CostTable(tmp_path / "again.json", "npu2", "fused")
    assert measure_steps(again, found, timing, cache=cache) == {}
    assert again.steps == table.steps
    assert {p: p.stat().st_mtime_ns for p in cache.directory.iterdir()} == stamps


@pytest.mark.supported_devices("npu2")
def test_a_graph_sharing_measured_designs_measures_nothing(tmp_path):
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "costs")
    pairs = [("ElementwiseAdd", "SiLU")]
    timing = Timing(rounds=1, calls=5)
    chain = CostTable(tmp_path / "chain.json", "npu2", "fused")
    shapes = dict(a=(SIZE,), b=(SIZE,))
    ran = measure_graph(
        chain, [Call(Chain().trace(**shapes))], pairs, timing, cache=cache
    )
    assert len(ran) == len(chain.steps) + 1
    assert len(list(cache.directory.iterdir())) == len(ran)

    table = CostTable(tmp_path / "add_silu.json", "npu2", "fused")
    ran = measure_graph(
        table, [Call(AddSilu().trace(**shapes))], pairs, timing, cache=cache
    )
    assert ran == []
    assert table.steps and table.steps.items() <= chain.steps.items()
    assert table.calibrations == chain.calibrations


@pytest.mark.supported_devices("npu2")
def test_an_xclbin_chain_is_measured_and_tuned_by_its_own_model(tmp_path):
    # Strix Halo: a 1-column add loads in ~84 us, an 8-column one in ~626 us.
    report = platform()
    cache = CostCache(report["Name"], report["Power Mode"], root=tmp_path / "c")
    table = CostTable(tmp_path / "costs.json", "npu2", "separate")
    shapes = dict(a=(SIZE,), b=(SIZE,))
    timing = Timing(rounds=4, calls=20)
    triangle = [
        ("ElementwiseAdd", "ElementwiseMul"),
        ("ElementwiseAdd", "SiLU"),
        ("SiLU", "ElementwiseMul"),
    ]
    traced = Chain().trace(**shapes)
    dev = aie_utils.ensure_current_device()
    measure_graph(table, [Call(traced)], triangle, timing, cache=cache)

    assert len(table.calibrations) == 3
    assert all(
        c.reset_us == c.base_us == 0 and c.switch_us > 0
        for c in table.calibrations.values()
    )
    [(reference, _), *_] = [k.split("|") for k in table.calibrations]
    solved = {k for pair in table.calibrations for k in pair.split("|")}
    loaded = [k for k in table.steps if k not in solved]
    assert loaded and all(table.steps[k].beside == reference for k in loaded)
    add = variants(traced.steps[0].op, dev)
    narrow, wide = (min(add, key=lambda v: v.mm2s), max(add, key=lambda v: v.mm2s))
    assert table.load(wide.key) > 2 * table.load(narrow.key) > 0
    again = CostTable(tmp_path / "again.json", "npu2", "separate")
    assert measure_graph(again, [Call(traced)], triangle, timing, cache=cache) == []
    assert again.steps == table.steps

    tuner = JointNarrowing(table, fit_cache=tmp_path / "fits")
    tuned = Chain().compile(boundaries=iron.each_step, coresident=tuner, **shapes)
    untuned = Chain().compile(boundaries=iron.each_step, **shapes)
    assert tuned.tuning.groups == () and tuned.tuning.configures == 5
    rng = np.random.default_rng(0)
    tensors = [(rng.random(SIZE) * 4 - 2).astype(bfloat16) for _ in range(2)]
    want = np.array(untuned(*tensors).numpy()[:SIZE])
    got = np.array(tuned(*tensors).numpy()[:SIZE])
    check = check_model(tuned, untuned, tensors, timing=timing)
    del tuned, untuned
    assert want.view(np.uint16).tolist() == got.view(np.uint16).tolist()
    # Each dispatch's host cost is bimodal by ~12% over minutes; the gain is not.
    assert check.baseline_us - check.predicted_us == pytest.approx(
        check.baseline_measured_us - check.measured_us, rel=0.1
    ), check.report()


@pytest.mark.supported_devices("npu2")
def test_an_xclbin_chain_measures_a_design_its_call_gives_values(tmp_path):
    # An xclbin has no parameter table: its per-call values are dispatch-time.
    shapes = dict(x=(2048,), rows=(16, 2048))
    traced = Gather().trace(**shapes)
    table = CostTable(tmp_path / "costs.json", "npu2", "separate")
    measure_graph(table, [Call(traced, dict(pos=5))], [], Timing(rounds=2, calls=10))
    keys = {cost_key(s.op) for s in traced.steps}
    assert keys <= table.steps.keys()
    assert all(c.exact for c in table.steps.values())

    version = Gather().compile(boundaries=iron.each_step, **shapes)
    rng = np.random.default_rng(0)
    x = (rng.random(2048) * 4 - 2).astype(bfloat16)
    rows = (rng.random((16, 2048)) * 4 - 2).astype(bfloat16)
    for pos in (5, 11):
        got = np.array(version(x, rows, pos=pos).numpy()[:2048])
        want = (x.astype(np.float32) + rows[pos].astype(np.float32)).astype(bfloat16)
        assert got.view(np.uint16).tolist() == want.view(np.uint16).tolist(), pos
    del version
