# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct end to end on the NPU; see ``iron/applications/idefics3/README.md``."""

__all__ = ["SmolVLMText", "SmolVLM"]


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.idefics3.model``
    # runs that module once.
    if name in __all__:
        from . import model

        return getattr(model, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
