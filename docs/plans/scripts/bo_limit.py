# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse

import pyxrt as xrt

parser = argparse.ArgumentParser()
parser.add_argument("--nbytes", type=int, default=679477248)
parser.add_argument("--count", type=int, default=24)
args = parser.parse_args()

device = xrt.device(0)
held = []
for i in range(args.count):
    try:
        held.append(xrt.bo(device, args.nbytes, xrt.bo.host_only, 0))
    except RuntimeError as e:
        print(f"bo {i} failed after {i * args.nbytes / 2**30:.2f} GiB: {e}")
        break
else:
    print(f"all {args.count} held, {args.count * args.nbytes / 2**30:.2f} GiB")
