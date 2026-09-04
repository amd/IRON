#!/usr/bin/env python3
"""NPU INT8 GEMM benchmark: bit-exactness + TOPS for one or many shapes.

Replaces the earlier scratch scripts (bench_int8.py, int8_bench.py,
run_int8_gemm.py) with a single parameterized harness. Uses the exact
i8->i32 path (32-bit accumulator, the only bit-exact integer output).

Usage:
  PYTHONPATH=/usr/lib/python3/dist-packages python bench_int8_gemm.py \
      [--shapes M,K,N [M,K,N ...]] [--reps N] [--partition N] [--tiles m,k,n] \
      [--build-dir DIR] [--seed N]

Defaults: 2048x2048x2048, 3 reps, no partition, 64x64x64 tiles.

For wide outputs (N * n_aie_cols * 4 bytes > ~1 GiB of C, or per-column C
slices past the aie.dma_bd stride cap of 2^20 elements) the design must
split N via --partition: each partition compiles with N/partition and the
output is concatenated along the column axis.
"""
import argparse
import gc
import time

import numpy as np

import sys

sys.path.insert(0, "/home/bcloud/amd-oss/iron")

from iron.common.context import AIEContext
from iron.operators import GEMM
from aie.utils.hostruntime.xrtruntime.tensor import XRTTensor


