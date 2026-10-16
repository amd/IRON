# IRON - CI Summary

## Examples

<details>
<summary>iron/applications/gemma4_flm</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_iron_matches_engine[prompt_long_prompt] | ✅ | - | - | - |
| test_iron_matches_engine[prompt_word_problem] | ✅ | - | - | - |

</details>

<details>
<summary>iron/applications/gemma4_flm/gemm_dequant</summary>

| Test | Krackan Status | Krackan | Phoenix Status | Phoenix |
|---|---|---|---|---|
| test_all_gemm_dequant_selections[iter0] | ✅ | - | - | - |
| test_all_gemm_dequant_selections[iter1] | ✅ | - | - | - |
| test_all_gemm_dequant_selections[iter2] | ✅ | - | - | - |
| test_all_gemm_dequant_selections[iter3] | ✅ | - | - | - |
| test_all_gemm_dequant_selections[iter4] | ✅ | - | - | - |
| test_example_overrides_only_gemm_and_dequant[iter0] | ✅ | - | ✅ | - |
| test_example_overrides_only_gemm_and_dequant[iter1] | ✅ | - | ✅ | - |
| test_example_overrides_only_gemm_and_dequant[iter2] | ✅ | - | ✅ | - |
| test_example_overrides_only_gemm_and_dequant[iter3] | ✅ | - | ✅ | - |
| test_example_overrides_only_gemm_and_dequant[iter4] | ✅ | - | ✅ | - |
| test_offline_dequant_layout_is_a_permutation[iter0] | ✅ | - | ✅ | - |
| test_offline_dequant_layout_is_a_permutation[iter1] | ✅ | - | ✅ | - |
| test_offline_dequant_layout_is_a_permutation[iter2] | ✅ | - | ✅ | - |
| test_offline_dequant_layout_is_a_permutation[iter3] | ✅ | - | ✅ | - |
| test_offline_dequant_layout_is_a_permutation[iter4] | ✅ | - | ✅ | - |
| test_offline_dequant_uses_floor_rounding[iter0] | ✅ | - | ✅ | - |
| test_offline_dequant_uses_floor_rounding[iter1] | ✅ | - | ✅ | - |
| test_offline_dequant_uses_floor_rounding[iter2] | ✅ | - | ✅ | - |
| test_offline_dequant_uses_floor_rounding[iter3] | ✅ | - | ✅ | - |
| test_offline_dequant_uses_floor_rounding[iter4] | ✅ | - | ✅ | - |
| test_offline_dequant_writes_a_sidecar[iter0] | ✅ | - | ✅ | - |
| test_offline_dequant_writes_a_sidecar[iter1] | ✅ | - | ✅ | - |
| test_offline_dequant_writes_a_sidecar[iter2] | ✅ | - | ✅ | - |
| test_offline_dequant_writes_a_sidecar[iter3] | ✅ | - | ✅ | - |
| test_offline_dequant_writes_a_sidecar[iter4] | ✅ | - | ✅ | - |
| test_plot_contains_all_selections[iter0] | ✅ | - | ✅ | - |
| test_plot_contains_all_selections[iter1] | ✅ | - | ✅ | - |
| test_plot_contains_all_selections[iter2] | ✅ | - | ✅ | - |
| test_plot_contains_all_selections[iter3] | ✅ | - | ✅ | - |
| test_plot_contains_all_selections[iter4] | ✅ | - | ✅ | - |
| test_prepare_model_links_inputs_and_owns_sidecars[iter0] | ✅ | - | ✅ | - |
| test_prepare_model_links_inputs_and_owns_sidecars[iter1] | ✅ | - | ✅ | - |
| test_prepare_model_links_inputs_and_owns_sidecars[iter2] | ✅ | - | ✅ | - |
| test_prepare_model_links_inputs_and_owns_sidecars[iter3] | ✅ | - | ✅ | - |
| test_prepare_model_links_inputs_and_owns_sidecars[iter4] | ✅ | - | ✅ | - |

</details>

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
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 160.10 | ✅ | 388.58 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 156.76 | ✅ | 315.26 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 185.62 | ✅ | 301.76 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 194.14 | ✅ | 786.24 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 205.12 | ✅ | 482.08 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 177.16 | ✅ | 480.72 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 211.06 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 197.46 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 3171.00 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 879.12 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 163.40 | ✅ | 345.22 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 163.06 | ✅ | 337.98 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 174.30 | ✅ | 424.26 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 154.56 | ✅ | 354.20 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 190.18 | ✅ | 497.02 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 200.06 | ✅ | 476.98 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 178.82 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 250.24 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1742.28 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 461.80 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 161.86 | ✅ | 318.48 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 175.64 | ✅ | 774.70 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 186.88 | ✅ | 474.40 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 200.18 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4325.02 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 937.60 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 160.40 | ✅ | 262.60 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 183.28 | ✅ | 738.12 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 215.20 | ✅ | 528.12 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 189.74 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 4236.56 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 868.10 | - | - |

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
| test_large_k_shapes[K_4096-N_1536] | ✅ | 740.72 | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | 913.48 | - | - |
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
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 317.14 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 348.58 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 315.22 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 345.84 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 329.66 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 287.22 | - | - |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 355.78 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 421.86 | - | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 815.18 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 879.00 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 1193.40 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 1281.66 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 885.60 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 739.02 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 782.78 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 849.80 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 841.46 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 1222.08 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 1229.14 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 1148.38 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 1060.96 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 1049.62 | - | - |
| test_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/lm_head</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_softcap[dim_1536] | ✅ | - | - | - |
| test_gemma4_softcap[dim_2560] | ✅ | - | - | - |
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_inf-match_finite and positive] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter0] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter1] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter2] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter3] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 374.98 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 371.98 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 772.44 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 772.04 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1820.46 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 1822.10 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1002.66 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1000.80 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4510.48 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4495.26 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1992.66 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1916.66 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 217.64 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 217.16 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 800.82 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 802.96 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2353.44 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2358.72 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1252.10 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1254.20 | - | - |
| test_one_callable_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_callable_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 4}-match_query heads] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 157.72 | ✅ | 352.18 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 156.16 | ✅ | 338.90 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.58 | ✅ | 301.02 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 186.58 | ✅ | 349.14 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 183.46 | ✅ | 387.34 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 201.34 | ✅ | 413.58 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 193.22 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 233.12 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 4148.70 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 705.08 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2214.04 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 204.30 | ✅ | 793.14 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 244.14 | ✅ | 540.70 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47055.58 | ✅ | 82623.54 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27544.24 | ✅ | 18700.38 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7741.98 | - | - |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2231.86 | ✅ | 3119.68 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3605.60 | ✅ | 5826.20 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1510.48 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 178.76 | ✅ | 403.12 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2696.12 | ✅ | 9394.60 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1447.26 | ✅ | 5462.54 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 872.82 | ✅ | 4193.36 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 799.04 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2912.26 | ✅ | 9283.16 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1387.78 | ✅ | 5773.96 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 876.82 | ✅ | 4489.64 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 822.16 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 530.56 | ✅ | 1456.78 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 311.24 | ✅ | 753.30 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 233.00 | ✅ | 1113.12 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 421.96 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 961.66 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 228.04 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 272.20 | ✅ | 2034.62 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 171.46 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2685.88 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2628.86 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 157.58 | ✅ | 343.84 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 138.90 | ✅ | 417.28 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 164.88 | ✅ | 455.90 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 192.42 | ✅ | 389.86 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 154.60 | ✅ | 444.90 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 200.38 | ✅ | 495.88 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 177.70 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 229.96 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 1677.82 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 720.54 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 157.12 | ✅ | 323.94 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 178.26 | ✅ | 328.28 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 150.76 | ✅ | 286.18 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 203.96 | ✅ | 350.04 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 147.48 | ✅ | 393.58 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 179.84 | ✅ | 374.82 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 153.90 | ✅ | 367.92 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 186.76 | ✅ | 420.72 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 194.36 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 228.00 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 3222.94 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 667.10 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 145.24 | ✅ | 331.66 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 220.92 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 157.50 | ✅ | 633.20 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 161.86 | ✅ | 398.78 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 175.96 | ✅ | 419.90 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 182.68 | ✅ | 606.96 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 162.94 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 205.16 | ✅ | 418.96 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 687.62 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3593.18 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 16672.24 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 162.48 | ✅ | 329.86 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 189.10 | ✅ | 434.92 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 162.48 | ✅ | 340.16 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 157.76 | ✅ | 488.88 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 173.10 | ✅ | 416.00 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 147.18 | ✅ | 481.20 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 159.74 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 220.44 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3276.48 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 677.84 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 169.12 | ✅ | 425.78 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 177.14 | ✅ | 479.30 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 170.24 | ✅ | 358.30 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 167.02 | ✅ | 355.36 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 164.84 | ✅ | 400.14 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 154.84 | ✅ | 355.10 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 172.22 | ✅ | 277.84 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 167.94 | ✅ | 441.74 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 181.02 | ✅ | 362.58 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 166.16 | ✅ | 492.98 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 188.00 | ✅ | 443.98 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 198.40 | ✅ | 375.82 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 193.68 | ✅ | 483.54 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 172.76 | ✅ | 758.52 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 213.32 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 187.12 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 224.18 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 226.86 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3844.16 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3680.30 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 799.98 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 666.34 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 164.34 | ✅ | 495.62 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 166.78 | ✅ | 461.72 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 181.82 | ✅ | 1046.88 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 185.58 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 149.52 | ✅ | 332.82 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 174.98 | ✅ | 828.20 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 186.90 | ✅ | 489.82 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 194.16 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1635.44 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 287.70 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 150.82 | ✅ | 755.10 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 143.10 | ✅ | 394.96 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 180.82 | ✅ | 416.44 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 159.08 | ✅ | 426.74 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 150.96 | ✅ | 399.88 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 158.96 | ✅ | 392.58 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 170.14 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 206.76 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3248.88 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 712.32 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 179.10 | ✅ | 340.68 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 161.20 | ✅ | 413.16 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 148.88 | ✅ | 525.26 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 155.16 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 4448.72 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 610.88 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 536.28 | ✅ | 2193.66 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 189.06 | ✅ | 946.38 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 179.38 | ✅ | 566.20 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 190.44 | ✅ | 716.58 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 485.34 | ✅ | 2578.28 |
| test_strided_copy[chunked_transfer] | ✅ | 176.12 | ✅ | 369.48 |
| test_strided_copy[contiguous] | ✅ | 172.38 | ✅ | 330.40 |
| test_strided_copy[four_channels] | ✅ | 187.18 | ✅ | 396.02 |
| test_strided_copy[kv_slot0] | ✅ | 179.10 | ✅ | 353.84 |
| test_strided_copy[kv_slot5] | ✅ | 170.18 | ✅ | 321.32 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 172.06 | ✅ | 382.98 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 172.78 | ✅ | 389.24 |
| test_strided_copy[kv_slot_last] | ✅ | 169.96 | ✅ | 415.08 |
| test_strided_copy[two_channels] | ✅ | 163.34 | ✅ | 396.40 |
| test_strided_copy[two_channels_chunked] | ✅ | 166.56 | ✅ | 367.62 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 1016.79 | ✅ | 16918.62 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1047.05 | ✅ | 16139.97 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2121.02 | ✅ | 26153.01 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2308.30 | ✅ | 22847.40 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 156.80 | ✅ | 416.86 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 166.04 | ✅ | 373.42 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 210.12 | ✅ | 454.24 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 193.14 | ✅ | 329.22 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 171.48 | ✅ | 373.74 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 185.02 | ✅ | 471.58 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 188.38 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 212.98 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3792.26 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 689.38 | - | - |

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
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 195.24 | ✅ | 459.84 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 226.72 | ✅ | 2297.32 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 172.58 | ✅ | 704.42 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3365.24 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 1061.66 | - | - |

