# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON: operators for the NPU, and graphs over them.

``iron.Graph``, ``iron.state``, ``iron.weight``, ``iron.carry``, ``iron.clamp``,
``iron.CarriedLoop``, the per-call value annotations, ``Precision`` and ``Profile`` are
imported on first use, so ``import iron`` stays light.
"""

import importlib
from typing import TYPE_CHECKING

if TYPE_CHECKING:  # the same names, for a checker; the runtime loads them lazily
    from .common.declare import Precision, Profile
    from .common.graph import (
        Carried,
        CarriedLoop,
        CompiledGraph,
        Graph,
        Scratchpad,
        carry,
        clamp,
        state,
        weight,
    )

_LAZY = {
    "Graph": "iron.common.graph",
    "state": "iron.common.graph",
    "weight": "iron.common.graph",
    "carry": "iron.common.graph",
    "clamp": "iron.common.graph",
    "CarriedLoop": "iron.common.graph",
    "CompiledGraph": "iron.common.graph",
    "Scratchpad": "iron.common.graph",
    "Carried": "iron.common.graph",
    "Precision": "iron.common.declare",
    "Profile": "iron.common.declare",
}

__all__ = [
    "Carried",
    "CarriedLoop",
    "CompiledGraph",
    "Graph",
    "Precision",
    "Profile",
    "Scratchpad",
    "carry",
    "clamp",
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
