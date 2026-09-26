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
    # pytest's own collector takes a file that matches ``python_files`` and
    # any file named on the command line, whatever its name; collecting
    # those here too would collect them twice.
    if parent.session.isinitpath(file_path):
        return None
    patterns = parent.config.getini("python_files")
    if any(fnmatch.fnmatch(file_path.name, pat) for pat in patterns):
        return None
    return pytest.Module.from_parent(parent, path=file_path)


@pytest.fixture
def npu2():
    """An eight-column NPU2 bound as the current device, the previous one
    restored after: what a test that resolves or compiles device-free needs.
    """
    import aie.utils as aie_utils
    from aie.iron.device import from_name

    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name("npu2", n_cols=8))
    yield
    aie_utils.set_current_device(previous)