</details>

## Extensive

<details>
<summary>iron/operators/axpy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_1.003] | ✅ | 200.74 | ✅ | 366.06 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_10.0] | ✅ | 164.18 | ✅ | 302.02 |
| test_axpy[input_length_1024-num_aie_columns_1-tile_size_1024-scalar_factor_3.0] | ✅ | 162.94 | ✅ | 431.60 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_1.003] | ✅ | 164.54 | ✅ | 413.20 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_10.0] | ✅ | 159.50 | ✅ | 364.08 |
| test_axpy[input_length_1024-num_aie_columns_2-tile_size_512-scalar_factor_3.0] | ✅ | 184.26 | ✅ | 419.72 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_1.003] | ✅ | 174.26 | ✅ | 515.34 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_10.0] | ✅ | 171.88 | ✅ | 543.86 |
| test_axpy[input_length_1024-num_aie_columns_4-tile_size_256-scalar_factor_3.0] | ✅ | 190.70 | ✅ | 475.26 |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_1.003] | ✅ | 211.26 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_10.0] | ✅ | 183.48 | - | - |
| test_axpy[input_length_1024-num_aie_columns_8-tile_size_128-scalar_factor_3.0] | ✅ | 203.20 | - | - |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_1.003] | ✅ | 170.08 | ✅ | 705.86 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_10.0] | ✅ | 176.76 | ✅ | 498.32 |
| test_axpy[input_length_2048-num_aie_columns_1-tile_size_2048-scalar_factor_3.0] | ✅ | 175.50 | ✅ | 732.12 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_1.003] | ✅ | 170.06 | ✅ | 343.84 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_10.0] | ✅ | 165.36 | ✅ | 227.22 |
| test_axpy[input_length_2048-num_aie_columns_2-tile_size_1024-scalar_factor_3.0] | ✅ | 171.30 | ✅ | 363.82 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_1.003] | ✅ | 157.14 | ✅ | 875.76 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_10.0] | ✅ | 188.30 | ✅ | 529.96 |
| test_axpy[input_length_2048-num_aie_columns_4-tile_size_512-scalar_factor_3.0] | ✅ | 187.96 | ✅ | 466.08 |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_1.003] | ✅ | 175.28 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_10.0] | ✅ | 201.74 | - | - |
| test_axpy[input_length_2048-num_aie_columns_8-tile_size_256-scalar_factor_3.0] | ✅ | 213.60 | - | - |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_1.003] | ✅ | 143.90 | ✅ | 346.88 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_10.0] | ✅ | 165.46 | ✅ | 350.44 |
| test_axpy[input_length_4096-num_aie_columns_1-tile_size_4096-scalar_factor_3.0] | ✅ | 154.92 | ✅ | 238.18 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_1.003] | ✅ | 166.18 | ✅ | 473.18 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_10.0] | ✅ | 171.02 | ✅ | 312.76 |
| test_axpy[input_length_4096-num_aie_columns_2-tile_size_2048-scalar_factor_3.0] | ✅ | 155.56 | ✅ | 334.40 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_1.003] | ✅ | 157.64 | ✅ | 414.88 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_10.0] | ✅ | 188.30 | ✅ | 464.04 |
| test_axpy[input_length_4096-num_aie_columns_4-tile_size_1024-scalar_factor_3.0] | ✅ | 175.18 | ✅ | 435.90 |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_1.003] | ✅ | 190.06 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_10.0] | ✅ | 200.80 | - | - |
| test_axpy[input_length_4096-num_aie_columns_8-tile_size_512-scalar_factor_3.0] | ✅ | 179.82 | - | - |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_1.003] | ✅ | 155.32 | ✅ | 774.84 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_10.0] | ✅ | 151.26 | ✅ | 466.78 |
| test_axpy[input_length_8192-num_aie_columns_1-tile_size_8192-scalar_factor_3.0] | ✅ | 159.60 | ✅ | 312.86 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_1.003] | ✅ | 154.32 | ✅ | 787.00 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_10.0] | ✅ | 164.80 | ✅ | 436.50 |
| test_axpy[input_length_8192-num_aie_columns_2-tile_size_4096-scalar_factor_3.0] | ✅ | 153.14 | ✅ | 682.92 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_1.003] | ✅ | 182.28 | ✅ | 780.06 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_10.0] | ✅ | 178.58 | ✅ | 610.22 |
| test_axpy[input_length_8192-num_aie_columns_4-tile_size_2048-scalar_factor_3.0] | ✅ | 188.22 | ✅ | 707.68 |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_1.003] | ✅ | 196.60 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_10.0] | ✅ | 183.92 | - | - |
| test_axpy[input_length_8192-num_aie_columns_8-tile_size_1024-scalar_factor_3.0] | ✅ | 218.72 | - | - |
| test_axpy[input_length_8388608-num_aie_columns_4-tile_size_4096-scalar_factor_3.0] | - | - | ✅ | 4572.42 |
| test_axpy[input_length_8388608-num_aie_columns_8-tile_size_4096-scalar_factor_3.0] | ✅ | 918.52 | - | - |

</details>

