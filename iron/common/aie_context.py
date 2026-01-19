# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import logging
from pathlib import Path
import os

from .aie_device_manager import AIEDeviceManager, pyxrt
from . import compilation as comp
import aie.utils.config


class AIEContext:
    """Context for managing AIE operator compilation and runtime state"""

    def __init__(self, use_runlist=True):
        self.operators = []
        self.static_data_pool = {}
        self.device_manager = AIEDeviceManager()
        self.base_dir = Path(__file__).parent.parent.parent
        self.build_dir = Path(os.getcwd()) / "build"
        self.mlir_aie_dir = Path(aie.utils.config.root_path())
        self.peano_dir = Path(aie.utils.config.peano_install_dir())
        # Disable the XRT runlist sacrifices performance by executing kernels individually as separate xclbin invocations for easier debugging (can tell which part of runlist execution failed)
        self.use_runlist = use_runlist
        self._runtime_prepared = False

    def register_operator(self, operator):
        """Register an operator with this context"""
        if self._runtime_prepared:
            raise RuntimeError("Cannot register operators after runtime is prepared")
        operator.context = self
        self.operators.append(operator)

    def compile_all(self):
        """Compile all registered operators"""
        self.build_dir.mkdir(parents=True, exist_ok=True)
        for op in self.operators:
            op.compile()

    def prepare_runtime(self):
        """Setup XRT runtime for all registered operators"""
        if self._runtime_prepared:
            return

        for op in self.operators:
            op.set_up_runtime()

        # Pools of preallocated buffer objects; each buffer object is allocated
        # once at program start and then reused across operators where possible.
        bo_pools = {}
        page_sz = 4096
        get_pool_sz = lambda x: (x + page_sz - 1) // page_sz * page_sz

        # Allocate static buffers first
        for buffer_data in self.static_data_pool:
            logging.debug(
                f"Allocating static buffer with size {len(buffer_data)} bytes."
            )
            bo = pyxrt.bo(
                self.device_manager.device,
                len(buffer_data),
                pyxrt.bo.host_only,
                0x10000,
            )
            bo.write(np.frombuffer(buffer_data, dtype=np.uint8), 0)
            self.static_data_pool[buffer_data] = bo

        for op in self.operators:
            if len(op.kernels) == 0:
                continue

            logging.info(f"Preparing runtime for AIE operator: {op.__class__.__name__}")

            # Set up kernels
            for kernel_name, (xclbin, xclbin_kernel_name, insts) in op.kernels.items():
                handle = self.device_manager.get_kernel_handle(
                    str(xclbin.path), xclbin_kernel_name, str(insts.path)
                )
                op.xrt_kernels[kernel_name] = (
                    handle.context,
                    handle.kernel,
                    handle.insts_bo,
                    len(handle.insts),
                )

            # If multiple buffers (of the same binned size) are used in the
            # same kernel invocation OR across different invocations with shared
            # buffers, they require separate allocations.
            conflicting_buffers = {}  # map buffer -> {set of conflicting buffers}
            buffer_to_runlist_entries = {}  # map buffer -> set of runlist entry indices

            # First pass: track which buffers appear in which runlist entries
            for idx, (kernel, *args) in enumerate(op.runlist):
                for arg in args:
                    buffer_to_runlist_entries.setdefault(arg, set()).add(idx)

            # Second pass: determine conflicts
            for idx, (kernel, *args) in enumerate(op.runlist):
                for arg in args:
                    if arg in op.buffer_static_data:
                        # Static buffers never conflict
                        continue
                    pool_sz = get_pool_sz(op.buffers[arg])

                    # Buffers conflict if they're in the same runlist entry
                    conflicting_args = {
                        a for a in args if get_pool_sz(op.buffers[a]) == pool_sz
                    } - {arg}

                    # Also conflict with buffers in other runlist entries that share
                    # a buffer with this entry
                    for other_arg in args:
                        if other_arg == arg:
                            continue
                        for other_idx in buffer_to_runlist_entries.get(
                            other_arg, set()
                        ):
                            if other_idx != idx:
                                _, *other_args = op.runlist[other_idx]
                                conflicting_args.update(
                                    {
                                        a
                                        for a in other_args
                                        if get_pool_sz(op.buffers[a]) == pool_sz
                                        and a != arg
                                    }
                                )

                    conflicting_buffers[arg] = conflicting_buffers.get(
                        arg, set()
                    ).union(conflicting_args)

            # Allocate buffers
            buffer_allocations = {}
            for buffer_name, buffer_min_size in op.buffers.items():
                if buffer_name in op.buffer_static_data:
                    static_data = op.buffer_static_data[buffer_name]
                    op.buffer_bos[buffer_name] = self.static_data_pool[static_data]
                    continue

                alloc_pool = get_pool_sz(buffer_min_size)
                alloc_idx = 0
                for conflict in conflicting_buffers.get(buffer_name, set()):
                    if conflict not in buffer_allocations:
                        continue
                    conflict_pool, conflict_idx = buffer_allocations[conflict]
                    alloc_idx = max(alloc_idx, conflict_idx + 1)

                assert 0 <= alloc_idx < len(bo_pools.get(alloc_pool, [])) + 1
                if alloc_idx == len(bo_pools.get(alloc_pool, [])):
                    bo = pyxrt.bo(
                        self.device_manager.device,
                        alloc_pool,
                        pyxrt.bo.host_only,
                        0x10000,
                    )
                    bo_pools.setdefault(alloc_pool, []).append(bo)

                buffer_allocations[buffer_name] = (alloc_pool, alloc_idx)
                op.buffer_bos[buffer_name] = bo_pools[alloc_pool][alloc_idx]

            # Setup runlist
            _, (first_xclbin, first_xclbin_kernel_name, first_insts) = next(
                iter(op.kernels.items())
            )
            handle = self.device_manager.get_kernel_handle(
                str(first_xclbin.path), first_xclbin_kernel_name, str(first_insts.path)
            )
            context = handle.context
            if self.use_runlist:
                op.xrt_runlist = pyxrt.runlist(context)
                for i, (kernel_name, *buffer_args) in enumerate(op.runlist):
                    this_context, xrt_kernel, insts_bo, insts_len = op.xrt_kernels[
                        kernel_name
                    ]
                    assert this_context == context
                    opcode = 3
                    run = pyxrt.run(xrt_kernel)
                    run.set_arg(0, opcode)
                    run.set_arg(1, insts_bo)
                    run.set_arg(2, insts_len)
                    for j, buffer_arg in enumerate(buffer_args):
                        run.set_arg(j + 3, op.buffer_bos[buffer_arg])
                    op.xrt_runlist.add(run)
            else:
                op.xrt_runlist = None

        # Log allocation info
        bo_count = sum(len(pool) for pool in bo_pools.values())
        bo_footprint = sum(len(pool) * pool_sz for pool_sz, pool in bo_pools.items())
        logging.info(
            f"Allocated {bo_count} total buffer objects with a total memory footprint of "
            + (
                f"{bo_footprint//1024//1024} MiB."
                if bo_footprint >= 1024 * 1024
                else f"{bo_footprint//1024} KiB."
            )
        )
        static_data_footprint = sum(len(data) for data in self.static_data_pool)
        logging.info(
            f"Allocated {len(self.static_data_pool)} static buffers with a total memory footprint of "
            + (
                f"{static_data_footprint//1024//1024} MiB."
                if static_data_footprint >= 1024 * 1024
                else f"{static_data_footprint//1024} KiB."
            )
        )

        self._runtime_prepared = True
