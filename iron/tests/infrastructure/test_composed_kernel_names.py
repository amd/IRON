#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A design links the same kernel objects built alone as composed.

Composed MLIR is not an artifact, standalone builds call their generator
directly, and a kernel is named for its recipe rather than its position, so a
design names the same objects whether it is built alone or composed. The last
is what is checked here, end to end.

Needs a device: the full-ELF build runs for real, because the whole point is
what it leaves lying around; the standalone side only needs a device to
generate its own MLIR at all (device-specialized designs read the current
device), not to compile anything.
"""

import dataclasses
import re

import pytest

from iron.common.design import OperatorDesign
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.operators import ElementwiseAdd
from iron.tests.support.graphs import Adds

pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored

SIZE = 1024


def _linked_objects(operator):
    """What the operator's own MLIR tells the linker to bring in.

    Calls the generator directly rather than compiling and reading a file
    back: a standalone build no longer writes its MLIR to disk either (see
    the module docstring), so there is nothing to read.
    """
    mlir = str(OperatorDesign(operator).build())
    return sorted(set(re.findall(r'link_with\s*=\s*"([^"]+)"', mlir)))


def test_a_design_links_the_same_objects_alone_or_composed():
    """Build composed, then standalone, and check both name the same objects.

    Order matters: the standalone build has to come second, since it is the
    one reading what the full-ELF build left behind. Doing it the other way round
    passes whatever happens.
    """
    recording = Adds(ElementwiseAdd(size=SIZE, tile_size=128), 1).record(
        x=(SIZE,), w=(SIZE,)
    )
    seq = Image(dataclasses.replace(recording, name="poisoning_probe"), FullELF())
    seq.compile()
    composed = set(re.findall(r'link_with\s*=\s*"([^"]+)"', Composition(seq).text()))

    linked = _linked_objects(ElementwiseAdd(size=SIZE, tile_size=128))
    assert linked and set(linked) <= composed, (
        f"standalone build links {linked}, the composed one {sorted(composed)}; a "
        "design names different objects depending on what it is composed with"
    )
