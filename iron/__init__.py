# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON: operators for the NPU, and graph functions over them.

``iron.graph``, ``iron.state``, the per-call value annotations and
``Profile`` are imported on first use, so ``import iron`` stays light.
"""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # the same names, for a checker; the runtime loads them lazily
    from .common.declare import DispatchTime, Profile, Scratchpad
    from .common.graph import CompiledGraph, GraphFunction, graph, state
    from .common.image.packaging import ELF, XCLBIN, each_step

_LAZY = {
    "graph": "iron.common.graph",
    "state": "iron.common.graph",
    "GraphFunction": "iron.common.graph",
    "CompiledGraph": "iron.common.graph",
    "each_step": "iron.common.image.packaging",
    "ELF": "iron.common.image.packaging",
    "XCLBIN": "iron.common.image.packaging",
    "Scratchpad": "iron.common.declare",
    "DispatchTime": "iron.common.declare",
    "Profile": "iron.common.declare",
}

__all__ = [
    "CompiledGraph",
    "DispatchTime",
    "ELF",
    "GraphFunction",
    "Profile",
    "Scratchpad",
    "XCLBIN",
    "each_step",
    "graph",
    "state",
]
assert sorted(__all__) == sorted(_LAZY)


def __getattr__(name):
    module = _LAZY.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(module), name)
