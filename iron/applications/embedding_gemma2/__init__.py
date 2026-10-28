# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""EmbeddingGemma 2, its text encoder and its audio and vision towers, on the
NPU; see ``iron/applications/embedding_gemma2/README.md``.
"""

from iron.lm.cli import exports

__all__ = ["EmbeddingGemma", "Multimodal"]
__getattr__ = exports(__name__, __all__)
