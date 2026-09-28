# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The packaging rules: image and dispatch from device, values and boundaries."""

import numpy as np
import pytest
from aie.iron.device import NPU1, NPU2, NPU1Col1, from_name

from iron.common.graph import TracedGraph, Value
from iron.common.image.packaging import ELF, XCLBIN, each_step, plan


def _traced(*values):
    return TracedGraph("g", [], [], [], list(values), {}, {}, {}, [])


def test_default_is_a_full_elf_on_npu2():
    p = plan(NPU2(), _traced())
    assert (p.image, p.dispatch) == (ELF, "fused")
    assert p.reasons == ["one sequence, one configuration set: a full ELF"]


def test_a_dispatch_time_value_forces_xclbin_and_names_itself():
    t = _traced(Value("n", "dispatch", np.int32))
    with pytest.raises(
        ValueError, match="image=elf is not possible.*n: a DispatchTime"
    ):
        plan(NPU2(), t, image=ELF)
    p = plan(NPU2(), t, boundaries=each_step)
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert p.values == [
        ("n", "dispatch", "sizes, strides and offsets regenerated per call")
    ]


def test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering():
    t = _traced(Value("pos", "scratchpad", np.int32))
    with pytest.raises(ValueError, match=r"npu1 \(AIE2\) has no full-ELF dispatch"):
        plan(NPU1(), t, image=ELF)
    # An xclbin run has no parameter scratchpad: the value is a dispatch-
    # time scalar of its kernel, and the report says which way it lowers.
    p = plan(NPU1(), t, boundaries=each_step)
    assert p.image == XCLBIN and "dispatch-time scalar" in p.values[0][2]
    assert "written into the array by the sequence" in p.values[0][2]
    assert plan(NPU2(), t).values[0][2] == "patched through the parameter scratchpad"


def test_the_architecture_decides_not_the_name():
    # A partial NPU2 still dispatches a full ELF; a one-column NPU1 does not.
    assert plan(from_name("npu2", n_cols=4), _traced()).image == ELF
    with pytest.raises(ValueError, match=r"npu1_1col \(AIE2\) has no full-ELF"):
        plan(NPU1Col1(), _traced(), image=ELF)


def test_a_forced_xclbin_defaults_to_each_step():
    p = plan(NPU1(), _traced())
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert p.reasons == [
        "npu1 (AIE2) has no full-ELF dispatch",
        "boundaries=each_step: the xclbin form that is built",
    ]
    p = plan(NPU2(), _traced(Value("n", "dispatch", np.int32)))
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert plan(NPU1(), _traced(), image=XCLBIN).dispatch == "separate"


def test_boundaries_force_xclbin_and_the_unbuilt_forms_are_named():
    with pytest.raises(NotImplementedError, match="no proven construction"):
        plan(NPU2(), _traced(), image=XCLBIN)  # one fused sequence in an xclbin
    p = plan(NPU2(), _traced(), boundaries=each_step)
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert p.reasons == ["boundaries=each_step: more than one dispatch"]


def test_arguments_are_checked():
    with pytest.raises(ValueError, match="image must be"):
        plan(NPU2(), _traced(), image="pdi")
    with pytest.raises(ValueError, match="boundaries must be"):
        plan(NPU2(), _traced(), boundaries=8)


def test_report_reads_as_one_block():
    p = plan(NPU2(), _traced(Value("pos", "scratchpad", np.int32)))
    assert p.report("decode").splitlines() == [
        "decode: image elf, dispatch 'fused'",
        "  one sequence, one configuration set: a full ELF",
        "  pos: scratchpad; patched through the parameter scratchpad",
    ]
