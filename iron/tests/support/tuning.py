# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the transformation tests share: the marks for a type IRON does not build yet, and for one that waits on a kernel."""

import pytest

unbuilt = pytest.mark.xfail(
    strict=True,
    raises=NotImplementedError,
    reason="not built yet: the composition contract's stubs raise",
)

waits_on_a_kernel = pytest.mark.xfail(
    strict=True,
    raises=ValueError,
    reason="waits on a kernel mlir-aie does not have yet (PLAN step 3): the "
    "operators refuse the shape or type it needs",
)
