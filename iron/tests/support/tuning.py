# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What the transformation tests share: the mark for a type IRON does not build yet."""

import pytest

unbuilt = pytest.mark.xfail(
    strict=True,
    raises=NotImplementedError,
    reason="not built yet: the composition contract's stubs raise",
)
