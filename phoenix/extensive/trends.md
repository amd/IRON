# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 284.64 µs | 763.06 µs | ⚪ +168.08% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 511.79 µs | 766.61 µs | ⚪ +49.79% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.64 GB/s | 15.83 GB/s | 🟢 +180.53% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 2972.81 µs | 1059.70 µs | 🟢 -64.35% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 267.61 µs | 11.64 µs | ⚪ -95.65% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 31.44 µs | 10.82 µs | ⚪ -65.61% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 309.05 µs | 1171.12 µs | ⚪ +278.94% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.68 GB/s | 15.53 GB/s | 🔴 -52.48% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1540.28 µs | 3241.38 µs | 🔴 +110.44% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 66.41 µs | 276.61 µs | ⚪ +316.51% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.45 GOP/s | 2.59 GOP/s | 🔴 -52.48% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.97 µs | 10.00 µs | ⚪ +25.53% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 335.03 µs | 533.13 µs | ⚪ +59.13% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 150.30 µs | 254.24 µs | ⚪ +69.16% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 427.37 µs | 399.62 µs | ⚪ -6.49% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 10.23 GB/s | 15.46 GB/s | 🟢 +51.18% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3283.18 µs | 2171.76 µs | 🟢 -33.85% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 425.62 µs | 123.40 µs | ⚪ -71.01% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 10.22 GOP/s | 15.45 GOP/s | 🟢 +51.18% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3418.01 µs | 1687.73 µs | 🟢 -50.62% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 265.26 µs | 550.26 µs | ⚪ +107.44% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.80 µs | 609.45 µs | ⚪ +6827.94% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.92 GB/s | 10.89 GB/s | 🔴 -63.62% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1121.37 µs | 3082.25 µs | 🔴 +174.87% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.70 µs | 607.91 µs | ⚪ +6886.71% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.88 GOP/s | 16.33 GOP/s | 🔴 -63.62% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.16 GB/s | 7.03 GB/s | 🔴 -66.76% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 991.20 µs | 2981.77 µs | 🔴 +200.82% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 5.42 µs | 136.77 µs | ⚪ +2423.38% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.32 GOP/s | 0.44 GOP/s | 🔴 -66.76% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 110.77 µs | 69.35 µs | ⚪ -37.40% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 73.92 µs | 82.48 µs | ⚪ +11.58% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 2.43 µs | 36.48 µs | ⚪ +1401.79% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 13.56 µs | 12.79 µs | ⚪ -5.66% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.20 µs | 34.52 µs | ⚪ +379.61% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.95 GB/s | 11.00 GB/s | 🔴 -60.65% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1200.89 µs | 3051.87 µs | 🔴 +154.13% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 35.21 µs | 178.39 µs | ⚪ +406.68% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 27.94 GOP/s | 10.99 GOP/s | 🔴 -60.65% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 937.01 µs | 388.06 µs | ⚪ -58.59% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.94 GB/s | 10.17 GB/s | 🔴 -66.03% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1120.82 µs | 3299.54 µs | 🔴 +194.38% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.09 µs | 307.73 µs | ⚪ +4241.24% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.48 GOP/s | 2.54 GOP/s | 🔴 -66.03% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 257.71 µs | 211.96 µs | ⚪ -17.75% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 92.02 µs | 59.49 µs | ⚪ -35.35% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.07 µs | 71.72 µs | ⚪ +494.36% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.81 GB/s | 10.71 GB/s | 🔴 -62.82% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1164.81 µs | 3133.26 µs | 🔴 +168.99% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 15.35 µs | 715.58 µs | ⚪ +4562.07% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.20 GOP/s | 2.68 GOP/s | 🔴 -62.82% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 27.42 µs | 9.56 µs | ⚪ -65.13% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 248.55 µs | 522.72 µs | ⚪ +110.31% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 410.78 µs | 263.57 µs | ⚪ -35.84% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 270.26 µs | 843.59 µs | ⚪ +212.14% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 805.93 µs | 550.83 µs | ⚪ -31.65% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1368.19 µs | 678.24 µs | ⚪ -50.43% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.62 GB/s | 0.50 GB/s | 🔴 -18.14% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 3403.67 µs | 4158.06 µs | 🔴 +22.16% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 110.82 µs | 136.95 µs | ⚪ +23.58% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 223.91 µs | 1008.38 µs | ⚪ +350.35% |

