# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The base of what an operator declares besides its fields."""

from __future__ import annotations

from typing import Any, Generic, Mapping, Self, TypeVar, overload

from .shape import _DimSpec

B = TypeVar("B")  # the bound form an instance serves


class Member(Generic[B]):
    """Base of everything declared unannotated in an Operator body; on an
    instance it reads as its bound form ``B``.
    """

    name: str = ""
    owner: type | None = None
    when: _DimSpec | None = None

    def __set_name__(self, owner: type, name: str) -> None:
        self.name = name
        self.owner = owner

    @overload
    def __get__(self, instance: None, owner: type | None = None) -> Self: ...
    @overload
    def __get__(self, instance: object, owner: type | None = None) -> B: ...
    def __get__(self, instance, owner=None):
        if instance is None:
            return self
        try:
            return instance._bound[self.name]
        except (AttributeError, KeyError):
            if self.when is not None and not vars(instance)[self.when.name]:
                raise AttributeError(
                    f"{type(instance).__name__}.{self.name} is declared when="
                    f"{self.when.name}, which is False on this instance"
                ) from None
            raise AttributeError(
                f"{type(instance).__name__}.{self.name} is not bound yet"
            ) from None

    def present(self, flags: Mapping[str, Any]) -> bool:
        """Whether this member exists under ``flags``; a flag left out is its default."""
        when = self.when
        return when is None or bool(flags.get(when.name, when.default))
