# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Operand shapes to dimension fields: the lookup a declaration makes possible.

A host buffer's dimension is a :func:`~iron.common.declare.param` field or an
integer literal (see the package docstring), so binding an operator to its
operands is a lookup over the declared members, not a solver. The functions
take the class because that is all they read: its members, its fields, and
its name for error messages.
"""

from __future__ import annotations

import dataclasses
from dataclasses import MISSING
from typing import Any

import numpy as np

from .field import DimRef, _Optional, _Select
from .member import _Buffer


def infer(cls, *operand_shapes, outputs=(), **given) -> dict[str, Any]:
    """Bind dimension fields from operand shapes, in ``In`` declaration order.

    Each declared dimension is a field or a literal, so this is a lookup.
    Returns ``{field: value}``; ``given`` pins values and is checked for
    agreement. ``outputs`` are the shapes of caller-supplied ``Out`` buffers,
    in declaration order, which bind the same way.
    """
    ins = [
        m
        for m in cls._members
        if isinstance(m, _Buffer) and m.direction in ("in", "inout")
    ]
    if len(operand_shapes) != len(ins):
        raise TypeError(
            f"{cls.__name__} takes {len(ins)} operand(s) "
            f"({', '.join(m.name for m in ins)}), got {len(operand_shapes)}"
        )
    outs = [m for m in cls._members if isinstance(m, _Buffer) and m.direction == "out"]
    if outputs and len(outputs) != len(outs):
        raise TypeError(
            f"{cls.__name__} produces {len(outs)} output(s) "
            f"({', '.join(m.name for m in outs)}), got {len(outputs)}"
        )
    pairs = list(zip(ins, operand_shapes)) + list(zip(outs, outputs))
    bound: dict[str, Any] = dict(given)
    origin: dict[str, str] = {k: "given" for k in given}

    def bind(ref: DimRef, value: int, where: str) -> None:
        key = ref.name
        if key in bound and bound[key] != value:
            raise ValueError(
                f"{cls.__name__}: {ref!r} is {value} from {where} but "
                f"{bound[key]} from {origin[key]}"
            )
        bound[key] = value
        origin.setdefault(key, where)

    for m, shape in pairs:
        shape = tuple(int(s) for s in shape)
        dims = list(m.dims)
        at = next((i for i, d in enumerate(dims) if isinstance(d, _Optional)), None)
        if at is not None:
            optional = dims.pop(at)
            if len(shape) == len(dims) + 1:
                bind(optional.ref, shape[at], f"{m.name}.shape[{at}]")
                shape = shape[:at] + shape[at + 1 :]
            elif len(shape) == len(dims):
                bind(optional.ref, 1, f"{m.name} (rank {len(shape)})")
            else:
                raise ValueError(
                    f"{cls.__name__}: operand {m.name} has rank {len(shape)}, "
                    f"declared {m!r}"
                )
        expanded: list = []
        for d in dims:
            if isinstance(d, _Select):
                flag = d.flag
                if flag.name in bound:
                    value = bound[flag.name]
                else:
                    fld = next(
                        (
                            f
                            for f in dataclasses.fields(flag.owner)
                            if f.name == flag.name
                        ),
                        None,
                    )
                    if fld is None or fld.default is MISSING:
                        raise ValueError(
                            f"{cls.__name__}: {flag!r} selects {m.name}'s shape and "
                            f"has no default; pass it explicitly"
                        )
                    value = fld.default
                expanded.extend(d.when_true if value else d.when_false)
            else:
                expanded.append(d)
        dims = expanded
        if len(dims) == 1 and len(shape) != 1:
            # A flat buffer takes an operand of any rank: its one
            # dimension is the element count.
            shape = (int(np.prod(shape)) if shape else 1,)
        if len(shape) != len(dims):
            raise ValueError(
                f"{cls.__name__}: operand {m.name} has rank {len(shape)} {shape}, "
                f"declared rank {len(dims)} {m!r}"
            )
        for i, (d, n) in enumerate(zip(dims, shape)):
            if isinstance(d, DimRef):
                bind(d, n, f"{m.name}.shape[{i}]")
            elif int(d) != n:
                raise ValueError(
                    f"{cls.__name__}: operand {m.name}.shape[{i}] is {n}, declared {d}"
                )
    return bound


def infer_kwargs(cls, kwargs) -> dict[str, Any]:
    """The part of ``kwargs`` that :func:`infer` takes: the dimension fields
    and the flags that select a buffer's shape.
    """
    names = set(cls._param_fields)
    for m in cls._members:
        if isinstance(m, _Buffer):
            names.update(d.flag.name for d in m.dims if isinstance(d, _Select))
    return {k: v for k, v in kwargs.items() if k in names}
