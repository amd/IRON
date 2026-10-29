# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 14.57 | 15.83 | 🟢 +8.62% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3453.37 | 3179.29 | 🟢 -7.94% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 533.66 | 417.23 | 🟢 -21.82% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 4.86 | 5.28 | 🟢 +8.62% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 15.13 | 29.34 | 🟢 +93.90% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 2217.86 | 1143.83 | 🟢 -48.43% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1172.19 | 36.61 | 🟢 -96.88% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 3.78 | 7.33 | 🟢 +93.90% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.78 | 15.82 | 🟢 +173.48% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 2900.95 | 1060.75 | 🟢 -63.43% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 223.45 | 1.58 | 🟢 -99.29% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 14.21 | 56.06 | 🔴 +294.47% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.43 | 32.16 | 🟢 +108.42% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3262.36 | 1565.28 | 🟢 -52.02% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 307.90 | 12.20 | 🟢 -96.04% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.57 | 5.36 | 🟢 +108.42% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.10 | 0.12 | 🟢 +17.61% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 19.26 | 16.38 | 🟢 -14.98% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.83 | 6.25 | 🔴 +7.33% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.84 | 11.78 | 🟢 +19.70% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3409.30 | 2848.29 | 🟢 -16.46% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 158.28 | 619.85 | 🔴 +291.61% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.46 | 2.95 | 🟢 +19.70% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 3.08 | 3.25 | 🟢 +5.42% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 8172.84 | 7752.65 | 🟢 -5.14% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 704.10 | 170.82 | 🟢 -75.74% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 2102.07 | 2216.00 | 🟢 +5.42% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 46.65 | 51.48 | 🔴 +10.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.31 | 29.20 | 🟢 +158.27% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2967.56 | 1148.99 | 🟢 -61.28% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 589.49 | 16.91 | 🟢 -97.13% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 16.96 | 43.81 | 🟢 +158.27% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 258.07 | 233.67 | 🟢 -9.45% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 142.35 | 112.84 | 🟢 -20.73% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.22 | 0.20 | 🔴 -5.91% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 75.94 | 80.71 | 🔴 +6.28% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.21 | 6.71 | 🔴 +453.42% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.38 | 0.42 | 🟢 +9.83% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 135.39 | 123.27 | 🟢 -8.95% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 19.00 | 9.60 | 🟢 -49.49% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 9.61 | 25.61 | 🔴 +166.45% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.40 | 33.59 | 🔴 +299.82% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.85 | 29.05 | 🟢 +194.80% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3405.03 | 1155.03 | 🟢 -66.08% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 514.39 | 59.02 | 🟢 -88.53% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.46 | 7.26 | 🟢 +194.80% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 204.02 | 363.04 | 🔴 +77.94% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 29.35 | 184.03 | 🔴 +527.01% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 18.41 | 7.80 | 🟢 -57.63% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.80 | 21.02 | 🟢 +94.59% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3106.71 | 1596.57 | 🟢 -48.61% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 451.18 | 600.48 | 🔴 +33.09% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.70 | 5.25 | 🟢 +94.59% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 14.41 | 13.12 | 🟢 -8.97% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 20.49 | 11.02 | 🟢 -46.23% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 9.57 | 12.49 | 🟢 +30.55% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3507.07 | 2686.34 | 🟢 -23.40% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 149.73 | 685.53 | 🔴 +357.84% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.39 | 3.12 | 🟢 +30.55% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.85 | 29.37 | 🟢 +170.65% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3092.23 | 1142.50 | 🟢 -63.05% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 557.75 | 44.15 | 🟢 -92.08% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.71 | 7.34 | 🟢 +170.65% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 18.05 | 83.89 | 🔴 +364.68% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.33 | 18.82 | 🟢 +82.29% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3249.27 | 1782.50 | 🟢 -45.14% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 475.75 | 731.93 | 🔴 +53.85% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.58 | 4.71 | 🟢 +82.29% |

