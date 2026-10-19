# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What an operator class declares, read once as its body finishes."""

from __future__ import annotations

import dataclasses
import enum
import inspect
import math
import types
from collections.abc import Mapping
from typing import Annotated, Any, ClassVar, Union, get_args, get_origin

from aie.iron import In, InOut, Out

from .domain import Divisors, Domain
from .field import AutoSpec, ParamSpec
from .member import Member
from .operand import Operand
from .shape import Select, Shape
from .value import DispatchValue, Extent, Value

# What an Array annotates by hand, besides what it is given: its operands
# and the device.
LIBRARY_VIEWS = frozenset({"buffers", "inputs", "outputs", "dev"})


def _marked(cls: type, name: str, hint, tag: str):
    """``T`` of ``hint`` when it is ``Annotated[T, tag]`` (aie.iron's
    ``CompileTime[T]`` or ``DispatchTime[T]``), else None.

    A marker inside a union is refused: ``CompileTime[int] | None`` reads as
    either, so the optional type goes inside, ``CompileTime[int | None]``.
    """
    if get_origin(hint) is Annotated:
        return get_args(hint)[0] if tag in hint.__metadata__ else None
    if get_origin(hint) in (Union, types.UnionType) and any(
        get_origin(a) is Annotated for a in get_args(hint)
    ):
        raise TypeError(
            f"{cls.__name__}.{name}: annotated {hint!r}; put the union inside "
            f"the marker, `CompileTime[int | None]`"
        )
    return None


def _call(marker) -> tuple[tuple, dict]:
    """The arguments an ``In``/``Out``/``InOut`` was called with: its
    ``args``/``kwargs`` on mlir-aie 1.4.5a1, its typed fields on PR #50.
    The 1.4.5a1 branch goes with the pin bump.
    """
    if hasattr(marker, "kwargs"):
        return marker.args, marker.kwargs
    return marker.dims, dict(
        dtype=marker.declared_dtype,
        obj_shape=marker.obj_dims,
        per=marker.per,
        depth=marker.depth,
        replicate=marker.replicate,
        when=marker.when,
    )


