# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from ml_dtypes import bfloat16
from pathlib import Path
from dataclasses import dataclass
from typing import Optional, List

import numpy as np
import math
import argparse
import sys

from aie.iron import (
    Kernel,
    ObjectFifo,
    Program,
    Runtime,
    Worker,
)
from aie.iron.placers import SequentialPlacer
from aie.iron.device import Tile, NPU1, NPU2
from aie.helpers.taplib.tap import TensorAccessPattern
from aie.iron.controlflow import range_
from aie.iron.runtime.endpoint import RuntimeEndpoint
from aie.iron.device import AnyShimTile
import aie.dialects.index as index_dialect

# The maximum value the 4th dimension of DMA BD can be set
TAP_REPEAT_MAX = 64
# The maximum fill/drain tasks to put in a group for 1 objectfifo
TASK_GROUP_SIZE = 4


@dataclass
class PartialWorkloadConfig:
    """Configuration for partial workload processing."""

    full_taps: List[TensorAccessPattern]
    num_cores_with_no_tiles: int
    num_cores_with_full_tiles: int
    padding_tap_repeats: List[int] | None = None
    padding_taps: List[TensorAccessPattern] | None = None
    partial_tap: TensorAccessPattern | None = None


def create_whole_workload_taps(
    size: int, num_cores: int, line_size: int, whole_partition_size: int
) -> List[TensorAccessPattern]:
    """
    Create TensorAccessPatterns for whole workload processing.

    Args:
        size: Total size of the workload
        num_cores: Number of cores to distribute work across
        line_size: Size of each line/tile
        whole_partition_size: Size of the evenly divisible partition

    Returns:
        taps: Lists of TensorAccessPatterns
    """
    chunk_size = whole_partition_size // num_cores
    taps = [
        TensorAccessPattern(
            (1, size),
            chunk_size * i,
            [1, 1, 1, chunk_size],
            [0, 0, 0, 1],
        )
        for i in range(num_cores)
    ]
    return taps


def create_partial_workload_config(
    size: int,
    num_cores: int,
    line_size: int,
    minimum_work_size: int,
    whole_partition_size: int,
    partial_work_size: int,
) -> PartialWorkloadConfig:
    """
    Create configuration for partial workload processing.

    Args:
        size: Total size of the workload
        num_cores: Number of cores to distribute work across
        line_size: Size of each line/tile
        minimum_work_size: Size of the minimum workload that the NPU is configured to process
        whole_partition_size: Size of the evenly divisible partition
        partial_work_size: Size of the remaining partial workload

    Returns:
        PartialWorkloadConfig: Configuration object containing all partial workload parameters
    """
    # If the workload is larger than the minimum, use part of the input data that's already been
    # processed for filling the objectfifos to reduce the number of times to repeat fill/drain calls
    if size > minimum_work_size:
        partial_work_size = minimum_work_size
        start_offset = size - minimum_work_size
    else:
        start_offset = whole_partition_size

    # Calculate core distribution
    num_cores_with_full_tiles = partial_work_size // line_size
    partial_tile_size = partial_work_size % line_size
    num_cores_with_no_tiles = (
        num_cores - num_cores_with_full_tiles - (1 if partial_tile_size > 0 else 0)
    )

    # Create TAPs for cores with full tiles
    full_taps = [
        TensorAccessPattern(
            (1, size),
            line_size * i + start_offset,
            [1, 1, 1, line_size],
            [0, 0, 0, 1],
        )
        for i in range(num_cores_with_full_tiles)
    ]

    # Handle partial tile if present
    config = PartialWorkloadConfig(
        full_taps=full_taps,
        num_cores_with_no_tiles=num_cores_with_no_tiles,
        num_cores_with_full_tiles=num_cores_with_full_tiles,
    )

    if partial_tile_size > 0:
        config.padding_tap_repeats = []
        config.padding_taps = []
        # Calculations for padding add processing partial tile
        partial_tile_offset = line_size * num_cores_with_full_tiles + start_offset
        padding_needed = line_size - partial_tile_size
        highest_common_factor_pad = math.gcd(partial_tile_size, padding_needed)
        for tap_repeat_exp in reversed(
            range(0, math.ceil(math.log2(TAP_REPEAT_MAX) + 1))
        ):  # +1 to include the end of range
            padding_size = highest_common_factor_pad * 2**tap_repeat_exp
            padding_tap_repeat = math.floor(padding_needed / padding_size)
            config.padding_tap_repeats.append(padding_tap_repeat)
            config.padding_taps.append(
                TensorAccessPattern(
                    (1, size),
                    partial_tile_offset,
                    [2**tap_repeat_exp, 1, 1, highest_common_factor_pad],
                    [0, 0, 0, 1],
                )
            )
            padding_needed = padding_needed - (padding_size * padding_tap_repeat)
        config.partial_tap = TensorAccessPattern(
            (1, size),
            partial_tile_offset,
            [1, 1, 1, partial_tile_size],
            [0, 0, 0, 1],
        )

    return config


