# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 378.47 µs | 554.49 µs | ⚪ +46.51% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 29.50 GB/s | 11.45 GB/s | 🔴 -61.17% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 24.47 µs | 984.35 µs | ⚪ +3923.32% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 7.37 GOP/s | 2.86 GOP/s | 🔴 -61.17% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 14.58 GB/s | 5.11 GB/s | 🔴 -64.93% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1151.00 µs | 3282.38 µs | 🔴 +185.18% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 231.75 µs | 196.54 µs | ⚪ -15.19% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 33.09 µs | 10.24 µs | ⚪ -69.05% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 539.10 µs | 577.02 µs | ⚪ +7.03% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 199.00 µs | 324.75 µs | ⚪ +63.19% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 18.02 µs | 5.14 µs | ⚪ -71.50% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 454.27 µs | 639.88 µs | ⚪ +40.86% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 581.39 µs | 540.56 µs | ⚪ -7.02% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 270.19 µs | 82.70 µs | ⚪ -69.39% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.98 GB/s | 15.78 GB/s | 🟢 +43.64% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3056.72 µs | 2128.10 µs | 🟢 -30.38% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 163.40 µs | 7.17 µs | ⚪ -95.61% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.98 GOP/s | 15.77 GOP/s | 🟢 +43.64% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 776.33 µs | 200.91 µs | ⚪ -74.12% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 535.83 µs | 278.82 µs | ⚪ -47.96% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 357.74 µs | 257.40 µs | ⚪ -28.05% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.49 µs | 13.49 µs | ⚪ +7.94% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 14.36 µs | 12.21 µs | ⚪ -14.94% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 84.73 µs | 76.45 µs | ⚪ -9.77% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 109.79 µs | 196.26 µs | ⚪ +78.76% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 169.07 µs | 314.25 µs | ⚪ +85.87% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 8.38 µs | 11.92 µs | ⚪ +42.27% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 3.41 µs | 16.99 µs | ⚪ +397.95% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 398.44 µs | 334.40 µs | ⚪ -16.07% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 363.36 µs | 535.13 µs | ⚪ +47.27% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 309.28 µs | 248.40 µs | ⚪ -19.69% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 238.43 µs | 48.77 µs | ⚪ -79.55% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 10.69 µs | 39.24 µs | ⚪ +267.08% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 8.76 µs | 663.95 µs | ⚪ +7477.59% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.78 GB/s | 11.76 GB/s | 🔴 -59.12% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1166.34 µs | 2852.82 µs | 🔴 +144.60% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 10.87 µs | 692.83 µs | ⚪ +6273.18% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.19 GOP/s | 2.94 GOP/s | 🔴 -59.12% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 37.50 µs | 11.85 µs | ⚪ -68.40% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 333.57 µs | 206.59 µs | ⚪ -38.07% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 933.68 µs | 263.80 µs | ⚪ -71.75% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.85 GB/s | 30.09 GB/s | 🟢 +177.39% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3092.85 µs | 1115.00 µs | 🟢 -63.95% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 402.13 µs | 10.50 µs | ⚪ -97.39% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.71 GOP/s | 7.52 GOP/s | 🟢 +177.39% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1654.05 µs | 3032.24 µs | 🔴 +83.32% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 464.66 µs | 239.43 µs | ⚪ -48.47% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 18.95 µs | 49.74 µs | ⚪ +162.46% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.56 GB/s | 0.48 GB/s | 🔴 -69.10% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1345.03 µs | 4352.56 µs | 🔴 +223.60% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 28.25 µs | 134.11 µs | ⚪ +374.76% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 2.98 GB/s | 4.09 GB/s | 🟢 +37.26% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 5636.46 µs | 4106.38 µs | 🟢 -27.15% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 761.22 µs | 285.60 µs | ⚪ -62.48% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 1524.00 GOP/s | 2091.85 GOP/s | 🟢 +37.26% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 399.90 µs | 695.19 µs | ⚪ +73.84% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 409.72 µs | 490.04 µs | ⚪ +19.61% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 615.88 µs | 667.86 µs | ⚪ +8.44% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 651.59 µs | 739.11 µs | ⚪ +13.43% |

