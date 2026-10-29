# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Profiles: tunable values for operator shapes, applied as an operator is made.

A call's own value wins, then the profile's, then ``Operator.resolve``. An
entry matches what a call constructs with, so a dimension that defaults from
another (MHA's ``seq_len``) is keyed by the one given (``seq_pad``).
"""

from __future__ import annotations

import json
from dataclasses import MISSING
from enum import Enum
from types import FunctionType
from pathlib import Path
from typing import TYPE_CHECKING, Any, Iterator, Mapping, Sequence, TypeVar

from ..image.step import FusionKind

if TYPE_CHECKING:
    from .operator import Operator

_Op = TypeVar("_Op", bound="Operator")

# A fusion entry: ``kind`` steps, each ``(operator class, dims, tunables)``
# in order, wired by ``edges`` (local indices into ``steps``, ``(producer,
# output, consumer, input)``); dims are matched the same way a tunable
# entry's are (``Profile.dims``, ``Profile.matches``). ``tunables``, where a
# step gives them, are what it takes running inside this fusion, which may
# differ from what the same shape takes unfused (``Profile.fusion_tunables``);
# None where a step moves none from its own.
_FusionEntry = tuple[
    FusionKind,
    tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...],
    tuple[tuple[int, str, int, str], ...],
]
_FusionStep = (
    tuple[type, Mapping[str, Any] | None]
    | tuple[type, Mapping[str, Any] | None, Mapping[str, Any] | None]
)
# A packing entry: the shapes whose designs share one device configuration
# wherever a version runs them, each ``(operator class, dims, tunables)``;
# ``tunables`` what every step of that shape takes there so they co-reside,
# None where it keeps its own.
_PackingEntry = tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...]


def _normalized(value: Any) -> Any:
    """``value``, a list (what JSON gives back a tuple-valued field as, a
    ``finish=()``, say) turned into a tuple, recursively: a dim or a
    tunable loaded from a file must still match the same value a live
    operator holds.
    """
    if isinstance(value, (list, tuple)):
        return tuple(_normalized(v) for v in value)
    return value


def _with_enum_fields(cls: type, fields: dict[str, Any]) -> dict[str, Any]:
    """``fields`` with an Enum-domain one, JSON's string, its member (should
    `1`: a `Pinned` member's own value, not its ordinal).
    """
    for key, param in cls.declaration.params.items():
        domain = param.domain
        if key in fields and isinstance(domain, type) and issubclass(domain, Enum):
            fields[key] = domain(fields[key])
    return fields


class Profile:
    """Tunable values by operator shape, as ``(cls, dims, tunables)`` entries. An
    open tunable comes from the most specific match (a dimension left out matches
    any, a subclass its base's); equally specific ones that disagree raise.

    ``fusions`` names steps to run fused as one device configuration, each
    matched the same way, by class and dims alone (a tunable moves what a
    fusion itself takes, not which it is); a step may give the tunables it
    takes running inside this fusion, where they differ from what the same
    shape takes unfused.

    ``packings`` names shapes whose designs share one device configuration
    in a full ELF, so a version runs them without reconfiguring between
    them; a member may give the tunables every step of its shape takes there.
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []
        self._fusions: list[_FusionEntry] = []
        self._packings: list[_PackingEntry] = []

    def make(self, cls: type[_Op], **kwargs: Any) -> _Op:
        """``cls(**kwargs)``, its open tunables filled from this profile's
        entries: standalone use of what a graph's recorder applies implicitly
        to every step it constructs.
        """
        pinned = frozenset(
            name
            for name, value in kwargs.items()
            if name in cls.declaration.tunables and value is not None
        )
        given = {**self.tunables_for(cls, kwargs), **kwargs}
        return cls(**given, pinned=pinned)

    def add(self, cls: type, **fields: Any) -> None:
        """Add an entry for ``cls``: ``param()`` values to match (one left out
        matches any value) and ``tunable()`` values to give.
        """
        dims, tunables, unknown, fixed = {}, {}, [], []
        for name, value in fields.items():
            param = cls.declaration.params.get(name)
            if name in cls.declaration.tunables:
                tunables[name] = value
            elif param is not None and param.tunable:
                fixed.append(name)
            elif param is not None:
                dims[name] = value
            else:
                unknown.append(name)
        if unknown:
            raise TypeError(f"{cls.__name__} declares no field {unknown}")
        if fixed:
            raise TypeError(
                f"{cls.__name__}.{fixed} are derived or fixed by the class, not "
                f"tunables a profile gives"
            )
        if not tunables:
            raise TypeError(f"an entry for {cls.__name__} must give a tunable")
        self._entries.append((cls, dims, tunables))

    def add_fusion(
        self,
        kind: FusionKind,
        steps: Sequence[_FusionStep],
        edges: Sequence[tuple[int, str, int, str]],
    ) -> None:
        """Add a fusion entry: ``kind`` steps (each ``(operator class, dims)``
        or ``(operator class, dims, tunables)``, in order) run as one device
        configuration, wired by ``edges`` (local indices into ``steps``,
        ``producer``'s drained ``output`` into ``consumer``'s filled
        ``input``); each step matches by class and dims (a dim left out
        matches any, a subclass its base's, as a tunable entry does).
        ``tunables``, where a step gives them, are what it takes running
        inside this fusion (``fusion_tunables``); a step giving none keeps
        what it takes unfused.

        Raises:
            TypeError: Fewer than two steps are given, a dim is not a
                non-tunable ``param()`` of its class, a name in ``tunables``
                is not a ``tunable()`` of its class, an edge names a step
                out of range or itself, or either side of an edge declares
                no such operand.
        """
        if len(steps) < 2:
            raise TypeError("a fusion entry needs at least two steps")
        resolved = self._members(steps)
        for producer, output, consumer, input in edges:
            if not 0 <= producer < len(steps) or not 0 <= consumer < len(steps):
                raise TypeError(
                    f"edge names step {(producer, consumer)}, outside "
                    f"0..{len(steps) - 1}"
                )
            if producer == consumer:
                raise TypeError("an edge cannot feed a step from itself")
            p_cls, c_cls = steps[producer][0], steps[consumer][0]
            if not any(
                m.name == output and m.drains for m in p_cls.declaration.operands
            ):
                raise TypeError(f"{p_cls.__name__} declares no output {output!r}")
            if not any(m.name == input and m.fills for m in c_cls.declaration.operands):
                raise TypeError(f"{c_cls.__name__} declares no input {input!r}")
        self._fusions.append((kind, resolved, tuple(edges)))

    def add_packing(self, members: Sequence[_FusionStep]) -> None:
        """Add a packing entry: the designs of ``members``' shapes (each
        ``(operator class, dims)`` or ``(operator class, dims, tunables)``,
        matched as a fusion's steps are) share one device configuration in
        a full ELF wherever a version runs them. ``tunables``, where a member
        gives them, are what every step of its shape takes in such a version.

        Raises:
            TypeError: Fewer than two members are given, a dim is not a
                non-tunable ``param()`` of its class, or a name in
                ``tunables`` is not a ``tunable()`` of its class.
        """
        if len(members) < 2:
            raise TypeError("a packing entry needs at least two members")
        self._packings.append(self._members(members))

    @staticmethod
    def _members(
        steps: Sequence[_FusionStep],
    ) -> tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...]:
        """``steps`` as ``(class, dims, tunables)``, each name checked
        against its class's declaration.
        """
        resolved: list[tuple[type, dict[str, Any], dict[str, Any] | None]] = []
        for cls, dims, *rest in steps:
            dims = dict(dims or {})
            unknown = [
                name
                for name in dims
                if name not in cls.declaration.params
                or cls.declaration.params[name].tunable
            ]
            if unknown:
                raise TypeError(f"{cls.__name__} declares no dim {unknown}")
            tunables = rest[0] if rest else None
            if tunables is not None:
                unknown_t = [n for n in tunables if n not in cls.declaration.tunables]
                if unknown_t:
                    raise TypeError(f"{cls.__name__} has no tunable {unknown_t}")
                tunables = dict(tunables)
            resolved.append((cls, dims, tunables))
        return tuple(resolved)

    def fused(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
    ) -> bool:
        """Whether this profile fuses ``steps`` (resolved operators, in
        order) of ``kind``, wired by ``edges`` (local indices): a fusion
        entry of the same kind, length and wiring whose steps' classes and
        dims (``Profile.dims``, ``Profile.matches``) match them, in order.
        """
        return self._matching(kind, steps, edges) is not None

    def fusion_tunables(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
    ) -> list[dict[str, Any] | None] | None:
        """The matching fusion entry's per-step tunables (``add_fusion``'s
        ``tunables``), in order; None where no entry matches ``kind``,
        ``steps`` and ``edges`` (``fused``). A step's own entry is None
        where it keeps what it takes unfused.
        """
        entry = self._matching(kind, steps, edges)
        return None if entry is None else [t for _, _, t in entry]

    def _matching(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
    ) -> tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...] | None:
        step_dims = [self.dims(type(s), vars(s)) for s in steps]
        edges = tuple(edges)
        return next(
            (
                entry_steps
                for entry_kind, entry_steps, entry_edges in self._fusions
                if entry_kind is kind
                and len(entry_steps) == len(steps)
                and entry_edges == edges
                and all(
                    isinstance(s, cls) and self.matches(matched, dims)
                    for s, (cls, matched, _), dims in zip(steps, entry_steps, step_dims)
                )
            ),
            None,
        )

    def fusions(self) -> list[_FusionEntry]:
        """Each fusion entry as ``(kind, steps, edges)``, ``steps`` each
        ``(operator class, dims, tunables)``, in the order added."""
        return list(self._fusions)

    def packing_of(self, op: Operator) -> tuple[int, dict[str, Any] | None] | None:
        """The first packing entry with a member matching ``op`` (a resolved
        operator, by class and dims), as its index in ``packings()`` and the
        member's tunables; None where no entry names its shape.
        """
        dims = self.dims(type(op), vars(op))
        for index, members in enumerate(self._packings):
            for cls, matched, tunables in members:
                if isinstance(op, cls) and self.matches(matched, dims):
                    return index, tunables
        return None

    def packings(self) -> list[_PackingEntry]:
        """Each packing entry's members, ``(operator class, dims,
        tunables)``, in the order added."""
        return list(self._packings)

    def tunables_for(self, cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """The tunables for the ``cls`` a call with ``given`` keywords makes,
        each from the most specific entry naming it.
        """
        dims = self.dims(cls, given)
        chosen: dict[str, tuple[int, Any]] = {}
        for base, matched, tunables in self._entries:
            if not issubclass(cls, base) or not self.matches(matched, dims):
                continue
            rank = len(matched)
            for name, value in tunables.items():
                if name not in chosen or rank > chosen[name][0]:
                    chosen[name] = (rank, value)
                elif rank == chosen[name][0] and chosen[name][1] != value:
                    raise ValueError(
                        f"profile is ambiguous for {cls.__name__} {dims}: "
                        f"{name}={chosen[name][1]} and {name}={value} from "
                        f"entries of equal specificity"
                    )
        return {name: value for name, (_, value) in chosen.items()}

    @staticmethod
    def dims(cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """Every dimension (``param()``) of the ``cls`` a call with
        ``given`` keywords makes, as an entry is matched against: one it
        leaves out is its default, None where a function computes it.
        """
        dims = {}
        for name, p in cls.declaration.params.items():
            if p.tunable:
                continue
            if name in given:
                dims[name] = given[name]
            elif p.derive is not None or isinstance(p.default, FunctionType):
                # Unknown until made, so an entry naming it matches only a call
                # giving it: entries key on what a call constructs with.
                dims[name] = None
            elif p.default is not MISSING:
                dims[name] = p.default
        return dims

    @staticmethod
    def matches(matched: Mapping[str, Any], dims: Mapping[str, Any]) -> bool:
        """Whether an entry's ``matched`` dimensions cover ``dims``: equal,
        a value JSON round-tripped to a list (``_normalized``) where a live
        one is still the tuple it held, counted equal too.
        """
        return all(
            name in dims and _normalized(dims[name]) == _normalized(v)
            for name, v in matched.items()
        )

    @classmethod
    def load(cls, path: str | Path) -> Profile:
        """The profile ``save`` wrote to ``path``."""
        from ...operators import CATALOG  # the operators import this module

        with open(path) as f:
            data = json.load(f)
        if not isinstance(data, dict) or not {"entries"} <= set(data) <= {
            "entries",
            "fusions",
            "packings",
        }:
            raise ValueError(f"{path}: a profile is {{'entries': [...]}}")
        profile = cls()
        for entry in data["entries"]:
            fields = dict(entry)
            name = fields.pop("operator")
            if name not in CATALOG:
                raise ValueError(f"{path}: no operator {name!r} in iron.operators")
            op_cls = CATALOG[name]
            profile.add(op_cls, **_with_enum_fields(op_cls, fields))

        def members(entries) -> list[tuple[type, dict[str, Any], Any]]:
            out = []
            for entry in entries:
                fields = dict(entry)
                name = fields.pop("operator")
                tunables = fields.pop("tunables", None)
                if name not in CATALOG:
                    raise ValueError(f"{path}: no operator {name!r} in iron.operators")
                op_cls = CATALOG[name]
                out.append((op_cls, _with_enum_fields(op_cls, fields), tunables))
            return out

        for fusion in data.get("fusions", ()):
            if set(fusion) != {"kind", "steps", "edges"}:
                raise ValueError(
                    f"{path}: a fusion is {{'kind': ..., 'steps': [...], "
                    f"'edges': [...]}}"
                )
            edges = [tuple(e) for e in fusion["edges"]]
            profile.add_fusion(
                FusionKind(fusion["kind"]), members(fusion["steps"]), edges
            )
        for packing in data.get("packings", ()):
            profile.add_packing(members(packing))
        return profile

    def save(self, path: str | Path) -> None:
        """Write the profile as JSON, one entry to a line, then its fusions
        where there are any.

        Raises:
            ValueError: An entry's or a fusion step's operator is not in
                ``iron.operators.CATALOG``.
        """
        from ...operators import CATALOG  # the operators import this module

        names = {cls: name for name, cls in CATALOG.items()}

        def members(entries) -> list[dict[str, Any]]:
            for cls, _, _ in entries:
                if cls not in names:
                    raise ValueError(
                        f"{cls.__qualname__} is not in iron.operators.CATALOG"
                    )
            return [
                {
                    "operator": names[cls],
                    **dims,
                    **({"tunables": tunables} if tunables else {}),
                }
                for cls, dims, tunables in entries
            ]

        lines = []
        for cls, dims, tunables in self._entries:
            if cls not in names:
                raise ValueError(f"{cls.__qualname__} is not in iron.operators.CATALOG")
            name = names[cls]
            lines.append(json.dumps({"operator": name, **dims, **tunables}))
        fusion_lines = [
            json.dumps(
                {
                    "kind": kind.value,
                    "steps": members(steps),
                    "edges": [list(e) for e in edges],
                }
            )
            for kind, steps, edges in self._fusions
        ]
        packing_lines = [json.dumps(members(p)) for p in self._packings]
        body = '{"entries": [\n  ' + ",\n  ".join(lines) + "\n]"
        if fusion_lines:
            body += ',\n"fusions": [\n  ' + ",\n  ".join(fusion_lines) + "\n]"
        if packing_lines:
            body += ',\n"packings": [\n  ' + ",\n  ".join(packing_lines) + "\n]"
        with open(path, "w") as f:
            f.write(body + "}\n")

    def __iter__(self) -> Iterator[tuple[type, dict[str, Any], dict[str, Any]]]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        names = dict.fromkeys(cls.__name__ for cls, _, _ in self._entries)
        return f"Profile({', '.join(names)})"
