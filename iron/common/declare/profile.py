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

_FusionStep = (
    tuple[type, Mapping[str, Any] | None]
    | tuple[type, Mapping[str, Any] | None, Mapping[str, Any] | None]
)


@dataclasses.dataclass(frozen=True)
class FusionEntry:
    """Steps that run as one device configuration, each ``(operator class, dims, tunables)``.

    ``edges`` wire them on-chip as ``(producer, output, consumer, input)``, local indices into
    ``steps``; ``versions`` limits where this applies, every version where None; a ``phased``
    stream or staged fusion runs one sequence per phase (``Fusion.phased``).
    """

    kind: FusionKind
    steps: tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...]
    edges: tuple[tuple[int, str, int, str], ...]
    versions: frozenset[Version] | None = None
    phased: bool = False


@dataclasses.dataclass(frozen=True)
class PackingEntry:
    """Shapes whose designs share one device configuration, each ``(operator class, dims, tunables)``.

    ``tunables`` is what every step takes there, where it differs from unfused;
    ``versions`` limits where this applies, every version where None.
    """

    members: tuple[tuple[type, dict[str, Any], dict[str, Any] | None], ...]
    versions: frozenset[Version] | None = None


def _normalized(value: Any) -> Any:
    """Return ``value`` with each list (JSON's rendering of a tuple) turned recursively into a tuple.

    A dim or a tunable loaded from a file must still match the same value a live
    operator holds.
    """
    if isinstance(value, (list, tuple)):
        return tuple(_normalized(v) for v in value)
    return value


def _load_versions(versions: list | None) -> list[Version] | None:
    """Return ``versions`` turned from JSON's list form into the live ``Version`` tuples ``add_fusion``/``add_packing`` take, None kept as is.

    A version is a dict key, so it must come back exact.
    """
    if versions is None:
        return None
    return [
        tuple((n, tuple(shape), dtype) for n, (shape, dtype) in v.items())
        for v in versions
    ]


def _dump_versions(versions: frozenset[Version] | None) -> dict[str, Any]:
    """Return ``{"versions": [...]}`` for ``versions``, JSON-safe; empty where ``versions`` is None so a caller can splat it in unconditionally."""
    if versions is None:
        return {}
    return {
        "versions": [
            {n: [list(shape), dtype] for n, shape, dtype in v} for v in sorted(versions)
        ]
    }


def _with_enum_fields(cls: type, fields: dict[str, Any]) -> dict[str, Any]:
    """Return ``fields`` with each Enum-domain value turned from JSON's string into its member."""
    for key, param in cls.declaration.params.items():
        domain = param.domain
        if key in fields and isinstance(domain, type) and issubclass(domain, Enum):
            fields[key] = domain(fields[key])
    return fields


