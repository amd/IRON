# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator class declares, read once as its body finishes."""

from __future__ import annotations

import dataclasses

from .field import Auto, DimRef, Param
from .member import Member
from .operand import Operand
from .shape import OptionalDim, Shape
from .value import Extent, Value


class Declaration:
    """What an operator class declares: its members and the kind of each field.

    ``Operator.__init_subclass__`` makes one for every subclass, so none can
    forget to be checked. Making it applies ``dataclass`` to the class,
    re-attaches every field as a ``DimRef`` (resolving the field objects the
    body captured in its shapes), checks the shape rules and records what
    the library reads. Checking extents against resolved tunables needs an
    instance, so that is ``Operator.compatible``'s.

    Args:
        cls: The subclass, its body just run.
        library: The class whose attributes the library reads; a field may
            not hide one of them, but may replace an operator base's own.
        shipped: The class runs a shipped image (``image=``), so its streams
            are pinned and its derived values placed.

    Attributes:
        members: The members, the most derived body's order first.
        params: The `Param` fields.
        derived: Each `Param` field's computing default, by name.
        autos: The `Auto` fields.
        tunables: The `Auto` fields a caller, a profile or the tuner sets.
        domains: Each tunable's declared `Domain`, by name.
        array: The fields the array reads: what a stream's tile, a core's
            block of it, its dtype, its replication or its presence names,
            and what declares itself ``array=True``.
        probes: Each `Param(probe=)` field's probe, by name.
    """

    def __init__(self, cls: type, library: type, shipped: bool = False) -> None:
        # Members must be unannotated, or dataclass would make them constructor args.
        annotations = cls.__dict__.get("__annotations__", {})
        for name, value in list(vars(cls).items()):
            if isinstance(value, Member) and name in annotations:
                raise TypeError(
                    f"{cls.__name__}.{name}: members are declared without an "
                    f"annotation; annotating one turns it into a constructor argument"
                )
            if not isinstance(value, Member):
                continue
            base = next((b for b in cls.__mro__[1:] if name in vars(b)), None)
            if base is not None and not isinstance(vars(base)[name], Member):
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
                and not isinstance(value, Member)
                and not callable(value)
                and not isinstance(value, (property, classmethod, staticmethod))
            ):
                raise TypeError(
                    f"{cls.__name__}.{name} = {value!r} does not override the inherited "
                    f"field: annotate it, `{name}: int = Auto({value!r})` (with "
                    f"init=False to pin it), or dataclass keeps the base's default"
                )

        dataclasses.dataclass(cls, eq=False, repr=False, kw_only=True)  # in place

        fields = {f.name: f for f in dataclasses.fields(cls)}
        for name in fields.keys() - inherited:
            base = next((b for b in library.__mro__ if name in vars(b)), None)
            if base is not None:
                raise TypeError(
                    f"{cls.__name__}.{name} hides {base.__name__}.{name}, which "
                    f"the library reads; name the field otherwise"
                )

        # dataclass names the Field objects the class body bound to bare names,
        # so a shape that captured one is rewritten by name (Shape.rewrite).
        for f in fields.values():
            setattr(cls, f.name, DimRef(cls, f))

        # The most derived body's order wins for the members it declares;
        # inherited members it does not redeclare follow, in their own order.
        ordered: dict[str, Member] = {}
        seen: set[str] = set()
        for klass in cls.__mro__:
            for name, value in vars(klass).items():
                if name in seen:
                    continue
                seen.add(name)
                # A subclass hides an inherited member by assigning it None: a
                # shipped image keeps the port's fields and operands but not
                # its values, whose block the image lays out differently.
                if isinstance(value, Member):
                    ordered[name] = value
        members = list(ordered.values())
        for m in members:
            if m.owner is not cls:
                continue  # inherited; already processed on its own class
            if isinstance(m, Operand):
                m.dims = m.dims.rewrite(cls)
                (m.declared_dtype,) = Shape((m.declared_dtype,)).rewrite(cls).dims
                m.dims.check(cls, m, "dimension", allow_tunable=False)
                if m.tile_dims is not None:
                    m.tile_dims = m.tile_dims.rewrite(cls)
                    m.tile_dims.check(cls, m, "tile dimension", allow_tunable=True)
                if m.finish_block is not None:
                    m.finish_block = m.finish_block.rewrite(cls)
                    m.finish_block.check(
                        cls, m, "finish block dimension", allow_tunable=True
                    )
                if sum(isinstance(d, OptionalDim) for d in m.dims.dims) > 1:
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: at most one OptionalDim() dimension, "
                        f"since the rank tells whether it is present"
                    )
                if m.when is not None:
                    (m.when,) = Shape((m.when,)).rewrite(cls).dims
                    if not isinstance(m.when, DimRef) or not isinstance(
                        m.when.field, Param
                    ):
                        raise TypeError(
                            f"{cls.__name__}.{m.name}: when={m.when!r} must be a "
                            f"Param() field, the flag the operand exists under"
                        )
            if isinstance(m, Extent):
                (ref,) = Shape((m.field,)).rewrite(cls).dims
                if not isinstance(ref, DimRef) or not isinstance(ref.field, Param):
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: Extent({ref!r}) must name a Param() "
                        f"field, the one a graph may bound per call"
                    )
                m.field = ref
            if isinstance(m, Operand) and m.tile_dims is not None and m.per is not None:
                m.per = m.per.rewrite(cls)
                for ref in m.per.dims:
                    if not isinstance(ref, DimRef) or not isinstance(
                        ref.field, (Param, Auto)
                    ):
                        raise TypeError(
                            f"{cls.__name__}.{m.name}: per={ref!r} must be a Param() or Auto() field"
                        )

        prepared = [m.name for m in members if isinstance(m, Operand) and m.prepare]
        if len(prepared) > 1:
            raise TypeError(
                f"{cls.__name__}: {prepared} are each prepare=True; a core prepares "
                f"one input, the one its operator's prepare names"
            )
        fed = [m.name for m in members if isinstance(m, Operand) and m.feed]
        if len(fed) > 1:
            raise TypeError(
                f"{cls.__name__}: {fed} are each feed=True; a finish's inputs ride "
                f"one stream"
            )
        self.members = tuple(members)

        params = [f for f in fields.values() if isinstance(f, Param)]
        autos = [f for f in fields.values() if isinstance(f, Auto)]
        self.params = tuple(f.name for f in params)
        self.derived = {f.name: f.derive for f in params if f.derive is not None}
        self.autos = tuple(f.name for f in autos)
        self.tunables = tuple(f.name for f in autos if f.init and not f.derived)
        self.domains = {
            f.name: f.domain
            for f in autos
            if f.name in self.tunables and f.domain is not None
        }
        for n, domain in self.domains.items():
            if domain.when is not None and domain.when not in fields:
                raise TypeError(
                    f"{cls.__name__}.{n}: when={domain.when!r} must name a bool field, "
                    f"the flag the tunable is searched under"
                )
        # The array tier: what a stream's tile, a core's block of it, its dtype,
        # its replication or its presence names, and what declares itself array=True.
        named: set[str] = set()
        for m in members:
            if isinstance(m, Operand) and m.tile_dims is not None:
                named |= m.tile_dims.names()
                if m.finish_block is not None:
                    named |= m.finish_block.names()
                if m.per is not None:
                    named |= m.per.names()
                if isinstance(m.declared_dtype, DimRef):
                    named.add(m.declared_dtype.name)
                if m.when is not None:
                    named.add(m.when.name)
        self.array = tuple(
            n
            for n, f in fields.items()
            if n in named or (isinstance(f, (Param, Auto)) and f.array)
        )
        self.probes = {
            f.name: f.probe for f in params if f.probe is not dataclasses.MISSING
        }
        shaped: set[str] = set()
        for m in members:
            if isinstance(m, Operand):
                shaped |= m.dims.names()
                if m.when is not None:
                    shaped.add(m.when.name)
            elif isinstance(m, Extent):
                shaped.add(m.field.name)
        for n in self.probes:
            if n in self.array:
                raise TypeError(
                    f"{cls.__name__}.{n}: probe= on an array field; the cores are "
                    f"built from it, so its cost may follow it"
                )
            if n in shaped:
                raise TypeError(
                    f"{cls.__name__}.{n}: probe= on a field an operand's shape or "
                    f"presence names; the transfers follow it"
                )
            if not fields[n].init:
                raise TypeError(
                    f"{cls.__name__}.{n}: probe= on an init=False field; the tuner "
                    f"sets the probe through the constructor"
                )
        if not shipped:
            return
        if "array" in vars(cls):
            raise TypeError(
                f"{cls.__name__} runs a shipped image, so nothing builds its array(); "
                f"drop the override"
            )
        for m in members:
            if isinstance(m, Operand) and m.tile_dims is not None and m.via is None:
                raise TypeError(
                    f"{cls.__name__}.{m.name}: a stream into a shipped image must be "
                    f"pinned with via=; nothing else says which shim it uses"
                )
            if isinstance(m, Value) and m.derive is not None and m.address is None:
                raise TypeError(
                    f"{cls.__name__}.{m.name}: a value written into a shipped image "
                    f"needs an address; the sequence writes it there"
                )
