# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 14.10 µs | 15.76 µs | ⚪ +11.77% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 9.85 µs | 8.69 µs | ⚪ -11.80% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.63 µs | 3.63 µs | ⚪ -21.61% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.90 µs | 2.47 µs | ⚪ +29.97% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.06 µs | 2.86 µs | ⚪ -64.57% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 12.35 µs | 6.07 µs | ⚪ -50.88% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.85 µs | 1.30 µs | ⚪ -54.33% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.80 µs | 5.67 µs | ⚪ +49.22% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 9.34 µs | 7.65 µs | ⚪ -18.09% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 25.38 µs | 12.46 µs | ⚪ -50.91% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 12.90 µs | 14.91 µs | ⚪ +15.61% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 11.07 µs | 11.81 µs | ⚪ +6.74% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 16.18 µs | 10.96 µs | ⚪ -32.26% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.10 µs | 4.72 µs | ⚪ +15.15% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.11 µs | 3.67 µs | ⚪ -10.63% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.16 µs | 1.50 µs | ⚪ -52.39% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 10.97 µs | 9.51 µs | ⚪ -13.25% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 35.40 µs | 4.34 µs | ⚪ -87.73% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 51.79 µs | 27.72 µs | ⚪ -46.48% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 4.89 µs | 6.67 µs | ⚪ +36.48% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 6.02 µs | 1.08 µs | ⚪ -82.09% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.25 µs | 2.08 µs | ⚪ +66.72% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 6.47 µs | 9.09 µs | ⚪ +40.40% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 15.47 µs | 2.03 µs | ⚪ -86.86% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.44 µs | 6.15 µs | ⚪ +13.19% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 34.27 µs | 41.99 µs | ⚪ +22.52% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 3.45 µs | 0.91 µs | ⚪ -73.75% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.74 µs | 2.05 µs | ⚪ +17.89% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 5.24 µs | 8.73 µs | ⚪ +66.40% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.01 µs | 3.21 µs | ⚪ -64.41% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.87 µs | 1.20 µs | ⚪ -35.88% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 1.52 µs | 10.48 µs | ⚪ +590.05% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.23 µs | 8.13 µs | ⚪ +92.32% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.16 µs | 3.63 µs | ⚪ +67.99% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.86 µs | 1.13 µs | ⚪ -39.34% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.11 µs | 2.37 µs | ⚪ -23.98% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 4.74 GB/s | 5.02 GB/s | 🟢 +5.88% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 442.30 µs | 417.73 µs | 🟢 -5.55% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 31.37 µs | 14.46 µs | ⚪ -53.90% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 27.92 µs | 30.68 µs | ⚪ +9.87% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.57 µs | 3.45 µs | ⚪ -54.50% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.70 µs | 8.23 µs | ⚪ +22.71% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 13.99 µs | 7.08 µs | ⚪ -49.39% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 3.56 µs | 9.95 µs | ⚪ +179.83% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 5.05 µs | 8.51 µs | ⚪ +68.45% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 7.27 µs | 9.36 µs | ⚪ +28.75% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 7.64 µs | 7.23 µs | ⚪ -5.37% |

