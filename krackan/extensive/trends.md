# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 4.74 µs | 13.50 µs | ⚪ +184.43% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 6.63 µs | 3.79 µs | ⚪ -42.79% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.86 µs | 1.36 µs | ⚪ -52.54% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 1.49 µs | 1.21 µs | ⚪ -19.16% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 11.29 µs | 2.30 µs | ⚪ -79.59% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 1.87 µs | 11.47 µs | ⚪ +511.90% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.17 µs | 5.56 µs | ⚪ +376.32% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 0.86 µs | 9.40 µs | ⚪ +996.62% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 28.36 µs | 389.14 µs | ⚪ +1272.14% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 3.60 µs | 18.74 µs | ⚪ +420.88% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 17.34 µs | 9.21 µs | ⚪ -46.91% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 1.16 µs | 15.92 µs | ⚪ +1275.58% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 1.80 µs | 3.40 µs | ⚪ +89.08% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.23 µs | 4.09 µs | ⚪ -21.78% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.97 µs | 4.14 µs | ⚪ +109.93% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 7.00 µs | 8.26 µs | ⚪ +18.03% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.93 µs | 4.68 µs | ⚪ +59.86% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 106.15 µs | 31.65 µs | ⚪ -70.19% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 125.83 µs | 104.78 µs | ⚪ -16.73% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 14.37 µs | 3.09 µs | ⚪ -78.53% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.70 µs | 8.98 µs | ⚪ +428.66% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 3.59 µs | 22.31 µs | ⚪ +522.11% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 11.73 µs | 7.71 µs | ⚪ -34.29% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 7.53 µs | 5.99 µs | ⚪ -20.56% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.17 µs | 3.03 µs | ⚪ -41.53% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 7.63 µs | 28.95 µs | ⚪ +279.65% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 2.06 µs | 1.83 µs | ⚪ -11.39% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.52 µs | 2.68 µs | ⚪ +76.19% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 4.54 µs | 9.11 µs | ⚪ +100.76% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.35 µs | 3.82 µs | ⚪ -48.00% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.30 µs | 1.61 µs | ⚪ +23.49% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 11.71 µs | 4.76 µs | ⚪ -59.30% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 4.07 µs | 2.33 µs | ⚪ -42.91% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.08 µs | 5.54 µs | ⚪ +79.62% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.06 µs | 10.00 µs | ⚪ +842.00% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.03 µs | 1.50 µs | ⚪ -62.69% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.01 µs | 6.80 µs | ⚪ -51.45% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 19.84 µs | 17.58 µs | ⚪ -11.38% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.01 µs | 2.18 µs | ⚪ +8.43% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 10.82 µs | 5.22 µs | ⚪ -51.72% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 4.80 µs | 7.88 µs | ⚪ +64.18% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.50 µs | 13.21 µs | ⚪ +76.04% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 13.24 µs | 6.47 µs | ⚪ -51.10% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 14.69 µs | 9.90 µs | ⚪ -32.59% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 2.64 µs | 2.19 µs | ⚪ -17.06% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 7.14 µs | 5.86 µs | ⚪ -18.03% |

