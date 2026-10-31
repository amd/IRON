# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The API site's operator signatures against each operator's own declaration."""

import dataclasses
from pathlib import Path

import pytest

from iron.operators import CATALOG

# The docs' requirements (docs/requirements-mkdocs.txt), not IRON's.
griffe = pytest.importorskip("griffe")

ROOT = Path(__file__).resolve().parents[3]


@pytest.fixture(scope="module")
def package():
    return griffe.load(
        "iron",
        search_paths=[ROOT],
        allow_inspection=False,
        docstring_parser="google",
        extensions=griffe.load_extensions(str(ROOT / "docs/hooks/operator_fields.py")),
    )


@pytest.mark.parametrize("name", sorted(CATALOG))
def test_documented_signature_is_the_declaration(package, name):
    cls = CATALOG[name]
    documented = package[f"{cls.__module__.removeprefix('iron.')}.{cls.__qualname__}"]
    declared = {n: p for n, p in cls.declaration.params.items() if p.init}
    parameters = documented.members["__init__"].parameters

    assert [p.name for p in parameters] == list(declared)
    assert [p.name for p in parameters if p.default is None] == [
        n
        for n, p in declared.items()
        if p.default is dataclasses.MISSING and p.derive is None
    ]
