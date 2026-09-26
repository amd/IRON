# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``@operator``: the class-creation checks both layers go through.

Everything here runs once, when a class body is executed. What it cannot
prove then -- an operator's extents against a tuned overlay -- is left to
:func:`~iron.common.declare.infer`.

:func:`from_spec` is the same checks reached the other way: a class built
from an exported description at run time still goes through ``@operator``.
"""

from __future__ import annotations

import dataclasses
import types
from dataclasses import Field
from typing import Any, Callable

import numpy as np
from ml_dtypes import bfloat16

from .field import DeclarationError, DimRef, dim, _Optional, _Select, _tier_of
from .member import (
    DispatchTime,
    In,
    Out,
    Resident,
    Xclbin,
    _Buffer,
    _Member,
    _Stream,
)
from .operator import Operator
from .overlay import Overlay


def _members_of(cls: type) -> list[_Member]:
    """Members declared in this class body and its ``@operator`` bases, in order.

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
            # external overlay of a built one keeps its fields and streams but
            # not its residents, whose block the image lays out differently.
            if isinstance(value, _Member):
                ordered[name] = value
    return list(ordered.values())


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

    A host buffer's dimension is a ``dim()`` field or an integer: never a
    tunable (inference would cycle through tuning) and never an expression.
    A stream's tile dimension may also be a tunable, since choosing the tile
    is what tuning is for; inference never reads a stream.
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
        allowed = ("dim", "tunable") if allow_tunable else ("dim",)
        if spec.tier not in allowed:
            why = (
                "a tunable; a host shape may not depend on tuning"
                if spec.tier == "tunable"
                else "not declared with dim()"
            )
            raise DeclarationError(
                f"{cls.__name__}.{member.name}: {what} {spec!r} is {why}. A "
                f"shape dimension is a dim() field or an integer literal"
            )
        return
    raise DeclarationError(
        f"{cls.__name__}.{member.name}: {what} {spec!r} is not a dim() field or an "
        f"integer. Expressions are not allowed in shapes; declare the result as a field"
    )


def operator(cls: type) -> type:
    """Process an :class:`Overlay` or :class:`Operator` subclass.

    Applies ``dataclass`` (identity equality; the base supplies ``__eq__``),
    resolves the field objects the class body captured in its shapes to
    names, re-attaches every field as a :class:`DimRef`, checks the shape
    rule, and records the members in declaration order.
    """
    if not (issubclass(cls, Overlay) or issubclass(cls, Operator)):
        raise DeclarationError(
            f"@operator applies to Overlay or Operator subclasses, not {cls}"
        )

    # Members must be unannotated, or dataclass would make them constructor args.
    annotations = cls.__dict__.get("__annotations__", {})
    for name, value in list(vars(cls).items()):
        if isinstance(value, _Member) and name in annotations:
            raise DeclarationError(
                f"{cls.__name__}.{name}: members are declared without an "
                f"annotation; annotating one turns it into a constructor argument"
            )

    # The Field objects the class body bound to bare names, before dataclass
    # processing renames/replaces them.
    pre_fields = {id(v): v for v in vars(cls).values() if isinstance(v, Field)}

    # Overlays get the generated repr; Operators define their own on the base.
    cls = dataclasses.dataclass(cls, eq=False, repr=issubclass(cls, Overlay))  # type: ignore[call-overload]

    fields = {f.name: f for f in dataclasses.fields(cls)}
    fields_by_obj = {i: f for i, f in pre_fields.items()}
    # dataclass reuses the same Field object and sets .name, so identity holds.
    for f in fields.values():
        fields_by_obj.setdefault(id(f), f)

    # Re-attach every field as a DimRef on the class.
    for f in fields.values():
        setattr(cls, f.name, DimRef(cls, f.name, _tier_of(f), f.default))

    members = _members_of(cls)
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
        if isinstance(m, _Stream) and m.per is not None:
            per = m.per if isinstance(m.per, tuple) else (m.per,)
            per = _rewrite_refs(per, cls, fields_by_obj)
            for ref in per:
                if not isinstance(ref, DimRef) or ref.tier is None:
                    raise DeclarationError(
                        f"{cls.__name__}.{m.name}: per={ref!r} must be a dim() or tunable() field"
                    )
            m.per = per

    cls._members = tuple(members)  # type: ignore[attr-defined]
    cls._dim_fields = tuple(f.name for f in fields.values() if _tier_of(f) == "dim")  # type: ignore[attr-defined]
    cls._tunable_fields = tuple(
        f.name for f in fields.values() if _tier_of(f) == "tunable"
    )  # type: ignore[attr-defined]

    if issubclass(cls, Overlay):
        _finish_overlay(cls)
    else:
        _finish_operator(cls, fields)
    return cls


