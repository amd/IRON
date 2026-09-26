#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A fused build must not leave its MLIR in the standalone operator's slot.

A fused build once renamed each design's kernels by position::

    generator.kwargs["func_prefix"] = f"op{idx}_"

on a generator that was also an artifact the fused build compiled to disk --
to the exact path a standalone build of the same operator reads. The cache
keyed only on filename and mtime, so a later standalone build trusted the
prefixed file and asked the linker for ``op0_add.o``, which a standalone
build never produces. The failure surfaced as an undefined symbol at link
time, in a build that did nothing wrong, possibly in a different process from
the fused build that poisoned it.

Nothing is left to poison now: fused MLIR is not an artifact, standalone
builds call their generator directly, and a kernel is named for its recipe
rather than its position, so a design names the same objects whether it is
built alone or fused. The last is what is checked here, end to end.

Needs a device: the fused build runs for real, because the whole point is
what it leaves lying around; the standalone side only needs a device to
generate its own MLIR at all (device-specialized designs read the current
device), not to compile anything.
"""

import re

import pytest

import iron
from iron.common.image import build_fused_mlir
from iron.operators import ElementwiseAdd

SIZE = 1024
TILE = 128


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _operator():
    return ElementwiseAdd(size=SIZE, tile_size=TILE)


def _linked_objects(operator):
    """What the operator's own MLIR tells the linker to bring in.

    Calls the generator directly rather than compiling and reading a file
    back: a standalone build no longer writes its MLIR to disk either (see
    the module docstring), so there is nothing to read.
    """
    mlir = str(operator.generator()())
    return sorted(set(re.findall(r'link_with\s*=\s*"([^"]+)"', mlir)))


def test_fused_build_does_not_poison_the_standalone_mlir():
    """Build fused, then standalone, and check both name the same objects.

    Order matters: the standalone build has to come second, since it is the
    one reading what the fused build left behind. Doing it the other way round
    passes whatever happens.
    """
    add = _operator()

    @iron.graph
    def probe(x, w):
        return add(x, w)

    seq = probe.trace(x=(SIZE,), w=(SIZE,)).sequence(
        "poisoning_probe", dispatch="fused"
    )
    seq.compile()
    fused = set(re.findall(r'link_with\s*=\s*"([^"]+)"', build_fused_mlir(seq)))

    linked = _linked_objects(_operator())
    assert linked and set(linked) <= fused, (
        f"standalone build links {linked}, the fused one {sorted(fused)}; a "
        "design names different objects depending on what it is fused with"
    )
