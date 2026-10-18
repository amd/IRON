#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
"""Write a dequantized weight sidecar next to model.q4nx.

    python3 dequantize.py <model_dir> --mode bf16 --only ""
    python3 dequantize.py <model_dir> --mode bfp --only ""

The ``bf16`` mode writes the layout consumed by FastFlowLM GEMM. The ``bfp``
mode writes the packed BFP16EBS8 layout consumed by IRON GEMM.
"""

import argparse
import json
import os
import struct
import sys

import aie.utils as aie_utils
import numpy as np
from aie.iron.device import NPU2

from iron.applications.gemma4_flm.build import gemm
from iron.operators.flm.aie2p_math_emulation import f32_to_bf16_floor
from iron.operators.flm.q4nx import BLOCK_BYTES, GROUP, K_TILE, M_TILE, parts

SUFFIX = {"bf16": ".dq_bf16", "bfp": ".dq_bfp"}
DTYPE = {"bf16": "BF16", "bfp": "U8"}


def read_header(path):
    with open(path, "rb") as file:
        (header_len,) = struct.unpack("<Q", file.read(8))
        return json.loads(file.read(header_len)), 8 + header_len


def read_tensor(path, header, data_start, name):
    meta = header[name]
    start, end = meta["data_offsets"]
    with open(path, "rb") as file:
        file.seek(data_start + start)
        return np.frombuffer(file.read(end - start), dtype=np.uint8), meta


def bf16_to_f32(values):
    return (values.astype(np.uint32) << 16).view(np.float32)


