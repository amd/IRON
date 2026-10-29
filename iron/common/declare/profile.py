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
from typing import TYPE_CHECKING, Any, Iterator, Mapping, TypeVar

if TYPE_CHECKING:
    from .operator import Operator

_Op = TypeVar("_Op", bound="Operator")

# A chain entry: fuse ``producer``'s output into ``consumer``'s ``input``,
# each matched on its own dims (``Profile.dims``, ``Profile.matches``).
_ChainEntry = tuple[type, dict[str, Any], type, dict[str, Any], str]


class Profile:
    """Tunable values by operator shape, as ``(cls, dims, tunables)`` entries. An
    open tunable comes from the most specific match (a dimension left out matches
    any, a subclass its base's); equally specific ones that disagree raise.

    ``chains`` names producer -> consumer edges to run fused on-chip, each
    matched the same way, by class and dims alone (no tunable, since a chain
    is not a value).
    """

    def __init__(self) -> None:
        self._entries: list[tuple[type, dict[str, Any], dict[str, Any]]] = []
        self._chains: list[_ChainEntry] = []

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

    def add_chain(
        self,
        producer: type,
        consumer: type,
        input: str,
        *,
        producer_dims: Mapping[str, Any] | None = None,
        consumer_dims: Mapping[str, Any] | None = None,
    ) -> None:
        """Add a chain entry: fuse ``producer``'s output into ``consumer``'s
        ``input`` on-chip, where each matches (a dim left out matches any,
        a subclass its base's, as a tunable entry does).

        Raises:
            TypeError: A dim is not a non-tunable ``param()`` of its class, or
                ``consumer`` declares no input ``input``.
        """
        producer_dims, consumer_dims = dict(producer_dims or {}), dict(
            consumer_dims or {}
        )
        for cls, dims in ((producer, producer_dims), (consumer, consumer_dims)):
            unknown = [
                name
                for name in dims
                if name not in cls.declaration.params
                or cls.declaration.params[name].tunable
            ]
            if unknown:
                raise TypeError(f"{cls.__name__} declares no dim {unknown}")
        if not any(m.name == input and m.fills for m in consumer.declaration.operands):
            raise TypeError(f"{consumer.__name__} declares no input {input!r}")
        self._chains.append((producer, producer_dims, consumer, consumer_dims, input))

    def chained(self, producer: Operator, consumer: Operator, input: str) -> bool:
        """Whether this profile's chains fuse ``producer``'s output into
        ``consumer``'s ``input``: a chain entry whose producer and consumer
        classes and dims (``Profile.dims``, ``Profile.matches``) match them.
        """
        p_dims = self.dims(type(producer), vars(producer))
        c_dims = self.dims(type(consumer), vars(consumer))
        return any(
            input == entry_input
            and isinstance(producer, p_cls)
            and isinstance(consumer, c_cls)
            and self.matches(p_entry, p_dims)
            and self.matches(c_entry, c_dims)
            for p_cls, p_entry, c_cls, c_entry, entry_input in self._chains
        )

    def chains(self) -> list[_ChainEntry]:
        """Each chain entry as ``(producer, producer_dims, consumer,
        consumer_dims, input)``, in the order added."""
        return list(self._chains)

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
            "chains",
        }:
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
        for chain in data.get("chains", ()):
            if set(chain) != {"producer", "consumer", "input"}:
                raise ValueError(
                    f"{path}: a chain is {{'producer': {{...}}, 'consumer': "
                    f"{{...}}, 'input': ...}}"
                )
            sides = []
            for side in (chain["producer"], chain["consumer"]):
                fields = dict(side)
                name = fields.pop("operator")
                if name not in CATALOG:
                    raise ValueError(f"{path}: no operator {name!r} in iron.operators")
                sides.append((CATALOG[name], fields))
            (producer, producer_dims), (consumer, consumer_dims) = sides
            profile.add_chain(
                producer,
                consumer,
                chain["input"],
                producer_dims=producer_dims,
                consumer_dims=consumer_dims,
            )
        return profile

    def save(self, path: str | Path) -> None:
        """Write the profile as JSON, one entry to a line, then its chains
        where there are any.

        Raises:
            ValueError: An entry's or a chain's operator is not in
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
        chain_lines = []
        for producer, producer_dims, consumer, consumer_dims, input in self._chains:
            for cls in (producer, consumer):
                if cls not in names:
                    raise ValueError(
                        f"{cls.__qualname__} is not in iron.operators.CATALOG"
                    )
            chain_lines.append(
                json.dumps(
                    {
                        "producer": {"operator": names[producer], **producer_dims},
                        "consumer": {"operator": names[consumer], **consumer_dims},
                        "input": input,
                    }
                )
            )
        body = '{"entries": [\n  ' + ",\n  ".join(lines) + "\n]"
        if chain_lines:
            body += ',\n"chains": [\n  ' + ",\n  ".join(chain_lines) + "\n]"
        with open(path, "w") as f:
            f.write(body + "}\n")

    def __iter__(self) -> Iterator[tuple[type, dict[str, Any], dict[str, Any]]]:
        return iter(self._entries)

    def __len__(self) -> int:
        return len(self._entries)

    def __repr__(self) -> str:
        names = dict.fromkeys(cls.__name__ for cls, _, _ in self._entries)
        return f"Profile({', '.join(names)})"
