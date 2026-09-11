#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""reference() must match the device's angle convention: design.py's core_body
acquires one angle row and applies it to `rows // angle_rows` consecutive input
rows before moving to the next, so row r uses angle row
`r // (rows // angle_rows)`.

That convention and the interleaved one (`r % angle_rows`) agree whenever
angle_rows is 1 or rows, so only 1 < angle_rows < rows tells them apart --
the regime llama_npu.py's prefill RoPE shape sits in
(rows=prompt_len*n_heads, angle_rows=prompt_len).
"""

import torch

from iron.operators.rope.reference import reference


def _block_major_expected(x, angles, rows, angle_rows):
    """Device convention spelled out row by row: row r uses angle row
    r // (rows // angle_rows)."""
    cols = x.shape[-1]
    half = cols // 2
    tensor_rows_per_angle_row = rows // angle_rows
    out = torch.empty(rows, cols, dtype=torch.float32)
    for r in range(rows):
        a = r // tensor_rows_per_angle_row
        cos = angles[a, 0::2].to(torch.float32)
        sin = angles[a, 1::2].to(torch.float32)
        x1, x2 = x[r, :half].to(torch.float32), x[r, half:].to(torch.float32)
        out[r, :half] = x1 * cos - x2 * sin
        out[r, half:] = x2 * cos + x1 * sin
    return out.to(torch.bfloat16)


def _make_inputs(rows, angle_rows, cols=4, seed=0):
    torch.manual_seed(seed)
    half = cols // 2
    x = torch.randn(rows, cols).to(torch.bfloat16)
    angles = torch.zeros(angle_rows, cols, dtype=torch.bfloat16)
    angles[:, 0::2] = torch.rand(angle_rows, half).to(torch.bfloat16)
    angles[:, 1::2] = torch.rand(angle_rows, half).to(torch.bfloat16)
    return x, angles


def test_reference_matches_device_convention_for_batched_angle_rows():
    """1 < angle_rows < rows, the only regime that separates the two conventions."""
    rows, angle_rows = 6, 3
    x, angles = _make_inputs(rows, angle_rows)
    expected = _block_major_expected(x, angles, rows, angle_rows)
    got = reference(x, angles, rows=rows, cols=x.shape[-1])
    assert torch.equal(expected, got)


def test_reference_matches_device_convention_across_shapes():
    for rows, angle_rows in [(8, 2), (1024, 1), (4, 4), (13, 13), (12, 4)]:
        x, angles = _make_inputs(rows, angle_rows)
        expected = _block_major_expected(x, angles, rows, angle_rows)
        got = reference(x, angles, rows=rows, cols=x.shape[-1])
        assert torch.equal(
            expected, got
        ), f"mismatch at rows={rows} angle_rows={angle_rows}"