class Declaration:
    """What an operator class declares: its members and the kind of each field.

    ``Operator.__init_subclass__`` makes one for every subclass, so none can
    forget to be checked. Making it applies ``dataclass`` to the class,
    re-attaches every field to the class (the field objects its shapes
    captured), checks the shape rules and records what the library reads. Checking extents against resolved tunables needs an
    instance, so that is ``Operator.compatible``'s.

    Args:
        cls: The subclass, its body just run.
        library: The class whose attributes the library reads; a field may
            not hide one of them, but may replace an operator base's own.
        shipped: The class runs a shipped image (``image=``), so it takes
            no per-call value.

    Attributes:
        name: The class's name.
        members: The members, the most derived body's order first.
        params: The `field()` fields.
        derived: Each `field()` field's computing default, by name.
        held: The held `field(derive=)` fields, which a given value must agree with.
        autos: The `Auto` fields.
        tunables: The `Auto` fields a caller, a profile or the tuner sets.
        domains: Each tunable's declared `Domain`, by name.
        array: The fields the array reads, which its generated ``Array``
            holds: what a stream's tile, its dtype, its replication or its
            presence names, and those declared ``array=True``.
        probes: Each `field(probe=)` field's probe, by name.
    """

    def __init__(self, cls: type, library: type, shipped: bool = False) -> None:
        self.name = cls.__name__
        # aie.iron's In, Out and InOut, called in the body, become operands.
        for name, value in list(vars(cls).items()):
            if isinstance(value, (In, Out, InOut)):
                args, kwargs = _call(value)
                member = Operand(type(value), *args, **kwargs)
                setattr(cls, name, member)
                member.__set_name__(cls, name)
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
        # A field is CompileTime[T] or DispatchTime[T]; a DispatchTime one
        # is a member, its dtype T.
        for name, hint in inspect.get_annotations(cls, eval_str=True).items():
            if hint is ClassVar or get_origin(hint) is ClassVar:
                continue
            spec = ParamSpec.of(vars(cls).get(name))
            dtype = _marked(cls, name, hint, "aie.dispatch_time")
            if dtype is not None:
                f = vars(cls).get(name)
                if (
                    spec is None
                    or f.init
                    or f.default is not dataclasses.MISSING
                    or isinstance(spec, AutoSpec)
                    or spec.derive is not None
                    or spec.probe is not dataclasses.MISSING
                    or spec.array
                ):
                    raise TypeError(
                        f"{cls.__name__}.{name}: declare a DispatchTime value "
                        f"`{name}: DispatchTime[np.int32] = field(init=False)`, "
                        f"with no other option"
                    )
                del annotations[name]
                member = DispatchValue(dtype=dtype)
                setattr(cls, name, member)
                member.__set_name__(cls, name)
            elif _marked(cls, name, hint, "aie.compile_time") is None:
                raise TypeError(
                    f"{cls.__name__}.{name}: annotated {hint!r}; a field is "
                    f"annotated aie.iron's CompileTime[T] or DispatchTime[T]"
                )
            elif spec is None:
                raise TypeError(
                    f"{cls.__name__}.{name}: declare a CompileTime field with "
                    f"field() or Auto(), `{name}: ... = field(...)`"
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
                    f"field: annotate it, `{name}: CompileTime[int] = Auto(default={value!r})` (with "
                    f"init=False to pin it), or dataclass keeps the base's default"
                )

        dataclasses.dataclass(cls, eq=False, repr=False, kw_only=True)  # in place

        fields = {f.name: f for f in dataclasses.fields(cls)}
        # The bare name `from __future__ import annotations` leaves as a
        # string, resolved per class rather than for the whole MRO at once:
        # the library base's own annotations name TYPE_CHECKING-only types,
        # and an operator's fields are its subclasses', so only theirs are
        # evaluated.
        hints = {}
        for klass in reversed(cls.__mro__):
            if klass is not library and issubclass(klass, library):
                hints |= {
                    n: _marked(klass, n, h, "aie.compile_time") or h
                    for n, h in inspect.get_annotations(klass, eval_str=True).items()
                }
        # A field's type is `T | None`: a shape dimension of it is present
        # only where it resolves to something other than None.
        self.nullable = frozenset(
            name for name, hint in hints.items() if type(None) in get_args(hint)
        )
        for name in fields.keys() - inherited:
            base = next((b for b in library.__mro__ if name in vars(b)), None)
            if base is not None:
                raise TypeError(
                    f"{cls.__name__}.{name} hides {base.__name__}.{name}, which "
                    f"the library reads; name the field otherwise"
                )

        # dataclass replaced each with its default; a field is its own reference.
        for f in fields.values():
            setattr(cls, f.name, f)

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
                m.dims.check(cls, m, "dimension", allow_tunable=False)
                if m.obj_dims is not None:
                    m.obj_dims.check(cls, m, "obj_shape dimension", allow_tunable=True)
                optional = [
                    d.name
                    for d in m.dims.dims
                    if ParamSpec.of(d) is not None and d.name in self.nullable
                ]
                if len(optional) > 1:
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: at most one T | None dimension "
                        f"{optional}, since the rank tells whether it is present"
                    )
                if m.when is not None:
                    when = ParamSpec.of(m.when)
                    if when is None or isinstance(when, AutoSpec):
                        raise TypeError(
                            f"{cls.__name__}.{m.name}: when={Shape((m.when,))} must "
                            f"be a field(), the flag the operand exists under"
                        )
            if isinstance(m, Extent):
                extent = ParamSpec.of(m.field)
                if extent is None or isinstance(extent, AutoSpec):
                    raise TypeError(
                        f"{cls.__name__}.{m.name}: Extent({Shape((m.field,))}) must "
                        f"name a field(), the one a graph may bound per call"
                    )
            if isinstance(m, Operand) and m.streamed and m.per is not None:
                for ref in m.per.dims:
                    if ParamSpec.of(ref) is None:
                        raise TypeError(
                            f"{cls.__name__}.{m.name}: per={Shape((ref,))} must be "
                            f"a field() or Auto() field"
                        )

        self.members = tuple(members)

        specs = {
            name: spec
            for name, f in fields.items()
            if (spec := ParamSpec.of(f)) is not None
        }
        params = {n: s for n, s in specs.items() if not isinstance(s, AutoSpec)}
        autos = {n: s for n, s in specs.items() if isinstance(s, AutoSpec)}
        self.params = tuple(params)
        self.derived = {n: s.derive for n, s in params.items() if s.derive is not None}
        self.held = tuple(n for n, s in params.items() if s.held)
        self.autos = tuple(autos)
        self.tunables = tuple(n for n in autos if fields[n].init)
        # A tunable given no domain and annotated with an Enum is searched
        # over that Enum's members.
        self.domains = {}
        for n, s in autos.items():
            if n not in self.tunables:
                continue
            domain = s.domain
            if domain is None:
                hint = hints.get(n)
                if isinstance(hint, type) and issubclass(hint, enum.Enum):
                    domain = hint
            if domain is not None:
                self.domains[n] = domain
        for n, domain in self.domains.items():
            when = domain.when if isinstance(domain, Domain) else None
            if when is not None and not callable(when):
                raise TypeError(
                    f"{cls.__name__}.{n}: when={when!r} must be a callable of "
                    f"(op, dev), the flag the tunable is searched under"
                )
        # The array tier (``array`` above).
        named: set[str] = set()
        for m in members:
            if isinstance(m, Operand) and m.obj_dims is not None:
                named |= m.obj_dims.names()
                if m.per is not None:
                    named |= m.per.names()
                if isinstance(m.declared_dtype, dataclasses.Field):
                    named.add(m.declared_dtype.name)
                if m.when is not None:
                    named.add(m.when.name)
        named |= {n for n, s in specs.items() if s.array}
        # By hand an Array annotates only the library's views it reads.
        if "Array" in vars(cls):
            hand = sorted(inspect.get_annotations(cls.Array).keys() - LIBRARY_VIEWS)
            if hand:
                raise TypeError(
                    f"{cls.__name__}.Array annotates {hand}, but an Array annotates "
                    f"only {sorted(LIBRARY_VIEWS)}: it is given every member and "
                    f"every field a stream names; declare another field it reads "
                    f"field(array=True) or Auto(array=True), and compute anything "
                    f"else in the Array"
                )
        listed = (
            {f.name for f in dataclasses.fields(cls.Array)}
            if dataclasses.is_dataclass(cls.Array)
            else set()
        )
        missing = [
            n
            for n in [*fields, *(m.name for m in members)]
            if n not in listed and (n in named or n not in fields)
        ]
        if missing:
            cls.Array = type(
                cls.Array.__name__,
                (cls.Array,),
                {
                    "__module__": cls.Array.__module__,
                    "__qualname__": cls.Array.__qualname__,
                    "__annotations__": {n: Any for n in missing},
                },
            )
            listed |= set(missing)
        own = fields.keys() - {f.name for f in dataclasses.fields(library)}
        self.array = tuple(n for n in fields if n in listed and n in own)
        self.probes = {
            n: s.probe for n, s in params.items() if s.probe is not dataclasses.MISSING
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
        for m in members:
            if isinstance(m, Value) and m.derive is None:
                raise TypeError(
                    f"{cls.__name__}.{m.name}: a shipped image takes no per-call "
                    f"value; its stream is built once per shape"
                )

    def __repr__(self) -> str:
        """What was declared and inferred, a line a kind: fields, tunables
        with the values each is searched over, members with their symbolic
        shapes, and the array tier the cores are built from.
        """
        given = [n for n in self.params if n not in self.derived]
        lines = [
            f"{self.name}",
            f"  fields:   {', '.join(given) or '-'}",
            f"  derived:  {', '.join(self.derived) or '-'}",
            "  tunables: "
            + (
                ", ".join(
                    f"{n} in {_domain(self.domains[n])}" if n in self.domains else n
                    for n in self.tunables
                )
                or "-"
            ),
            "  resolved: "
            + (", ".join(n for n in self.autos if n not in self.tunables) or "-"),
            *(f"  {_member(m)}" for m in self.members),
            f"  array:    ({', '.join(self.array)})",
        ]
        return "\n".join(lines)

    def shim_columns(
        self,
        dev,
        num_channels: int = 1,
        flags: Mapping[str, Any] | None = None,
    ) -> int:
        """How many of ``dev``'s columns fit the class's streams in the shim DMA budget.

        A ``replicate`` stream is paid once per channel rather than per column,
        and a stream with no ``per=`` once.
        """
        streams = [
            m
            for m in self.members
            if isinstance(m, Operand) and m.streamed and m.present(flags or {})
        ]
        cols = dev.cols
        for drains, budget in (
            (False, dev.shim_dma_channels_in),
            (True, dev.shim_dma_channels_out),
        ):
            ours = [m for m in streams if m.drains == drains]
            lanes = [m for m in ours if m.per is not None]
            per_core = sum(not m.replicate for m in lanes) * num_channels
            once = len(ours) - len(lanes)
            shared = sum(m.replicate for m in lanes) * num_channels + once
            if per_core:
                cols = min(cols, (budget - shared) // per_core)
        return max(1, cols)

    def call_operands(
        self, args, kwargs
    ) -> tuple[dict[str, Any], list, dict[str, Any]]:
        """Bind a call's operands as ``(x, ..., [outputs...], *, weight=None,
        ...)`` would: an optional input is a keyword, so an output is never
        taken for it.

        Returns:
            The inputs by name, in declaration order; the outputs; the other
            keywords.
        """
        ins = [m for m in self.members if isinstance(m, Operand) and m.fills]
        required = [m.name for m in ins if m.when is None]
        optional = {m.name for m in ins if m.when is not None}
        given = {k: v for k, v in kwargs.items() if k in optional and v is not None}
        if len(args) < len(required):
            raise TypeError(
                f"{self.name} takes {len(required)} positional operand(s) "
                f"({', '.join(required)}), got {len(args)}"
            )
        bound = {**dict(zip(required, args)), **given}
        inputs = {m.name: bound[m.name] for m in ins if m.name in bound}
        rest = {k: v for k, v in kwargs.items() if k not in optional}
        return inputs, list(args[len(required) :]), rest

    def infer(self, inputs: Mapping[str, Any], outputs=(), **kwargs) -> dict[str, Any]:
        """Bind the dimension fields from operand shapes.

        Each declared dimension is a field or a literal, so this is a lookup.
        An optional input's ``when=`` flag is true where ``inputs`` names it.

        Args:
            inputs: The input shapes, by operand name.
            outputs: The shapes of caller-supplied outputs, in declaration
                order.
            **kwargs: Construction arguments; the dimension fields and shape
                flags among them pin values and are checked for agreement.

        Returns:
            ``{field: value}``: the pinned and the inferred fields, and the
            operand flags.

        Raises:
            TypeError: The operands are not the declared ones.
            ValueError: A shape disagrees with the declaration or another
                operand.
        """
        buffers = [m for m in self.members if isinstance(m, Operand)]
        names = set(self.params)
        for m in buffers:
            names.update(m.dims.names())
        given = {k: v for k, v in kwargs.items() if k in names}
        flags: dict[str, bool] = {}
        for m in buffers:
            if not m.fills or m.when is None:
                continue
            flag, has = m.when.name, m.name in inputs
            if flags.setdefault(flag, has) != has:
                raise TypeError(
                    f"{self.name}: the operands {flag}= brings are given together"
                )
            if flag in given and bool(given[flag]) != has:
                raise TypeError(
                    f"{self.name}({flag}=True) takes {m.name}="
                    if has is False
                    else f"{self.name}: {m.name}= is an operand only where "
                    f"{flag} is true"
                )
        given |= flags
        ins = [m for m in buffers if m.fills and m.present(given)]
        if [m.name for m in ins] != list(inputs):
            raise TypeError(
                f"{self.name} takes {len(ins)} operand(s) "
                f"({', '.join(m.name for m in ins)}), got {len(inputs)}"
            )
        outs = [m for m in buffers if not m.fills and m.present(given)]
        if outputs and len(outputs) != len(outs):
            raise TypeError(
                f"{self.name} produces {len(outs)} output(s) "
                f"({', '.join(m.name for m in outs)}), got {len(outputs)}"
            )
        pairs = [(m, inputs[m.name]) for m in ins] + list(zip(outs, outputs))
        bound: dict[str, Any] = dict(given)
        # Each dimension an operand's shape gives: (field, value, where).
        found: list[tuple[dataclasses.Field, int | None, str]] = []
        for m, shape in pairs:
            shape = tuple(int(s) for s in shape)
            dims = list(m.dims.dims)
            at = next(
                (
                    i
                    for i, d in enumerate(dims)
                    if ParamSpec.of(d) is not None and d.name in self.nullable
                ),
                None,
            )
            if at is not None:
                optional = dims.pop(at)
                if len(shape) == len(dims) + 1:
                    found.append((optional, shape[at], f"{m.name}.shape[{at}]"))
                    shape = shape[:at] + shape[at + 1 :]
                elif len(shape) == len(dims):
                    found.append((optional, None, f"{m.name} (rank {len(shape)})"))
                else:
                    raise ValueError(
                        f"{self.name}: operand {m.name} has rank {len(shape)}, "
                        f"declared {m!r}"
                    )
            expanded: list = []
            while dims:
                d = dims.pop(0)
                if not isinstance(d, Select):
                    expanded.append(d)
                    continue
                flag = d.flag
                value = bound.get(flag.name, flag.default)
                if value is dataclasses.MISSING:
                    raise ValueError(
                        f"{self.name}: {flag.name} selects {m.name}'s shape and "
                        f"has no default; pass it explicitly"
                    )
                dims[:0] = d.when_true if value else d.when_false
            dims = expanded
            if len(dims) == 1 and len(shape) != 1:
                # A flat buffer takes an operand of any rank: its one
                # dimension is the element count.
                shape = (math.prod(shape),)
            if len(shape) != len(dims):
                raise ValueError(
                    f"{self.name}: operand {m.name} has rank {len(shape)} "
                    f"{shape}, declared rank {len(dims)} {m!r}"
                )
            for i, (d, n) in enumerate(zip(dims, shape)):
                if ParamSpec.of(d) is not None:
                    found.append((d, n, f"{m.name}.shape[{i}]"))
                elif int(d) != n:
                    raise ValueError(
                        f"{self.name}: operand {m.name}.shape[{i}] is {n}, "
                        f"declared {d}"
                    )
        origin: dict[str, str] = {k: "given" for k in given}
        for ref, value, where in found:
            if ref.name in bound and bound[ref.name] != value:
                raise ValueError(
                    f"{self.name}: {ref.name} is {value} from {where} but "
                    f"{bound[ref.name]} from {origin[ref.name]}"
                )
            bound[ref.name] = value
            origin.setdefault(ref.name, where)
        return bound


def _bound(bound) -> str:
    if isinstance(bound, dataclasses.Field):
        return bound.name
    return "f(op, dev)" if callable(bound) else repr(bound)


def _domain(domain) -> str:
    """``domain`` in a few words."""
    if isinstance(domain, type):
        return "{" + ", ".join(m.name for m in domain) + "}"
    if not isinstance(domain, Domain):
        return "{" + ", ".join(map(repr, domain)) + "}"
    text = type(domain).__name__
    if isinstance(domain, Divisors):
        parts = [f"of {_bound(domain.of)}"]
        if domain.step != 1:
            parts.append(f"step {_bound(domain.step)}")
        if domain.cap is not None:
            parts.append(f"cap {_bound(domain.cap)}")
        text += f"({', '.join(parts)})"
    return text + (" when f(op, dev)" if domain.when is not None else "")


def _member(m) -> str:
    """A member's kind, name and, for an operand, its symbolic shape."""
    if isinstance(m, Operand):
        per = "" if m.per is None else f" per [{m.per}]"
        return f"{m.role.__name__:<9} {m.name} [{m.dims}]{per}"
    return f"{type(m).__name__:<9} {m.name}"
