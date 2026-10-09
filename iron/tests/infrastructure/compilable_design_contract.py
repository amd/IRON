#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What CompilableDesign's cache key does and does not distinguish.

IRON hands its designs and captured graphs to ``CompilableDesign``, which
brings content-addressed caching, cross-process locking and depfile
validation. That only works if its key distinguishes two different graphs,
and these tests pin exactly where the line falls -- a cache that fails to
discriminate is silent, handing back another graph's artifacts.

Two captured graphs go through one call site, so their generators share a
code object and differ only in what they close over. The key reads a
closure's plain values (strings, numbers), but an object it closes over only
by the module that defines it: two ``Fusion``s of different sequences
collide. So IRON's generators take their identity as a ``CompileTime``
argument, through ``compile_kwargs``.

Device-free; nothing here compiles.
"""

import pytest
from aie.utils.compile.jit.compilabledesign import CompilableDesign


class _Graph:
    def __init__(self, text: str):
        self.text = text


def _graph_design(graph: _Graph, **kwargs):
    """A generator closing over an object, as ``Fusion`` and ``OperatorDesign``
    arrive.
    """
    return CompilableDesign(lambda: graph.text, full_elf=True, **kwargs)


def test_an_object_closed_over_alone_does_not_change_the_key():
    """The hole IRON's ``CompileTime`` key routes around: handing objects to
    CompilableDesign as bare closures would give the second one the first
    one's artifacts.
    """
    a = _graph_design(_Graph("module { /* graph A */ }"))
    b = _graph_design(_Graph("module { /* graph B */ }"))
    assert a._compute_cache_hash() == b._compute_cache_hash(), (
        "if this now fails, upstream started hashing objects' state and "
        "IRON's generators can drop their key"
    )


@pytest.mark.parametrize("full_elf", [True, False])
def test_full_elf_is_part_of_the_key(full_elf):
    """Fused dispatch asks for a full ELF and separate does not, so the two
    produce different artifacts from the same MLIR and must not share an entry.
    """
    text = "module { /* same */ }"
    this = CompilableDesign(lambda: text, full_elf=full_elf)
    other = CompilableDesign(lambda: text, full_elf=not full_elf)
    assert this._compute_cache_hash() != other._compute_cache_hash()
