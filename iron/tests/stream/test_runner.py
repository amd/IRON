# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""How every stream-dse solve runs, and the cache that keeps each one."""

from types import SimpleNamespace

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from aie.iron.device import from_name  # noqa: E402
from aie.utils.compile.jit.operator import Unresolvable  # noqa: E402

from iron.common.stream import hardware, runner  # noqa: E402
from iron.operators.swiglu_prefill_stream import design  # noqa: E402

pytestmark = pytest.mark.usefixtures("npu2")


def test_the_compute_grid_is_the_devices(npu2):
    grid = hardware.ComputeArray.from_device(npu2)
    assert (grid.num_columns, grid.num_rows) == (8, 4)


def test_a_device_stream_does_not_describe_is_unresolvable():
    with pytest.raises(Unresolvable, match="npu1"):
        hardware.accelerator(from_name("npu1", n_cols=4))


def test_every_solve_builds_the_default_families_under_its_options(npu2):
    from stream.api import default_families

    options = runner.solve_options(npu2, None)
    names = [next(iter(f)) if isinstance(f, dict) else f for f in options.families]
    assert names == list(default_families(hardware.accelerator(npu2)))
    for name, family_options in runner.FAMILY_OPTIONS.items():
        assert {name: family_options} in options.families
    assert options.nb_cols_to_use == 8 and options.stage_options == {"npu": "npu2"}


@pytest.fixture
def solver(monkeypatch, tmp_path):
    """Stand in for stream-dse's solve, counting calls, the cache under ``tmp_path``."""
    calls = SimpleNamespace(select=0, generate=0)

    def select_mapping(hardware, workload, out, candidates, options):
        calls.select += 1
        return SimpleNamespace(mapping=candidates[-1])

    def generate_code(hardware, workload, out, mapping, options, estimate=None):
        calls.generate += 1
        return SimpleNamespace(
            cycles=30.0, group_cycles=(10.0, 15.0), dispatch_cycles=5.0
        )

    import stream.api

    monkeypatch.setattr(stream.api, "select_mapping", select_mapping)
    monkeypatch.setattr(stream.api, "generate_code", generate_code)
    monkeypatch.setattr(runner, "ROOT", tmp_path)
    return calls


def test_a_solve_builds_the_cheapest_candidate_once(solver, npu2):
    workload = design.workload(256, 512, 2048)
    candidates = design.candidates(256, 512, 2048, npu2)
    solution = runner.solve("swiglu", ("key",), workload, candidates, npu2, None)
    assert solution.candidate == len(candidates) - 1
    assert solution.groups == tuple(tuple(g.layers) for g in candidates[-1].groups)
    assert (solution.cycles, solution.group_cycles) == (30.0, (10.0, 15.0))
    assert (solution.directory / "inputs" / "workload.onnx").exists()

    again = runner.solve("swiglu", ("key",), workload, candidates, npu2, None)
    assert again == solution and (solver.select, solver.generate) == (1, 1)
    other = runner.solve("swiglu", ("other",), workload, candidates, npu2, None)
    assert other.directory != solution.directory and solver.generate == 2


def test_one_candidate_is_built_unpriced(solver, npu2):
    workload = design.workload(256, 512, 2048)
    [mapping] = design.candidates(
        256, 512, 2048, npu2, partition=1, gemm_block=(32, 32, 64)
    )
    assert runner.solve("swiglu", (), workload, [mapping], npu2, None).candidate == 0
    assert (solver.select, solver.generate) == (0, 1)
