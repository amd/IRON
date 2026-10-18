# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Granite 4.2 3B end to end on the NPU; see ``iron/applications/granite/README.md``."""

__all__ = ["Granite"]


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.granite.model``
    # runs that module once.
    if name in __all__:
        from . import model

        return getattr(model, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
