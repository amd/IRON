# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Whole models built on IRON's operators, one package each.

An application owns everything about the model it runs: its parameter tree,
its graph functions, and the host loop that feeds them. Nothing in the
library imports an application, so one can be replaced or deleted on its
own. A second Llama size would share code by growing a package between
these two levels; with one there is nothing to share.
"""
