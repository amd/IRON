# Performance trends

**Operators added:** `lm_server`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 9.88 µs | 13.95 µs | ⚪ +41.09% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 3.29 µs | 6.12 µs | ⚪ +85.96% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.05 µs | 12.39 µs | ⚪ +504.76% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 3.63 µs | 1.81 µs | ⚪ -50.07% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.80 µs | 7.29 µs | ⚪ +52.01% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.68 µs | 7.44 µs | ⚪ -23.08% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.65 µs | 8.52 µs | ⚪ +221.00% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.09 µs | 7.83 µs | ⚪ +53.93% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 663.22 µs | 12.86 µs | ⚪ -98.06% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 81.95 µs | 21.00 µs | ⚪ -74.37% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 14.52 µs | 6.37 µs | ⚪ -56.16% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.16 µs | 2.19 µs | ⚪ -30.75% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 7.69 µs | 1.34 µs | ⚪ -82.61% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 2.89 µs | 6.46 µs | ⚪ +123.56% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.26 µs | 4.56 µs | ⚪ -13.32% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.40 µs | 1.18 µs | ⚪ -50.98% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 9.41 µs | 6.48 µs | ⚪ -31.14% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.21 µs | 41.80 µs | ⚪ +1201.56% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 72.95 µs | 52.81 µs | ⚪ -27.61% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 96.56 µs | 137.52 µs | ⚪ +42.41% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.30 µs | 0.87 µs | ⚪ -73.59% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.17 GB/s | 0.19 GB/s | 🟢 +7.88% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 95.53 µs | 88.55 µs | 🟢 -7.31% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.56 µs | 1.29 µs | ⚪ -49.81% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.78 µs | 2.82 µs | ⚪ +58.62% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.18 µs | 3.82 µs | ⚪ +20.17% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.54 µs | 2.57 µs | ⚪ -27.35% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.75 µs | 4.23 µs | ⚪ +12.69% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 69.36 µs | 11.61 µs | ⚪ -83.27% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 6.25 µs | 1.06 µs | ⚪ -83.09% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.52 µs | 1.56 µs | ⚪ -38.17% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 6.39 µs | 2.57 µs | ⚪ -59.80% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 9.72 µs | 12.56 µs | ⚪ +29.28% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 9.12 µs | 2.22 µs | ⚪ -75.62% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.53 µs | 5.89 µs | ⚪ +29.84% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.09 µs | 0.91 µs | ⚪ -56.58% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.76 µs | 3.47 µs | ⚪ -7.72% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 11.80 µs | 17.65 µs | ⚪ +49.60% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 34.78 µs | 25.66 µs | ⚪ -26.23% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.17 µs | 1.80 µs | ⚪ +53.88% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.30 µs | 5.17 µs | ⚪ +56.60% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 11.35 µs | 6.12 µs | ⚪ -46.11% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 15.03 µs | 6.03 µs | ⚪ -59.91% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 2.94 µs | 1.79 µs | ⚪ -39.08% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 8.72 µs | 5.51 µs | ⚪ -36.88% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 6.76 µs | 4.82 µs | ⚪ -28.69% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 4.03 µs | 6.19 µs | ⚪ +53.63% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 55.34 µs | 186.33 µs | ⚪ +236.70% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 79.24 µs | 38.64 µs | ⚪ -51.24% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 70.54 µs | 75.08 µs | ⚪ +6.43% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 94.48 µs | 153.04 µs | ⚪ +61.97% |
| `mha_prefill_lxl` | `separate-projected-causal-defaults` | `Latency MAD` | 34.91 µs | 26.15 µs | ⚪ -25.10% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 26.51 µs | 36.14 µs | ⚪ +36.29% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 49.78 µs | 46.31 µs | ⚪ -6.97% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 109.56 µs | 34.53 µs | ⚪ -68.49% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency` | 5107.66 µs | 6509.61 µs | 🔴 +27.45% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 2.87 µs | 486.18 µs | ⚪ +16866.69% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 758.97 µs | 4.32 µs | ⚪ -99.43% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.23 µs | 4.75 µs | ⚪ +113.01% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 5.20 µs | 4.57 µs | ⚪ -12.12% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 8.46 µs | 642.89 µs | ⚪ +7498.30% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 9.32 µs | 11.56 µs | ⚪ +24.03% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5584.27 µs | 4674.25 µs | 🟢 -16.30% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 3.80 µs | 3.29 µs | ⚪ -13.57% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency` | 6799.27 µs | 7869.65 µs | 🔴 +15.74% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 25.43 µs | 127.67 µs | ⚪ +401.96% |

