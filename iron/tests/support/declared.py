# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The catalog's declared cases, walked once for the tests that run or lower them."""

import aie.utils as aie_utils

import iron.operators as catalog
from iron.common import Unresolvable


def declared(dev):
    """Every catalog operator that declares its cases, with each case at `dev`.

    Read from the catalog's own table, so an operator added there is covered
    without touching a test. A sweep may read the bound device, so `dev`
    is bound while the cases are made and the previous one restored after.
    Nothing is resolved: resolving can build kernels, which a test does when
    it runs, not when it is collected.

    Args:
        dev: The device the cases are declared for.

    Returns:
        `(name, cls, case)` for each case.
    """
    with aie_utils.set_current_device(dev):
        return [
            (name, cls, case)
            for name, cls in sorted(catalog.CATALOG.items())
            if cls.test is not None and not cls.reference_only
            for case in cls.test.resolve(cls, dev)
        ]


def unresolvable(cls, case, dev) -> str | None:
    """Why `dev` cannot resolve `case` of `cls` (more columns than it has,
    say), else None.
    """
    with aie_utils.set_current_device(dev):
        try:
            cls(**case.kwargs).resolved(dev)
        except Unresolvable as e:
            return str(e)
    return None