def _finish_overlay(cls: type) -> None:
    images = [v for v in vars(cls).values() if isinstance(v, Xclbin)]
    if len(images) > 1:
        raise DeclarationError(f"{cls.__name__} declares more than one Xclbin")
    if images:
        cls._external = images[0]  # type: ignore[attr-defined]
    for m in cls._members:  # type: ignore[attr-defined]
        if isinstance(m, (_Buffer, DispatchTime)):
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: an Overlay declares streams, residents and "
                f"core-read Scratchpad values; buffers and DispatchTime values belong "
                f"on the Operator"
            )
        if images and isinstance(m, _Stream) and m.via is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a stream of an external overlay must be "
                f"pinned with via=; nothing else says which shim it uses"
            )
        if images and isinstance(m, Resident) and m.address is None:
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: a resident of an external overlay needs "
                f"an address; the sequence writes it there"
            )

    if not images:
        return
    for hook in ("prebuilt", "build"):
        if getattr(cls, hook) is getattr(Overlay, hook):
            raise DeclarationError(
                f"{cls.__name__} declares an Xclbin, so nothing builds its array: "
                f"it must supply {hook}() (iron.common.external.External "
                f"does, for a downloaded image)"
            )


def _finish_operator(cls: type, fields: dict[str, Field]) -> None:
    overlay_cls = _overlay_class_of(cls)
    cls._overlay_class = overlay_cls  # type: ignore[attr-defined]
    for m in cls._members:  # type: ignore[attr-defined]
        if isinstance(m, (_Stream, Resident)):
            raise DeclarationError(
                f"{cls.__name__}.{m.name}: an Operator declares buffers and per-call "
                f"values; streams and residents belong on the Overlay"
            )
        if isinstance(m, _Buffer):
            target = m.to if m.direction == "in" else m.from_
            if m.direction == "inout":
                target = m.to or m.from_
            if target is not None and not isinstance(target, _Stream):
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: to=/from_= must name a stream, got {target!r}"
                )
            if (
                target is not None
                and overlay_cls is not None
                and not issubclass(overlay_cls, target.owner)  # type: ignore[arg-type]
            ):
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: stream {target!r} belongs to "
                    f"{target.owner.__name__}, not to {overlay_cls.__name__}"  # type: ignore[union-attr]
                )
            if m.to is not None and m.to.direction != "in":
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: to= must be a StreamIn"
                )
            if m.from_ is not None and m.from_.direction != "out":
                raise DeclarationError(
                    f"{cls.__name__}.{m.name}: from_= must be a StreamOut"
                )
            for d in m.dims:
                ref = d.ref if isinstance(d, _Optional) else d
                if (
                    isinstance(ref, DimRef)
                    and not issubclass(cls, ref.owner)
                    and overlay_cls is not None
                ):
                    if not issubclass(overlay_cls, ref.owner):
                        raise DeclarationError(
                            f"{cls.__name__}.{m.name}: {ref!r} is neither a field of "
                            f"{cls.__name__} nor of its overlay {overlay_cls.__name__}"
                        )

    # Classic construction: overlay fields as keyword arguments. The operator
    # builds the overlay itself. Untyped, and goes away once every call site
    # passes an overlay.
    if overlay_cls is not None:
        generated_init = cls.__init__

        def __init__(self, ov=None, *args, **kwargs):
            if ov is None or not isinstance(ov, Overlay):
                if ov is not None:
                    args = (ov,) + args
                ov, kwargs = type(self)._split_kwargs(dict(kwargs))
            generated_init(self, ov, *args, **kwargs)

        __init__.__wrapped__ = generated_init  # type: ignore[attr-defined]
        cls.__init__ = __init__  # type: ignore[misc]


def _overlay_class_of(cls: type) -> type | None:
    """The ``O`` in ``class X(Operator[O])``, searched up the bases."""
    for klass in cls.__mro__:
        for base in getattr(klass, "__orig_bases__", ()):
            args = getattr(base, "__args__", ())
            for a in args:
                if isinstance(a, type) and issubclass(a, Overlay):
                    return a
    return None


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

    The dynamic escape for a design whose shapes come from a file rather
    than a formula (swiglu_prefill_stream's stream-dse export). ``inputs``
    and ``outputs`` are literal shapes in argument order; ``params`` are
    the numbers that identify the instance (they become ``dim()`` fields
    with those defaults and reach the name); ``key`` identifies the
    generated design, for sharing; ``generator`` replaces
    :meth:`Operator.generator`, since the sequence is not derived. The
    overlay is a stand-in carrying only ``key``.
    """
    module = Operator.__module__

    def overlay_ns(ns):
        ns["__module__"] = module
        ns["__annotations__"] = {"key": str}
        ns["key"] = dim(key, repr=False)

    overlay_cls = operator(
        types.new_class(f"{name}Overlay", (Overlay,), {}, overlay_ns)
    )

    def operator_ns(ns):
        ns["__module__"] = module
        ns["__annotations__"] = {}
        for pname, value in (params or {}).items():
            ns["__annotations__"][pname] = type(value)
            ns[pname] = dim(value)
        for bname, shape in inputs.items():
            ns[bname] = In(*shape, dtype=dtype)
        for bname, shape in outputs.items():
            ns[bname] = Out(*shape, dtype=dtype)
        ns["design_key"] = lambda self: self.ov.key or None
        if generator is not None:
            ns["generator"] = generator

    return operator(types.new_class(name, (Operator[overlay_cls],), {}, operator_ns))
