# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Scratch harness (not shipped): capture npu1's own ``resolve(dev)`` choices
for every operator each Whisper version records, at both checkpoints, as a
``Profile`` -- not a timed tune (no npu1 device is reachable here), but a
compile-validated starting point for ``profiles/npu1.json``, to tune for
real on Phoenix. Reuses ``iron.tune.autotune.Shape`` for the same dims a
real tune keeps (off each field's default), so entries read as a tuned
profile's do.
"""
import argparse
import json

import aie.utils as aie_utils
from aie.iron.device import from_name

from iron.applications.whisper.model import Whisper
from iron.common.declare import Profile
from iron.lm.testing import weights_dir
from iron.tune.autotune import Shape

VERSIONS = ["decode", "prompt", "encode"]
CHECKPOINTS = ["whisper-large-v3-turbo", "whisper-small"]

parser = argparse.ArgumentParser()
parser.add_argument("out", help="profiles/npu1.json path to write")
parser.add_argument("--seed", type=int, default=0)
args = parser.parse_args()

device = from_name("npu1", n_cols=4)
profile = Profile()
seen = set()
with aie_utils.set_current_device(device):
    for checkpoint in CHECKPOINTS:
        model = Whisper.from_checkpoint(weights_dir(checkpoint), random_weights=args.seed)
        for name, shapes in zip(VERSIONS, model.shapes()):
            recording = model.record(**shapes)
            for unresolved in recording.operators:
                op = unresolved.resolved(device)
                if not op._domains(device):
                    continue
                shape = Shape(op)
                values = vars(op)
                tunables = {
                    n: values[n] for n in op.declaration.tunables if n not in op.pinned
                }
                dims = shape.named(())
                key = (
                    shape.cls,
                    tuple(sorted(dims.items())),
                    tuple(sorted(tunables.items())),
                )
                if key in seen or not tunables:
                    continue
                seen.add(key)
                try:
                    json.dumps({**dims, **tunables})
                except TypeError as e:
                    # A dim that is a per-call object (Copy's access patterns), not
                    # a shape a profile can key on: no production profile names one.
                    print(f"skip {shape.cls.__name__} {dims}: {e}")
                    continue
                profile.add(shape.cls, **dims, **tunables)
            print(
                f"{checkpoint} {name}: {len(recording.operators)} operators, "
                f"{len(seen)} entries so far"
            )

profile.save(args.out)
print(f"wrote {args.out} ({len(profile)} entries)")
