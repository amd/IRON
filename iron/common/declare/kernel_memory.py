# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a core's kernels hold in its memory, read from their compiled objects."""

from __future__ import annotations

import tempfile
from pathlib import Path

from aie.iron import ExternalFunction, Kernel
from aie.utils.compile import NPU_CACHE_HOME
from aie.utils.compile.jit._object_cache import KernelObjectCache
from aie.utils.compile.jit.compilabledesign import COMPILE_LOCK_TIMEOUT_SECONDS
from aie.utils.compile.readobj import linked
from aie.utils.compile.utils import compile_external_kernel, resolve_target_arch

# The deepest frames below each kernel, by (object, symbol, arch).
_frames: dict[tuple[str, str, str], int] = {}


def _built(func: ExternalFunction, arch: str, directory: str) -> Path:
    """``func``'s object in ``directory``, through the store a design's build shares."""
    compile_external_kernel(
        func,
        directory,
        arch,
        object_cache=KernelObjectCache(
            NPU_CACHE_HOME / "objects", COMPILE_LOCK_TIMEOUT_SECONDS
        ),
    )
    return Path(directory) / func.object_file_name


def core_stack(dev, *calls: Kernel | None, objects: tuple = ()) -> int:
    """The stack aiecc reserves at most for a core of ``dev`` calling ``calls``.

    The device's default stack covers the core's own frame; the deepest
    kernel's frames go on top, read from its object's ``.stack_sizes``. A
    kernel's object is built through the store a design's build shares, so
    that build then hits it.

    Args:
        dev: The device the core runs on.
        *calls: What the core calls; None is skipped.
        objects: The ``ExternalFunction`` that builds each object a bound
            ``Kernel`` of ``calls`` names; an ``ExternalFunction`` call builds
            its own.
    """
    arch = resolve_target_arch(dev)
    calls = tuple(k for k in calls if k is not None)
    builds = {
        f.object_file_name: f
        for f in (*objects, *calls)
        if isinstance(f, ExternalFunction)
    }
    deepest = 0
    with tempfile.TemporaryDirectory() as tmp:
        for k in calls:
            if k.stack_size_override is not None:
                deepest = max(deepest, k.stack_size_override)
                continue
            key = (k.object_file_name, k.name, arch)
            if key not in _frames:
                obj = _built(builds[k.object_file_name], arch, tmp)
                _frames[key] = linked(obj, k.name).stack or 0
            deepest = max(deepest, _frames[key])
    return dev.default_core_stack_bytes + deepest
