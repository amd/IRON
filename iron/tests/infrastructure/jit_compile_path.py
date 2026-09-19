#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Compiling a captured graph through CompilableDesign produces a real ELF.

This is the step the artifact-graph retirement rests on, so it is checked on
hardware rather than argued about: a graph recorded from dataflow, through the
upstream compile path, out the other side as a linked full ELF.

Needs a device, since the fused path is NPU2-only and the ELF is genuinely
built here rather than mocked.
"""

from pathlib import Path

import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.capture import capture
from iron.common.context import AIEContext
from iron.common.jit_compile import compile_sequence, _digest
from iron.operators import ElementwiseAdd


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _captured(name):
    add = ElementwiseAdd(size=1024, tile_size=128, context=AIEContext())
    with capture() as graph:
        x = graph.input("x")
        w = graph.input("w")
        value = graph(add, x, w)
        value = graph(add, value, w)
    sequence = graph.build(name, dispatch="fused")
    sequence.compile()
    return sequence


def test_captured_graph_compiles_to_an_elf(tmp_path):
    """The load-bearing claim: it links, and the ELF is real."""
    sequence = _captured("jitpath_elf")
    elf = compile_sequence(sequence, tmp_path / "graph.elf")
    assert elf.exists(), "no ELF produced"
    assert elf.stat().st_size > 1024, f"ELF suspiciously small: {elf.stat().st_size}"
    assert elf.read_bytes()[:4] == b"\x7fELF", "not an ELF"


def test_kernel_objects_are_staged_under_bare_names(tmp_path):
    """object_files does not stage; the work dir has to be populated.

    The fused MLIR's link_with names objects without a directory, so a path
    that is merely declared is not a path aiecc can find. This is the one
    thing the retirement cannot delete along with the artifact graph.
    """
    sequence = _captured("jitpath_stage")
    elf = tmp_path / "graph.elf"
    compile_sequence(sequence, elf)
    staged = {p.name for p in elf.with_suffix(".prj").iterdir() if p.suffix == ".o"}
    assert staged, "no kernel objects staged into the work directory"
    assert all("/" not in name for name in staged)


def test_two_graphs_get_distinct_cache_keys():
    """Identity rides in compile_kwargs because the key ignores closures.

    Without this the second graph would be handed the first one's ELF, and
    nothing would report it.
    """
    one = _digest("module { /* graph one */ }")
    two = _digest("module { /* graph two */ }")
    assert one != two
