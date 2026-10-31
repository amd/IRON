# Performance trends

**Operators added:** `merge_results`

**Operators dropped:** `pre_push_hook`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 309.92 µs | 504.02 µs | ⚪ +62.63% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.54 GB/s | 15.80 GB/s | 🟢 +49.88% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3183.81 µs | 2124.20 µs | 🟢 -33.28% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 373.54 µs | 1061.47 µs | ⚪ +184.16% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.63 GOP/s | 3.95 GOP/s | 🟢 +49.88% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.38 GB/s | 15.49 GB/s | 🟢 +187.91% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3117.78 µs | 1082.89 µs | 🟢 -65.27% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 120.35 µs | 31.72 µs | ⚪ -73.64% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 9.96 µs | 6.15 µs | ⚪ -38.30% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 13.50 GB/s | 31.93 GB/s | 🟢 +136.50% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3728.26 µs | 1576.46 µs | 🟢 -57.72% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 660.44 µs | 33.66 µs | ⚪ -94.90% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.25 GOP/s | 5.32 GOP/s | 🟢 +136.50% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.47 GB/s | 16.34 GB/s | 🟢 +5.61% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3253.49 µs | 3080.62 µs | 🟢 -5.31% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 560.24 µs | 290.37 µs | ⚪ -48.17% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.58 GOP/s | 2.72 GOP/s | 🟢 +5.61% |
| `Emit` | `npu1-Emit-eight_carried` | `Bandwidth` | 0.09 GB/s | 0.11 GB/s | 🟢 +23.59% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency` | 21.37 µs | 17.29 µs | 🟢 -19.09% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 10.68 µs | 1.92 µs | ⚪ -82.03% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 274.26 µs | 487.55 µs | ⚪ +77.77% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 479.06 µs | 253.16 µs | ⚪ -47.16% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 12.30 GB/s | 13.15 GB/s | 🟢 +6.85% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 3070.47 µs | 2873.52 µs | 🟢 -6.41% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 173.22 µs | 57.06 µs | ⚪ -67.06% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 12.29 GOP/s | 13.14 GOP/s | 🟢 +6.85% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 308.84 µs | 253.41 µs | ⚪ -17.95% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Bandwidth` | 9.88 GB/s | 10.53 GB/s | 🟢 +6.57% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency` | 3399.22 µs | 3189.58 µs | 🟢 -6.17% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 354.10 µs | 403.00 µs | ⚪ +13.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Throughput` | 9.87 GOP/s | 10.52 GOP/s | 🟢 +6.57% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 9.77 GB/s | 10.31 GB/s | 🟢 +5.52% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 3437.07 µs | 3257.16 µs | 🟢 -5.23% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 9.76 GOP/s | 10.30 GOP/s | 🟢 +5.52% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 10.89 GB/s | 9.90 GB/s | 🔴 -9.11% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 3080.89 µs | 3389.56 µs | 🔴 +10.02% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 430.63 µs | 281.91 µs | ⚪ -34.53% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 16.34 GOP/s | 14.85 GOP/s | 🔴 -9.11% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 13.95 GB/s | 10.38 GB/s | 🔴 -25.56% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2406.01 µs | 3232.14 µs | 🔴 +34.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1203.26 µs | 336.52 µs | ⚪ -72.03% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 20.92 GOP/s | 15.57 GOP/s | 🔴 -25.56% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.04 GB/s | 6.80 GB/s | 🔴 -67.69% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 996.82 µs | 3084.82 µs | 🔴 +209.47% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 9.77 µs | 200.59 µs | ⚪ +1953.46% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.31 GOP/s | 0.42 GOP/s | 🔴 -67.69% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 288.47 µs | 231.01 µs | ⚪ -19.92% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 38.42 µs | 163.62 µs | ⚪ +325.88% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Bandwidth` | 4.35 GB/s | 4.70 GB/s | 🟢 +8.06% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency` | 3614.91 µs | 3345.44 µs | 🟢 -7.45% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 346.85 µs | 205.53 µs | ⚪ -40.74% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Throughput` | 0.36 GOP/s | 0.39 GOP/s | 🟢 +8.06% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.21 GB/s | 0.20 GB/s | 🔴 -5.84% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 78.40 µs | 83.27 µs | 🔴 +6.21% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.47 µs | 7.95 µs | ⚪ +221.34% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.40 GB/s | 0.43 GB/s | 🟢 +7.00% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 126.58 µs | 118.30 µs | 🟢 -6.54% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 11.02 µs | 7.42 µs | ⚪ -32.65% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 10.08 µs | 21.51 µs | ⚪ +113.32% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.59 GB/s | 10.67 GB/s | 🔴 -63.94% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1134.06 µs | 3145.06 µs | 🔴 +177.33% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.58 µs | 418.85 µs | ⚪ +2772.31% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 29.59 GOP/s | 10.67 GOP/s | 🔴 -63.94% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.71 GB/s | 29.77 GB/s | 🟢 +178.11% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3134.15 µs | 1126.96 µs | 🟢 -64.04% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 771.80 µs | 10.32 µs | ⚪ -98.66% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.68 GOP/s | 7.44 GOP/s | 🟢 +178.11% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 357.27 µs | 284.45 µs | ⚪ -20.38% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 48.08 µs | 134.22 µs | ⚪ +179.16% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.78 µs | 21.87 µs | ⚪ +71.04% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 23.00 GB/s | 29.08 GB/s | 🟢 +26.40% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1459.07 µs | 1154.34 µs | 🟢 -20.88% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 429.91 µs | 45.80 µs | ⚪ -89.35% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 5.75 GOP/s | 7.27 GOP/s | 🟢 +26.40% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 9.93 GB/s | 28.43 GB/s | 🟢 +186.33% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3379.64 µs | 1180.34 µs | 🟢 -65.07% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 185.37 µs | 8.45 µs | ⚪ -95.44% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.48 GOP/s | 7.11 GOP/s | 🟢 +186.33% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 17.19 µs | 35.03 µs | ⚪ +103.75% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 381.52 µs | 435.25 µs | ⚪ +14.08% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.16 GB/s | 11.33 GB/s | 🟢 +11.58% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3303.30 µs | 2960.41 µs | 🟢 -10.38% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 380.12 µs | 315.43 µs | ⚪ -17.02% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.54 GOP/s | 2.83 GOP/s | 🟢 +11.58% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 15.39 GB/s | 29.62 GB/s | 🟢 +92.53% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2180.72 µs | 1132.65 µs | 🟢 -48.06% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1100.79 µs | 20.15 µs | ⚪ -98.17% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 3.85 GOP/s | 7.41 GOP/s | 🟢 +92.53% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3108.11 µs | 3267.41 µs | 🔴 +5.13% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 73.81 µs | 101.25 µs | ⚪ +37.17% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.34 GB/s | 9.51 GB/s | 🔴 -67.58% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1143.82 µs | 3528.14 µs | 🔴 +208.45% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.32 µs | 123.06 µs | ⚪ +759.49% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.33 GOP/s | 2.38 GOP/s | 🔴 -67.58% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.36 GB/s | 1.25 GB/s | 🔴 -8.29% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1539.88 µs | 1679.07 µs | 🔴 +9.04% |