class Profile:
    """Tunable values by operator shape, as ``(cls, dims, tunables)`` entries.

    An open tunable comes from the most specific match (a dimension left out matches
    any, a subclass its base's); equally specific ones that disagree raise.

    ``fusions`` names steps to run fused as one device configuration, matched by class
    and dims; a step may give the tunables it takes fused, where they differ from
    unfused. An entry may scope to graph versions, else every version it matches.

    ``packings`` names shapes whose designs share one device configuration in a full
    ELF; a member may give the tunables it takes there. An entry may scope to graph
    versions, since one version's arrays can be another's at other extents.
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []
        self._fusions: list[FusionEntry] = []
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
        phased: bool = False,
    ) -> None:
        """Add a fusion entry: ``kind`` steps run as one device configuration, wired on-chip by ``edges``.

        Args:
            kind: How the steps run as one configuration.
            steps: Each step as ``(operator class, dims)`` or ``(operator class, dims,
                tunables)``, in order.
            edges: Each on-chip hand-off as ``(producer, output, consumer, input)``,
                local indices into ``steps``.
            versions: The graph versions (``Recording.version``) the entry
                applies in, as a packing entry's own; every version where
                None.
            phased: The fusion runs one sequence per phase (``Fusion.phased``), so its
                phases take the shim's channels in turn; stream and staged only.

        Raises:
            TypeError: ``kind`` is ``MERGE`` (a packing's form on an xclbin,
                ``add_packing``), ``phased`` is given for a kind other than stream or
                staged, fewer than two steps are given, no version is given
                (an empty ``versions``, not None), a dim is not a
                non-tunable ``param()`` of its class, a name in ``tunables``
                is not a ``tunable()`` of its class, an edge names a step
                out of range or itself, or either side of an edge declares
                no such operand.
        """
        if kind is FusionKind.MERGE:
            raise TypeError(
                "a merge is what a packing runs as on an xclbin: name its steps' "
                "shapes in add_packing"
            )
        if phased and kind not in (FusionKind.STREAM, FusionKind.STAGED):
            raise TypeError(f"a {kind.value} fusion has no phases to run apart")
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
        self._fusions.append(FusionEntry(kind, resolved, tuple(edges), scope, phased))

    def add_packing(
        self,
        members: Sequence[_FusionStep],
        versions: Iterable[Version] | None = None,
    ) -> None:
        """Add a packing entry: ``members``' shapes share one device configuration wherever a version runs them.

        Args:
            members: Each shape as ``(operator class, dims)`` or ``(operator class,
                dims, tunables)``.
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
        """Return ``steps`` as ``(class, dims, tunables)``, each name checked against its class's declaration."""
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
        phased: bool = False,
    ) -> bool:
        """Whether this profile fuses ``steps`` (resolved operators, in order) of ``kind``, wired by ``edges``, in ``version``.

        Matched to a fusion entry of the same kind, length, wiring and ``phased``, whose
        steps' classes and dims match in order, and whose own ``versions`` names
        ``version`` or names none.
        """
        return self._matching(kind, steps, edges, version, phased) is not None

    def fusion_tunables(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
        version: Version | None = None,
        phased: bool = False,
    ) -> list[dict[str, Any] | None] | None:
        """Return the matching fusion entry's per-step tunables (``add_fusion``'s ``tunables``), in order.

        Returns:
            None where no entry matches (``fused``); a step's own entry is None where
            it keeps what it takes unfused.
        """
        entry = self._matching(kind, steps, edges, version, phased)
        return None if entry is None else [t for _, _, t in entry.steps]

    def _matching(
        self,
        kind: FusionKind,
        steps: Sequence[Operator],
        edges: Sequence[tuple[int, str, int, str]],
        version: Version | None = None,
        phased: bool = False,
    ) -> FusionEntry | None:
        step_dims = [self.dims(type(s), vars(s)) for s in steps]
        edges = tuple(edges)
        return next(
            (
                entry
                for entry in self._fusions
                if entry.kind is kind
                and entry.phased == phased
                and len(entry.steps) == len(steps)
                and entry.edges == edges
                and (entry.versions is None or version in entry.versions)
                and all(
                    isinstance(s, cls) and self.matches(matched, dims)
                    for s, (cls, matched, _), dims in zip(steps, entry.steps, step_dims)
                )
            ),
            None,
        )

    def fusions(self) -> list[FusionEntry]:
        """Each fusion entry, in the order added."""
        return list(self._fusions)

    def packings_of(
        self, op: Operator, version: Version | None
    ) -> list[tuple[int, int, dict[str, Any] | None]]:
        """Each packing entry with a member matching ``op`` (class and dims) in ``version``, as ``(entry index, member index, tunables)``, in the order added.

        Two entries may each match ``op``, since two models sharing a profile can name
        one shape in different entries; ``graph.packing.apply`` picks among them.
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
        """Whether an entry's ``matched`` dimensions cover ``dims``, normalizing a JSON round-tripped list to compare equal to a live tuple."""
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
                if tunables is not None:
                    tunables = _with_enum_fields(op_cls, tunables)
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
                    "phased",
                }
            ) or fusion.get("phased", True) is not True:
                raise ValueError(
                    f"{path}: a fusion is {{'kind': ..., 'steps': [...], "
                    f"'edges': [...]}}, with 'versions': [{{input: [shape, "
                    f"dtype]}}, ...] where it applies in only some of a "
                    f"graph's versions, and 'phased': true where it runs a "
                    f"sequence per phase"
                )
            edges = [tuple(e) for e in fusion["edges"]]
            profile.add_fusion(
                FusionKind(fusion["kind"]),
                members(fusion["steps"]),
                edges,
                _load_versions(fusion.get("versions")),
                phased="phased" in fusion,
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
        """Write the profile as JSON, one entry to a line, then its fusions where there are any.

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
                    "kind": f.kind.value,
                    "steps": members(f.steps),
                    "edges": [list(e) for e in f.edges],
                    **_dump_versions(f.versions),
                    **({"phased": True} if f.phased else {}),
                }
            )
            for f in self._fusions
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
        body = '{"entries": [' + ",".join(f"\n  {s}" for s in lines) + "\n]"
        if fusion_lines:
            body += ',\n"fusions": [' + ",".join(f"\n  {s}" for s in fusion_lines)
            body += "\n]"
        if packing_lines:
            body += ',\n"packings": [' + ",".join(f"\n  {s}" for s in packing_lines)
            body += "\n]"
        with open(path, "w") as f:
            f.write(body + "}\n")

    def __iter__(self) -> Iterator[tuple[type, dict[str, Any], dict[str, Any]]]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        names = dict.fromkeys(cls.__name__ for cls, _, _ in self._entries)
        return f"Profile({', '.join(names)})"
