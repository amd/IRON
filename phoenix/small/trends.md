# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 578.91 µs | 608.18 µs | ⚪ +5.06% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.19 GB/s | 15.80 GB/s | 🟢 +204.42% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3232.08 µs | 1061.72 µs | 🟢 -67.15% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 94.09 µs | 20.05 µs | ⚪ -78.69% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 28.31 µs | 21.93 µs | ⚪ -22.56% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 472.71 µs | 393.60 µs | ⚪ -16.74% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 590.80 µs | 362.43 µs | ⚪ -38.65% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 3.38 µs | 7.30 µs | ⚪ +116.27% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 397.96 µs | 231.93 µs | ⚪ -41.72% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 505.07 µs | 202.81 µs | ⚪ -59.84% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 11.64 GB/s | 13.32 GB/s | 🟢 +14.49% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 228.07 µs | 38.66 µs | ⚪ -83.05% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 11.63 GOP/s | 13.31 GOP/s | 🟢 +14.49% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 426.84 µs | 768.89 µs | ⚪ +80.13% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 615.82 µs | 360.42 µs | ⚪ -41.47% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 556.25 µs | 430.84 µs | ⚪ -22.55% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.00 GB/s | 9.66 GB/s | 🔴 -65.50% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1198.49 µs | 3474.30 µs | 🔴 +189.89% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 13.98 µs | 449.94 µs | ⚪ +3119.35% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.00 GOP/s | 14.49 GOP/s | 🔴 -65.50% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.47 GB/s | 10.70 GB/s | 🔴 -63.68% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1138.59 µs | 3134.99 µs | 🔴 +175.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 23.50 µs | 316.67 µs | ⚪ +1247.27% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.21 GOP/s | 16.05 GOP/s | 🔴 -63.68% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.68 GB/s | 21.30 GB/s | 🟢 +218.96% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3140.74 µs | 984.67 µs | 🟢 -68.65% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 127.24 µs | 12.32 µs | ⚪ -90.31% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.42 GOP/s | 1.33 GOP/s | 🟢 +218.96% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 243.79 µs | 179.56 µs | ⚪ -26.35% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Bandwidth` | 0.10 GB/s | 0.11 GB/s | 🟢 +10.12% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency` | 81271.39 µs | 73799.93 µs | 🟢 -9.19% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 90.05 µs | 286.14 µs | ⚪ +217.77% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Throughput` | 422.80 GOP/s | 465.61 GOP/s | 🟢 +10.12% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 515.28 µs | 123.10 µs | ⚪ -76.11% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 51.43 µs | 5.34 µs | ⚪ -89.62% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.14 GB/s | 10.12 GB/s | 🔴 -64.02% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1192.84 µs | 3315.68 µs | 🔴 +177.97% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 47.20 µs | 353.42 µs | ⚪ +648.71% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.13 GOP/s | 10.12 GOP/s | 🔴 -64.02% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.19 µs | 12.78 µs | ⚪ +56.00% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 24.25 µs | 5.40 µs | ⚪ -77.73% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 239.13 µs | 216.38 µs | ⚪ -9.51% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 146.36 µs | 42.82 µs | ⚪ -70.74% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 7.65 µs | 15.29 µs | ⚪ +99.88% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 334.71 µs | 385.91 µs | ⚪ +15.30% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.15 GB/s | 28.47 GB/s | 🟢 +180.61% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3308.07 µs | 1178.87 µs | 🟢 -64.36% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 307.61 µs | 31.02 µs | ⚪ -89.92% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.54 GOP/s | 7.12 GOP/s | 🟢 +180.61% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 9.57 µs | 18.08 µs | ⚪ +88.86% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 228.04 µs | 193.14 µs | ⚪ -15.31% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 11.49 GB/s | 17.86 GB/s | 🟢 +55.46% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 636.37 µs | 206.21 µs | ⚪ -67.60% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.87 GOP/s | 4.46 GOP/s | 🟢 +55.46% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 617.86 µs | 358.48 µs | ⚪ -41.98% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1782.69 µs | 3062.07 µs | 🔴 +71.77% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 569.87 µs | 255.05 µs | ⚪ -55.24% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.13 GB/s | 30.14 GB/s | 🟢 +170.89% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3015.68 µs | 1113.24 µs | 🟢 -63.08% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 310.58 µs | 13.06 µs | ⚪ -95.79% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.78 GOP/s | 7.54 GOP/s | 🟢 +170.89% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.57 GB/s | 1.59 GB/s | 🟢 +178.89% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 3676.55 µs | 1318.29 µs | 🟢 -64.14% |

