# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Llama 3 end to end on the NPU; see ``iron/applications/llama/README.md``."""


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.llama.model``
    # runs that module once.
    if name == "Llama":
        from .model import Llama

        return Llama
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
