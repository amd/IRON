#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What CompilableDesign's cache key does and does not distinguish.

The plan is to retire IRON's artifact graph and hand a captured graph to
``CompilableDesign``, which brings content-addressed caching, cross-process
locking and depfile validation the artifact graph lacks. That only works if
its key distinguishes two different graphs. It does not, in the obvious
encoding, and these tests pin exactly where the line falls -- a cache that
fails to discriminate is silent, handing back another graph's artifacts.

The trap is easy to miss. Probing this with ``lambda: a`` and ``lambda: b``
suggests the key discriminates, but those two lambdas have *different code
objects* because they name different variables. Two captured graphs go through
one call site, so their generators share a code object and differ only in what
they close over -- which is the case below, and the one that collides.

Device-free; nothing here compiles.
"""

import pytest
from aie.utils.compile.jit.compilabledesign import CompilableDesign


def _design(mlir_text, **kwargs):
    """A generator closing over its MLIR, as a captured graph would arrive."""
    return CompilableDesign(lambda: mlir_text, full_elf=True, **kwargs)


def test_closure_value_alone_does_not_change_the_key():
    """The hole L3.5 has to route around.

    Both generators share a code object and differ only in the MLIR they close
    over. The key is the same, so handing captured graphs to CompilableDesign
    as bare closures would give the second one the first one's artifacts.
    """
    a = _design("module { /* graph A */ }")
    b = _design("module { /* graph B */ }")
    assert a._compute_cache_hash() == b._compute_cache_hash(), (
        "if this now fails, upstream started hashing closure contents and "
        "IRON can stop working around it"
    )


def test_compile_kwargs_do_change_the_key():
    """The supported way to carry a graph's identity.

    compile_kwargs is part of the recipe hash, so putting something that
    identifies the graph there discriminates where a closure does not.
    """
    text = "module { /* same text */ }"
    a = CompilableDesign(lambda: text, full_elf=True, compile_kwargs={"graph": "A"})
    b = CompilableDesign(lambda: text, full_elf=True, compile_kwargs={"graph": "B"})
    assert a._compute_cache_hash() != b._compute_cache_hash()


def test_the_same_graph_gets_the_same_key():
    """Otherwise nothing would ever hit cache."""
    text = "module { /* stable */ }"
    assert _design(text)._compute_cache_hash() == _design(text)._compute_cache_hash()


@pytest.mark.parametrize("full_elf", [True, False])
def test_full_elf_is_part_of_the_key(full_elf):
    """Fused dispatch asks for a full ELF and separate does not, so the two
    produce different artifacts from the same MLIR and must not share an entry.
    """
    text = "module { /* same */ }"
    this = CompilableDesign(lambda: text, full_elf=full_elf)
    other = CompilableDesign(lambda: text, full_elf=not full_elf)
    assert this._compute_cache_hash() != other._compute_cache_hash()
