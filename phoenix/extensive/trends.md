# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 275.41 µs | 571.79 µs | ⚪ +107.61% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.93 µs | 49.07 µs | ⚪ +607.81% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 187.40 µs | 1140.27 µs | ⚪ +508.46% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 12.54 µs | 8.33 µs | ⚪ -33.55% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 31.44 GB/s | 14.88 GB/s | 🔴 -52.67% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1601.10 µs | 3382.80 µs | 🔴 +111.28% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 118.42 µs | 707.63 µs | ⚪ +497.57% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.24 GOP/s | 2.48 GOP/s | 🔴 -52.67% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 378.61 µs | 494.85 µs | ⚪ +30.70% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 6.20 µs | 13.98 µs | ⚪ +125.64% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 583.62 µs | 320.98 µs | ⚪ -45.00% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 281.11 µs | 471.72 µs | ⚪ +67.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 648.43 µs | 407.09 µs | ⚪ -37.22% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 598.24 µs | 892.32 µs | ⚪ +49.16% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.30 GB/s | 26.57 GB/s | 🟢 +157.85% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3256.98 µs | 1263.13 µs | 🟢 -61.22% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 301.31 µs | 203.74 µs | ⚪ -32.38% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 15.45 GOP/s | 39.85 GOP/s | 🟢 +157.85% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 311.78 µs | 167.63 µs | ⚪ -46.24% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.51 GB/s | 7.36 GB/s | 🔴 -65.77% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 974.99 µs | 2848.01 µs | 🔴 +192.11% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 40.27 µs | 680.83 µs | ⚪ +1590.62% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.34 GOP/s | 0.46 GOP/s | 🔴 -65.77% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 196.25 µs | 346.81 µs | ⚪ +76.72% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 66.73 µs | 62.76 µs | ⚪ -5.96% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 38.01 µs | 63.69 µs | ⚪ +67.57% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 184.78 µs | 39.49 µs | ⚪ -78.63% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 15.46 µs | 2.71 µs | ⚪ -82.47% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 16.01 µs | 13.48 µs | ⚪ -15.82% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 11.65 GB/s | 28.59 GB/s | 🟢 +145.33% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1088.41 µs | 79.52 µs | ⚪ -92.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 11.65 GOP/s | 28.58 GOP/s | 🟢 +145.33% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 24.79 GB/s | 11.04 GB/s | 🔴 -55.47% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1353.38 µs | 3039.23 µs | 🔴 +124.57% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 367.74 µs | 482.06 µs | ⚪ +31.09% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 24.79 GOP/s | 11.04 GOP/s | 🔴 -55.47% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.57 GB/s | 10.08 GB/s | 🔴 -65.93% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1134.74 µs | 3330.31 µs | 🔴 +193.49% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.26 µs | 324.49 µs | ⚪ +4367.47% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.39 GOP/s | 2.52 GOP/s | 🔴 -65.93% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 238.67 µs | 263.13 µs | ⚪ +10.25% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 43.68 µs | 60.95 µs | ⚪ +39.52% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 86.46 µs | 12.98 µs | ⚪ -84.99% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 366.74 µs | 638.06 µs | ⚪ +73.98% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 6.57 µs | 17.02 µs | ⚪ +159.19% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 27.82 µs | 20.97 µs | ⚪ -24.60% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 456.23 µs | 153.06 µs | ⚪ -66.45% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 745.19 µs | 313.09 µs | ⚪ -57.98% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 300.25 µs | 1219.86 µs | ⚪ +306.28% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 12.95 µs | 25.26 µs | ⚪ +95.07% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.65 GB/s | 9.52 GB/s | 🔴 -67.89% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1131.63 µs | 3524.77 µs | 🔴 +211.48% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.24 µs | 315.28 µs | ⚪ +3311.23% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.41 GOP/s | 2.38 GOP/s | 🔴 -67.89% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.53 GB/s | 0.48 GB/s | 🔴 -68.66% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1367.49 µs | 4364.04 µs | 🔴 +219.13% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 88.49 µs | 74.18 µs | ⚪ -16.17% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 609.72 µs | 233.25 µs | ⚪ -61.74% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 336.68 µs | 540.80 µs | ⚪ +60.63% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 456.42 µs | 1057.68 µs | ⚪ +131.73% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 511.75 µs | 814.02 µs | ⚪ +59.07% |

