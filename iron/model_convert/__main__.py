# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
IRON Model Converter CLI Entry Point

Run as: python -m iron.model_convert <command> [args]
Or: python -m iron.model_convert.cli <command> [args]
"""

from .cli import main

if __name__ == "__main__":
    import sys

    sys.exit(main())
