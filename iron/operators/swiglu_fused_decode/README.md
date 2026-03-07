<!--
SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Decode Dataflow Operators for Llama 3.2 1B on AMD XDNA2 NPU

This document describes the four new operators built for the high-performance
decode dataflow pipeline targeting the AMD XDNA2 (NPU2) architecture. Together,
they eliminate unnecessary DDR round-trips by keeping intermediate activations
on-chip and streaming weights through the compute tile array.

**Target model**: Llama 3.2 1B (16 layers, d_model=2048, d_ffn=8192, 32 heads,
8 KV heads, head_dim=64)

**Target hardware**: AMD XDNA2 -- 4 rows x 8 columns = 32 compute tiles,
64 KB L1 per tile, 512 KB L2 per memory tile, 50-80 GB/s DDR bandwidth

---

## Table of Contents

1. [Operator Overview](#1-operator-overview)
2. [NPU2 Tile Mapping -- Individual Operators](#2-npu2-tile-mapping----individual-operators)
3. [Full-Layer Decode Dataflow (Phase 4 Vision)](#3-full-layer-decode-dataflow-phase-4-vision)
4. [DMA Channel Budget Tables](#4-dma-channel-budget-tables)
5. [L1 Memory Budget Tables](#5-l1-memory-budget-tables)
6. [DDR Bandwidth Savings Analysis](#6-ddr-bandwidth-savings-analysis)
7. [Operator Architecture Details](#7-operator-architecture-details)

---

## 1. Operator Overview

| # | Operator | Location | Role in Decode Pipeline | Phase |
|---|----------|----------|------------------------|-------|
| 1 | `fused_qkv_proj` | `iron/operators/fused_qkv_proj/` | Fuse Q, K, V projections into a single GEMV | Phase 1 |
| 2 | `flowkv_decode` | `iron/operators/flowkv_decode/` | Streaming attention with online softmax, 2-tile pipeline | Phase 2 |
| 3 | `swiglu_fused_decode` | `iron/operators/swiglu_fused_decode/` | Complete SwiGLU MLP with on-chip intermediate | Phase 3 |
| 4 | `fused_dequant_gemv` | `iron/operators/fused_dequant_gemv/` | INT4 dequant + GEMV in a single pass (4x BW savings) | Phase 5 |

**Pipeline position in a transformer layer:**

```
Token (4 KB bf16)
  |
  v
RMSNorm
  |
  v
[1] fused_qkv_proj  ---- Wq,Wk,Wv concatenated, single GEMV
  |         |        |
  Q         K        V
  |         |        |
  v         v        v
[2] flowkv_decode  ------ 2-tile pipeline per KV head, online softmax
  |                        K/V cache streamed from DDR
  v
Output Projection (GEMV)
  |
  v
Residual Add + RMSNorm
  |
  v
[3] swiglu_fused_decode -- Dual-GEMV + SiLU*Mul + Down proj
  |                         Intermediate stays on-chip
  v
Residual Add
  |
  v
Token' (4 KB bf16)
```

Operators [4] `fused_dequant_gemv` can substitute for any bf16 GEMV stage
to achieve 4x DDR bandwidth reduction via INT4 weight quantization.

---

## 2. NPU2 Tile Mapping -- Individual Operators

### NPU2 Compute Tile Array Reference

```
NPU2 XDNA2 Architecture: 4 compute rows x 8 columns = 32 compute tiles
Rows 2-5 are compute tiles. Row 1 is memory tiles. Row 0 is shim/interface tiles.

                Col 0      Col 1      Col 2      Col 3      Col 4      Col 5      Col 6      Col 7
Row 5    +----------+----------+----------+----------+----------+----------+----------+----------+
         |  CT(0,3) |  CT(1,3) |  CT(2,3) |  CT(3,3) |  CT(4,3) |  CT(5,3) |  CT(6,3) |  CT(7,3) |
Row 4    +----------+----------+----------+----------+----------+----------+----------+----------+
         |  CT(0,2) |  CT(1,2) |  CT(2,2) |  CT(3,2) |  CT(4,2) |  CT(5,2) |  CT(6,2) |  CT(7,2) |
Row 3    +----------+----------+----------+----------+----------+----------+----------+----------+
         |  CT(0,1) |  CT(1,1) |  CT(2,1) |  CT(3,1) |  CT(4,1) |  CT(5,1) |  CT(6,1) |  CT(7,1) |
Row 2    +----------+----------+----------+----------+----------+----------+----------+----------+
         |  CT(0,0) |  CT(1,0) |  CT(2,0) |  CT(3,0) |  CT(4,0) |  CT(5,0) |  CT(6,0) |  CT(7,0) |
         +----------+----------+----------+----------+----------+----------+----------+----------+
MemTile  |  MT-0    |  MT-1    |  MT-2    |  MT-3    |  MT-4    |  MT-5    |  MT-6    |  MT-7    |
         +----------+----------+----------+----------+----------+----------+----------+----------+
Shim     |  Shim-0  |  Shim-1  |  Shim-2  |  Shim-3  |  Shim-4  |  Shim-5  |  Shim-6  |  Shim-7  |
         +----------+----------+----------+----------+----------+----------+----------+----------+
                                            DDR (LPDDR5)
```

### 2a. fused_qkv_proj -- 4 Columns, 1 Tile Per Column

Reuses the standard GEMV design with Wq/Wk/Wv concatenated row-wise into a
single (3072 x 2048) weight matrix. Each column processes 768 output rows.

```
         Col 0        Col 1        Col 2        Col 3        Col 4-7
Row 5   +------------+------------+------------+------------+- - - - -+
        |            |            |            |            |         |
Row 4   +------------+------------+------------+------------+ unused  |
        |            |            |            |            |         |
Row 3   +------------+------------+------------+------------+- - - - -+
        |            |            |            |            |
Row 2   +--[GEMV-0]--+--[GEMV-1]--+--[GEMV-2]--+--[GEMV-3]--+
        | Wqkv rows  | Wqkv rows  | Wqkv rows  | Wqkv rows  |
        | 0..767     | 768..1535  | 1536..2303 | 2304..3071 |
        +------+-----+------+-----+------+-----+------+-----+
               |            |            |            |
          DDR  v  DDR       v  DDR       v  DDR       v
        +------+-----+------+-----+------+-----+------+-----+
Shim    | Shim-0     | Shim-1     | Shim-2     | Shim-3     |
        | W_in, x_in | W_in, x_in | W_in, x_in | W_in, x_in |
        | out[0:768] |out[768:1536|out[1536:230|out[2304:307|
        +------------+------------+------------+------------+

ObjectFIFO connections per column:
  DDR --[of_weights]--> GEMV tile    (depth=2, weight rows streamed)
  DDR --[of_input]----> GEMV tile    (depth=1, x vector broadcast)
  GEMV tile --[of_output]--> DDR     (depth=2, output rows drained)

Host post-processing: split output[0:3072] into Q[0:2048], K[0:512], V[0:512]
```

### 2b. flowkv_decode -- 4 Columns, 2 Tiles Per Column (8 tiles total)

Two-tile pipeline per KV head group. Score tile computes Q*K^T with online
softmax. Value tile accumulates weighted V and normalizes. Intermediates
(exponentiated scores F_c, correction factors C_c, denominator l) flow
tile-to-tile via on-chip ObjectFIFO and never touch DDR.

With 8 KV heads and 4 columns, the runtime processes 2 batches of 4 KV
head groups each.

```
         Col 0        Col 1        Col 2        Col 3
Row 5   +------------+------------+------------+------------+
        |            |            |            |            |
Row 4   +------------+------------+------------+------------+
        |            |            |            |            |
Row 3   +--[Score-0]-+--[Score-1]-+--[Score-2]-+--[Score-3]-+
        | Q*K^T/sqrt | Q*K^T/sqrt | Q*K^T/sqrt | Q*K^T/sqrt |
        | online smax| online smax| online smax| online smax|
        +-----+------+-----+------+-----+------+-----+------+
              | inter       | inter       | inter       | inter
              | FIFO        | FIFO        | FIFO        | FIFO
              | (on-chip)   | (on-chip)   | (on-chip)   | (on-chip)
        +-----v------+-----v------+-----v------+-----v------+
Row 2   +--[Value-0]-+--[Value-1]-+--[Value-2]-+--[Value-3]-+
        | F_c*V accum| F_c*V accum| F_c*V accum| F_c*V accum|
        | O = Y / l  | O = Y / l  | O = Y / l  | O = Y / l  |
        +------+-----+------+-----+------+-----+------+-----+
               |            |            |            |
          DDR  v  DDR       v  DDR       v  DDR       v
        +------+-----+------+-----+------+-----+------+-----+
Shim    | Shim-0     | Shim-1     | Shim-2     | Shim-3     |
        | KV_in,Q_in | KV_in,Q_in | KV_in,Q_in | KV_in,Q_in |
        | O_out      | O_out      | O_out      | O_out      |
        +------------+------------+------------+------------+

ObjectFIFO connections per column:
  DDR --[Q_fifo]-----> Score tile   (depth=1, Q vectors for KV group)
  DDR --[K_fifo]-----> Score tile   (depth=2, K chunks streamed)
  Score --[inter_fifo]--> Value     (depth=2, on-chip: F_c, C_c, l packed)
  DDR --[V_fifo]-----> Value tile   (depth=2, V chunks streamed)
  Value --[O_fifo]---> DDR          (depth=2, attention output drained)

Inter-tile FIFO payload per chunk (group_size=4, chunk_size=32):
  F_c: 32 * 4 = 128 bf16 values (exponentiated scores)
  C_c: 4 bf16 values (correction factors)
  l:   4 bf16 values (running denominators)
  Total: 136 bf16 = 272 bytes per chunk transfer
```

### 2c. swiglu_fused_decode -- 4 Columns, 2 Tiles Per Column (8 tiles total)

Two-stage pipeline. Stage 1 performs dual-GEMV (Wgate and Wup interleaved)
plus SiLU activation and elementwise multiply. Stage 2 performs the down
projection GEMV. The 8192-element intermediate vector stays on-chip via
inter-tile ObjectFIFOs.

```
         Col 0        Col 1        Col 2        Col 3
Row 5   +------------+------------+------------+------------+
        |            |            |            |            |
Row 4   +------------+------------+------------+------------+
        |            |            |            |            |
Row 3   +--[Stage1-0]+--[Stage1-1]+--[Stage1-2]+--[Stage1-3]+
        |DualGEMV    |DualGEMV    |DualGEMV    |DualGEMV    |
        |SiLU * Mul  |SiLU * Mul  |SiLU * Mul  |SiLU * Mul  |
        |Wgate+Wup   |Wgate+Wup   |Wgate+Wup   |Wgate+Wup   |
        |rows 0..2047|rows 2048.. |rows 4096.. |rows 6144.. |
        +-----+------+-----+------+-----+------+-----+------+
              | inter       | inter       | inter       | inter
              | FIFO        | FIFO        | FIFO        | FIFO
              | 2048 elems  | 2048 elems  | 2048 elems  | 2048 elems
              | (on-chip)   | (on-chip)   | (on-chip)   | (on-chip)
        +-----v------+-----v------+-----v------+-----v------+
Row 2   +--[Stage2-0]+--[Stage2-1]+--[Stage2-2]+--[Stage2-3]+
        |DownProj    |DownProj    |DownProj    |DownProj    |
        |GEMV        |GEMV        |GEMV        |GEMV        |
        |Wdown[:,    |Wdown[:,    |Wdown[:,    |Wdown[:,    |
        | 0:2048]    | 2048:4096] | 4096:6144] | 6144:8192] |
        +------+-----+------+-----+------+-----+------+-----+
               |            |            |            |
          DDR  v  DDR       v  DDR       v  DDR       v
        +------+-----+------+-----+------+-----+------+-----+
Shim    | Shim-0     | Shim-1     | Shim-2     | Shim-3     |
        | Wgate+up   | Wgate+up   | Wgate+up   | Wgate+up   |
        | x_in,Wdown | x_in,Wdown | x_in,Wdown | x_in,Wdown |
        | partial_out| partial_out| partial_out| partial_out |
        +------------+------------+------------+------------+

ObjectFIFO connections per column:
  DDR --[A1_fifo]----> Stage 1     (depth=2, interleaved Wgate/Wup rows)
  DDR --[B_fifo]-----> Stage 1     (depth=1, x vector broadcast)
  Stage1 --[inter_fifo]--> Stage2  (depth=2, on-chip: silu(gate)*up chunk)
  DDR --[A2_fifo]----> Stage 2     (depth=2, Wdown column-slice rows)
  Stage2 --[C_fifo]--> DDR         (depth=2, partial output drained)

Host post-processing: sum 4 partial output vectors (each 2048 elements)
  output = partial[0] + partial[1] + partial[2] + partial[3]
```

### 2d. fused_dequant_gemv -- 4 Columns, 1 Tile Per Column

Single-tile GEMV with fused INT4 dequantization. Loads packed INT4 weights
(2 weights per byte) plus per-group bf16 scale factors, dequantizes
in-register, and performs MAC in one pass. Achieves 4x DDR bandwidth
reduction vs. bf16 weight streaming.

```
         Col 0        Col 1        Col 2        Col 3
Row 5   +------------+------------+------------+------------+
        |            |            |            |            |
Row 4   +------------+------------+------------+------------+
        |            |            |            |            |
Row 3   +------------+------------+------------+------------+
        |            |            |            |            |
Row 2   +--[DQ-GV-0]-+--[DQ-GV-1]-+--[DQ-GV-2]-+--[DQ-GV-3]-+
        | INT4 unpack| INT4 unpack| INT4 unpack| INT4 unpack|
        | dequant    | dequant    | dequant    | dequant    |
        | bf16 MAC   | bf16 MAC   | bf16 MAC   | bf16 MAC   |
        +------+-----+------+-----+------+-----+------+-----+
               |            |            |            |
          DDR  v  DDR       v  DDR       v  DDR       v
        +------+-----+------+-----+------+-----+------+-----+
Shim    | Shim-0     | Shim-1     | Shim-2     | Shim-3     |
        | packed_W   | packed_W   | packed_W   | packed_W   |
        | vec_in     | vec_in     | vec_in     | vec_in     |
        | result_out | result_out | result_out | result_out |
        +------------+------------+------------+------------+

ObjectFIFO connections per column:
  DDR --[A_fifo]-----> DQ-GV tile  (depth=2, packed INT4 weight tiles)
  DDR --[B_fifo]-----> DQ-GV tile  (depth=1, x vector broadcast)
  DQ-GV --[C_fifo]--> DDR          (depth=2, output rows drained)

Packed weight tile layout (m_input rows, K columns, group_size=32):
  +------------------------------------------+
  | m_input * K / 2 bytes:  packed INT4 data |
  | m_input * (K/32) * 2 bytes: bf16 scales  |
  +------------------------------------------+
```

---

## 3. Full-Layer Decode Dataflow (Phase 4 Vision)

The ultimate goal is to compose all operators into a single NPU design that
processes one complete transformer layer per invocation. Activations enter
from DDR once (4 KB) and exit once (4 KB). All intermediates stay on-chip.

### 3a. Full NPU2 Tile Allocation (32 tiles)

```
NPU2 Full-Layer Decode Tile Map
=================================================================================================

              Col 0      Col 1      Col 2      Col 3      Col 4      Col 5      Col 6      Col 7
            +----------+----------+----------+----------+----------+----------+----------+----------+
            |          |          |          |          |          |          |          |          |
Row 5       | Proj     | Proj     | Proj     | Proj     | Proj     | Proj     | Proj     | Proj     |
(Row 4 of   | GEMV-0   | GEMV-1   | GEMV-2   | GEMV-3   | GEMV-4   | GEMV-5   | GEMV-6   | GEMV-7   |
 compute)   | QKV/MLP  | QKV/MLP  | QKV/MLP  | QKV/MLP  | QKV/MLP  | QKV/MLP  | QKV/MLP  | QKV/MLP  |
            | time-mux | time-mux | time-mux | time-mux | time-mux | time-mux | time-mux | time-mux |
            +----------+----------+----------+----------+----------+----------+----------+----------+
            |          |          |          |          |          |          |          |          |
Row 4       | Attn     | Attn     | Attn     | Attn     | MLP      | MLP      | MLP      | MLP      |
(Row 3 of   | Score-0  | Score-1  | Score-2  | Score-3  | DualGV-4 | DualGV-5 | DualGV-6 | DualGV-7 |
 compute)   | Q*K^T    | Q*K^T    | Q*K^T    | Q*K^T    | SiLU*Mul | SiLU*Mul | SiLU*Mul | SiLU*Mul |
            | softmax  | softmax  | softmax  | softmax  | Wgate+up | Wgate+up | Wgate+up | Wgate+up |
            +----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+
            |    |     |    |     |    |     |    |     |    |     |    |     |    |     |    |     |
            |    |inter|    |inter|    |inter|    |inter|    |inter|    |inter|    |inter|    |inter|
            |    v     |    v     |    v     |    v     |    v     |    v     |    v     |    v     |
            +----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+----+-----+
Row 3       | Attn     | Attn     | Attn     | Attn     | MLP      | MLP      | MLP      | MLP      |
(Row 2 of   | Value-0  | Value-1  | Value-2  | Value-3  | DownPr-4 | DownPr-5 | DownPr-6 | DownPr-7 |
 compute)   | F_c*V    | F_c*V    | F_c*V    | F_c*V    | Wdown    | Wdown    | Wdown    | Wdown    |
            | accum    | accum    | accum    | accum    | partial  | partial  | partial  | partial  |
            +----------+----------+----------+----------+----------+----------+----------+----------+
            |          |          |          |          |          |          |          |          |
Row 2       | Norm+    | Norm+    | OutProj  | OutProj  | OutProj  | OutProj  | Residual | Residual |
(Row 1 of   | RoPE     | Add      | GEMV-0   | GEMV-1   | GEMV-2   | GEMV-3   | +Norm    | +Add     |
 compute)   |          |          |          |          |          |          |          |          |
            +----------+----------+----------+----------+----------+----------+----------+----------+
            |          |          |          |          |          |          |          |          |
MemTile     | MT-0     | MT-1     | MT-2     | MT-3     | MT-4     | MT-5     | MT-6     | MT-7     |
            | Residual | Weight   | Weight   | Weight   | Weight   | Weight   | Weight   | Residual |
            | stash    | staging  | staging  | staging  | staging  | staging  | staging  | stash    |
            +----------+----------+----------+----------+----------+----------+----------+----------+
            |          |          |          |          |          |          |          |          |
Shim        | Shim-0   | Shim-1   | Shim-2   | Shim-3   | Shim-4   | Shim-5   | Shim-6   | Shim-7   |
            | DDR I/O  | DDR I/O  | DDR I/O  | DDR I/O  | DDR I/O  | DDR I/O  | DDR I/O  | DDR I/O  |
            +----------+----------+----------+----------+----------+----------+----------+----------+
                                               DDR (LPDDR5)

Tile allocation summary:
  Row 5 (8 tiles):      Projection GEMV engine -- QKV proj + gate/up proj (time-multiplexed)
  Row 4 cols 0-3:       FlowKV attention score tiles (4 KV head groups)
  Row 3 cols 0-3:       FlowKV attention value tiles (4 KV head groups)
  Row 4 cols 4-7:       SwiGLU dual-GEMV + SiLU*Mul tiles
  Row 3 cols 4-7:       SwiGLU down-projection tiles
  Row 2 cols 0-1:       RMSNorm, RoPE, residual add (utility)
  Row 2 cols 2-5:       Output projection GEMV (4 columns)
  Row 2 cols 6-7:       Residual add + post-attention norm (utility)
  MemTiles 0,7:         Residual activation stash (4 KB each)
  MemTiles 1-6:         Weight staging / FIFO depth extension
```

### 3b. Full-Layer Temporal Execution Phases

The 32 tiles process one layer in 4 temporal phases, reusing tiles across
roles. Activations flow between phases via on-chip ObjectFIFOs.

```
Time ------>

Phase A: Input Normalization + QKV Projection
+-------------------------------------------------------------------+
| Row 5 (all 8 cols): Stream Wq/Wk/Wv, column-parallel GEMV        |
| Row 2 col 0:        RMSNorm produces normalized x --> Row 5       |
| MemTile 0:          Stash original x for residual add later       |
+-------------------------------------------------------------------+
     |
     | Q, K, V vectors flow on-chip
     v
Phase B: Attention + Output Projection
+-------------------------------------------------------------------+
| Rows 3-4 cols 0-3:  FlowKV attention (score + value tiles)       |
|                      KV cache streamed from DDR                   |
| Row 2 cols 2-5:     Output projection GEMV (Wo weight streaming)  |
+-------------------------------------------------------------------+
     |
     | Attention output flows on-chip
     v
Phase C: Post-Attention Norm + SwiGLU MLP
+-------------------------------------------------------------------+
| Row 2 cols 6-7:     Residual add (from MemTile) + RMSNorm        |
| Row 5 (all 8 cols): Stream Wgate/Wup, compute gate+up projection |
| Rows 3-4 cols 4-7:  Down projection (consumes intermediate)      |
+-------------------------------------------------------------------+
     |
     | MLP output flows on-chip
     v
Phase D: Final Residual Add + Output
+-------------------------------------------------------------------+
| Row 2 col 1:        Add MLP output to post-attention residual     |
| Output:             Final token (4 KB) written to DDR             |
+-------------------------------------------------------------------+

Data flow (DDR touches marked with *):
  *Token in (4 KB)* --> RMSNorm --> QKV Proj --> RoPE --> FlowKV Attn
       ^                                                     |
       |                                              *KV cache stream*
       |                                                     |
       |                    Output Proj <-------- attn output
       |                         |
       |                    Residual Add <-- *stashed x from MemTile*
       |                         |
       |                    RMSNorm
       |                         |
       |                    Gate+Up Proj --> SiLU*Mul --> Down Proj
       |                         ^                          |
       |                   *Wgate,Wup,Wdown stream*         |
       |                                                    |
       +--- Residual Add <---------------------------------+
                  |
             *Token out (4 KB)*
```

---

## 4. DMA Channel Budget Tables

Each compute tile has 2 input (S2MM) + 2 output (MM2S) DMA channels.
Each shim tile has 2 input (S2MM) + 2 output (MM2S) DMA channels.

### 4a. fused_qkv_proj (per compute tile)

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | DDR --> tile | `of_weights` | Wqkv rows (768 x 2048 bf16) | 2 |
| S2MM-1 | DDR --> tile | `of_input` | x vector (2048 bf16) | 1 |
| MM2S-0 | tile --> DDR | `of_output` | Output rows (768 bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Budget: 2 in + 1 out = 3 of 4 channels used per tile**

### 4b. flowkv_decode (per column, 2 tiles)

**Score tile:**

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | DDR --> tile | `Q_fifo` | Q vectors (4 heads x 64 = 256 bf16) | 1 |
| S2MM-1 | DDR --> tile | `K_fifo` | K chunk (32 x 64 = 2048 bf16) | 2 |
| MM2S-0 | tile --> tile | `inter_fifo` | Packed [F_c, C_c, l] (136 bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Value tile:**

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | tile --> tile | `inter_fifo` | Packed [F_c, C_c, l] (136 bf16) | 2 |
| S2MM-1 | DDR --> tile | `V_fifo` | V chunk (32 x 64 = 2048 bf16) | 2 |
| MM2S-0 | tile --> DDR | `O_fifo` | Output (4 x 64 = 256 bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Budget: Score = 2 in + 1 out = 3/4; Value = 2 in + 1 out = 3/4**

### 4c. swiglu_fused_decode (per column, 2 tiles)

**Stage 1 tile (dual-GEMV + SiLU*Mul):**

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | DDR --> tile | `A1_fifo` | Interleaved Wgate/Wup rows | 2 |
| S2MM-1 | DDR --> tile | `B_fifo` | x vector (2048 bf16) | 1 |
| MM2S-0 | tile --> tile | `inter_fifo` | Intermediate chunk (2048 bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Stage 2 tile (down-projection GEMV):**

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | DDR --> tile | `A2_fifo` | Wdown column-slice rows | 2 |
| S2MM-1 | tile --> tile | `inter_fifo` | Intermediate chunk (2048 bf16) | 2 |
| MM2S-0 | tile --> DDR | `C_fifo` | Partial output (2048 bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Budget: Stage 1 = 2 in + 1 out = 3/4; Stage 2 = 2 in + 1 out = 3/4**

### 4d. fused_dequant_gemv (per compute tile)

| Channel | Direction | ObjectFIFO | Data | Depth |
|---------|-----------|------------|------|-------|
| S2MM-0 | DDR --> tile | `A_fifo` | Packed INT4 weight tiles | 2 |
| S2MM-1 | DDR --> tile | `B_fifo` | x vector (K bf16) | 1 |
| MM2S-0 | tile --> DDR | `C_fifo` | Output rows (M/cols bf16) | 2 |
| MM2S-1 | -- | unused | -- | -- |

**Budget: 2 in + 1 out = 3 of 4 channels used per tile**

### 4e. Full-Layer Shim DMA Budget (per phase)

| Phase | Input Channels (S2MM) | Output Channels (MM2S) | Fit? |
|-------|----------------------|----------------------|------|
| A: QKV Proj | 8 (weights, 1/col) + 1 (x broadcast) = 9 | 8 (QKV output, 1/col) | 9+8 <= 16+16 |
| B: Attention | 8 (K/V cache, 2/KV group) + 4 (Q) = 12 | 4 (attn output) | 12+4 <= 16+16 |
| C: MLP | 8 (weights) + 1 (x broadcast) = 9 | 8 (partial outputs) | 9+8 <= 16+16 |

**All phases fit within the 16 S2MM + 16 MM2S shim channel budget.**

---

## 5. L1 Memory Budget Tables

Each compute tile has **64 KB** of L1 data memory. ObjectFIFO buffers, stack,
and static kernel data all share this space.

### 5a. fused_qkv_proj (Llama 3.2 1B: M=3072, K=2048)

| Buffer | Size | Notes |
|--------|------|-------|
| of_weights (depth=2) | 2 x m_input x 2048 x 2B = 2 x 4 x 4096B = 32 KB | m_input=4 |
| of_input (depth=1) | 1 x 2048 x 2B = 4 KB | x vector |
| of_output (depth=2) | 2 x m_output x 2B | Depends on m_output |
| Stack + kernel code | ~2 KB | Estimate |
| **Worst case (m_output=768)** | 32 + 4 + 3 + 2 = **~41 KB** | Fits in 64 KB |

### 5b. flowkv_decode -- Score Tile (head_dim=64, chunk=32, group=4)

| Buffer | Size | Notes |
|--------|------|-------|
| Q_fifo (depth=1) | 1 x 4 x 64 x 2B = 512 B | 4 query heads |
| K_fifo (depth=2) | 2 x 32 x 64 x 2B = 8 KB | K chunk double-buffered |
| inter_fifo (depth=2) | 2 x 136 x 2B = 544 B | Packed [F_c, C_c, l] |
| Static: scores | 4 x 32 x 4B = 512 B | float32 accumulators |
| Static: softmax state | 4 x 3 x 4B = 48 B | m, l, correction per head |
| Stack + kernel code | ~2 KB | Estimate |
| **Total** | ~12 KB | **Fits easily in 64 KB** |

### 5b'. flowkv_decode -- Value Tile

| Buffer | Size | Notes |
|--------|------|-------|
| inter_fifo (depth=2) | 2 x 136 x 2B = 544 B | Packed [F_c, C_c, l] |
| V_fifo (depth=2) | 2 x 32 x 64 x 2B = 8 KB | V chunk double-buffered |
| O_fifo (depth=2) | 2 x 4 x 64 x 2B = 1 KB | Output double-buffered |
| Static: Y accumulator | 4 x 64 x 4B = 1 KB | float32 accumulation |
| Static: denominator | 4 x 4B = 16 B | l values |
| Stack + kernel code | ~2 KB | Estimate |
| **Total** | ~13 KB | **Fits easily in 64 KB** |

### 5c. swiglu_fused_decode -- Stage 1 (d_model=2048, d_ffn=8192)

| Buffer | Size | Notes |
|--------|------|-------|
| A1_fifo (depth=2) | 2 x m_in x 2048 x 2B = 2 x 4 x 4096B = 32 KB | m_input=4 |
| B_fifo (depth=1) | 1 x 2048 x 2B = 4 KB | x vector |
| inter_fifo (depth=2) | 2 x 2048 x 2B = 8 KB | Intermediate chunk output |
| Static: left_buf | 2048 x 2B = 4 KB | Gate GEMV accumulator |
| Static: right_buf | 2048 x 2B = 4 KB | Up GEMV accumulator |
| Stack + kernel code | ~2 KB | Estimate |
| **Total** | ~54 KB | **Fits in 64 KB (10 KB margin)** |

### 5c'. swiglu_fused_decode -- Stage 2

| Buffer | Size | Notes |
|--------|------|-------|
| A2_fifo (depth=2) | 2 x 1 x 2048 x 2B = 8 KB | m_input_stage2=1 |
| inter_fifo (depth=2) | 2 x 2048 x 2B = 8 KB | Intermediate from Stage 1 |
| C_fifo (depth=2) | 2 x 2048 x 2B = 8 KB | Output partial |
| Stack + kernel code | ~2 KB | Estimate |
| **Total** | ~26 KB | **Fits easily in 64 KB** |

### 5d. fused_dequant_gemv (M=3072, K=2048, group_size=32)

| Buffer | Size | Notes |
|--------|------|-------|
| A_fifo (depth=2) | 2 x packed_tile_bytes | Depends on m_input |
| | m_input=1: 2 x (1024 + 128) = 2304 B | INT4 weights + scales |
| B_fifo (depth=1) | 1 x 2048 x 2B = 4 KB | x vector |
| C_fifo (depth=2) | 2 x m_output x 2B | Depends on m_output |
| Stack + kernel code | ~2 KB | Estimate |
| **Typical (m_input=1, m_output=768)** | 2.3 + 4 + 3 + 2 = **~11 KB** | **Fits easily** |

### 5e. L1 Budget Summary

| Operator | Tightest Tile | L1 Used | Margin |
|----------|--------------|---------|--------|
| fused_qkv_proj | GEMV tile | ~41 KB | 23 KB |
| flowkv_decode | Value tile | ~13 KB | 51 KB |
| swiglu_fused_decode | Stage 1 tile | ~54 KB | **10 KB** |
| fused_dequant_gemv | DQ-GV tile | ~11 KB | 53 KB |

The tightest L1 budget is the SwiGLU Stage 1 tile at ~54 KB. This is the
tile that must hold the full x vector (4 KB), double-buffered weight rows
(32 KB), double-buffered intermediate output (8 KB), and two static
accumulator buffers (8 KB). The 10 KB margin is sufficient but does not
allow increasing m_input beyond 4 without exceeding 64 KB.

---

## 6. DDR Bandwidth Savings Analysis

### 6a. Per-Layer DDR Traffic Comparison (Llama 3.2 1B, bf16)

```
                        Current (10 ops)          Fused Operators          Savings
                        ================          ===============          =======
Weights streamed:

  Q projection          8 MB                      |                       |
  K projection          2 MB                      | 10 MB (single GEMV)   | 0 MB (same weight data)
  V projection          2 MB                      |                       |
  -------               -----                     ---------               -----
  QKV subtotal          12 MB                     10 MB                   2 MB (input vector savings)

  Output projection     8 MB                      8 MB                    0 MB

  Gate projection       32 MB                     |                       |
  Up projection         32 MB                     | 96 MB (single design) | 0 MB (same weight data)
  Down projection       32 MB                     |                       |
  -------               -----                     ---------               -----
  MLP subtotal          96 MB                     96 MB                   0 MB (weight traffic same)

Activation DDR I/O (the real win):

  Operator              Current DDR Act. Traffic  Fused DDR Act. Traffic
  -------               -----------------------   ----------------------
  RMSNorm (input)       4 KB read + 4 KB write    0 (on-chip)
  Q proj                4 KB read + 4 KB write    |
  K proj                4 KB read + 1 KB write    | Single x read (4 KB)
  V proj                4 KB read + 1 KB write    | QKV output to DDR (6 KB)
  RoPE                  5 KB read + 5 KB write    0 (fused into FlowKV)
  GQA attention         ~10 KB read + 4 KB write  0 (Q on-chip, output on-chip)
  Output proj           4 KB read + 4 KB write    On-chip input, output to DDR
  Residual add          8 KB read + 4 KB write    On-chip (MemTile stash)
  RMSNorm (post-attn)   4 KB read + 4 KB write    0 (on-chip)
  Gate proj             4 KB read + 16 KB write   |
  Up proj               4 KB read + 16 KB write   | Single x read (4 KB)
  SiLU*Mul              32 KB read + 16 KB write  | Intermediate on-chip (0 KB)
  Down proj             16 KB read + 4 KB write   | Partials to DDR (16 KB)
  Residual add          8 KB read + 4 KB write    On-chip
  -------               ---------                 ----------
  Act. subtotal         ~152 KB                   ~30 KB

Kernel launch overhead:

  Current:              12+ launches x ~75 us     = ~900 us per layer
  Fused (Phase 4):      1 launch x ~75 us         = ~75 us per layer
  -------               ---------                 ---------
  Overhead savings:     ~825 us per layer x 16 layers = ~13 ms per token
```

### 6b. INT4 Quantization Impact (fused_dequant_gemv)

| Weight Matrix | bf16 Size | INT4 Size | Reduction |
|---------------|-----------|-----------|-----------|
| Wq (2048x2048) | 8 MB | 2 MB + 32 KB scales | 3.9x |
| Wk (512x2048) | 2 MB | 0.5 MB + 8 KB | 3.9x |
| Wv (512x2048) | 2 MB | 0.5 MB + 8 KB | 3.9x |
| Wo (2048x2048) | 8 MB | 2 MB + 32 KB | 3.9x |
| Wgate (8192x2048) | 32 MB | 8 MB + 128 KB | 3.9x |
| Wup (8192x2048) | 32 MB | 8 MB + 128 KB | 3.9x |
| Wdown (2048x8192) | 32 MB | 8 MB + 128 KB | 3.9x |
| **Layer total** | **116 MB** | **~29.5 MB** | **3.9x** |
| **16-layer total** | **1,856 MB** | **~472 MB** | **3.9x** |

### 6c. End-to-End Token Latency Projection

```
Configuration                  Weight DDR    Act. DDR    Overhead    Total/tok   Tok/s
                               (16 layers)   (16 layers) (16 layers) (@ 50 GB/s)
------------------------------ ----------    ---------   ---------   ----------  -----
Current (12 ops, bf16)         1,856 MB      ~2.4 MB     ~14 ms      ~51 ms      ~20
Phase 1-3 fused (bf16)         1,856 MB      ~0.5 MB     ~2 ms       ~39 ms      ~26
Phase 1-4 full layer (bf16)    1,856 MB      ~0.1 MB     ~1.2 ms     ~38 ms      ~26
Phase 5 + INT4 (full fusion)   472 MB        ~0.1 MB     ~1.2 ms     ~11 ms      ~91

Configuration                  @ 80 GB/s
------------------------------ ----------
Current (12 ops, bf16)         ~37 ms        ~27 tok/s
Phase 1-3 fused (bf16)         ~25 ms        ~40 tok/s
Phase 1-4 full layer (bf16)    ~24 ms        ~42 tok/s
Phase 5 + INT4 (full fusion)   ~7.1 ms       ~140 tok/s
```

The dominant cost is always weight traffic from DDR. INT4 quantization
(`fused_dequant_gemv`) provides the single largest speedup (3.9x). Operator
fusion eliminates activation round-trips and kernel launch overhead, adding
another ~1.5x on top.

---

## 7. Operator Architecture Details

### 7a. fused_qkv_proj

**Directory**: `iron/operators/fused_qkv_proj/`

**What it does**: Concatenates the Q, K, and V weight matrices row-wise into
a single (q_dim + k_dim + v_dim) x embedding_dim matrix. Runs one standard
GEMV to produce the concatenated [Q, K, V] output vector. The host-side
`forward()` method splits the output into separate Q, K, V tensors.

**Key design decisions**:
- Reuses the existing GEMV design (`iron/operators/gemv/design.py`) and the
  existing `mv.o` kernel -- no new AIE kernel needed.
- Weight concatenation is done once at setup time via `concatenate_weights()`.
- For Llama 3.2 1B: M=3072 (2048+512+512), K=2048, 4 columns, 768 rows/col.

**Benefit**: Eliminates 3 redundant 4 KB input vector loads from DDR and
3 kernel launch overheads. Total savings: 12 KB DDR activation traffic +
~150 us launch overhead per layer.

**AIE kernel**: `aie_kernels/generic/mv.cc` (standard GEMV, unmodified)

### 7b. flowkv_decode

**Directory**: `iron/operators/flowkv_decode/`

**What it does**: Implements streaming decode attention with exact
FlashAttention-style online softmax. Uses a 2-tile pipeline per KV head
group:

1. **Score tile**: Receives Q vectors and streams K chunks from the KV
   cache. Computes scaled dot-product attention scores with running max
   tracking. Produces exponentiated scores (F_c), correction factors (C_c),
   and running denominator (l), packed into an inter-tile ObjectFIFO.

2. **Value tile**: Receives the packed intermediates from the score tile
   and streams V chunks from the KV cache. Accumulates weighted V values
   with correction factor application. After all chunks, normalizes by the
   denominator to produce the final attention output.

**Key design decisions**:
- Online softmax enables single-pass streaming over the KV cache (no
  materialization of the full attention matrix).
- K and V are interleaved in DDR (`interleave_kv_cache()`) so a single
  contiguous DMA region serves both tiles per KV head.
- With 8 KV heads and 4 columns, the runtime sequence processes 2 batches
  of 4 KV head groups sequentially.
- Intermediates (F_c, C_c, l) are 136 bf16 values per chunk (272 bytes) --
  transferred tile-to-tile via on-chip ObjectFIFO, never touching DDR.

**AIE kernel**: `aie_kernels/aie2p/flowkv.cc`
- `flowkv_score_init_bf16`: Initialize softmax state (m=-inf, l=0)
- `flowkv_score_chunk_bf16`: Process one K chunk, update softmax state
- `flowkv_value_init_bf16`: Initialize Y accumulator to zero
- `flowkv_value_accum_bf16`: Accumulate weighted V chunk with correction
- `flowkv_value_normalize_bf16`: Final O = Y / l normalization

### 7c. swiglu_fused_decode

**Directory**: `iron/operators/swiglu_fused_decode/`

**What it does**: Fuses the entire SwiGLU MLP computation into a single NPU
design: `output = Wdown @ (silu(Wgate @ x) * (Wup @ x))`. Uses a 2-stage
tile pipeline where the 8192-element intermediate vector stays on-chip.

1. **Stage 1 (per column)**: Dual-GEMV with SiLU activation and elementwise
   multiply. Streams interleaved Wgate/Wup weight rows from DDR, computes
   `silu(Wgate_partial @ x) * (Wup_partial @ x)`, and outputs the
   intermediate chunk (2048 bf16 per column) via an inter-tile ObjectFIFO.

2. **Stage 2 (per column)**: Down-projection GEMV. Reads the intermediate
   chunk from Stage 1 on-chip and streams Wdown column-slice rows from DDR.
   Produces a partial output vector (2048 bf16 elements = the full output
   dimension, but only a partial dot product per row).

The host sums the 4 partial output vectors to get the final result.

**Key design decisions**:
- Wgate and Wup weights are pre-interleaved in DDR per column:
  `[Wgate_col0_rows, Wup_col0_rows, Wgate_col1_rows, ...]`
- The SiLU+Mul is computed from two static buffers (left_buf, right_buf)
  that accumulate the gate and up GEMV results respectively.
- The inter-tile ObjectFIFO depth=2 allows Stage 1 to produce the next
  chunk while Stage 2 consumes the current one.
- Stage 1 is the L1-tightest tile in the entire decode pipeline (~54 KB
  of 64 KB used).

**AIE kernel**: `aie_kernels/aie2p/swiglu_fused.cc`
- `swiglu_fused_dual_gemv_bf16`: GEMV to static buffer with phase select
- `swiglu_fused_silu_mul_bf16`: SiLU(left) * right to FIFO output
- `swiglu_fused_down_gemv_bf16`: Standard GEMV for down projection

### 7d. fused_dequant_gemv

**Directory**: `iron/operators/fused_dequant_gemv/`

**What it does**: Performs matrix-vector multiplication with fused INT4
weight dequantization. Loads packed INT4 weights and per-group bf16 scale
factors from DDR, dequantizes in-register, and performs the MAC in a single
streaming pass. Achieves 3.9x DDR bandwidth reduction compared to bf16.

**Key design decisions**:
- INT4 weights are packed 2-per-byte in DDR. The kernel unpacks via
  shift+mask operations.
- Scale factors are stored per quantization group (default group_size=32).
  Each group of 32 weights shares one bf16 scale factor.
- The packed weight tile layout places INT4 data first, followed by scale
  factors, so the kernel can locate scales at a known offset within each
  FIFO buffer.
- The operator is a drop-in replacement for standard bf16 GEMV in any
  projection stage of the decode pipeline.

**Weight packing**: The reference module provides `quantize_and_pack()`
which converts a bf16 weight matrix to the packed DDR layout. Tiles are
organized per-column: all tiles for column 0 first, then column 1, etc.

**Packed tile structure** (for m_input rows, K columns, group_size G):
```
  Offset 0:                   m_input * K / 2 bytes   (packed INT4 weights)
  Offset m_input * K / 2:     m_input * (K/G) * 2 bytes (bf16 scale factors)
```

**AIE kernel**: `aie_kernels/aie2p/fused_dequant_gemv.cc`
- `fused_dequant_matvec_bf16`: Fused unpack + dequant + MAC kernel

---

## Summary

These four operators form the building blocks of a high-performance decode
pipeline that minimizes DDR bandwidth waste:

| Operator | Eliminates | Standalone Tiles | Key Innovation |
|----------|-----------|-----------------|----------------|
| fused_qkv_proj | 3 redundant x-vector loads | 4 (1/col) | Weight concatenation, reuses GEMV |
| flowkv_decode | Q/K/V DDR writes + attn matrix DDR | 8 (2/col) | Online softmax, inter-tile pipeline |
| swiglu_fused_decode | 16 KB intermediate DDR round-trip | 8 (2/col) | Dual-GEMV + down-proj pipeline |
| fused_dequant_gemv | 75% of weight DDR traffic | 4 (1/col) | In-register INT4 dequant + MAC |

When composed into the Phase 4 full-layer design, these operators will
process an entire transformer layer with only 8 KB of activation DDR
traffic (4 KB in + 4 KB out), down from ~152 KB in the current implementation.
Combined with INT4 quantization, the target is ~91-140 tokens/second on
XDNA2 hardware.

---

## 8. Hardware Benchmark Results

Measured on AMD Ryzen AI 9 HX 370 (RyzenAI-npu4), XRT 2.21.75, 20 timed
iterations after 5 warmup runs.

### SwiGLU MLP: swiglu_fused_decode vs. swiglu_decode (baseline)

#### Small dimensions (2048x2048)

```
                      Baseline (2 runlists)     Fused (1 runlist)     Improvement
                      =======================   ===================   ===========
Median latency        2072 us                   1101 us               1.88x
Effective bandwidth   12.15 GB/s                22.88 GB/s            1.88x
DDR intermediate      8 KB round-trip           0 KB (on-chip)        Eliminated
```

#### Llama 3.2 1B production dimensions (embedding=2048, hidden=8192)

```
                      Baseline (2 runlists)     Fused (1 runlist)     Improvement
                      =======================   ===================   ===========
Median latency        5410 us                   4103 us               1.32x
Min latency           4882 us                   3974 us               1.23x
Effective bandwidth   18.61 GB/s                24.54 GB/s            1.32x
DDR intermediate      32 KB round-trip          0 KB (on-chip)        Eliminated
Weight traffic        100.7 MB                  100.7 MB              (same)
16-layer MLP time     86.6 ms                   65.7 ms               20.9 ms saved
MLP-only tok/s        11.6                      15.2                  +31%
```

### Key Takeaways

- **1.32x speedup** at Llama production dims from eliminating the 32 KB DDR
  intermediate round-trip and one kernel launch overhead
- **24.5 GB/s effective bandwidth** -- approaching DDR theoretical limits
- **31% improvement in MLP tok/s** (11.6 -> 15.2) for the SwiGLU portion of
  each transformer layer
- DDR partial-sum reduction (host `sum()`) outperforms on-chip MemTile
  reduction at this scale: the extra reduction tile adds ~400 us of pipeline
  serialization that costs more than the 12 KB DDR write it saves (~0.5 us)
- The speedup is larger at smaller dims (1.88x) because kernel launch overhead
  is a bigger fraction; at production dims the weight streaming dominates
