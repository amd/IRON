# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a declared class goes through once its body has run.

``Operator`` calls ``declare`` from ``__init_subclass__``, so every
subclass is processed and none can forget to be. It applies ``dataclass``,
resolves the field objects the class body captured in its shapes to names,
re-attaches every field as a ``DimRef``, checks the shape rule, and
records the members in declaration order. Checking an operator's extents
against its resolved tunables needs an instance, so that is left to
``Operator.compatible``.
"""

from __future__ import annotations

import dataclasses

from .field import Auto, DimRef, OptionalDim, Param, Shape, Tier
from .member import Extent, _Buffer, _Member


def members_of(cls: type) -> list[_Member]:
    """Members declared in this class body and its declared bases, in order.

    The most derived class's body order wins for the members it declares;
    inherited members it does not redeclare follow, in their own order. So a
    subclass that inserts a buffer between two inherited ones (a weight
    between an input and an output) gets the order it wrote. A member the
    subclass sets to ``None`` is hidden.
    """
    ordered: dict[str, _Member] = {}
    seen: set[str] = set()
    for klass in cls.__mro__:
        for name, value in vars(klass).items():
            if name in seen:
                continue
            seen.add(name)
            # A subclass hides an inherited member by assigning it None: a
            # shipped image keeps the port's fields and operands but not its
            # values, whose block the image lays out differently.
            if isinstance(value, _Member):
                ordered[name] = value
    return list(ordered.values())


def declare(cls: type) -> None:
    """Process a freshly created ``Operator`` subclass.

    Equality is identity; the base defines its own ``repr``.
    """
    # Members must be unannotated, or dataclass would make them constructor args.
    annotations = cls.__dict__.get("__annotations__", {})
    for name, value in list(vars(cls).items()):
        if isinstance(value, _Member) and name in annotations:
            raise TypeError(
                f"{cls.__name__}.{name}: members are declared without an "
                f"annotation; annotating one turns it into a constructor argument"
            )
        if not isinstance(value, _Member):
            continue
        base = next((b for b in cls.__mro__[1:] if name in vars(b)), None)
        if base is not None and not isinstance(vars(base)[name], _Member):
            raise TypeError(
                f"{cls.__name__}.{name} hides {base.__name__}.{name}, which "
                f"the library reads; name the member otherwise"
            )

    inherited = {
        f.name
        for base in cls.__mro__[1:]
        if dataclasses.is_dataclass(base)
        for f in dataclasses.fields(base)
    }
    for name, value in list(vars(cls).items()):
        if (
            name in inherited
            and name not in annotations
            and value is not None
            and not isinstance(value, _Member)
            and not callable(value)
            and not isinstance(value, (property, classmethod, staticmethod))
        ):
            raise TypeError(
                f"{cls.__name__}.{name} = {value!r} does not override the inherited "
                f"field: annotate it, `{name}: int = auto({value!r})` (with "
                f"init=False to pin it), or dataclass keeps the base's default"
            )

    dataclasses.dataclass(cls, eq=False, repr=False, kw_only=True)  # in place

    # dataclass names the Field objects the class body bound to bare names,
    # so a shape that captured one is rewritten by name (Shape.rewrite).
    fields = {f.name: f for f in dataclasses.fields(cls)}
    for f in fields.values():
        setattr(cls, f.name, DimRef(cls, f.name, f.metadata.get(Tier), f.default))

    members = members_of(cls)
    for m in members:
        if m.owner is not cls:
            continue  # inherited; already processed on its own class
        if isinstance(m, _Buffer):
            m.shape = m.shape.rewrite(cls)
            (m.dtype,) = Shape((m.dtype,)).rewrite(cls).dims
            m.shape.check(cls, m, "dimension", allow_tunable=False)
            if m.tile is not None:
                m.tile = m.tile.rewrite(cls)
                m.tile.check(cls, m, "tile dimension", allow_tunable=True)
            if m.finish_block is not None:
                m.finish_block = m.finish_block.rewrite(cls)
                m.finish_block.check(
                    cls, m, "finish block dimension", allow_tunable=True
                )
            if sum(isinstance(d, OptionalDim) for d in m.shape.dims) > 1:
                raise TypeError(
                    f"{cls.__name__}.{m.name}: at most one OptionalDim() dimension, "
                    f"since the rank tells whether it is present"
                )
            if m.when is not None:
                (m.when,) = Shape((m.when,)).rewrite(cls).dims
                if not isinstance(m.when, DimRef) or not isinstance(m.when.tier, Param):
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: when={m.when!r} must be a "
                        f"param() field, the flag the operand exists under"
                    )
        if isinstance(m, Extent):
            (ref,) = Shape((m.field,)).rewrite(cls).dims
            if not isinstance(ref, DimRef) or not isinstance(ref.tier, Param):
                raise TypeError(
                    f"{cls.__name__}.{m.name}: Extent({ref!r}) must name a param() "
                    f"field, the one a graph may bound per call"
                )
            m.field = ref
        if isinstance(m, _Buffer) and m.tile is not None and m.per is not None:
            m.per = m.per.rewrite(cls)
            for ref in m.per.dims:
                if not isinstance(ref, DimRef) or ref.tier is None:
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: per={ref!r} must be a param() or auto() field"
                    )

    cls._members = tuple(members)
    tiers = {f.name: f.metadata.get(Tier) for f in fields.values()}
    cls._param_fields = tuple(n for n, t in tiers.items() if isinstance(t, Param))
    cls._derived_params = {
        n: t.derive for n, t in tiers.items() if isinstance(t, Param) and t.derive
    }
    cls._auto_fields = tuple(n for n, t in tiers.items() if isinstance(t, Auto))
    cls._tunable_fields = tuple(
        n
        for n in cls._auto_fields
        if fields[n].init and not fields[n].metadata[Tier].derived
    )
    # The array tier: what a stream's tile, a core's block of it, its dtype,
    # its replication or its presence names, and what declares itself array=True.
    named: set[str] = set()
    for m in members:
        if isinstance(m, _Buffer) and m.tile is not None:
            named |= m.tile.names()
            if m.finish_block is not None:
                named |= m.finish_block.names()
            if m.per is not None:
                named |= m.per.names()
            if isinstance(m.dtype, DimRef):
                named.add(m.dtype.name)
            if m.when is not None:
                named.add(m.when.name)
    cls._array_fields = tuple(
        n for n, t in tiers.items() if n in named or (t is not None and t.array)
    )
