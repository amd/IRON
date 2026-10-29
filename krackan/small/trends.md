# Performance trends

**Operators added:** `programming_guide`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.36 | 8.60 | 🔴 +263.76% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 1.14 | 3.40 | 🔴 +199.03% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.32 | 7.93 | 🔴 +138.76% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Bandwidth` | 50.16 | 44.30 | 🔴 -11.69% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency` | 62.91 | 71.24 | 🔴 +13.23% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.37 | 0.97 | 🟢 -29.57% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Throughput` | 125.00 | 110.39 | 🔴 -11.69% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.65 | 3.48 | 🔴 +31.38% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.66 | 13.45 | 🔴 +406.44% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.19 | 0.11 | 🔴 -40.35% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 10.36 | 17.37 | 🔴 +67.65% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.11 | 5.55 | 🔴 +399.15% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 0.92 | 1.17 | 🔴 +26.63% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.93 | 12.86 | 🟢 +44.05% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2818.70 | 1956.74 | 🟢 -30.58% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 14.29 | 7.35 | 🟢 -48.54% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 6094.96 | 8779.83 | 🟢 +44.05% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 0.92 | 4.44 | 🔴 +383.50% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.46 | 4.79 | 🔴 +38.47% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.21 | 2.59 | 🔴 +16.78% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.10 | 17.54 | 🔴 +1498.04% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 1.18 | 8.10 | 🔴 +584.90% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.15 | 4.63 | 🔴 +114.85% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 4.12 | 5.79 | 🔴 +40.63% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.12 | 6.47 | 🟢 -9.15% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency` | 30378.13 | 31933.59 | 🔴 +5.12% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 14.89 | 53.64 | 🔴 +260.19% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 4.76 | 3.99 | 🟢 -16.11% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 | 0.18 | 🟢 +9.94% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 97.76 | 88.92 | 🟢 -9.04% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.42 | 5.47 | 🔴 +125.59% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.77 | 0.70 | 🔴 -9.62% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 66.39 | 73.45 | 🔴 +10.64% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.25 | 7.48 | 🔴 +130.21% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.79 | 4.51 | 🔴 +61.61% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.93 | 3.94 | 🔴 +103.62% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 14.13 | 31.08 | 🔴 +119.94% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 131.34 | 3.37 | 🟢 -97.44% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency` | 142.25 | 149.70 | 🔴 +5.24% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.35 | 1.60 | 🟢 -52.24% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 25.96 | 12.98 | 🟢 -50.01% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.02 | 2.56 | 🟢 -78.71% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.09 | 1.21 | 🔴 +10.53% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 1.94 | 9.19 | 🔴 +374.06% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 20.11 | 12.98 | 🟢 -35.47% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.16 | 3.20 | 🔴 +176.66% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 0.97 | 4.54 | 🔴 +369.86% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 15.62 | 3.18 | 🟢 -79.64% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Bandwidth` | 47.94 | 44.64 | 🔴 -6.89% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency` | 521.51 | 560.11 | 🔴 +7.40% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Throughput` | 148.28 | 138.07 | 🔴 -6.89% |

