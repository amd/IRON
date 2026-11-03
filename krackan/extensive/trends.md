# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 15.76 µs | 2.75 µs | ⚪ -82.52% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 8.69 µs | 6.65 µs | ⚪ -23.52% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 3.63 µs | 4.52 µs | ⚪ +24.56% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.47 µs | 2.30 µs | ⚪ -7.07% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.86 µs | 10.08 µs | ⚪ +252.91% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.07 µs | 10.72 µs | ⚪ +76.72% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 1.30 µs | 2.94 µs | ⚪ +125.88% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.67 µs | 5.00 µs | ⚪ -11.78% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 11.67 GB/s | 9.87 GB/s | 🔴 -15.39% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 2964.95 µs | 3504.39 µs | 🔴 +18.19% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 7.65 µs | 29.61 µs | ⚪ +287.10% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 6518.61 GOP/s | 5515.18 GOP/s | 🔴 -15.39% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 12.46 µs | 16.61 µs | ⚪ +33.33% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 11.81 µs | 13.43 µs | ⚪ +13.69% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 10.96 µs | 6.44 µs | ⚪ -41.28% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.72 µs | 5.36 µs | ⚪ +13.46% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 3.67 µs | 7.36 µs | ⚪ +100.56% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.50 µs | 1.81 µs | ⚪ +20.70% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 9.51 µs | 4.03 µs | ⚪ -57.67% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.34 µs | 30.17 µs | ⚪ +594.67% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 27.72 µs | 58.40 µs | ⚪ +110.66% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 106.71 µs | 125.70 µs | ⚪ +17.80% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 6.67 µs | 2.12 µs | ⚪ -68.24% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.08 µs | 2.32 µs | ⚪ +115.68% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 2.08 µs | 0.95 µs | ⚪ -54.26% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 9.09 µs | 6.55 µs | ⚪ -27.96% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.03 µs | 2.36 µs | ⚪ +16.00% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 6.15 µs | 3.01 µs | ⚪ -51.07% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 41.99 µs | 35.71 µs | ⚪ -14.94% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.91 µs | 0.72 µs | ⚪ -20.92% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.73 µs | 4.32 µs | ⚪ -50.52% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.21 µs | 5.73 µs | ⚪ +78.60% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.20 µs | 0.71 µs | ⚪ -40.58% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 8.13 µs | 2.96 µs | ⚪ -63.64% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.63 µs | 1.75 µs | ⚪ -51.67% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.13 µs | 1.36 µs | ⚪ +20.45% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.37 µs | 5.80 µs | ⚪ +145.29% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 5.02 GB/s | 3.74 GB/s | 🔴 -25.49% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 417.73 µs | 560.68 µs | 🔴 +34.22% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.46 µs | 6.04 µs | ⚪ -58.23% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 30.68 µs | 21.68 µs | ⚪ -29.34% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 1.26 µs | 7.54 µs | ⚪ +499.92% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 3.45 µs | 6.73 µs | ⚪ +95.34% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 8.23 µs | 2.73 µs | ⚪ -66.81% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 7.08 µs | 10.12 µs | ⚪ +42.95% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 9.95 µs | 13.02 µs | ⚪ +30.85% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 8.51 µs | 10.30 µs | ⚪ +21.09% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 9.36 µs | 4.66 µs | ⚪ -50.16% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 7.23 µs | 13.09 µs | ⚪ +81.01% |

