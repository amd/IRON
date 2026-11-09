# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 236.98 µs | 781.54 µs | ⚪ +229.79% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 251.26 µs | 456.57 µs | ⚪ +81.71% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.96 GB/s | 5.22 GB/s | 🔴 -67.29% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1051.34 µs | 3214.59 µs | 🔴 +205.76% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 47.69 µs | 109.21 µs | ⚪ +128.98% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 743.84 µs | 672.18 µs | ⚪ -9.63% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 298.49 µs | 463.39 µs | ⚪ +55.25% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 1.99 µs | 11.80 µs | ⚪ +493.24% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 288.77 µs | 421.10 µs | ⚪ +45.83% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 822.18 µs | 208.46 µs | ⚪ -74.65% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 9.87 GB/s | 14.80 GB/s | 🟢 +50.00% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3402.66 µs | 2268.49 µs | 🟢 -33.33% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 365.32 µs | 226.55 µs | ⚪ -37.99% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 9.86 GOP/s | 14.79 GOP/s | 🟢 +50.00% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 770.81 µs | 229.09 µs | ⚪ -70.28% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 410.08 µs | 166.50 µs | ⚪ -59.40% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 543.07 µs | 375.64 µs | ⚪ -30.83% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 20.98 GB/s | 7.01 GB/s | 🔴 -66.60% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 999.59 µs | 2992.94 µs | 🔴 +199.42% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 2.37 µs | 103.04 µs | ⚪ +4249.45% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.31 GOP/s | 0.44 GOP/s | 🔴 -66.60% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Bandwidth` | 0.10 GB/s | 0.11 GB/s | 🟢 +9.60% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency` | 81163.62 µs | 74054.62 µs | 🟢 -8.76% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 74.74 µs | 111.22 µs | ⚪ +48.81% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Throughput` | 423.36 GOP/s | 464.01 GOP/s | 🟢 +9.60% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Bandwidth` | 0.07 GB/s | 0.07 GB/s | 🟢 +10.94% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency` | 639561.94 µs | 576494.61 µs | 🟢 -9.86% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 61.55 µs | 106.41 µs | ⚪ +72.89% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Throughput` | 429.82 GOP/s | 476.84 GOP/s | 🟢 +10.94% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 432.26 µs | 103.30 µs | ⚪ -76.10% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 11.64 µs | 7.69 µs | ⚪ -33.87% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 8.93 µs | 10.81 µs | ⚪ +21.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 32.73 µs | 19.59 µs | ⚪ -40.16% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 396.86 µs | 332.19 µs | ⚪ -16.30% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.61 GB/s | 29.61 GB/s | 🟢 +179.17% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3163.97 µs | 1133.36 µs | 🟢 -64.18% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 277.79 µs | 6.03 µs | ⚪ -97.83% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.65 GOP/s | 7.40 GOP/s | 🟢 +179.17% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 218.64 µs | 180.48 µs | ⚪ -17.46% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 78.65 µs | 99.77 µs | ⚪ +26.85% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 13.03 µs | 14.82 µs | ⚪ +13.76% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 1113.14 µs | 11.48 µs | ⚪ -98.97% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 80.01 µs | 20.04 µs | ⚪ -74.96% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 19.32 µs | 28.84 µs | ⚪ +49.30% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 168.63 µs | 380.48 µs | ⚪ +125.63% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 307.36 µs | 250.57 µs | ⚪ -18.48% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.59 GB/s | 10.26 GB/s | 🔴 -65.33% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1134.07 µs | 3270.79 µs | 🔴 +188.41% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.51 µs | 390.04 µs | ⚪ +5889.53% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.40 GOP/s | 2.56 GOP/s | 🔴 -65.33% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.44 GB/s | 2.96 GB/s | 🔴 -53.98% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1302.58 µs | 2830.72 µs | 🔴 +117.32% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 118.84 µs | 660.59 µs | ⚪ +455.88% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.61 GOP/s | 0.74 GOP/s | 🔴 -53.98% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.57 µs | 5.75 µs | ⚪ -39.95% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 1.52 GB/s | 🟢 +209.11% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4253.56 µs | 1376.06 µs | 🟢 -67.65% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 214.62 µs | 328.06 µs | ⚪ +52.85% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 497.20 µs | 295.05 µs | ⚪ -40.66% |

