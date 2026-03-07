# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Fused QKV projection design.

The fused QKV projection is implemented as a standard GEMV with
M = q_dim + k_dim + v_dim and K = embedding_dim. No custom AIE kernel
is needed; the operator reuses the mv.o kernel and my_matvec design
from the GEMV operator.

This module re-exports the GEMV design function for documentation and
to maintain the 4-file operator convention.
"""

from iron.operators.gemv.design import my_matvec as my_fused_qkv_proj
