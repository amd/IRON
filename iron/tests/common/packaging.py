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


def test_npu1_forces_xclbin_and_a_scratchpad_value_has_no_home_there_yet():
    t = _traced(Value("pos", "scratchpad", np.int32))
    with pytest.raises(ValueError, match="npu1 has no full-ELF dispatch"):
        plan("npu1", t, image=ELF)
    # An xclbin run has no parameter scratchpad (S2): the value is a dispatch-
    # time scalar of its kernel, and the report says which way it lowers.
    p = plan("npu1", t, boundaries=each_step)
    assert p.image == XCLBIN and "dispatch-time scalar" in p.values[0][2]
    assert "spike S3" in p.values[0][2]
    # On a chunked image the fused sequence forwards the scalars its chunks
    # use, but its stream's PDI preloads are beyond the Python dispatch bridge.
    with pytest.raises(NotImplementedError, match="chunked image.*PDI loads"):
        plan("npu1", t)
    assert plan("npu2", t).values[0][2] == "patched through the parameter scratchpad"


def test_boundaries_force_xclbin_and_pick_the_dispatch():
    from iron.common.sequence import ChunkedDispatch

    p = plan("npu2", _traced(), boundaries=chunks(8))
    assert p.image == XCLBIN
    assert isinstance(p.dispatch, ChunkedDispatch) and p.dispatch.n == 8
    assert p.report("g").splitlines()[0] == "g: image xclbin, dispatch 'chunked(8)'"
    # One fused sequence in an xclbin (spike S1's construction) is one chunk.
    p = plan("npu2", _traced(), image=XCLBIN)
    assert isinstance(p.dispatch, ChunkedDispatch) and p.dispatch.n is None
    assert p.reasons == ["one sequence, one configuration set: a full ELF"]
    p = plan("npu1", _traced())  # the NPU1 default: one chunk of everything
    assert p.image == XCLBIN and isinstance(p.dispatch, ChunkedDispatch)
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
