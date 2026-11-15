# SPDX-FileCopyrightText: Copyright (C) 2026 KU Leuven (MICAS). All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``StreamOperator``: a fused group of a stream-dse design as an exported design.

The solve is stood in for by a solution written to disk: what the operator
does with it is the subject, not what stream-dse solves.
"""

import json

import pytest

pytest.importorskip("stream", reason="stream-dse is not installed")
pytest.importorskip("onnxscript", reason="onnxscript is not installed")

from aie import ir  # noqa: E402
from aie.iron import In, Out  # noqa: E402
from aie.utils.compile.jit.operator import Unresolvable  # noqa: E402
from ml_dtypes import bfloat16  # noqa: E402

from iron.common.design import OperatorDesign  # noqa: E402
from iron.common.stream.runner import Solution  # noqa: E402
from iron.operators.swiglu_prefill_stream.op import (  # noqa: E402
    GATE,
    PARTITIONS,
    SwiGLUFusedStream,
    SwiGLUProjectionStream,
    _SwiGLUStream,
)

pytestmark = pytest.mark.usefixtures("npu2")

DIMS = dict(seq_len=256, embedding_dim=512, hidden_dim=2048)
MODULE = "module {\n}\n"


def _solved(tmp_path, groups):
    for index in range(len(groups)):
        codegen = tmp_path / f"group_{index}" / "codegen"
        codegen.mkdir(parents=True)
        (codegen / "final.mlir").write_text(MODULE)
        (codegen / "kernels.json").write_text(json.dumps([]))
    return Solution(tmp_path, 0, groups, 3.0, (1.0,) * len(groups), 0.0)


@pytest.fixture
def solved(monkeypatch, tmp_path):
    """Give every SwiGLU group the solution ``partition`` names."""

    def solve(partition):
        solution = _solved(tmp_path, PARTITIONS[partition])
        monkeypatch.setattr(_SwiGLUStream, "solution", lambda self: solution)
        return solution

    return solve


def _design_text(op):
    with ir.Context(), ir.Location.unknown():
        return str(OperatorDesign(op).build())


def test_a_group_builds_stream_dses_design(solved):
    solved(1)
    op = SwiGLUFusedStream(**DIMS, partition=1)
    assert [b.name for b in op.buffers] == [
        "input",
        "w_gate",
        "w_up",
        "w_down",
        "output",
    ]
    assert _design_text(op) == MODULE


def test_each_layer_by_layer_group_finds_its_own(solved):
    solved(5)
    gate = SwiGLUProjectionStream(**DIMS, layer=GATE).resolved()
    assert gate.group() == 0 and _design_text(gate) == MODULE


def test_a_group_the_partition_does_not_have_is_unresolvable(solved):
    solved(5)
    with pytest.raises(Unresolvable, match="fused the layers"):
        SwiGLUFusedStream(**DIMS).resolved().group()


def test_operands_out_of_the_sequences_order_are_refused(solved):
    solved(5)

    class Swapped(_SwiGLUStream):
        w = In(_SwiGLUStream.embedding_dim, _SwiGLUStream.hidden_dim, dtype=bfloat16)
        x = In(_SwiGLUStream.seq_len, _SwiGLUStream.embedding_dim, dtype=bfloat16)
        y = Out(_SwiGLUStream.seq_len, _SwiGLUStream.hidden_dim, dtype=bfloat16)

        def layers(self):
            return (GATE,)

    with pytest.raises(ValueError, match="its group takes"):
        _design_text(Swapped(**DIMS))


def test_the_identity_follows_the_solver(monkeypatch):
    """Another solver may generate another design, so it is another build."""
    op = SwiGLUFusedStream(**DIMS).resolved()
    _, own = op.design_key()
    monkeypatch.setenv("STREAM_BACKEND", "another")
    assert own[-1][0] == "stream" and op.design_key()[1][-1] != own[-1]


def test_groups_of_one_design_share_its_solve():
    ops = [
        SwiGLUFusedStream(**DIMS).resolved(),
        SwiGLUProjectionStream(**DIMS, layer=GATE).resolved(),
    ]
    assert len({op.solve_key() for op in ops}) == 1
    pinned = SwiGLUFusedStream(**DIMS, partition=1).resolved()
    assert pinned.solve_key() != ops[0].solve_key()


@pytest.mark.parametrize("missing", ["stream", "torch", "onnxscript"])
def test_without_the_optional_stack_it_is_unresolvable(monkeypatch, missing):
    from iron.common.stream import operator

    find_spec = operator.find_spec
    monkeypatch.setattr(
        operator, "find_spec", lambda name: None if name == missing else find_spec(name)
    )
    with pytest.raises(Unresolvable, match=f"{missing} not installed"):
        SwiGLUFusedStream(**DIMS).resolved()


def test_a_size_no_candidate_fits_is_incompatible():
    with pytest.raises(ValueError, match="hidden_dim"):
        SwiGLUFusedStream(seq_len=256, embedding_dim=512, hidden_dim=2000).resolved()
