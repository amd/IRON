# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 17.83 GB/s | 32.09 GB/s | 🟢 +79.95% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 2822.60 µs | 1568.56 µs | 🟢 -44.43% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 581.49 µs | 62.60 µs | ⚪ -89.23% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.94 GOP/s | 10.70 GOP/s | 🟢 +79.95% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 29.30 GB/s | 13.35 GB/s | 🔴 -54.46% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 45.20 µs | 1251.08 µs | ⚪ +2667.56% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 7.33 GOP/s | 3.34 GOP/s | 🔴 -54.46% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1466.69 µs | 3094.37 µs | 🔴 +110.98% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 556.40 µs | 172.91 µs | ⚪ -68.92% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 985.36 µs | 351.56 µs | ⚪ -64.32% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 8.10 µs | 4.47 µs | ⚪ -44.80% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 249.93 µs | 467.85 µs | ⚪ +87.20% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 676.64 µs | 496.48 µs | ⚪ -26.63% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 210.15 µs | 136.98 µs | ⚪ -34.82% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 705.25 µs | 13.20 µs | ⚪ -98.13% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3345.35 µs | 2372.95 µs | 🟢 -29.07% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 296.09 µs | 394.91 µs | ⚪ +33.37% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.42 GB/s | 27.52 GB/s | 🟢 +164.16% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3221.34 µs | 1219.49 µs | 🟢 -62.14% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 175.35 µs | 57.54 µs | ⚪ -67.18% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 15.62 GOP/s | 41.27 GOP/s | 🟢 +164.16% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 64.33 µs | 1349.34 µs | ⚪ +1997.66% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.01 GB/s | 8.48 GB/s | 🔴 -59.63% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 5.69 µs | 930.38 µs | ⚪ +16262.60% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.31 GOP/s | 0.53 GOP/s | 🔴 -59.63% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 206.38 µs | 236.20 µs | ⚪ +14.45% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 48.53 µs | 233.33 µs | ⚪ +380.81% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 149.10 µs | 97.20 µs | ⚪ -34.81% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 5.56 µs | 110.06 µs | ⚪ +1879.37% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 14.30 µs | 12.48 µs | ⚪ -12.71% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 11.68 µs | 8.90 µs | ⚪ -23.81% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 361.32 µs | 706.30 µs | ⚪ +95.48% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.87 µs | 188.10 µs | ⚪ +897.05% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 288.17 µs | 848.00 µs | ⚪ +194.27% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 199.82 µs | 296.01 µs | ⚪ +48.14% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 74.02 µs | 180.12 µs | ⚪ +143.35% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 10.08 µs | 27.77 µs | ⚪ +175.51% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 74.62 µs | 9.81 µs | ⚪ -86.86% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 1020.55 µs | 7.32 µs | ⚪ -99.28% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 15.06 µs | 47.47 µs | ⚪ +215.13% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 217.60 µs | 431.95 µs | ⚪ +98.51% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.02 GB/s | 18.31 GB/s | 🟢 +82.68% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3347.24 µs | 1832.32 µs | 🟢 -45.26% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 391.95 µs | 15.74 µs | ⚪ -95.98% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.51 GOP/s | 4.58 GOP/s | 🟢 +82.68% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.28 GB/s | 10.78 GB/s | 🔴 -63.20% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1145.99 µs | 3113.76 µs | 🔴 +171.71% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 15.82 µs | 306.61 µs | ⚪ +1838.14% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.32 GOP/s | 2.69 GOP/s | 🔴 -63.20% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 384.34 µs | 358.77 µs | ⚪ -6.65% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1129.91 µs | 13.84 µs | ⚪ -98.77% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.48 GB/s | 1.54 GB/s | 🟢 +223.60% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4402.02 µs | 1360.33 µs | 🟢 -69.10% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 46.73 µs | 212.70 µs | ⚪ +355.19% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 3.86 GB/s | 2.97 GB/s | 🔴 -23.19% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 4343.87 µs | 5655.41 µs | 🔴 +30.19% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 485.43 µs | 459.53 µs | ⚪ -5.34% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 1977.49 GOP/s | 1518.89 GOP/s | 🔴 -23.19% |

