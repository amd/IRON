# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device's DDR ceiling, measured: the bytes a host stream moves a core cycle, against how many run at once and how large an object.

Each figure is the slope of a call's latency over the bytes each stream
moves, fitted across four sizes of one design, so a call's fixed cost
drops out; every timed run is first checked against its operator's
reference. Read and write together are ``Copy``'s memtile pass-throughs,
each channel a stream in and a stream out; read alone is a weight-bound
``GEMV``'s ``A``, a lane a stream, at the widths the bandwidth tests
request.

``python -m iron.tune.ddr`` measures the attached NPU and writes its curves,
under its power mode, to the cost store (``CostModel.ddr``).
"""

from __future__ import annotations

import argparse
import dataclasses
from collections.abc import Callable, Mapping, Sequence

import aie.utils as aie_utils
import numpy as np
from ml_dtypes import bfloat16

from iron.common.declare import Operator, Unresolvable
from iron.common.image.packaging import require_device
from iron.common.testing import run_test, vectors
from iron.operators.copy import Copy
from iron.operators.gemv import GEMV

from .costmodel import CostModel
from .measure import pmode

# bf16 elements a stream moves, the sizes its slope is fitted across.
PER_STREAM = (1 << 17, 1 << 18, 1 << 19, 1 << 20)
# Copy's pass-throughs, each a stream in and a stream out.
CHANNELS = (1, 2, 3, 4, 6, 8)
# Elements an object, at OBJECT_CHANNELS pass-throughs.
OBJECTS = (256, 1024, 4096, 16384)
OBJECT_CHANNELS = 3
# A weight-bound GEMV's (columns, channels), as the bandwidth tests request.
READ_WIDTHS = ((1, 1), (2, 1), (4, 1), (8, 1), (8, 2))
# GEMV's K, and the rows of A a lane reads, the sizes its slope is fitted across.
READ_K, READ_ROWS = 2048, (64, 128, 256, 512)
FIELDS = ("mixed", "objects", "read")
TIMED_ITERS = 50


def _per_stream(
    ops: Sequence[Operator], moved: Sequence[int], hz: float, log: Callable
) -> float:
    """Return the bytes a stream moves a cycle: the inverse slope of ``ops``' latencies over the bytes ``moved`` a stream, each.

    Raises:
        RuntimeError: An output differs from its operator's reference.
    """
    latencies = []
    for op in ops:
        timed: dict[str, float] = {}
        errors = run_test(
            op,
            vectors(op),
            tolerance=op.tolerance(),
            timed_iters=TIMED_ITERS,
            record=timed.__setitem__,
        )
        if errors:
            raise RuntimeError(
                f"{op!r}: {', '.join(f'{n}: {v.detail}' for n, v in errors.items())}"
            )
        latencies.append(timed["Latency"] * 1e-6)
    slope, _ = np.polyfit(moved, latencies, 1)
    log(f"  latencies (us) {[round(t * 1e6, 1) for t in latencies]} at {list(moved)} B")
    return 1 / slope / hz


def read_gemv(rows: int, columns: int, channels: int, device) -> GEMV:
    """Return a weight-bound GEMV, resolved, reading ``rows`` of ``A`` a lane at the widest width up to ``columns`` the shim's DMAs admit.

    Args:
        rows: A's rows each lane reads, ``READ_K`` long.
        columns: The columns asked for.
        channels: The lanes a column.
        device: The device it resolves for.
    """
    while True:
        try:
            return GEMV(
                M=rows * columns * channels,
                K=READ_K,
                feed_b=True,
                num_aie_columns=columns,
                num_channels=channels,
            ).resolved(device)
        except Unresolvable:
            columns -= 1


@dataclasses.dataclass
class Ceiling:
    """A device's measured DDR rates, each the bytes a stream moves a core cycle.

    Attributes:
        core_mhz: The clock the cycles count (the runtime's ``core_mhz``).
        mixed: Against the streams running at once, half reading and half
            writing.
        objects: Against an object's elements, at ``OBJECT_CHANNELS``
            pass-throughs.
        read: Against the streams running at once, all reading (a GEMV lane
            each).
    """

    core_mhz: float
    mixed: dict[int, float]
    objects: dict[int, float]
    read: dict[int, float]

    @classmethod
    def measure(cls, device, log: Callable[[str], object] = print) -> Ceiling:
        """Return ``device``'s ceiling, measured on it (the attached NPU, bound as current).

        Args:
            device: The device.
            log: Called with each figure as it is measured.
        """
        core_mhz = float(aie_utils.DefaultNPURuntime.core_mhz)
        hz = core_mhz * 1e6
        item = np.dtype(bfloat16).itemsize
        mixed, objects, read = {}, {}, {}
        for channels, tile in dict.fromkeys(
            [(c, 4096) for c in CHANNELS] + [(OBJECT_CHANNELS, t) for t in OBJECTS]
        ):
            ops = [
                Copy(
                    input_buffer_size=channels * n,
                    num_channels=channels,
                    tile_size=tile,
                ).resolved(device)
                for n in PER_STREAM
            ]
            rate = _per_stream(ops, [n * item for n in PER_STREAM], hz, log)
            log(f"Copy, {channels} channels, objects of {tile}: {rate:.3f}")
            if tile == 4096:
                mixed[2 * channels] = rate
            if channels == OBJECT_CHANNELS:
                objects[tile] = rate
        for columns, channels in READ_WIDTHS:
            ops = [read_gemv(r, columns, channels, device) for r in READ_ROWS]
            streams = ops[0].num_aie_columns * ops[0].num_channels
            read[streams] = _per_stream(
                ops, [r * READ_K * item for r in READ_ROWS], hz, log
            )
            log(f"GEMV, {streams} streams reading: {read[streams]:.3f}")
        return cls(core_mhz, mixed, objects, read)

    @classmethod
    def stored(cls, device: str) -> Ceiling | None:
        """Return ``device``'s ceiling in the NPU's present power mode, as the cost store keeps it; None where it is not measured."""
        model = CostModel.load(device)
        if model is None or not model.ddr:
            return None
        kept = model.ddr.get(pmode())
        return None if kept is None else cls.from_json(kept)

    @classmethod
    def from_json(cls, data: Mapping) -> Ceiling:
        """Return the ceiling ``as_json`` wrote."""
        return cls(
            float(data["core_mhz"]),
            *({int(k): float(v) for k, v in data[f].items()} for f in FIELDS),
        )

    def as_json(self) -> dict:
        """Return this ceiling as the cost store keeps it."""
        return {
            "core_mhz": self.core_mhz,
            **{f: {str(k): v for k, v in vars(self)[f].items()} for f in FIELDS},
        }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    device = require_device()
    name = device.name
    ceiling = Ceiling.measure(device)
    mode = pmode()
    for field in FIELDS:
        curve = ", ".join(f"{k}: {v:.2f}" for k, v in vars(ceiling)[field].items())
        print(
            f"{name} ({mode}) {field}, bytes a stream a cycle at {ceiling.core_mhz:.0f} MHz: {curve}"
        )
    model = CostModel.load(name) or CostModel()
    model.ddr[mode] = ceiling.as_json()
    print(f"wrote {model.save(name)}")


if __name__ == "__main__":
    main()
