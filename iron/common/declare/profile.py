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
from pathlib import Path
from types import FunctionType
from typing import TYPE_CHECKING, Any, Iterator, Mapping, TypeVar

if TYPE_CHECKING:
    from .operator import Operator

_Op = TypeVar("_Op", bound="Operator")


class Profile:
    """Tunable values by operator shape, as ``(cls, dims, tunables)`` entries.

    An open tunable comes from the most specific match (a dimension left out
    matches any, a subclass its base's); equally specific ones that disagree
    raise.
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []

    def make(self, cls: type[_Op], **kwargs: Any) -> _Op:
        """Build ``cls(**kwargs)`` with its open tunables filled from this profile.

        Standalone use of what a graph's recorder applies implicitly to every
        step it constructs.
        """
        pinned = frozenset(
            name
            for name, value in kwargs.items()
            if name in cls.declaration.tunables and value is not None
        )
        given = {**self.tunables_for(cls, kwargs), **kwargs}
        return cls(**given, pinned=pinned)

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
        """Load the profile ``save`` wrote to ``path``."""
        from ...operators import CATALOG  # the operators import this module

        with open(path) as f:
            data = json.load(f)
        if not isinstance(data, dict) or set(data) != {"entries"}:
            raise ValueError(f"{path}: a profile is {{'entries': [...]}}")
        profile = cls()
        for entry in data["entries"]:
            fields = dict(entry)
            name = fields.pop("operator")
            if name not in CATALOG:
                raise ValueError(f"{path}: no operator {name!r} in iron.operators")
            op_cls = CATALOG[name]
            # An Enum-domain tunable is JSON's string, its member's value
            # (should 1: a Pinned member's own value, not its ordinal).
            for key, param in op_cls.declaration.params.items():
                domain = param.domain
                if (
                    key in fields
                    and isinstance(domain, type)
                    and issubclass(domain, Enum)
                ):
                    fields[key] = domain(fields[key])
            profile.add(op_cls, **fields)
        return profile

    def save(self, path: str | Path) -> None:
        """Write the profile as JSON, one entry to a line.

        Raises:
            ValueError: An entry's operator is not in ``iron.operators.CATALOG``.
        """
        from ...operators import CATALOG  # the operators import this module

        names = {cls: name for name, cls in CATALOG.items()}
        lines = []
        for cls, dims, tunables in self._entries:
            if cls not in names:
                raise ValueError(f"{cls.__qualname__} is not in iron.operators.CATALOG")
            name = names[cls]
            lines.append(json.dumps({"operator": name, **dims, **tunables}))
        with open(path, "w") as f:
            f.write('{"entries": [\n  ' + ",\n  ".join(lines) + "\n]}\n")

    def __iter__(self) -> Iterator[tuple[type, dict[str, Any], dict[str, Any]]]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        names = dict.fromkeys(cls.__name__ for cls, _, _ in self._entries)
        return f"Profile({', '.join(names)})"
