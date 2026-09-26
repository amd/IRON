# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's array does not depend on its extents (C11).

One array serves every extent (OPERATOR_MODEL_PLAN.md §3): the core
programs an array compiles to must be the same bytes whether the operator
is built for one extent or twice it, with the same knobs. Each case
compiles an operator at two extents (the real build: an insts-only
lowering compiles no core) and compares the per-core ELFs the build
leaves, byte for byte. Compiles are cheap enough for this to run
device-free, and the cache keeps a repeat quick.
"""

import importlib

import pytest

from iron.common import Incompatible, Unresolvable
from iron.tests.toolchain.tools import requires

pytestmark = requires("aiecc")

# (module, class, knobs, the extent doubled). Every knob the array could
# resolve from the extent is given, so only the extent differs. Repeat and
# Copy are memtile pass-throughs with no core, so nothing of theirs is
# compiled per extent.
PAIRS = [
    (
        "relu",
        "ReLU",
        dict(num_aie_columns=1, num_channels=1, tile_size=256),
        ("size", 1024),
    ),
    (
        "elementwise_add",
        "ElementwiseAdd",
        dict(tile_size=256, num_aie_columns=1),
        ("size", 2048),
    ),
    ("softmax", "Softmax", dict(cols=64, num_aie_columns=2), ("rows", 16)),
    ("rope.op", "RoPE", dict(cols=64, num_aie_columns=2), ("rows", 16)),
    (
        "gemv.op",
        "GEMV",
        dict(K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=2),
        ("M", 256),
    ),
    ("gemm.op", "GEMM", dict(K=64, N=512, num_aie_columns=4), ("M", 256)),
]


def _core_elfs(op) -> dict[str, bytes]:
    """The per-core ELFs of an operator's build, by core."""
    entry = op.compile().artifacts.entry
    assert entry is not None
    elfs = {
        p.parent.name: p.read_bytes()
        for p in sorted(entry.directory.glob("elfs_*_core_*/*.elf"))
    }
    assert elfs, f"{op.name}: the build left no core ELFs in {entry.directory}"
    return elfs


@pytest.mark.parametrize(
    "module,cls_name,knobs,extent",
    PAIRS,
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_the_array_is_the_same_at_two_extents(
    device, module, cls_name, knobs, extent, tmp_path, monkeypatch
):
    # A cache of its own: an entry another test left for the same design,
    # an insts-only lowering's say, holds no core ELF.
    from aie.utils.compile.jit import compilabledesign

    monkeypatch.setattr(compilabledesign, "NPU_CACHE_HOME", tmp_path)
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    name, n = extent
    elfs = []
    for size in (n, 2 * n):
        try:
            op = cls(**knobs, **{name: size}).resolved(device)
        except (ValueError, Unresolvable, Incompatible) as e:
            pytest.skip(f"not for {device.resolve().name}: {e}")
        elfs.append(_core_elfs(op))
    small, large = elfs
    assert small.keys() == large.keys(), "the same cores"
    differing = [core for core in small if small[core] != large[core]]
    assert (
        not differing
    ), f"{cls_name}: cores {differing} compile differently at {name}={n} and {2 * n}"
