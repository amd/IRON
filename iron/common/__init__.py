# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Common utilities and base classes for IRON operators.

This module provides conditional imports to support both:
1. Production environments with AMD AIE hardware (real 'aie' package)
2. Testing environments without hardware (mock 'aie' package)

The mock is automatically used when the real 'aie' package is unavailable.
"""

# Conditional import: try real aie, fall back to mock
try:
    # Attempt to import real AIE package (production mode)
    import aie  # noqa: F401

    _AIE_MOCK_ENABLED = False
except ImportError:
    # No hardware available - use mock (testing mode)
    from . import aie_mock

    aie_mock.setup_mock()
    _AIE_MOCK_ENABLED = True

from .aie_base import AIEOperatorBase, AIEOperatorConstraintError
from .aie_context import AIEContext
from .compilation import (
    XclbinArtifact,
    InstsBinArtifact,
    KernelObjectArtifact,
    KernelArchiveArtifact,
    SourceArtifact,
    PythonGeneratedMLIRArtifact,
)
from .aie_device_manager import AIEDeviceManager


def is_mock_mode() -> bool:
    """Check if running in mock mode (no AIE hardware).

    Returns:
        True if using mock AIE package, False if real hardware available.

    Example:
        >>> from iron.common import is_mock_mode
        >>> if is_mock_mode():
        ...     print("Running tests without hardware")
    """
    return _AIE_MOCK_ENABLED
