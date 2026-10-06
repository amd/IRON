# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Profiles: tunable values for operator shapes, applied as an operator is made.

A call's own value wins, then the profile's, then ``Operator.resolve``. An
entry matches on what the call constructs the operator with, so a dimension
whose default follows from another (MHA's ``seq_len``) is keyed by the one
given (``seq_pad``).
"""

from __future__ import annotations

import contextvars
import dataclasses
import json
from pathlib import Path
from typing import Any, ClassVar, Iterator, Mapping

from ... import operators
from .field import Auto, Param, Tier


@dataclasses.dataclass(frozen=True)
class Entry:
    """One line of a profile: the tunables for the operators ``dims`` selects."""

    cls: type
    dims: dict[str, Any]  # param() values to match; a dimension left out matches any
    tunables: dict[str, Any]  # auto() values to give

    def matches(self, cls: type, dims: Mapping[str, Any]) -> bool:
        return issubclass(cls, self.cls) and all(
            name in dims and dims[name] == value for name, value in self.dims.items()
        )


class Profile:
    """Tunable values for operators, keyed by their shape.

    Within ``with profile:``, a tunable a call leaves open comes from the
    most specific entry naming it; entries of equal specificity that
    disagree raise. A subclass matches its base's entries.
    """

    _active: ClassVar[contextvars.ContextVar[Profile | None]] = contextvars.ContextVar(
        "iron.profile", default=None
    )
    # Per context rather than on the profile, which threads may share.
    _entered: ClassVar[contextvars.ContextVar[tuple[contextvars.Token, ...]]] = (
        contextvars.ContextVar("iron.profile.entered", default=())
    )

    def __init__(self) -> None:
        self._entries: list[Entry] = []

    @classmethod
    def current(cls) -> Profile | None:
        """The profile applied in this scope, if any."""
        return cls._active.get()

    def add(self, cls: type, **fields: Any) -> None:
        """Add an entry for ``cls``: ``param()`` fields to match (one left out
        matches any value) and ``auto()`` fields to give.
        """
        tiers = {f.name: f.metadata.get(Tier) for f in dataclasses.fields(cls)}
        dims, tunables, unknown = {}, {}, []
        for name, value in fields.items():
            tier = tiers.get(name)
            if isinstance(tier, Param):
                dims[name] = value
            elif isinstance(tier, Auto):
                tunables[name] = value
            else:
                unknown.append(name)
        if unknown:
            raise TypeError(f"{cls.__name__} declares no field {unknown}")
        if not tunables:
            raise TypeError(f"an entry for {cls.__name__} must give a tunable")
        self._entries.append(Entry(cls, dims, tunables))

    def tunables_for(self, cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """The tunables for the ``cls`` a call with ``given`` keywords makes,
        each from the most specific entry naming it.
        """
        dims = {}
        for f in dataclasses.fields(cls):
            if not isinstance(f.metadata.get(Tier), Param):
                continue
            if f.name in given:
                dims[f.name] = given[f.name]
            elif f.default is not dataclasses.MISSING:
                dims[f.name] = f.default
            elif f.default_factory is not dataclasses.MISSING:
                dims[f.name] = f.default_factory()
        chosen: dict[str, tuple[int, Any]] = {}
        for entry in self._entries:
            if not entry.matches(cls, dims):
                continue
            rank = len(entry.dims)
            for name, value in entry.tunables.items():
                if name not in chosen or rank > chosen[name][0]:
                    chosen[name] = (rank, value)
                elif rank == chosen[name][0] and chosen[name][1] != value:
                    raise ValueError(
                        f"profile is ambiguous for {cls.__name__} {dims}: "
                        f"{name}={chosen[name][1]} and {name}={value} from "
                        f"entries of equal specificity"
                    )
        return {name: value for name, (_, value) in chosen.items()}

    def lookup(self, op) -> dict[str, Any]:
        """The tunables the profile gives an operator of ``op``'s class and shape."""
        return self.tunables_for(
            type(op), {f.name: getattr(op, f.name) for f in dataclasses.fields(op)}
        )

    @classmethod
    def load(cls, path: str | Path) -> Profile:
        """The profile ``save`` wrote to ``path``."""
        with open(path) as f:
            data = json.load(f)
        if not isinstance(data, dict) or set(data) != {"entries"}:
            raise ValueError(f"{path}: a profile is {{'entries': [...]}}")
        profile = cls()
        for entry in data["entries"]:
            fields = dict(entry)
            name = fields.pop("operator")
            if name not in operators.__all__:
                raise ValueError(f"{path}: no operator {name!r} in iron.operators")
            profile.add(getattr(operators, name), **fields)
        return profile

    def save(self, path: str | Path) -> None:
        """Write the profile as JSON, one entry to a line."""
        lines = []
        for entry in self._entries:
            name = entry.cls.__name__
            if (
                name not in operators.__all__
                or getattr(operators, name) is not entry.cls
            ):
                raise ValueError(f"{name} is not iron.operators.{name}")
            lines.append(json.dumps({"operator": name, **entry.dims, **entry.tunables}))
        with open(path, "w") as f:
            f.write('{"entries": [\n  ' + ",\n  ".join(lines) + "\n]}\n")

    def __iter__(self) -> Iterator[Entry]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __enter__(self) -> Profile:
        Profile._entered.set(Profile._entered.get() + (Profile._active.set(self),))
        return self

    def __exit__(self, *exc) -> None:
        *outer, token = Profile._entered.get()
        Profile._active.reset(token)
        Profile._entered.set(tuple(outer))
