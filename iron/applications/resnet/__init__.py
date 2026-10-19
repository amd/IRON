# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""ResNet-50; see ``iron/applications/resnet/README.md``."""

from iron.lm.cli import exports

__all__ = ["ResNet"]
__getattr__ = exports(__name__, __all__)