<details>
<summary>iron/operators/dequant</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-group_size_32] | ✅ | 148.88 | ✅ | 364.08 |
| test_dequant[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-group_size_32] | ✅ | 145.06 | ✅ | 669.42 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-group_size_32] | ✅ | 158.04 | ✅ | 406.80 |
| test_dequant[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-group_size_32] | ✅ | 156.56 | ✅ | 384.14 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-group_size_32] | ✅ | 157.70 | ✅ | 419.34 |
| test_dequant[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-group_size_32] | ✅ | 160.20 | ✅ | 811.50 |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-group_size_32] | ✅ | 224.18 | - | - |
| test_dequant[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-group_size_32] | ✅ | 234.32 | - | - |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-group_size_32] | ✅ | 167.14 | ✅ | 322.90 |
| test_dequant[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-group_size_32] | ✅ | 162.14 | ✅ | 360.32 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-group_size_32] | ✅ | 159.98 | ✅ | 484.72 |
| test_dequant[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-group_size_32] | ✅ | 170.02 | ✅ | 443.54 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-group_size_32] | ✅ | 174.50 | ✅ | 454.78 |
| test_dequant[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-group_size_32] | ✅ | 167.84 | ✅ | 510.38 |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-group_size_32] | ✅ | 176.68 | - | - |
| test_dequant[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-group_size_32] | ✅ | 234.70 | - | - |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-group_size_32] | ✅ | 173.24 | ✅ | 337.40 |
| test_dequant[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-group_size_32] | ✅ | 148.28 | ✅ | 304.92 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-group_size_32] | ✅ | 152.54 | ✅ | 467.84 |
| test_dequant[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-group_size_32] | ✅ | 178.20 | ✅ | 358.78 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-group_size_32] | ✅ | 169.22 | ✅ | 471.28 |
| test_dequant[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-group_size_32] | ✅ | 196.78 | ✅ | 514.12 |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-group_size_32] | ✅ | 179.78 | - | - |
| test_dequant[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-group_size_32] | ✅ | 213.24 | - | - |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-group_size_32] | ✅ | 159.46 | ✅ | 304.10 |
| test_dequant[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-group_size_32] | ✅ | 210.88 | ✅ | 365.76 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-group_size_32] | ✅ | 175.06 | ✅ | 334.86 |
| test_dequant[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-group_size_32] | ✅ | 174.56 | ✅ | 322.88 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-group_size_32] | ✅ | 168.52 | ✅ | 869.98 |
| test_dequant[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-group_size_32] | ✅ | 211.10 | ✅ | 1076.12 |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-group_size_32] | ✅ | 189.20 | - | - |
| test_dequant[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-group_size_32] | ✅ | 269.64 | - | - |
| test_dequant[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-group_size_32] | - | - | ✅ | 1471.10 |
| test_dequant[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-group_size_32] | ✅ | 475.14 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_add</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_add[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 158.16 | ✅ | 409.30 |
| test_elementwise_add[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 151.70 | ✅ | 646.00 |
| test_elementwise_add[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 168.68 | ✅ | 477.38 |
| test_elementwise_add[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 192.36 | - | - |
| test_elementwise_add[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 179.72 | ✅ | 403.66 |
| test_elementwise_add[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 168.54 | ✅ | 439.16 |
| test_elementwise_add[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 176.86 | ✅ | 475.32 |
| test_elementwise_add[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 199.78 | - | - |
| test_elementwise_add[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 201.52 | ✅ | 455.46 |
| test_elementwise_add[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 166.16 | ✅ | 446.20 |
| test_elementwise_add[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 189.88 | ✅ | 475.50 |
| test_elementwise_add[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 200.44 | - | - |
| test_elementwise_add[input_length_8192-num_aie_columns_1-tile_size_8192] | ✅ | 168.90 | ✅ | 284.94 |
| test_elementwise_add[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 165.08 | ✅ | 382.02 |
| test_elementwise_add[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 189.06 | ✅ | 579.24 |
| test_elementwise_add[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 195.00 | - | - |
| test_elementwise_add[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 5038.06 |
| test_elementwise_add[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 870.16 | - | - |

</details>

<details>
<summary>iron/operators/elementwise_mul</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_elementwise_mul[input_length_1024-num_aie_columns_1-tile_size_1024] | ✅ | 152.48 | ✅ | 291.58 |
| test_elementwise_mul[input_length_1024-num_aie_columns_2-tile_size_512] | ✅ | 168.06 | ✅ | 329.56 |
| test_elementwise_mul[input_length_1024-num_aie_columns_4-tile_size_256] | ✅ | 170.64 | ✅ | 758.32 |
| test_elementwise_mul[input_length_1024-num_aie_columns_8-tile_size_128] | ✅ | 206.72 | - | - |
| test_elementwise_mul[input_length_2048-num_aie_columns_1-tile_size_2048] | ✅ | 181.44 | ✅ | 429.88 |
| test_elementwise_mul[input_length_2048-num_aie_columns_2-tile_size_1024] | ✅ | 168.84 | ✅ | 302.64 |
| test_elementwise_mul[input_length_2048-num_aie_columns_4-tile_size_512] | ✅ | 187.84 | ✅ | 463.78 |
| test_elementwise_mul[input_length_2048-num_aie_columns_8-tile_size_256] | ✅ | 185.88 | - | - |
| test_elementwise_mul[input_length_4096-num_aie_columns_1-tile_size_4096] | ✅ | 182.80 | ✅ | 439.46 |
| test_elementwise_mul[input_length_4096-num_aie_columns_2-tile_size_2048] | ✅ | 162.66 | ✅ | 420.32 |
| test_elementwise_mul[input_length_4096-num_aie_columns_4-tile_size_1024] | ✅ | 172.70 | ✅ | 402.36 |
| test_elementwise_mul[input_length_4096-num_aie_columns_8-tile_size_512] | ✅ | 185.70 | - | - |
| test_elementwise_mul[input_length_8192-num_aie_columns_2-tile_size_4096] | ✅ | 152.80 | ✅ | 441.18 |
| test_elementwise_mul[input_length_8192-num_aie_columns_4-tile_size_2048] | ✅ | 165.68 | ✅ | 472.26 |
| test_elementwise_mul[input_length_8192-num_aie_columns_8-tile_size_1024] | ✅ | 192.30 | - | - |
| test_elementwise_mul[input_length_8388608-num_aie_columns_4-tile_size_4096] | - | - | ✅ | 3730.50 |
| test_elementwise_mul[input_length_8388608-num_aie_columns_8-tile_size_4096] | ✅ | 982.98 | - | - |

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
| test_large_k_shapes[K_12288-N_1536] | ✅ | 1653.86 | - | - |
| test_large_k_shapes[K_4096-N_1536] | ✅ | 623.60 | - | - |
| test_large_k_shapes[K_6144-N_1536] | ✅ | 823.22 | - | - |
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
| test_artifact_stem_differs_from_generic_gemm[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_artifact_stem_differs_from_generic_gemm[M_512-K_1024-N_2048] | ✅ | - | - | - |
| test_gemm[M_1024-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 3936.86 | - | - |
| test_gemm[M_1024-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 759.60 | - | - |
| test_gemm[M_1024-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 3367.58 | - | - |
| test_gemm[M_1024-K_2560-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1228.72 | - | - |
| test_gemm[M_16384-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 2320.26 | - | - |
| test_gemm[M_2048-K_10240-N_2560-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 7723.02 | - | - |
| test_gemm[M_2048-K_2048-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 1342.28 | - | - |
| test_gemm[M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 5957.92 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_gelu-clamp_None-rounding_conv_even] | ✅ | 329.44 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_(-2.0, 2.0)-rounding_conv_even] | ✅ | 327.04 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 342.72 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_none-clamp_None-rounding_floor] | ✅ | 313.20 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_sigmoid-clamp_None-rounding_conv_even] | ✅ | 368.10 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 360.92 | - | - |
| test_gemm[M_256-K_512-N_1024-epilogue_silu-clamp_None-rounding_floor] | ✅ | 353.22 | - | - |
| test_gemm[M_256-K_512-N_128-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 327.76 | - | - |
| test_gemm[M_256-K_512-N_1536-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 366.20 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_none-clamp_None-rounding_conv_even] | ✅ | 442.34 | - | - |
| test_gemm[M_512-K_1024-N_2048-epilogue_silu-clamp_(-4.0, 4.0)-rounding_conv_even] | ✅ | 424.96 | - | - |
| test_gemm[M_512-K_1536-N_1536-epilogue_silu-clamp_None-rounding_conv_even] | ✅ | 471.94 | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_256-K_512-N_1024] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_256] | ✅ | - | - | - |
| test_gemm_gelu_bf16_steps_matches_overlay[M_512-K_1536-N_6144] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter0] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter1] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter2] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter3] | ✅ | - | - | - |
| test_gemm_split_leg_bounds_runs[iter4] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn128-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn16-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma32] | ✅ | - | - | - |
| test_gemm_tile_options[tn32-ma64-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma16] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma32-default] | ✅ | - | - | - |
| test_gemm_tile_options[tn64-ma64] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_clamp_bound[iter4] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter0] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter1] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter2] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter3] | ✅ | - | - | - |
| test_one_xclbin_serves_every_shape[iter4] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/flm/layer</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_matches_reference[gemma4_e2b-global-5] | ✅ | 804.68 | - | - |
| test_matches_reference[gemma4_e2b-global-700] | ✅ | 877.16 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-37] | ✅ | 1147.60 | - | - |
| test_matches_reference[gemma4_e2b-global_skip-700] | ✅ | 1249.42 | - | - |
| test_matches_reference[gemma4_e2b-swa-1023] | ✅ | 763.66 | - | - |
| test_matches_reference[gemma4_e2b-swa-37] | ✅ | 732.94 | - | - |
| test_matches_reference[gemma4_e2b-swa-511] | ✅ | 737.32 | - | - |
| test_matches_reference[gemma4_e2b-swa-512] | ✅ | 744.48 | - | - |
| test_matches_reference[gemma4_e2b-swa-700] | ✅ | 764.52 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-1023] | ✅ | 1129.64 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-37] | ✅ | 1078.30 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-511] | ✅ | 1143.82 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-512] | ✅ | 1060.56 | - | - |
| test_matches_reference[gemma4_e2b-swa_skip-700] | ✅ | 1147.80 | - | - |
| test_matches_reference[gemma4_e4b-global-5] | ✅ | 1985.04 | - | - |
| test_matches_reference[gemma4_e4b-global-700] | ✅ | 1832.80 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-37] | ✅ | 1782.96 | - | - |
| test_matches_reference[gemma4_e4b-global_skip-700] | ✅ | 1895.26 | - | - |
| test_matches_reference[gemma4_e4b-swa-1023] | ✅ | 1722.04 | - | - |
| test_matches_reference[gemma4_e4b-swa-37] | ✅ | 1560.22 | - | - |
| test_matches_reference[gemma4_e4b-swa-511] | ✅ | 1595.10 | - | - |
| test_matches_reference[gemma4_e4b-swa-512] | ✅ | 1948.92 | - | - |
| test_matches_reference[gemma4_e4b-swa-700] | ✅ | 1688.50 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-1023] | ✅ | 1642.82 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-37] | ✅ | 1947.28 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-511] | ✅ | 1874.70 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-512] | ✅ | 1914.90 | - | - |
| test_matches_reference[gemma4_e4b-swa_skip-700] | ✅ | 1524.32 | - | - |
| test_rejects_unknown_configurations[geometry] | ✅ | - | ✅ | - |
| test_rejects_unknown_configurations[layer_type] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e2b-layer_type_swa_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_global_skip] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa] | ✅ | - | ✅ | - |
| test_weight_reads_fit_proj[gemma4_e4b-layer_type_swa_skip] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/flm/lm_head</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_softcap[dim_1536] | ✅ | - | - | - |
| test_gemma4_softcap[dim_2560] | ✅ | - | - | - |
| test_gemma4_vocabulary[dim_1536] | ✅ | 4116.34 | - | - |
| test_gemma4_vocabulary[dim_2560] | ✅ | 6621.48 | - | - |
| test_projection_matches_reference[dim_1536] | ✅ | - | - | - |
| test_projection_matches_reference[dim_2560] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1000-vocab_4096-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_1000-softcap_30.0-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_0.0-match_finite and positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[dim_1536-vocab_4096-softcap_inf-match_finite and positive] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter0] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter1] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter2] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter3] | ✅ | - | - | - |
| test_softcap_bounds_the_logits[iter4] | ✅ | - | - | - |

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
<summary>iron/operators/flm/prefill_attn</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemma4_cache_bound[kind_attn-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_attn-num_kv_heads_2] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_1] | ✅ | - | - | - |
| test_gemma4_cache_bound[kind_swa-num_kv_heads_2] | ✅ | - | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_1] | ✅ | 376.50 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_128-max_l_1024-num_kv_heads_2] | ✅ | 375.90 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_1] | ✅ | 774.70 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_256-max_l_512-num_kv_heads_2] | ✅ | 774.04 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 1826.44 | - | - |
| test_matches_reference[kind_attn-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 1824.98 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_1] | ✅ | 1013.86 | - | - |
| test_matches_reference[kind_attn-L_begin_128-L_end_384-max_l_1024-num_kv_heads_2] | ✅ | 1001.04 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_1] | ✅ | 4708.72 | - | - |
| test_matches_reference[kind_attn-L_begin_256-L_end_1024-max_l_1024-num_kv_heads_2] | ✅ | 4500.10 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 2254.02 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1914.68 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_1] | ✅ | 216.90 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_128-max_l_2048-num_kv_heads_2] | ✅ | 215.20 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_1] | ✅ | 803.20 | - | - |
| test_matches_reference[kind_swa-L_begin_0-L_end_512-max_l_1024-num_kv_heads_2] | ✅ | 804.76 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_1] | ✅ | 2359.34 | - | - |
| test_matches_reference[kind_swa-L_begin_1024-L_end_2048-max_l_2048-num_kv_heads_2] | ✅ | 2365.30 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_1] | ✅ | 1256.80 | - | - |
| test_matches_reference[kind_swa-L_begin_512-L_end_1024-max_l_2048-num_kv_heads_2] | ✅ | 1250.56 | - | - |
| test_one_callable_serves_every_range[kind_attn] | ✅ | - | - | - |
| test_one_callable_serves_every_range[kind_swa] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 0}-match_must be positive] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillAttention'>-kwargs_{'num_kv_heads': 8}-match_query heads] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'max_context': 1000, 'num_kv_heads': 1}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 1, 'window': 500}-match_multiple of 128] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 3}-match_multiple of] | ✅ | - | - | - |
| test_rejects_unservable_shapes[cls_<class 'iron.operators.flm.prefill_attn.op.PrefillSlidingAttention'>-kwargs_{'num_kv_heads': 4}-match_query heads] | ✅ | - | - | - |

