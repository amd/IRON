# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 292.72 µs | 443.41 µs | ⚪ +51.48% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 436.82 µs | 697.28 µs | ⚪ +59.63% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.68 GB/s | 5.14 GB/s | 🔴 -67.21% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1069.81 µs | 3262.36 µs | 🔴 +204.95% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 29.64 µs | 124.41 µs | ⚪ +319.73% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 8.08 µs | 12.53 µs | ⚪ +54.97% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 559.39 µs | 344.97 µs | ⚪ -38.33% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 458.48 µs | 712.79 µs | ⚪ +55.47% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 0.61 µs | 2.29 µs | ⚪ +278.94% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.21 GB/s | 15.83 GB/s | 🟢 +55.07% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3287.28 µs | 2119.90 µs | 🟢 -35.51% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 244.21 µs | 269.98 µs | ⚪ +10.55% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.55 GOP/s | 3.96 GOP/s | 🟢 +55.07% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 328.09 µs | 56.15 µs | ⚪ -82.89% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 293.59 µs | 10.94 µs | ⚪ -96.27% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 288.75 µs | 357.21 µs | ⚪ +23.71% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 424.59 µs | 218.97 µs | ⚪ -48.43% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 265.42 µs | 227.19 µs | ⚪ -14.40% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.12 GB/s | 14.20 GB/s | 🔴 -49.50% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.26 µs | 1097.77 µs | ⚪ +17430.69% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.17 GOP/s | 21.29 GOP/s | 🔴 -49.50% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 486.51 µs | 336.17 µs | ⚪ -30.90% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 929.11 µs | 304.66 µs | ⚪ -67.21% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 202.07 µs | 246.41 µs | ⚪ +21.94% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 67.67 µs | 101.87 µs | ⚪ +50.54% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 68.84 µs | 125.80 µs | ⚪ +82.73% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 146.01 µs | 425.69 µs | ⚪ +191.55% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 5.45 µs | 6.41 µs | ⚪ +17.65% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 15.02 µs | 8.97 µs | ⚪ -40.28% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 267.87 µs | 501.81 µs | ⚪ +87.34% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.75 GB/s | 29.56 GB/s | 🟢 +175.06% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3122.36 µs | 1135.14 µs | 🟢 -63.64% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 377.81 µs | 6.61 µs | ⚪ -98.25% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.75 GOP/s | 29.56 GOP/s | 🟢 +175.06% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.89 GB/s | 29.54 GB/s | 🟢 +198.69% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3392.59 µs | 1135.83 µs | 🟢 -66.52% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 243.19 µs | 7.67 µs | ⚪ -96.84% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.47 GOP/s | 7.39 GOP/s | 🟢 +198.69% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 327.02 µs | 184.83 µs | ⚪ -43.48% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 38.58 µs | 46.59 µs | ⚪ +20.76% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 11.34 µs | 13.22 µs | ⚪ +16.60% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.17 GB/s | 10.53 GB/s | 🔴 -62.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1191.26 µs | 3188.69 µs | 🔴 +167.67% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 13.24 µs | 327.18 µs | ⚪ +2372.09% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.04 GOP/s | 2.63 GOP/s | 🔴 -62.64% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 1112.34 µs | 268.74 µs | ⚪ -75.84% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 347.13 µs | 193.08 µs | ⚪ -44.38% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 555.94 µs | 243.25 µs | ⚪ -56.25% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.89 GB/s | 29.59 GB/s | 🟢 +199.09% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3391.45 µs | 1133.92 µs | 🟢 -66.57% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 254.82 µs | 5.41 µs | ⚪ -97.88% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.47 GOP/s | 7.40 GOP/s | 🟢 +199.09% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 6.21 µs | 4.75 µs | ⚪ -23.50% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 251.36 µs | 320.22 µs | ⚪ +27.40% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.48 GB/s | 1.63 GB/s | 🟢 +240.95% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4374.70 µs | 1283.10 µs | 🟢 -70.67% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 145.98 µs | 388.63 µs | ⚪ +166.23% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 259.82 µs | 930.03 µs | ⚪ +257.95% |

