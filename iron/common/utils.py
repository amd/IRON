# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import numpy as np
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor, xrt as _pyxrt


def get_shim_dma_limit(dev) -> int:
    """Return the total number of ShimDMA output channels available on the device.

    Each shim tile exposes a fixed number of DMA source connections; summing
    across all shim tiles gives the device-wide ShimDMA budget.
    """
    return sum(dev.get_num_connections(t, output=True) for t in dev.get_shim_tiles())


def float_to_name(v: float) -> str:
    """Convert a float to a filesystem-safe string for use in operator names.

    Uses repr() for the shortest exact round-trip representation, then sanitizes
    characters that are problematic in filenames or shell scripts:
      '.' -> 'p'  (decimal point)
      '-' -> 'n'  (negative sign / negative exponent)
      '+' -> ''   (positive exponent, redundant)

    Examples:
      3.0   -> '3p0'
      0.01  -> '0p01'
      -0.5  -> 'n0p5'
      1e-10 -> '1en10'
    """
    return repr(v).replace(".", "p").replace("-", "n").replace("+", "")


class XRTSubBuffer(XRTTensor):
    """
    A view into a sub-region of an XRTTensor's underlying pyxrt.bo buffer.

    Inherits from XRTTensor so that isinstance checks in the runtime pass.
    Bypasses XRTTensor.__init__ to avoid allocating a new buffer object.

    The parent XRTTensor must remain alive as long as this sub-buffer is in use.
    """

    def __init__(self, parent_bo, offset_bytes, size_bytes, shape, dtype):
        """
        Args:
            parent_bo: The parent pyxrt.bo object.
            offset_bytes: Byte offset into the parent buffer.
            size_bytes: Size of this sub-region in bytes.
            shape: Tuple giving the logical shape of this sub-buffer.
            dtype: numpy dtype for interpreting the buffer contents.
        """
        # Skip XRTTensor.__init__ (which would allocate a new bo); set base attrs directly.
        self.device = "npu"
        self.dtype = np.dtype(dtype)
        # TODO: replace with XRTTensor.__getitem__ slice support when available upstream
        self._bo = _pyxrt.bo(parent_bo, size_bytes, offset_bytes)
        self._shape = tuple(shape)
        ptr = self._bo.map()
        self._data = np.frombuffer(ptr, dtype=self.dtype).reshape(self._shape)

    @property
    def shape(self) -> tuple[int, ...]:
        return self._shape

    @property
    def data(self) -> np.ndarray:
        return self._data

    def buffer_object(self):
        """Return the underlying pyxrt.bo (required by NPUKernel)."""
        return self._bo

    @classmethod
    def from_parent(cls, parent, shape, offset_elements, length_elements, dtype):
        """Create an XRTSubBuffer into a sub-region of a parent XRTTensor.

        Accepts element-count offsets/lengths and converts to bytes internally.
        XRTTensor has no built-in slice API; use this until mlir-aie gains
        XRTTensor.__getitem__ slice support.
        """
        itemsize = np.dtype(dtype).itemsize
        return cls(
            parent_bo=parent.buffer_object(),
            offset_bytes=offset_elements * itemsize,
            size_bytes=length_elements * itemsize,
            shape=shape,
            dtype=dtype,
        )