</details>

<details>
<summary>iron/operators/gelu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 150.74 | ✅ | 331.16 |
| test_gelu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 162.28 | ✅ | 785.76 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 184.38 | ✅ | 484.30 |
| test_gelu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 169.30 | ✅ | 466.02 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 216.64 | ✅ | 492.32 |
| test_gelu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 195.64 | ✅ | 475.74 |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 169.00 | - | - |
| test_gelu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 200.14 | - | - |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 167.26 | ✅ | 328.46 |
| test_gelu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 162.70 | ✅ | 427.24 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 167.62 | ✅ | 451.34 |
| test_gelu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 164.58 | ✅ | 524.02 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 173.18 | ✅ | 476.64 |
| test_gelu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 180.72 | ✅ | 528.62 |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 198.98 | - | - |
| test_gelu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 228.70 | - | - |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 155.26 | ✅ | 295.94 |
| test_gelu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 159.62 | ✅ | 525.80 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 160.62 | ✅ | 406.64 |
| test_gelu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 183.98 | ✅ | 386.72 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 144.74 | ✅ | 499.04 |
| test_gelu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 179.54 | ✅ | 470.64 |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 167.86 | - | - |
| test_gelu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 214.68 | - | - |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 180.26 | ✅ | 469.70 |
| test_gelu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 178.62 | ✅ | 452.92 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 160.92 | ✅ | 518.80 |
| test_gelu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 187.98 | ✅ | 401.46 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 168.18 | ✅ | 457.18 |
| test_gelu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 192.80 | ✅ | 764.76 |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 199.76 | - | - |
| test_gelu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 239.98 | - | - |
| test_gelu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3450.52 |
| test_gelu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 780.28 | - | - |

</details>

