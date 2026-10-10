<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Handoff, 2026-10-10 (xcoradaie220, Strix Halo, npu2)

The plan and its decisions are in `plan.md` beside this file; its "Status and decisions, 10-10" section has the current order. This file is where the work stands.

## Environment

- **Venv:** `source build/env-next.sh` (`build/venv-next`, mlir_aie 1.4.5.dev22+g35fa6b1, the pin). It sets `NPU_CACHE_HOME=build/npu-cache-next`. Source `/opt/xilinx/xrt/setup.sh` before any device run.
- **Device runs** go from an exported tree, so that edits in the main tree don't reach the run:
  `git checkout-index -a --prefix=/tmp/claude-idxN/`, then run there with `PYTHONPATH=/tmp/claude-idxN:$PYTHONPATH`.
- Run under `ulimit -v 16000000` (48000000 for a table build, below) with `NUMPY_MADVISE_HUGEPAGE=0`, one NPU job at a time, and no CPU-heavy work (an mlir-aie build) while a table measures.

## IRON

- Everything this handoff needs is on `iron-next`; the last commit is this file's.
- **`Runtime.add_buffer` is a patch, `add_buffer.patch` beside this file**, not applied. An `array()` may return a `Buffer` only the sequence reaches (`design/build.py`); flm.GEMM returns its memtile B buffers and names its flows (`flm/gemm/op.py`); a fused image refuses two designs with one `array_key` whose arrays differ beyond their per-call symbols (`image/fusion.py`); tests in `tests/common/fused_identity.py`; one AGENTS.md line. The dev22 pin has no `Runtime.add_buffer`, so applied on the pin it would break flm.GEMM; it is unverified. Apply it (`git apply docs/plans/add_buffer.patch`) on a venv built from mlir-aie iron-next (below), test, and commit it as code. The same edits are also still uncommitted in the main tree on xcoradaie220.

## The fused table build (stopped at handoff; resumes from the cache)

- **What:** the fused Llama npu2 cost table, `python -m iron.lm.llama3.tune`, at turbo. All 53 steps, the MHA points and the calibrations are measured. Every setting is exact and accurate.
- **Run it under `ulimit -v 48000000`.** The MHA points phase needs more than a 16 GB address space: a batch holds 16 probes (`CONTEXTS`), each with a 679 MB input buffer, plus their host copies. Under 16 GB it fails with `mmap_range(len=679477248) failed (err=-12)`. The limit is the virtual cap, not locked memory: `scripts/bo_limit.py` holds 23 such buffers (14.55 GiB) under the 16 GB cap and 30 (19 GiB) under 48 GB.
- **The negative load that stopped it is fixed by e29b04d9.** `measure_loads` refused the 11 ms LM-head-sized GEMV beside the reference Add (−60.7 us, then −77.0 us on a rerun). Alternated and grouped runs of a DDR-bound step differ by 0.55–0.70% of it, a bias the per-round noise misses. `ORDER_BIAS`, 1% of the step, now counts in the noise, so such a load is priced as zero. Verified by the two pack tests in `tests/infrastructure/narrowing.py` on npu2; the build itself has not yet passed that batch.
- **What's left:** loads for 549 settings (378 of them GEMVs, with the 11 ms ones among them), then up to 3 rounds of packs. That's a few hours of NPU time; the first 198 loads are cached. The table is saved after each phase.
- **Resume** from a fresh export of `iron-next`. Every measurement is in the cost cache (`build/npu-cache-next/iron/costs/<platform>/turbo/`), so nothing measured is repeated:

  ```bash
  git checkout-index -a --prefix=/tmp/claude-idx19/
  cd /tmp/claude-idx19 && source /opt/xilinx/xrt/setup.sh >/dev/null && source /scratch/ehunhoff/IRON/build/env-next.sh && export PYTHONPATH=/tmp/claude-idx19:$PYTHONPATH NUMPY_MADVISE_HUGEPAGE=0 && ulimit -v 48000000 && python -m iron.lm.llama3.tune > /tmp/claude-table-fused7.log 2>&1
  ```

