# Performance trends

**Operators added:** `mha_prefill_lxl`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 455.84 µs | 866.55 µs | ⚪ +90.10% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 358.66 µs | 312.93 µs | ⚪ -12.75% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 39.07 µs | 10.50 µs | ⚪ -73.11% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.15 µs | 15.19 µs | ⚪ +49.63% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 41.83 µs | 1200.24 µs | ⚪ +2769.10% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.40 GB/s | 15.68 GB/s | 🔴 -51.61% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1553.66 µs | 3210.88 µs | 🔴 +106.67% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 7.84 µs | 640.28 µs | ⚪ +8066.29% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.40 GOP/s | 2.61 GOP/s | 🔴 -51.61% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 384.35 µs | 594.15 µs | ⚪ +54.59% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 516.36 µs | 629.55 µs | ⚪ +21.92% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 13.32 GB/s | 12.00 GB/s | 🔴 -9.96% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 2835.73 µs | 3149.30 µs | 🔴 +11.06% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 21.70 µs | 145.47 µs | ⚪ +570.34% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 13.31 GOP/s | 11.99 GOP/s | 🔴 -9.96% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 343.49 µs | 526.70 µs | ⚪ +53.34% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 15.58 GB/s | 10.02 GB/s | 🔴 -35.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 2154.44 µs | 3350.16 µs | 🔴 +55.50% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 69.61 µs | 284.86 µs | ⚪ +309.25% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 15.57 GOP/s | 10.02 GOP/s | 🔴 -35.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1180.01 µs | 352.71 µs | ⚪ -70.11% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.23 GB/s | 11.01 GB/s | 🔴 -61.00% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1188.75 µs | 3048.09 µs | 🔴 +156.41% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 39.49 µs | 446.81 µs | ⚪ +1031.32% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.34 GOP/s | 16.51 GOP/s | 🔴 -61.00% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 906.60 µs | 747.51 µs | ⚪ -17.55% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 319.55 µs | 416.86 µs | ⚪ +30.45% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 318.20 µs | 136.52 µs | ⚪ -57.10% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 109.02 µs | 44.67 µs | ⚪ -59.03% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 229.21 µs | 279.41 µs | ⚪ +21.90% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 17.82 µs | 8.58 µs | ⚪ -51.85% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.55 µs | 8.96 µs | ⚪ +18.63% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 9.66 GB/s | 28.17 GB/s | 🟢 +191.64% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3474.22 µs | 1191.29 µs | 🟢 -65.71% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 270.65 µs | 67.04 µs | ⚪ -75.23% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 9.66 GOP/s | 28.17 GOP/s | 🟢 +191.64% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1241.37 µs | 464.60 µs | ⚪ -62.57% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 380.01 µs | 564.34 µs | ⚪ +48.51% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 337.06 µs | 485.71 µs | ⚪ +44.10% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 132.80 µs | 168.19 µs | ⚪ +26.65% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 25.42 µs | 12.02 µs | ⚪ -52.71% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 152.17 µs | 51.09 µs | ⚪ -66.42% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 18.89 µs | 27.79 µs | ⚪ +47.09% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 322.48 µs | 353.87 µs | ⚪ +9.73% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 11.39 GB/s | 18.34 GB/s | 🟢 +60.93% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2944.84 µs | 1829.92 µs | 🟢 -37.86% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 58.97 µs | 15.06 µs | ⚪ -74.46% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.85 GOP/s | 4.58 GOP/s | 🟢 +60.93% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1325.97 µs | 324.53 µs | ⚪ -75.53% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3134.87 µs | 1753.78 µs | 🟢 -44.06% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 236.75 µs | 522.49 µs | ⚪ +120.69% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.72 µs | 6.72 µs | ⚪ -37.29% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.48 GB/s | 1.53 GB/s | 🟢 +217.54% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4344.56 µs | 1368.21 µs | 🟢 -68.51% |

