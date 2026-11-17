# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 396.43 µs | 529.75 µs | ⚪ +33.63% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 282.40 µs | 553.38 µs | ⚪ +95.95% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 918.69 µs | 34.29 µs | ⚪ -96.27% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 8.57 µs | 36.20 µs | ⚪ +322.64% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.82 GB/s | 33.15 GB/s | 🟢 +97.08% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2992.36 µs | 1518.37 µs | 🟢 -49.26% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 675.31 µs | 43.95 µs | ⚪ -93.49% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.80 GOP/s | 5.52 GOP/s | 🟢 +97.08% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 1370.58 µs | 372.02 µs | ⚪ -72.86% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.41 µs | 8.80 µs | ⚪ +62.55% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.38 GB/s | 17.95 GB/s | 🟢 +57.67% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2947.71 µs | 1869.56 µs | 🟢 -36.58% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 398.29 µs | 45.27 µs | ⚪ -88.63% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.85 GOP/s | 4.49 GOP/s | 🟢 +57.67% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 836.34 µs | 485.06 µs | ⚪ -42.00% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 6.58 µs | 33.99 µs | ⚪ +416.48% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.52 GB/s | 15.30 GB/s | 🟢 +45.44% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3190.97 µs | 2194.03 µs | 🟢 -31.24% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 221.64 µs | 151.40 µs | ⚪ -31.69% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.52 GOP/s | 15.29 GOP/s | 🟢 +45.44% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 10.20 GB/s | 16.01 GB/s | 🟢 +56.98% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3291.74 µs | 2096.94 µs | 🟢 -36.30% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 545.42 µs | 52.70 µs | ⚪ -90.34% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 10.19 GOP/s | 16.00 GOP/s | 🟢 +56.98% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 27.23 GB/s | 10.45 GB/s | 🔴 -61.65% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1232.81 µs | 3214.28 µs | 🔴 +160.73% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 26.27 µs | 323.67 µs | ⚪ +1132.12% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 27.22 GOP/s | 10.44 GOP/s | 🔴 -61.65% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1057.14 µs | 419.43 µs | ⚪ -60.32% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 333.61 µs | 407.25 µs | ⚪ +22.07% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 162.85 µs | 208.39 µs | ⚪ +27.97% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 338.67 µs | 115.84 µs | ⚪ -65.80% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 42.81 µs | 69.81 µs | ⚪ +63.07% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 188.34 µs | 85.76 µs | ⚪ -54.46% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 162.62 µs | 104.03 µs | ⚪ -36.03% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 12.11 µs | 1.07 µs | ⚪ -91.15% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 358.88 µs | 1537.52 µs | ⚪ +328.42% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1523.83 µs | 3167.10 µs | 🔴 +107.84% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 696.56 µs | 465.28 µs | ⚪ -33.20% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 348.94 µs | 215.74 µs | ⚪ -38.17% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 207.22 µs | 33.82 µs | ⚪ -83.68% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 11.03 µs | 44.53 µs | ⚪ +303.73% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.68 GB/s | 27.39 GB/s | 🟢 +156.36% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3141.20 µs | 1225.32 µs | 🟢 -60.99% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 509.59 µs | 67.53 µs | ⚪ -86.75% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.67 GOP/s | 6.85 GOP/s | 🟢 +156.36% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 355.51 µs | 19.45 µs | ⚪ -94.53% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 8.16 µs | 44.72 µs | ⚪ +448.05% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 287.24 µs | 360.41 µs | ⚪ +25.47% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.43 µs | 56.20 µs | ⚪ +774.43% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.53 GB/s | 2.76 GB/s | 🔴 -57.80% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1284.59 µs | 3044.05 µs | 🔴 +136.97% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 9.23 µs | 577.70 µs | ⚪ +6157.21% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.63 GOP/s | 0.69 GOP/s | 🔴 -57.80% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 30.11 µs | 152.29 µs | ⚪ +405.83% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.54 GB/s | 0.49 GB/s | 🔴 -67.85% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1362.93 µs | 4239.84 µs | 🔴 +211.08% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 206.94 µs | 11.81 µs | ⚪ -94.29% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 282.76 µs | 626.30 µs | ⚪ +121.50% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 335.20 µs | 547.55 µs | ⚪ +63.35% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 405.57 µs | 505.46 µs | ⚪ +24.63% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 547.00 µs | 707.71 µs | ⚪ +29.38% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 277.79 µs | 464.25 µs | ⚪ +67.12% |