def run_shape(M, K, N, tiles, cols, reps, seed, build_dir, retry_on_mismatch=False, b_i4=False):
    tm, tk, tn = tiles
    rng = np.random.default_rng(seed)
    A_np = rng.integers(-8, 8, size=(M, K), dtype=np.int8)
    B_np = rng.integers(-8, 8, size=(K, N), dtype=np.int8)
    ref = A_np.astype(np.int32) @ B_np.astype(np.int32)

    ctx = AIEContext(build_dir=build_dir)
    ctx.build_dir.mkdir(parents=True, exist_ok=True)
    kw = dict(M=M, K=K, N=N, tile_m=tm, tile_k=tk, tile_n=tn,
              num_aie_columns=cols, dtype_in="i8", dtype_out="i32", context=ctx)
    if b_i4:
        # Asymmetric 4-bit weights: B arrives packed (K, N//2) int8 (two
        # nibbles per byte, low nibble first) and the kernel uses the AIE2P
        # 4x16x16 mmul (2x int8xint8 MAC density). N must be even.
        assert N % 2 == 0, "N must be even for packed i4 weights"
        kw["dtype_b"] = "i4"
    op = (
        GEMM(**kw)
        .compile()
        .get_callable()
    )
    A = XRTTensor((M, K), dtype=np.int8)
    B = XRTTensor((K, N // 2) if b_i4 else (K, N), dtype=np.int8)
    C = XRTTensor((M, N), dtype=np.int32)
    A.numpy()[:] = A_np
    B.numpy()[:] = GEMM.pack_i4(B_np) if b_i4 else B_np

    op(A, B, C)  # warm-up: also settles the first-dispatch context race
    times = []
    C_np = None
    for _ in range(reps):
        res = op(A, B, C)
        times.append(res.npu_time)
        C_np = C.to_torch().numpy()  # read back each rep; last one is checked
    n_ops = 2 * M * K * N
    t = np.asarray(times) * 1e-9
    exact = bool(np.array_equal(C_np, ref))
    bad = int(np.count_nonzero(C_np != ref)) if not exact else 0
    md = int(np.abs(C_np.astype(np.int64) - ref.astype(np.int64)).max()) if not exact else 0
    # The XRT/amdxdna first-dispatch flake (see GEMM docstring) is transient
    # and self-heals on the next dispatch: if the last result mismatches,
    # re-run once and report the retry outcome so a flake doesn't read as a
    # kernel failure.
    if not exact and retry_on_mismatch:
        op(A, B, C)  # warm again (same buffers, same context)
        res = op(A, B, C)
        C_retry = C.to_torch().numpy()
        exact_retry = bool(np.array_equal(C_retry, ref))
        bad_retry = int(np.count_nonzero(C_retry != ref)) if not exact_retry else 0
        md_retry = int(np.abs(C_retry.astype(np.int64) - ref.astype(np.int64)).max()) if not exact_retry else 0
        print(
            f"  [retry] first dispatch mismatched (flake?); retry: "
            f"exact={exact_retry} bad={bad_retry} max_abs={md_retry}",
            flush=True,
        )
        if exact_retry:
            exact, bad, md = True, 0, 0
    print(
        f"{M}x{K}x{N} (tile {tm}x{tk}x{tn}, {cols} col): "
        f"exact={exact} bad={bad} max_abs={md} "
        f"npu_ms={np.round(t * 1e3, 2).tolist()} "
        f"TOPS best={n_ops / t.min() / 1e12:.2f} mean={n_ops / t.mean() / 1e12:.2f}",
        flush=True,
    )
    return exact


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--shapes", nargs="+", default=["2048,2048,2048"],
                   help="M,K,N triples, e.g. '2048,2048,2048'")
    p.add_argument("--reps", type=int, default=3)
    p.add_argument("--partition", type=int, default=1,
                   help="split each shape's N into this many partitions")
    p.add_argument("--tiles", default="64,64,64", help="tile_m,tile_k,tile_n")
    p.add_argument("--cols", type=int, default=8, help="num_aie_columns")
    p.add_argument("--build-dir", default="build_int8_gemm")
    p.add_argument("--seed", type=int, default=0)
    p.add_argument("--verify-retry", action="store_true",
                   help="re-run once on a result mismatch (handles the transient "
                        "XRT first-dispatch flake; see GEMM docstring)")
    p.add_argument("--b-i4", action="store_true",
                   help="asymmetric INT4 weights: B values in [-8,7] packed "
                        "(K, N//2) int8, kernel uses the 4x16x16 mmul")
    args = p.parse_args()

    tm, tk, tn = (int(v) for v in args.tiles.split(","))
    all_exact = True
    for spec in args.shapes:
        M, K, N = (int(v) for v in spec.split(","))
        if args.partition <= 1:
            ex = run_shape(M, K, N, (tm, tk, tn), args.cols, args.reps,
                           args.seed, args.build_dir, args.verify_retry,
                           args.b_i4)
            all_exact = all_exact and ex
        else:
            # Partition: per-partition N must keep each C slice inside the
            # aie.dma_bd stride cap (see module docstring).
            N_part, parts = N, args.partition
            assert N % parts == 0, f"N={N} not divisible by {parts}"
            N_part = N // parts
            rng = np.random.default_rng(args.seed)
            A_np = rng.integers(-8, 8, size=(M, K), dtype=np.int8)
            B_full = rng.integers(-8, 8, size=(K, N), dtype=np.int8)
            ref = A_np.astype(np.int32) @ B_full.astype(np.int32)
            ctx = AIEContext(build_dir=args.build_dir)
            ctx.build_dir.mkdir(parents=True, exist_ok=True)
            op = (
                GEMM(
                    M=M, K=K, N=N_part, tile_m=tm, tile_k=tk, tile_n=tn,
                    num_aie_columns=args.cols, dtype_in="i8", dtype_out="i32",
                    context=ctx,
                )
                .compile()
                .get_callable()
            )
            A = XRTTensor((M, K), dtype=np.int8)
            A.numpy()[:] = A_np
            tot_ns = 0.0
            C_parts = []
            for i in range(parts):
                Bp = B_full[:, i * N_part:(i + 1) * N_part]
                B = XRTTensor((K, N_part), dtype=np.int8)
                B.numpy()[:] = Bp
                C = XRTTensor((M, N_part), dtype=np.int32)
                op(A, B, C)  # warm
                res = op(A, B, C)
                tot_ns += res.npu_time
                Cp = np.array(C.to_torch().numpy(), copy=True)
                C_parts.append(Cp)
                del B, C
                gc.collect()
            C_concat = np.concatenate(C_parts, axis=1)
            ex = bool(np.array_equal(C_concat, ref))
            bad = int(np.count_nonzero(C_concat != ref)) if not ex else 0
            n_ops = 2 * M * K * N
            print(
                f"{M}x{K}x{N} (partition={parts}): exact={ex} bad={bad} "
                f"TOPS={n_ops / (tot_ns * 1e-9) / 1e12:.2f}",
                flush=True,
            )
            all_exact = all_exact and ex

    print(f"ALL EXACT: {all_exact}")
    return 0 if all_exact else 1


if __name__ == "__main__":
    sys.exit(main())
