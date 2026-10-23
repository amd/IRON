# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator's array does not depend on its extents.

One array serves every extent: the core
programs an array compiles to must be the same bytes whether the operator
is built for one extent or twice it, with the same tunables. Each case
compiles an operator at two extents (the real build: an insts-only
lowering compiles no core) and compares the per-core ELFs the build
leaves, byte for byte. Compiles are cheap enough for this to run
device-free. A composition of the two extents
holds one device, so their sequences run on one configured array.
"""

import importlib
import re

import pytest

from aie.iron import Out
from iron import Precision
from iron.common.design import OperatorDesign
from iron.common.graph.record import Recording
from iron.common.image.coresidence import Packing
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.tests.support import sequences
from iron.tests.support.tools import requires

pytestmark = requires("aiecc", "peano")

# (module, class, tunables, the extent doubled). Every tunable the array could
# resolve from the extent is given, so only the extent differs. Copy is a
# memtile pass-through with no core, so nothing of its is compiled per
# extent.
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
    (
        "softmax",
        "Softmax",
        dict(rows=16, block=64, streamed=True, num_aie_columns=2),
        ("cols", 128),
    ),
    ("rope", "RoPE", dict(cols=64, num_aie_columns=2), ("rows", 16)),
    (
        "gemv",
        "GEMV",
        dict(K=64, num_aie_columns=2, tile_size_input=2, tile_size_output=2),
        ("M", 256),
    ),
    (
        "gemm",
        "GEMM",
        dict(K=64, N=512, num_aie_columns=4, precision=Precision.MEDIUM),
        ("M", 256),
    ),
]


def _core_elfs(op) -> dict[str, bytes]:
    """The per-core ELFs of an operator's build, by core.

    Built past the cache: a cached build shares each device's compiled cores
    across designs, and an entry that reused them holds no core ELF.
    """
    design = OperatorDesign(op.xclbin_operator(), full_elf=False).compile(
        use_cache=False
    )
    entry = design.get_cache_entry()
    assert entry is not None
    elfs = {
        p.parent.name: p.read_bytes()
        for p in sorted(entry.directory.glob("elfs_*_core_*/*.elf"))
    }
    assert elfs, f"{op.name}: the build left no core ELFs in {entry.directory}"
    return elfs


@pytest.mark.parametrize(
    "module,cls_name,tunables,extent",
    PAIRS,
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_the_array_is_the_same_at_two_extents(
    device, module, cls_name, tunables, extent
):
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    name, n = extent
    elfs = []
    for size in (n, 2 * n):
        elfs.append(_core_elfs(cls(**tunables, **{name: size}).resolved(device)))
    small, large = elfs
    assert small.keys() == large.keys(), "the same cores"
    differing = [core for core in small if small[core] != large[core]]
    assert (
        not differing
    ), f"{cls_name}: cores {differing} compile differently at {name}={n} and {2 * n}"


@pytest.mark.parametrize(
    "module,cls_name,tunables,extent",
    PAIRS,
    ids=lambda v: v if isinstance(v, str) else "",
)
def test_the_extents_share_one_device(npu2, module, cls_name, tunables, extent):
    cls = getattr(importlib.import_module(f"iron.operators.{module}"), cls_name)
    name, n = extent
    ops = [cls(**tunables, **{name: size}).resolved(npu2) for size in (n, 2 * n)]
    runlist, inputs, outputs = [], [], []
    for k, op in enumerate(ops):
        names = [f"s{k}_{b.name}" for b in op.buffers]
        runlist.append((op, *names))
        for b, buf in zip(op.buffers, names):
            (outputs if b.role is Out else inputs).append(buf)
    recording = Recording.of_steps(cls_name, sequences.steps(*runlist), inputs, outputs)
    seq = Image(recording, FullELF())
    seq._prepare()
    composed = Composition(seq)
    pack = Packing.device_name(list(composed.designs))
    devices = re.findall(r"^  aie\.device\(\w+\) @(\w+) \{$", composed.text(), re.M)
    assert devices == [pack]
