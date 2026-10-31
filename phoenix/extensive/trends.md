# Performance trends

**Operators added:** `merge_results`

**Operators dropped:** `pre_push_hook`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 15.86 GB/s | 14.83 GB/s | 🔴 -6.50% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 3173.00 µs | 3393.41 µs | 🔴 +6.95% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 438.64 µs | 1070.94 µs | ⚪ +144.15% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.29 GOP/s | 4.94 GOP/s | 🔴 -6.50% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.31 GB/s | 11.00 GB/s | 🟢 +6.62% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3253.76 µs | 3051.70 µs | 🟢 -6.21% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 362.01 µs | 458.77 µs | ⚪ +26.73% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.58 GOP/s | 2.75 GOP/s | 🟢 +6.62% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.61 GB/s | 15.77 GB/s | 🟢 +180.96% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 2989.70 µs | 1064.10 µs | 🟢 -64.41% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 409.03 µs | 3.13 µs | ⚪ -99.24% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 27.53 µs | 41.23 µs | ⚪ +49.76% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.10 GB/s | 15.26 GB/s | 🔴 -52.47% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1568.07 µs | 3298.97 µs | 🔴 +110.38% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 19.99 µs | 537.25 µs | ⚪ +2587.94% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.35 GOP/s | 2.54 GOP/s | 🔴 -52.47% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 15.48 GB/s | 32.28 GB/s | 🟢 +108.52% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3251.40 µs | 1559.26 µs | 🟢 -52.04% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 645.54 µs | 23.02 µs | ⚪ -96.43% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.58 GOP/s | 5.38 GOP/s | 🟢 +108.52% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 1.52 µs | 4.29 µs | ⚪ +182.77% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 447.50 µs | 558.53 µs | ⚪ +24.81% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 3.07 GB/s | 3.26 GB/s | 🟢 +6.20% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 8199.72 µs | 7720.94 µs | 🟢 -5.84% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 502.62 µs | 325.86 µs | ⚪ -35.17% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 2095.18 GOP/s | 2225.10 GOP/s | 🟢 +6.20% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Bandwidth` | 13.14 GB/s | 10.93 GB/s | 🔴 -16.81% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency` | 2875.61 µs | 3456.61 µs | 🔴 +20.20% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 95.10 µs | 479.46 µs | ⚪ +404.17% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Throughput` | 13.13 GOP/s | 10.92 GOP/s | 🔴 -16.81% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.69 GB/s | 9.58 GB/s | 🔴 -38.91% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2139.96 µs | 3503.02 µs | 🔴 +63.70% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 13.75 µs | 120.05 µs | ⚪ +773.01% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.68 GOP/s | 9.58 GOP/s | 🔴 -38.91% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 346.18 µs | 118.21 µs | ⚪ -65.85% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 21.70 GB/s | 12.64 GB/s | 🔴 -41.75% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1547.37 µs | 2656.58 µs | 🔴 +71.68% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 486.63 µs | 857.18 µs | ⚪ +76.15% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 21.68 GOP/s | 12.63 GOP/s | 🔴 -41.75% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 81.18 µs | 5.25 µs | ⚪ -93.54% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 30.13 GB/s | 25.44 GB/s | 🔴 -15.57% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1113.56 µs | 1318.90 µs | 🔴 +18.44% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.51 µs | 212.22 µs | ⚪ +2724.09% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 45.20 GOP/s | 38.16 GOP/s | 🔴 -15.57% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 18.97 GB/s | 6.55 GB/s | 🔴 -65.44% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 1105.75 µs | 3199.83 µs | 🔴 +189.38% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 174.33 µs | 207.41 µs | ⚪ +18.98% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.19 GOP/s | 0.41 GOP/s | 🔴 -65.44% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 66.13 µs | 94.16 µs | ⚪ +42.39% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 69.28 µs | 133.31 µs | ⚪ +92.42% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 51.86 µs | 34.24 µs | ⚪ -33.97% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.20 GB/s | 0.19 GB/s | 🔴 -6.61% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 82.58 µs | 88.42 µs | 🔴 +7.08% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 4.30 µs | 15.49 µs | ⚪ +260.03% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 12.69 µs | 11.47 µs | ⚪ -9.63% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 11.50 GB/s | 28.27 GB/s | 🟢 +145.89% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 2919.37 µs | 1187.26 µs | 🟢 -59.33% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 838.07 µs | 23.96 µs | ⚪ -97.14% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 11.49 GOP/s | 28.26 GOP/s | 🟢 +145.89% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.73 µs | 16.63 µs | ⚪ +510.20% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 79.96 µs | 14.60 µs | ⚪ -81.74% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 87.80 µs | 181.80 µs | ⚪ +107.07% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.61 GB/s | 18.61 GB/s | 🟢 +75.35% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3163.13 µs | 1803.86 µs | 🟢 -42.97% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 354.01 µs | 734.36 µs | ⚪ +107.44% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.65 GOP/s | 4.65 GOP/s | 🟢 +75.35% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.66 GB/s | 13.63 GB/s | 🟢 +27.89% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3148.63 µs | 2462.01 µs | 🟢 -21.81% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 318.43 µs | 915.49 µs | ⚪ +187.50% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.66 GOP/s | 3.41 GOP/s | 🟢 +27.89% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 13.56 µs | 24.65 µs | ⚪ +81.76% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 191.97 µs | 483.60 µs | ⚪ +151.92% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 10.13 GB/s | 11.98 GB/s | 🟢 +18.32% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3314.00 µs | 2800.78 µs | 🟢 -15.49% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 197.52 µs | 902.93 µs | ⚪ +357.13% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.53 GOP/s | 3.00 GOP/s | 🟢 +18.32% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 21.17 GB/s | 19.88 GB/s | 🔴 -6.08% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1585.32 µs | 1687.88 µs | 🔴 +6.47% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 523.92 µs | 713.76 µs | ⚪ +36.24% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 5.29 GOP/s | 4.97 GOP/s | 🔴 -6.08% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 86.35 µs | 4.51 µs | ⚪ -94.78% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.60 GB/s | 11.19 GB/s | 🟢 +5.58% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3165.10 µs | 2997.89 µs | 🟢 -5.28% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 327.81 µs | 706.32 µs | ⚪ +115.47% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.65 GOP/s | 2.80 GOP/s | 🟢 +5.58% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 1.28 GB/s | 0.50 GB/s | 🔴 -61.12% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 1638.73 µs | 4215.24 µs | 🔴 +157.23% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 261.74 µs | 311.42 µs | ⚪ +18.98% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Bandwidth` | 4.06 GB/s | 3.24 GB/s | 🔴 -20.06% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency` | 4135.40 µs | 5173.09 µs | 🔴 +25.09% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 258.95 µs | 1018.61 µs | ⚪ +293.36% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Throughput` | 2077.17 GOP/s | 1660.50 GOP/s | 🔴 -20.06% |

