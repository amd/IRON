# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A ``param(probe=)`` field reaches its design only as words the cores
read, so its cost key may leave it out.

Each operator that declares a probe is generated away from it and at it,
and the two modules are walked operation by operation: only constants
whose every user is an ``aiex.npu.rtp_write`` may differ. A probe field
leaking into a transfer, a trip count or a core shows up as any other
difference. What the walk cannot see is a kernel whose time follows the
words' values; the hardware check in
``iron/tests/infrastructure/narrowing.py`` measures that.

No toolchain and no NPU: the modules are generated in process.
"""

import itertools
import re

import pytest

import iron.operators as ops
import iron.operators.flm as flm
from iron.common.design import OperatorDesign
from iron.common.image.fusion import generate
from iron.operators.clamp import Clamp
from iron.operators.flm.gemm.op import GEMM as FlmGEMM

pytestmark = pytest.mark.usefixtures("npu2")

# Every operator that declares a probe, constructed with each probe field
# away from its probe.
AWAY = {
    Clamp: dict(size=65536, low=-0.75, high=1.25),
    FlmGEMM: dict(M=256, K=512, N=1024, clamp=(-2.0, 2.0)),
}

# mlir-aie numbers an unnamed Flow from a process-wide counter, so two
# generations of one design name their flows apart.
FLOW = re.compile(r"\bflow(\d+)")


def _operations(op):
    """Every operation nested in ``op``, in program order."""
    for region in op.regions:
        for block in region.blocks:
            for inner in block.operations:
                yield inner.operation
                yield from _operations(inner)


def _attributes(op, flows: dict[str, int]) -> dict[str, str]:
    """``op``'s attributes as text, each flow renumbered by its first
    appearance in the module (``flows``, filled as the walk goes).
    """
    return {
        name: FLOW.sub(
            lambda m: f"flow#{flows.setdefault(m.group(1), len(flows))}",
            str(op.attributes[name]),
        )
        for name in op.attributes
    }


def test_every_operator_declaring_a_probe_is_checked():
    catalog = {getattr(ops, n) for n in ops.__all__}
    catalog |= {getattr(flm, n) for n in flm.__all__}
    assert {cls for cls in catalog if cls._probe_fields} == set(AWAY)


@pytest.mark.parametrize("cls", list(AWAY), ids=lambda cls: cls.__qualname__)
def test_a_probe_field_moves_only_runtime_parameter_words(cls):
    away = cls(**AWAY[cls])
    probe = away.probed()
    assert all(getattr(away, n) != v for n, v in cls._probe_fields.items())
    modules = [generate(OperatorDesign(op.resolved())).module for op in (away, probe)]
    flows = ({}, {})
    moved = 0
    for a, b in itertools.zip_longest(*(_operations(m.operation) for m in modules)):
        assert a is not None and b is not None, "one module has more operations"
        assert a.name == b.name
        assert len(a.operands) == len(b.operands)
        if _attributes(a, flows[0]) == _attributes(b, flows[1]):
            continue
        users = {
            u.owner.operation.name for op in (a, b) for r in op.results for u in r.uses
        }
        assert a.name == "arith.constant" and users == {
            "aiex.npu.rtp_write"
        }, f"{a} and {b} differ, and reach {sorted(users)}"
        moved += 1
    assert moved, "the probe fields reach no runtime parameter word"
