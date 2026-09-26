# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A fused image names its kernels, its devices and itself by content.

Each is what lets one build reuse another's work: a kernel object shared by
the designs (and graphs) whose recipes agree, a device aiecc has placed
before, a whole image found without fusing it again. A name derived from a
position instead (which step a design is, where a kernel's design sits)
compiles once per position and moves when a graph gains a step.

No toolchain and no NPU: the fused text and the key are generated in
process, and the one cross-process check runs a second interpreter.
"""

import re
import subprocess
import sys
from pathlib import Path

import aie.utils as aie_utils
import pytest
from aie.iron.device import from_name

from iron.common.image import OperatorSequence, build_fused_mlir
from iron.common.image.fused import fused_identity, fused_plan
from iron.operators.gemv.op import GEMV


def _bind_npu2():
    aie_utils.set_current_device(from_name("npu2", n_cols=8))


pytestmark = pytest.mark.usefixtures("npu2")  # a bound device, restored


def _sequence(shapes):
    """One GEMV per ``(M, K)``, each on its own buffers."""
    runlist = [
        (GEMV(M=m, K=k), f"w{i}", f"x{i}", f"y{i}") for i, (m, k) in enumerate(shapes)
    ]
    seq = OperatorSequence(
        name="fused_identity_probe",
        runlist=runlist,
        input_args=[b for _, w, x, _ in runlist for b in (w, x)],
        output_args=[y for *_, y in runlist],
        dispatch="fused",
    )
    seq.subbuffer_layout, seq.buffer_sizes, seq.slice_info = (
        seq.calculate_buffer_layout()
    )
    return seq


def _identity(shapes):
    seq = _sequence(shapes)
    return fused_identity(seq, fused_plan(seq))


SHAPES = [(512, 1024), (256, 1024), (512, 2048)]


def _objects_by_step(shapes):
    """Each step's device name and the kernel objects that device links."""
    seq = _sequence(shapes)
    plan = fused_plan(seq)
    text = build_fused_mlir(seq, plan)
    devices = re.split(r"(?=aie\.device\()", text)
    linked = {}
    for body in devices:
        name = re.match(r"aie\.device\(\w+\) @(\w+)", body)
        if name:
            linked[name.group(1)] = set(re.findall(r'link_with\s*=\s*"([^"]+)"', body))
    return [(name, linked[name]) for name, *_ in plan[1]]


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
