# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The catalog's declared cases, walked once for the tests that run or lower them."""

import aie.utils as aie_utils

import iron.operators as catalog
from iron.common import Unresolvable


def declared(dev):
    """Every catalog operator that declares its cases, with each case at `dev`.

    Read from the catalog's own table, so an operator added there is covered
    without touching a test. Resolving reads the bound device, so `dev` is
    bound while the cases resolve and the previous one restored after.

    Args:
        dev: The device the cases are declared and resolved for.

    Returns:
        `(name, cls, case, unresolvable)` for each case: `unresolvable` is
        why `dev` cannot resolve it (more columns than it has, say), else
        None.
    """
    previous = aie_utils.get_current_device(probe_runtime=False)
    aie_utils.set_current_device(dev)
    try:
        cases = []
        for name in sorted(catalog._OPERATOR_MODULES):
            cls = getattr(catalog, name)
            if cls.test is None:
                continue
            for case in cls.test.resolve(cls, dev):
                try:
                    cls(**case.kwargs).resolved(dev)
                    unresolvable = None
                except Unresolvable as e:
                    unresolvable = str(e)
                cases.append((name, cls, case, unresolvable))
        return cases
    finally:
        aie_utils.set_current_device(previous)