<details>
<summary>iron/operators/gemm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemm[M_1024-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 18887.52 | - | - |
| test_gemm[M_1792-K_896-N_1152-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_64-k_32-n_48-partition_N_1] | ✅ | 2085.78 | - | - |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_False-c_col_maj_False-m_48-k_96-n_16-partition_N_1] | ✅ | 207.48 | ✅ | 1122.02 |
| test_gemm[M_192-K_384-N_64-num_aie_columns_4-b_col_maj_True-c_col_maj_True-m_48-k_96-n_16-partition_N_1] | ✅ | 244.34 | ✅ | 626.28 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_1-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 47075.66 | ✅ | 81830.54 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_8-k_16-n_32-partition_N_1] | ✅ | 119903.68 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 27680.86 | ✅ | 18537.14 |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_32-k_32-n_128-partition_N_1] | ✅ | 7021.42 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_False-m_128-k_32-n_32-partition_N_1] | ✅ | 8443.32 | - | - |
| test_gemm[M_2048-K_2048-N_2048-num_aie_columns_8-b_col_maj_True-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 7596.26 | - | - |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93406.90 | ✅ | 91417.54 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100819.40 | ✅ | 90702.08 |
| test_gemm[M_2048-K_2048-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 107283.48 | ✅ | 72502.62 |
| test_gemm[M_2048-K_2560-N_10240-num_aie_columns_8-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 37022.16 | - | - |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1060.62 | ✅ | 2719.72 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 1094.32 | ✅ | 2747.16 |
| test_gemm[M_2048-K_64-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 1205.00 | ✅ | 2858.68 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3622.98 | ✅ | 6434.64 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 3846.38 | ✅ | 7442.76 |
| test_gemm[M_2048-K_64-N_8192-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 3928.06 | ✅ | 6550.10 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 93209.70 | ✅ | 98084.06 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_False-c_col_maj_True-m_64-k_64-n_64-partition_N_1] | ✅ | 100669.02 | ✅ | 97586.48 |
| test_gemm[M_2048-K_8192-N_2048-num_aie_columns_2-b_col_maj_True-c_col_maj_False-m_64-k_64-n_64-partition_N_1] | ✅ | 106518.42 | ✅ | 75680.02 |
| test_gemm[M_384-K_1536-N_1792-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_32-k_48-n_64-partition_N_1] | ✅ | 2033.46 | ✅ | 4132.92 |
| test_gemm[M_64-K_512-N_256-num_aie_columns_4-b_col_maj_True-c_col_maj_False-m_16-k_64-n_64-partition_N_4] | ✅ | 3267.12 | ✅ | 6623.70 |
| test_gemm[M_896-K_1792-N_640-num_aie_columns_8-b_col_maj_False-c_col_maj_True-m_32-k_64-n_80-partition_N_1] | ✅ | 1337.78 | - | - |

</details>

<details>
<summary>iron/operators/gemv</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_gemv[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 158.30 | ✅ | 734.76 |
| test_gemv[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2583.38 | ✅ | 9228.36 |
| test_gemv[M_2048-K_8192-num_aie_columns_2-tile_size_input_1-tile_size_output_1024] | ✅ | 1394.58 | ✅ | 5389.80 |
| test_gemv[M_2048-K_8192-num_aie_columns_4-tile_size_input_1-tile_size_output_512] | ✅ | 958.86 | ✅ | 3671.82 |
| test_gemv[M_2048-K_8192-num_aie_columns_8-tile_size_input_1-tile_size_output_256] | ✅ | 777.52 | - | - |
| test_gemv[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2644.06 | ✅ | 9247.30 |
| test_gemv[M_8192-K_2048-num_aie_columns_2-tile_size_input_4-tile_size_output_1024] | ✅ | 1357.10 | ✅ | 6242.88 |
| test_gemv[M_8192-K_2048-num_aie_columns_4-tile_size_input_4-tile_size_output_1024] | ✅ | 839.32 | ✅ | 3985.48 |
| test_gemv[M_8192-K_2048-num_aie_columns_8-tile_size_input_4-tile_size_output_1024] | ✅ | 802.54 | - | - |
| test_gemv_batched[M_1024-K_1024-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_2] | ✅ | 490.46 | ✅ | 1824.14 |
| test_gemv_batched[M_1026-K_64-num_aie_columns_1-tile_size_input_1-tile_size_output_2-num_batches_2] | ✅ | 324.04 | ✅ | 1240.68 |
| test_gemv_batched[M_256-K_128-num_aie_columns_1-tile_size_input_1-tile_size_output_256-num_batches_4] | ✅ | 245.82 | ✅ | 512.32 |
| test_gemv_batched[M_256-K_128-num_aie_columns_8-tile_size_input_1-tile_size_output_32-num_batches_100] | ✅ | 478.80 | - | - |
| test_gemv_batched[M_448-K_64-num_aie_columns_8-tile_size_input_1-tile_size_output_56-num_batches_192] | ✅ | 1001.82 | - | - |
| test_gemv_batched[M_512-K_64-num_aie_columns_8-tile_size_input_4-tile_size_output_64-num_batches_32] | ✅ | 226.94 | - | - |
| test_gemv_batched[M_64-K_1536-num_aie_columns_1-tile_size_input_1-tile_size_output_64-num_batches_8] | ✅ | 288.50 | ✅ | 1874.74 |
| test_gemv_gelu[M_128-K_128-num_aie_columns_1-tile_size_input_32-tile_size_output_128] | ✅ | 130.30 | ❌ | - |
| test_gemv_gelu[M_2048-K_8192-num_aie_columns_1-tile_size_input_1-tile_size_output_2048] | ✅ | 2603.80 | ❌ | - |
| test_gemv_gelu[M_8192-K_2048-num_aie_columns_1-tile_size_input_4-tile_size_output_1024] | ✅ | 2528.60 | ❌ | - |

</details>

<details>
<summary>iron/operators/layer_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 183.16 | ✅ | 370.26 |
| test_layer_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 183.86 | ✅ | 281.90 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 190.48 | ✅ | 374.44 |
| test_layer_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 177.38 | ✅ | 884.44 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 191.36 | ✅ | 542.82 |
| test_layer_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 185.66 | ✅ | 445.00 |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 185.40 | - | - |
| test_layer_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 206.46 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 192.82 | ✅ | 367.00 |
| test_layer_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 167.28 | ✅ | 643.94 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 159.78 | ✅ | 291.12 |
| test_layer_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 177.70 | ✅ | 426.90 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 202.38 | ✅ | 766.96 |
| test_layer_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 192.64 | ✅ | 527.54 |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 204.52 | - | - |
| test_layer_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 231.42 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 156.80 | ✅ | 235.18 |
| test_layer_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 179.68 | ✅ | 439.70 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 160.20 | ✅ | 376.94 |
| test_layer_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 206.66 | ✅ | 409.92 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 184.10 | ✅ | 619.94 |
| test_layer_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 175.26 | ✅ | 517.00 |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 177.34 | - | - |
| test_layer_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 253.96 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192] | ✅ | 186.16 | ✅ | 348.38 |
| test_layer_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 176.86 | ✅ | 406.60 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 159.12 | ✅ | 702.12 |
| test_layer_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 176.82 | ✅ | 348.96 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 182.26 | ✅ | 450.04 |
| test_layer_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 189.42 | ✅ | 363.58 |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 205.26 | - | - |
| test_layer_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 208.18 | - | - |
| test_layer_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3501.44 |
| test_layer_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 686.56 | - | - |

</details>

<details>
<summary>iron/operators/leaky_relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 153.68 | ✅ | 649.58 |
| test_leaky_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 188.92 | ✅ | 528.96 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 233.28 | ✅ | 320.30 |
| test_leaky_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 187.20 | ✅ | 461.02 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 164.12 | ✅ | 537.02 |
| test_leaky_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 187.72 | ✅ | 485.96 |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-alpha_0.01] | ✅ | 187.28 | - | - |
| test_leaky_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-alpha_0.01] | ✅ | 205.32 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 169.76 | ✅ | 747.42 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.1] | ✅ | 171.30 | ✅ | 293.34 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-alpha_0.25] | ✅ | 169.20 | ✅ | 373.76 |
| test_leaky_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 192.22 | ✅ | 561.28 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 168.46 | ✅ | 451.88 |
| test_leaky_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 176.18 | ✅ | 451.62 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 183.16 | ✅ | 789.38 |
| test_leaky_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 203.84 | ✅ | 537.02 |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-alpha_0.01] | ✅ | 178.08 | - | - |
| test_leaky_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-alpha_0.01] | ✅ | 226.88 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 147.14 | ✅ | 382.20 |
| test_leaky_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 169.96 | ✅ | 674.02 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 138.94 | ✅ | 361.70 |
| test_leaky_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 189.84 | ✅ | 393.20 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 207.40 | ✅ | 354.06 |
| test_leaky_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 204.06 | ✅ | 459.42 |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-alpha_0.01] | ✅ | 202.66 | - | - |
| test_leaky_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-alpha_0.01] | ✅ | 234.28 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 178.20 | ✅ | 405.02 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-alpha_0.01] | ✅ | 173.48 | ✅ | 611.28 |
| test_leaky_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-alpha_0.01] | ✅ | 188.42 | ✅ | 827.12 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-alpha_0.01] | ✅ | 199.18 | ✅ | 352.62 |
| test_leaky_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-alpha_0.01] | ✅ | 216.66 | ✅ | 405.72 |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-alpha_0.01] | ✅ | 186.94 | - | - |
| test_leaky_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-alpha_0.01] | ✅ | 205.62 | - | - |
| test_leaky_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-alpha_0.01] | - | - | ✅ | 3693.78 |
| test_leaky_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-alpha_0.01] | ✅ | 790.96 | - | - |

</details>

