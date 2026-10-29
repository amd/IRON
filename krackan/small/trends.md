# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 2.16 | 4.45 | 🔴 +105.57% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 2.65 | 5.92 | 🔴 +123.29% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.56 | 5.68 | 🔴 +24.38% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.27 | 18.53 | 🔴 +1361.44% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.95 | 2.00 | 🟢 -81.75% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 0.76 | 2.26 | 🔴 +198.48% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.35 | 13.61 | 🔴 +910.06% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.37 | 12.89 | 🟢 +54.05% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 3007.59 | 1952.30 | 🟢 -35.09% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 53.44 | 6.98 | 🟢 -86.94% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5712.16 | 8799.82 | 🟢 +54.05% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.66 | 13.71 | 🔴 +274.29% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.15 | 4.18 | 🔴 +32.80% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 10.20 | 3.53 | 🟢 -65.44% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 13.32 | 4.03 | 🟢 -69.75% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.36 | 12.88 | 🔴 +283.35% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.81 | 2.81 | 🟢 -68.09% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 9.24 | 8.07 | 🟢 -12.64% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 198.78 | 4.74 | 🟢 -97.62% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 27.64 | 144.15 | 🔴 +421.49% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.12 | 2.97 | 🔴 +40.45% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.49 | 6.01 | 🔴 +302.65% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.25 | 1.07 | 🟢 -52.42% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.41 | 6.11 | 🟢 -17.62% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.14 | 2.97 | 🟢 -42.25% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.38 | 2.13 | 🟢 -10.32% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 8.41 | 21.81 | 🔴 +159.21% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.53 | 0.87 | 🟢 -43.12% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.48 | 1.94 | 🔴 +31.46% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.34 | 5.70 | 🔴 +6.56% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.22 | 8.30 | 🔴 +274.35% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 0.83 | 0.77 | 🟢 -7.22% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.06 | 7.52 | 🟢 -6.70% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.27 | 6.17 | 🔴 +17.11% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 0.76 | 3.06 | 🔴 +304.29% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.64 | 2.29 | 🟢 -37.00% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.71 | 4.77 | 🔴 +28.77% |
| `flm/layer` | `gemma4_e2b-global-700` | `Bandwidth` | 41.91 | 44.20 | 🟢 +5.46% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency` | 723.90 | 686.43 | 🟢 -5.18% |
| `flm/layer` | `gemma4_e2b-global-700` | `Throughput` | 136.45 | 143.90 | 🟢 +5.46% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 9.90 | 5.50 | 🔴 -44.45% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 953.03 | 1715.71 | 🔴 +80.03% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 2257.72 | 1254.10 | 🔴 -44.45% |

