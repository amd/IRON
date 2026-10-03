# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/llama_3.2_1b</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1] | ✅ | - | - | - |
| test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_accuracy[iter4] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter0] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter1] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter2] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter3] | ✅ | - | - | - |
| test_llama_3_2_1b_determinism[iter4] | ✅ | - | - | - |

</details>

## Small

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 159.52 | ✅ | 332.54 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 200.20 | ✅ | 330.64 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 198.66 | ✅ | 436.40 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 189.68 | ✅ | 820.18 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 174.58 | ✅ | 411.98 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 196.60 | ✅ | 469.28 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 211.54 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 213.06 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 5092.92 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 850.82 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 132.56 | ✅ | 378.16 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 148.58 | ✅ | 430.74 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 168.42 | ✅ | 488.82 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 177.54 | ✅ | 506.34 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 147.94 | ✅ | 623.96 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 201.70 | ✅ | 508.14 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 193.72 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 245.10 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 3184.38 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 466.70 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 165.48 | ✅ | 395.52 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 155.68 | ✅ | 530.84 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 152.72 | ✅ | 434.02 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 196.30 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4478.96 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 859.94 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 180.44 | ✅ | 356.86 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 182.16 | ✅ | 566.16 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 176.94 | ✅ | 510.92 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 211.82 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4319.12 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 901.50 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 297.16 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 324.08 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 310.10 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 322.54 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 306.10 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 297.66 | ✅ | 613.92 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 327.64 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 563.98 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1107.74 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 806.06 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 787.66 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 744.50 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 1627.44 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 556.12 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 434.24 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 2977.82 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 164.90 | ✅ | 365.34 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 165.84 | ✅ | 408.20 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 155.80 | ✅ | 405.76 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 158.46 | ✅ | 481.86 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 148.00 | ✅ | 818.24 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 195.48 | ✅ | 446.36 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 184.42 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 207.60 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4000.12 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 679.36 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2116.84 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 233.64 | ✅ | 672.74 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 251.42 | ✅ | 577.22 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47049.26 | ✅ | 80997.48 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27596.74 | ✅ | 19728.92 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7916.52 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2370.88 | ✅ | 3707.88 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3610.96 | ✅ | 6407.82 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1520.18 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 184.24 | ✅ | 379.58 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2768.96 | ✅ | 9691.54 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1381.38 | ✅ | 5416.68 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 874.30 | ✅ | 3866.14 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 821.14 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2813.00 | ✅ | 9349.20 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1409.14 | ✅ | 5719.38 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 854.68 | ✅ | 3499.60 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 824.56 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 500.28 | ✅ | 2562.54 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 332.34 | ✅ | 1536.44 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 276.04 | ✅ | 1084.24 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 462.10 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1000.92 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 250.72 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 291.60 | ✅ | 2776.42 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 173.16 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2710.60 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2547.34 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 154.02 | ✅ | 254.70 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 151.16 | ✅ | 314.90 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 182.48 | ✅ | 274.80 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 149.74 | ✅ | 454.48 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 190.36 | ✅ | 413.36 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 192.96 | ✅ | 510.72 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 180.26 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 224.06 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2330.70 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 663.50 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 158.54 | ✅ | 445.36 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 139.60 | ✅ | 298.40 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 141.02 | ✅ | 447.88 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 171.02 | ✅ | 451.30 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 203.64 | ✅ | 445.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 160.58 | ✅ | 449.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 139.76 | ✅ | 456.24 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 232.28 | ✅ | 415.60 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 178.12 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 227.84 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 2604.12 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 633.96 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 151.70 | ✅ | 390.80 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 217.62 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 143.40 | ✅ | 654.90 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 185.66 | ✅ | 325.70 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 184.02 | ✅ | 388.04 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 168.26 | ✅ | 491.32 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 193.22 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 186.22 | ✅ | 454.94 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 689.66 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 2854.68 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 15604.08 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 192.68 | ✅ | 340.40 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 178.18 | ✅ | 414.00 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 180.52 | ✅ | 503.10 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 182.40 | ✅ | 444.44 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 217.44 | ✅ | 504.22 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 182.56 | ✅ | 409.04 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 198.18 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 217.22 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3240.02 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 692.94 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 155.84 | ✅ | 435.52 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 137.98 | ✅ | 379.92 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 140.76 | ✅ | 274.70 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 179.24 | ✅ | 252.52 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 169.94 | ✅ | 712.78 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 169.94 | ✅ | 349.94 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 180.72 | ✅ | 265.82 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 189.64 | ✅ | 373.04 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 191.56 | ✅ | 429.24 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 179.44 | ✅ | 414.88 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 205.32 | ✅ | 416.10 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 190.86 | ✅ | 414.12 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 216.54 | ✅ | 334.30 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 206.38 | ✅ | 404.50 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 240.32 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 191.04 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 237.68 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 244.26 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3189.26 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 2981.20 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 703.84 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 658.60 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 171.54 | ✅ | 303.22 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 172.72 | ✅ | 393.50 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 171.28 | ✅ | 460.50 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 202.68 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 167.36 | ✅ | 319.74 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 160.48 | ✅ | 445.88 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 181.92 | ✅ | 455.86 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 190.64 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 785.66 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 315.04 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 151.38 | ✅ | 402.82 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 177.72 | ✅ | 253.06 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 189.20 | ✅ | 401.02 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 205.58 | ✅ | 391.16 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 186.08 | ✅ | 421.30 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 183.58 | ✅ | 481.92 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 221.56 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 219.34 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2442.68 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 724.90 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 178.28 | ✅ | 363.04 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 172.98 | ✅ | 410.96 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 181.08 | ✅ | 579.62 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 182.36 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4448.80 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 664.90 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 549.50 | ✅ | 2467.54 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 192.04 | ✅ | 449.42 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 187.84 | ✅ | 539.24 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 191.92 | ✅ | 426.62 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 468.66 | ✅ | 2523.18 |
| test_strided_copy[chunked_transfer] | ✅ | 156.06 | ✅ | 358.46 |
| test_strided_copy[contiguous] | ✅ | 191.44 | ✅ | 304.02 |
| test_strided_copy[four_channels] | ✅ | 193.88 | ✅ | 369.18 |
| test_strided_copy[kv_slot0] | ✅ | 179.98 | ✅ | 299.00 |
| test_strided_copy[kv_slot5] | ✅ | 181.80 | ✅ | 341.78 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 180.86 | ✅ | 690.12 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 178.52 | ✅ | 388.26 |
| test_strided_copy[kv_slot_last] | ✅ | 179.44 | ✅ | 417.78 |
| test_strided_copy[two_channels] | ✅ | 155.84 | ✅ | 266.94 |
| test_strided_copy[two_channels_chunked] | ✅ | 158.30 | ✅ | 342.06 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 995.19 | ✅ | 12175.02 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1064.76 | ✅ | 17227.29 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2130.91 | ✅ | 23728.51 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2349.51 | ✅ | 19173.00 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 143.06 | ✅ | 267.62 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 181.58 | ✅ | 432.02 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 179.88 | ✅ | 334.64 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 187.02 | ✅ | 437.26 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 179.56 | ✅ | 484.62 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 212.28 | ✅ | 471.02 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 184.76 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 230.66 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3545.26 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 676.98 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.62 | ✅ | 1212.78 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 257.96 | ✅ | 1089.68 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 175.96 | ✅ | 561.08 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3464.36 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 934.84 | - | - |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003] | ✅ | 192.90 | ✅ | 369.68 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 158.58 | ✅ | 343.14 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 164.98 | ✅ | 391.14 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003] | ✅ | 158.16 | ✅ | 326.70 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 169.18 | ✅ | 497.54 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 173.50 | ✅ | 380.02 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003] | ✅ | 195.00 | ✅ | 462.16 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 192.06 | ✅ | 465.48 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 168.36 | ✅ | 521.82 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_1.003] | ✅ | 204.42 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 240.30 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 211.08 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 155.54 | ✅ | 422.50 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 191.46 | ✅ | 307.82 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 192.72 | ✅ | 362.94 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 170.34 | ✅ | 446.36 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 178.50 | ✅ | 376.16 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 179.02 | ✅ | 376.02 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 162.58 | ✅ | 535.54 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 163.06 | ✅ | 376.72 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 162.34 | ✅ | 442.16 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 167.22 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 172.64 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 161.40 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003] | ✅ | 173.98 | ✅ | 413.10 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 175.38 | ✅ | 381.56 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 191.68 | ✅ | 342.88 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003] | ✅ | 170.24 | ✅ | 362.94 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 169.92 | ✅ | 369.56 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 152.18 | ✅ | 492.28 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003] | ✅ | 186.82 | ✅ | 430.26 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 173.52 | ✅ | 474.36 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 186.44 | ✅ | 310.02 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_1.003] | ✅ | 180.76 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 202.32 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 200.18 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003] | ✅ | 163.44 | ✅ | 394.40 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 174.90 | ✅ | 382.24 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 151.32 | ✅ | 317.44 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003] | ✅ | 167.72 | ✅ | 406.78 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 177.86 | ✅ | 430.26 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 164.66 | ✅ | 443.92 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003] | ✅ | 168.30 | ✅ | 469.80 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 157.38 | ✅ | 540.14 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 163.42 | ✅ | 494.90 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_1.003] | ✅ | 195.98 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 175.58 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 193.78 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4327.38 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 894.46 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 152.22 | ✅ | 442.82 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 148.44 | ✅ | 393.76 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 150.18 | ✅ | 469.84 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 187.64 | ✅ | 393.68 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 160.70 | ✅ | 377.92 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 206.64 | ✅ | 786.80 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 197.42 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 226.38 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 184.74 | ✅ | 430.86 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 165.26 | ✅ | 620.66 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 150.80 | ✅ | 305.40 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 169.78 | ✅ | 462.04 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 193.16 | ✅ | 523.84 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 177.36 | ✅ | 483.18 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 162.38 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 209.40 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 157.38 | ✅ | 351.50 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 165.76 | ✅ | 491.00 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 186.66 | ✅ | 782.84 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 147.38 | ✅ | 539.14 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 192.78 | ✅ | 529.36 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 146.84 | ✅ | 545.30 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 169.74 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 199.12 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 139.70 | ✅ | 377.08 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 172.48 | ✅ | 371.36 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 184.36 | ✅ | 442.56 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 140.96 | ✅ | 459.02 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 148.80 | ✅ | 439.18 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 141.40 | ✅ | 484.68 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 173.60 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 194.50 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 2012.54 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 486.02 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 164.50 | ✅ | 357.64 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 188.64 | ✅ | 540.66 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 189.02 | ✅ | 482.40 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 188.16 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 150.38 | ✅ | 409.02 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 156.34 | ✅ | 462.64 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 160.38 | ✅ | 928.00 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 172.64 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 155.34 | ✅ | 453.02 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 182.86 | ✅ | 439.58 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 187.58 | ✅ | 560.20 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 192.34 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 166.28 | ✅ | 413.68 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 143.80 | ✅ | 688.26 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 153.54 | ✅ | 413.38 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 178.70 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3575.82 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 858.18 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 152.66 | ✅ | 341.16 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 178.32 | ✅ | 434.20 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 175.14 | ✅ | 551.58 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 185.54 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 166.48 | ✅ | 358.98 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 175.82 | ✅ | 360.08 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 191.96 | ✅ | 368.60 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 212.08 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 182.86 | ✅ | 428.40 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 202.68 | ✅ | 358.04 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 178.30 | ✅ | 428.42 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 187.86 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 169.24 | ✅ | 581.20 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 185.34 | ✅ | 472.62 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 193.78 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4320.94 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 875.24 | - | - |

