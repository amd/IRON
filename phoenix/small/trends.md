# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 32.37 GB/s | 14.81 GB/s | 🔴 -54.25% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 1555.11 µs | 3399.06 µs | 🔴 +118.57% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 10.37 µs | 461.86 µs | ⚪ +4353.85% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 10.79 GOP/s | 4.94 GOP/s | 🔴 -54.25% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Bandwidth` | 10.31 GB/s | 28.18 GB/s | 🟢 +173.30% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency` | 3253.99 µs | 1190.63 µs | 🟢 -63.41% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 244.03 µs | 120.62 µs | ⚪ -50.57% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Throughput` | 2.58 GOP/s | 7.05 GOP/s | 🟢 +173.30% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Bandwidth` | 5.37 GB/s | 15.77 GB/s | 🟢 +193.36% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3121.86 µs | 1064.16 µs | 🟢 -65.91% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 244.27 µs | 25.73 µs | ⚪ -89.47% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 26.75 µs | 14.57 µs | ⚪ -45.55% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.69 GB/s | 32.37 GB/s | 🟢 +93.90% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3015.08 µs | 1554.98 µs | 🟢 -48.43% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 516.29 µs | 49.95 µs | ⚪ -90.32% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.78 GOP/s | 5.39 GOP/s | 🟢 +93.90% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 604.56 µs | 322.45 µs | ⚪ -46.66% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 7.78 µs | 4.81 µs | ⚪ -38.18% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 310.95 µs | 285.32 µs | ⚪ -8.24% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 1055.98 µs | 491.37 µs | ⚪ -53.47% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 260.86 µs | 132.76 µs | ⚪ -49.11% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.82 GB/s | 10.05 GB/s | 🔴 -36.49% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2122.17 µs | 3341.69 µs | 🔴 +57.47% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 36.86 µs | 338.40 µs | ⚪ +818.09% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.81 GOP/s | 10.04 GOP/s | 🔴 -36.49% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 170.15 µs | 667.52 µs | ⚪ +292.31% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Bandwidth` | 26.89 GB/s | 10.13 GB/s | 🔴 -62.34% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency` | 1248.61 µs | 3315.14 µs | 🔴 +165.51% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 10.18 µs | 386.91 µs | ⚪ +3699.04% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Throughput` | 26.87 GOP/s | 10.12 GOP/s | 🔴 -62.34% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 27.82 GB/s | 10.17 GB/s | 🔴 -63.43% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1206.48 µs | 3299.10 µs | 🔴 +173.45% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 29.14 µs | 266.67 µs | ⚪ +815.00% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 41.72 GOP/s | 15.26 GOP/s | 🔴 -63.43% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.70 GB/s | 10.81 GB/s | 🔴 -63.61% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.88 µs | 3104.53 µs | 🔴 +174.77% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 54.21 µs | 409.60 µs | ⚪ +655.54% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.55 GOP/s | 16.21 GOP/s | 🔴 -63.61% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 624.43 µs | 530.77 µs | ⚪ -15.00% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 219.53 µs | 274.11 µs | ⚪ +24.86% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 120.02 µs | 162.27 µs | ⚪ +35.20% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.71 µs | 7.28 µs | ⚪ +8.52% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 15.88 µs | 9.49 µs | ⚪ -40.20% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 279.61 µs | 463.35 µs | ⚪ +65.71% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.62 GB/s | 29.53 GB/s | 🟢 +178.06% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3159.32 µs | 1136.22 µs | 🟢 -64.04% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 513.11 µs | 6.98 µs | ⚪ -98.64% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 10.62 GOP/s | 29.53 GOP/s | 🟢 +178.06% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.68 GB/s | 29.17 GB/s | 🟢 +173.03% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3140.51 µs | 1150.26 µs | 🟢 -63.37% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 338.59 µs | 29.91 µs | ⚪ -91.17% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.67 GOP/s | 7.29 GOP/s | 🟢 +173.03% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 278.65 µs | 238.41 µs | ⚪ -14.44% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 111.70 µs | 26.46 µs | ⚪ -76.31% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 12.56 µs | 11.11 µs | ⚪ -11.53% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.28 GB/s | 28.36 GB/s | 🟢 +175.88% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3264.95 µs | 1183.46 µs | 🟢 -63.75% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 289.90 µs | 18.43 µs | ⚪ -93.64% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.57 GOP/s | 7.09 GOP/s | 🟢 +175.88% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 28.40 GB/s | 10.05 GB/s | 🔴 -64.60% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1181.93 µs | 3339.18 µs | 🔴 +182.52% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 24.98 µs | 245.06 µs | ⚪ +880.97% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 7.10 GOP/s | 2.51 GOP/s | 🔴 -64.60% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 24.08 µs | 33.15 µs | ⚪ +37.67% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 537.18 µs | 115.21 µs | ⚪ -78.55% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 434.19 µs | 343.07 µs | ⚪ -20.99% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 583.24 µs | 545.56 µs | ⚪ -6.46% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 6.47 GB/s | 2.63 GB/s | 🔴 -59.41% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 1296.61 µs | 3194.30 µs | 🔴 +146.36% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 16.22 µs | 131.44 µs | ⚪ +710.60% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 1.62 GOP/s | 0.66 GOP/s | 🔴 -59.41% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.58 GB/s | 27.91 GB/s | 🟢 +163.78% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3170.87 µs | 1202.11 µs | 🟢 -62.09% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 295.29 µs | 177.68 µs | ⚪ -39.83% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.65 GOP/s | 6.98 GOP/s | 🟢 +163.78% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 0.49 GB/s | 1.55 GB/s | 🟢 +219.63% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 4323.22 µs | 1352.59 µs | 🟢 -68.71% |

