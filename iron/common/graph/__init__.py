# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Graphs: a ``Graph`` subclass's ``body`` traced on handles.

A ``Carried[T]`` value is one the graph computes for its own next call:
``return logits, iron.carry(pos=pos + 1)``; on a full ELF the device can
compute it and loop (``CarriedLoop``).
"""

from .carried import CarriedLoop
from .compiled import CompiledGraph, Graph
from .handle import Carried, Carry, Handle, Scratchpad, carry, state, weight

__all__ = [
    "Carried",
    "CarriedLoop",
    "Carry",
    "CompiledGraph",
    "Graph",
    "Handle",
    "Scratchpad",
    "carry",
    "state",
    "weight",
]
