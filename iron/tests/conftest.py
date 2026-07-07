# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Collection hook scoped to ``iron/tests/``.

The repo-wide ``python_files = test.py`` setting only collects files literally
named ``test.py`` (so operator directories don't sweep in ``op.py`` etc.).
Tests under ``iron/tests/`` are grouped by the subsystem they cover, so we
collect any module here (e.g. ``sequence.py``) regardless of its name.
"""

import fnmatch

import pytest

_EXCLUDED_NAMES = {"conftest.py", "__init__.py"}


def pytest_collect_file(parent, file_path):
    if file_path.suffix != ".py" or file_path.name in _EXCLUDED_NAMES:
        return None
    # Let the default collector handle files matching the configured patterns
    # (e.g. ``test.py``) to avoid double-collection.
    patterns = parent.config.getini("python_files")
    if any(fnmatch.fnmatch(file_path.name, pat) for pat in patterns):
        return None
    return pytest.Module.from_parent(parent, path=file_path)
