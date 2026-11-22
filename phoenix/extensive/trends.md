# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 2090.70 µs | 3362.94 µs | 🔴 +60.85% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 571.79 µs | 378.47 µs | ⚪ -33.81% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 49.07 µs | 24.47 µs | ⚪ -50.14% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 1140.27 µs | 231.75 µs | ⚪ -79.68% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 8.33 µs | 33.09 µs | ⚪ +297.16% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 707.63 µs | 539.10 µs | ⚪ -23.82% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 494.85 µs | 199.00 µs | ⚪ -59.79% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 13.98 µs | 18.02 µs | ⚪ +28.87% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 358.07 µs | 454.27 µs | ⚪ +26.87% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 320.98 µs | 581.39 µs | ⚪ +81.13% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 202.16 µs | 270.19 µs | ⚪ +33.66% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 471.72 µs | 163.40 µs | ⚪ -65.36% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 407.09 µs | 776.33 µs | ⚪ +90.70% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 892.32 µs | 535.83 µs | ⚪ -39.95% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 26.57 GB/s | 10.66 GB/s | 🔴 -59.89% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1263.13 µs | 3148.84 µs | 🔴 +149.29% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 203.74 µs | 357.74 µs | ⚪ +75.59% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 39.85 GOP/s | 15.98 GOP/s | 🔴 -59.89% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 167.63 µs | 12.49 µs | ⚪ -92.55% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 7.36 GB/s | 21.12 GB/s | 🟢 +186.88% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 2848.01 µs | 992.74 µs | 🟢 -65.14% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 680.83 µs | 14.36 µs | ⚪ -97.89% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.46 GOP/s | 1.32 GOP/s | 🟢 +186.88% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 346.81 µs | 175.37 µs | ⚪ -49.43% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 62.76 µs | 84.73 µs | ⚪ +35.01% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 63.69 µs | 109.79 µs | ⚪ +72.37% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 39.49 µs | 169.07 µs | ⚪ +328.17% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.71 µs | 8.38 µs | ⚪ +209.10% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 13.48 µs | 3.41 µs | ⚪ -74.69% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.59 GB/s | 10.85 GB/s | 🔴 -62.04% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1173.89 µs | 3092.51 µs | 🔴 +163.44% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 79.52 µs | 398.44 µs | ⚪ +401.03% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.58 GOP/s | 10.85 GOP/s | 🔴 -62.04% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 482.06 µs | 363.36 µs | ⚪ -24.62% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 324.49 µs | 434.96 µs | ⚪ +34.04% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 263.13 µs | 309.28 µs | ⚪ +17.54% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 60.95 µs | 238.43 µs | ⚪ +291.21% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.98 µs | 10.69 µs | ⚪ -17.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 11.20 GB/s | 28.38 GB/s | 🟢 +153.48% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 2997.66 µs | 1182.59 µs | 🟢 -60.55% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 638.06 µs | 8.76 µs | ⚪ -98.63% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.80 GOP/s | 7.09 GOP/s | 🟢 +153.48% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 17.02 µs | 10.87 µs | ⚪ -36.14% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 20.97 µs | 37.50 µs | ⚪ +78.76% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 153.06 µs | 333.57 µs | ⚪ +117.93% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 313.09 µs | 933.68 µs | ⚪ +198.21% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1219.86 µs | 402.13 µs | ⚪ -67.03% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 25.26 µs | 464.66 µs | ⚪ +1739.37% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.52 GB/s | 29.65 GB/s | 🟢 +211.43% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3524.77 µs | 1131.81 µs | 🟢 -67.89% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 315.28 µs | 18.95 µs | ⚪ -93.99% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.38 GOP/s | 7.41 GOP/s | 🟢 +211.43% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.48 GB/s | 1.56 GB/s | 🟢 +224.46% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4364.04 µs | 1345.03 µs | 🟢 -69.18% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 74.18 µs | 28.25 µs | ⚪ -61.92% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 4.05 GB/s | 2.98 GB/s | 🔴 -26.42% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 233.25 µs | 761.22 µs | ⚪ +226.35% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 2071.08 GOP/s | 1524.00 GOP/s | 🔴 -26.42% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 540.80 µs | 399.90 µs | ⚪ -26.05% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 1057.68 µs | 409.72 µs | ⚪ -61.26% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 814.02 µs | 651.59 µs | ⚪ -19.95% |

