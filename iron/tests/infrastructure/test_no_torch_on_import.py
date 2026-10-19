# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Importing IRON never imports torch or transformers."""

import subprocess
import sys

import pytest

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
