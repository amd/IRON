# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Target: what an operator's array is built against besides itself."""

from __future__ import annotations

from dataclasses import dataclass
from typing import Any, ClassVar

import numpy as np


@dataclass(frozen=True)
class Target:
    """What an operator's ``array()`` is given besides the operator itself.

    Attributes:
        dev: The device the array is built for.
        image: ``"elf"``, where per-call values reach the array through the
            parameter scratchpad, or ``"xclbin"``, which has none: there
            they are dispatch-time scalars of the sequence, and a core-read
            value is a resident the sequence writes.
    """

    dev: Any
    image: str = "elf"

    # AIE2 and AIE2P both have eight 8 KB banks of core memory; the target
    # model gives the total (Device.core_memory_bytes) but not the banking.
    L1_BANK_BYTES: ClassVar[int] = 8192

    @classmethod
    def fifo_depth(cls, elements: int, dtype) -> int:
        """The depth a core-side fifo of ``elements``-long objects can have:
        two, or one when an object spans more than a bank.
        """
        return 1 if elements * np.dtype(dtype).itemsize > cls.L1_BANK_BYTES else 2
