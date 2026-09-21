# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""One build per case.

The repo-wide ``--iterations`` (default 5) repeats every test for timing
statistics. A lowering or a full-ELF build is deterministic and minutes
long, and its cache would make the repeats no-ops in any case, so only the
first iteration of each toolchain test is kept.
"""


def pytest_collection_modifyitems(config, items):
    keep, dropped = [], []
    for item in items:
        params = getattr(getattr(item, "callspec", None), "params", {})
        (dropped if params.get("_iteration", 0) else keep).append(item)
    if dropped:
        config.hook.pytest_deselected(items=dropped)
        items[:] = keep
