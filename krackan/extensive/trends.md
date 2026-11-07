# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.79 µs | 14.29 µs | ⚪ +276.91% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.36 µs | 2.06 µs | ⚪ +51.64% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.21 µs | 4.97 µs | ⚪ +311.76% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.30 µs | 7.24 µs | ⚪ +214.12% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.47 µs | 12.91 µs | ⚪ +12.58% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.56 µs | 2.43 µs | ⚪ -56.31% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 9.40 µs | 3.10 µs | ⚪ -67.06% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 389.14 µs | 2.33 µs | ⚪ -99.40% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.82 GB/s | 6.73 GB/s | 🔴 -23.66% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2853.76 µs | 3738.07 µs | 🔴 +30.99% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 14.09 µs | 64.13 µs | ⚪ +355.25% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 6020.09 GOP/s | 4595.92 GOP/s | 🔴 -23.66% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 18.74 µs | 15.53 µs | ⚪ -17.14% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.09 µs | 6.71 µs | ⚪ +64.12% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.14 µs | 5.07 µs | ⚪ +22.47% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.68 µs | 4.10 µs | ⚪ -12.39% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 31.65 µs | 35.24 µs | ⚪ +11.36% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 104.78 µs | 88.85 µs | ⚪ -15.20% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.09 µs | 2.60 µs | ⚪ -15.91% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 8.98 µs | 1.14 µs | ⚪ -87.28% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 22.31 µs | 1.85 µs | ⚪ -91.72% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.71 µs | 7.25 µs | ⚪ -5.91% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.99 µs | 3.13 µs | ⚪ -47.70% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.03 µs | 4.67 µs | ⚪ +54.49% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 28.95 µs | 6.67 µs | ⚪ -76.97% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.83 µs | 1.07 µs | ⚪ -41.35% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.68 µs | 1.99 µs | ⚪ -25.47% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 9.11 µs | 6.21 µs | ⚪ -31.83% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.82 µs | 12.13 µs | ⚪ +217.45% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.61 µs | 2.21 µs | ⚪ +37.64% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 4.76 µs | 5.48 µs | ⚪ +15.03% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.33 µs | 2.88 µs | ⚪ +23.89% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.54 µs | 30.88 µs | ⚪ +457.98% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 10.00 µs | 1.51 µs | ⚪ -84.88% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.50 µs | 1.29 µs | ⚪ -14.28% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 6.80 µs | 2.27 µs | ⚪ -66.64% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 17.58 µs | 21.96 µs | ⚪ +24.90% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.18 µs | 0.86 µs | ⚪ -60.44% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.22 µs | 1.64 µs | ⚪ -68.66% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.88 µs | 2.43 µs | ⚪ -69.16% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 13.21 µs | 9.83 µs | ⚪ -25.56% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 6.47 µs | 12.41 µs | ⚪ +91.78% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 9.90 µs | 4.47 µs | ⚪ -54.83% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 2.19 µs | 5.01 µs | ⚪ +128.82% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 5.86 µs | 18.06 µs | ⚪ +208.50% |

