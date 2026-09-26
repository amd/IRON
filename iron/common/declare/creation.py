# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a declared class goes through once its body has run.

:class:`Operator` calls :func:`declare` from ``__init_subclass__``, so every
subclass is processed and none can forget to be. It applies ``dataclass``,
resolves the field objects the class body captured in its shapes to names,
re-attaches every field as a :class:`DimRef`, checks the shape rule, and
records the members in declaration order. Checking an operator's extents
against its resolved knobs needs an instance, so that is left to
:meth:`Operator.compatible`.
"""

from __future__ import annotations

import dataclasses
from dataclasses import Field

import numpy as np

from .field import (
    _DERIVE,
    DeclarationError,
    DimRef,
    _declares_array,
    _Optional,
    _Select,
    _tier_of,
)
from .member import Extent, _Buffer, _Member, _Stream


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
    members = []
    for m in ordered.values():
        members.append(m)
        if isinstance(m, _Buffer) and m.stream is not None:
            members.append(m.stream)  # the buffer's own stream, right after it
    return members


def _rewrite_refs(specs: tuple, cls: type, fields_by_obj: dict[int, Field]) -> tuple:
    """Replace same-class Field objects in a member's dims with DimRefs."""
    out = []
    for spec in specs:
        if isinstance(spec, _Optional):
            out.append(_Optional(_rewrite_refs((spec.ref,), cls, fields_by_obj)[0]))
        elif isinstance(spec, _Select):
            out.append(
                _Select(
                    _rewrite_refs((spec.flag,), cls, fields_by_obj)[0],
                    _rewrite_refs(spec.when_true, cls, fields_by_obj),
                    _rewrite_refs(spec.when_false, cls, fields_by_obj),
                )
            )
        elif isinstance(spec, Field):
            f = fields_by_obj.get(id(spec))
            if f is None:
                raise DeclarationError(
                    f"{cls.__name__}: a shape references a field object that is "
                    f"not one of this class's fields"
                )
            out.append(getattr(cls, f.name))  # the DimRef re-attached to the class
        else:
            out.append(spec)
    return tuple(out)


def _check_dim_ref(
    cls: type, member: _Member, spec, what: str, *, allow_tunable: bool
) -> None:
    """The shape rule.

    A host buffer's dimension is a ``param()`` field or an integer: never an
    ``auto()`` (inference would cycle through tuning) and never an expression.
    A stream's tile dimension may also be an ``auto()``, since tuning chooses
    the tile and inference never reads a stream.
    """
    if isinstance(spec, _Optional):
        _check_dim_ref(cls, member, spec.ref, what, allow_tunable=allow_tunable)
        return
    if isinstance(spec, _Select):
        for d in spec.when_true + spec.when_false:
            _check_dim_ref(cls, member, d, what, allow_tunable=allow_tunable)
        return
    if isinstance(spec, bool):
        raise DeclarationError(
            f"{cls.__name__}.{member.name}: {spec!r} is not a {what}"
        )
    if isinstance(spec, (int, np.integer)):
        return
    if isinstance(spec, DimRef):
        allowed = ("param", "auto") if allow_tunable else ("param",)
        if spec.tier not in allowed:
            why = (
                "an auto(); a host shape may not depend on tuning"
                if spec.tier == "auto"
                else "not declared with param()"
            )
            raise DeclarationError(
                f"{cls.__name__}.{member.name}: {what} {spec!r} is {why}. A "
                f"shape dimension is a param() field or an integer literal"
            )
        return
    raise DeclarationError(
        f"{cls.__name__}.{member.name}: {what} {spec!r} is not a param() field or an "
        f"integer. Expressions are not allowed in shapes; declare the result as a field"
    )


