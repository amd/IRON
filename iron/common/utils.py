# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import torch
import numpy as np
from ml_dtypes import bfloat16
import pyxrt
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor


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


torch_dtype_map = {
    "bf16": torch.bfloat16,
    "f32": torch.float32,
    "i8": torch.int8,
    "ui8": torch.uint8,
    "i16": torch.int16,
    "i32": torch.int32,
}

# Maps XRTTensor dtype objects/types to their torch equivalents.
# Both np.dtype(...) objects and bare ml_dtypes types are included because
# xrttensor.dtype may return either form depending on how the tensor was created.
_XRT_TO_TORCH_DTYPE: dict = {
    np.dtype("float32"): torch.float32,
    np.dtype("int32"): torch.int32,
    np.dtype("int16"): torch.int16,
    np.dtype("int8"): torch.int8,
    np.dtype("uint8"): torch.uint8,
    np.dtype("float16"): torch.float16,
    np.dtype(bfloat16): torch.bfloat16,
    bfloat16: torch.bfloat16,
}


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
        self._bo = pyxrt.bo(parent_bo, size_bytes, offset_bytes)
        self._shape = tuple(shape)
        ptr = self._bo.map()
        self._data = np.frombuffer(ptr, dtype=self.dtype).reshape(self._shape)

    @property
    def shape(self):
        return self._shape

    @property
    def data(self) -> np.ndarray:
        return self._data

    def buffer_object(self):
        """Return the underlying pyxrt.bo (required by NPUKernel)."""
        return self._bo

    def to(self, target_device: str) -> "XRTSubBuffer":
        """Sync buffer to/from the NPU."""
        if target_device == "npu":
            self._bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_TO_DEVICE)
        elif target_device == "cpu":
            self._bo.sync(pyxrt.xclBOSyncDirection.XCL_BO_SYNC_BO_FROM_DEVICE)
        else:
            raise ValueError(f"Unknown device '{target_device}'")
        return self

    def to_torch(self) -> torch.Tensor:
        """Return a torch tensor view of this sub-buffer's data (syncs from device first)."""
        self.to("cpu")
        torch_dtype = _XRT_TO_TORCH_DTYPE.get(self.dtype)
        if torch_dtype is None:
            raise ValueError(f"Unsupported dtype: {self.dtype}")
        return torch.frombuffer(self._bo.map(), dtype=torch_dtype).reshape(self._shape)

    def torch_view(self) -> torch.Tensor:
        """Return a torch tensor view of this sub-buffer's host memory without syncing from device.

        Marks the buffer as CPU-resident so that a subsequent .to("npu") call (or the
        NPU operator's implicit sync) will push the written data to device.
        """
        self.device = "cpu"  # mark dirty so next to("npu") will actually sync
        torch_dtype = _XRT_TO_TORCH_DTYPE.get(self.dtype)
        if torch_dtype is None:
            raise ValueError(f"Unsupported dtype: {self.dtype}")
        return torch.frombuffer(self._bo.map(), dtype=torch_dtype).reshape(self._shape)

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