#
# Memcpy is designed to use every column's shimDMA in-out pairs
# to fully saturate DDR bandwidth. It is a superset of passthrough_kernel
# and passthrough_dmas. As such, it can be used as a microbenchmark or as
# a template for multi-core unary operations.
#


def my_mem_copy(dev, size, num_cores, num_channels, bypass, tile_size, trace_size):
    # --------------------------------------------------------------------------
    # Configuration
    # --------------------------------------------------------------------------
    xfr_dtype = bfloat16
    line_size = 8192 if tile_size > 8192 else tile_size
    # P1-5 FIX: Enhanced depth for 8-core 2-channel small-tile triple regression
    # Issue: -17.85% bw, +47.18% lat, +106.34% stddev (mem_copy_8_cores_2_chans_2048_tile_256_False0)
    # Source: memcopy.txt benchmark file (897d04e vs 84d3478)
    # Depth=4 for 8+ cores OR 4+ cores with 2-ch small tile (<512)
    # Depth=3 for 4+ cores OR 2-ch with large tile (>=2048)
    # Depth=2 otherwise
    fifodepth = (
        4
        if (num_cores >= 8 or (num_cores >= 4 and num_channels == 2 and line_size < 512))
        else (3 if (num_cores >= 4 or (num_channels == 2 and line_size >= 2048)) else 2)
    )
    line_type = np.ndarray[(line_size,), np.dtype[xfr_dtype]]
    transfer_type = np.ndarray[(size,), np.dtype[xfr_dtype]]

    # --------------------------------------------------------------------------
    # In-Array Data Movement
    # --------------------------------------------------------------------------

    # Dataflow with ObjectFifos
    of_ins = [
        ObjectFifo(line_type, name=f"in{i}", depth=fifodepth) for i in range(num_cores)
    ]
    # Bypass path is a special case where we don't need to create a Worker
    # and we can use the ObjectFifo directly to read and write the data with
    # a `forward` through a MemTile.
    if bypass:
        of_outs = [of_ins[i].cons().forward() for i in range(num_cores)]
    else:
        of_outs = [
            ObjectFifo(line_type, name=f"out{i}", depth=fifodepth)
            for i in range(num_cores)
        ]

        # --------------------------------------------------------------------------
        # Task core will run
        # --------------------------------------------------------------------------

        # External, binary kernel definition
        mem_copy_fcn = Kernel(
            "passThroughLine",
            "mem_copy.o",
            [line_type, line_type, np.int32],
        )

        # Task for the core to perform
        def core_fn(of_in, of_out, mem_copyLine):
            elemOut = of_out.acquire(1)
            elemIn = of_in.acquire(1)
            mem_copyLine(elemIn, elemOut, line_size)
            of_in.release(1)
            of_out.release(1)

        # Create a worker to perform the task
        my_workers = [
            Worker(
                core_fn,
                [
                    of_ins[i].cons(),
                    of_outs[i].prod(),
                    mem_copy_fcn,
                ],
            )
            for i in range(num_cores)
        ]

    # --------------------------------------------------------------------------
    # DRAM-NPU data movement and work dispatch
    # --------------------------------------------------------------------------

    # Runtime operations to move data to/from the AIE-array
    rt = Runtime()
    with rt.sequence(transfer_type, transfer_type) as (a_in, b_out):
        # Start the workers if not bypass
        if not bypass:
            rt.start(*my_workers)

        # Calculate how much of workload can be partitioned evenly and what's remaining
        minimum_work_size = (
            line_size * num_cores
        )  # Workload size the NPU is configured for
        num_whole_partitions = math.floor(size / minimum_work_size)
        whole_partition_size = minimum_work_size * num_whole_partitions
        partial_work_size = size - whole_partition_size

        # Runtime for the part of the workload partitionable to all cores utilized
        if num_whole_partitions > 0:
            taps = create_whole_workload_taps(
                size, num_cores, line_size, whole_partition_size
            )

            tg_out = rt.task_group()  # Use taskgroup for parallel drain tasks
            # Fill the input objectFIFOs with data
            for i in range(num_cores):
                rt.fill(of_ins[i].prod(), a_in, taps[i], task_group=tg_out)
            # Drain the output objectFIFOs with data
            for i in range(num_cores):
                rt.drain(
                    of_outs[i].cons(),
                    b_out,
                    taps[i],
                    wait=True,  # wait for the transfer to complete and data to be available
                    task_group=tg_out,
                )
            rt.finish_task_group(tg_out)

        # Runtime for the part of the workload partially partitionable to the cores utilized
        if partial_work_size > 0:
            partial_config = create_partial_workload_config(
                size,
                num_cores,
                line_size,
                minimum_work_size,
                whole_partition_size,
                partial_work_size,
            )

            # Use a while loop below so that the tasks for sending full tiles can
            # be grouped together in a for-loop
            objfifo_idx = 0
            while objfifo_idx < num_cores:
                if objfifo_idx < partial_config.num_cores_with_no_tiles:
                    if num_whole_partitions == 0:
                        # Resolving the IRON program requires all objectfifos to have
                        # a defined connection
                        for j in range(partial_config.num_cores_with_no_tiles):
                            ofh = of_ins[objfifo_idx + j].prod()
                            ofh.endpoint = RuntimeEndpoint(AnyShimTile)
                            rt._fifos.add(ofh)
                            ofh = of_outs[objfifo_idx + j].cons()
                            ofh.endpoint = RuntimeEndpoint(AnyShimTile)
                            rt._fifos.add(ofh)
                    objfifo_idx = objfifo_idx + partial_config.num_cores_with_no_tiles
                elif (
                    objfifo_idx == num_cores - 1
                    and partial_config.partial_tap is not None
                ):
                    # Fill the last objfifo with padding+real data
                    tg_out = rt.task_group()
                    tg_count = 1
                    for padding_tap_repeat, padding_tap in zip(
                        partial_config.padding_tap_repeats, partial_config.padding_taps
                    ):
                        for _ in range(padding_tap_repeat):
                            if tg_count % TASK_GROUP_SIZE == 0:
                                rt.fill(
                                    of_ins[objfifo_idx].prod(),
                                    a_in,
                                    padding_tap,
                                    wait=True,
                                    task_group=tg_out,
                                )
                                rt.finish_task_group(tg_out)
                                tg_out = rt.task_group()
                            else:
                                rt.fill(
                                    of_ins[objfifo_idx].prod(),
                                    a_in,
                                    padding_tap,
                                    task_group=tg_out,
                                )
                            tg_count = tg_count + 1
                    if tg_count % TASK_GROUP_SIZE == 0:
                        rt.fill(
                            of_ins[objfifo_idx].prod(),
                            a_in,
                            partial_config.partial_tap,
                            wait=True,
                            task_group=tg_out,
                        )
                        rt.finish_task_group(tg_out)
                        tg_out = rt.task_group()
                    else:
                        rt.fill(
                            of_ins[objfifo_idx].prod(),
                            a_in,
                            partial_config.partial_tap,
                            task_group=tg_out,
                        )
                    tg_count = tg_count + 1
                    # Drain the last objfifo with padding+real data
                    for padding_tap_repeat, padding_tap in zip(
                        partial_config.padding_tap_repeats, partial_config.padding_taps
                    ):
                        for _ in range(padding_tap_repeat):
                            if tg_count % TASK_GROUP_SIZE == 0:
                                rt.drain(
                                    of_outs[objfifo_idx].cons(),
                                    b_out,
                                    padding_tap,
                                    wait=True,
                                    task_group=tg_out,
                                )
                                rt.finish_task_group(tg_out)
                                tg_out = rt.task_group()
                            else:
                                rt.drain(
                                    of_outs[objfifo_idx].cons(),
                                    b_out,
                                    padding_tap,
                                    task_group=tg_out,
                                )
                            tg_count = tg_count + 1
                    rt.drain(
                        of_outs[objfifo_idx].cons(),
                        b_out,
                        partial_config.partial_tap,
                        wait=True,
                        task_group=tg_out,
                    )
                    rt.finish_task_group(tg_out)
                    objfifo_idx = objfifo_idx + 1
                else:
                    tg_out = rt.task_group()  # Use taskgroup for parallel drain tasks
                    for j in range(partial_config.num_cores_with_full_tiles):
                        # Fill the input objectFIFOs with valid data
                        rt.fill(
                            of_ins[objfifo_idx + j].prod(),
                            a_in,
                            partial_config.full_taps[j],
                            task_group=tg_out,
                        )
                    for j in range(partial_config.num_cores_with_full_tiles):
                        # Drain the output objectFIFOs with valid data
                        rt.drain(
                            of_outs[objfifo_idx + j].cons(),
                            b_out,
                            partial_config.full_taps[j],
                            wait=True,
                            task_group=tg_out,
                        )
                    rt.finish_task_group(tg_out)
                    objfifo_idx = objfifo_idx + partial_config.num_cores_with_full_tiles

    # Place components (assign them resources on the device) and generate an MLIR module
    return Program(dev, rt).resolve_program(SequentialPlacer(num_channels))


