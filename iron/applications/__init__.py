# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Applications built on IRON: the models over ``iron.lm`` and their device tests."""

import importlib

MODELS = {
    "embedding_gemma2": (
        "iron.applications.embedding_gemma2",
        "EmbeddingGemma",
    ),
    "embedding_gemma2_multimodal": (
        "iron.applications.embedding_gemma2",
        "Multimodal",
    ),
    "gemma4": ("iron.applications.gemma4", "Gemma4"),
    "gemma4_multimodal": ("iron.applications.gemma4", "Gemma4Multimodal"),
    "llama": ("iron.applications.llama", "Llama"),
}


def model_class(name):
    module_name, export = MODELS[name]
    return getattr(importlib.import_module(module_name), export)
