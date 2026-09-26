# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Labels for declared instances.

An operator's label follows it through a graph and into the symbols a host
writes through. Nothing on disk is keyed by it; the compile cache keys by
content.
"""

from __future__ import annotations

import dataclasses
from typing import Container

_NAME_ALIASES = {
    "num_aie_columns": "c",
    "num_channels": "ch",
    "tile_size": "t",
    "size": "sz",
    "scalar_factor": "sf",
    "rows": "r",
    "cols": "n",
}


def label_parts(obj, *, skip: Container[str] = ()) -> list[str]:
    """A declared instance's shown fields, as fragments of its label."""
    return [
        f"{_NAME_ALIASES.get(f.name, f.name)}{serialize_param(getattr(obj, f.name))}"
        for f in dataclasses.fields(obj)
        if f.name not in skip and f.repr and getattr(obj, f.name) is not None
    ]


def serialize_param(v: object) -> str:
    """A parameter value as a short, filesystem-safe token for labels."""
    if isinstance(v, bool):
        return str(int(v))
    if isinstance(v, float):
        return float_to_name(v)
    if isinstance(v, (list, tuple)):
        return "x".join(str(x) for x in v)
    return str(v)


def float_to_name(v: float) -> str:
    """Convert a float to a filesystem-safe string for use in operator names.

    Uses repr() for the shortest exact round-trip representation, then sanitizes
    characters that are problematic in filenames or shell scripts, for instance:
      '.' -> 'p'  (decimal point)
      '-' -> 'n'  (negative sign / negative exponent)
      '+' -> ''   (positive exponent, redundant)

    Examples:
      3.0   -> '3p0'
      0.01  -> '0p01'
      -0.5  -> 'n0p5'
      1e-10 -> '1en10'
    """
    return repr(v).replace(".", "p").replace("-", "n").replace("+", "")
