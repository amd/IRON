# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 1.91 µs | 11.34 µs | ⚪ +492.55% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 8.16 µs | 5.02 µs | ⚪ -38.39% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.03 µs | 5.18 µs | ⚪ +71.18% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.94 µs | 2.36 µs | ⚪ -19.59% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.68 µs | 2.47 µs | ⚪ -71.50% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.59 µs | 13.15 µs | ⚪ +53.21% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.39 µs | 3.55 µs | ⚪ +48.10% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.15 µs | 3.42 µs | ⚪ -52.13% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 502.67 µs | 10.49 µs | ⚪ -97.91% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Bandwidth` | 8.76 GB/s | 12.80 GB/s | 🟢 +46.22% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency` | 2873.80 µs | 1965.45 µs | 🟢 -31.61% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 17.93 µs | 4.56 µs | ⚪ -74.55% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Throughput` | 5978.11 GOP/s | 8740.92 GOP/s | 🟢 +46.22% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 5.50 µs | 2.75 µs | ⚪ -49.96% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 1.70 µs | 14.45 µs | ⚪ +751.43% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 7.82 µs | 3.40 µs | ⚪ -56.54% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 2.38 µs | 3.99 µs | ⚪ +67.46% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 23.41 µs | 3.51 µs | ⚪ -85.02% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.41 µs | 5.00 µs | ⚪ -7.42% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 18.48 µs | 20.61 µs | ⚪ +11.52% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 90.77 µs | 77.12 µs | ⚪ -15.04% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 100.83 µs | 132.75 µs | ⚪ +31.65% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 0.98 µs | 2.50 µs | ⚪ +155.70% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.18 GB/s | 🟢 +5.57% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.50 µs | 2.02 µs | ⚪ -19.40% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 3.39 µs | 2.81 µs | ⚪ -17.13% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.00 µs | 2.55 µs | ⚪ -14.88% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.23 µs | 1.75 µs | ⚪ -75.74% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 18.42 µs | 10.46 µs | ⚪ -43.20% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.61 µs | 2.26 µs | ⚪ +273.68% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.71 µs | 1.51 µs | ⚪ -59.33% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.83 µs | 9.16 µs | ⚪ +89.45% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.83 µs | 5.26 µs | ⚪ -32.88% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.01 µs | 1.16 µs | ⚪ +14.38% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 9.70 µs | 1.50 µs | ⚪ -84.52% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 17.81 µs | 4.84 µs | ⚪ -72.81% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.38 µs | 1.96 µs | ⚪ -17.85% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.57 µs | 1.92 µs | ⚪ +22.00% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.78 µs | 5.32 µs | ⚪ +40.76% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 6.66 µs | 3.63 µs | ⚪ -45.49% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 29.39 µs | 35.93 µs | ⚪ +22.26% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 3.32 µs | 1.29 µs | ⚪ -60.99% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.84 µs | 4.91 µs | ⚪ +73.02% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.80 µs | 4.48 µs | ⚪ +17.92% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 18.58 µs | 5.53 µs | ⚪ -70.25% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.15 µs | 12.40 µs | ⚪ -5.64% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 14.25 µs | 10.31 µs | ⚪ -27.64% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 12.13 µs | 2.91 µs | ⚪ -76.04% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 9.53 µs | 4.27 µs | ⚪ -55.18% |

