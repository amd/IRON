# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 32.12 GB/s | 16.93 GB/s | 🔴 -47.28% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 8.65 µs | 1014.66 µs | ⚪ +11635.65% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 10.71 GOP/s | 5.64 GOP/s | 🔴 -47.28% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 425.03 µs | 213.34 µs | ⚪ -49.81% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 110.99 µs | 1190.65 µs | ⚪ +972.72% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 4.86 µs | 14.72 µs | ⚪ +202.58% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1130.45 µs | 29.21 µs | ⚪ -97.42% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.14 GB/s | 13.75 GB/s | 🔴 -57.23% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1565.91 µs | 3661.35 µs | 🔴 +133.82% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 5.34 µs | 748.36 µs | ⚪ +13901.09% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.36 GOP/s | 2.29 GOP/s | 🔴 -57.23% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.17 µs | 4.25 µs | ⚪ -40.67% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1152.73 µs | 5.40 µs | ⚪ -99.53% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 680.20 µs | 71.82 µs | ⚪ -89.44% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 217.53 µs | 13.32 µs | ⚪ -93.87% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 615.53 µs | 647.97 µs | ⚪ +5.27% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 569.56 µs | 314.01 µs | ⚪ -44.87% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.23 GB/s | 9.73 GB/s | 🔴 -64.28% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1233.12 µs | 3452.33 µs | 🔴 +179.97% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 37.42 µs | 308.81 µs | ⚪ +725.25% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.21 GOP/s | 9.72 GOP/s | 🔴 -64.28% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1102.39 µs | 12.47 µs | ⚪ -98.87% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 527.65 µs | 626.47 µs | ⚪ +18.73% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 287.61 µs | 687.54 µs | ⚪ +139.06% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 88.15 µs | 262.72 µs | ⚪ +198.04% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 63.77 µs | 128.78 µs | ⚪ +101.94% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 44.93 µs | 71.77 µs | ⚪ +59.73% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 20.61 µs | 10.02 µs | ⚪ -51.39% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 19.80 µs | 27.79 µs | ⚪ +40.35% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.56 GB/s | 27.99 GB/s | 🟢 +165.05% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3177.96 µs | 1199.00 µs | 🟢 -62.27% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 226.67 µs | 12.19 µs | ⚪ -94.62% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.56 GOP/s | 27.99 GOP/s | 🟢 +165.05% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 611.62 µs | 312.61 µs | ⚪ -48.89% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 790.17 µs | 12.21 µs | ⚪ -98.45% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 249.52 µs | 422.00 µs | ⚪ +69.12% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 127.57 µs | 197.56 µs | ⚪ +54.86% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 25.85 µs | 9.96 µs | ⚪ -61.46% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 342.27 µs | 306.94 µs | ⚪ -10.32% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.44 GB/s | 10.71 GB/s | 🔴 -62.33% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1180.31 µs | 3133.65 µs | 🔴 +165.49% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 4.33 µs | 412.60 µs | ⚪ +9433.20% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.11 GOP/s | 2.68 GOP/s | 🔴 -62.33% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 7.18 µs | 11.10 µs | ⚪ +54.57% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 294.88 µs | 403.69 µs | ⚪ +36.90% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 18.46 GB/s | 11.21 GB/s | 🔴 -39.25% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1817.78 µs | 2992.20 µs | 🔴 +64.61% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 69.96 µs | 203.19 µs | ⚪ +190.45% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 4.61 GOP/s | 2.80 GOP/s | 🔴 -39.25% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 17.34 µs | 11.83 µs | ⚪ -31.77% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.44 GB/s | 2.74 GB/s | 🔴 -57.38% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1302.62 µs | 3056.04 µs | 🔴 +134.61% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 37.42 µs | 117.47 µs | ⚪ +213.92% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.61 GOP/s | 0.69 GOP/s | 🔴 -57.38% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.67 GB/s | 11.15 GB/s | 🔴 -62.41% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1131.04 µs | 3009.00 µs | 🔴 +166.04% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.87 µs | 385.21 µs | ⚪ +2893.32% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.42 GOP/s | 2.79 GOP/s | 🔴 -62.41% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 169.61 µs | 143.18 µs | ⚪ -15.58% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 213.65 µs | 944.38 µs | ⚪ +342.03% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 334.35 µs | 307.20 µs | ⚪ -8.12% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 398.00 µs | 505.40 µs | ⚪ +26.99% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 1009.09 µs | 925.63 µs | ⚪ -8.27% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 1097.46 µs | 647.99 µs | ⚪ -40.96% |

