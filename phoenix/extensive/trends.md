# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 32.34 GB/s | 12.91 GB/s | 🔴 -60.07% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 1556.54 µs | 3898.59 µs | 🔴 +150.47% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 21.52 µs | 711.16 µs | ⚪ +3205.33% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 10.78 GOP/s | 4.30 GOP/s | 🔴 -60.07% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 29.60 GB/s | 14.65 GB/s | 🔴 -50.51% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 102.79 µs | 977.55 µs | ⚪ +850.98% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 7.40 GOP/s | 3.66 GOP/s | 🔴 -50.51% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 1136.83 µs | 114.93 µs | ⚪ -89.89% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 7.16 µs | 10.96 µs | ⚪ +53.11% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.48 GB/s | 17.38 GB/s | 🔴 -46.50% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 29.14 µs | 1168.75 µs | ⚪ +3910.14% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.41 GOP/s | 2.90 GOP/s | 🔴 -46.50% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 343.87 µs | 474.75 µs | ⚪ +38.06% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 3.87 µs | 4.51 µs | ⚪ +16.71% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 661.15 µs | 269.69 µs | ⚪ -59.21% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 417.24 µs | 751.80 µs | ⚪ +80.19% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 97.85 µs | 106.91 µs | ⚪ +9.26% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 608.30 µs | 250.56 µs | ⚪ -58.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 393.89 µs | 182.19 µs | ⚪ -53.75% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 10.08 GB/s | 27.43 GB/s | 🟢 +172.10% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3330.51 µs | 1224.00 µs | 🟢 -63.25% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 187.60 µs | 6.22 µs | ⚪ -96.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 10.07 GOP/s | 27.41 GOP/s | 🟢 +172.10% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1168.82 µs | 1020.23 µs | ⚪ -12.71% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 676.48 µs | 323.46 µs | ⚪ -52.18% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 13.22 µs | 11.35 µs | ⚪ -14.17% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 325.76 µs | 226.25 µs | ⚪ -30.55% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 89.36 µs | 96.58 µs | ⚪ +8.08% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 85.71 µs | 104.25 µs | ⚪ +21.64% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 76.23 µs | 102.85 µs | ⚪ +34.92% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 9.68 µs | 15.82 µs | ⚪ +63.42% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 16.94 µs | 30.48 µs | ⚪ +79.94% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 397.51 µs | 249.78 µs | ⚪ -37.16% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 352.38 µs | 385.76 µs | ⚪ +9.47% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 418.69 µs | 466.00 µs | ⚪ +11.30% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 224.63 µs | 293.62 µs | ⚪ +30.72% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 72.17 µs | 45.95 µs | ⚪ -36.33% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Bandwidth` | 2.63 GB/s | 26.06 GB/s | 🟢 +889.34% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency` | 3188.02 µs | 322.24 µs | 🟢 -89.89% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 105.13 µs | 13.79 µs | ⚪ -86.88% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Throughput` | 1.97 GOP/s | 19.52 GOP/s | 🟢 +889.34% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 341.66 µs | 164.18 µs | ⚪ -51.94% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.39 GB/s | 10.21 GB/s | 🔴 -64.03% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1182.39 µs | 3287.07 µs | 🔴 +178.00% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 11.56 µs | 332.35 µs | ⚪ +2774.51% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.09 GOP/s | 2.55 GOP/s | 🔴 -64.03% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 14.68 µs | 18.80 µs | ⚪ +28.09% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Bandwidth` | 0.10 GB/s | 0.09 GB/s | 🔴 -6.83% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency` | 8402.33 µs | 9018.06 µs | 🔴 +7.33% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 24.64 µs | 299.53 µs | ⚪ +1115.57% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Throughput` | 2.50 GOP/s | 2.33 GOP/s | 🔴 -6.83% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 231.17 µs | 896.59 µs | ⚪ +287.86% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.87 µs | 8.47 µs | ⚪ -22.08% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.50 GB/s | 2.81 GB/s | 🔴 -56.72% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1289.81 µs | 2980.12 µs | 🔴 +131.05% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 5.79 µs | 457.60 µs | ⚪ +7808.68% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.63 GOP/s | 0.70 GOP/s | 🔴 -56.72% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.70 GB/s | 29.54 GB/s | 🟢 +176.10% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3135.83 µs | 1135.77 µs | 🟢 -63.78% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 723.86 µs | 19.60 µs | ⚪ -97.29% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.68 GOP/s | 7.39 GOP/s | 🟢 +176.10% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.57 GB/s | 0.49 GB/s | 🔴 -68.89% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1338.70 µs | 4302.81 µs | 🔴 +221.42% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 226.49 µs | 38.00 µs | ⚪ -83.22% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 58.00 µs | 944.40 µs | ⚪ +1528.30% |

