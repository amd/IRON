# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 339.52 µs | 292.72 µs | ⚪ -13.78% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 621.70 µs | 436.82 µs | ⚪ -29.74% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 4.63 µs | 29.64 µs | ⚪ +540.34% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 8.74 µs | 8.08 µs | ⚪ -7.52% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 13.93 GB/s | 15.35 GB/s | 🟢 +10.19% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3612.29 µs | 3278.39 µs | 🟢 -9.24% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 510.70 µs | 559.39 µs | ⚪ +9.53% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.32 GOP/s | 2.56 GOP/s | 🟢 +10.19% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.25 GB/s | 26.29 GB/s | 🟢 +72.38% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3300.42 µs | 1914.59 µs | 🟢 -41.99% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 399.85 µs | 458.48 µs | ⚪ +14.66% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.54 GOP/s | 4.38 GOP/s | 🟢 +72.38% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.08 GB/s | 0.13 GB/s | 🟢 +51.10% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 23.62 µs | 15.63 µs | 🟢 -33.82% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 8.56 µs | 0.61 µs | ⚪ -92.92% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 283.43 µs | 244.21 µs | ⚪ -13.84% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 90.22 µs | 328.09 µs | ⚪ +263.67% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 12.64 GB/s | 11.55 GB/s | 🔴 -8.63% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 2987.69 µs | 3269.99 µs | 🔴 +9.45% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 170.22 µs | 293.59 µs | ⚪ +72.48% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 12.63 GOP/s | 11.54 GOP/s | 🔴 -8.63% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.30 GB/s | 9.55 GB/s | 🔴 -7.27% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3259.68 µs | 3515.33 µs | 🔴 +7.84% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 469.80 µs | 288.75 µs | ⚪ -38.54% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.29 GOP/s | 9.55 GOP/s | 🔴 -7.27% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 15.08 GB/s | 11.40 GB/s | 🔴 -24.39% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 2226.65 µs | 2945.05 µs | 🔴 +32.26% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 157.09 µs | 424.59 µs | ⚪ +170.27% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 15.07 GOP/s | 11.39 GOP/s | 🔴 -24.39% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 9.43 GB/s | 10.10 GB/s | 🟢 +7.11% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3560.71 µs | 3324.37 µs | 🟢 -6.64% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 320.98 µs | 265.42 µs | ⚪ -17.31% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 9.42 GOP/s | 10.09 GOP/s | 🟢 +7.11% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.69 GB/s | 28.12 GB/s | 🟢 +162.98% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3138.80 µs | 1193.56 µs | 🟢 -61.97% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 395.26 µs | 6.26 µs | ⚪ -98.42% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 16.04 GOP/s | 42.17 GOP/s | 🟢 +162.98% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.82 GB/s | 11.02 GB/s | 🔴 -63.02% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1125.38 µs | 3043.49 µs | 🔴 +170.44% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.39 µs | 486.51 µs | ⚪ +7511.17% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.72 GOP/s | 16.54 GOP/s | 🔴 -63.02% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.78 GB/s | 9.64 GB/s | 🟢 +42.05% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3091.16 µs | 2176.09 µs | 🟢 -29.60% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 164.80 µs | 929.11 µs | ⚪ +463.79% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.42 GOP/s | 0.60 GOP/s | 🟢 +42.05% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 302.74 µs | 202.07 µs | ⚪ -33.25% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 162.17 µs | 67.67 µs | ⚪ -58.27% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 151.63 µs | 68.84 µs | ⚪ -54.60% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 139.02 µs | 146.01 µs | ⚪ +5.03% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 13.49 µs | 5.45 µs | ⚪ -59.59% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.35 GB/s | 0.45 GB/s | 🟢 +28.05% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 146.64 µs | 114.51 µs | 🟢 -21.91% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 53.71 µs | 15.02 µs | ⚪ -72.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.64 GB/s | 9.86 GB/s | 🔴 -7.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3155.65 µs | 3402.92 µs | 🔴 +7.84% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 313.13 µs | 267.87 µs | ⚪ -14.46% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.63 GOP/s | 9.86 GOP/s | 🔴 -7.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 358.90 µs | 377.81 µs | ⚪ +5.27% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 25.26 GB/s | 9.89 GB/s | 🔴 -60.84% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1328.53 µs | 3392.59 µs | 🔴 +155.37% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 313.30 µs | 243.19 µs | ⚪ -22.38% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 6.31 GOP/s | 2.47 GOP/s | 🔴 -60.84% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 235.58 µs | 327.02 µs | ⚪ +38.81% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 164.12 µs | 38.58 µs | ⚪ -76.49% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 9.88 GB/s | 28.17 GB/s | 🟢 +185.06% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3395.83 µs | 1191.26 µs | 🟢 -64.92% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 397.28 µs | 13.24 µs | ⚪ -96.67% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.47 GOP/s | 7.04 GOP/s | 🟢 +185.06% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.34 GB/s | 15.54 GB/s | 🟢 +50.31% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3246.60 µs | 2159.93 µs | 🟢 -33.47% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 639.53 µs | 1112.34 µs | ⚪ +73.93% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.58 GOP/s | 3.88 GOP/s | 🟢 +50.31% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 9.15 µs | 11.25 µs | ⚪ +22.92% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 264.29 µs | 347.13 µs | ⚪ +31.35% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.77 GB/s | 11.41 GB/s | 🟢 +5.91% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3115.19 µs | 2941.44 µs | 🟢 -5.58% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 338.60 µs | 555.94 µs | ⚪ +64.19% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.69 GOP/s | 2.85 GOP/s | 🟢 +5.91% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.40 GB/s | 9.89 GB/s | 🔴 -66.35% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1141.28 µs | 3391.45 µs | 🔴 +197.16% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 27.11 µs | 254.82 µs | ⚪ +840.10% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.35 GOP/s | 2.47 GOP/s | 🔴 -66.35% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 11.73 µs | 6.21 µs | ⚪ -47.10% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.53 GB/s | 10.22 GB/s | 🔴 -65.38% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1136.38 µs | 3281.98 µs | 🔴 +188.81% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.56 µs | 251.36 µs | ⚪ +2836.08% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.38 GOP/s | 2.56 GOP/s | 🔴 -65.38% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.34 GB/s | 0.48 GB/s | 🔴 -64.24% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1564.46 µs | 4374.70 µs | 🔴 +179.63% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 110.47 µs | 145.98 µs | ⚪ +32.14% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 3.43 GB/s | 4.02 GB/s | 🟢 +17.38% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 4896.77 µs | 4171.81 µs | 🟢 -14.80% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 788.90 µs | 259.82 µs | ⚪ -67.07% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 1754.20 GOP/s | 2059.04 GOP/s | 🟢 +17.38% |

