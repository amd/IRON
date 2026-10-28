# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON: operators for the NPU, and graphs over them.

Its names are imported on first use, so ``import iron`` stays light.
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
        on_host,
        param,
        state,
        weight,
    )

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
    "on_host",
    "param",
    "state",
    "weight",
]
# Each name's module, loaded on first use.
_LAZY = dict.fromkeys(__all__, "iron.common.graph") | dict.fromkeys(
    ["Precision", "Profile"], "iron.common.declare"
)


def __getattr__(name):
    module = _LAZY.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(module), name)


def __dir__():
    return sorted(set(globals()) | set(_LAZY))
