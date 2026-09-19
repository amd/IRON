#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A kernel object's on-disk path must be unique per target arch.

KernelCompilationRule.compile() passes a different --target and
aie_runtime_lib -I per arch for the same output filename (e.g. "mul.o"), and
for aie_kernels/generic/ sources the very same input file compiles to
different machine code per arch. CompilationArtifact.is_available_in_filesystem()
only ever compares mtimes and never records which arch an object was built
for, so if two arches' objects resolve to the same build_dir path, whichever
was compiled last is silently handed to the other arch's link step. This is
what happened in production: an npu1 (aie2) build's mul.o was reused by a
following npu2 (aie2p) run in the same build/, producing bogus ElementwiseMul
failures. These tests build the real artifact graph for both arches and
assert their kernel object paths never collide.
"""

from pathlib import Path

import aie.utils as aie_utils
from aie.iron.device import NPU1, NPU2

from iron.common import AIEContext
from iron.common.compilation import CompilationArtifactGraph, KernelObjectArtifact
from iron.common.compilation.base import _link_build_outputs_into


def _mul_kernel_object(build_dir, device):
    """Resolve a kernel object's build_dir path for `device`.

    The graph is built here rather than taken from an operator. This is a
    property of move_artifacts, not of any operator, and every operator that
    used to serve as the vehicle has since moved its kernels to
    ExternalFunction and stopped producing an artifact to test -- twice, so
    far. Upstream keys such an object on content and on device identity, so
    the collision below is unrepresentable there; these tests guard what is
    left on the artifact path, and retire with it.
    """
    aie_utils.set_current_device(device)
    ctx = AIEContext(build_dir=build_dir)
    artifact = KernelObjectArtifact("mul.o", dependencies=[])
    graph = CompilationArtifactGraph([artifact])
    graph.move_artifacts(str(ctx.build_dir))
    graph.populate_availability_from_filesystem()
    return artifact


def test_two_arches_do_not_resolve_the_same_kernel_object_path(tmp_path):
    """aie_kernels/generic/mul.cc is one source shared by aie2 and aie2p
    (ElementwiseMul.kernel_subdir); its object must not collide in build_dir."""
    aie2 = _mul_kernel_object(tmp_path, NPU1())
    aie2p = _mul_kernel_object(tmp_path, NPU2())
    assert aie2.filename != aie2p.filename


def test_a_stale_object_from_one_arch_is_not_silently_reused_by_another(tmp_path):
    """Reproduces the production incident: plant a real leftover aie2 object,
    then check the following aie2p build does not report it available."""
    aie2 = _mul_kernel_object(tmp_path, NPU1())
    Path(aie2.filename).parent.mkdir(parents=True, exist_ok=True)
    Path(aie2.filename).write_bytes(b"aie2-machine-code")

    aie2p = _mul_kernel_object(tmp_path, NPU2())

    assert not aie2p.is_available_in_filesystem(), (
        "aie2p build reused a leftover aie2 kernel object -- both resolved "
        f"to {aie2p.filename}"
    )


def test_the_arch_scoped_object_is_linked_into_the_aiecc_work_dir(tmp_path):
    """Scoping the object under build_dir/<arch> must not hide it from the
    link step. aiecc resolves link_with="mul.o" against its own work_dir, fed
    by _link_build_outputs_into(), which skips directories -- so an object
    moved into a subdirectory stops being linked and ld.lld fails with
    "cannot open .../mul.o: No such file or directory"."""
    obj = _mul_kernel_object(tmp_path, NPU2())
    Path(obj.filename).parent.mkdir(parents=True, exist_ok=True)
    Path(obj.filename).write_bytes(b"aie2p-machine-code")

    work_dir = tmp_path / "design.mlir.d"
    work_dir.mkdir()
    _link_build_outputs_into(work_dir, tmp_path)

    linked = work_dir / Path(obj.filename).name
    assert linked.exists(), (
        f"{Path(obj.filename).name} was not linked into the aiecc work dir; "
        f"the object is at {obj.filename}"
    )
    assert linked.read_bytes() == b"aie2p-machine-code"
