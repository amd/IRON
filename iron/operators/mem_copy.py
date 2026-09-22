# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Memory copy, in the declared form.

Memcpy is designed to use every column's shimDMA in-out pairs to fully
saturate DDR bandwidth. It is a superset of passthrough_kernel and
passthrough_dmas, so it serves as a microbenchmark and as a template for
multi-core unary operations.

:class:`MemCopyOverlay` is ``num_cores`` cores (or, with ``bypass``, memtile
forwards) each streaming ``line_size``-element lines; the cores loop
forever, so no trip count reaches the array. :class:`MemCopy` copies a flat
``size`` buffer through it: whole partitions split evenly across the cores,
and a remainder handled by re-reading already-copied data to pad a full
line, which is the hand-written sequence kept as an override.
"""

import dataclasses
import math
from dataclasses import dataclass
from typing import List

import numpy as np

from iron.common.declare import (
    In,
    Operator,
    Out,
    Overlay,
    StreamIn,
    StreamOut,
    Untunable,
    dim,
    operator,
    tunable,
)
from iron.common.testing import Case, Testing, device_columns
from iron.common.tiling import bank_elements
from iron.common.tiling import Access

# The maximum value the 4th dimension of DMA BD can be set
TAP_REPEAT_MAX = 64
# The maximum fill/drain tasks to put in a group for 1 objectfifo
TASK_GROUP_SIZE = 4


# --------------------------------------------------------------------------
# The overlay: cores (or forwards) over fixed lines.
# --------------------------------------------------------------------------


@operator
class MemCopyOverlay(Overlay):
    """``num_cores`` copy paths, at most ``num_channels`` per column."""

    # None: one core per column, one channel, 1024-element tiles.
    num_cores: int | None = tunable(None)
    num_channels: int = tunable(1)
    tile_size: int | None = tunable(None)
    bypass: bool = False
    # min(tile_size, 8192): one 16 KB line at most; filled by tuning.
    line_size: int | None = tunable(None, repr=False)

    s = StreamIn(line_size, per=num_cores)
    d = StreamOut(line_size, per=num_cores)

    def tuning(self, dev) -> "MemCopyOverlay":

        cores = self.num_cores
        if cores is None:
            if dev is None:
                raise Untunable("num_cores defaults from the device; none given")
            cores = self.shim_columns(dev, self.num_channels) * self.num_channels
        tile_size = 1024 if self.tile_size is None else self.tile_size
        return dataclasses.replace(
            self, num_cores=cores, tile_size=tile_size, line_size=min(tile_size, 8192)
        )

    def design(self, target) -> list:
        from aie.iron import ObjectFifo, Worker
        from aie.iron.controlflow import range_

        line_type = self.s.tile
        line_size, num_cores = self.line_size, self.num_cores
        # A line spanning more than one bank cannot be double-buffered in
        # what is left of local memory.
        fifodepth = 1 if line_size > bank_elements(self.s.dtype) else 2

        of_ins = [
            ObjectFifo(line_type, name=f"in{i}", depth=fifodepth)
            for i in range(num_cores)
        ]
        # Bypass path is a special case where we don't need to create a
        # Worker: the ObjectFifo is forwarded through a MemTile.
        if self.bypass:
            of_outs = [of_ins[i].cons().forward() for i in range(num_cores)]
            workers = []
        else:
            of_outs = [
                ObjectFifo(line_type, name=f"out{i}", depth=fifodepth)
                for i in range(num_cores)
            ]
            mem_copy_fcn = target.kernel(
                "passThroughLine",
                [line_type, line_type, np.int32],
                source=target.kernels_dir / "generic" / "passThrough.cc",
                compile_flags=["-DBIT_WIDTH=16"],
            )
            num_lines = self.tile_size // line_size

            def core_fn(of_in, of_out, mem_copy_line):
                for _ in range_(num_lines):
                    elem_in = of_in.acquire(1)
                    elem_out = of_out.acquire(1)
                    mem_copy_line(elem_in, elem_out, line_size)
                    of_in.release(1)
                    of_out.release(1)

            workers = [
                Worker(core_fn, [of_ins[i].cons(), of_outs[i].prod(), mem_copy_fcn])
                for i in range(num_cores)
            ]
        for i in range(num_cores):
            self.s[i].bind(of_ins[i].prod())
            self.d[i].bind(of_outs[i].cons())
        return workers


# --------------------------------------------------------------------------
# The operator: a flat buffer through it.
# --------------------------------------------------------------------------


@dataclass
class PartialWorkloadConfig:
    """Configuration for partial workload processing."""

    full_taps: List[Access]
    num_cores_with_no_tiles: int
    num_cores_with_full_tiles: int
    padding_tap_repeats: List[int] | None = None
    padding_taps: List[Access] | None = None
    partial_tap: Access | None = None


def _linear(size, offset, run, repeat=1) -> Access:
    return Access(size, offset, (repeat, 1, 1, run), (0, 0, 0, 1))


def create_whole_workload_taps(
    size: int, num_cores: int, line_size: int, whole_partition_size: int
) -> List[Access]:
    """One contiguous chunk of the evenly divisible partition per core."""
    chunk_size = whole_partition_size // num_cores
    return [_linear(size, chunk_size * i, chunk_size) for i in range(num_cores)]


def create_partial_workload_config(
    size: int,
    num_cores: int,
    line_size: int,
    minimum_work_size: int,
    whole_partition_size: int,
    partial_work_size: int,
) -> PartialWorkloadConfig:
    """How the remainder after the whole partitions is spread over the cores.

    ``minimum_work_size`` is what the array is configured to process at once
    (one line per core). A remainder is padded to that by re-reading data
    already copied, so the fill/drain calls are not repeated per line.
    """
    if size > minimum_work_size:
        partial_work_size = minimum_work_size
        start_offset = size - minimum_work_size
    else:
        start_offset = whole_partition_size

    num_cores_with_full_tiles = partial_work_size // line_size
    partial_tile_size = partial_work_size % line_size
    num_cores_with_no_tiles = (
        num_cores - num_cores_with_full_tiles - (1 if partial_tile_size > 0 else 0)
    )
    full_taps = [
        _linear(size, line_size * i + start_offset, line_size)
        for i in range(num_cores_with_full_tiles)
    ]
    config = PartialWorkloadConfig(
        full_taps=full_taps,
        num_cores_with_no_tiles=num_cores_with_no_tiles,
        num_cores_with_full_tiles=num_cores_with_full_tiles,
    )
    if partial_tile_size > 0:
        config.padding_tap_repeats = []
        config.padding_taps = []
        # The partial tile is padded to a full line with repeats of a common
        # factor of the two sizes, largest repeat count first.
        partial_tile_offset = line_size * num_cores_with_full_tiles + start_offset
        padding_needed = line_size - partial_tile_size
        highest_common_factor_pad = math.gcd(partial_tile_size, padding_needed)
        for tap_repeat_exp in reversed(
            range(0, math.ceil(math.log2(TAP_REPEAT_MAX)) + 1)
        ):
            padding_size = highest_common_factor_pad * 2**tap_repeat_exp
            padding_tap_repeat = math.floor(padding_needed / padding_size)
            config.padding_tap_repeats.append(padding_tap_repeat)
            config.padding_taps.append(
                _linear(
                    size,
                    partial_tile_offset,
                    highest_common_factor_pad,
                    repeat=2**tap_repeat_exp,
                )
            )
            padding_needed = padding_needed - (padding_size * padding_tap_repeat)
        config.partial_tap = _linear(size, partial_tile_offset, partial_tile_size)
    return config


def _cases():
    """Every core and channel split that divides each size, with and without
    the memtile bypass; the 2048 shape through the memtile is the default."""
    out = []
    columns = device_columns()
    for size in [1024, 2048, 4096, 8192]:
        for num_cores in range(1, columns * 2 + 1):
            for channels in (1, 2):
                # A channel needs at least one core, and a core a shim channel.
                if not channels <= num_cores <= columns * channels:
                    continue
                for bypass in (False, True):
                    tile_size = min(size // num_cores, 8192)
                    if tile_size * num_cores != size:
                        continue
                    out.append(
                        Case(
                            dict(
                                size=size,
                                num_cores=num_cores,
                                num_channels=channels,
                                bypass=bypass,
                                tile_size=tile_size,
                            ),
                            extensive=not (size == 2048 and not bypass),
                        )
                    )
    return out


@operator
class MemCopy(Operator[MemCopyOverlay]):
    """AIE-accelerated memory copy operator."""

    # A copy that alters a value is a broken copy, so gate it exactly.
    test = Testing(_cases, rel_tol=0.0, abs_tol=0.0)

    size: int = dim()

    x = In(size, to=MemCopyOverlay.s)
    y = Out(size, from_=MemCopyOverlay.d)

    def reference(self, x):
        """CPU reference: the copy."""
        return x.copy()

    # -- the runtime sequence --------------------------------------------------

    def design(self, rt):
        ov = self.ov
        size, num_cores, line_size = self.size, ov.num_cores, ov.line_size
        s, d = ov.s, ov.d
        x, y = self.x, self.y

        # How much of the workload partitions evenly, and what remains.
        minimum_work_size = line_size * num_cores  # what the array is configured for
        num_whole_partitions = math.floor(size / minimum_work_size)
        whole_partition_size = minimum_work_size * num_whole_partitions
        partial_work_size = size - whole_partition_size

        if num_whole_partitions > 0:
            taps = create_whole_workload_taps(
                size, num_cores, line_size, whole_partition_size
            )
            with rt.group():
                for i in range(num_cores):
                    rt.fill(s[i], (x, taps[i]))
                for i in range(num_cores):
                    rt.drain(d[i], (y, taps[i]), wait=True)

        if partial_work_size == 0:
            return
        partial = create_partial_workload_config(
            size,
            num_cores,
            line_size,
            minimum_work_size,
            whole_partition_size,
            partial_work_size,
        )

        def padded(verb, slot, buf):
            """The padding repeats then the partial tile on one fifo, in
            groups of TASK_GROUP_SIZE transfers, each group awaited."""
            tg = rt.new_group()
            count = 0
            for repeats, tap in zip(partial.padding_tap_repeats, partial.padding_taps):
                for _ in range(repeats):
                    if count % TASK_GROUP_SIZE == 0:
                        verb(slot, (buf, tap), wait=True, group=tg)
                        tg.finish()
                        tg = rt.new_group()
                    else:
                        verb(slot, (buf, tap), wait=False, group=tg)
                    count += 1
            return tg, count

        # A while loop, so the cores with full lines are grouped together.
        idx = 0
        while idx < num_cores:
            if idx < partial.num_cores_with_no_tiles:
                # Cores with no work: their fifos are placed by the build.
                idx += partial.num_cores_with_no_tiles
            elif idx == num_cores - 1 and partial.partial_tap is not None:
                # Fill the last fifo with padding + real data
                tg, count = padded(rt.fill, s[idx], x)
                if count % TASK_GROUP_SIZE == 0:
                    rt.fill(s[idx], (x, partial.partial_tap), wait=True, group=tg)
                    tg.finish()
                    tg = rt.new_group()
                else:
                    rt.fill(s[idx], (x, partial.partial_tap), wait=False, group=tg)
                count += 1
                # Drain it the same way, continuing the same count.
                for repeats, tap in zip(
                    partial.padding_tap_repeats, partial.padding_taps
                ):
                    for _ in range(repeats):
                        if count % TASK_GROUP_SIZE == 0:
                            rt.drain(d[idx], (y, tap), wait=True, group=tg)
                            tg.finish()
                            tg = rt.new_group()
                        else:
                            rt.drain(d[idx], (y, tap), wait=False, group=tg)
                        count += 1
                rt.drain(d[idx], (y, partial.partial_tap), wait=True, group=tg)
                tg.finish()
                idx += 1
            else:
                with rt.group():
                    for j in range(partial.num_cores_with_full_tiles):
                        rt.fill(s[idx + j], (x, partial.full_taps[j]))
                    for j in range(partial.num_cores_with_full_tiles):
                        rt.drain(d[idx + j], (y, partial.full_taps[j]), wait=True)
                idx += partial.num_cores_with_full_tiles
