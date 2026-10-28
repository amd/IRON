# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A full ELF names its kernels, its devices and itself by content, not
by position, so one build reuses another's work. No toolchain and no NPU.
"""

import re
import subprocess
import sys
from pathlib import Path

import aie.utils as aie_utils
import pytest
from aie.iron.device import from_name

from iron.common.design import OperatorDesign
from iron.common.graph.record import Recording
from iron.common.image.compose import Composition
from iron.common.image.link import FullELF
from iron.common.image.sequence import Image
from iron.common.image.step import BufferRef, SequenceStep
from iron.operators import ReLU
from iron.operators.gemv import GEMV


def _bind_npu2():
    aie_utils.set_current_device(from_name("npu2", n_cols=8))


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _sequence(shapes):
    """One GEMV per ``(M, K)``, each on its own buffers."""
    steps = [
        SequenceStep(GEMV(M=m, K=k), tuple(map(BufferRef, (f"w{i}", f"x{i}", f"y{i}"))))
        for i, (m, k) in enumerate(shapes)
    ]
    seq = Image(
        Recording.of_steps(
            "composition_identity_probe",
            steps,
            [f"{b}{i}" for i in range(len(shapes)) for b in "wx"],
            [f"y{i}" for i in range(len(shapes))],
        ),
        FullELF(),
    )
    seq._prepare()
    return seq


def _identity(shapes):
    return Composition(_sequence(shapes)).identity


SHAPES = [(512, 1024), (256, 1024), (512, 2048)]


def _objects_by_step(shapes):
    """Each step's design name and the kernel objects its device links."""
    composition = Composition(_sequence(shapes))
    devices = re.split(r"(?=aie\.device\()", composition.text())
    linked = {}
    for body in devices:
        name = re.match(r"aie\.device\(\w+\) @(\w+)", body)
        if name:
            objects = set(re.findall(r'link_with\s*=\s*"([^"]+)"', body))
            # A device several designs share names each one's sequence.
            for design in [
                name.group(1),
                *re.findall(r"runtime_sequence @(\w+)", body),
            ]:
                linked[design] = objects
    return [(name, linked[name]) for name, _ in composition.steps]


def test_equal_kernel_recipes_share_one_object_across_designs():
    """Two GEMVs that differ only in M compile mv.cc with the same flags,
    so their designs link one object; a different K is a different recipe,
    and a different object.
    """
    (_, a), (_, b), (_, c) = _objects_by_step(SHAPES)
    assert a and a == b, f"M=512 links {a}, M=256 links {b}: one recipe, two objects"
    assert a.isdisjoint(c), f"K=1024 and K=2048 both link {a & c}"


def test_devices_are_named_for_their_design_not_their_step():
    """A design is the same device at any step of any sequence."""
    alone = _objects_by_step(SHAPES[2:])
    shifted = _objects_by_step(SHAPES)
    assert alone[0][0] == shifted[2][0]
    assert len({name for name, _ in shifted}) == 3


def test_identity_is_what_the_text_is_a_function_of():
    """Equal sequences have one identity; a changed shape or order a new one."""
    assert _identity(SHAPES) == _identity(SHAPES)
    assert _identity(SHAPES) != _identity([(512, 1024), (256, 1024), (512, 4096)])
    assert _identity(SHAPES) != _identity(SHAPES[::-1])


def test_two_designs_whose_device_names_collide_are_refused():
    """A device is named by eight hex digits of its design's identity, so two
    designs can share one; the composition refuses rather than run one design for both.
    """
    seen = {}
    for size in range(1024, 1024 * 200_000, 1024):
        op = ReLU(size=size, num_aie_columns=1, num_channels=1, tile_size=1024)
        # Resolved, as the composition names it: the device is in its key.
        name = OperatorDesign(op.resolved()).name
        if name in seen:
            break
        seen[name] = op
    else:
        pytest.fail("no two ReLU sizes up to 200k tiles share a device name")
    seq = Image(
        Recording.of_steps(
            "colliding_names",
            [
                SequenceStep(seen[name], (BufferRef("x0"), BufferRef("y0"))),
                SequenceStep(op, (BufferRef("x1"), BufferRef("y1"))),
            ],
            ["x0", "x1"],
            ["y0", "y1"],
        ),
        FullELF(),
    )
    seq._prepare()
    with pytest.raises(ValueError, match=f"device names collide, {name}"):
        Composition(seq)


def test_identity_holds_across_processes():
    """The key a warm process computes is the one the cold process stored.

    An object address or a hash-seeded ordering anywhere in it would pass
    every in-process check and still miss the cache on every run.
    """
    here = Path(__file__)
    script = (
        "import importlib.util, sys\n"
        f"spec = importlib.util.spec_from_file_location('probe', {str(here)!r})\n"
        "probe = importlib.util.module_from_spec(spec)\n"
        "spec.loader.exec_module(probe)\n"
        "probe._bind_npu2()\n"
        "print(probe._identity(probe.SHAPES))\n"
    )
    other = subprocess.run(
        [sys.executable, "-c", script],
        capture_output=True,
        text=True,
        check=True,
    )
    assert other.stdout.strip().splitlines()[-1] == _identity(SHAPES)
