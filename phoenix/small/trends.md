# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 608.18 µs | 455.84 µs | ⚪ -25.05% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 318.54 µs | 358.66 µs | ⚪ +12.60% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 20.05 µs | 39.07 µs | ⚪ +94.83% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 21.93 µs | 10.15 µs | ⚪ -53.69% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.26 GB/s | 32.41 GB/s | 🟢 +112.39% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3297.92 µs | 1552.76 µs | 🟢 -52.92% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 393.60 µs | 41.83 µs | ⚪ -89.37% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.54 GOP/s | 5.40 GOP/s | 🟢 +112.39% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 17.48 GB/s | 32.40 GB/s | 🟢 +85.32% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2879.30 µs | 1553.66 µs | 🟢 -46.04% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 362.43 µs | 7.84 µs | ⚪ -97.84% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.91 GOP/s | 5.40 GOP/s | 🟢 +85.32% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.30 µs | 7.73 µs | ⚪ +5.83% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 231.93 µs | 384.35 µs | ⚪ +65.72% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 202.81 µs | 516.36 µs | ⚪ +154.60% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 38.66 µs | 21.70 µs | ⚪ -43.86% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 768.89 µs | 343.49 µs | ⚪ -55.33% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 11.01 GB/s | 15.58 GB/s | 🟢 +41.52% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3048.88 µs | 2154.44 µs | 🟢 -29.34% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 360.42 µs | 69.61 µs | ⚪ -80.69% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 11.01 GOP/s | 15.57 GOP/s | 🟢 +41.52% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 430.84 µs | 1180.01 µs | ⚪ +173.89% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 9.66 GB/s | 28.23 GB/s | 🟢 +192.26% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3474.30 µs | 1188.75 µs | 🟢 -65.78% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 449.94 µs | 39.49 µs | ⚪ -91.22% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 14.49 GOP/s | 42.34 GOP/s | 🟢 +192.26% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 316.67 µs | 906.60 µs | ⚪ +186.29% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.30 GB/s | 6.79 GB/s | 🔴 -68.12% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 984.67 µs | 3088.25 µs | 🔴 +213.63% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 12.32 µs | 319.55 µs | ⚪ +2493.03% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.33 GOP/s | 0.42 GOP/s | 🔴 -68.12% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 179.56 µs | 318.20 µs | ⚪ +77.21% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 286.14 µs | 109.02 µs | ⚪ -61.90% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 123.10 µs | 229.21 µs | ⚪ +86.19% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 5.34 µs | 17.82 µs | ⚪ +234.05% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 15.39 µs | 7.55 µs | ⚪ -50.92% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 353.42 µs | 270.65 µs | ⚪ -23.42% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.53 GB/s | 11.80 GB/s | 🔴 -60.05% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.78 µs | 1241.37 µs | ⚪ +9609.97% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.53 GOP/s | 11.80 GOP/s | 🔴 -60.05% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.62 GB/s | 11.03 GB/s | 🔴 -62.75% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1132.88 µs | 3041.12 µs | 🔴 +168.44% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.40 µs | 380.01 µs | ⚪ +6937.89% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.40 GOP/s | 2.76 GOP/s | 🔴 -62.75% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 216.38 µs | 337.06 µs | ⚪ +55.77% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 42.82 µs | 132.80 µs | ⚪ +210.14% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 15.29 µs | 25.42 µs | ⚪ +66.28% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.45 GB/s | 26.21 GB/s | 🟢 +150.78% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3211.17 µs | 1280.45 µs | 🟢 -60.13% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 385.91 µs | 152.17 µs | ⚪ -60.57% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.61 GOP/s | 6.55 GOP/s | 🟢 +150.78% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.47 GB/s | 10.43 GB/s | 🔴 -63.38% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1178.87 µs | 3219.03 µs | 🔴 +173.06% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 31.02 µs | 326.28 µs | ⚪ +951.90% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.12 GOP/s | 2.61 GOP/s | 🔴 -63.38% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 193.14 µs | 322.48 µs | ⚪ +66.97% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 17.86 GB/s | 11.39 GB/s | 🔴 -36.20% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1878.81 µs | 2944.84 µs | 🔴 +56.74% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 206.21 µs | 58.97 µs | ⚪ -71.40% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 4.46 GOP/s | 2.85 GOP/s | 🔴 -36.20% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 358.48 µs | 1325.97 µs | ⚪ +269.89% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 255.05 µs | 236.75 µs | ⚪ -7.18% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.06 µs | 10.72 µs | ⚪ -17.95% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.59 GB/s | 0.48 GB/s | 🔴 -69.66% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1318.29 µs | 4344.56 µs | 🔴 +229.56% |