</details>

<details>
<summary>iron/operators/flm/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_e4b_gate_up_interleaved[iter0] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter1] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter2] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter3] | ✅ | - | - | - |
| test_e4b_gate_up_interleaved[iter4] | ✅ | - | - | - |
| test_e4b_shapes[K_10240-N_2560] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_10240] | ✅ | - | - | - |
| test_e4b_shapes[K_2560-N_2560] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter0] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter1] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter2] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter3] | ✅ | - | - | - |
| test_gate_up_interleaved_blob[iter4] | ✅ | - | - | - |
| test_large_k_shapes[K_12288-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | - | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_128] | ✅ | - | - | - |
| test_matches_reference[K_1024-N_512] | ✅ | - | - | - |
| test_matches_reference[K_1536-N_640] | ✅ | - | - | - |
| test_matches_reference[K_2048-N_256] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter0] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter1] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter2] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter3] | ✅ | - | - | - |
| test_output_feeds_gemm_unchanged[iter4] | ✅ | - | - | - |
| test_rejects_unservable_shapes[K_1000-N_128-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_1024-N_100-exc_<class 'ValueError'>-match_multiple of] | ✅ | - | ✅ | - |
| test_rejects_unservable_shapes[K_512-N_128-exc_<class 'NotImplementedError'>-match_tile_n] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | ✅ | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | ✅ | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4005.18 | - | - |
| test_gemm[M_1024-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 3925.28 |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1005.64 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 4144.58 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1408.32 | ✅ | 9801.56 |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7785.78 | - | - |
| test_gemm[M_2048-K_2048-N_1024-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 7056.18 |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1477.70 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7661.26 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 338.36 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 341.48 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 332.48 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 312.12 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 380.68 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 331.02 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 346.38 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 301.60 | ✅ | 1220.06 |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 368.64 | - | - |
| test_gemm[M_256-K_512-N_256-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 607.70 |
| test_gemm[M_256-K_512-N_320-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 550.30 |
| test_gemm[M_256-K_512-N_512-epilogue_gelu-clamp_None-rounding_conv_even] | - | - | ✅ | 931.44 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | - | - | ✅ | 1007.82 |
| test_gemm[M_256-K_512-N_512-epilogue_none-clamp_None-rounding_floor] | - | - | ✅ | 838.40 |
| test_gemm[M_256-K_512-N_512-epilogue_sigmoid-clamp_None-rounding_conv_even] | - | - | ✅ | 932.22 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_conv_even] | - | - | ✅ | 833.00 |
| test_gemm[M_256-K_512-N_512-epilogue_silu-clamp_None-rounding_floor] | - | - | ✅ | 753.58 |
| test_gemm[M_256-K_512-N_64-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 608.66 |
| test_gemm[M_512-K_1024-N_1024-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | - | - | ✅ | 2854.98 |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 449.86 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 473.58 | - | - |
| test_gemm[M_512-K_1024-N_512-epilogue_none-clamp_None-rounding_conv_even] | - | - | ✅ | 1322.90 |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 498.34 | ✅ | 3692.14 |
| test_gemm_split_leg_bounds[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds[iter4] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | ✅ | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32-default] | - | - | ✅ | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64] | - | - | ✅ | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | ❌ | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | ✅ | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | ✅ | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/mm_prebuilt</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1024-epilogue_silu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_1280-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_256-K_512-N_640-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt[M_512-K_1024-N_2048-epilogue_none-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_gelu-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_none-clamp_(-2.0, 2.0)] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_sigmoid-clamp_None] | ✅ | - | - | - |
| test_mm_prebuilt_epilogue_matches_accumulator[epilogue_silu-clamp_None] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 168.02 | ✅ | 469.00 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 171.76 | ✅ | 448.50 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 175.46 | ✅ | 448.04 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 184.78 | ✅ | 333.44 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 172.26 | ✅ | 515.22 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 186.42 | ✅ | 457.34 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 227.48 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 230.36 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 205.94 | ✅ | 379.36 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 184.94 | ✅ | 612.50 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 149.68 | ✅ | 319.94 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 176.88 | ✅ | 390.04 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 161.10 | ✅ | 395.38 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 186.88 | ✅ | 505.20 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 175.64 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 216.00 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 161.84 | ✅ | 374.10 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 169.58 | ✅ | 444.22 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 181.70 | ✅ | 388.00 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 204.20 | ✅ | 468.46 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 181.44 | ✅ | 411.26 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 201.20 | ✅ | 475.16 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 209.72 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 231.22 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 175.56 | ✅ | 407.76 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 187.72 | ✅ | 820.84 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 159.62 | ✅ | 500.50 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 174.74 | ✅ | 367.66 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 206.46 | ✅ | 514.58 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 175.84 | ✅ | 507.18 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 172.50 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 185.30 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3857.66 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 656.82 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 18909.52 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2039.90 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 215.12 | ✅ | 573.38 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 225.14 | ✅ | 752.88 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47059.62 | ✅ | 82589.32 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-partition_N_1] | ✅ | 119368.10 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27727.14 | ✅ | 18618.08 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-partition_N_1] | ✅ | 6877.20 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-partition_N_1] | ✅ | 8238.28 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7728.92 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93220.12 | ✅ | 91744.40 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100926.36 | ✅ | 93046.70 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 107194.68 | ✅ | 73486.08 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 37069.90 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1070.62 | ✅ | 2906.10 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 1131.82 | ✅ | 2796.36 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1244.20 | ✅ | 3272.24 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3613.70 | ✅ | 6115.00 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 3899.10 | ✅ | 7927.54 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 4032.90 | ✅ | 5913.58 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93196.46 | ✅ | 96570.98 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100759.24 | ✅ | 96905.68 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 106454.34 | ✅ | 75817.58 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2309.96 | ✅ | 4735.46 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3016.56 | ✅ | 6836.14 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1285.88 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 154.34 | ✅ | 423.88 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2755.22 | ✅ | 9580.52 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1392.68 | ✅ | 6215.52 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 840.02 | ✅ | 4207.58 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 780.06 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2642.86 | ✅ | 9467.18 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1380.04 | ✅ | 5424.14 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 877.70 | ✅ | 4259.90 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 798.00 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 477.22 | ✅ | 3382.20 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 311.94 | ✅ | 1866.58 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 272.46 | ✅ | 1406.32 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 445.12 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 978.46 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 232.02 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 269.10 | ✅ | 1873.64 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 149.88 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2638.92 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2659.42 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 230.88 | ✅ | 660.48 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 174.54 | ✅ | 384.62 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 173.54 | ✅ | 540.40 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 207.54 | ✅ | 387.18 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 200.34 | ✅ | 479.28 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 183.42 | ✅ | 463.66 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 173.72 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 219.20 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 158.08 | ✅ | 474.04 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 163.68 | ✅ | 693.54 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 164.02 | ✅ | 503.88 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 190.88 | ✅ | 794.50 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 177.04 | ✅ | 511.88 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 208.78 | ✅ | 440.40 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 194.74 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 203.62 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 179.50 | ✅ | 443.60 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 172.68 | ✅ | 241.32 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 166.54 | ✅ | 477.90 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 180.90 | ✅ | 495.16 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 169.86 | ✅ | 443.78 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 192.84 | ✅ | 548.24 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 202.92 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 193.80 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 189.28 | ✅ | 372.28 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 200.18 | ✅ | 343.36 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 189.54 | ✅ | 361.22 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 162.32 | ✅ | 289.30 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 178.40 | ✅ | 411.18 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 183.78 | ✅ | 483.90 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 192.86 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 248.16 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3678.66 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 684.88 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 163.78 | ✅ | 291.66 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 180.72 | ✅ | 697.42 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 179.46 | ✅ | 740.62 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 190.40 | ✅ | 618.46 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 183.38 | ✅ | 373.12 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 203.44 | ✅ | 551.46 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 183.46 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 211.92 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 214.34 | ✅ | 384.36 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 172.90 | ✅ | 397.14 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 174.72 | ✅ | 440.42 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 181.00 | ✅ | 459.58 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 179.80 | ✅ | 367.66 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 182.14 | ✅ | 779.82 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 211.08 | ✅ | 438.92 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 176.64 | ✅ | 553.00 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 184.08 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 211.80 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 168.10 | ✅ | 352.82 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 195.18 | ✅ | 465.46 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 184.16 | ✅ | 331.98 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 186.20 | ✅ | 313.48 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 192.30 | ✅ | 497.12 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 213.28 | ✅ | 433.62 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 169.52 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 216.14 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 165.64 | ✅ | 532.46 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 157.48 | ✅ | 456.24 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 174.50 | ✅ | 392.98 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 177.06 | ✅ | 356.06 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 198.30 | ✅ | 480.06 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 183.68 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 217.14 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 3738.82 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 773.86 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 159.80 | ✅ | 337.52 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 154.14 | ✅ | 779.66 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 182.70 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 188.14 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 150.36 | ✅ | 370.60 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 166.84 | ✅ | 366.90 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 169.72 | ✅ | 474.40 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 155.38 | ✅ | 444.64 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 162.30 | ✅ | 413.96 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 179.12 | ✅ | 365.10 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 159.60 | ✅ | 414.00 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 155.98 | ✅ | 500.40 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 188.10 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 178.94 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 156.98 | ✅ | 517.72 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 179.60 | ✅ | 432.56 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 159.38 | ✅ | 360.28 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 158.22 | ✅ | 330.84 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 194.98 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 190.06 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 180.88 | ✅ | 340.90 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 162.86 | ✅ | 311.98 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 176.20 | ✅ | 598.38 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 159.18 | ✅ | 324.00 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 189.20 | ✅ | 457.18 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 185.04 | ✅ | 425.28 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 175.48 | ✅ | 342.60 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 169.02 | ✅ | 320.04 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 172.92 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 190.28 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 188.12 | ✅ | 496.16 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 189.34 | ✅ | 702.50 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 152.90 | ✅ | 382.14 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 181.50 | ✅ | 320.22 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 218.14 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 189.08 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 158.02 | ✅ | 499.80 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 150.26 | ✅ | 402.64 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 185.94 | ✅ | 355.66 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 174.30 | ✅ | 356.56 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 196.70 | ✅ | 764.06 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 181.36 | ✅ | 418.24 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 193.40 | ✅ | 466.74 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 225.56 | ✅ | 706.34 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 197.00 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 210.00 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 174.74 | ✅ | 476.52 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 165.90 | ✅ | 382.82 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 157.16 | ✅ | 379.58 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 170.10 | ✅ | 347.76 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 192.34 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 191.28 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 169.64 | ✅ | 332.38 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 161.54 | ✅ | 385.06 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 160.54 | ✅ | 409.84 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 156.54 | ✅ | 325.68 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 167.08 | ✅ | 621.64 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 157.44 | ✅ | 381.56 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 165.70 | ✅ | 334.46 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 150.98 | ✅ | 423.76 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 172.80 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 166.34 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 164.90 | ✅ | 462.68 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 160.56 | ✅ | 716.02 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 732.76 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3608.52 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 17138.84 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 17431.72 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 151636.48 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 161.06 | ✅ | 421.30 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 186.76 | ✅ | 307.24 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 177.32 | ✅ | 367.32 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 176.82 | ✅ | 572.40 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 183.76 | ✅ | 855.10 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 177.98 | ✅ | 460.40 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 179.76 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 218.24 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 164.72 | ✅ | 420.10 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 167.48 | ✅ | 334.90 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 158.26 | ✅ | 633.26 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 180.90 | ✅ | 356.70 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.26 | ✅ | 471.40 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 196.08 | ✅ | 490.26 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 189.10 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 271.34 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 172.68 | ✅ | 426.46 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 179.72 | ✅ | 426.32 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 187.48 | ✅ | 431.64 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 174.04 | ✅ | 509.04 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 214.62 | ✅ | 446.14 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 205.50 | ✅ | 788.14 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 189.32 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 218.08 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 158.08 | ✅ | 270.76 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 168.34 | ✅ | 633.72 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 184.76 | ✅ | 425.50 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 178.74 | ✅ | 425.86 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 207.66 | ✅ | 449.64 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 239.02 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 253.60 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2510.62 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 743.96 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 203.52 | ✅ | 408.48 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 190.26 | ✅ | 404.18 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 828.58 | ✅ | 3211.38 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 173.54 | ✅ | 433.14 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 159.06 | ✅ | 287.96 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 177.62 | ✅ | 501.90 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 176.56 | ✅ | 502.10 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 191.54 | ✅ | 346.26 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 164.14 | ✅ | 469.64 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 180.90 | ✅ | 322.20 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 171.66 | ✅ | 535.32 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 174.90 | ✅ | 446.58 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 187.86 | ✅ | 555.12 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 197.30 | ✅ | 505.40 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 196.18 | ✅ | 443.36 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 185.54 | ✅ | 521.96 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 196.92 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 172.78 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 195.88 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 226.46 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 156.02 | ✅ | 448.26 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 153.88 | ✅ | 503.80 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 158.58 | ✅ | 413.30 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 187.36 | ✅ | 486.40 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 172.00 | ✅ | 435.30 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 180.02 | ✅ | 426.44 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 167.92 | ✅ | 344.18 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 202.36 | ✅ | 503.38 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 184.30 | ✅ | 422.84 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 186.52 | ✅ | 419.86 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 210.76 | ✅ | 758.96 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 195.80 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 154.26 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 212.00 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 208.54 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 231.72 | ✅ | 261.40 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 184.76 | ✅ | 425.06 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 171.04 | ✅ | 577.72 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 159.88 | ✅ | 534.78 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 165.02 | ✅ | 401.88 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 175.44 | ✅ | 488.62 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 176.34 | ✅ | 510.22 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 167.46 | ✅ | 432.74 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 165.56 | ✅ | 735.26 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 162.02 | ✅ | 1176.66 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 190.38 | ✅ | 534.56 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 211.12 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 190.72 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 222.38 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 239.54 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 183.90 | ✅ | 378.56 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 151.74 | ✅ | 387.58 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 163.30 | ✅ | 472.04 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 188.44 | ✅ | 701.84 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 175.26 | ✅ | 535.60 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 186.18 | ✅ | 487.26 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 170.52 | ✅ | 567.44 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 180.80 | ✅ | 522.62 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 197.70 | ✅ | 504.82 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 194.14 | ✅ | 443.62 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 228.04 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 185.68 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 189.88 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 187.68 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3673.94 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3364.80 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 712.36 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 843.02 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 164.08 | ✅ | 350.92 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 175.68 | ✅ | 345.18 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 175.98 | ✅ | 403.10 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 159.74 | ✅ | 310.16 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 145.06 | ✅ | 466.28 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 161.60 | ✅ | 457.90 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 199.76 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 197.08 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 170.44 | ✅ | 523.36 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 164.94 | ✅ | 309.50 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 200.44 | ✅ | 478.88 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 148.08 | ✅ | 379.08 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 182.96 | ✅ | 511.58 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 155.10 | ✅ | 504.94 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 226.10 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 177.04 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 155.62 | ✅ | 304.64 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 168.62 | ✅ | 376.48 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 164.96 | ✅ | 329.54 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 182.54 | ✅ | 426.80 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 173.02 | ✅ | 467.28 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 177.96 | ✅ | 593.00 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 207.96 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 195.36 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 175.42 | ✅ | 476.56 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 161.38 | ✅ | 571.06 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 164.64 | ✅ | 546.50 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 198.16 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 174.72 | ✅ | 374.88 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 182.48 | ✅ | 397.78 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 176.06 | ✅ | 437.56 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 203.50 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1034.64 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 298.04 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 181.78 | ✅ | 366.96 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 197.74 | ✅ | 276.16 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 167.26 | ✅ | 500.60 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 193.92 | ✅ | 431.80 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 191.76 | ✅ | 424.90 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 163.38 | ✅ | 430.74 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 184.98 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 217.90 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 187.52 | ✅ | 273.72 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 158.38 | ✅ | 372.28 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 190.94 | ✅ | 731.24 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 184.68 | ✅ | 416.22 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 177.54 | ✅ | 489.36 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 172.12 | ✅ | 493.60 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 167.64 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 191.16 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 159.38 | ✅ | 373.94 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 177.42 | ✅ | 362.74 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 185.46 | ✅ | 532.40 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 182.96 | ✅ | 456.96 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 212.08 | ✅ | 390.12 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 185.50 | ✅ | 307.20 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 191.44 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 185.70 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 160.16 | ✅ | 336.06 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 154.00 | ✅ | 376.80 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 155.06 | ✅ | 429.94 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 162.90 | ✅ | 422.44 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 168.50 | ✅ | 861.76 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 180.68 | ✅ | 726.96 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 195.20 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 233.02 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 172.06 | ✅ | 430.64 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 188.08 | ✅ | 402.66 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 145.36 | ✅ | 431.88 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 158.36 | ✅ | 500.50 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 181.38 | ✅ | 426.12 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 183.90 | ✅ | 420.60 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 169.28 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 228.06 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 135.08 | ✅ | 348.42 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 169.02 | ✅ | 416.76 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 161.82 | ✅ | 415.08 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 185.64 | ✅ | 431.18 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 178.96 | ✅ | 397.22 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 201.00 | ✅ | 816.68 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 201.74 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 257.52 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 165.96 | ✅ | 399.24 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 162.30 | ✅ | 423.12 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 182.58 | ✅ | 560.78 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 153.76 | ✅ | 466.22 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 175.50 | ✅ | 541.48 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 167.48 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 206.12 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3912.88 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 695.06 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 140.34 | ✅ | 312.92 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 162.26 | ✅ | 754.64 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 174.00 | ✅ | 399.18 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 198.24 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 163.02 | ✅ | 272.60 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.26 | ✅ | 422.24 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 186.92 | ✅ | 432.76 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 184.96 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 151.26 | ✅ | 353.20 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 177.30 | ✅ | 368.12 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 157.16 | ✅ | 460.04 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 189.56 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 149.74 | ✅ | 326.74 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 157.34 | ✅ | 415.32 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 197.80 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4401.06 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 756.54 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 513.52 | ✅ | 1935.76 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 166.42 | ✅ | 545.06 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 184.76 | ✅ | 851.58 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 180.74 | ✅ | 522.42 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 503.00 | ✅ | 2849.78 |
| test_strided_copy[chunked_transfer] | ✅ | 158.30 | ✅ | 324.42 |
| test_strided_copy[contiguous] | ✅ | 165.52 | ✅ | 424.20 |
| test_strided_copy[four_channels] | ✅ | 189.24 | ✅ | 472.46 |
| test_strided_copy[kv_llama_full] | ✅ | 148.86 | ✅ | 695.60 |
| test_strided_copy[kv_slot0] | ✅ | 158.82 | ✅ | 399.22 |
| test_strided_copy[kv_slot5] | ✅ | 155.90 | ✅ | 452.20 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 180.70 | ✅ | 477.36 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 179.44 | ✅ | 418.32 |
| test_strided_copy[kv_slot_last] | ✅ | 172.62 | ✅ | 415.36 |
| test_strided_copy[two_channels] | ✅ | 179.66 | ✅ | 429.50 |
| test_strided_copy[two_channels_chunked] | ✅ | 171.28 | ✅ | 467.94 |
| test_strided_copy_cache_offset_parameter[iter0] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter1] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter2] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter3] | ✅ | - | - | - |
| test_strided_copy_cache_offset_parameter[iter4] | ✅ | - | - | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter0] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter1] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter2] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter3] | ✅ | - | ✅ | - |
| test_transfer_size_not_dividing_per_channel_share_is_rejected[iter4] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/swiglu_decode</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 1007.32 | ✅ | 15977.05 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1054.89 | ✅ | 16173.97 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2188.36 | ✅ | 19073.75 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2349.20 | ✅ | 19826.08 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 167.66 | ✅ | 317.18 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 180.82 | ✅ | 492.56 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 183.30 | ✅ | 525.00 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 187.36 | ✅ | 720.38 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 189.54 | ✅ | 428.30 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 216.14 | ✅ | 521.80 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 186.10 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 262.26 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 160.66 | ✅ | 460.94 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 176.62 | ✅ | 398.60 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 178.70 | ✅ | 370.94 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 160.82 | ✅ | 250.00 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 145.48 | ✅ | 337.12 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 198.28 | ✅ | 828.50 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 170.64 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 233.84 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 146.24 | ✅ | 328.18 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 168.14 | ✅ | 269.10 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 176.72 | ✅ | 473.02 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 179.30 | ✅ | 384.32 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 194.54 | ✅ | 384.30 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 196.86 | ✅ | 442.42 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 182.22 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 191.20 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 179.28 | ✅ | 491.98 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 154.52 | ✅ | 350.02 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 176.42 | ✅ | 483.52 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 193.76 | ✅ | 374.16 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 209.06 | ✅ | 452.52 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 186.24 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 218.58 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3499.70 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 684.10 | - | - |

