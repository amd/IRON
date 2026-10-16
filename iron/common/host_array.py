# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Host-array conversion that does not import torch unless a tensor is passed."""

import numpy as np


def as_numpy(values):
    """Return ``values`` as a NumPy array.

    A torch tensor is detached, moved to CPU, and made contiguous. ``bfloat16``
    is bitcast through ``uint16`` so the conversion does not round. Any other
    value goes through ``np.asarray``.
    """
    module = getattr(type(values), "__module__", "") or ""
    if module == "torch" or module.startswith("torch."):
        import torch
        from ml_dtypes import bfloat16

        tensor = values.detach()
        if tensor.device.type != "cpu":
            tensor = tensor.cpu()
        if not tensor.is_contiguous():
            tensor = tensor.contiguous()
        if tensor.dtype == torch.bfloat16:
            return tensor.view(torch.uint16).numpy().view(bfloat16)
        return tensor.numpy()
    return np.asarray(values)
