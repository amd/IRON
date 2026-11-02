# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 443.41 µs | 581.49 µs | ⚪ +31.14% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 11.34 GB/s | 29.30 GB/s | 🟢 +158.30% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 2957.81 µs | 1145.10 µs | 🟢 -61.29% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 697.28 µs | 45.20 µs | ⚪ -93.52% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.84 GOP/s | 7.33 GOP/s | 🟢 +158.30% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3262.36 µs | 1466.69 µs | 🟢 -55.04% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 124.41 µs | 556.40 µs | ⚪ +347.22% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 344.97 µs | 670.21 µs | ⚪ +94.28% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 712.79 µs | 985.36 µs | ⚪ +38.24% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 2.29 µs | 8.10 µs | ⚪ +252.82% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 15.83 GB/s | 10.74 GB/s | 🔴 -32.15% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2119.90 µs | 3124.59 µs | 🔴 +47.39% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 269.98 µs | 249.93 µs | ⚪ -7.43% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 3.96 GOP/s | 2.68 GOP/s | 🔴 -32.15% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 56.15 µs | 676.64 µs | ⚪ +1105.03% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 10.94 µs | 210.15 µs | ⚪ +1820.85% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 357.21 µs | 705.25 µs | ⚪ +97.43% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 218.97 µs | 364.37 µs | ⚪ +66.40% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 227.19 µs | 296.09 µs | ⚪ +30.33% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1097.77 µs | 175.35 µs | ⚪ -84.03% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.61 GB/s | 29.22 GB/s | 🟢 +175.40% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3162.97 µs | 1148.50 µs | 🟢 -63.69% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 336.17 µs | 64.33 µs | ⚪ -80.87% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 15.91 GOP/s | 43.82 GOP/s | 🟢 +175.40% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.97 GB/s | 21.01 GB/s | 🟢 +201.42% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3008.42 µs | 998.07 µs | 🟢 -66.82% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 304.66 µs | 5.69 µs | ⚪ -98.13% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.44 GOP/s | 1.31 GOP/s | 🟢 +201.42% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 246.41 µs | 206.38 µs | ⚪ -16.24% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 101.87 µs | 48.53 µs | ⚪ -52.36% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 125.80 µs | 149.10 µs | ⚪ +18.52% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 425.69 µs | 5.56 µs | ⚪ -98.69% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.41 µs | 14.30 µs | ⚪ +122.96% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 8.97 µs | 11.68 µs | ⚪ +30.14% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 501.81 µs | 361.32 µs | ⚪ -28.00% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.61 µs | 18.87 µs | ⚪ +185.30% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.54 GB/s | 9.90 GB/s | 🔴 -66.47% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1135.83 µs | 3387.67 µs | 🔴 +198.26% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.67 µs | 288.17 µs | ⚪ +3654.94% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.39 GOP/s | 2.48 GOP/s | 🔴 -66.47% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 184.83 µs | 199.82 µs | ⚪ +8.11% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 46.59 µs | 74.02 µs | ⚪ +58.87% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 13.22 µs | 10.08 µs | ⚪ -23.79% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.53 GB/s | 27.96 GB/s | 🟢 +165.68% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3188.69 µs | 1200.18 µs | 🟢 -62.36% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 327.18 µs | 74.62 µs | ⚪ -77.19% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.63 GOP/s | 6.99 GOP/s | 🟢 +165.68% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 268.74 µs | 1020.55 µs | ⚪ +279.75% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 10.93 µs | 15.06 µs | ⚪ +37.81% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 193.08 µs | 217.60 µs | ⚪ +12.70% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 243.25 µs | 391.95 µs | ⚪ +61.13% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.41 µs | 15.82 µs | ⚪ +192.69% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.49 GB/s | 2.72 GB/s | 🔴 -58.10% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1291.91 µs | 3083.63 µs | 🔴 +138.69% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 4.75 µs | 384.34 µs | ⚪ +7994.00% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.62 GOP/s | 0.68 GOP/s | 🔴 -58.10% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 320.22 µs | 1129.91 µs | ⚪ +252.86% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.63 GB/s | 0.48 GB/s | 🔴 -70.85% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1283.10 µs | 4402.02 µs | 🔴 +243.08% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 388.63 µs | 46.73 µs | ⚪ -87.98% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 930.03 µs | 485.43 µs | ⚪ -47.80% |

