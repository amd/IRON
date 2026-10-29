# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 15.83 | 16.72 | 🟢 +5.59% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3179.29 | 3010.99 | 🟢 -5.29% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 417.23 | 1131.82 | 🔴 +171.27% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.28 | 5.57 | 🟢 +5.59% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 29.34 | 24.74 | 🔴 -15.66% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 1143.83 | 1356.22 | 🔴 +18.57% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 36.61 | 322.26 | 🔴 +780.25% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 7.33 | 6.19 | 🔴 -15.66% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.82 | 5.16 | 🔴 -67.38% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1060.75 | 3252.28 | 🔴 +206.60% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 1.58 | 147.66 | 🔴 +9260.57% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 56.06 | 10.39 | 🟢 -81.47% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.16 | 18.65 | 🔴 -42.00% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1565.28 | 2698.80 | 🔴 +72.42% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 12.20 | 1190.66 | 🔴 +9661.15% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.36 | 3.11 | 🔴 -42.00% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 6.25 | 3.07 | 🟢 -50.88% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.78 | 18.07 | 🟢 +53.37% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2848.29 | 1857.16 | 🟢 -34.80% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 619.85 | 8.58 | 🟢 -98.62% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.95 | 4.52 | 🟢 +53.37% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 170.82 | 248.04 | 🔴 +45.21% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.50 | 16.10 | 🔴 -41.45% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1220.54 | 2084.64 | 🔴 +70.80% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 51.48 | 936.92 | 🔴 +1720.09% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 41.24 | 24.14 | 🔴 -41.45% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.20 | 11.16 | 🔴 -61.79% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1148.99 | 3007.15 | 🔴 +161.72% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 16.91 | 202.86 | 🔴 +1099.48% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 43.81 | 16.74 | 🔴 -61.79% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 233.67 | 294.45 | 🔴 +26.01% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 112.84 | 131.20 | 🔴 +16.27% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.71 | 3.53 | 🟢 -47.42% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.60 | 11.66 | 🔴 +21.46% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.91 | 11.72 | 🔴 -57.99% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1202.52 | 2862.69 | 🔴 +138.06% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 25.61 | 828.02 | 🔴 +3132.76% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 27.90 | 11.72 | 🔴 -57.99% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.25 | 10.52 | 🔴 -64.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1147.35 | 3189.93 | 🔴 +178.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 33.59 | 299.98 | 🔴 +793.10% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.25 | 10.52 | 🔴 -64.03% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.05 | 11.14 | 🔴 -61.65% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1155.03 | 3012.13 | 🔴 +160.78% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 59.02 | 385.35 | 🔴 +552.96% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.26 | 2.78 | 🔴 -61.65% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 363.04 | 179.90 | 🟢 -50.45% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 184.03 | 90.97 | 🟢 -50.57% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 7.80 | 38.49 | 🔴 +393.53% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 21.02 | 17.17 | 🔴 -18.33% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1596.57 | 1954.89 | 🔴 +22.44% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 600.48 | 880.47 | 🔴 +46.63% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 5.25 | 4.29 | 🔴 -18.33% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.32 | 16.04 | 🔴 -43.37% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1185.01 | 2092.42 | 🔴 +76.57% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 13.12 | 997.75 | 🔴 +7504.79% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.08 | 4.01 | 🔴 -43.37% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 11.02 | 16.63 | 🔴 +50.93% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 12.49 | 10.65 | 🔴 -14.72% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2686.34 | 3150.07 | 🔴 +17.26% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 685.53 | 494.60 | 🟢 -27.85% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 3.12 | 2.66 | 🔴 -14.72% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 44.15 | 74.10 | 🔴 +67.82% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 83.89 | 5.66 | 🟢 -93.25% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 18.82 | 13.37 | 🔴 -28.99% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1782.50 | 2510.26 | 🔴 +40.83% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 731.93 | 948.68 | 🔴 +29.61% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.71 | 3.34 | 🔴 -28.99% |

