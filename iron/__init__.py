# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""IRON: operators for the NPU, and graph functions over them.

``iron.graph`` and ``iron.state`` are imported on first use, so ``import
iron`` stays light.
"""

import importlib

_LAZY = {
    "graph": "iron.common.graph",
    "state": "iron.common.graph",
    "GraphFunction": "iron.common.graph",
    "CompiledGraph": "iron.common.graph",
    "each_step": "iron.common.image.packaging",
    "ELF": "iron.common.image.packaging",
    "XCLBIN": "iron.common.image.packaging",
}

__all__ = sorted(_LAZY)


def __getattr__(name):
    module = _LAZY.get(name)
    if module is None:
        raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
    return getattr(importlib.import_module(module), name)
