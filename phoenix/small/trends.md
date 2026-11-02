# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 15.46 GB/s | 32.37 GB/s | 🟢 +109.31% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3254.94 µs | 1555.11 µs | 🟢 -52.22% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 504.02 µs | 10.37 µs | ⚪ -97.94% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.15 GOP/s | 10.79 GOP/s | 🟢 +109.31% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 15.80 GB/s | 10.31 GB/s | 🔴 -34.72% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 2124.20 µs | 3253.99 µs | 🔴 +53.19% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1061.47 µs | 244.03 µs | ⚪ -77.01% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 3.95 GOP/s | 2.58 GOP/s | 🔴 -34.72% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 15.49 GB/s | 5.37 GB/s | 🔴 -65.31% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 1082.89 µs | 3121.86 µs | 🔴 +188.29% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 31.72 µs | 244.27 µs | ⚪ +669.97% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 6.15 µs | 26.75 µs | ⚪ +335.19% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 31.93 GB/s | 16.69 GB/s | 🔴 -47.71% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1576.46 µs | 3015.08 µs | 🔴 +91.26% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 33.66 µs | 516.29 µs | ⚪ +1433.94% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.32 GOP/s | 2.78 GOP/s | 🔴 -47.71% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.34 GB/s | 13.40 GB/s | 🔴 -17.97% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3080.62 µs | 3755.54 µs | 🔴 +21.91% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 290.37 µs | 604.56 µs | ⚪ +108.21% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.72 GOP/s | 2.23 GOP/s | 🔴 -17.97% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.11 GB/s | 0.08 GB/s | 🔴 -26.34% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 17.29 µs | 23.47 µs | 🔴 +35.76% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 1.92 µs | 7.78 µs | ⚪ +305.47% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.96 GB/s | 9.90 GB/s | 🔴 -9.61% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3062.44 µs | 3387.85 µs | 🔴 +10.63% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 487.55 µs | 310.95 µs | ⚪ -36.22% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.74 GOP/s | 2.48 GOP/s | 🔴 -9.61% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 3.22 GB/s | 2.93 GB/s | 🔴 -8.83% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 7817.44 µs | 8574.47 µs | 🔴 +9.68% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 253.16 µs | 1055.98 µs | ⚪ +317.13% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 2197.63 GOP/s | 2003.61 GOP/s | 🔴 -8.83% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 13.15 GB/s | 11.78 GB/s | 🔴 -10.41% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 2873.52 µs | 3207.28 µs | 🔴 +11.62% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 57.06 µs | 260.86 µs | ⚪ +357.19% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 13.14 GOP/s | 11.77 GOP/s | 🔴 -10.41% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 10.91 GB/s | 15.82 GB/s | 🟢 +44.95% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 3076.13 µs | 2122.17 µs | 🟢 -31.01% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 253.41 µs | 36.86 µs | ⚪ -85.45% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 10.91 GOP/s | 15.81 GOP/s | 🟢 +44.95% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 403.00 µs | 170.15 µs | ⚪ -57.78% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 10.31 GB/s | 26.89 GB/s | 🟢 +160.86% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3257.16 µs | 1248.61 µs | 🟢 -61.67% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 263.37 µs | 10.18 µs | ⚪ -96.13% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 10.30 GOP/s | 26.87 GOP/s | 🟢 +160.86% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 9.90 GB/s | 27.82 GB/s | 🟢 +180.95% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3389.56 µs | 1206.48 µs | 🟢 -64.41% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 281.91 µs | 29.14 µs | ⚪ -89.66% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 14.85 GOP/s | 41.72 GOP/s | 🟢 +180.95% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.38 GB/s | 29.70 GB/s | 🟢 +186.06% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3232.14 µs | 1129.88 µs | 🟢 -65.04% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 336.52 µs | 54.21 µs | ⚪ -83.89% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 15.57 GOP/s | 44.55 GOP/s | 🟢 +186.06% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 6.80 GB/s | 7.22 GB/s | 🟢 +6.27% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 3084.82 µs | 2902.81 µs | 🟢 -5.90% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 200.59 µs | 624.43 µs | ⚪ +211.29% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.42 GOP/s | 0.45 GOP/s | 🟢 +6.27% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 163.62 µs | 120.02 µs | ⚪ -26.65% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 205.53 µs | 165.75 µs | ⚪ -19.35% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 7.95 µs | 6.71 µs | ⚪ -15.57% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.43 GB/s | 0.41 GB/s | 🔴 -6.39% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 118.30 µs | 126.38 µs | 🔴 +6.82% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.42 µs | 15.88 µs | ⚪ +113.98% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.27 GB/s | 10.13 GB/s | 🔴 -64.17% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1187.34 µs | 3313.41 µs | 🔴 +179.06% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 21.51 µs | 279.61 µs | ⚪ +1199.85% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 28.26 GOP/s | 10.13 GOP/s | 🔴 -64.17% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 418.85 µs | 513.11 µs | ⚪ +22.50% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.77 GB/s | 10.68 GB/s | 🔴 -64.12% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1126.96 µs | 3140.51 µs | 🔴 +178.67% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.32 µs | 338.59 µs | ⚪ +3181.35% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.44 GOP/s | 2.67 GOP/s | 🔴 -64.12% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 134.22 µs | 111.70 µs | ⚪ -16.78% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 21.87 µs | 12.56 µs | ⚪ -42.57% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 29.08 GB/s | 10.28 GB/s | 🔴 -64.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1154.34 µs | 3264.95 µs | 🔴 +182.84% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 45.80 µs | 289.90 µs | ⚪ +533.04% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.27 GOP/s | 2.57 GOP/s | 🔴 -64.64% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 8.45 µs | 24.98 µs | ⚪ +195.62% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 35.03 µs | 24.08 µs | ⚪ -31.26% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Bandwidth` | 0.09 GB/s | 0.09 GB/s | 🟢 +5.56% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency` | 9299.08 µs | 8809.58 µs | 🟢 -5.26% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 435.25 µs | 537.18 µs | ⚪ +23.42% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Throughput` | 2.26 GOP/s | 2.38 GOP/s | 🟢 +5.56% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 11.33 GB/s | 10.68 GB/s | 🔴 -5.74% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 2960.41 µs | 3140.67 µs | 🔴 +6.09% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 315.43 µs | 434.19 µs | ⚪ +37.65% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.83 GOP/s | 2.67 GOP/s | 🔴 -5.74% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.62 GB/s | 11.04 GB/s | 🔴 -62.75% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1132.65 µs | 3040.35 µs | 🔴 +168.43% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 20.15 µs | 583.24 µs | ⚪ +2794.69% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.41 GOP/s | 2.76 GOP/s | 🔴 -62.75% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.57 GB/s | 6.47 GB/s | 🟢 +152.00% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3267.41 µs | 1296.61 µs | 🟢 -60.32% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 101.25 µs | 16.22 µs | ⚪ -83.98% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.64 GOP/s | 1.62 GOP/s | 🟢 +152.00% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 9.51 GB/s | 10.58 GB/s | 🟢 +11.27% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3528.14 µs | 3170.87 µs | 🟢 -10.13% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 123.06 µs | 295.29 µs | ⚪ +139.95% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.38 GOP/s | 2.65 GOP/s | 🟢 +11.27% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.25 GB/s | 0.49 GB/s | 🔴 -61.16% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1679.07 µs | 4323.22 µs | 🔴 +157.48% |

