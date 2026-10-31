# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The packaging rules: one full ELF or an xclbin per step, from the device and the values."""

import numpy as np
import pytest
from aie.helpers.taplib import PerCall
from aie.iron.device import NPU1, NPU2, NPU1Col1, from_name

import iron
from iron import Carried, Scratchpad
from iron.common.graph.compiled import _step_words
from iron.common.graph.record import Recording
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF
from iron.common.image.packaging import SCRATCHPAD_WORDS, Kind, plan
from iron.common.image.sequence import Image
from iron.common.image.step import Fusion, FusionKind
from iron.operators.mha import MHA
from iron.operators.relu import ReLU
from iron.tests.support.llama_model import small
from iron.tests.support.shipped import Shipped


def _recorded(*values):
    return Recording("g", [], [], [], values=list(values))


def test_default_is_a_full_elf_on_npu2():
    p = plan(NPU2(), _recorded())
    assert p.full_elf
    assert p.reasons == ["one sequence, one configuration set: a full ELF"]


def test_npu1_forces_xclbin_and_reports_the_scratchpad_lowering():
    t = _recorded(PerCall("pos", Kind.SCRATCHPAD, np.int32))
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
    # NPU2Col1 is no NPU2 subclass, and NPU1Col1 is named "npu1_1col".
    assert plan(from_name("npu2", n_cols=4), _recorded()).full_elf
    with pytest.raises(ValueError, match=r"npu1_1col \(AIE2\) has no full-ELF"):
        plan(NPU1Col1(), _recorded(), full_elf=True)


def test_a_forced_xclbin_is_derived_and_says_why():
    p = plan(NPU1(), _recorded())
    assert not p.full_elf
    assert p.reasons == ["npu1 (AIE2) has no full-ELF dispatch"]
    p = plan(NPU1(), _recorded(), full_elf=False)
    assert p.reasons == [
        "full_elf=False: asked for",
        "npu1 (AIE2) has no full-ELF dispatch",
    ]


def test_an_xclbin_is_asked_for_where_a_full_elf_would_do():
    p = plan(NPU2(), _recorded(), full_elf=False)
    assert not p.full_elf
    assert p.reasons == ["full_elf=False: asked for"]


def test_check_takes_an_xclbin_per_step():
    p = plan(NPU2(), _recorded(), check=True)
    assert not p.full_elf
    assert p.reasons == ["check=True: each step its own dispatch, checked"]
    with pytest.raises(ValueError, match="full_elf=True is not possible.*check"):
        plan(NPU2(), _recorded(), full_elf=True, check=True)


def test_a_shipped_image_in_a_graph_is_refused(npu2):
    class Shipping(iron.Graph):
        def body(self, a, b):
            return Shipped.step(a, b)

    recording = Shipping().record(a=(256, 1024), b=(1024, 1152))
    for full_elf in (None, False):
        with pytest.raises(ValueError, match=r"Shipped \(flm_mm_.*outside a graph"):
            plan(npu2, recording, full_elf=full_elf)


def test_report_reads_as_one_block():
    p = plan(NPU2(), _recorded(PerCall("pos", Kind.SCRATCHPAD, np.int32)))
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


class Encoding(iron.Graph):
    """Two layers' attention over a call's own rows, as a tower's are.

    Bounded by a scratchpad value.
    """

    def body(self, x, *, n: Scratchpad[np.int32]):
        rows, heads, d = x.shape
        x = x[:n]
        for _ in range(2):
            o = MHA.step(
                x, x, x, heads_interleaved=True, kv_interleaved=True, causal=False
            )
            x = ReLU.step(o.reshape(rows * heads * d)).reshape(rows, heads, d)
        return x


def test_a_bounded_step_ends_no_command(npu2):
    """Check that a bounded step ends no command.

    However a call bounds a step, carried or scratchpad, attention or
    not, a full ELF stays one command: a prompt chunk, a decode step and
    an encoder call alike.
    """
    model = small()
    for recording in (
        Grows().record(x=(4096,)),
        Bounded().record(x=(4096,)),
        Encoding().record(x=(256, 2, 64)),
        *(model.record(**shapes) for shapes in model.shapes()),
    ):
        p = plan(npu2, recording)
        assert p.full_elf and p.commands == (), recording.name
        assert p.report("g").splitlines()[0] == "g: one full ELF"


class ManyWords(iron.Graph):
    def body(self, x, *, n: Scratchpad[np.int32]):
        return tuple(ReLU.step(x[: n + k]) for k in range(40))


def test_a_command_reads_at_most_a_scratchpads_words(npu2):
    """Check that a command reads at most a scratchpad's words.

    Forty steps, each bounded by its own word, are commands of at most 32
    words each, the state table a command's scratchpad has.
    """
    recording = ManyWords().record(x=(4096,))
    words = _step_words(recording)
    assert len(frozenset().union(*words)) > SCRATCHPAD_WORDS
    p = plan(npu2, recording, step_words=words)
    edges = (0, *p.commands, len(recording.steps))
    held = [frozenset().union(*words[a:b]) for a, b in zip(edges, edges[1:])]
    assert len(held) > 1 and all(len(h) <= SCRATCHPAD_WORDS for h in held)
    assert any("scratchpad holds 32 words" in r for r in p.reasons)


def test_a_command_never_starts_within_a_fusion(npu2):
    """A fusion of the steps either side of a split moves the split to its first member.

    The composition starts each command at that step's place among the fused steps,
    one fewer past the fusion.
    """
    recording = ManyWords().record(x=(4096,))
    words = _step_words(recording)
    first = plan(npu2, recording, step_words=words).commands[0]
    pack = Fusion(FusionKind.PACK, (first - 1, first))
    p = plan(npu2, recording, step_words=words, fusions=(pack,))
    assert p.commands[0] == first - 1
    edges = (0, *p.commands, len(recording.steps))
    held = [frozenset().union(*words[a:b]) for a, b in zip(edges, edges[1:])]
    assert all(len(h) <= SCRATCHPAD_WORDS for h in held)
    image = Image(recording, FullELF(commands=p.commands), fusions=(pack,))
    image._prepare()
    assert Composition(image).commands == (
        p.commands[0],
        *(c - 1 for c in p.commands[1:]),
    )


class Shrinks(iron.Graph):
    def __init__(self):
        self.staged = iron.state((4096,))

    def body(self, x, *, n: Scratchpad[np.int32]):
        iron.on_host(self.stage, ReLU.step(x), writes=(self.staged,))
        return ReLU.step(self.staged[:n])

    def stage(self, y, staged):
        staged[:] = y


def test_a_call_skips_the_commands_its_values_leave_without_work(npu2):
    recording = Shrinks().record(x=(4096,))
    p = plan(npu2, recording)
    # The host step ends a command; the step after reads only n rows.
    assert p.commands == (1,)
    assert p.idle(recording.steps, dict(n=0)) == {1}
    assert p.idle(recording.steps, dict(n=1)) == set()


def test_a_host_step_within_a_fusion_is_refused(npu2):
    recording = Shrinks().record(x=(4096,))
    with pytest.raises(ValueError, match=r"host step runs within a fusion"):
        plan(npu2, recording, fusions=(Fusion(FusionKind.PACK, (0, 1)),))
