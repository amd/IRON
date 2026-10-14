# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The packaging rules: one full ELF or an xclbin per step, from the device and the values."""

import numpy as np
import pytest
from aie.iron.device import NPU1, NPU2, NPU1Col1, NPU2Col1, from_name

import iron
from iron.common.graph import TracedGraph
from iron.common.graph.handle import PerCall
from iron.common.image.packaging import Kind, dispatches_full_elf, plan
from iron.operators.flm.gemm.shipped import Shipped


def _traced(*values):
    return TracedGraph("g", [], [], [], list(values), {}, {}, {}, [])


def test_default_is_a_full_elf_on_npu2():
    p = plan(NPU2(), _traced())
    assert p.full_elf
    assert p.reasons == ["one sequence, one configuration set: a full ELF"]


def test_a_dispatch_time_value_forces_xclbin_and_names_itself():
    t = _traced(PerCall("n", Kind.DISPATCH_TIME, np.int32))
    with pytest.raises(
        ValueError, match="full_elf=True is not possible.*n: a DispatchTime"
    ):
        plan(NPU2(), t, full_elf=True)
    p = plan(NPU2(), t, full_elf=False)
    assert not p.full_elf
    assert p.values == [
        ("n", "aie.dispatch_time", "sizes, strides and offsets regenerated per call")
    ]


def test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering():
    t = _traced(PerCall("pos", Kind.SCRATCHPAD, np.int32))
    with pytest.raises(ValueError, match=r"npu1 \(AIE2\) has no full-ELF dispatch"):
        plan(NPU1(), t, full_elf=True)
    # An xclbin run has no parameter scratchpad: the value is a dispatch-
    # time scalar of its kernel, and the report says which way it lowers.
    p = plan(NPU1(), t, full_elf=False)
    assert not p.full_elf and "dispatch-time scalar" in p.values[0][2]
    assert "written into the array by the sequence" in p.values[0][2]
    assert plan(NPU2(), t).values[0][2] == "patched through the parameter scratchpad"


def test_the_architecture_decides_not_the_name():
    # A partial NPU2 still dispatches a full ELF; a one-column NPU1 does not.
    assert plan(from_name("npu2", n_cols=4), _traced()).full_elf
    with pytest.raises(ValueError, match=r"npu1_1col \(AIE2\) has no full-ELF"):
        plan(NPU1Col1(), _traced(), full_elf=True)


def test_full_elf_goes_by_architecture():
    # NPU2Col1 is no NPU2 subclass, and NPU1Col1 is named "npu1_1col".
    assert dispatches_full_elf(NPU2()) and dispatches_full_elf(NPU2Col1())
    assert not dispatches_full_elf(NPU1()) and not dispatches_full_elf(NPU1Col1())


def test_a_forced_xclbin_is_derived_and_says_why():
    p = plan(NPU1(), _traced())
    assert not p.full_elf
    assert p.reasons == ["npu1 (AIE2) has no full-ELF dispatch"]
    assert not plan(
        NPU2(), _traced(PerCall("n", Kind.DISPATCH_TIME, np.int32))
    ).full_elf
    p = plan(NPU1(), _traced(), full_elf=False)
    assert p.reasons == [
        "full_elf=False: asked for",
        "npu1 (AIE2) has no full-ELF dispatch",
    ]


def test_an_xclbin_is_asked_for_where_a_full_elf_would_do():
    p = plan(NPU2(), _traced(), full_elf=False)
    assert not p.full_elf
    assert p.reasons == ["full_elf=False: asked for"]


def test_a_shipped_image_in_a_graph_is_refused(npu2):
    class Shipping(iron.Graph):
        def body(self, a, b):
            return Shipped(a, b)

    traced = Shipping().trace(a=(256, 1024), b=(1024, 1152))
    for full_elf in (None, False):
        with pytest.raises(ValueError, match=r"Shipped \(flm_mm_.*outside a graph"):
            plan(npu2, traced, full_elf=full_elf)


def test_report_reads_as_one_block():
    p = plan(NPU2(), _traced(PerCall("pos", Kind.SCRATCHPAD, np.int32)))
    assert p.report("decode").splitlines() == [
        "decode: one full ELF",
        "  one sequence, one configuration set: a full ELF",
        "  pos: iron.scratchpad; patched through the parameter scratchpad",
    ]