<details>
<summary>iron/operators/mem_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_False-tile_size_1024] | ✅ | 166.78 | ✅ | 388.02 |
| test_mem_copy[input_length_1024-num_cores_1-num_channels_1-bypass_True-tile_size_1024] | ✅ | 171.22 | ✅ | 460.50 |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_False-tile_size_64] | ✅ | 187.80 | - | - |
| test_mem_copy[input_length_1024-num_cores_16-num_channels_2-bypass_True-tile_size_64] | ✅ | 189.88 | - | - |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_False-tile_size_512] | ✅ | 179.82 | ✅ | 726.28 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_1-bypass_True-tile_size_512] | ✅ | 172.56 | ✅ | 467.80 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_False-tile_size_512] | ✅ | 169.92 | ✅ | 456.18 |
| test_mem_copy[input_length_1024-num_cores_2-num_channels_2-bypass_True-tile_size_512] | ✅ | 173.60 | ✅ | 373.80 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_False-tile_size_256] | ✅ | 184.60 | ✅ | 503.18 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_1-bypass_True-tile_size_256] | ✅ | 176.72 | ✅ | 540.44 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_False-tile_size_256] | ✅ | 157.12 | ✅ | 482.24 |
| test_mem_copy[input_length_1024-num_cores_4-num_channels_2-bypass_True-tile_size_256] | ✅ | 190.24 | ✅ | 487.04 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_False-tile_size_128] | ✅ | 171.12 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_1-bypass_True-tile_size_128] | ✅ | 217.36 | - | - |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_False-tile_size_128] | ✅ | 170.78 | ✅ | 466.34 |
| test_mem_copy[input_length_1024-num_cores_8-num_channels_2-bypass_True-tile_size_128] | ✅ | 159.76 | ✅ | 501.20 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_False-tile_size_2048] | ✅ | 167.80 | ✅ | 498.12 |
| test_mem_copy[input_length_2048-num_cores_1-num_channels_1-bypass_True-tile_size_2048] | ✅ | 188.94 | ✅ | 315.10 |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_False-tile_size_128] | ✅ | 221.36 | - | - |
| test_mem_copy[input_length_2048-num_cores_16-num_channels_2-bypass_True-tile_size_128] | ✅ | 201.76 | - | - |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_False-tile_size_1024] | ✅ | 190.04 | ✅ | 419.44 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_1-bypass_True-tile_size_1024] | ✅ | 182.20 | ✅ | 375.84 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_False-tile_size_1024] | ✅ | 167.60 | ✅ | 484.22 |
| test_mem_copy[input_length_2048-num_cores_2-num_channels_2-bypass_True-tile_size_1024] | ✅ | 158.90 | ✅ | 447.46 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_False-tile_size_512] | ✅ | 143.00 | ✅ | 463.46 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_1-bypass_True-tile_size_512] | ✅ | 180.22 | ✅ | 477.92 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_False-tile_size_512] | ✅ | 166.26 | ✅ | 489.96 |
| test_mem_copy[input_length_2048-num_cores_4-num_channels_2-bypass_True-tile_size_512] | ✅ | 171.56 | ✅ | 420.30 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_False-tile_size_256] | ✅ | 175.52 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_1-bypass_True-tile_size_256] | ✅ | 182.18 | - | - |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_False-tile_size_256] | ✅ | 186.98 | ✅ | 565.42 |
| test_mem_copy[input_length_2048-num_cores_8-num_channels_2-bypass_True-tile_size_256] | ✅ | 207.58 | ✅ | 416.54 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_False-tile_size_4096] | ✅ | 177.54 | ✅ | 373.54 |
| test_mem_copy[input_length_4096-num_cores_1-num_channels_1-bypass_True-tile_size_4096] | ✅ | 174.40 | ✅ | 380.38 |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_False-tile_size_256] | ✅ | 203.86 | - | - |
| test_mem_copy[input_length_4096-num_cores_16-num_channels_2-bypass_True-tile_size_256] | ✅ | 212.78 | - | - |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_False-tile_size_2048] | ✅ | 167.72 | ✅ | 412.92 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_1-bypass_True-tile_size_2048] | ✅ | 171.20 | ✅ | 364.00 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_False-tile_size_2048] | ✅ | 175.52 | ✅ | 379.42 |
| test_mem_copy[input_length_4096-num_cores_2-num_channels_2-bypass_True-tile_size_2048] | ✅ | 175.86 | ✅ | 325.78 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_False-tile_size_1024] | ✅ | 193.78 | ✅ | 414.22 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_1-bypass_True-tile_size_1024] | ✅ | 183.98 | ✅ | 448.92 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_False-tile_size_1024] | ✅ | 190.10 | ✅ | 509.98 |
| test_mem_copy[input_length_4096-num_cores_4-num_channels_2-bypass_True-tile_size_1024] | ✅ | 177.20 | ✅ | 463.34 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_False-tile_size_512] | ✅ | 171.64 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_1-bypass_True-tile_size_512] | ✅ | 183.56 | - | - |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_False-tile_size_512] | ✅ | 196.16 | ✅ | 390.76 |
| test_mem_copy[input_length_4096-num_cores_8-num_channels_2-bypass_True-tile_size_512] | ✅ | 185.42 | ✅ | 444.80 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_False-tile_size_8192] | ✅ | 204.78 | ✅ | 317.80 |
| test_mem_copy[input_length_8192-num_cores_1-num_channels_1-bypass_True-tile_size_8192] | ✅ | 171.72 | ✅ | 523.92 |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_False-tile_size_512] | ✅ | 218.08 | - | - |
| test_mem_copy[input_length_8192-num_cores_16-num_channels_2-bypass_True-tile_size_512] | ✅ | 200.24 | - | - |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_False-tile_size_4096] | ✅ | 191.94 | ✅ | 647.16 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_1-bypass_True-tile_size_4096] | ✅ | 173.04 | ✅ | 313.44 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_False-tile_size_4096] | ✅ | 173.12 | ✅ | 313.98 |
| test_mem_copy[input_length_8192-num_cores_2-num_channels_2-bypass_True-tile_size_4096] | ✅ | 171.84 | ✅ | 476.02 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_False-tile_size_2048] | ✅ | 167.88 | ✅ | 467.96 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_1-bypass_True-tile_size_2048] | ✅ | 172.92 | ✅ | 389.58 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_False-tile_size_2048] | ✅ | 152.42 | ✅ | 788.38 |
| test_mem_copy[input_length_8192-num_cores_4-num_channels_2-bypass_True-tile_size_2048] | ✅ | 165.76 | ✅ | 424.18 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_False-tile_size_1024] | ✅ | 160.90 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_1-bypass_True-tile_size_1024] | ✅ | 177.96 | - | - |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_False-tile_size_1024] | ✅ | 195.22 | ✅ | 543.82 |
| test_mem_copy[input_length_8192-num_cores_8-num_channels_2-bypass_True-tile_size_1024] | ✅ | 177.06 | ✅ | 794.50 |
| test_mem_copy[input_length_8388608-num_cores_16-num_channels_2-bypass_False-tile_size_4096] | ✅ | 676.78 | - | - |
| test_mem_copy[input_length_8388608-num_cores_8-num_channels_2-bypass_False-tile_size_4096] | - | - | ✅ | 3894.04 |

</details>

<details>
<summary>iron/operators/mha</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | - | ✅ | - |
| test_arg_spec_matches_design_shapes[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | - | ✅ | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_4-num_kv_heads_0] | ✅ | 17226.42 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_1-num_pipelines_8-num_kv_heads_0] | ✅ | 16823.80 | - | - |
| test_mha[seq_len_16384-dim_64-num_heads_8-num_pipelines_8-num_kv_heads_2] | ✅ | 152048.02 | - | - |

</details>

<details>
<summary>iron/operators/relu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_relu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 170.54 | ✅ | 373.84 |
| test_relu[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 184.80 | ✅ | 392.84 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 179.30 | ✅ | 396.52 |
| test_relu[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 166.10 | ✅ | 679.78 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 194.54 | ✅ | 391.64 |
| test_relu[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 190.58 | ✅ | 482.56 |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 166.68 | - | - |
| test_relu[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 194.76 | - | - |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 167.80 | ✅ | 302.24 |
| test_relu[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 175.64 | ✅ | 467.46 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 166.86 | ✅ | 426.54 |
| test_relu[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 175.36 | ✅ | 459.40 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 153.14 | ✅ | 377.20 |
| test_relu[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 167.28 | ✅ | 435.40 |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 183.14 | - | - |
| test_relu[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 231.50 | - | - |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 148.68 | ✅ | 419.66 |
| test_relu[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 145.32 | ✅ | 352.50 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 139.56 | ✅ | 437.44 |
| test_relu[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 165.84 | ✅ | 448.22 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 184.90 | ✅ | 473.02 |
| test_relu[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 162.64 | ✅ | 583.62 |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 173.94 | - | - |
| test_relu[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 210.04 | - | - |
| test_relu[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.36 | ✅ | 425.86 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 173.58 | ✅ | 370.00 |
| test_relu[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 204.08 | ✅ | 400.10 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 165.46 | ✅ | 496.32 |
| test_relu[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 227.72 | ✅ | 451.14 |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 181.32 | - | - |
| test_relu[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 237.80 | - | - |
| test_relu[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 3486.32 |
| test_relu[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 664.38 | - | - |

</details>

<details>
<summary>iron/operators/repeat</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_cols_without_a_legal_split_is_rejected[cols_1031-why_prime > 1023: the only divisors are 1 and cols, neither legal] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_2062-why_2 x 1031: the only word-aligned chunk leaves a 1031-wide chunk count] | ✅ | - | ✅ | - |
| test_cols_without_a_legal_split_is_rejected[cols_513-why_odd: every divisor is odd, so no chunk is a whole 32-bit word] | ✅ | - | ✅ | - |
| test_repeat[rows_4-cols_1024-repeat_2-transfer_size_None] | ✅ | 156.72 | ✅ | 369.94 |
| test_repeat[rows_4-cols_2048-repeat_2-transfer_size_None] | ✅ | 155.36 | ✅ | 293.66 |
| test_repeat[rows_8-cols_131072-repeat_4-transfer_size_64] | ✅ | 811.72 | ✅ | 3478.64 |
| test_repeat[rows_8-cols_512-repeat_4-transfer_size_64] | ✅ | 148.30 | ✅ | 403.66 |
| test_repeat[rows_8-cols_64-repeat_4-transfer_size_None] | ✅ | 151.30 | ✅ | 265.38 |

</details>

<details>
<summary>iron/operators/rms_norm</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_False] | ✅ | 162.88 | ✅ | 406.70 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024-weighted_True] | ✅ | 173.28 | ✅ | 405.92 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_False] | ✅ | 189.92 | ✅ | 351.78 |
| test_rms_norm[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512-weighted_True] | ✅ | 163.66 | ✅ | 467.42 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_False] | ✅ | 155.28 | ✅ | 484.58 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512-weighted_True] | ✅ | 180.16 | ✅ | 332.74 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_False] | ✅ | 176.64 | ✅ | 719.66 |
| test_rms_norm[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256-weighted_True] | ✅ | 179.86 | ✅ | 473.90 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_False] | ✅ | 198.60 | ✅ | 422.90 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256-weighted_True] | ✅ | 198.76 | ✅ | 404.96 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_False] | ✅ | 181.22 | ✅ | 506.46 |
| test_rms_norm[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128-weighted_True] | ✅ | 197.12 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_False] | ✅ | 190.04 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128-weighted_True] | ✅ | 191.66 | - | - |
| test_rms_norm[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64-weighted_False] | ✅ | 239.90 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_False] | ✅ | 175.74 | ✅ | 458.38 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048-weighted_True] | ✅ | 153.24 | ✅ | 409.10 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_False] | ✅ | 154.22 | ✅ | 434.64 |
| test_rms_norm[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024-weighted_True] | ✅ | 162.84 | ✅ | 424.46 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_False] | ✅ | 200.22 | ✅ | 394.82 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024-weighted_True] | ✅ | 160.24 | ✅ | 362.60 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_False] | ✅ | 161.60 | ✅ | 485.60 |
| test_rms_norm[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512-weighted_True] | ✅ | 144.66 | ✅ | 473.36 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_False] | ✅ | 174.98 | ✅ | 653.40 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512-weighted_True] | ✅ | 166.52 | ✅ | 589.60 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_False] | ✅ | 165.16 | ✅ | 485.96 |
| test_rms_norm[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256-weighted_True] | ✅ | 207.48 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_False] | ✅ | 198.74 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256-weighted_True] | ✅ | 184.70 | - | - |
| test_rms_norm[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128-weighted_False] | ✅ | 265.66 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_False] | ✅ | 155.56 | ✅ | 356.88 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096-weighted_True] | ✅ | 155.54 | ✅ | 365.10 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_False] | ✅ | 164.68 | ✅ | 350.36 |
| test_rms_norm[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048-weighted_True] | ✅ | 156.70 | ✅ | 747.16 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_False] | ✅ | 197.22 | ✅ | 417.88 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048-weighted_True] | ✅ | 168.52 | ✅ | 452.04 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_False] | ✅ | 169.86 | ✅ | 567.62 |
| test_rms_norm[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024-weighted_True] | ✅ | 179.68 | ✅ | 544.54 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_False] | ✅ | 195.40 | ✅ | 859.30 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024-weighted_True] | ✅ | 174.48 | ✅ | 489.02 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_False] | ✅ | 186.34 | ✅ | 523.38 |
| test_rms_norm[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512-weighted_True] | ✅ | 197.44 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_False] | ✅ | 189.52 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512-weighted_True] | ✅ | 218.12 | - | - |
| test_rms_norm[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256-weighted_False] | ✅ | 196.78 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_1-tile_size_8192-weighted_False] | ✅ | 150.90 | ✅ | 493.46 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_False] | ✅ | 172.88 | ✅ | 401.64 |
| test_rms_norm[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096-weighted_True] | ✅ | 181.26 | ✅ | 390.52 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_False] | ✅ | 177.90 | ✅ | 397.60 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096-weighted_True] | ✅ | 174.06 | ✅ | 473.50 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_False] | ✅ | 197.38 | ✅ | 434.50 |
| test_rms_norm[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048-weighted_True] | ✅ | 178.94 | ✅ | 407.00 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_False] | ✅ | 207.52 | ✅ | 432.34 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048-weighted_True] | ✅ | 179.20 | ✅ | 381.30 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_False] | ✅ | 211.58 | ✅ | 473.02 |
| test_rms_norm[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024-weighted_True] | ✅ | 238.18 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_False] | ✅ | 178.60 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024-weighted_True] | ✅ | 218.60 | - | - |
| test_rms_norm[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512-weighted_False] | ✅ | 230.90 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_2-num_channels_2-tile_size_4096-weighted_True] | - | - | ✅ | 3425.50 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_False] | - | - | ✅ | 3799.58 |
| test_rms_norm[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096-weighted_True] | ✅ | 742.14 | - | - |
| test_rms_norm[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096-weighted_False] | ✅ | 731.36 | - | - |

