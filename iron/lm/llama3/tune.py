# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Measure Llama 3's decode cost table on this NPU (:mod:`iron.lm.tune`).

``decode_costs_npu2.json`` beside this file is such a table, measured on a
Strix Halo NPU (8 columns)::

    python -m iron.lm.llama3.tune model.safetensors tokenizer.model
"""

from pathlib import Path

from iron.lm import tune

from .model import Runner

if __name__ == "__main__":
    tune.main(
        Runner,
        "Measure Llama 3.2 1B's decode cost table",
        Path(__file__).with_name("decode_costs_npu2.json"),
    )
