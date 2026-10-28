# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.69 | 13.02 | 🟢 +21.76% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3138.23 | 2577.46 | 🟢 -17.87% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 240.77 | 1005.51 | 🔴 +317.61% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.67 | 3.25 | 🟢 +21.76% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 11.55 | 10.15 | 🔴 -12.11% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1452.98 | 1653.20 | 🔴 +13.78% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 494.20 | 738.56 | 🔴 +49.45% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 495.73 | 399.01 | 🟢 -19.51% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 25.18 | 16.43 | 🔴 -34.75% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1998.64 | 3062.83 | 🔴 +53.25% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 568.97 | 707.83 | 🔴 +24.41% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 4.20 | 2.74 | 🔴 -34.75% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.10 | 0.12 | 🟢 +17.66% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 19.43 | 16.51 | 🟢 -15.01% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 6.06 | 2.84 | 🟢 -53.18% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.17 | 10.09 | 🔴 -9.68% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3003.76 | 3325.55 | 🔴 +10.71% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 295.08 | 440.18 | 🔴 +49.18% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.79 | 2.52 | 🔴 -9.68% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 302.19 | 548.26 | 🔴 +81.43% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 17.21 | 10.20 | 🔴 -40.75% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1949.98 | 3291.17 | 🔴 +68.78% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 901.01 | 278.93 | 🟢 -69.04% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 25.81 | 15.29 | 🔴 -40.75% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.85 | 10.65 | 🔴 -64.32% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1124.23 | 3150.76 | 🔴 +180.26% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.65 | 357.16 | 🔴 +3599.80% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.77 | 15.97 | 🔴 -64.32% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 195.24 | 270.58 | 🔴 +38.59% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Bandwidth` | 0.10 | 0.08 | 🔴 -22.19% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency` | 81349.04 | 104554.11 | 🔴 +28.53% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 57.47 | 129.78 | 🔴 +125.81% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Throughput` | 422.40 | 328.65 | 🔴 -22.19% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 151.96 | 83.91 | 🟢 -44.78% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.19 | 0.20 | 🟢 +6.26% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 88.49 | 83.28 | 🟢 -5.89% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 9.35 | 16.46 | 🔴 +76.09% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 4.11 | 6.68 | 🔴 +62.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.53 | 9.64 | 🔴 -66.23% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1176.29 | 3483.24 | 🔴 +196.12% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 30.50 | 147.22 | 🔴 +382.63% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.53 | 9.63 | 🔴 -66.23% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 355.59 | 237.48 | 🟢 -33.22% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.76 | 10.55 | 🔴 -64.56% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1127.45 | 3181.22 | 🔴 +182.16% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.52 | 411.06 | 🔴 +4216.52% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.44 | 2.64 | 🔴 -64.56% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 312.96 | 249.12 | 🟢 -20.40% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 105.14 | 110.73 | 🔴 +5.32% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 16.55 | 11.08 | 🟢 -33.05% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.03 | 10.85 | 🔴 -61.29% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1197.33 | 3092.82 | 🔴 +158.31% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 49.86 | 538.38 | 🔴 +979.82% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.01 | 2.71 | 🔴 -61.29% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 29.16 | 27.55 | 🟢 -5.53% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 26.77 | 11.79 | 🟢 -55.94% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 319.21 | 437.86 | 🔴 +37.17% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.98 | 10.04 | 🔴 -16.21% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2801.09 | 3343.08 | 🔴 +19.35% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 848.47 | 378.69 | 🟢 -55.37% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.99 | 2.51 | 🔴 -16.21% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 23.25 | 72.02 | 🔴 +209.72% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 16.44 | 29.40 | 🟢 +78.86% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2041.47 | 1141.38 | 🟢 -44.09% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 993.92 | 17.31 | 🟢 -98.26% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.11 | 7.35 | 🟢 +78.86% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 121.31 | 339.66 | 🔴 +179.99% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 3.26 | 3.03 | 🔴 -7.28% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 5142.08 | 5545.63 | 🔴 +7.85% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 922.75 | 738.17 | 🟢 -20.00% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 1670.52 | 1548.96 | 🔴 -7.28% |

