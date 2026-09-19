#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A fused build must not leave its MLIR in the standalone operator's slot.

``FusedDispatch.build_fused_mlir`` takes each operator's MLIR artifact and
mutates its generator::

    mlir_artifact.generator.kwargs["func_prefix"] = f"op{idx}_"

without changing the artifact's filename. Those artifacts are dependencies of
the SequenceMLIRArtifact, so they are compiled to disk -- writing symbol-
prefixed MLIR to the path a standalone build of the same operator reads.

This used to poison the standalone build: the cache keyed only on filename and
mtime, so it trusted the prefixed file and asked the linker for ``op0_add.o``,
which a standalone build never produces. ``PythonGeneratedMLIRArtifact`` now
keys its own availability on a recipe hash of the generator's current kwargs
(see ``mlir_recipe_hash.py`` for the device-free unit tests of that
mechanism), so the standalone build detects the mismatch and regenerates
unprefixed MLIR in place, regardless of what filename either build used.

The failure is far from its cause: it surfaces as an undefined symbol at link
time, in a build that did nothing wrong, possibly in a different process or
session from the fused build that poisoned it.

Needs a device: both builds run for real, because the whole point is what
lands on disk.
"""

import re
from pathlib import Path

import pytest

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.capture import capture
from iron.common.context import AIEContext
from iron.operators import ElementwiseAdd

SIZE = 1024
TILE = 128


@pytest.fixture(autouse=True)
def device():
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)


def _operator():
    return ElementwiseAdd(size=SIZE, tile_size=TILE, context=AIEContext())


def _linked_objects(operator):
    """What the operator's own MLIR tells the linker to bring in."""
    operator.compile()
    mlir = next(
        a.filename
        for a in operator.artifacts.bfs()
        if str(a.filename).endswith(".mlir")
    )
    return sorted(set(re.findall(r'link_with\s*=\s*"([^"]+)"', Path(mlir).read_text())))


def test_fused_build_does_not_poison_the_standalone_mlir():
    """Build fused, then standalone, and check the standalone is unprefixed.

    Order matters: the standalone build has to come second, since it is the
    one reading what the fused build left behind. Doing it the other way round
    passes whatever happens.
    """
    with capture() as graph:
        x = graph.input("x")
        w = graph.input("w")
        graph(_operator(), x, w)
    graph.build("poisoning_probe", dispatch="fused").compile()

    linked = _linked_objects(_operator())
    assert not any(name.startswith("op") for name in linked), (
        f"standalone build links {linked}; a fused build left its symbol-"
        "prefixed MLIR in the standalone operator's cache slot, and nothing "
        "about the filename distinguishes the two"
    )
