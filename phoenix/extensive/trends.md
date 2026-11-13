# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1154.37 µs | 346.45 µs | ⚪ -69.99% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 502.27 µs | 327.98 µs | ⚪ -34.70% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.72 GB/s | 5.27 GB/s | 🔴 -66.46% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1066.99 µs | 3180.81 µs | 🔴 +198.11% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 6.15 µs | 85.46 µs | ⚪ +1290.35% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 12.98 µs | 6.35 µs | ⚪ -51.08% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 634.29 µs | 433.79 µs | ⚪ -31.61% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.94 GB/s | 32.27 GB/s | 🟢 +90.49% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2971.49 µs | 1559.93 µs | 🟢 -47.50% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 658.23 µs | 6.52 µs | ⚪ -99.01% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.82 GOP/s | 5.38 GOP/s | 🟢 +90.49% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.07 µs | 12.91 µs | ⚪ +154.49% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 443.88 µs | 381.07 µs | ⚪ -14.15% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 345.84 µs | 321.56 µs | ⚪ -7.02% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 129.24 µs | 90.23 µs | ⚪ -30.18% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 4.87 µs | 55.90 µs | ⚪ +1046.79% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 600.21 µs | 278.84 µs | ⚪ -53.54% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 9.88 GB/s | 27.03 GB/s | 🟢 +173.53% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3397.97 µs | 1242.26 µs | 🟢 -63.44% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 364.95 µs | 80.74 µs | ⚪ -77.88% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 9.87 GOP/s | 27.01 GOP/s | 🟢 +173.53% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.92 GB/s | 10.91 GB/s | 🔴 -60.94% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1202.04 µs | 3077.18 µs | 🔴 +156.00% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 36.04 µs | 543.92 µs | ⚪ +1409.08% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 41.87 GOP/s | 16.36 GOP/s | 🔴 -60.94% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.98 µs | 10.48 µs | ⚪ -44.79% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 5.48 µs | 25.69 µs | ⚪ +368.85% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 272.73 µs | 314.61 µs | ⚪ +15.36% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 83.48 µs | 29.26 µs | ⚪ -64.96% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 54.35 µs | 79.02 µs | ⚪ +45.38% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 135.23 µs | 341.73 µs | ⚪ +152.70% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 9.76 µs | 8.49 µs | ⚪ -13.03% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 9.12 µs | 13.89 µs | ⚪ +52.22% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 308.66 µs | 532.80 µs | ⚪ +72.62% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.21 GB/s | 10.30 GB/s | 🔴 -64.75% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1148.83 µs | 3259.14 µs | 🔴 +183.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 21.53 µs | 390.30 µs | ⚪ +1712.77% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.21 GOP/s | 10.30 GOP/s | 🔴 -64.75% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.14 µs | 10.55 µs | ⚪ -41.86% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 88.22 µs | 43.00 µs | ⚪ -51.26% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 106.62 µs | 87.03 µs | ⚪ -18.38% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 436.73 µs | 798.62 µs | ⚪ +82.86% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.55 GB/s | 10.88 GB/s | 🔴 -61.88% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1175.60 µs | 3084.30 µs | 🔴 +162.36% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 15.65 µs | 420.96 µs | ⚪ +2589.94% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.14 GOP/s | 2.72 GOP/s | 🔴 -61.88% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 12.75 µs | 37.19 µs | ⚪ +191.74% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 414.24 µs | 229.70 µs | ⚪ -44.55% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.31 GB/s | 17.47 GB/s | 🟢 +69.35% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 717.28 µs | 185.95 µs | ⚪ -74.08% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.58 GOP/s | 4.37 GOP/s | 🟢 +69.35% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.08 GB/s | 29.56 GB/s | 🟢 +193.28% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3329.39 µs | 1135.23 µs | 🟢 -65.90% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 284.43 µs | 10.69 µs | ⚪ -96.24% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.52 GOP/s | 7.39 GOP/s | 🟢 +193.28% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 25.48 µs | 28.92 µs | ⚪ +13.50% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1163.78 µs | 950.47 µs | ⚪ -18.33% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.46 GB/s | 1.58 GB/s | 🟢 +8.46% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1440.57 µs | 1328.18 µs | 🟢 -7.80% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 136.61 µs | 443.02 µs | ⚪ +224.30% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.69 µs | 1004.64 µs | ⚪ +21327.83% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 728.74 µs | 515.01 µs | ⚪ -29.33% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 422.57 µs | 551.66 µs | ⚪ +30.55% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 571.22 µs | 884.70 µs | ⚪ +54.88% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 584.05 µs | 810.36 µs | ⚪ +38.75% |

