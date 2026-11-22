# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 11.18 µs | 8.09 µs | ⚪ -27.65% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 11.15 µs | 7.57 µs | ⚪ -32.08% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.91 µs | 1.57 µs | ⚪ -46.03% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.64 µs | 2.44 µs | ⚪ -7.45% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 10.91 µs | 8.77 µs | ⚪ -19.61% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.76 µs | 8.40 µs | ⚪ +45.74% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.94 µs | 4.03 µs | ⚪ +107.71% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.49 µs | 1.32 µs | ⚪ -84.42% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 10.66 GB/s | 9.90 GB/s | 🔴 -7.11% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3245.91 µs | 3494.35 µs | 🔴 +7.65% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 5.06 µs | 25.01 µs | ⚪ +394.70% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5954.37 GOP/s | 5531.03 GOP/s | 🔴 -7.11% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 11.94 µs | 12.84 µs | ⚪ +7.55% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 16.87 µs | 8.64 µs | ⚪ -48.78% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 9.80 µs | 7.95 µs | ⚪ -18.90% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 6.14 µs | 15.43 µs | ⚪ +151.52% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 2.30 µs | 15.62 µs | ⚪ +578.00% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.30 µs | 5.50 µs | ⚪ +27.95% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.94 µs | 5.24 µs | ⚪ +32.95% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.79 µs | 8.48 µs | ⚪ +46.57% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.86 µs | 2.70 µs | ⚪ -30.08% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 53.98 µs | 70.85 µs | ⚪ +31.25% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 99.33 µs | 167.94 µs | ⚪ +69.09% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.47 µs | 7.05 µs | ⚪ +103.01% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 5.19 µs | 1.63 µs | ⚪ -68.63% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 3.10 µs | 2.06 µs | ⚪ -33.49% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.23 µs | 2.24 µs | ⚪ +82.89% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.16 µs | 2.48 µs | ⚪ -65.29% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 31.17 µs | 16.81 µs | ⚪ -46.07% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.00 µs | 5.42 µs | ⚪ +440.97% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 3.65 µs | 2.28 µs | ⚪ -37.36% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.13 µs | 8.93 µs | ⚪ +185.51% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.07 µs | 6.14 µs | ⚪ -23.95% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.06 µs | 1.38 µs | ⚪ +30.32% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 6.63 µs | 11.82 µs | ⚪ +78.39% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.72 µs | 3.21 µs | ⚪ -63.24% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.79 µs | 1.32 µs | ⚪ -72.49% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 2.23 µs | 1.04 µs | ⚪ -53.49% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.77 µs | 1.49 µs | ⚪ -46.03% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 6.31 µs | 3.03 µs | ⚪ -51.99% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 25.93 µs | 30.64 µs | ⚪ +18.16% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 31.37 µs | 1.20 µs | ⚪ -96.18% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.96 µs | 7.56 µs | ⚪ +155.50% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.96 µs | 3.08 µs | ⚪ -22.26% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 15.70 µs | 143.74 µs | ⚪ +815.53% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 15.43 µs | 10.94 µs | ⚪ -29.06% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 19.21 µs | 2.47 µs | ⚪ -87.14% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 11.06 µs | 3.97 µs | ⚪ -64.09% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 4.73 µs | 4.11 µs | ⚪ -13.04% |
| `mha_prefill_lxl` | `separate-core-causal-defaults` | `Latency MAD` | 24.93 µs | 88.62 µs | ⚪ +255.44% |
| `mha_prefill_lxl` | `separate-core-causal-profile` | `Latency MAD` | 54.18 µs | 34.31 µs | ⚪ -36.67% |
| `mha_prefill_lxl` | `separate-core-unmasked-defaults` | `Latency MAD` | 19.14 µs | 35.07 µs | ⚪ +83.22% |
| `mha_prefill_lxl` | `separate-core-unmasked-profile` | `Latency MAD` | 42.34 µs | 30.47 µs | ⚪ -28.05% |
| `mha_prefill_lxl` | `separate-projected-causal-profile` | `Latency MAD` | 361.44 µs | 178.30 µs | ⚪ -50.67% |
| `mha_prefill_lxl` | `separate-projected-unmasked-defaults` | `Latency MAD` | 53.20 µs | 112.17 µs | ⚪ +110.83% |
| `mha_prefill_lxl` | `separate-projected-unmasked-profile` | `Latency MAD` | 38.76 µs | 296.49 µs | ⚪ +664.88% |
| `mha_prefill_lxl` | `single-core-causal-defaults` | `Latency MAD` | 2.09 µs | 3.19 µs | ⚪ +52.81% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency` | 5580.77 µs | 6992.36 µs | 🔴 +25.29% |
| `mha_prefill_lxl` | `single-core-causal-profile` | `Latency MAD` | 380.80 µs | 5.83 µs | ⚪ -98.47% |
| `mha_prefill_lxl` | `single-core-unmasked-defaults` | `Latency MAD` | 2.60 µs | 2.82 µs | ⚪ +8.65% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency` | 5607.88 µs | 4693.05 µs | 🟢 -16.31% |
| `mha_prefill_lxl` | `single-core-unmasked-profile` | `Latency MAD` | 5.02 µs | 3.44 µs | ⚪ -31.53% |
| `mha_prefill_lxl` | `single-projected-causal-defaults` | `Latency MAD` | 709.50 µs | 350.62 µs | ⚪ -50.58% |
| `mha_prefill_lxl` | `single-projected-causal-profile` | `Latency MAD` | 241.09 µs | 337.51 µs | ⚪ +39.99% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency` | 5994.48 µs | 4657.28 µs | 🟢 -22.31% |
| `mha_prefill_lxl` | `single-projected-unmasked-defaults` | `Latency MAD` | 4.04 µs | 4.77 µs | ⚪ +18.12% |
| `mha_prefill_lxl` | `single-projected-unmasked-profile` | `Latency MAD` | 21.73 µs | 212.60 µs | ⚪ +878.55% |

