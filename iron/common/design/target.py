# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Target: the device and the kernel tree, as one handle."""

from __future__ import annotations

from functools import partial
from pathlib import Path
from typing import Any

from aie.iron import Buffer, WorkerRuntimeBarrier

from ..kernels import declare_kernel, target_arch


class Target:
    """What an operator's ``array()`` is given besides the operator itself.

    Carries the device and the kernel tree. ``kernel`` is
    :func:`~iron.common.kernels.declare_kernel`, whose digest prefix keeps
    kernels apart when designs are fused, whatever else is fused with them;
    ``rtp`` is a runtime-parameter :class:`~aie.iron.Buffer`; ``register``
    hands the build what the Runtime must be told of explicitly.
    """

    def __init__(
        self,
        dev,
        kernels_dir,
        trace_size: int = 0,
        image: str = "elf",
    ):
        self.dev = dev
        self.kernels_dir = Path(kernels_dir)
        self.arch = target_arch(dev)  # "aie2" | "aie2p"
        self.trace_size = trace_size
        # "elf": per-call values reach the array through the parameter
        # scratchpad. "xclbin": an xclbin run has none; they are dispatch-
        # time scalars of the sequence, and a core-read value is a resident
        # the sequence writes (bind it to the runtime-parameter buffer).
        self.image = image
        # The function itself rather than a method: a method would restate
        # every declare_kernel parameter, and would have to track them.
        self.kernel = declare_kernel
        self.rtp = partial(Buffer, use_write_rtp=True)
        self.barriers: list[Any] = []
        self.registered: list[Any] = []

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
