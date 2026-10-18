# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Importing one operator must not import the rest of the catalog.

``iron.operators`` re-exports lazily (PEP 562), so ``from iron.operators import
GEMM`` pulls in ``iron.operators.gemm`` and nothing else. Each check runs in
a fresh interpreter, since ``sys.modules`` holds what the whole session
imported, and covers every entry of ``_OPERATOR_MODULES``.
"""

import subprocess
import sys

import pytest

import iron
from iron.operators import _OPERATOR_MODULES


def _modules_after_importing(name):
    """Import `name` from the catalog in a fresh interpreter; list what came with it.

    `name` is a catalog key: a bare name (``"GEMM"``) or a dotted one
    (``"flm.ProjectionGEMM"``, ``iron.operators.flm``'s own catalog under its
    prefix), which a real caller imports as ``from iron.operators.flm
    import ProjectionGEMM``, not as a single dotted import name (invalid syntax).
    """
    prefix, _, bare = name.rpartition(".")
    package = f"iron.operators.{prefix}" if prefix else "iron.operators"
    program = (
        "import sys\n"
        f"from {package} import {bare}\n"
        # Every export is a class carrying its own name.
        f"assert {bare}.__name__ == {bare!r}, {bare}.__name__\n"
        # Only the operator modules, named as the catalog names them:
        # importing one necessarily creates the package around it, which says
        # nothing about laziness.
        "from iron.operators import _OPERATOR_MODULES\n"
        "known = {f'iron.operators.{m}' for m in _OPERATOR_MODULES.values()}\n"
        "print('\\n'.join(sorted(known & set(sys.modules))))\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", program], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    return set(result.stdout.split())


#: flm.ProjectionGEMM names Clamp, Sigmoid and
#: SiLU directly, by module, to recognize a fused epilogue's consumer
#: (isinstance checks): eager by design, not a lazy-catalog regression.
_NAMES_OTHER_OPERATOR_TYPES = {"flm.ProjectionGEMM"}


def _is_composite(name):
    """Whether `name` is built from other operators rather than from a kernel.

    A composite is a graph (an ``iron.Graph``, not an ``Operator``): its
    body calls other operators, so importing it must import them. That
    is composition, not an eager catalog, and the two need different
    expectations.
    """
    from iron import operators

    return issubclass(getattr(operators, name), iron.Graph) or (
        name in _NAMES_OTHER_OPERATOR_TYPES
    )


@pytest.mark.parametrize("name", sorted(_OPERATOR_MODULES))
def test_importing_one_operator_imports_no_unrelated_operator(name):
    own = f"iron.operators.{_OPERATOR_MODULES[name]}"
    imported = _modules_after_importing(name)
    others = sorted(imported - {own})

    if not _is_composite(name):
        assert (
            not others
        ), f"importing {name} also imported {others}; the catalog is not lazy"
    else:
        # A composite may import its parts, but never the whole catalog --
        # that is the regression this guards against.
        catalog = {f"iron.operators.{m}" for m in _OPERATOR_MODULES.values()}
        assert len(imported) < len(catalog), (
            f"importing {name} imported the entire catalog ({sorted(imported)}); "
            "a composite should pull in only the operators it is built from"
        )


def test_the_check_can_observe_an_import():
    """Guard the guard.

    Every assertion above is about a module being *absent*, so a subprocess
    that silently imported nothing -- or a name typo -- would make them all
    vacuously true. This pins that the probe does observe the module the
    operator legitimately needs.
    """
    imported = _modules_after_importing("GEMM")
    assert "iron.operators.gemm" in imported


#: What IRON does not require: recording a golden's packages and the
#: examples' tokenizers. Nothing a user imports may ask for them.
_RECORDING_ONLY = ("torch", "torchvision", "transformers", "tokenizers")


def _heavy_imports_asked_for(modules):
    """The `_RECORDING_ONLY` packages a fresh interpreter is asked to import
    while it imports `modules`, whether or not they are installed.
    """
    program = (
        "import importlib, sys\n"
        "asked = set()\n"
        "class Watch:\n"
        "    def find_spec(self, name, path=None, target=None):\n"
        f"        if name.split('.')[0] in {_RECORDING_ONLY!r}:\n"
        "            asked.add(name.split('.')[0])\n"
        "sys.meta_path.insert(0, Watch())\n"
        f"for m in {modules!r}:\n"
        "    importlib.import_module(m)\n"
        "print(' '.join(sorted(asked)))\n"
    )
    result = subprocess.run(
        [sys.executable, "-c", program], capture_output=True, text=True
    )
    assert result.returncode == 0, result.stderr
    return result.stdout.split()


def _user_modules():
    """iron, its functions and model library, and every application module
    but the transformers builders (``hugging_face``) only tests import.
    """
    import pkgutil

    import iron.applications

    apps = [
        m.name
        for m in pkgutil.walk_packages(iron.applications.__path__, "iron.applications.")
        if not m.name.endswith(".hugging_face")
    ]
    return ["iron", "iron.functional", "iron.lm", "iron.operators", *apps]


def test_importing_iron_and_its_applications_imports_no_torch_or_transformers():
    asked = _heavy_imports_asked_for(_user_modules())
    assert not asked, f"importing IRON asked for {asked}; import them lazily"


def test_the_heavy_import_check_can_observe_one():
    """Guard the guard: a builder that does import transformers is seen."""
    pytest.importorskip("transformers")
    module = "iron.applications.embedding_gemma2.hugging_face"
    assert "transformers" in _heavy_imports_asked_for([module])
