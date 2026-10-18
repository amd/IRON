# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""LFM2-1.2B end to end on the NPU; see ``iron/applications/lfm2/README.md``."""

__all__ = ["Lfm2"]


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.lfm2.model``
    # runs that module once.
    if name in __all__:
        from . import model

        return getattr(model, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