- **Output:** `iron/lm/llama3/costs_npu2.json` in the export. Copy it into the main tree to commit it.

- **Expected in the log:** decode MHA settings refused with "moves by a per-call size, so it must fit one buffer descriptor"; the GEMM builds print aiecc `maskpoll` notes (not errors; left alone).
- **Then, in order:**
  1. `--dispatch separate` (writes `costs_npu2_separate.json`), under the same 48 GB cap.
  2. Check both tables for negative loads.
  3. Fold search and re-tune every version: decode, the prompt chunk, EG2's rows.
  4. Interleaved A/B, 8 or more rounds, with the accuracy checks.
  5. Commit the tables; `iron/tests/common/cost_tables.py` should then pass.

## mlir-aie

- **Local clone:** `build/mlir-aie-addbuf-src` (blobless, fetches over https), checked out on its local `iron-next`:
  - origin/iron-next 8db6b9e5e (shim channel sharing, the placer that agrees with it, time-mode links, fan-in routes);
  - ca96fee23, `Runtime.add_buffer`;
  - 81d29767d, a cherry-pick of cf4a6b79f from `objectfifo-transport-routes` ("Keep a sending shim end in flight to the end of its sequence"): applied cleanly, patch identical, `-x` line in its message.
- **Not built and not pushed.** Build it after the tables, run the lit tests the cherry-pick touches (`shim_sharing.mlir`, `sequential_placer/test_place_errors.mlir`, `test_place_shim_sharing.mlir`), then the npu-xrt test `test_objectfifo_placed_shim_sharing.py`.
- **Push (yours, after those pass):** `git -C /scratch/ehunhoff/IRON/build/mlir-aie-addbuf-src push git@github.com:Xilinx/mlir-aie.git iron-next:iron-next` sends both commits.
- These two commits live only in that clone on xcoradaie220 until you push them.
- Then an IRON venv on it, to apply, verify and commit `add_buffer.patch`.

## Next IRON work, after the tables

1. **Per-core stream count in `Operator._finish_at`** (`iron/common/declare/operator.py`, around line 908). Today `reads` sums every streamed operand of the array against one core's `core_dma_channels_in`. Count, per core, the shim and memtile reads of the finishing core plus its finish inputs; leave core-to-core fifos to the placer. Device-test RMSNorm → Add, re-census EG2's folds, and correct c9dc5cbd's AGENTS.md lines that say pinning the two cores would free the first.
2. **The held ride.** Today's `feed=True` ride is per output tile and needs `feed.count == out.count`; RMSNorm's weight has one lane per channel against `y`'s columns × channels, so it is refused. Add a held variant: the feed held, the rider a held row, one more fill per lane per call.
3. **Dataflow fusion design,** starting with the null-kernel experiment in `plan.md`.

## Fold census (device-free, `scripts/llama_folds.py --step decode|prompt`, one Llama layer on npu2)

- **Prompt chunk:** 23 → 21 steps (RMSNorm into GEMV, SiLU into GEMM); left Copy 4, RMSNorm 2, GEMM 7, RoPE 2, MHA 1, ElementwiseAdd 2, ElementwiseMul 1, GEMV 1, Sample 1.
- **Decode:** 23 → 14 steps (every norm, Add and Mul folded); left Copy 2, GEMV 8, RoPE 2, MHA 1, Sample 1.

## Untracked files to keep

`.flmenv.sh`, `scratch_merge/`, `scratch_review/` (the review reports behind `plan.md`), `build/aie-overlay-addbuf`, `build/mlir-aie-addbuf-src`, `build/wheel-main` and the `/tmp/claude-*` trees (exports and logs; nothing in them is needed to resume). None is to be deleted without asking.
