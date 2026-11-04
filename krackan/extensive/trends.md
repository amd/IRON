# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 9.48 µs | 10.16 µs | ⚪ +7.13% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.28 µs | 4.35 µs | ⚪ -30.77% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.17 µs | 1.88 µs | ⚪ -54.95% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 10.76 µs | 1.83 µs | ⚪ -82.96% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.70 µs | 8.37 µs | ⚪ +24.90% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 16.56 µs | 3.94 µs | ⚪ -76.20% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 0.82 µs | 1.35 µs | ⚪ +64.64% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.04 µs | 4.93 µs | ⚪ -29.98% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 5.94 µs | 591.14 µs | ⚪ +9857.80% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 202.12 µs | 16.98 µs | ⚪ -91.60% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 14.21 µs | 12.94 µs | ⚪ -8.92% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.15 µs | 4.94 µs | ⚪ +56.76% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 10.85 µs | 13.82 µs | ⚪ +27.32% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 3.93 µs | 1.62 µs | ⚪ -58.85% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.62 µs | 4.43 µs | ⚪ +22.39% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.17 µs | 2.95 µs | ⚪ -6.98% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 8.80 µs | 5.61 µs | ⚪ -36.25% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 15.36 µs | 3.89 µs | ⚪ -74.69% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 129.74 µs | 137.02 µs | ⚪ +5.61% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 1.57 µs | 5.63 µs | ⚪ +258.23% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 3.39 µs | 1.11 µs | ⚪ -67.31% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.76 GB/s | 0.69 GB/s | 🔴 -8.62% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 67.69 µs | 74.08 µs | 🔴 +9.44% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.54 µs | 3.96 µs | ⚪ +11.92% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.66 µs | 8.79 µs | ⚪ +140.36% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.79 µs | 5.60 µs | ⚪ -36.27% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 26.16 µs | 12.51 µs | ⚪ -52.17% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 13.80 µs | 10.03 µs | ⚪ -27.30% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.41 µs | 1.72 µs | ⚪ +22.10% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 1.43 µs | 3.25 µs | ⚪ +127.28% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.15 µs | 1.02 µs | ⚪ -11.29% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 10.70 µs | 7.44 µs | ⚪ -30.45% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.10 µs | 9.71 µs | ⚪ +19.85% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 23.10 µs | 3.26 µs | ⚪ -85.90% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.22 µs | 2.39 µs | ⚪ +96.22% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.49 µs | 4.23 µs | ⚪ +21.08% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 11.74 µs | 10.03 µs | ⚪ -14.51% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 32.76 µs | 35.19 µs | ⚪ +7.43% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.61 µs | 0.63 µs | ⚪ -60.85% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 8.26 µs | 3.02 µs | ⚪ -63.48% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.77 µs | 6.61 µs | ⚪ +38.65% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 12.86 µs | 7.34 µs | ⚪ -42.96% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 3.95 µs | 15.32 µs | ⚪ +287.59% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 4.74 µs | 13.09 µs | ⚪ +176.31% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 4.05 µs | 4.89 µs | ⚪ +20.65% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 5.22 µs | 8.27 µs | ⚪ +58.61% |

