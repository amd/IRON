# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Bitwise device goldens of the flm operators, for changes that move their MLIR.

``python -m iron.operators.flm.goldens record|check <dir>``. Record before a
change that moves the MLIR, then check after; inputs are saved, not redrawn,
so a later change to a test's draw doesn't move a golden. The .npz files
stay local; they are not committed.
"""

import argparse
import sys
from pathlib import Path

import aie.utils as aie_utils
import numpy as np
from aie.dialects._aie_enum_gen import AIEArch
from aie.iron.kernels import FLM_GEMMA4_E2B_DECODE, FLM_GEMMA4_E4B_DECODE
from ml_dtypes import bfloat16

from iron.common.testing import vectors
from iron.operators.flm.dequant.op import DequantBFP
from iron.operators.flm.layer.design import LayerType
from iron.operators.flm.layer.op import DecodeLayer
from iron.operators.flm.layer.reference import generate_inputs
from iron.operators.flm.lm_head.op import LMHead
from iron.operators.flm.prefill_attn.op import (
    PrefillAttention,
    PrefillSlidingAttention,
)

# Every byte of an output before the dispatch (bf16 3.0), so a write past its
# rows shows.
SENTINEL = 0x40

# The dispatches of layer/test.py: near the start of a cache and deep into
# it, and a sliding window before, at and after its ring wraps.
DECODE_CONTEXTS = {
    LayerType.GLOBAL: (5, 700),
    LayerType.SWA: (37, 511, 512, 700, 1023),
    LayerType.GLOBAL_SKIP: (37, 700),
    LayerType.SWA_SKIP: (37, 511, 512, 700, 1023),
}
DECODE_MAX_L = 1024

# prefill_attn/test.py's builds and token ranges (L_begin, L_end, max_l).
PREFILL = {
    "attn": (
        PrefillAttention,
        1024,
        [(0, 128, 1024), (0, 512, 1024), (128, 384, 1024), (256, 1024, 1024)],
    ),
    "swa": (
        PrefillSlidingAttention,
        2048,
        [(0, 128, 2048), (0, 1024, 2048), (512, 1024, 2048), (1024, 2048, 2048)],
    ),
}


def _prefill_inputs(op, max_l, seed):
    rng = np.random.default_rng(seed)
    half = max_l * op.num_kv_heads * op.head_dim
    q = (rng.standard_normal(op.qo_len) * 0.2).astype(bfloat16)
    kv = np.zeros(op.kv_len, dtype=bfloat16)
    kv[:half] = (rng.standard_normal(half) * 0.2).astype(bfloat16)
    kv[half : 2 * half] = rng.standard_normal(half).astype(bfloat16)
    return dict(q=q, kv=kv)


def cases():
    """Each golden: its file stem, the operator, its inputs by buffer name
    (a function of nothing, drawn only when recording) and its per-call values.
    """
    for name, geometry in (
        ("E2B", FLM_GEMMA4_E2B_DECODE),
        ("E4B", FLM_GEMMA4_E4B_DECODE),
    ):
        for layer_type, contexts in DECODE_CONTEXTS.items():
            op = DecodeLayer(geometry=geometry, layer_type=layer_type)
            for c in contexts:
                yield (
                    f"DecodeLayer-{name}-{layer_type}-{c}",
                    op,
                    lambda op=op, c=c: dict(
                        zip(
                            ("x", "proj", "rms", "rope_rms", "kv"),
                            generate_inputs(op.dims, c, DECODE_MAX_L, seed=c),
                        )
                    ),
                    dict(context_len=c, max_l=DECODE_MAX_L),
                )
    for cls, max_context, ranges in PREFILL.values():
        for num_kv_heads in (1, 2):
            op = cls(max_context=max_context, num_heads=8, num_kv_heads=num_kv_heads)
            for L_begin, L_end, max_l in ranges:
                yield (
                    f"{cls.__name__}-kv{num_kv_heads}-{L_begin}-{L_end}-{max_l}",
                    op,
                    lambda op=op, m=max_l, s=L_end: _prefill_inputs(op, m, s),
                    dict(L_begin=L_begin, L_end=L_end, max_l=max_l),
                )
    for cls in (LMHead, DequantBFP):
        for case in cls.test.cases:
            if not case.extensive:
                op = cls(**case.kwargs)
                yield (
                    f"{cls.__name__}-{case.label}",
                    op,
                    lambda op=op: vectors(op, **op.test.draw(op)).inputs,
                    {},
                )


def dispatch(op, initial, values):
    """Run ``op`` once on buffers holding ``initial``'s bytes at their start;
    each buffer's bytes after, by name.
    """
    tensors = []
    for b in op.buffers:
        t = aie_utils.DEFAULT_TENSOR_CLASS(b.host_shape, dtype=b.host_dtype)
        view = t.numpy_view().reshape(-1).view(np.uint8)
        data = np.ascontiguousarray(initial[b.name]).reshape(-1).view(np.uint8)
        view[:] = 0
        view[: data.size] = data[: view.size]
        tensors.append(t)
    op(*tensors, **values)
    return {
        b.name: t.numpy().reshape(-1).view(np.uint8).copy()
        for b, t in zip(op.buffers, tensors)
    }


def _initial(op, draw):
    inputs = draw()
    return {
        b.name: (
            inputs[b.name]
            if b.fills
            else np.full(
                np.zeros(b.host_shape, b.host_dtype).nbytes, SENTINEL, np.uint8
            )
        )
        for b in op.buffers
    }


def record(root: Path) -> None:
    root.mkdir(parents=True, exist_ok=True)
    for stem, op, draw, values in cases():
        initial = _initial(op, draw)
        after = dispatch(op, initial, values)
        np.savez(
            root / f"{stem}.npz",
            **{
                f"in/{k}": np.ascontiguousarray(v).reshape(-1).view(np.uint8)
                for k, v in initial.items()
            },
            **{f"out/{b.name}": after[b.name] for b in op.outputs},
        )
        print(f"recorded {stem}")


def check(root: Path) -> int:
    """The number of goldens that differ, or are missing, on this build."""
    failed = 0
    for stem, op, _, values in cases():
        path = root / f"{stem}.npz"
        if not path.exists():
            print(f"MISSING {stem}")
            failed += 1
            continue
        saved = np.load(path)
        initial = {b.name: saved[f"in/{b.name}"] for b in op.buffers}
        after = dispatch(op, initial, values)
        bad = [
            f"{b.name}: {np.count_nonzero(after[b.name] != saved[f'out/{b.name}'])} bytes"
            for b in op.outputs
            if not np.array_equal(after[b.name], saved[f"out/{b.name}"])
        ]
        print(f"{'DIFFERS' if bad else 'ok'} {stem} {', '.join(bad)}")
        failed += bool(bad)
    return failed


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("action", choices=("record", "check"))
    p.add_argument("dir", type=Path)
    args = p.parse_args(argv)
    dev = aie_utils.get_current_device()
    if dev is None or dev.arch != AIEArch.AIE2p:
        p.error(
            "the goldens are recorded and checked on an NPU2; "
            + ("this host has no NPU" if dev is None else f"this host's is {dev.name}")
        )
    if args.action == "check" and not args.dir.is_dir():
        p.error(f"{args.dir} holds no goldens; record them first")
    if args.action == "record":
        record(args.dir)
        return 0
    return 1 if check(args.dir) else 0


if __name__ == "__main__":
    sys.exit(main())