</details>

<details>
<summary>iron/operators/rope</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 185.66 | ✅ | 439.46 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 182.00 | ✅ | 405.44 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 180.48 | ✅ | 276.26 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 171.32 | ✅ | 290.66 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 210.96 | ✅ | 445.46 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 167.96 | ✅ | 419.12 |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 193.28 | - | - |
| test_rope[rows_32-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 217.62 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 171.06 | ✅ | 334.48 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 155.12 | ✅ | 421.04 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 214.48 | ✅ | 306.22 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 193.52 | ✅ | 303.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 194.74 | ✅ | 465.02 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 148.78 | ✅ | 360.76 |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 213.12 | - | - |
| test_rope[rows_32-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 205.74 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 167.46 | ✅ | 423.74 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 187.82 | ✅ | 322.48 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 213.60 | ✅ | 324.14 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 159.62 | ✅ | 381.14 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 173.58 | ✅ | 397.06 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 175.08 | ✅ | 404.24 |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 187.08 | - | - |
| test_rope[rows_32-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 174.26 | - | - |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 177.54 | ✅ | 381.02 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 177.92 | ✅ | 615.00 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 184.58 | ✅ | 751.36 |
| test_rope[rows_32-cols_512-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 198.58 | - | - |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 185.18 | ✅ | 447.40 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 174.12 | ✅ | 371.44 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 189.76 | ✅ | 417.64 |
| test_rope[rows_32-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 203.86 | - | - |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_4-method_type_0] | - | - | ✅ | 1471.92 |
| test_rope[rows_4096-cols_512-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 298.62 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_0] | ✅ | 162.88 | ✅ | 368.38 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_1-method_type_1] | ✅ | 174.10 | ✅ | 355.58 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_0] | ✅ | 174.72 | ✅ | 482.50 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_2-method_type_1] | ✅ | 208.70 | ✅ | 464.64 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_0] | ✅ | 178.48 | ✅ | 423.80 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_4-method_type_1] | ✅ | 173.14 | ✅ | 369.92 |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_0] | ✅ | 174.14 | - | - |
| test_rope[rows_64-cols_128-angle_rows_16-aie_columns_8-method_type_1] | ✅ | 188.92 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_0] | ✅ | 206.78 | ✅ | 311.68 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_1-method_type_1] | ✅ | 187.14 | ✅ | 549.26 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_0] | ✅ | 200.68 | ✅ | 462.32 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_2-method_type_1] | ✅ | 191.48 | ✅ | 424.46 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_0] | ✅ | 187.90 | ✅ | 368.80 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_4-method_type_1] | ✅ | 192.36 | ✅ | 416.76 |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_0] | ✅ | 184.56 | - | - |
| test_rope[rows_64-cols_128-angle_rows_32-aie_columns_8-method_type_1] | ✅ | 191.84 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_0] | ✅ | 171.50 | ✅ | 271.50 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_1-method_type_1] | ✅ | 180.24 | ✅ | 406.88 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_0] | ✅ | 181.22 | ✅ | 381.78 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_2-method_type_1] | ✅ | 166.44 | ✅ | 374.84 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_0] | ✅ | 172.36 | ✅ | 385.80 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_4-method_type_1] | ✅ | 164.66 | ✅ | 402.60 |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_0] | ✅ | 186.38 | - | - |
| test_rope[rows_64-cols_128-angle_rows_8-aie_columns_8-method_type_1] | ✅ | 187.10 | - | - |

</details>

