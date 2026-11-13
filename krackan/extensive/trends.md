# Performance trends

**Operators added:** `mha_prefill_lxl`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 10.56 µs | 2.11 µs | ⚪ -80.02% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.03 µs | 6.42 µs | ⚪ +111.43% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 1.22 µs | 1.59 µs | ⚪ +30.40% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 10.05 µs | 2.23 µs | ⚪ -77.81% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.25 µs | 1.14 µs | ⚪ -49.57% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.10 µs | 8.05 µs | ⚪ +282.60% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.25 µs | 3.23 µs | ⚪ -55.46% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 159.35 µs | 8.43 µs | ⚪ -94.71% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 25.53 µs | 13.79 µs | ⚪ -45.98% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 9.70 µs | 1.29 µs | ⚪ -86.73% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.56 µs | 1.52 µs | ⚪ -57.34% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 4.27 µs | 2.16 µs | ⚪ -49.29% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.36 µs | 1.57 µs | ⚪ +15.51% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 7.11 µs | 4.42 µs | ⚪ -37.82% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.44 µs | 4.87 µs | ⚪ +99.73% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.99 µs | 10.40 µs | ⚪ +73.58% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 27.91 µs | 31.69 µs | ⚪ +13.52% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 19.76 µs | 29.73 µs | ⚪ +50.47% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 78.34 µs | 107.18 µs | ⚪ +36.81% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.75 µs | 1.25 µs | ⚪ -66.77% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 GB/s | 0.17 GB/s | 🔴 -7.59% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 89.86 µs | 97.24 µs | 🔴 +8.21% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.06 µs | 1.46 µs | ⚪ -29.12% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 7.95 µs | 1.55 µs | ⚪ -80.52% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.72 µs | 7.65 µs | ⚪ +180.95% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.61 µs | 7.33 µs | ⚪ +103.03% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.63 µs | 1.93 µs | ⚪ -74.67% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 17.01 µs | 35.58 µs | ⚪ +109.20% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.76 µs | 11.46 µs | ⚪ +315.97% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.53 µs | 2.38 µs | ⚪ +55.22% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.70 µs | 3.35 µs | ⚪ +24.13% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.45 µs | 3.74 µs | ⚪ -16.10% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.26 µs | 2.29 µs | ⚪ +82.03% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 20.11 µs | 18.49 µs | ⚪ -8.05% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 1.67 µs | 8.24 µs | ⚪ +392.41% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.81 µs | 18.46 µs | ⚪ +558.05% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.64 µs | 2.90 µs | ⚪ +9.68% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.15 µs | 4.39 µs | ⚪ +39.66% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.95 µs | 3.67 µs | ⚪ -75.44% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 21.84 µs | 23.10 µs | ⚪ +5.80% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.36 µs | 1.66 µs | ⚪ -29.52% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 11.62 µs | 10.05 µs | ⚪ -13.54% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.56 µs | 2.73 µs | ⚪ -23.38% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 9.49 µs | 17.83 µs | ⚪ +87.86% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 12.22 µs | 7.36 µs | ⚪ -39.77% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 9.97 µs | 9.14 µs | ⚪ -8.34% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 8.25 µs | 7.00 µs | ⚪ -15.12% |

