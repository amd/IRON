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

# A fusion entry: ``kind`` steps, each ``(operator class, dims)`` in order,
# wired by ``edges`` (local indices into ``steps``, ``(producer, output,
# consumer, input)``); dims are matched the same way a tunable entry's are
# (``Profile.dims``, ``Profile.matches``).
_FusionEntry = tuple[
    FusionKind,
    tuple[tuple[type, dict[str, Any]], ...],
    tuple[tuple[int, str, int, str], ...],
]


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
    matched the same way, by class and dims alone (no tunable, since a
    fusion is not a value).
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []
        self._fusions: list[_FusionEntry] = []

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
        steps: Sequence[tuple[type, Mapping[str, Any] | None]],
        edges: Sequence[tuple[int, str, int, str]],
    ) -> None:
        """Add a fusion entry: ``kind`` steps (each ``(operator class, dims)``,
        in order) run as one device configuration, wired by ``edges`` (local
        indices into ``steps``, ``producer``'s drained ``output`` into
        ``consumer``'s filled ``input``); each step matches by class and dims
        (a dim left out matches any, a subclass its base's, as a tunable
        entry does).

        Raises:
            TypeError: Fewer than two steps are given, a dim is not a
                non-tunable ``param()`` of its class, an edge names a step
                out of range or itself, or either side of an edge declares
                no such operand.
        """
        if len(steps) < 2:
            raise TypeError("a fusion entry needs at least two steps")
        resolved: list[tuple[type, dict[str, Any]]] = []
        for cls, dims in steps:
            dims = dict(dims or {})
            unknown = [
                name
                for name in dims
                if name not in cls.declaration.params
                or cls.declaration.params[name].tunable
            ]
            if unknown:
                raise TypeError(f"{cls.__name__} declares no dim {unknown}")
            resolved.append((cls, dims))
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
        self._fusions.append((kind, tuple(resolved), tuple(edges)))

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
        step_dims = [self.dims(type(s), vars(s)) for s in steps]
        edges = tuple(edges)
        return any(
            entry_kind is kind
            and len(entry_steps) == len(steps)
            and entry_edges == edges
            and all(
                isinstance(s, cls) and self.matches(matched, dims)
                for s, (cls, matched), dims in zip(steps, entry_steps, step_dims)
            )
            for entry_kind, entry_steps, entry_edges in self._fusions
        )

    def fusions(self) -> list[_FusionEntry]:
        """Each fusion entry as ``(kind, steps, edges)``, ``steps`` each
        ``(operator class, dims)``, in the order added."""
        return list(self._fusions)

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
        """Whether an entry's ``matched`` dimensions cover ``dims``."""
        return all(name in dims and dims[name] == v for name, v in matched.items())

    @classmethod
    def load(cls, path: str | Path) -> Profile:
        """The profile ``save`` wrote to ``path``."""
        from ...operators import CATALOG  # the operators import this module

        with open(path) as f:
            data = json.load(f)
        if not isinstance(data, dict) or not {"entries"} <= set(data) <= {
            "entries",
            "fusions",
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
        for fusion in data.get("fusions", ()):
            if set(fusion) != {"kind", "steps", "edges"}:
                raise ValueError(
                    f"{path}: a fusion is {{'kind': ..., 'steps': [...], "
                    f"'edges': [...]}}"
                )
            steps = []
            for entry in fusion["steps"]:
                fields = dict(entry)
                name = fields.pop("operator")
                if name not in CATALOG:
                    raise ValueError(f"{path}: no operator {name!r} in iron.operators")
                op_cls = CATALOG[name]
                steps.append((op_cls, _with_enum_fields(op_cls, fields)))
            edges = [tuple(e) for e in fusion["edges"]]
            profile.add_fusion(FusionKind(fusion["kind"]), steps, edges)
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
        lines = []
        for cls, dims, tunables in self._entries:
            if cls not in names:
                raise ValueError(f"{cls.__qualname__} is not in iron.operators.CATALOG")
            name = names[cls]
            lines.append(json.dumps({"operator": name, **dims, **tunables}))
        fusion_lines = []
        for kind, steps, edges in self._fusions:
            for cls, _ in steps:
                if cls not in names:
                    raise ValueError(
                        f"{cls.__qualname__} is not in iron.operators.CATALOG"
                    )
            fusion_lines.append(
                json.dumps(
                    {
                        "kind": kind.value,
                        "steps": [
                            {"operator": names[cls], **dims} for cls, dims in steps
                        ],
                        "edges": [list(e) for e in edges],
                    }
                )
            )
        body = '{"entries": [\n  ' + ",\n  ".join(lines) + "\n]"
        if fusion_lines:
            body += ',\n"fusions": [\n  ' + ",\n  ".join(fusion_lines) + "\n]"
        with open(path, "w") as f:
            f.write(body + "}\n")

    def __iter__(self) -> Iterator[tuple[type, dict[str, Any], dict[str, Any]]]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        names = dict.fromkeys(cls.__name__ for cls, _, _ in self._entries)
        return f"Profile({', '.join(names)})"
