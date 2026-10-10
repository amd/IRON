<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Handoff, 2026-10-10 (xcoradaie220, Strix Halo, npu2)

The plan and its decisions are in `plan.md` beside this file; its "Status and decisions, 10-10" section has the current order. This file is where the work stands.

## Environment

- **Venv:** `source build/env-next.sh` (`build/venv-next`, mlir_aie 1.4.5.dev22+g35fa6b1, the pin). It sets `NPU_CACHE_HOME=build/npu-cache-next`. Source `/opt/xilinx/xrt/setup.sh` before any device run.
- **Device runs** go from an exported tree, because the main tree holds edits that need a newer mlir-aie (below):
  `git checkout-index -a --prefix=/tmp/claude-idxN/`, then run there with `PYTHONPATH=/tmp/claude-idxN:$PYTHONPATH`.
- Run under `ulimit -v 16000000` (48000000 for a table build, below) with `NUMPY_MADVISE_HUGEPAGE=0`, one NPU job at a time, and no CPU-heavy work (an mlir-aie build) while a table measures.

## IRON

- `iron-next` is at 0a0774d9, all pushed.
- **Uncommitted in the main tree: `Runtime.add_buffer`.** An `array()` may return a `Buffer` only the sequence reaches (`design/build.py`); flm.GEMM returns its memtile B buffers and names its flows (`flm/gemm/op.py`); a fused image refuses two designs with one `array_key` whose arrays differ beyond their per-call symbols (`image/fusion.py`); tests in `tests/common/fused_identity.py`; one AGENTS.md line. It needs an mlir-aie with `Runtime.add_buffer` (below), so it is unverified on dev22.

## The table build (running at handoff)

- **What:** the fused Llama npu2 cost table, `python -m iron.lm.llama3.tune`, at turbo, from `/tmp/claude-idx17` (an export of 0a0774d9). All 53 steps are measured, every setting exact and accurate (`/tmp/claude-table-fused2.log`).
- **The MHA points phase needs more than a 16 GB address space.** Under `ulimit -v 16000000` it failed twice in `measure_points` ("MHA: 3 points of 24 settings") with `mmap_range(len=679477248) failed (err=-12)`. A batch holds 16 probes (`CONTEXTS`), each with a 679 MB input buffer, plus their host copies. The limit is the virtual cap, not locked memory: `/tmp/claude-bo-limit.py` holds 23 such buffers (14.55 GiB) under the 16 GB cap and 30 (19 GiB) under 48 GB, with `ulimit -l` unchanged. The host has ~108 GB available.
- Under `ulimit -v 48000000` the MHA points pass (`/tmp/claude-table-fused4.log`).
- **Open, and the build's blocker: a negative load on the 11 ms GEMV.** `measure_loads` refuses `GEMV_9f44cdecd41cf49579d1defe` beside `ElementwiseAdd_0c0e29c7f4f78b14e9a495bf`. It measured −60.7 us, then −77.0 us on a rerun (`/tmp/claude-table-fused5.log`), so the effect is systematic, not noise. That GEMV is the LM-head-sized one: `t_step_us` 11047 (noise 1.3), and its step entry already has `alone_us` −40.3. Alternating it with the Add runs faster than grouping it, by about 0.5–0.7% of a step. The per-round standard error misses that, because the difference sits between the two orders, not between rounds. Every other load is measured and cached, so a rerun repeats only this batch.
  - **Your call:** how to price a load the model can't resolve on a step this long. For example, count a load within a fraction of the pair's step time as zero (as `calibrate` in `probe.py` already does within its noise), or give the step's order effect its own noise term. Nothing was changed.
  - The table at `/tmp/claude-idx17/iron/lm/llama3/costs_npu2.json` (16:12) has every step and the calibrations, but no loads past this point.
- **Output:** `/tmp/claude-idx17/iron/lm/llama3/costs_npu2.json`. Copy it into the main tree's `iron/lm/llama3/` to commit it.
- **If it was stopped:** rerun the same command. Every measurement is kept in the cost cache (`build/npu-cache-next/iron/costs/<platform>/turbo/`), so it resumes where it was.

  ```bash
  cd /tmp/claude-idx17 && source /opt/xilinx/xrt/setup.sh >/dev/null && source /scratch/ehunhoff/IRON/build/env-next.sh && export PYTHONPATH=/tmp/claude-idx17:$PYTHONPATH NUMPY_MADVISE_HUGEPAGE=0 && ulimit -v 48000000 && python -m iron.lm.llama3.tune > /tmp/claude-table-fused6.log 2>&1
  ```

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
- Then an IRON venv on it, to verify and commit the `add_buffer` edits.

## Next IRON work, after the tables

1. **Per-core stream count in `Operator._finish_at`** (`iron/common/declare/operator.py`, around line 908). Today `reads` sums every streamed operand of the array against one core's `core_dma_channels_in`. Count, per core, the shim and memtile reads of the finishing core plus its finish inputs; leave core-to-core fifos to the placer. Device-test RMSNorm → Add, re-census EG2's folds, and correct c9dc5cbd's AGENTS.md lines that say pinning the two cores would free the first.
2. **The held ride.** Today's `feed=True` ride is per output tile and needs `feed.count == out.count`; RMSNorm's weight has one lane per channel against `y`'s columns × channels, so it is refused. Add a held variant: the feed held, the rider a held row, one more fill per lane per call.
3. **Dataflow fusion design,** starting with the null-kernel experiment in `plan.md`.

## Fold census (device-free, `/tmp/claude-llama-folds.py`, one Llama layer on npu2)

- **Prompt chunk:** 23 → 21 steps (RMSNorm into GEMV, SiLU into GEMM); left Copy 4, RMSNorm 2, GEMM 7, RoPE 2, MHA 1, ElementwiseAdd 2, ElementwiseMul 1, GEMV 1, Sample 1.
- **Decode:** 23 → 14 steps (every norm, Add and Mul folded); left Copy 2, GEMV 8, RoPE 2, MHA 1, Sample 1.

## Untracked files to keep

`.flmenv.sh`, `scratch_merge/`, `scratch_review/` (the review reports behind `plan.md`), `build/aie-overlay-addbuf`, `build/mlir-aie-addbuf-src`, `build/wheel-main` and the `/tmp/claude-*` trees. None is to be deleted without asking.
