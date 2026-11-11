# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 711.16 µs | 284.64 µs | ⚪ -59.98% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 977.55 µs | 511.79 µs | ⚪ -47.65% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 114.93 µs | 267.61 µs | ⚪ +132.86% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.96 µs | 31.44 µs | ⚪ +186.89% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1168.75 µs | 309.05 µs | ⚪ -73.56% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 17.41 GB/s | 32.68 GB/s | 🟢 +87.70% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2891.17 µs | 1540.28 µs | 🟢 -46.72% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 474.75 µs | 66.41 µs | ⚪ -86.01% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.90 GOP/s | 5.45 GOP/s | 🟢 +87.70% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.51 µs | 7.97 µs | ⚪ +76.60% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 16.14 GB/s | 10.40 GB/s | 🔴 -35.55% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2078.70 µs | 3225.28 µs | 🔴 +55.16% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 269.69 µs | 197.52 µs | ⚪ -26.76% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.04 GOP/s | 2.60 GOP/s | 🔴 -35.55% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 751.80 µs | 335.03 µs | ⚪ -55.44% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 106.91 µs | 150.30 µs | ⚪ +40.59% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 250.56 µs | 427.37 µs | ⚪ +70.57% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 182.19 µs | 425.62 µs | ⚪ +133.61% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.43 GB/s | 9.82 GB/s | 🔴 -64.19% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1224.00 µs | 3418.01 µs | 🔴 +179.25% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 6.22 µs | 265.26 µs | ⚪ +4166.76% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.41 GOP/s | 9.82 GOP/s | 🔴 -64.19% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 14.45 GB/s | 28.20 GB/s | 🟢 +95.12% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1020.23 µs | 8.80 µs | ⚪ -99.14% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 21.68 GOP/s | 42.30 GOP/s | 🟢 +95.12% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.40 GB/s | 29.92 GB/s | 🟢 +187.64% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3225.51 µs | 1121.37 µs | 🟢 -65.23% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 323.46 µs | 8.70 µs | ⚪ -97.31% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 15.60 GOP/s | 44.88 GOP/s | 🟢 +187.64% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 11.35 µs | 5.42 µs | ⚪ -52.23% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 96.58 µs | 110.77 µs | ⚪ +14.70% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 104.25 µs | 73.92 µs | ⚪ -29.10% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 102.85 µs | 2.43 µs | ⚪ -97.64% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 15.82 µs | 13.56 µs | ⚪ -14.29% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 30.48 µs | 7.20 µs | ⚪ -76.38% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.27 GB/s | 27.95 GB/s | 🟢 +172.08% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3267.34 µs | 1200.89 µs | 🟢 -63.25% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 249.78 µs | 35.21 µs | ⚪ -85.90% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 10.27 GOP/s | 27.94 GOP/s | 🟢 +172.08% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 385.76 µs | 937.01 µs | ⚪ +142.90% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.84 GB/s | 29.94 GB/s | 🟢 +176.22% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3095.92 µs | 1120.82 µs | 🟢 -63.80% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 466.00 µs | 7.09 µs | ⚪ -98.48% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.71 GOP/s | 7.48 GOP/s | 🟢 +176.22% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 293.62 µs | 257.71 µs | ⚪ -12.23% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 45.95 µs | 92.02 µs | ⚪ +100.25% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 13.79 µs | 12.07 µs | ⚪ -12.50% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 9.78 GB/s | 28.81 GB/s | 🟢 +194.75% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3433.22 µs | 1164.81 µs | 🟢 -66.07% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 164.18 µs | 15.35 µs | ⚪ -90.65% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.44 GOP/s | 7.20 GOP/s | 🟢 +194.75% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 332.35 µs | 249.29 µs | ⚪ -24.99% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 18.80 µs | 27.42 µs | ⚪ +45.86% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 299.53 µs | 248.55 µs | ⚪ -17.02% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 896.59 µs | 410.78 µs | ⚪ -54.18% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.87 GB/s | 9.91 GB/s | 🔴 -66.82% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1123.29 µs | 3385.31 µs | 🔴 +201.37% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.47 µs | 270.26 µs | ⚪ +3090.84% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.47 GOP/s | 2.48 GOP/s | 🔴 -66.82% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 457.60 µs | 805.93 µs | ⚪ +76.12% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.54 GB/s | 13.47 GB/s | 🔴 -54.39% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 19.60 µs | 1368.19 µs | ⚪ +6881.63% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.39 GOP/s | 3.37 GOP/s | 🔴 -54.39% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 0.62 GB/s | 🟢 +26.42% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4302.81 µs | 3403.67 µs | 🟢 -20.90% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 38.00 µs | 110.82 µs | ⚪ +191.61% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 944.40 µs | 223.91 µs | ⚪ -76.29% |