if __name__ == "__main__":

    def str_to_device(device: str):
        if device == "npu":
            return NPU1()
        elif device == "npu2":
            return NPU2()
        else:
            raise ValueError(f"Device name {device} is unknown.")

    p = argparse.ArgumentParser()
    # Parse command line arguments

    # Device name is required to select the AIE device: npu or npu2
    p.add_argument(
        "-d",
        "--dev",
        required=True,
        dest="device",
        help="AIE Device",
        type=str_to_device,
    )
    # Transfer size is required to define the size of the data to be transferred
    # It must be a multiple of 1024 and divisible by the number of num_cores
    p.add_argument("-l", "--length", required=True, dest="length", help="Transfer size")
    # Number of cores is required to define the number of cores to be used
    # It must be less than or equal to 16 for npu and 32 for npu2
    p.add_argument(
        "-c", "--cores", required=True, dest="num_cores", help="Number of cores"
    )
    # Number of channels is required to define the number of channels to be used
    # It must be 1 or 2
    p.add_argument(
        "-ch", "--channels", required=True, dest="chans", help="Number of channels"
    )
    ## Bypass is required to define if the bypass path should be used
    p.add_argument(
        "-b", "--bypass", required=True, dest="bypass", help="Use DMA-only bypass path"
    )
    # Tile size (elements per tile) - defaults to 1024 for backward compatibility
    p.add_argument(
        "-ts",
        "--tile-size",
        required=False,
        dest="tile_size",
        default="1024",
        help="Tile size (elements per tile)",
    )
    # Trace Size
    p.add_argument(
        "-t", "--trace-size", required=True, dest="trace_size", help="Trace size"
    )
    p.add_argument(
        "--output-file-path",
        "-o",
        type=str,
        help="Output file path for the generated MLIR module",
    )
    opts = p.parse_args(sys.argv[1:])

    length = int(opts.length)
    num_cores = int(opts.num_cores)
    dev = opts.device  # Now this is already a device object!

    # Validate num_cores based on device type
    if num_cores > len(dev.get_compute_tiles()):
        raise ValueError(
            f"[ERROR] Device cannot allocate more than {len(dev.get_compute_tiles())} cores"
        )

    channels = int(opts.chans)
    if channels < 1 or channels > 2:
        raise ValueError("Number of channels must be 1 or 2")
    tile_size = int(opts.tile_size)
    # Check the size of the workload. Since DMA transfers operate on a granularity of
    # 32 bits, the workload must have a size that's a multiple of 32 bits
    # Calculate how many bfloat16 values fit in an int32
    bfloat16_per_int32 = np.dtype(np.int32).itemsize // np.dtype(bfloat16).itemsize
    if length % bfloat16_per_int32 != 0:
        print(
            f"DMA transfers operate on a granularity of 32-bits, so for bfloat16 length must be a multiple of {bfloat16_per_int32} but is {length}"
        )
    ## Bypass is a boolean value that indicates if the bypass path should be used
    ## It must be one of the following: yes, true, t, 1
    ## It is converted to a boolean value
    bypass = str(opts.bypass).lower() in ("yes", "true", "t", "1")
    trace_size = opts.trace_size
    # Call the my_mem_copy function with the parsed arguments
    # and print the MLIR as a result
    module = my_mem_copy(
        dev, length, num_cores, channels, bypass, tile_size, trace_size
    )

    output_file_path = Path(opts.output_file_path)

    with open(output_file_path, "w") as f:
        f.write(str(module))
