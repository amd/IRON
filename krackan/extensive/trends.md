# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 10.16 µs | 4.74 µs | ⚪ -53.30% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 4.35 µs | 6.63 µs | ⚪ +52.42% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.88 µs | 2.86 µs | ⚪ +52.32% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.83 µs | 1.49 µs | ⚪ -18.57% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.37 µs | 11.29 µs | ⚪ +34.88% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.94 µs | 1.87 µs | ⚪ -52.46% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.35 µs | 1.17 µs | ⚪ -13.68% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.93 µs | 0.86 µs | ⚪ -82.61% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 591.14 µs | 28.36 µs | ⚪ -95.20% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 16.98 µs | 13.99 µs | ⚪ -17.59% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 12.94 µs | 3.60 µs | ⚪ -72.20% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 4.94 µs | 17.34 µs | ⚪ +251.11% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 13.82 µs | 1.16 µs | ⚪ -91.63% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.62 µs | 1.80 µs | ⚪ +11.15% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.43 µs | 5.23 µs | ⚪ +17.88% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.95 µs | 1.97 µs | ⚪ -33.00% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.61 µs | 7.00 µs | ⚪ +24.73% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.89 µs | 2.93 µs | ⚪ -24.62% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 84.81 µs | 106.15 µs | ⚪ +25.17% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 137.02 µs | 125.83 µs | ⚪ -8.17% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 5.63 µs | 14.37 µs | ⚪ +155.06% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.11 µs | 1.70 µs | ⚪ +53.48% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.91 µs | 3.59 µs | ⚪ +87.92% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.96 µs | 11.73 µs | ⚪ +196.42% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.79 µs | 7.53 µs | ⚪ -14.29% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.60 µs | 5.17 µs | ⚪ -7.60% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 12.51 µs | 7.63 µs | ⚪ -39.06% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 10.03 µs | 2.06 µs | ⚪ -79.43% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.72 µs | 1.52 µs | ⚪ -11.64% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.87 µs | 4.54 µs | ⚪ -33.96% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.25 µs | 7.35 µs | ⚪ +126.45% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.02 µs | 1.30 µs | ⚪ +28.01% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 7.44 µs | 11.71 µs | ⚪ +57.37% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.71 µs | 4.07 µs | ⚪ -58.05% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.26 µs | 3.08 µs | ⚪ -5.37% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.39 µs | 1.06 µs | ⚪ -55.55% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 10.03 µs | 14.01 µs | ⚪ +39.65% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 35.19 µs | 19.84 µs | ⚪ -43.62% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 0.63 µs | 2.01 µs | ⚪ +218.21% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.02 µs | 10.82 µs | ⚪ +258.83% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.61 µs | 4.80 µs | ⚪ -27.42% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 15.32 µs | 13.24 µs | ⚪ -13.61% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 13.09 µs | 14.69 µs | ⚪ +12.20% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 4.89 µs | 2.64 µs | ⚪ -46.01% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 8.27 µs | 7.14 µs | ⚪ -13.64% |

