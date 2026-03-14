#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
Setup script for iron-convert CLI

Install with: pip install -e .
Then run: iron-convert --help
"""

from setuptools import setup, find_packages

setup(
    name="iron-model-convert",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "torch",
        "numpy",
        "safetensors",
        "transformers",
        "huggingface_hub",
    ],
    entry_points={
        "console_scripts": [
            "iron-convert=iron.model_convert.cli:main",
        ],
    },
    author="AMD",
    description="IRON Model Converter - Convert HuggingFace models to NPU format",
    license="Apache-2.0",
)
