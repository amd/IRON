# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Bandwidth` | 16.93 GB/s | 30.54 GB/s | 🟢 +80.33% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1014.66 µs | 102.30 µs | ⚪ -89.92% |
| `AXPY` | `npu1-AXPY-size_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0` | `Throughput` | 5.64 GOP/s | 10.18 GOP/s | 🟢 +80.33% |
| `Clamp` | `npu1-Clamp-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 213.34 µs | 743.37 µs | ⚪ +248.45% |
| `Copy` | `npu1-Copy-bench_flat_4mi` | `Latency MAD` | 1190.65 µs | 322.20 µs | ⚪ -72.94% |
| `DepthwiseConv1d` | `npu1-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_4` | `Latency MAD` | 14.72 µs | 13.31 µs | ⚪ -9.53% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Bandwidth` | 32.10 GB/s | 15.30 GB/s | 🔴 -52.33% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency` | 1567.95 µs | 3288.90 µs | 🔴 +109.76% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 29.21 µs | 582.88 µs | ⚪ +1895.52% |
| `ElementwiseAdd` | `npu1-ElementwiseAdd-size_8388608-num_aie_columns_4-tile_size_4096` | `Throughput` | 5.35 GOP/s | 2.55 GOP/s | 🔴 -52.33% |
| `ElementwiseMul` | `npu1-ElementwiseMul-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 748.36 µs | 245.44 µs | ⚪ -67.20% |
| `Emit` | `npu1-Emit-eight_carried` | `Latency MAD` | 4.25 µs | 5.20 µs | ⚪ +22.27% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 18.13 GB/s | 11.74 GB/s | 🔴 -35.24% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 1850.50 µs | 2857.63 µs | 🔴 +54.43% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.40 µs | 411.18 µs | ⚪ +7514.40% |
| `GELU` | `npu1-GELU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 4.53 GOP/s | 2.94 GOP/s | 🔴 -35.24% |
| `GEMM` | `npu1-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 71.82 µs | 338.42 µs | ⚪ +371.20% |
| `GEMV` | `npu1-GEMV-M_1536-K_12288-num_aie_columns_4-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 13.32 µs | 310.20 µs | ⚪ +2228.07% |
| `GEMV` | `npu1-GEMV-M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 647.97 µs | 14.18 µs | ⚪ -97.81% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 314.01 µs | 1048.92 µs | ⚪ +234.05% |
| `GEMV` | `npu1-GEMV-M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 308.81 µs | 816.06 µs | ⚪ +164.26% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Bandwidth` | 28.29 GB/s | 10.56 GB/s | 🔴 -62.69% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency` | 1186.24 µs | 3179.57 µs | 🔴 +168.04% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 12.47 µs | 526.25 µs | ⚪ +4118.94% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Throughput` | 42.43 GOP/s | 15.83 GOP/s | 🔴 -62.69% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency` | 2830.19 µs | 1501.51 µs | 🟢 -46.95% |
| `LayerNorm` | `npu1-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 626.47 µs | 456.82 µs | ⚪ -27.08% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Bandwidth` | 7.35 GB/s | 20.99 GB/s | 🟢 +185.46% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency` | 2852.71 µs | 999.35 µs | 🟢 -64.97% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Latency MAD` | 687.54 µs | 15.87 µs | ⚪ -97.69% |
| `Limbs` | `npu1-Limbs-rows_4096-line_320-num_aie_columns_4` | `Throughput` | 0.46 GOP/s | 1.31 GOP/s | 🟢 +185.46% |
| `Log` | `npu1-Log-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 262.72 µs | 220.96 µs | ⚪ -15.89% |
| `MHA` | `npu1-MHA-num_heads_1-seq_len_16384-num_pipelines_4` | `Latency MAD` | 88.31 µs | 61.83 µs | ⚪ -29.99% |
| `MHA` | `npu1-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_4` | `Latency MAD` | 128.78 µs | 117.94 µs | ⚪ -8.42% |
| `Magnitude` | `npu1-Magnitude-rows_4096-width_640-num_aie_columns_4` | `Latency MAD` | 71.77 µs | 256.53 µs | ⚪ +257.41% |
| `Merge` | `npu1-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 10.02 µs | 12.48 µs | ⚪ +24.55% |
| `PatchPositions` | `npu1-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 27.79 µs | 11.64 µs | ⚪ -58.11% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 12.19 µs | 89.99 µs | ⚪ +638.07% |
| `RMSNorm` | `npu1-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 312.61 µs | 457.59 µs | ⚪ +46.38% |
| `ReLU` | `npu1-ReLU-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.21 µs | 14.15 µs | ⚪ +15.84% |
| `Resample` | `npu1-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 422.00 µs | 256.86 µs | ⚪ -39.13% |
| `ResampleTaps` | `npu1-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 197.56 µs | 39.07 µs | ⚪ -80.22% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.50 GB/s | 28.24 GB/s | 🟢 +168.99% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3196.46 µs | 1188.31 µs | 🟢 -62.82% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 306.94 µs | 16.95 µs | ⚪ -94.48% |
| `RowwiseAdd` | `npu1-RowwiseAdd-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.62 GOP/s | 7.06 GOP/s | 🟢 +168.99% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Bandwidth` | 10.71 GB/s | 28.66 GB/s | 🟢 +167.63% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency` | 3133.65 µs | 1170.89 µs | 🟢 -62.63% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Latency MAD` | 412.60 µs | 21.17 µs | ⚪ -94.87% |
| `RowwiseMul` | `npu1-RowwiseMul-rows_2048-num_aie_columns_2-num_channels_2-tile_size_4096` | `Throughput` | 2.68 GOP/s | 7.16 GOP/s | 🟢 +167.63% |
| `Sample` | `npu1-Sample-llama` | `Latency MAD` | 11.10 µs | 14.71 µs | ⚪ +32.60% |
| `SiLU` | `npu1-SiLU-size_8388608-num_aie_columns_4-tile_size_4096` | `Latency MAD` | 203.19 µs | 522.68 µs | ⚪ +157.24% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Bandwidth` | 29.67 GB/s | 13.53 GB/s | 🔴 -54.39% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 11.83 µs | 986.38 µs | ⚪ +8236.15% |
| `Sigmoid` | `npu1-Sigmoid-size_8388608-num_aie_columns_4-num_channels_2-tile_size_4096` | `Throughput` | 7.42 GOP/s | 3.38 GOP/s | 🔴 -54.39% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Bandwidth` | 2.74 GB/s | 6.50 GB/s | 🟢 +136.68% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency` | 3056.04 µs | 1291.19 µs | 🟢 -57.75% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 117.47 µs | 11.41 µs | ⚪ -90.29% |
| `Softmax` | `npu1-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Throughput` | 0.69 GOP/s | 1.62 GOP/s | 🟢 +136.68% |
| `flm/gemm` | `npu1-M_1024-K_2560-N_2560-epilogue_none-rounding_conv_even` | `Latency MAD` | 143.18 µs | 255.19 µs | ⚪ +78.22% |
| `flm/gemm` | `npu1-M_2048-K_2048-N_1024-epilogue_none-rounding_conv_even` | `Latency MAD` | 944.38 µs | 887.57 µs | ⚪ -6.02% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 307.20 µs | 555.41 µs | ⚪ +80.80% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 505.40 µs | 559.25 µs | ⚪ +10.65% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 925.63 µs | 1425.63 µs | ⚪ +54.02% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 647.99 µs | 597.09 µs | ⚪ -7.86% |

