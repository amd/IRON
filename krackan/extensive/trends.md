# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `AXPY` | `npu2-AXPY-size_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0` | `Latency MAD` | 7.83 | 3.16 | 🟢 -59.69% |
| `Copy` | `npu2-Copy-bench_flat_4mi` | `Latency MAD` | 4.06 | 2.25 | 🟢 -44.46% |
| `DepthwiseConv1d` | `npu2-DepthwiseConv1d-rows_768-channels_1024-num_aie_columns_8` | `Latency MAD` | 2.91 | 2.51 | 🟢 -14.05% |
| `ElementwiseAdd` | `npu2-ElementwiseAdd-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 2.36 | 10.93 | 🔴 +363.16% |
| `ElementwiseMul` | `npu2-ElementwiseMul-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 14.39 | 2.47 | 🟢 -82.80% |
| `Emit` | `npu2-Emit-eight_carried` | `Bandwidth` | 0.09 | 0.12 | 🟢 +31.01% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency` | 22.14 | 16.90 | 🟢 -23.67% |
| `Emit` | `npu2-Emit-eight_carried` | `Latency MAD` | 5.09 | 2.16 | 🟢 -57.52% |
| `GELU` | `npu2-GELU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.67 | 4.83 | 🔴 +188.82% |
| `GEMV` | `npu2-GEMV-M_1536-K_12288-num_aie_columns_8-tile_size_input_1-tile_size_output_64` | `Latency MAD` | 15.51 | 5.83 | 🟢 -62.45% |
| `GEMV` | `npu2-GEMV-M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256` | `Latency MAD` | 2.45 | 11.21 | 🔴 +357.71% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024` | `Latency MAD` | 3.91 | 15.50 | 🔴 +296.60% |
| `GEMV` | `npu2-GEMV-M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_512-num_channels_2` | `Latency MAD` | 6.47 | 3.60 | 🟢 -44.44% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True` | `Latency MAD` | 5.64 | 2.44 | 🟢 -56.75% |
| `LayerNorm` | `npu2-LayerNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.46 | 4.15 | 🔴 +183.93% |
| `Limbs` | `npu2-Limbs-rows_4096-line_320-num_aie_columns_8` | `Latency MAD` | 5.30 | 6.07 | 🔴 +14.56% |
| `Log` | `npu2-Log-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 8.60 | 4.46 | 🟢 -48.17% |
| `Magnitude` | `npu2-Magnitude-rows_4096-width_640-num_aie_columns_8` | `Latency MAD` | 2.56 | 8.59 | 🔴 +235.63% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Bandwidth` | 0.18 | 0.16 | 🔴 -8.49% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency` | 91.05 | 99.49 | 🔴 +9.28% |
| `Merge` | `npu2-Merge-rows_2048-placeholders_((258881, 2048), (258880, 2560))` | `Latency MAD` | 1.33 | 1.43 | 🔴 +7.95% |
| `PatchPositions` | `npu2-PatchPositions-rows_2560-out_height_672-out_width_912` | `Latency MAD` | 1.77 | 1.68 | 🟢 -5.12% |
| `RMSNorm` | `npu2-RMSNorm-rows_2048-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 1.89 | 3.47 | 🔴 +83.58% |
| `ReLU` | `npu2-ReLU-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 9.31 | 3.11 | 🟢 -66.62% |
| `Resample` | `npu2-Resample-height_3024-width_4032-out_height_672-out_width_912` | `Latency MAD` | 14.90 | 15.76 | 🔴 +5.74% |
| `ResampleTaps` | `npu2-ResampleTaps-in_size_4032-out_size_912` | `Latency MAD` | 1.50 | 3.94 | 🔴 +163.18% |
| `RowwiseAdd` | `npu2-RowwiseAdd-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 8.70 | 7.06 | 🟢 -18.89% |
| `RowwiseMul` | `npu2-RowwiseMul-rows_2048-num_aie_columns_4-num_channels_2-tile_size_4096` | `Latency MAD` | 2.67 | 6.98 | 🔴 +162.03% |
| `Sample` | `npu2-Sample-llama` | `Latency MAD` | 1.47 | 2.38 | 🔴 +61.60% |
| `SelectiveScan` | `npu2-SelectiveScan-rows_64-heads_16-head_dim_64-state_size_64-groups_2` | `Latency MAD` | 2.87 | 4.78 | 🔴 +66.43% |
| `SiLU` | `npu2-SiLU-size_8388608-num_aie_columns_8-tile_size_4096` | `Latency MAD` | 3.76 | 5.86 | 🔴 +55.64% |
| `Sigmoid` | `npu2-Sigmoid-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 2.37 | 2.93 | 🔴 +23.68% |
| `Tanh` | `npu2-Tanh-size_8388608-num_aie_columns_8-num_channels_2-tile_size_4096` | `Latency MAD` | 4.09 | 23.50 | 🔴 +474.99% |
| `flm.DequantBFP` | `npu2-flm.DequantBFP-K_6144-N_1536` | `Latency MAD` | 15.29 | 13.43 | 🟢 -12.19% |
| `flm.LMHead` | `npu2-flm.LMHead-dim_1536-vocab_262144-softcap_30.0` | `Latency MAD` | 36.89 | 31.86 | 🟢 -13.63% |
| `flm/gemm` | `npu2-M_1024-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 5.69 | 4.59 | 🟢 -19.21% |
| `flm/gemm` | `npu2-M_2048-K_2560-N_10240-epilogue_none-rounding_conv_even` | `Latency MAD` | 52.66 | 12.23 | 🟢 -76.78% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Bandwidth` | 5.96 | 5.53 | 🔴 -7.27% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Latency` | 1583.58 | 1707.75 | 🔴 +7.84% |
| `flm/prefill_attn` | `kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1` | `Throughput` | 1358.74 | 1259.95 | 🔴 -7.27% |

