# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Profiles: knob values for operator shapes, applied as an operator is made.

A :class:`Profile` is data: entries that name a class, some of its
dimensions and values for its knobs. Applied in a ``with`` scope, it fills
the knobs a call leaves open as the operator is constructed, before
:meth:`~.operator.Operator.resolve` sees it, so the precedence is the
explicit call-site value, then the profile, then the knob's declared
default or the value resolution proposes. A tuner writes a profile and a
graph applies it; operator classes know nothing about profiles.

On disk a profile is JSON, one object per entry holding what :meth:`Profile.add`
takes: ``"operator"``, the class's name in :mod:`iron.operators`, then its
dimensions and knobs as keywords::

    {"entries": [
      {"operator": "GEMV", "M": 2048, "K": 8192, "tile_size_input": 1},
      {"operator": "MHA", "seq_pad": 2048, "num_pipelines": 8}
    ]}

An entry matches on what the call constructs the operator with: its
keywords and, in a graph, the extents inferred from its operands. A
dimension whose default follows from another (MHA's ``seq_len``, from the
``seq_pad`` its shape gives) is not yet known then, so key by the one given.
"""

from __future__ import annotations

import contextvars
import dataclasses
import json
from pathlib import Path
from typing import Any, Iterator, Mapping

from ... import operators
from .field import _tier_of

_active: contextvars.ContextVar[Profile | None] = contextvars.ContextVar(
    "iron.profile", default=None
)
# The tokens of the scopes entered in this context, innermost last: kept
# here rather than on the profile, which threads may share.
_entered: contextvars.ContextVar[tuple[contextvars.Token, ...]] = (
    contextvars.ContextVar("iron.profile.entered", default=())
)


def current() -> Profile | None:
    """The profile applied in this scope, if any."""
    return _active.get()


@dataclasses.dataclass(frozen=True)
class Entry:
    """One line of a profile: the knobs for the operators ``dims`` selects."""

    cls: type
    dims: dict[str, Any]  # param() values to match; a dimension left out matches any
    knobs: dict[str, Any]  # auto() values to give

    def matches(self, cls: type, dims: Mapping[str, Any]) -> bool:
        return issubclass(cls, self.cls) and all(
            name in dims and dims[name] == value for name, value in self.dims.items()
        )


def _dims_of(cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
    """The dimensions of the ``cls`` a call with ``given`` keywords constructs."""
    dims = {}
    for f in dataclasses.fields(cls):
        if _tier_of(f) != "param":
            continue
        if f.name in given:
            dims[f.name] = given[f.name]
        elif f.default is not dataclasses.MISSING:
            dims[f.name] = f.default
        elif f.default_factory is not dataclasses.MISSING:
            dims[f.name] = f.default_factory()
    return dims


class Profile:
    """Knob values for operators, keyed by their shape.

    :meth:`add` takes a class and keyword fields: its ``param()`` fields
    select the operators the entry is for (one left out matches any value),
    its ``auto()`` fields are the values given. Within ``with profile:``, a
    call that constructs an operator and leaves a knob open takes it from
    the most specific entry that matches the class and the dimensions and
    names that knob, whether the knob has a declared default or not; a knob
    the call gives is never touched. Two entries of equal specificity that
    name one knob for one operator and disagree are an error, raised at
    that call. A subclass matches its base's entries.
    """

    def __init__(self) -> None:
        self._entries: list[Entry] = []

    def add(self, cls: type, **fields: Any) -> None:
        """Add an entry for ``cls``: dimensions to match and knobs to give."""
        tiers = {f.name: _tier_of(f) for f in dataclasses.fields(cls)}
        dims, knobs, unknown = {}, {}, []
        for name, value in fields.items():
            tier = tiers.get(name)
            if tier == "param":
                dims[name] = value
            elif tier == "auto":
                knobs[name] = value
            else:
                unknown.append(name)
        if unknown:
            raise TypeError(f"{cls.__name__} declares no field {unknown}")
        if not knobs:
            raise TypeError(f"an entry for {cls.__name__} must give a knob")
        self._entries.append(Entry(cls, dims, knobs))

    def knobs_for(self, cls: type, given: Mapping[str, Any]) -> dict[str, Any]:
        """The knobs for the ``cls`` a call with ``given`` keywords makes,
        each from the most specific entry naming it.
        """
        dims = _dims_of(cls, given)
        chosen: dict[str, tuple[int, Any]] = {}
        for entry in self._entries:
            if not entry.matches(cls, dims):
                continue
            rank = len(entry.dims)
            for name, value in entry.knobs.items():
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
        """The knobs the profile gives an operator of ``op``'s class and shape."""
        return self.knobs_for(
            type(op), {f.name: getattr(op, f.name) for f in dataclasses.fields(op)}
        )

    @classmethod
    def load(cls, path: str | Path) -> Profile:
        """The profile :meth:`save` wrote to ``path``; each entry is checked
        as :meth:`add` checks it.
        """
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
            if getattr(operators, name, None) is not entry.cls:
                raise ValueError(f"{name} is not iron.operators.{name}")
            lines.append(json.dumps({"operator": name, **entry.dims, **entry.knobs}))
        with open(path, "w") as f:
            f.write('{"entries": [\n  ' + ",\n  ".join(lines) + "\n]}\n")

    def __iter__(self) -> Iterator[Entry]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __enter__(self) -> Profile:
        _entered.set(_entered.get() + (_active.set(self),))
        return self

    def __exit__(self, *exc) -> None:
        *outer, token = _entered.get()
        _active.reset(token)
        _entered.set(tuple(outer))
