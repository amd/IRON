#!/bin/bash

# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

# Ensure /opt/xilinx/xrt is mounted.
if [ ! -f /opt/xilinx/xrt/setup.sh ]; then
    echo "Error: /opt/xilinx/xrt is not mounted. Please mount XRT to /opt/xilinx/xrt."
    exit 1
fi

source /opt/xilinx/xrt/setup.sh

# Treat any commands to the container as a command line and execute it within this environment
if [ $# -eq 0 ]; then
    exec bash
else
    exec "$@"
fi
