# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 8.60 | 2.16 | 🟢 -74.84% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.40 | 2.65 | 🟢 -22.11% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 7.93 | 4.56 | 🟢 -42.45% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 0.97 | 1.27 | 🔴 +31.13% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.48 | 1.97 | 🟢 -43.33% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 13.45 | 10.95 | 🟢 -18.56% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.55 | 0.76 | 🟢 -86.36% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.17 | 1.35 | 🔴 +15.42% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 12.86 | 8.37 | 🔴 -34.94% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 1956.74 | 3007.59 | 🔴 +53.70% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 7.35 | 53.44 | 🔴 +626.71% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 8779.83 | 5712.16 | 🔴 -34.94% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 4.44 | 3.66 | 🟢 -17.49% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 4.79 | 3.15 | 🟢 -34.38% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.59 | 10.20 | 🔴 +294.74% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 17.54 | 13.32 | 🟢 -24.08% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.10 | 3.36 | 🟢 -58.48% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.63 | 8.81 | 🔴 +90.25% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.79 | 9.24 | 🔴 +59.61% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.47 | 198.78 | 🔴 +2971.14% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 53.64 | 27.64 | 🟢 -48.47% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.99 | 2.12 | 🟢 -47.03% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 | 0.17 | 🔴 -8.49% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 88.92 | 97.16 | 🔴 +9.27% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 5.47 | 1.49 | 🟢 -72.71% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.49 | 2.25 | 🔴 +51.48% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.51 | 5.14 | 🔴 +14.09% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.94 | 2.38 | 🟢 -39.56% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 31.08 | 8.41 | 🟢 -72.93% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 3.37 | 1.53 | 🟢 -54.46% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.60 | 1.48 | 🟢 -7.51% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 12.98 | 5.34 | 🟢 -58.82% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.56 | 2.22 | 🟢 -13.34% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.21 | 0.83 | 🟢 -31.18% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.19 | 8.06 | 🟢 -12.26% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 12.98 | 5.27 | 🟢 -59.43% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 3.20 | 0.76 | 🟢 -76.35% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.54 | 3.64 | 🟢 -19.84% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 3.18 | 3.71 | 🔴 +16.55% |
| `flm/layer` | `gemma4_e2b-global-700` | `Bandwidth` | 44.63 | 41.91 | 🔴 -6.10% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency` | 679.74 | 723.90 | 🔴 +6.50% |
| `flm/layer` | `gemma4_e2b-global-700` | `Throughput` | 145.32 | 136.45 | 🔴 -6.10% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 5.54 | 9.90 | 🟢 +78.79% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 1703.89 | 953.03 | 🟢 -44.07% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 1262.80 | 2257.72 | 🟢 +78.79% |

