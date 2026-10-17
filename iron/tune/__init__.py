# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Tuning: measuring designs on the NPU (``probe``, ``costcache``) and
choosing a graph's tunables, folds and packs from what was measured
(``narrowing``). The graph core asks only for ``iron.common.graph.tuner``'s
interfaces; nothing in it imports this package.
"""
