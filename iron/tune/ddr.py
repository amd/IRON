# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""The device's DDR ceiling, measured: the bytes a host stream moves a core cycle, and what a phase boundary costs beyond its streams.

Each rate is the slope of a call's latency over the bytes each stream
moves, fitted across four sizes of one design, so a call's fixed cost
drops out; every timed run is first checked against its operator's
reference. Read and write together are ``Copy``'s memtile pass-throughs,
each channel a stream in and a stream out; read alone is a weight-bound
``GEMV``'s ``A``, a lane a stream, at the widths the bandwidth tests
request. A phase boundary is the fixed cost those lines leave out, of a
chain whose edges run through host memory (``_boundary``).

``python -m iron.tune.ddr`` measures the attached NPU and writes its ceiling
(``sdf.Ceiling``), under its power mode, to the cost store
(``CostModel.ddr``).
"""

from __future__ import annotations

import argparse
from collections.abc import Callable, Sequence

import aie.utils as aie_utils
import numpy as np
from aie.utils import set_current_device
from ml_dtypes import bfloat16

from iron.common.declare import Operator, Profile, Unresolvable
from iron.common.declare.composition import Entry, Member, Region
from iron.common.graph.record import Recording
from iron.common.graph.sdf import Ceiling
from iron.common.image.packaging import require_device
from iron.common.image.step import BufferRef, Edge, EdgeKind, SequenceStep
from iron.common.testing import run_test, vectors
from iron.operators.copy import Copy
from iron.operators.gemv import GEMV
from iron.operators.relu import ReLU

from .autotune import Timed
from .costmodel import CostModel
from .fusions import Applied, drawn_inputs
from .measure import pmode
from .search import measure

# bf16 elements a stream moves, the sizes its slope is fitted across.
PER_STREAM = (1 << 17, 1 << 18, 1 << 19, 1 << 20)
# Copy's pass-throughs, each a stream in and a stream out.
CHANNELS = (1, 2, 3, 4, 6, 8)
# Elements an object of the mixed curve's pass-throughs.
MIXED_TILE = 4096
# Elements an object, at OBJECT_CHANNELS pass-throughs.
OBJECTS = (256, 1024, 4096, 16384)
OBJECT_CHANNELS = 3
# A weight-bound GEMV's (columns, channels), as the bandwidth tests request.
READ_WIDTHS = ((1, 1), (2, 1), (4, 1), (8, 1), (8, 2))
# GEMV's K, and the rows of A a lane reads, the sizes its slope is fitted across.
READ_K, READ_ROWS = 2048, (64, 128, 256, 512)
TIMED_ITERS = 50
# The phase boundary's probe: elements a lane moves, its lanes and its objects.
BOUNDARY_PER_LANE = (1 << 13, 1 << 14, 1 << 15, 1 << 16)
BOUNDARY_COLUMNS = 2
BOUNDARY_TILE = 128


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


def _checked(call: Timed, profile: Profile, device) -> None:
    """Run ``call`` built under ``profile`` once on drawn inputs.

    Raises:
        RuntimeError: An output differs from its recording's reference.
    """
    recording = call.recording
    inputs = drawn_inputs(recording, 0)
    want, _ = recording.reference(
        {h.name: t for h, t in zip(recording.inputs, inputs, strict=True)}, {}
    )
    with set_current_device(device):
        graph = Applied.of(call, profile, device).built(device)
    try:
        graph(*inputs)
        for h, ref in zip(recording.returned, want, strict=True):
            got = np.array(graph.read(h)[h.valid_index({})], dtype=np.float32)
            if not np.array_equal(got, np.asarray(ref, dtype=np.float32)):
                raise RuntimeError(
                    f"{recording.name}: {h.name} differs from its reference"
                )
    finally:
        graph.release()


def _boundary(device, hz: float, log: Callable) -> float:
    """Return the cycles a phase boundary costs beyond its streams.

    A chain of three ``ReLU``s, ``BOUNDARY_COLUMNS`` lanes each, with one
    and with two of its edges through host memory (a phase boundary each),
    is timed against the chain all on chip at each of ``BOUNDARY_PER_LANE``
    (``search.measure``'s paired delta, each build checked against its
    reference first). Each delta's line over the bytes a lane moves meets
    zero bytes at what its boundaries cost beyond their streams; the figure
    is the least-squares cost a boundary across the two.

    Args:
        device: The device, the attached NPU.
        hz: The core clock the cycles count.
        log: Called with each delta as it is measured.

    Raises:
        RuntimeError: A build differs from its reference.
    """
    item = np.dtype(bfloat16).itemsize
    deltas: dict[int, list[float]] = {1: [], 2: []}
    for per_lane in BOUNDARY_PER_LANE:
        relu = ReLU(
            size=per_lane * BOUNDARY_COLUMNS,
            tile_size=BOUNDARY_TILE,
            num_aie_columns=BOUNDARY_COLUMNS,
            num_channels=1,
        )
        steps = [
            SequenceStep(relu, (BufferRef(a), BufferRef(b)))
            for a, b in (("x", "m1"), ("m1", "m2"), ("m2", "y"))
        ]
        call = Timed(
            Recording.of_steps(f"ddr_boundary_{per_lane}", steps, ["x"], ["y"])
        )
        member = Member(ReLU, Profile.dims(ReLU, vars(relu)))
        profiles = []
        for through_host in range(3):
            profile = Profile()
            profile.add_entry(
                Entry(
                    Region(
                        parts=(member,) * 3,
                        edges=tuple(
                            Edge(
                                i,
                                "y",
                                i + 1,
                                "x",
                                kind=(
                                    EdgeKind.DDR
                                    if i < through_host
                                    else EdgeKind.STREAM
                                ),
                            )
                            for i in range(2)
                        ),
                    )
                )
            )
            _checked(call, profile, device)
            profiles.append(profile)
        for k in deltas:
            m = measure(profiles[k], profiles[0], [call], device)
            deltas[k].append((m.ratio - 1) * m.base_seconds)
        log(
            f"  {per_lane * item} B a lane: "
            + ", ".join(
                f"{k} boundaries {d[-1] * 1e6:.2f} us" for k, d in deltas.items()
            )
        )
    moved = [n * item for n in BOUNDARY_PER_LANE]
    at_zero = {k: float(np.polyfit(moved, d, 1)[1]) for k, d in deltas.items()}
    return sum(k * a for k, a in at_zero.items()) / sum(k * k for k in at_zero) * hz


def measured(device, log: Callable[[str], object] = print) -> Ceiling:
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
        [(c, MIXED_TILE) for c in CHANNELS] + [(OBJECT_CHANNELS, t) for t in OBJECTS]
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
        if tile == MIXED_TILE:
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
    try:
        boundary = _boundary(device, hz, log)
        log(f"a phase boundary: {boundary:.0f} cycles, {boundary / core_mhz:.2f} us")
    except (NotImplementedError, ValueError) as e:
        boundary = None
        log(f"a phase boundary is not measured: its probe is not built here: {e}")
    return Ceiling(
        core_mhz=core_mhz,
        mixed=mixed,
        objects=objects,
        read=read,
        boundary=boundary,
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.parse_args()
    device = require_device()
    name = device.name
    ceiling = measured(device)
    mode = pmode()
    for field in ("mixed", "objects", "read"):
        curve = ", ".join(f"{k}: {v:.2f}" for k, v in vars(ceiling)[field].items())
        print(
            f"{name} ({mode}) {field}, bytes a stream a cycle at {ceiling.core_mhz:.0f} MHz: {curve}"
        )
    print(f"{name} ({mode}) a phase boundary, cycles: {ceiling.boundary}")
    model = CostModel.load(name) or CostModel()
    model.ddr[mode] = ceiling.as_json()
    print(f"wrote {model.save(name)}")


if __name__ == "__main__":
    main()
