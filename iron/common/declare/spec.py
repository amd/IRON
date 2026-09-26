# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator class built from an exported description, at run time."""

from __future__ import annotations

import types
from typing import Any, Callable

from ml_dtypes import bfloat16

from .field import param
from .member import In, Out
from .operator import Operator


def from_spec(
    name: str,
    *,
    inputs: dict[str, tuple[int, ...]],
    outputs: dict[str, tuple[int, ...]],
    dtype: Any = bfloat16,
    key: str = "",
    params: dict[str, Any] | None = None,
    generator: Callable | None = None,
) -> type:
    """An operator class from an exported description, at run time.

    For a design whose shapes come from a file rather than a formula
    (swiglu_prefill_stream's stream-dse export). ``inputs``
    and ``outputs`` are literal shapes in argument order; ``params`` are
    the numbers that identify the instance (they become ``param()`` fields
    with those defaults and reach the name); ``key`` identifies the
    generated design, for sharing; ``generator`` replaces
    :meth:`Operator.generator`, since the sequence is not derived. A class
    made this way goes through the same creation checks as one written in
    a class body.
    """

    def operator_ns(ns):
        ns["__module__"] = Operator.__module__
        ns["__annotations__"] = {"key": str}
        ns["key"] = param(default=key, repr=False)
        for pname, value in (params or {}).items():
            ns["__annotations__"][pname] = type(value)
            ns[pname] = param(default=value)
        for bname, shape in inputs.items():
            ns[bname] = In(*shape, dtype=dtype)
        for bname, shape in outputs.items():
            ns[bname] = Out(*shape, dtype=dtype)
        ns["design_key"] = lambda self: self.key or None
        if generator is not None:
            ns["generator"] = generator

    return types.new_class(name, (Operator,), {}, operator_ns)