def dequantize(raw, cols):
    """Dequantize a q4nx tensor to f32 with shape (out_features, cols)."""
    codes, scales, mins = parts(raw)
    grp = np.arange(K_TILE) // GROUP
    values = mins[..., grp] + scales[..., grp] * codes
    blocks_per_row = cols // K_TILE
    result = np.empty((len(values) // blocks_per_row * M_TILE, cols), np.float32)
    for block, value in enumerate(values):
        row = (block // blocks_per_row) * M_TILE
        col = (block % blocks_per_row) * K_TILE
        result[row : row + M_TILE, col : col + K_TILE] = value
    return result


def dequant_offset(k, n, k_dim):
    """Return the dequant output offset for logical element (k, n)."""
    return (
        (n // 128) * 128 * k_dim
        + (k // 512) * 128 * 512
        + ((n % 128) // 8) * 8 * 512
        + (k % 8) * 512
        + ((k % 512) // 8) * 8
        + (n % 8)
    )


def to_dequant_layout(weights):
    """Scatter an (N, K) matrix into FastFlowLM dequant output order."""
    n_dim, k_dim = weights.shape
    kk, nn = np.meshgrid(np.arange(k_dim), np.arange(n_dim), indexing="ij")
    result = np.empty(k_dim * n_dim, dtype=np.uint16)
    result[dequant_offset(kk, nn, k_dim)] = f32_to_bf16_floor(
        np.ascontiguousarray(weights.T)
    )
    return result


def through_bf16(weights):
    """Apply the dequant kernel's bf16 conversion and widen to f32."""
    return (f32_to_bf16_floor(weights).astype(np.uint32) << 16).view(np.float32)


def to_bfp16ebs8(weights):
    """Pack an (N, K) matrix for the B operand of build.gemm()."""
    n_dim, k_dim = weights.shape
    op = gemm(M=256, K=k_dim, N=n_dim, gelu=False)
    return op.pack_B(np.ascontiguousarray(through_bf16(weights).T)).view(np.uint8)


def build(raw, cols, mode):
    weights = dequantize(raw, cols)
    if mode == "bf16":
        return to_dequant_layout(weights).view(np.uint8), DTYPE[mode]
    if mode == "bfp":
        return to_bfp16ebs8(weights), DTYPE[mode]
    raise ValueError(f"unknown mode {mode!r}")


def write_container(path, plan, note):
    """Write one tensor at a time after constructing the container header."""
    header, offset = {}, 0
    for name, nbytes, dtype, _ in plan:
        header[name] = {
            "dtype": dtype,
            "shape": [nbytes // (2 if dtype == "BF16" else 1)],
            "data_offsets": [offset, offset + nbytes],
        }
        offset += nbytes
    header["__metadata__"] = note

    blob = json.dumps(header).encode()
    blob += b" " * ((-len(blob)) % 8)
    with open(path, "wb") as file:
        file.write(struct.pack("<Q", len(blob)))
        file.write(blob)
        for name, nbytes, _, make_payload in plan:
            payload = make_payload()
            assert payload.nbytes == nbytes, f"{name}: {payload.nbytes} != {nbytes}"
            file.write(payload.tobytes())
            yield name


IN_FEATURES = {
    "self_attn.q_proj": "D",
    "self_attn.k_proj": "D",
    "self_attn.v_proj": "D",
    "self_attn.o_proj": "DQ",
    "mlp.gate_proj": "D",
    "mlp.up_proj": "D",
    "mlp.down_proj": "I",
}


def layer_dims(config, layer_idx):
    hidden = config["hidden_size"]
    non_skip = config["num_hidden_layers"] - config["num_kv_shared_layers"]
    intermediate = config["intermediate_size"]
    if layer_idx >= non_skip and config.get("use_double_wide_mlp"):
        intermediate *= 2
    head = (
        config["global_head_dim"]
        if config["layer_types"][layer_idx] == "full_attention"
        else config["head_dim"]
    )
    return {
        "D": hidden,
        "I": intermediate,
        "DQ": head * config["num_attention_heads"],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("model_dir")
    parser.add_argument("--mode", default="bf16", choices=sorted(SUFFIX))
    parser.add_argument("--only", default="")
    parser.add_argument("--layers", default=None, help="comma-separated layer indices")
    parser.add_argument("--out", default=None)
    args = parser.parse_args()
    layers = (
        None if args.layers is None else {int(item) for item in args.layers.split(",")}
    )

    q4nx = os.path.join(args.model_dir, "model.q4nx")
    header, data_start = read_header(q4nx)
    with open(os.path.join(args.model_dir, "config.json")) as file:
        config = json.load(file)

    plan = []
    for layer_idx in range(config["num_hidden_layers"]):
        if layers is not None and layer_idx not in layers:
            continue
        dims = layer_dims(config, layer_idx)
        for suffix, dimension in IN_FEATURES.items():
            if args.only not in suffix:
                continue
            name = f"model.layers.{layer_idx}.{suffix}.weight"
            if name not in header:
                continue
            cols = dims[dimension]
            meta = header[name]
            raw_bytes = meta["data_offsets"][1] - meta["data_offsets"][0]
            n_values = raw_bytes // BLOCK_BYTES * M_TILE * K_TILE
            n_bytes = n_values * 2 if args.mode == "bf16" else n_values // 8 * 9
            output_name = name + SUFFIX[args.mode]

            def make(name=name, cols=cols):
                raw, _ = read_tensor(q4nx, header, data_start, name)
                payload, _ = build(raw, cols, args.mode)
                return payload

            plan.append((output_name, n_bytes, DTYPE[args.mode], make))

    if not plan:
        print(f"No tensors matched --only {args.only!r}")
        return 1

    total = sum(nbytes for _, nbytes, _, _ in plan)
    output = args.out or f"model.dq_{args.mode}"
    output_path = os.path.join(args.model_dir, output)
    print(f"Writing {len(plan)} tensors, {total / 1024**3:.3f} GiB -> {output_path}")

    note = {
        "producer": "dequantize.py",
        "mode": args.mode,
        "source": "model.q4nx",
    }
    with aie_utils.set_current_device(NPU2()):
        for index, name in enumerate(write_container(output_path, plan, note)):
            if index % 10 == 0 or index == len(plan) - 1:
                print(f"  [{index + 1:3d}/{len(plan)}] {name}")
    print(f"done: {os.path.getsize(output_path) / 1024**3:.3f} GiB")
    return 0


if __name__ == "__main__":
    sys.exit(main())
