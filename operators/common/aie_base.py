# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import os
from pathlib import Path
from abc import ABC, abstractmethod
import logging
import time
import torch
from ml_dtypes import bfloat16

import aie.utils.config
from . import compilation as comp
from .aie_device_manager import AIEDeviceManager, pyxrt
from .utils import numpy_to_torch, torch_to_numpy


class AIEOperatorBase(ABC):
    """Base class for AIE-accelerated operations"""

    registered_operators = []
    static_data_pool = {}  # Map bytes -> number of users

    # Global configuration
    device_manager = AIEDeviceManager()
    base_dir = Path(__file__).parent.parent.parent  # IRON base dir
    build_dir = Path(os.getcwd()) / "build"
    mlir_aie_dir = Path(aie.utils.config.root_path())
    peano_dir = Path(aie.utils.config.peano_install_dir())

    @classmethod
    def compile_all_operators(cls, dry_run=False):
        """Compile all registered AIE operators."""
        cmds = [] if dry_run else None
        if not dry_run:
            cls.build_dir.mkdir(parents=True, exist_ok=True)
        for op in cls.registered_operators:
            op.compile(dry_run=cmds)
        if dry_run:
            return cmds

    @classmethod
    def prepare_runtime(cls):
        """Setup XRT runtime for AIE execution using shared device manager"""

        for op in cls.registered_operators:
            op.set_up_runtime()

        # Pools of preallocated buffer objects; each buffer object is allocated
        # once at program start and then reused across operators where possible.
        bo_pools = {}  # size (multiple of page_sz) -> list of XRT buffer objects
        page_sz = 4096
        get_pool_sz = lambda x: (x + page_sz - 1) // page_sz * page_sz

        # Allocate static buffers first
        for buffer_data in cls.static_data_pool:
            logging.debug(
                f"Allocating static buffer with size {len(buffer_data)} bytes."
            )
            bo = pyxrt.bo(
                cls.device_manager.device,
                len(buffer_data),
                pyxrt.bo.host_only,
                0x10000,
            )
            bo.write(np.frombuffer(buffer_data, dtype=np.uint8), 0)
            cls.static_data_pool[buffer_data] = bo

        for op in cls.registered_operators:
            if len(op.kernels) == 0:
                # Operator likely is used as a sub-operator in another operator and does need any setup.
                continue
            logging.info(f"Preparing runtime for AIE operator: {op.__class__.__name__}")

            # Set up for each kernel
            for kernel_name, (xclbin, xclbin_kernel_name, insts) in op.kernels.items():
                context, xrt_kernel = cls.device_manager.get_context_and_kernel(
                    str(xclbin.path), xclbin_kernel_name
                )
                with open(str(insts.path), "rb") as f:
                    instructions = np.frombuffer(f.read(), dtype=np.uint32)
                logging.debug(
                    f"Allocating instruction buffer for {len(instructions)} instructions."
                )
                insts_bo = pyxrt.bo(
                    cls.device_manager.device,
                    instructions.nbytes,
                    pyxrt.bo.cacheable,
                    xrt_kernel.group_id(1),
                )
                insts_bo.write(instructions.view(np.uint8), 0)
                op.xrt_kernels[kernel_name] = (
                    context,
                    xrt_kernel,
                    insts_bo,
                    len(instructions),
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

            buffer_allocations = {}  # map buffer -> (key into bo_pools, list index)
            for buffer_name, buffer_min_size in op.buffers.items():
                if buffer_name in op.buffer_static_data:
                    # Static buffers are allocated separately
                    static_data = op.buffer_static_data[buffer_name]
                    op.buffer_bos[buffer_name] = cls.static_data_pool[static_data]
                    continue
                alloc_pool = get_pool_sz(buffer_min_size)
                alloc_idx = 0
                for conflict in conflicting_buffers.get(buffer_name, set()):
                    if conflict not in buffer_allocations:
                        # Conflicting buffer does not yet have an allocation
                        continue
                    conflict_pool, conflict_idx = buffer_allocations[conflict]
                    alloc_idx = max(alloc_idx, conflict_idx + 1)
                assert 0 <= alloc_idx < len(bo_pools.get(alloc_pool, [])) + 1
                if alloc_idx == len(bo_pools.get(alloc_pool, [])):
                    # 0x10000 == group_id(3) and above, i.e., for all user buffers
                    bo = pyxrt.bo(
                        cls.device_manager.device,
                        alloc_pool,
                        pyxrt.bo.host_only,
                        0x10000,
                    )
                    bo_pools.setdefault(alloc_pool, []).append(bo)
                buffer_allocations[buffer_name] = (alloc_pool, alloc_idx)
                op.buffer_bos[buffer_name] = bo_pools[alloc_pool][alloc_idx]

            # Runlist setup
            _, (first_xclbin, first_xclbin_kernel_name, _) = next(
                iter(op.kernels.items())
            )
            context, _ = cls.device_manager.get_context_and_kernel(
                str(first_xclbin.path), first_xclbin_kernel_name
            )
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
        static_data_footprint = sum(len(data) for data in cls.static_data_pool)
        logging.info(
            f"Allocated {len(cls.static_data_pool)} static buffers with a total memory footprint of "
            + (
                f"{static_data_footprint//1024//1024} MiB."
                if static_data_footprint >= 1024 * 1024
                else f"{static_data_footprint//1024} KiB."
            )
        )

    def __init__(self):
        self.artifacts = (
            []
        )  # CompilationArtifact objects are globally uniqued, so any overlapping elements of this list will be shared with other operators and will be cached.
        self.kernels = {}  # Name -> (xclbin_path, xclbin_kernel_name, insts_path)
        self.buffers = {}  # Name -> required buffer size in bytes
        self.buffer_static_data = {}
        self.runlist = (
            []
        )  # List of (kernel_name, buffers_name, buffer_name...), will be executed in sequence

        # AIE runtime state
        self.buffer_bos = {}  # Buffer name -> buffer object
        self.xrt_kernels = (
            {}
        )  # Kernel name -> (XRT context, XRT kernel object, instruction buffer object, instruction length)
        self.xrt_runlist = None

        self.registered_operators.append(self)

    def __call__(self, *args, **kwargs):
        return self.forward(*args, **kwargs)

    def add_kernel(
        self,
        name: str,
        xclbin_artifact: comp.XclbinArtifact,
        xclbin_kernel_name: str,
        insts_artifact: comp.InstsBinArtifact,
    ):
        assert name not in self.kernels
        self.kernels[name] = (xclbin_artifact, xclbin_kernel_name, insts_artifact)

    def add_buffer(self, name, count, dtype=bfloat16, static_data=None):
        assert name not in self.buffers
        self.buffers[name] = count * np.dtype(dtype).itemsize
        if static_data is not None:
            assert (
                static_data.nbytes <= self.buffers[name]
            ), f"Static data for buffer {name} exceeds allocated size."
            static_data_bytes = static_data.flatten().view(np.uint8).tobytes()
            if static_data_bytes not in self.static_data_pool:
                self.static_data_pool[static_data_bytes] = None
            # The actual key in self.static_data_pool may be a different object than static_data_bytes (even if they compare equal).
            # Since these may be large buffers, we want to reuse a reference to the key rather than recreate the object in self.buffer_static_data.
            self.buffer_static_data[name] = next(
                k for k, v in self.static_data_pool.items() if k == static_data_bytes
            )

    def add_to_runlist(self, kernel_name, *args):
        if kernel_name not in self.kernels:
            raise RuntimeError(f"No such kernel: {kernel_name}")
        for arg in args:
            if arg not in self.buffers:
                raise RuntimeError(f"No such buffer: {arg}")
        self.runlist.append((kernel_name, *args))

    def get_bo(self, buffer_name):
        return self.buffer_bos[buffer_name]

    def read_buffer(self, buffer_name, shape, copy=False, dtype=bfloat16):
        """Read buffer and return values as a numpy array"""
        # Create a byte accessible memory view of the buffer object
        mv = self.get_bo(buffer_name).map()

        # Interpret the buffer as a 1-dimensional array then change its view to the expected shape
        arr = np.frombuffer(mv, dtype=dtype, count=np.prod(shape)).reshape(shape)

        # Return an independent copy of the array if needed
        return arr.copy() if copy else arr

    def read_buffer_as_torch(self, buffer_name, shape, dtype=bfloat16):
        return numpy_to_torch(self.read_buffer(buffer_name, shape, dtype))

    def write_buffer(self, buffer_name, array):
        """Write buffer from a numpy array into a XRT buffer object"""
        if buffer_name in self.buffer_static_data:
            raise RuntimeError(f"Cannot write to static buffer: {buffer_name}")

        # Normalize the source
        if isinstance(array, torch.Tensor):
            src = torch_to_numpy(array)
        else:
            src = np.asarray(array)

        # Create a flattened 1D byte view of the source
        src_bytes = src.ravel().view(np.uint8)

        bo = self.get_bo(buffer_name)
        mv = bo.map()  # byte accessible memory view
        # Interpret the buffer as a 1-dimensional array
        dst_bytes = np.frombuffer(mv, dtype=np.uint8, count=bo.size())

        # The BO is an existing array, so copyto() can be called, which doesn't create a new array
        np.copyto(dst_bytes[: src_bytes.size], src_bytes, casting="no")

    @abstractmethod
    def set_up_artifacts(self):
        """
        Subclasses should overwrite this method to set up their required dependenices and runtime runlist, kernels and buffers with calls to add_artifacts(), add_kernel(), add_buffer(), and add_to_runlist().
        Note: This method should only *describe* the required artifacts and runtime buffers, and not yet do any computation or compilation.
        Compilation will be handled automatically based on the provided description.
        """
        pass

    @abstractmethod
    def set_up_runtime(self):
        pass

    def compile(self, dry_run=None):
        """
        Set up the operator and compile any necessary artifacts.
        Subclasses are expected to overwrite set_up(); they may register any artifacts that they need to be compiled there.
        """
        self.set_up_artifacts()
        self._move_artifact_paths()
        work_list = comp.get_work_list(self.artifacts)
        compilation_rules = [
            comp.GenerateMLIRFromPythonCompilationRule(dry_run=dry_run),
            comp.PeanoCompilationRule(
                self.peano_dir, self.mlir_aie_dir, dry_run=dry_run
            ),
            comp.ArchiveCompilationRule(self.peano_dir, dry_run=dry_run),
            comp.AieccCompilationRule(
                self.build_dir, self.peano_dir, self.mlir_aie_dir, dry_run=dry_run
            ),
        ]
        if work_list:
            logging.info(
                f"Compiling {len(work_list)} new artifacts for AIE operator {self.__class__.__name__}: {', '.join(str(artifact.path.name) for artifact in work_list)}"
            )
        comp.compile(compilation_rules, work_list)

    def add_artifacts(self, artifacts):
        self.artifacts.extend(artifacts)

    def _move_artifact_paths(self):
        """Make all artifacts paths point into the build directory (source artifacts into the ironclad source directory). This doesn't phyisically move files; this function is called before artifact generation."""
        todo = self.artifacts.copy()
        while todo:
            artifact = todo[0]
            todo.pop(0)
            if isinstance(artifact, comp.SourceArtifact):
                artifact.set_path(self.base_dir / artifact.path)
            else:
                artifact.set_path(self.build_dir / artifact.path)
            todo.extend(artifact.depends)

    def run_runlist(self):
        bos = set(
            self.buffer_bos[buffer_arg]
            for _, *buffer_args in self.runlist
            for buffer_arg in buffer_args
        )
        insts_bos = set(
            self.xrt_kernels[kernel_name][2] for (kernel_name, *_) in self.runlist
        )
        for bo in bos | insts_bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        start = time.perf_counter()
        self.xrt_runlist.execute()
        self.xrt_runlist.wait()
        stop = time.perf_counter()
        for bo in bos:
            bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
        return stop - start


class AIEOperatorConstraintError(RuntimeError):
    pass
