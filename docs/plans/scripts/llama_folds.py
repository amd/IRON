# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

import argparse
from collections import Counter

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.common.graph.fold import folded
from iron.tests.common.llama_model import llama_1b

parser = argparse.ArgumentParser()
parser.add_argument("--step", choices=["decode", "prompt"], required=True)
args = parser.parse_args()

aie_utils.set_current_device(from_name("npu2", n_cols=8))
dev = aie_utils.ensure_current_device()
g = llama_1b(n_layers=1)
rows = 1 if args.step == "decode" else g.config.prefill_chunk
t = g.trace(**g.shapes(rows))
f, count = folded(t, dev)
print(f"steps {len(t.steps)} -> {len(f.steps)}")
for fold, n in sorted((str(k), v) for k, v in count.items()):
    print(f"  fold {n}x {fold}")
print("left:", dict(Counter(type(s.op).__name__ for s in f.steps)))
