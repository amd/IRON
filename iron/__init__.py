# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON: operators for the NPU, and graphs over them.

``iron.Graph``, ``iron.state``, ``iron.weight``, ``iron.carry``,
``iron.CarriedLoop``, the per-call value annotations and ``Profile`` are
imported on first use, so ``import iron`` stays light.
"""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # the same names, for a checker; the runtime loads them lazily
    from .common.declare import Carried, DispatchTime, Profile, Scratchpad
    from .common.graph import CarriedLoop, CompiledGraph, Graph, carry, state, weight
    from .common.image.packaging import ELF, XCLBIN, each_step

_LAZY = {
    "Graph": "iron.common.graph",
    "state": "iron.common.graph",
    "weight": "iron.common.graph",
    "carry": "iron.common.graph",
    "CarriedLoop": "iron.common.graph",
    "CompiledGraph": "iron.common.graph",
    "each_step": "iron.common.image.packaging",
    "ELF": "iron.common.image.packaging",
    "XCLBIN": "iron.common.image.packaging",
    "Scratchpad": "iron.common.declare",
    "Carried": "iron.common.declare",
    "DispatchTime": "iron.common.declare",
    "Profile": "iron.common.declare",
}

__all__ = [
    "Carried",
    "CarriedLoop",
    "CompiledGraph",
    "DispatchTime",
    "ELF",
    "Graph",
    "Profile",
    "Scratchpad",
    "XCLBIN",
    "carry",
    "each_step",
    "state",
    "weight",
]
assert sorted(__all__) == sorted(_LAZY)


def __getattr__(name):
    module = _LAZY.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(module), name)


def __dir__():
    return sorted(set(globals()) | set(_LAZY))
