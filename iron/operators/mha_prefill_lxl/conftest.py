# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0


def pytest_configure(config):
    config.addinivalue_line(
        "markers",
        "benchmark: benchmark-only tests (select with '-m benchmark')",
    )
