# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Profiles: tunable values for operator shapes, applied as an operator is made.

A call's own value wins, then the profile's, then ``Operator.resolve``. An
entry matches what a call constructs with, so a dimension that defaults from
another (MHA's ``seq_len``) is keyed by the one given (``seq_pad``).
"""

from __future__ import annotations

import dataclasses
import json
from dataclasses import MISSING
from enum import Enum
from pathlib import Path
from types import FunctionType
from typing import TYPE_CHECKING, Any, Iterable, Iterator, Mapping, Sequence, TypeVar

from ..image.step import FusionKind

if TYPE_CHECKING:
    from .operator import Operator

_Op = TypeVar("_Op", bound="Operator")

# A graph version's key (``Recording.version``, ``Graph.versions``): each
# input's name, shape and dtype name, in the order its body takes them.
Version = tuple[tuple[str, tuple[int, ...], str], ...]

# A fusion entry: ``kind`` steps, each ``(operator class, dims, tunables)``
# in order, wired by ``edges`` (local indices into ``steps``, ``(producer,
# output, consumer, input)``); dims are matched the same way a tunable
# entry's are (``Profile.dims``, ``Profile.matches``). ``tunables``, where a
# step gives them, are what it takes running inside this fusion, which may
# differ from what the same shape takes unfused (``Profile.fusion_tunables``);
# None where a step moves none from its own. ``versions``, as a packing
# entry's own, is the graph versions (``Recording.version``) it applies in,
# or every version where None: a kind no code scopes today (``STREAM``,
# ``STAGED``, ``PACK``, ``MERGE``) carries it as None throughout, one list
# serving every fusion kind rather than a parallel, ``FOLD``-only one.
_FusionEntry = tuple[
    FusionKind,
    tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...],
    tuple[tuple[int, str, int, str], ...],
    frozenset[Version] | None,
]
_FusionStep = (
    tuple[type, Mapping[str, Any] | None]
    | tuple[type, Mapping[str, Any] | None, Mapping[str, Any] | None]
)


@dataclasses.dataclass(frozen=True)
class PackingEntry:
    """The shapes whose designs share one device configuration, each
    ``(operator class, dims, tunables)``, ``tunables`` what every step of
    that shape takes there so they co-reside (None where it keeps its own),
    in the graph versions ``versions`` names, or in every version where None.
    """

    members: tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...]
    versions: frozenset[Version] | None = None


def _normalized(value: Any) -> Any:
    """``value``, a list (what JSON gives back a tuple-valued field as, a
    ``finish=()``, say) turned into a tuple, recursively: a dim or a
    tunable loaded from a file must still match the same value a live
    operator holds.
    """
    if isinstance(value, (list, tuple)):
        return tuple(_normalized(v) for v in value)
    return value


def _load_versions(versions: list | None) -> list[Version] | None:
    """``versions``, a fusion or packing entry's own JSON field, as the live
    ``Version`` tuples ``add_fusion``/``add_packing`` take: None kept as is,
    each one's shape turned back from JSON's list into the tuple a live
    ``Recording.version`` holds (the same round-trip ``_normalized`` spares
    a dim or a tunable; a version is a dict key, so it must be exact).
    """
    if versions is None:
        return None
    return [
        tuple((n, tuple(shape), dtype) for n, (shape, dtype) in v.items())
        for v in versions
    ]


def _dump_versions(versions: frozenset[Version] | None) -> dict[str, Any]:
    """``{"versions": [...]}`` for a fusion or packing entry's own
    ``versions``, JSON-safe (a tuple has none, so each version's shape is a
    list); empty where ``versions`` is None, so a caller splats it into an
    entry's own dict unconditionally.
    """
    if versions is None:
        return {}
    return {
        "versions": [
            {n: [list(shape), dtype] for n, shape, dtype in v} for v in sorted(versions)
        ]
    }


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
    shape takes unfused. An entry may name the graph versions it applies in,
    as a packing entry's own does; unscoped (every fusion kind but a
    tuner-proposed fold, today) in every version where it matches.

    ``packings`` names shapes whose designs share one device configuration
    in a full ELF, so a version runs them without reconfiguring between
    them; a member may give the tunables every step of its shape takes there.
    An entry may name the graph versions it applies in: one version's arrays
    are another's at other extents (a decode step's and a prompt chunk's), so
    a grouping that pays in one can cost in the other.
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []
        self._fusions: list[_FusionEntry] = []
        self._packings: list[PackingEntry] = []

    def make(self, cls: type[_Op], **kwargs: Any) -> _Op:
        """Build ``cls(**kwargs)`` with its open tunables filled from this profile.

        Standalone use of what a graph's recorder applies implicitly to every
        step it constructs.
        """
        given = {name: value for name, value in kwargs.items() if value is not None}
        pinned = frozenset(given.keys() & set(cls.declaration.tunables))
        return cls(**{**self.tunables_for(cls, given), **given}, pinned=pinned)

    def add(self, cls: type, **fields: Any) -> None:
        """Add an entry for ``cls``.

        ``param()`` values to match (one left out matches any value) and
        ``tunable()`` values to give.
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
        versions: Iterable[Version] | None = None,
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

        Args:
            versions: The graph versions (``Recording.version``) the entry
                applies in, as a packing entry's own; every version where
                None.

        Raises:
            TypeError: Fewer than two steps are given, no version is given
                (an empty ``versions``, not None), a dim is not a
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
        scope = None if versions is None else frozenset(versions)
        if scope is not None and not scope:
            raise TypeError("a fusion entry names at least one version, or None")
        self._fusions.append((kind, resolved, tuple(edges), scope))

    def add_packing(
        self,
        members: Sequence[_FusionStep],
        versions: Iterable[Version] | None = None,
    ) -> None:
        """Add a packing entry: the designs of ``members``' shapes (each
        ``(operator class, dims)`` or ``(operator class, dims, tunables)``,
        matched as a fusion's steps are) share one device configuration in
        a full ELF wherever a version runs them. ``tunables``, where a member
        gives them, are what every step of its shape takes in such a version.

        Args:
            versions: The graph versions (``Recording.version``) the entry
                applies in; every version where None.

        Raises:
            TypeError: Fewer than two members or no version are given, a dim
                is not a non-tunable ``param()`` of its class, or a name in
                ``tunables`` is not a ``tunable()`` of its class.
        """
        if len(members) < 2:
            raise TypeError("a packing entry needs at least two members")
        scope = None if versions is None else frozenset(versions)
        if scope is not None and not scope:
            raise TypeError("a packing entry names at least one version, or None")
        self._packings.append(PackingEntry(self._members(members), scope))

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
        version: Version | None = None,
    ) -> bool:
        """Whether this profile fuses ``steps`` (resolved operators, in
        order) of ``kind``, wired by ``edges`` (local indices), in
        ``version`` (``Recording.version``): a fusion entry of the same
        kind, length and wiring whose steps' classes and dims
        (``Profile.dims``, ``Profile.matches``) match them, in order, and
        whose own ``versions`` names ``version`` or names none. ``version``
        left out matches any entry regardless of its own scope: only a
        caller that tracks one (``chosen_folds``) need give it.
        """
        return self._matching(kind, steps, edges, version) is not None

    def fusion_tunables(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
        version: Version | None = None,
    ) -> list[dict[str, Any] | None] | None:
        """The matching fusion entry's per-step tunables (``add_fusion``'s
        ``tunables``), in order; None where no entry matches ``kind``,
        ``steps``, ``edges`` and ``version`` (``fused``). A step's own entry
        is None where it keeps what it takes unfused.
        """
        entry = self._matching(kind, steps, edges, version)
        return None if entry is None else [t for _, _, t in entry]

    def _matching(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
        version: Version | None = None,
    ) -> tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...] | None:
        step_dims = [self.dims(type(s), vars(s)) for s in steps]
        edges = tuple(edges)
        return next(
            (
                entry_steps
                for entry_kind, entry_steps, entry_edges, entry_versions in self._fusions
                if entry_kind is kind
                and len(entry_steps) == len(steps)
                and entry_edges == edges
                and (entry_versions is None or version in entry_versions)
                and all(
                    isinstance(s, cls) and self.matches(matched, dims)
                    for s, (cls, matched, _), dims in zip(steps, entry_steps, step_dims)
                )
            ),
            None,
        )

    def fusions(self) -> list[_FusionEntry]:
        """Each fusion entry as ``(kind, steps, edges, versions)``, ``steps``
        each ``(operator class, dims, tunables)``, in the order added."""
        return list(self._fusions)

    def packings_of(
        self, op: Operator, version: Version
    ) -> list[tuple[int, int, dict[str, Any] | None]]:
        """Each packing entry applying in ``version`` with a member matching
        ``op`` (a resolved operator, by class and dims), in the order added,
        as its index in ``packings()``, that member's index and its tunables.
        Two models sharing a profile can name one shape in different entries
        (the same MLP width); ``graph.packing.apply`` picks among them.
        """
        dims = self.dims(type(op), vars(op))
        found = []
        for index, entry in enumerate(self._packings):
            if entry.versions is not None and version not in entry.versions:
                continue
            for member, (cls, matched, tunables) in enumerate(entry.members):
                if isinstance(op, cls) and self.matches(matched, dims):
                    found.append((index, member, tunables))
                    break
        return found

    def packings(self) -> list[PackingEntry]:
        """Each packing entry, in the order added."""
        return list(self._packings)

    def tunables_for(self, cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """Resolve the tunables for the ``cls`` a call with ``given`` keywords makes.

        Each comes from the most specific entry naming it.
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
    def dims(kind: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """Collect every dimension (``param()``) a ``kind`` call with ``given`` makes.

        This is what an entry is matched against: one it leaves out is its
        default, ``None`` where a function computes it.
        """
        dims = {}
        for name, p in kind.declaration.params.items():
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
        """Load the profile ``save`` wrote to ``path``."""
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
            if (
                not {"kind", "steps", "edges"}
                <= set(fusion)
                <= {
                    "kind",
                    "steps",
                    "edges",
                    "versions",
                }
            ):
                raise ValueError(
                    f"{path}: a fusion is {{'kind': ..., 'steps': [...], "
                    f"'edges': [...]}}, with 'versions': [{{input: [shape, "
                    f"dtype]}}, ...] where it applies in only some of a "
                    f"graph's versions"
                )
            edges = [tuple(e) for e in fusion["edges"]]
            profile.add_fusion(
                FusionKind(fusion["kind"]),
                members(fusion["steps"]),
                edges,
                _load_versions(fusion.get("versions")),
            )
        for packing in data.get("packings", ()):
            if not isinstance(packing, dict) or not {"members"} <= set(packing) <= {
                "versions",
                "members",
            }:
                raise ValueError(
                    f"{path}: a packing is {{'members': [...]}}, with "
                    f"'versions': [{{input: [shape, dtype]}}, ...] where it "
                    f"applies in only some of a graph's versions"
                )
            profile.add_packing(
                members(packing["members"]), _load_versions(packing.get("versions"))
            )
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
                    **_dump_versions(versions),
                }
            )
            for kind, steps, edges, versions in self._fusions
        ]
        packing_lines = [
            json.dumps(
                {
                    **_dump_versions(p.versions),
                    "members": members(p.members),
                }
            )
            for p in self._packings
        ]
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
