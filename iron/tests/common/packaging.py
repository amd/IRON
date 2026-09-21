# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The packaging rules: image and dispatch from device, values and boundaries."""

import numpy as np
import pytest

from iron.common.graph import TracedGraph, Value
from iron.common.packaging import ELF, XCLBIN, chunks, each_step, plan


def _traced(*values):
    return TracedGraph("g", [], [], [], list(values), {}, {}, {}, [])


def test_default_is_a_full_elf_on_npu2():
    p = plan("npu2", _traced())
    assert (p.image, p.dispatch) == (ELF, "fused")
    assert p.reasons == ["one sequence, one configuration set: a full ELF"]


def test_a_dispatch_time_value_forces_xclbin_and_names_itself():
    t = _traced(Value("n", "dispatch", np.int32))
    with pytest.raises(
        ValueError, match="image=elf is not possible.*n: a DispatchTime"
    ):
        plan("npu2", t, image=ELF)
    p = plan("npu2", t, boundaries=each_step)
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert p.values == [
        ("n", "dispatch", "sizes, strides and offsets regenerated per call")
    ]


def test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering():
    t = _traced(Value("pos", "scratchpad", np.int32))
    with pytest.raises(ValueError, match="npu1 has no full-ELF dispatch"):
        plan("npu1", t, image=ELF)
    p = plan("npu1", t, boundaries=each_step)
    assert p.image == XCLBIN and "unverified (spike S2)" in p.values[0][2]
    assert plan("npu2", t).values[0][2] == "patched through the parameter scratchpad"


def test_boundaries_force_xclbin_and_the_unbuilt_forms_are_named():
    with pytest.raises(NotImplementedError, match="spike S1"):
        plan("npu2", _traced(), boundaries=chunks(8))
    with pytest.raises(NotImplementedError, match="spike S1"):
        plan("npu2", _traced(), image=XCLBIN)  # one fused sequence in an xclbin
    with pytest.raises(NotImplementedError, match="spike S1"):
        plan("npu1", _traced())  # the NPU1 default needs a boundary choice today
    p = plan("npu2", _traced(), boundaries=each_step)
    assert (p.image, p.dispatch) == (XCLBIN, "separate")
    assert p.reasons == ["boundaries=each_step: more than one dispatch"]


def test_arguments_are_checked():
    with pytest.raises(ValueError, match="image must be"):
        plan("npu2", _traced(), image="pdi")
    with pytest.raises(ValueError, match="boundaries must be"):
        plan("npu2", _traced(), boundaries=8)
    with pytest.raises(ValueError, match="n >= 1"):
        chunks(0)


def test_report_reads_as_one_block():
    p = plan("npu2", _traced(Value("pos", "scratchpad", np.int32)))
    assert p.report("decode").splitlines() == [
        "decode: image elf, dispatch 'fused'",
        "  one sequence, one configuration set: a full ELF",
        "  pos: scratchpad; patched through the parameter scratchpad",
    ]
