# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 6.25 µs | 14.10 µs | ⚪ +125.73% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 11.79 µs | 9.85 µs | ⚪ -16.45% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 2.12 µs | 4.63 µs | ⚪ +118.15% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.02 µs | 1.90 µs | ⚪ -5.95% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.67 µs | 8.06 µs | ⚪ +20.78% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 18.43 µs | 12.35 µs | ⚪ -32.99% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 2.57 µs | 2.85 µs | ⚪ +11.15% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.56 µs | 3.80 µs | ⚪ +48.34% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Bandwidth` | 10.07 GB/s | 11.67 GB/s | 🟢 +15.89% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency` | 3435.16 µs | 2964.18 µs | 🟢 -13.71% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 22.69 µs | 9.34 µs | ⚪ -58.84% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Throughput` | 5626.33 GOP/s | 6520.29 GOP/s | 🟢 +15.89% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 434.34 µs | 25.38 µs | ⚪ -94.16% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 13.68 µs | 12.90 µs | ⚪ -5.70% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 3.79 µs | 11.07 µs | ⚪ +191.81% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 14.83 µs | 16.18 µs | ⚪ +9.12% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 4.44 µs | 4.10 µs | ⚪ -7.56% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 2.77 µs | 4.11 µs | ⚪ +48.28% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.56 µs | 3.16 µs | ⚪ -43.19% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.83 µs | 10.97 µs | ⚪ +88.22% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.88 µs | 35.40 µs | ⚪ +1129.06% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 57.28 µs | 51.79 µs | ⚪ -9.57% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 17.94 µs | 4.89 µs | ⚪ -72.75% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.04 µs | 6.02 µs | ⚪ +194.40% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 4.81 µs | 1.25 µs | ⚪ -74.10% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 8.30 µs | 6.47 µs | ⚪ -21.98% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.58 µs | 15.47 µs | ⚪ +237.98% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.02 µs | 5.44 µs | ⚪ +35.11% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 29.61 µs | 34.27 µs | ⚪ +15.73% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 0.98 µs | 3.45 µs | ⚪ +253.33% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 1.50 µs | 1.74 µs | ⚪ +16.02% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.88 µs | 5.24 µs | ⚪ +82.35% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 7.82 µs | 9.01 µs | ⚪ +15.11% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.69 µs | 1.87 µs | ⚪ +10.60% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 3.92 µs | 1.52 µs | ⚪ -61.25% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 6.54 µs | 4.23 µs | ⚪ -35.33% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 5.16 µs | 2.16 µs | ⚪ -58.16% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 5.18 µs | 1.86 µs | ⚪ -64.16% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 3.68 µs | 3.11 µs | ⚪ -15.51% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 9.99 µs | 31.37 µs | ⚪ +214.09% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 19.51 µs | 27.92 µs | ⚪ +43.14% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 3.62 µs | 1.32 µs | ⚪ -63.47% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 2.15 µs | 7.57 µs | ⚪ +251.67% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 15.28 µs | 6.70 µs | ⚪ -56.14% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 16.28 µs | 13.99 µs | ⚪ -14.07% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 2.99 µs | 3.56 µs | ⚪ +18.92% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 16.12 µs | 5.05 µs | ⚪ -68.67% |
| `flm/prefill_attn` | `kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1` | `Latency MAD` | 6.60 µs | 7.64 µs | ⚪ +15.78% |

