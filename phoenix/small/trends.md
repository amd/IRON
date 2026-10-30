# Performance trends

**Operators added:** `SelectiveScan`, `pre_push_hook`

**Operators dropped:** `visualize`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 16.72 | 15.37 | 🔴 -8.02% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3010.99 | 3273.65 | 🔴 +8.72% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1131.82 | 309.92 | 🟢 -72.62% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.57 | 5.12 | 🔴 -8.02% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 24.74 | 10.54 | 🔴 -57.40% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 1356.22 | 3183.81 | 🔴 +134.76% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 322.26 | 373.54 | 🔴 +15.91% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 6.19 | 2.63 | 🔴 -57.40% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 147.66 | 120.35 | 🟢 -18.50% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.27 | 13.50 | 🔴 -58.17% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1559.66 | 3728.26 | 🔴 +139.04% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 10.39 | 660.44 | 🔴 +6256.82% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.38 | 2.25 | 🔴 -58.17% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 18.65 | 15.47 | 🔴 -17.05% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2698.80 | 3253.49 | 🔴 +20.55% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1190.66 | 560.24 | 🟢 -52.95% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 3.11 | 2.58 | 🔴 -17.05% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.13 | 0.09 | 🔴 -26.05% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 15.80 | 21.37 | 🔴 +35.22% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 3.07 | 10.68 | 🔴 +247.55% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 18.07 | 10.54 | 🔴 -41.68% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1857.16 | 3184.60 | 🔴 +71.48% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.58 | 274.26 | 🔴 +3098.00% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.52 | 2.63 | 🔴 -41.68% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 248.04 | 479.06 | 🔴 +93.14% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 16.10 | 10.89 | 🔴 -32.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 2084.64 | 3080.89 | 🔴 +47.79% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 936.92 | 430.63 | 🟢 -54.04% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 24.14 | 16.34 | 🔴 -32.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.16 | 13.95 | 🟢 +24.98% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3007.15 | 2406.01 | 🟢 -19.99% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 202.86 | 1203.26 | 🔴 +493.16% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.74 | 20.92 | 🟢 +24.98% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 131.20 | 38.42 | 🟢 -70.72% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 3.53 | 2.47 | 🟢 -29.85% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 11.66 | 11.02 | 🟢 -5.51% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 11.72 | 28.17 | 🟢 +140.25% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 2862.69 | 1191.55 | 🟢 -58.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 828.02 | 10.08 | 🟢 -98.78% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 11.72 | 28.16 | 🟢 +140.25% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.52 | 29.59 | 🟢 +181.28% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3189.93 | 1134.06 | 🟢 -64.45% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 299.98 | 14.58 | 🟢 -95.14% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.52 | 29.59 | 🟢 +181.28% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 385.35 | 771.80 | 🔴 +100.28% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 179.90 | 357.27 | 🔴 +98.59% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 90.97 | 48.08 | 🟢 -47.15% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 38.49 | 12.78 | 🟢 -66.79% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 17.17 | 23.00 | 🟢 +33.98% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1954.89 | 1459.07 | 🟢 -25.36% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 880.47 | 429.91 | 🟢 -51.17% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 4.29 | 5.75 | 🟢 +33.98% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 16.04 | 9.93 | 🔴 -38.09% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 2092.42 | 3379.64 | 🔴 +61.52% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 997.75 | 185.37 | 🟢 -81.42% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 4.01 | 2.48 | 🔴 -38.09% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 494.60 | 380.12 | 🟢 -23.15% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 28.80 | 15.39 | 🔴 -46.58% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1164.92 | 2180.72 | 🔴 +87.20% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 74.10 | 1100.79 | 🔴 +1385.57% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.20 | 3.85 | 🔴 -46.58% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.50 | 2.70 | 🔴 -58.45% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1291.50 | 3108.11 | 🔴 +140.66% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 5.66 | 73.81 | 🔴 +1204.13% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.62 | 0.67 | 🔴 -58.45% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 13.37 | 29.34 | 🟢 +119.46% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2510.26 | 1143.82 | 🟢 -54.43% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 948.68 | 14.32 | 🟢 -98.49% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 3.34 | 7.33 | 🟢 +119.46% |

