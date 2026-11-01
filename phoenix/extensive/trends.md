# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1070.94 µs | 339.52 µs | ⚪ -68.30% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 458.77 µs | 621.70 µs | ⚪ +35.52% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 3.13 µs | 4.63 µs | ⚪ +48.06% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 41.23 µs | 8.74 µs | ⚪ -78.80% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.26 GB/s | 13.93 GB/s | 🔴 -8.67% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3298.97 µs | 3612.29 µs | 🔴 +9.50% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.54 GOP/s | 2.32 GOP/s | 🔴 -8.67% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.28 GB/s | 15.25 GB/s | 🔴 -52.76% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1559.26 µs | 3300.42 µs | 🔴 +111.67% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 23.02 µs | 399.85 µs | ⚪ +1637.05% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.38 GOP/s | 2.54 GOP/s | 🔴 -52.76% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.12 GB/s | 0.08 GB/s | 🔴 -30.79% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 16.35 µs | 23.62 µs | 🔴 +44.48% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.29 µs | 8.56 µs | ⚪ +99.32% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 558.53 µs | 283.43 µs | ⚪ -49.25% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 325.86 µs | 90.22 µs | ⚪ -72.31% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 10.93 GB/s | 12.64 GB/s | 🟢 +15.70% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 3456.61 µs | 2987.69 µs | 🟢 -13.57% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 479.46 µs | 170.22 µs | ⚪ -64.50% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 10.92 GOP/s | 12.63 GOP/s | 🟢 +15.70% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 9.58 GB/s | 10.30 GB/s | 🟢 +7.47% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3503.02 µs | 3259.68 µs | 🟢 -6.95% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 120.05 µs | 469.80 µs | ⚪ +291.34% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 9.58 GOP/s | 10.29 GOP/s | 🟢 +7.47% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 10.40 GB/s | 15.08 GB/s | 🟢 +45.02% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3229.07 µs | 2226.65 µs | 🟢 -31.04% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 118.21 µs | 157.09 µs | ⚪ +32.89% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 10.39 GOP/s | 15.07 GOP/s | 🟢 +45.02% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 12.64 GB/s | 9.43 GB/s | 🔴 -25.39% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 2656.58 µs | 3560.71 µs | 🔴 +34.03% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 857.18 µs | 320.98 µs | ⚪ -62.55% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 12.63 GOP/s | 9.42 GOP/s | 🔴 -25.39% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.26 GB/s | 10.69 GB/s | 🔴 -62.17% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1187.56 µs | 3138.80 µs | 🔴 +164.31% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.25 µs | 395.26 µs | ⚪ +7436.02% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.38 GOP/s | 16.04 GOP/s | 🔴 -62.17% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 25.44 GB/s | 29.82 GB/s | 🟢 +17.20% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1318.90 µs | 1125.38 µs | 🟢 -14.67% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 212.22 µs | 6.39 µs | ⚪ -96.99% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 38.16 GOP/s | 44.72 GOP/s | 🟢 +17.20% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 207.41 µs | 164.80 µs | ⚪ -20.55% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 157.20 µs | 302.74 µs | ⚪ +92.58% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 94.16 µs | 162.17 µs | ⚪ +72.23% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 133.31 µs | 151.63 µs | ⚪ +13.74% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 34.24 µs | 139.02 µs | ⚪ +305.95% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.19 GB/s | 0.20 GB/s | 🟢 +6.09% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 88.42 µs | 83.35 µs | 🟢 -5.74% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 15.49 µs | 13.49 µs | ⚪ -12.96% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.40 GB/s | 0.35 GB/s | 🔴 -13.21% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 127.27 µs | 146.64 µs | 🔴 +15.22% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 11.47 µs | 53.71 µs | ⚪ +368.44% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.27 GB/s | 10.64 GB/s | 🔴 -62.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1187.26 µs | 3155.65 µs | 🔴 +165.79% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 23.96 µs | 313.13 µs | ⚪ +1206.83% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.26 GOP/s | 10.63 GOP/s | 🔴 -62.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.69 GB/s | 10.41 GB/s | 🔴 -64.93% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1130.07 µs | 3222.18 µs | 🔴 +185.13% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 16.63 µs | 358.90 µs | ⚪ +2058.02% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.69 GOP/s | 10.41 GOP/s | 🔴 -64.93% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.75 GB/s | 25.26 GB/s | 🔴 -15.10% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1127.93 µs | 1328.53 µs | 🔴 +17.78% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.60 µs | 313.30 µs | ⚪ +2045.59% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.44 GOP/s | 6.31 GOP/s | 🔴 -15.10% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 304.95 µs | 235.58 µs | ⚪ -22.75% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 181.80 µs | 164.12 µs | ⚪ -9.72% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 17.58 µs | 11.65 µs | ⚪ -33.74% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 18.61 GB/s | 9.88 GB/s | 🔴 -46.88% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1803.86 µs | 3395.83 µs | 🔴 +88.25% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 734.36 µs | 397.28 µs | ⚪ -45.90% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 4.65 GOP/s | 2.47 GOP/s | 🔴 -46.88% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 13.63 GB/s | 10.34 GB/s | 🔴 -24.17% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 2462.01 µs | 3246.60 µs | 🔴 +31.87% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 915.49 µs | 639.53 µs | ⚪ -30.14% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 3.41 GOP/s | 2.58 GOP/s | 🔴 -24.17% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 24.65 µs | 9.15 µs | ⚪ -62.86% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 483.60 µs | 264.29 µs | ⚪ -45.35% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 11.98 GB/s | 10.77 GB/s | 🔴 -10.09% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2800.78 µs | 3115.19 µs | 🔴 +11.23% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 902.93 µs | 338.60 µs | ⚪ -62.50% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 3.00 GOP/s | 2.69 GOP/s | 🔴 -10.09% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 19.88 GB/s | 29.40 GB/s | 🟢 +47.89% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1687.88 µs | 1141.28 µs | 🟢 -32.38% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 713.76 µs | 27.11 µs | ⚪ -96.20% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.97 GOP/s | 7.35 GOP/s | 🟢 +47.89% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 4.51 µs | 11.73 µs | ⚪ +160.20% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.19 GB/s | 29.53 GB/s | 🟢 +163.81% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2997.89 µs | 1136.38 µs | 🟢 -62.09% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 706.32 µs | 8.56 µs | ⚪ -98.79% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.80 GOP/s | 7.38 GOP/s | 🟢 +163.81% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.50 GB/s | 1.34 GB/s | 🟢 +169.44% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4215.24 µs | 1564.46 µs | 🟢 -62.89% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 311.42 µs | 110.47 µs | ⚪ -64.53% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 3.24 GB/s | 3.43 GB/s | 🟢 +5.64% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 5173.09 µs | 4896.77 µs | 🟢 -5.34% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 1018.61 µs | 788.90 µs | ⚪ -22.55% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 1660.50 GOP/s | 1754.20 GOP/s | 🟢 +5.64% |

