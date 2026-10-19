# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""An operator of rows whose count a graph may bound."""

from aie.iron import In, Out
from aie.utils.compile.jit.params import param, per_call, tunable, widths

from iron.common import Built, Operator


class Rows(Operator):
    """Rows of ``cols`` elements over ``lanes`` lanes; ``rows`` may be bounded."""

    rows: int = param()
    cols: int = param()
    lanes: int = tunable(default=2, domain=widths)
    valid = per_call(bounds=rows)
    count = per_call(derive=lambda op: op.valid // op.lanes)  # reads the extent
    width = per_call(derive=lambda op: op.cols)  # does not
    x = In(rows, cols, obj_shape=(1, cols), per=(lanes,))
    y = Out(rows, cols, obj_shape=(1, cols), per=(lanes,))

    def build(self) -> Built:
        return Built([])

    def reference(self, x):
        return x