def declare(cls: type) -> None:
    """Process a freshly created :class:`Operator` subclass.

    Equality is identity; the base defines its own ``repr``.
    """
    # Members must be unannotated, or dataclass would make them constructor args.
    annotations = cls.__dict__.get("__annotations__", {})
    for name, value in list(vars(cls).items()):
        if isinstance(value, _Member) and name in annotations:
            raise DeclarationError(
                f"{cls.__name__}.{name}: members are declared without an "
                f"annotation; annotating one turns it into a constructor argument"
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
            raise DeclarationError(
                f"{cls.__name__}.{name} = {value!r} does not override the inherited "
                f"field: annotate it, `{name}: int = auto({value!r})` (with "
                f"init=False to pin it), or dataclass keeps the base's default"
            )

    dataclasses.dataclass(cls, eq=False, repr=False, kw_only=True)  # in place

    # dataclass keeps the Field objects the class body bound to bare names
    # and sets their .name, so a shape that captured one is resolved by
    # identity here. (A Field without an annotation never gets this far:
    # dataclass rejects it.)
    fields = {f.name: f for f in dataclasses.fields(cls)}
    fields_by_obj = {id(f): f for f in fields.values()}

    # Re-attach every field as a DimRef on the class.
    for f in fields.values():
        setattr(cls, f.name, DimRef(cls, f.name, _tier_of(f), f.default))

    members = members_of(cls)
    for m in members:
        if m.owner is not cls:
            continue  # inherited; already processed on its own class
        if isinstance(m, (_Buffer, _Stream)):
            m.dims = _rewrite_refs(m.dims, cls, fields_by_obj)
            if isinstance(m.dtype, Field):
                m.dtype = getattr(cls, fields_by_obj[id(m.dtype)].name)
            for d in m.dims:
                _check_dim_ref(
                    cls, m, d, "dimension", allow_tunable=isinstance(m, _Stream)
                )
            if sum(isinstance(d, _Optional) for d in m.dims) > 1:
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: at most one optional() dimension, "
                    f"since the rank tells whether it is present"
                )
        if isinstance(m, Extent):
            (ref,) = _rewrite_refs((m.field,), cls, fields_by_obj)
            if not isinstance(ref, DimRef) or ref.tier != "param":
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: Extent({ref!r}) must name a param() "
                    f"field, the one a graph may bound per call"
                )
            m.field = ref
        if isinstance(m, _Stream) and m.per is not None:
            per = m.per if isinstance(m.per, tuple) else (m.per,)
            per = _rewrite_refs(per, cls, fields_by_obj)
            for ref in per:
                if not isinstance(ref, DimRef) or ref.tier is None:
                    raise DeclarationError(
                        f"{cls.__name__}.{m.name}: per={ref!r} must be a param() or auto() field"
                    )
            m.per = per

    cls._members = tuple(members)  # type: ignore[attr-defined]
    cls._param_fields = tuple(f.name for f in fields.values() if _tier_of(f) == "param")  # type: ignore[attr-defined]
    cls._derived_params = {  # type: ignore[attr-defined]
        f.name: f.metadata[_DERIVE] for f in fields.values() if _DERIVE in f.metadata
    }
    cls._auto_fields = tuple(f.name for f in fields.values() if _tier_of(f) == "auto")  # type: ignore[attr-defined]
    # The array tier: what a stream's tile, its dtype or its replication
    # names, and what declares itself array=True.
    named: set[str] = set()
    for m in members:
        if isinstance(m, _Stream):
            named.update(_named_fields(m.dims))
            if m.per is not None:
                named.update(_named_fields(m.per))
            if isinstance(m.dtype, DimRef):
                named.add(m.dtype.name)
    cls._array_fields = tuple(  # type: ignore[attr-defined]
        f.name for f in fields.values() if f.name in named or _declares_array(f)
    )


def _named_fields(specs) -> set[str]:
    """The field names a shape or a per= names, through optional()/select()."""
    out: set[str] = set()
    for spec in specs if isinstance(specs, tuple) else (specs,):
        if isinstance(spec, DimRef):
            out.add(spec.name)
        elif isinstance(spec, _Optional):
            out |= _named_fields((spec.ref,))
        elif isinstance(spec, _Select):
            out |= _named_fields((spec.flag,)) | _named_fields(spec.when_true)
            out |= _named_fields(spec.when_false)
    return out
