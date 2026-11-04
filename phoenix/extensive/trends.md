# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 62.60 µs | 943.03 µs | ⚪ +1406.37% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 13.35 GB/s | 29.66 GB/s | 🟢 +122.26% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1251.08 µs | 7.56 µs | ⚪ -99.40% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 3.34 GOP/s | 7.42 GOP/s | 🟢 +122.26% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 172.91 µs | 223.37 µs | ⚪ +29.19% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 12.97 µs | 9.27 µs | ⚪ -28.55% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 699.33 µs | 600.01 µs | ⚪ -14.20% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 351.56 µs | 411.86 µs | ⚪ +17.15% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.47 µs | 6.99 µs | ⚪ +56.51% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 467.85 µs | 193.08 µs | ⚪ -58.73% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 496.48 µs | 619.31 µs | ⚪ +24.74% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.75 GB/s | 10.96 GB/s | 🔴 -30.43% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2131.59 µs | 3063.91 µs | 🔴 +43.74% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 13.20 µs | 114.98 µs | ⚪ +770.70% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.74 GOP/s | 10.95 GOP/s | 🔴 -30.43% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 362.37 µs | 505.72 µs | ⚪ +39.56% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 10.22 GB/s | 27.65 GB/s | 🟢 +170.63% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3286.47 µs | 1214.38 µs | 🟢 -63.05% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 394.91 µs | 60.16 µs | ⚪ -84.77% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 10.21 GOP/s | 27.63 GOP/s | 🟢 +170.63% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 57.54 µs | 8.04 µs | ⚪ -86.04% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1349.34 µs | 503.64 µs | ⚪ -62.68% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 8.48 GB/s | 21.00 GB/s | 🟢 +147.49% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 930.38 µs | 13.58 µs | ⚪ -98.54% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.53 GOP/s | 1.31 GOP/s | 🟢 +147.49% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 236.20 µs | 185.04 µs | ⚪ -21.66% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 233.33 µs | 218.76 µs | ⚪ -6.25% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 97.20 µs | 62.17 µs | ⚪ -36.04% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 110.06 µs | 81.07 µs | ⚪ -26.34% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 12.48 µs | 25.80 µs | ⚪ +106.74% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 8.90 µs | 14.40 µs | ⚪ +61.89% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 706.30 µs | 272.14 µs | ⚪ -61.47% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 188.10 µs | 14.05 µs | ⚪ -92.53% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 848.00 µs | 29.48 µs | ⚪ -96.52% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 296.01 µs | 269.97 µs | ⚪ -8.80% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 180.12 µs | 50.11 µs | ⚪ -72.18% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 27.77 µs | 6.78 µs | ⚪ -75.57% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.31 GB/s | 11.79 GB/s | 🔴 -58.36% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1185.60 µs | 2847.54 µs | 🔴 +140.18% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 9.81 µs | 824.00 µs | ⚪ +8301.77% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.08 GOP/s | 2.95 GOP/s | 🔴 -58.36% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 7.32 µs | 64.57 µs | ⚪ +781.57% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 47.47 µs | 8.48 µs | ⚪ -82.13% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 431.95 µs | 555.94 µs | ⚪ +28.70% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 18.31 GB/s | 10.05 GB/s | 🔴 -45.09% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1832.32 µs | 3337.15 µs | 🔴 +82.13% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 15.74 µs | 303.53 µs | ⚪ +1828.50% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 4.58 GOP/s | 2.51 GOP/s | 🔴 -45.09% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.74 GB/s | 5.70 GB/s | 🟢 +108.43% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3066.06 µs | 1471.05 µs | 🟢 -52.02% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 358.77 µs | 320.15 µs | ⚪ -10.77% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.68 GOP/s | 1.43 GOP/s | 🟢 +108.43% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.35 GB/s | 11.12 GB/s | 🔴 -62.12% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1143.06 µs | 3017.76 µs | 🔴 +164.01% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.84 µs | 731.00 µs | ⚪ +5179.92% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.34 GOP/s | 2.78 GOP/s | 🔴 -62.12% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.54 GB/s | 1.27 GB/s | 🔴 -17.86% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1360.33 µs | 1656.05 µs | 🔴 +21.74% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 212.70 µs | 194.74 µs | ⚪ -8.44% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 5655.41 µs | 4507.91 µs | 🟢 -20.29% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 459.53 µs | 548.24 µs | ⚪ +19.30% |