<details>
<summary>iron/operators/sigmoid</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 164.64 | ✅ | 360.76 |
| test_sigmoid[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 195.60 | ✅ | 478.08 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 168.70 | ✅ | 363.42 |
| test_sigmoid[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 181.96 | ✅ | 455.78 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 176.54 | ✅ | 677.92 |
| test_sigmoid[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 180.82 | ✅ | 732.34 |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 178.98 | - | - |
| test_sigmoid[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 241.88 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 200.22 | ✅ | 500.94 |
| test_sigmoid[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 196.82 | ✅ | 353.70 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 189.30 | ✅ | 582.24 |
| test_sigmoid[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 168.70 | ✅ | 491.28 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 211.68 | ✅ | 383.24 |
| test_sigmoid[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 176.12 | ✅ | 429.40 |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 206.90 | - | - |
| test_sigmoid[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 221.36 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 168.38 | ✅ | 421.62 |
| test_sigmoid[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 172.72 | ✅ | 308.98 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 171.02 | ✅ | 352.14 |
| test_sigmoid[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 166.76 | ✅ | 316.18 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 152.94 | ✅ | 407.86 |
| test_sigmoid[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 186.72 | ✅ | 823.80 |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 169.28 | - | - |
| test_sigmoid[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 206.24 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 157.00 | ✅ | 303.06 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 147.08 | ✅ | 367.88 |
| test_sigmoid[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 181.44 | ✅ | 369.80 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 157.90 | ✅ | 470.66 |
| test_sigmoid[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 181.42 | ✅ | 969.10 |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 172.08 | - | - |
| test_sigmoid[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 189.66 | - | - |
| test_sigmoid[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2974.64 |
| test_sigmoid[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 761.90 | - | - |

</details>

<details>
<summary>iron/operators/silu</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_silu[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 159.70 | ✅ | 336.94 |
| test_silu[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 202.16 | ✅ | 683.26 |
| test_silu[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 155.62 | ✅ | 487.72 |
| test_silu[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 179.16 | - | - |
| test_silu[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 148.84 | ✅ | 335.44 |
| test_silu[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 153.56 | ✅ | 452.66 |
| test_silu[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 180.22 | ✅ | 695.06 |
| test_silu[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 179.92 | - | - |
| test_silu[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 166.94 | ✅ | 452.34 |
| test_silu[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 175.60 | ✅ | 422.72 |
| test_silu[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 164.00 | ✅ | 430.52 |
| test_silu[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 196.10 | - | - |
| test_silu[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 177.78 | ✅ | 759.08 |
| test_silu[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 148.36 | ✅ | 461.20 |
| test_silu[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 188.48 | - | - |
| test_silu[input_length_8388608-num_aie_columns_4-num_channels_1-tile_size_4096] | - | - | ✅ | 5144.94 |
| test_silu[input_length_8388608-num_aie_columns_8-num_channels_1-tile_size_4096] | ✅ | 655.08 | - | - |

</details>

<details>
<summary>iron/operators/softmax</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_softmax[input_length_2097152-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 530.74 | ✅ | 2693.48 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 161.74 | ✅ | 710.90 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 157.88 | ✅ | 707.08 |
| test_softmax[input_length_32768-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 190.66 | ✅ | 786.24 |

</details>

<details>
<summary>iron/operators/strided_copy</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_strided_copy[bench_flat_4mi] | ✅ | 477.70 | ✅ | 2770.18 |
| test_strided_copy[chunked_transfer] | ✅ | 161.88 | ✅ | 311.04 |
| test_strided_copy[contiguous] | ✅ | 151.24 | ✅ | 337.56 |
| test_strided_copy[four_channels] | ✅ | 178.36 | ✅ | 306.52 |
| test_strided_copy[kv_llama_full] | ✅ | 158.46 | ✅ | 491.78 |
| test_strided_copy[kv_slot0] | ✅ | 159.76 | ✅ | 491.14 |
| test_strided_copy[kv_slot5] | ✅ | 161.16 | ✅ | 327.42 |
| test_strided_copy[kv_slot5_four_channels] | ✅ | 165.94 | ✅ | 393.66 |
| test_strided_copy[kv_slot5_two_channels] | ✅ | 151.52 | ✅ | 336.02 |
| test_strided_copy[kv_slot_last] | ✅ | 152.90 | ✅ | 284.98 |
| test_strided_copy[two_channels] | ✅ | 155.56 | ✅ | 331.14 |
| test_strided_copy[two_channels_chunked] | ✅ | 144.26 | ✅ | 364.98 |
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
| test_swiglu_decode[embedding_dim_1024-hidden_dim_3584] | ✅ | 1018.17 | ✅ | 13939.08 |
| test_swiglu_decode[embedding_dim_2048-hidden_dim_2048] | ✅ | 1048.94 | ✅ | 17087.28 |

</details>

<details>
<summary>iron/operators/swiglu_prefill</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_False] | ✅ | 2150.16 | ✅ | 22916.72 |
| test_swiglu_prefill[seq_len_256-embedding_dim_2048-hidden_dim_2048-prio_accuracy_False-b_col_maj_True] | ✅ | 2380.73 | ✅ | 22480.11 |
| test_weight_layout_reaches_both_gemms[b_col_maj_False] | ✅ | - | ✅ | - |
| test_weight_layout_reaches_both_gemms[b_col_maj_True] | ✅ | - | ✅ | - |

</details>

<details>
<summary>iron/operators/tanh</summary>

| Test | Krackan Status | Krackan Latency (mean) | Phoenix Status | Phoenix Latency (mean) |
|---|---|---|---|---|
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_1-tile_size_1024] | ✅ | 148.84 | ✅ | 378.50 |
| test_tanh[input_length_1024-num_aie_columns_1-num_channels_2-tile_size_512] | ✅ | 174.12 | ✅ | 347.14 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_1-tile_size_512] | ✅ | 188.96 | ✅ | 345.74 |
| test_tanh[input_length_1024-num_aie_columns_2-num_channels_2-tile_size_256] | ✅ | 175.60 | ✅ | 468.10 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_1-tile_size_256] | ✅ | 164.18 | ✅ | 479.22 |
| test_tanh[input_length_1024-num_aie_columns_4-num_channels_2-tile_size_128] | ✅ | 203.92 | ✅ | 561.22 |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_1-tile_size_128] | ✅ | 215.04 | - | - |
| test_tanh[input_length_1024-num_aie_columns_8-num_channels_2-tile_size_64] | ✅ | 209.34 | - | - |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_1-tile_size_2048] | ✅ | 178.44 | ✅ | 489.66 |
| test_tanh[input_length_2048-num_aie_columns_1-num_channels_2-tile_size_1024] | ✅ | 160.92 | ✅ | 462.76 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_1-tile_size_1024] | ✅ | 155.68 | ✅ | 391.54 |
| test_tanh[input_length_2048-num_aie_columns_2-num_channels_2-tile_size_512] | ✅ | 137.00 | ✅ | 476.06 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_1-tile_size_512] | ✅ | 162.08 | ✅ | 400.22 |
| test_tanh[input_length_2048-num_aie_columns_4-num_channels_2-tile_size_256] | ✅ | 158.44 | ✅ | 424.78 |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_1-tile_size_256] | ✅ | 153.36 | - | - |
| test_tanh[input_length_2048-num_aie_columns_8-num_channels_2-tile_size_128] | ✅ | 213.14 | - | - |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_1-tile_size_4096] | ✅ | 150.70 | ✅ | 404.76 |
| test_tanh[input_length_4096-num_aie_columns_1-num_channels_2-tile_size_2048] | ✅ | 143.94 | ✅ | 455.20 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_1-tile_size_2048] | ✅ | 159.68 | ✅ | 341.64 |
| test_tanh[input_length_4096-num_aie_columns_2-num_channels_2-tile_size_1024] | ✅ | 172.74 | ✅ | 474.06 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_1-tile_size_1024] | ✅ | 177.82 | ✅ | 508.18 |
| test_tanh[input_length_4096-num_aie_columns_4-num_channels_2-tile_size_512] | ✅ | 175.14 | ✅ | 740.94 |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_1-tile_size_512] | ✅ | 184.22 | - | - |
| test_tanh[input_length_4096-num_aie_columns_8-num_channels_2-tile_size_256] | ✅ | 213.68 | - | - |
| test_tanh[input_length_8192-num_aie_columns_1-num_channels_2-tile_size_4096] | ✅ | 170.10 | ✅ | 454.72 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_1-tile_size_4096] | ✅ | 152.72 | ✅ | 531.84 |
| test_tanh[input_length_8192-num_aie_columns_2-num_channels_2-tile_size_2048] | ✅ | 163.82 | ✅ | 352.94 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_1-tile_size_2048] | ✅ | 176.64 | ✅ | 480.30 |
| test_tanh[input_length_8192-num_aie_columns_4-num_channels_2-tile_size_1024] | ✅ | 205.04 | ✅ | 450.16 |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_1-tile_size_1024] | ✅ | 183.18 | - | - |
| test_tanh[input_length_8192-num_aie_columns_8-num_channels_2-tile_size_512] | ✅ | 236.58 | - | - |
| test_tanh[input_length_8388608-num_aie_columns_4-num_channels_2-tile_size_4096] | - | - | ✅ | 2868.90 |
| test_tanh[input_length_8388608-num_aie_columns_8-num_channels_2-tile_size_4096] | ✅ | 728.70 | - | - |

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
| test_transpose[M_2048-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 223.06 | ✅ | 1834.08 |
| test_transpose[M_2048-N_128-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 216.82 | ✅ | 541.34 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 224.06 | ✅ | 774.86 |
| test_transpose[M_2048-N_128-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 210.04 | ✅ | 1089.10 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 274.86 | ✅ | 1428.06 |
| test_transpose[M_2048-N_256-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 273.30 | ✅ | 1315.16 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 288.08 | ✅ | 1218.36 |
| test_transpose[M_2048-N_256-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 264.42 | ✅ | 1194.20 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 246.62 | ✅ | 2237.50 |
| test_transpose[M_2048-N_256-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 240.24 | ✅ | 1213.12 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 371.54 | ✅ | 1614.84 |
| test_transpose[M_2048-N_512-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 375.98 | ✅ | 2347.12 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 380.66 | ✅ | 843.80 |
| test_transpose[M_2048-N_512-aie_columns_2-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 358.36 | ✅ | 861.74 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 332.34 | ✅ | 1747.30 |
| test_transpose[M_2048-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 330.70 | ✅ | 579.46 |
| test_transpose[M_2048-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 319.02 | - | - |
| test_transpose[M_2048-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 381.98 | - | - |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 187.92 | ✅ | 1107.98 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_2] | ✅ | 214.78 | ✅ | 548.82 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_4] | ✅ | 260.38 | ✅ | 1437.24 |
| test_transpose[M_2048-N_64-aie_columns_1-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 178.02 | ✅ | 469.68 |
| test_transpose[M_64-N_128-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 176.44 | ✅ | 381.42 |
| test_transpose[M_64-N_128-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 182.92 | ✅ | 406.86 |
| test_transpose[M_64-N_256-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 156.06 | ✅ | 337.20 |
| test_transpose[M_64-N_256-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 170.42 | ✅ | 382.26 |
| test_transpose[M_64-N_256-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 166.02 | ✅ | 377.12 |
| test_transpose[M_64-N_512-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 165.58 | ✅ | 506.44 |
| test_transpose[M_64-N_512-aie_columns_2-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 184.14 | ✅ | 368.56 |
| test_transpose[M_64-N_512-aie_columns_4-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 160.88 | ✅ | 569.16 |
| test_transpose[M_64-N_512-aie_columns_8-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 158.48 | - | - |
| test_transpose[M_64-N_64-aie_columns_1-channels_1-m_64-n_64-s_8-num_batches_1] | ✅ | 156.60 | ✅ | 457.08 |
| test_transpose[M_8192-N_512-aie_columns_4-channels_2-m_64-n_64-s_8-num_batches_1] | - | - | ✅ | 3262.62 |
| test_transpose[M_8192-N_512-aie_columns_8-channels_2-m_64-n_64-s_8-num_batches_1] | ✅ | 954.08 | - | - |

</details>

