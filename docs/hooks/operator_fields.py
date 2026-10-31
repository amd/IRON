# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""A griffe extension documenting each IRON operator by its declaration.

An operator's constructor is mlir-aie's ``Operator.__init__(**given)``; what
it takes is the class body's ``param()`` and ``tunable()`` fields, as a
dataclass's are. Each ``Operator`` subclass gets an ``__init__`` of those
fields, an ``Args`` entry for each and an ``Attributes`` entry for each
operand and per-call value, described by the comment above its declaration.
"""

from collections.abc import Iterator
from typing import Any

import griffe

OPERATOR = "iron.common.declare.operator.Operator"
ARGUMENTS = {"param", "tunable"}
MEMBERS = {"per_call", "In", "Out", "InOut"}


class OperatorFields(griffe.Extension):
    """Gives every ``Operator`` subclass its declared signature and fields."""

    def on_package(
        self, *, pkg: griffe.Module, loader: griffe.GriffeLoader, **kwargs: Any
    ) -> None:
        """Document every operator class once the whole package is loaded.

        Args:
            pkg: The package loaded.
            loader: The loader, whose docstring parser a new docstring takes.
            **kwargs: The rest of griffe's hook arguments.
        """
        for cls in self.classes(pkg):
            mro = cls.mro()
            if all(base.path != OPERATOR for base in mro):
                continue
            fields: dict[str, tuple[griffe.Attribute, str, dict[str, str]]] = {}
            for owner in [*reversed(mro), cls]:
                for member in owner.members.values():
                    if member.is_alias or not member.is_attribute:
                        continue
                    call = member.value
                    if not isinstance(call, griffe.ExprCall) or not isinstance(
                        call.function, (griffe.ExprName, griffe.ExprAttribute)
                    ):
                        continue
                    module, _, kind = call.function.canonical_path.rpartition(".")
                    if module.startswith("aie.") and kind in ARGUMENTS | MEMBERS:
                        keywords = {
                            arg.name: str(arg.value)
                            for arg in call.arguments
                            if isinstance(arg, griffe.ExprKeyword)
                        }
                        fields[member.name] = (member, kind, keywords)
            if fields:
                self.document(cls, fields, loader)

    def classes(self, module: griffe.Module) -> Iterator[griffe.Class]:
        """Yield every class defined in ``module`` and its submodules.

        Args:
            module: The module walked.
        """
        for member in module.members.values():
            if member.is_alias:
                continue
            if isinstance(member, griffe.Module):
                yield from self.classes(member)
            elif isinstance(member, griffe.Class):
                yield member

    def document(
        self,
        cls: griffe.Class,
        fields: dict[str, tuple[griffe.Attribute, str, dict[str, str]]],
        loader: griffe.GriffeLoader,
    ) -> None:
        """Set ``cls``'s ``__init__`` and append its fields to its docstring.

        Args:
            cls: The operator class.
            fields: Each declared field by name: its attribute, its kind
                (``param``, ``tunable``, ``per_call``, ``In``, ...) and its
                declaration's keywords.
            loader: The loader, whose docstring parser a new docstring takes.
        """
        parameters = griffe.Parameters()
        args, attributes = [], []
        for name, (attr, kind, keywords) in fields.items():
            lines = attr.module.lines
            at = attr.lineno - 2
            comment = []
            while at >= 0 and lines[at].lstrip().startswith("#"):
                comment.insert(0, lines[at].strip().lstrip("#").strip())
                at -= 1
            note = " ".join(comment)
            if kind in MEMBERS:
                what = f"``{attr.value}``" if kind != "per_call" else "Per call."
                attributes.append(f"    {name}: {' '.join(filter(None, (what, note)))}")
                continue
            if keywords.get("init") == "False":
                continue
            if kind == "tunable":
                default = "None"
                what = (
                    "Tunable: the call's, else the profile's, else ``resolve(dev)``'s"
                )
                what += (
                    f", else ``{keywords['default']}``."
                    if "default" in keywords
                    else "."
                )
            elif "derive" in keywords:
                default = keywords["derive"]
                what = "Derived where not given; a given value must equal it."
            else:
                default = keywords.get("default")
                what = ""
            parameters.add(
                griffe.Parameter(
                    name,
                    annotation=attr.annotation,
                    kind=griffe.ParameterKind.keyword_only,
                    default=default,
                )
            )
            args.append(f"    {name}: {' '.join(filter(None, (what, note)))}")
        if "__init__" not in cls.members:
            cls.set_member(
                "__init__",
                griffe.Function(
                    "__init__",
                    parameters=parameters,
                    returns="None",
                    lineno=cls.lineno,
                    endlineno=cls.lineno,
                ),
            )
        sections = [cls.docstring.value if cls.docstring else ""]
        if args:
            sections.append("Args:\n" + "\n".join(args))
        if attributes:
            sections.append("Attributes:\n" + "\n".join(attributes))
        cls.docstring = griffe.Docstring(
            "\n\n".join(s for s in sections if s),
            lineno=cls.docstring.lineno if cls.docstring else cls.lineno,
            parent=cls,
            parser=loader.docstring_parser,
            parser_options=loader.docstring_options,
        )
