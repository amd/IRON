# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2, its text encoder and its audio and vision towers, on the
NPU; see ``iron/applications/embedding_gemma2/README.md``.
"""

__all__ = ["EmbeddingGemma", "Multimodal"]


def __getattr__(name):
    # Imported on first use, so ``python -m iron.applications.embedding_gemma2.model``
    # runs that module once.
    if name in __all__:
        from . import model

        return getattr(model, name)
    raise AttributeError(f"module {__name__!r} has no attribute {name!r}")
