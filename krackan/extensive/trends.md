# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 3.83 µs | 1.91 µs | ⚪ -49.99% |
| `Clamp` | `npu2-Clamp-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-low_-0.75-high_1.25` | `Latency MAD` | 4.10 µs | 8.16 µs | ⚪ +98.76% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.01 µs | 2.94 µs | ⚪ +46.39% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.68 µs | 8.68 µs | ⚪ +224.54% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 12.23 µs | 8.59 µs | ⚪ -29.81% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 3.49 µs | 2.39 µs | ⚪ -31.40% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.70 µs | 7.15 µs | ⚪ +319.76% |
| `GEMM` | `npu2-GEMM-M_1024-K_1536-N_6144` | `Latency MAD` | 5.91 µs | 502.67 µs | ⚪ +8411.96% |
| `GEMM` | `npu2-GEMM-M_2048-K_2048-N_2048-b_col_maj_True` | `Latency MAD` | 9.65 µs | 17.93 µs | ⚪ +85.83% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 5.63 µs | 1.70 µs | ⚪ -69.85% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 2.67 µs | 7.82 µs | ⚪ +192.72% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 11.56 µs | 2.38 µs | ⚪ -79.38% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 4.73 µs | 23.41 µs | ⚪ +394.66% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 12.23 µs | 9.49 µs | ⚪ -22.40% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 37.93 µs | 18.48 µs | ⚪ -51.27% |
| `MHA` | `npu2-MHA-num_heads_1-seq_len_16384-num_pipelines_8` | `Latency MAD` | 17.51 µs | 90.77 µs | ⚪ +418.41% |
| `MHA` | `npu2-MHA-num_heads_8-num_KV_heads_2-seq_len_16384-num_pipelines_8` | `Latency MAD` | 171.15 µs | 100.83 µs | ⚪ -41.08% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 3.94 µs | 0.98 µs | ⚪ -75.21% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.16 GB/s | 0.17 GB/s | 🟢 +5.84% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 2.86 µs | 2.50 µs | ⚪ -12.57% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Bandwidth` | 0.64 GB/s | 0.71 GB/s | 🟢 +10.33% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency` | 80.12 µs | 72.62 µs | 🟢 -9.36% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.96 µs | 3.39 µs | ⚪ +73.12% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.99 µs | 5.69 µs | ⚪ -5.09% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.71 µs | 3.00 µs | ⚪ +75.70% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 9.93 µs | 7.23 µs | ⚪ -27.20% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 25.92 µs | 18.42 µs | ⚪ -28.93% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.15 µs | 0.61 µs | ⚪ -47.17% |
| `RoPE` | `npu2-RoPE-rows_4096-cols_512-angle_rows_8` | `Latency MAD` | 2.23 µs | 3.71 µs | ⚪ +65.92% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 14.38 µs | 4.83 µs | ⚪ -66.38% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 3.98 µs | 7.83 µs | ⚪ +96.60% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.96 µs | 1.01 µs | ⚪ -48.34% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 10.44 µs | 9.70 µs | ⚪ -7.05% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 5.79 µs | 17.81 µs | ⚪ +207.88% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.77 µs | 2.38 µs | ⚪ +34.42% |
| `Softmax` | `npu2-Softmax-rows_4096-cols_512-num_aie_columns_2-num_channels_2` | `Latency MAD` | 1.84 µs | 1.57 µs | ⚪ -14.44% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.37 µs | 3.78 µs | ⚪ +176.64% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Bandwidth` | 3.18 GB/s | 4.71 GB/s | 🟢 +48.25% |
| `copy_gather` | `test_a_prompt_chunk_s_rows_are_gathered_each_call` | `Latency` | 660.06 µs | 445.23 µs | 🟢 -32.55% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 14.52 µs | 6.66 µs | ⚪ -54.12% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 24.22 µs | 29.39 µs | ⚪ +21.35% |
| `flm/gemm` | `M_1024-K_1536-N_6144-epilogue_none` | `Latency MAD` | 2.44 µs | 3.32 µs | ⚪ +35.93% |
| `flm/gemm` | `npu2-M_1024-K_1536-N_6144-epilogue_none-rounding_conv_even` | `Latency MAD` | 8.16 µs | 2.84 µs | ⚪ -65.19% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 6.57 µs | 3.80 µs | ⚪ -42.15% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 11.89 µs | 18.58 µs | ⚪ +56.20% |
| `flm/layer` | `gemma4_e2b-global-700` | `Latency MAD` | 11.53 µs | 13.15 µs | ⚪ +14.04% |
| `flm/layer` | `gemma4_e2b-swa-700` | `Latency MAD` | 10.12 µs | 14.25 µs | ⚪ +40.72% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency MAD` | 2.96 µs | 12.13 µs | ⚪ +309.64% |

