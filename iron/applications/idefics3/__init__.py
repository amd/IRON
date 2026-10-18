# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""SmolVLM-256M-Instruct end to end on the NPU; see ``iron/applications/idefics3/README.md``."""

from iron.lm.cli import exports

__all__ = ["SmolVLMText", "SmolVLM"]
__getattr__ = exports(__name__, __all__)
