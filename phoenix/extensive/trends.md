# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 17.02 GB/s | 32.09 GB/s | 🟢 +88.49% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency` | 2956.57 µs | 1568.53 µs | 🟢 -46.95% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 554.49 µs | 39.39 µs | ⚪ -92.90% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.67 GOP/s | 10.70 GOP/s | 🟢 +88.49% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 984.35 µs | 303.40 µs | ⚪ -69.18% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency` | 3282.38 µs | 1518.07 µs | 🟢 -53.75% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 196.54 µs | 619.74 µs | ⚪ +215.33% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 10.24 µs | 18.44 µs | ⚪ +80.10% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 16.36 GB/s | 32.18 GB/s | 🟢 +96.65% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 3075.74 µs | 1564.06 µs | 🟢 -49.15% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 577.02 µs | 7.53 µs | ⚪ -98.69% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 2.73 GOP/s | 5.36 GOP/s | 🟢 +96.65% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 324.75 µs | 469.24 µs | ⚪ +44.49% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 5.14 µs | 11.27 µs | ⚪ +119.41% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 639.88 µs | 376.55 µs | ⚪ -41.15% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 540.56 µs | 641.86 µs | ⚪ +18.74% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 82.70 µs | 53.74 µs | ⚪ -35.02% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Bandwidth` | 15.78 GB/s | 11.48 GB/s | 🔴 -27.21% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency` | 2128.10 µs | 2923.69 µs | 🔴 +37.38% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 7.17 µs | 315.36 µs | ⚪ +4299.23% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Throughput` | 15.77 GOP/s | 11.48 GOP/s | 🔴 -27.21% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 200.91 µs | 311.60 µs | ⚪ +55.09% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 278.82 µs | 218.67 µs | ⚪ -21.57% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 257.40 µs | 273.42 µs | ⚪ +6.22% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.72 GB/s | 9.86 GB/s | 🔴 -66.81% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1129.09 µs | 3401.85 µs | 🔴 +201.29% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 13.49 µs | 512.54 µs | ⚪ +3700.56% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 44.58 GOP/s | 14.80 GOP/s | 🔴 -66.81% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 21.24 GB/s | 6.63 GB/s | 🔴 -68.78% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 987.51 µs | 3163.46 µs | 🔴 +220.35% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 12.21 µs | 404.61 µs | ⚪ +3213.09% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 1.33 GOP/s | 0.41 GOP/s | 🔴 -68.78% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 174.01 µs | 138.11 µs | ⚪ -20.63% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 76.45 µs | 114.47 µs | ⚪ +49.73% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 196.26 µs | 78.72 µs | ⚪ -59.89% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 314.25 µs | 161.05 µs | ⚪ -48.75% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 11.92 µs | 0.82 µs | ⚪ -93.10% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 16.99 µs | 14.76 µs | ⚪ -13.09% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 334.40 µs | 430.25 µs | ⚪ +28.66% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 11.21 GB/s | 29.98 GB/s | 🟢 +167.48% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2993.43 µs | 1119.14 µs | 🟢 -62.61% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 535.13 µs | 49.39 µs | ⚪ -90.77% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 11.21 GOP/s | 29.98 GOP/s | 🟢 +167.48% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 10.24 GB/s | 29.71 GB/s | 🟢 +190.24% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 3278.26 µs | 1129.50 µs | 🟢 -65.55% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 413.55 µs | 17.39 µs | ⚪ -95.79% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 2.56 GOP/s | 7.43 GOP/s | 🟢 +190.24% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 248.40 µs | 275.24 µs | ⚪ +10.81% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 48.77 µs | 225.36 µs | ⚪ +362.11% |
| `RoPE` | `npu1-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 39.24 µs | 20.59 µs | ⚪ -47.52% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 1744.20 µs | 3225.41 µs | 🔴 +84.92% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 663.95 µs | 359.44 µs | ⚪ -45.86% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 692.83 µs | 948.22 µs | ⚪ +36.86% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 11.85 µs | 16.36 µs | ⚪ +38.05% |
| `SelectiveScan` | `npu1-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 206.59 µs | 117.52 µs | ⚪ -43.11% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 10.50 µs | 25.46 µs | ⚪ +142.39% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.77 GB/s | 6.47 GB/s | 🟢 +133.85% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3032.24 µs | 1296.68 µs | 🟢 -57.24% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 239.43 µs | 38.58 µs | ⚪ -83.89% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.69 GOP/s | 1.62 GOP/s | 🟢 +133.85% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 30.03 GB/s | 9.70 GB/s | 🔴 -67.70% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1117.29 µs | 3459.04 µs | 🔴 +209.59% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 49.74 µs | 351.90 µs | ⚪ +607.49% |
| `Tanh` | `npu1-Tanh-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.51 GOP/s | 2.43 GOP/s | 🔴 -67.70% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 134.11 µs | 121.99 µs | ⚪ -9.04% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 285.60 µs | 965.74 µs | ⚪ +238.15% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 695.19 µs | 542.33 µs | ⚪ -21.99% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 667.86 µs | 573.73 µs | ⚪ -14.09% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 739.11 µs | 428.01 µs | ⚪ -42.09% |

