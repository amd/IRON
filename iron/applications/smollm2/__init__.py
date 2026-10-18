# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolLM2 end to end on the NPU; see ``iron/applications/smollm2/README.md``."""

__all__ = ["SmolLM2"]


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.smollm2.model``
    # runs that module once.
    if name in __all__:
        from . import model

        return getattr(model, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
