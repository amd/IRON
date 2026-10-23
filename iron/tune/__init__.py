# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tuning: timing each operator's settings on the NPU (``measure``) and
writing the fastest as a profile (``autotune``), which a graph then
compiles with like any other. Nothing in the graph core imports this
package.
"""
