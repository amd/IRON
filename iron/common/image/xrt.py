# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""What a full ELF's runs need of XRT beyond mlir-aie's host runtime: a
scratchpad another run can drain into and the host can read back,
whether the image a run was made on is still loaded, and unloading it.
"""

import ctypes
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
import pyxrt
from aie.utils.hostruntime.xrtruntime.hostruntime import (
    CachedXRTKernelHandle,
    CachedXRTRuntime,
    XRTHostRuntime,
    XRTKernelHandle,
)
from aie.utils.hostruntime.xrtruntime.parameter_scratchpad import ParameterScratchpad

# PyCapsule_New(pointer, name, destructor): pyxrt.ext.bo takes a host pointer
# only wrapped in a capsule.
_pointer_capsule = ctypes.PYFUNCTYPE(
    ctypes.py_object, ctypes.c_void_p, ctypes.c_char_p, ctypes.c_void_p
)(("PyCapsule_New", ctypes.pythonapi))


class Scratchpad(ParameterScratchpad):
    """A run's parameter scratchpad, which a device transfer can also write."""

    def __init__(self, run: pyxrt.run, params_path: str | Path):
        super().__init__(run, params_path)
        self._alias: pyxrt.bo | None = None

    def sync_from_device(self) -> None:
        """Sync from the device, so ``read`` sees what a transfer into
        ``alias`` wrote.
        """
        self._bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)

    def alias(self) -> pyxrt.bo:
        """A buffer object over this scratchpad's host mapping, which a
        kernel argument can be bound to.

        The scratchpad's own buffer object is on the device heap, at an
        address the shim DMA does not reach: a transfer into it silently goes
        nowhere. This user-pointer buffer is reached like any host buffer, so
        another run can drain into it and set this run's values with no host
        step between. It points into this scratchpad's mapping, which this
        object keeps alive; keep it for as long as the alias.

        Raises:
            RuntimeError: The shared runtime is not XRT's.
        """
        if self._alias is None:
            runtime = aie_utils.DefaultNPURuntime
            if not isinstance(runtime, XRTHostRuntime):
                raise RuntimeError(
                    f"a scratchpad alias is an XRT buffer; the runtime is {runtime!r}"
                )
            pointer = np.frombuffer(self._mv, dtype=np.uint8).ctypes.data
            self._alias = pyxrt.ext.bo(
                runtime._device, _pointer_capsule(pointer, None, None), self._bo.size()
            )
        return self._alias


def loaded(handle: XRTKernelHandle) -> bool:
    """Whether ``handle``'s image is still loaded: a caching runtime evicts
    one to make room for another, which ends every run made on it.
    """
    return not isinstance(handle, CachedXRTKernelHandle) or handle._is_valid


def unload(image: str | Path) -> None:
    """End the caching runtime's hw_context on ``image``, and every handle on it.

    A context holds some of the driver's device heap, placed after the runs
    made before it: while it lives, freeing those runs leaves holes no larger
    run fits in.
    """
    runtime = aie_utils.DefaultNPURuntime
    if isinstance(runtime, CachedXRTRuntime):
        runtime.evict_context(Path(image))
