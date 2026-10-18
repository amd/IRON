# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The packaging rules: one full ELF or an xclbin per step, from the device and the values."""

import numpy as np
import pytest
from aie.iron.device import NPU1, NPU2, NPU1Col1, NPU2Col1, from_name

import iron
from iron import Carried, Scratchpad
from iron.common.graph.trace import TracedGraph
from iron.common.graph.handle import PerCall
from iron.common.image.packaging import Kind, dispatches_full_elf, plan
from iron.tests.common.shipped import Shipped
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.tests.common.llama_model import small


def _traced(*values):
    return TracedGraph("g", [], [], [], values=list(values))


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


def test_check_takes_an_xclbin_per_step():
    p = plan(NPU2(), _traced(), check=True)
    assert not p.full_elf
    assert p.reasons == ["check=True: each step its own dispatch, checked"]
    with pytest.raises(ValueError, match="full_elf=True is not possible.*check"):
        plan(NPU2(), _traced(), full_elf=True, check=True)


def test_a_shipped_image_in_a_graph_is_refused(npu2):
    class Shipping(iron.Graph):
        def body(self, a, b):
            return Shipped.step(a, b)

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


class Grows(iron.Graph):
    def body(self, x, *, n: Carried[np.int32]):
        return ReLU.step(ReLU.step(x[: n + 1])), iron.carry(n=n + 1)


class Bounded(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return ReLU.step(ReLU.step(x[: n + 1]))


def test_a_step_a_carried_value_bounds_ends_a_command(npu2):
    traced = Grows().trace(x=(4096,))
    assert plan(npu2, traced).commands == (1,)
    assert plan(npu2, traced).report("g").splitlines()[0] == (
        "g: one full ELF in 2 commands"
    )
    # An xclbin is a dispatch per step already, and a scratchpad bound does
    # not grow from call to call.
    assert plan(npu2, traced, full_elf=False).commands == ()
    assert plan(npu2, Bounded().trace(x=(4096,))).commands == ()


def test_a_prompt_chunk_is_a_command_per_attention_and_decode_one(npu2):
    model = small()
    decode, prompt = (model.trace(**shapes) for shapes in model.shapes())
    assert plan(npu2, decode).commands == ()
    cuts = plan(npu2, prompt).commands
    attention = [i + 1 for i, s in enumerate(prompt.steps) if isinstance(s.op, MHA)]
    assert list(cuts) == attention and len(cuts) == model.config.num_hidden_layers


class Shrinks(iron.Graph):
    def body(self, x, *, n: Carried[np.int32]):
        return ReLU.step(ReLU.step(ReLU.step(x)[:n])), iron.carry(n=n + 1)


def test_a_call_skips_the_commands_its_values_leave_without_work(npu2):
    traced = Shrinks().trace(x=(4096,))
    p = plan(npu2, traced)
    # The bounded step ends a command; the step after reads only its rows.
    assert p.commands == (2,)
    assert p.idle(traced.steps, dict(n=0)) == {1}
    assert p.idle(traced.steps, dict(n=1)) == set()
