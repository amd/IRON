# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Target: what an operator's array is built against besides itself."""

from __future__ import annotations

from typing import Any

import numpy as np
from aie.iron import WorkerRuntimeBarrier


class Target:
    """What an operator's ``array()`` is given besides the operator itself.

    The device, the image the array is built for, and what the build must
    be told of: the barriers the preamble releases and the objects
    ``register`` hands the Runtime.
    """

    # One bank of a core's local memory. AIE2 and AIE2P both have eight 8 KB
    # banks, and a fifo object spanning more than one cannot be double-
    # buffered in what is left; the target model gives the total
    # (Device.core_memory_bytes) but not the banking.
    L1_BANK_BYTES = 8192

    def __init__(self, dev, image: str = "elf"):
        self.dev = dev
        # "elf": per-call values reach the array through the parameter
        # scratchpad. "xclbin": an xclbin run has none; they are dispatch-
        # time scalars of the sequence, and a core-read value is a resident
        # the sequence writes (bind it to the runtime-parameter buffer).
        self.image = image
        self.barriers: list[Any] = []
        self.registered: list[Any] = []

    @classmethod
    def fifo_depth(cls, elements: int, dtype) -> int:
        """The depth a core-side fifo of ``elements``-long objects can have:
        two, or one when an object spans more than a bank.
        """
        return 1 if elements * np.dtype(dtype).itemsize > cls.L1_BANK_BYTES else 2

    def barrier(self, initial_value: int = 0):
        """A worker/runtime barrier the preamble sets to 1 after writing residents."""
        b = WorkerRuntimeBarrier(initial_value)
        self.barriers.append(b)
        return b

    def register(self, obj):
        """An explicit ``Flow``, ``Lock``, ``TileDma`` or ``Buffer`` the
        runtime must know of; returns it.

        A fifo reaches the program through its handles and a buffer through
        the worker that takes it. These reach it through neither: a flow
        only the sequence transfers on, a lock only DMA descriptors and the
        sequence touch, a buffer only the sequence's DMA chains address. The
        build hands each to the Runtime (``add_flow``, ``add_lock``,
        ``add_tile_dma``, ``add_buffer``) before the program resolves.
        """
        self.registered.append(obj)
        return obj