</details>

<details>
<summary>iron/operators/transpose</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_2048-N_128-aie_columns_8-channels_1-m_256-n_32-bad_num_aie_columns] | ✅ | - | ✅ | - |
| test_a_dimension_that_floors_to_zero_is_refused_by_name[M_256-N_2048-aie_columns_1-channels_2-m_256-n_32-bad_num_channels] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_1] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_2] | ✅ | - | ✅ | - |
| test_a_tiling_that_fits_is_still_accepted[aie_columns_4] | ✅ | - | ✅ | - |
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 243.54 | ✅ | 1708.78 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 218.02 | ✅ | 649.08 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 238.80 | ✅ | 785.04 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 232.86 | ✅ | 900.08 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 277.28 | ✅ | 1034.36 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 282.36 | ✅ | 1277.76 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 282.20 | ✅ | 1376.92 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 267.52 | ✅ | 621.00 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 277.44 | ✅ | 1636.18 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 266.32 | ✅ | 1905.84 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 375.22 | ✅ | 2091.04 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 354.88 | ✅ | 1490.42 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 382.04 | ✅ | 3025.36 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 343.84 | ✅ | 1481.50 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 332.88 | ✅ | 1404.16 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 347.84 | ✅ | 1770.34 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 315.88 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 353.28 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 226.54 | ✅ | 1073.54 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 242.16 | ✅ | 630.50 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 274.14 | ✅ | 2420.86 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 210.16 | ✅ | 503.32 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 190.72 | ✅ | 423.46 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 173.38 | ✅ | 312.32 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 179.50 | ✅ | 381.74 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 191.08 | ✅ | 646.64 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 199.94 | ✅ | 403.14 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 193.58 | ✅ | 485.76 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 182.74 | ✅ | 318.84 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 188.24 | ✅ | 599.00 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 199.30 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 176.44 | ✅ | 376.64 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3704.36 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 976.84 | - | - |

</details>

