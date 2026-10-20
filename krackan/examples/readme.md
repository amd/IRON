
# IRON

Tested on `2026_10_20_23_36_03` at commit `b3ba3cf`.

<details>
<summary>iron/applications/gemma4_flm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_engine_reload_rebuilds_override_state[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_iron_matches_engine[prompt_long_prompt]</td><td>✅ 5/5</td><td>2.27</td><td>26.70</td></tr>
        <tr><td>test_iron_matches_engine[prompt_word_problem]</td><td>✅ 5/5</td><td>0.64</td><td>27.87</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/applications/gemma4_flm/gemm_dequant</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_all_gemm_dequant_selections[iter0]</td><td>✅ 1/1</td><td>0.85</td><td>n/a</td></tr>
        <tr><td>test_all_gemm_dequant_selections[iter1]</td><td>✅ 1/1</td><td>0.87</td><td>n/a</td></tr>
        <tr><td>test_all_gemm_dequant_selections[iter2]</td><td>✅ 1/1</td><td>0.86</td><td>n/a</td></tr>
        <tr><td>test_all_gemm_dequant_selections[iter3]</td><td>✅ 1/1</td><td>0.87</td><td>n/a</td></tr>
        <tr><td>test_all_gemm_dequant_selections[iter4]</td><td>✅ 1/1</td><td>0.88</td><td>n/a</td></tr>
        <tr><td>test_example_overrides_only_gemm_and_dequant[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_example_overrides_only_gemm_and_dequant[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_example_overrides_only_gemm_and_dequant[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_example_overrides_only_gemm_and_dequant[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_example_overrides_only_gemm_and_dequant[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_layout_is_a_permutation[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_layout_is_a_permutation[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_layout_is_a_permutation[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_layout_is_a_permutation[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_layout_is_a_permutation[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_uses_floor_rounding[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_uses_floor_rounding[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_uses_floor_rounding[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_uses_floor_rounding[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_uses_floor_rounding[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_writes_a_sidecar[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_writes_a_sidecar[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_writes_a_sidecar[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_writes_a_sidecar[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_offline_dequant_writes_a_sidecar[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_plot_contains_all_selections[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_plot_contains_all_selections[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_plot_contains_all_selections[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_plot_contains_all_selections[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_plot_contains_all_selections[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prepare_model_links_inputs_and_owns_sidecars[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prepare_model_links_inputs_and_owns_sidecars[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prepare_model_links_inputs_and_owns_sidecars[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prepare_model_links_inputs_and_owns_sidecars[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_prepare_model_links_inputs_and_owns_sidecars[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

<details>
<summary>iron/applications/llama_3.2_1b</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1]</td><td>✅ 5/5</td><td>2.06</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40]</td><td>✅ 5/5</td><td>2.09</td><td>7.66</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1]</td><td>✅ 5/5</td><td>2.00</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40]</td><td>✅ 5/5</td><td>2.01</td><td>7.62</td></tr>
        <tr><td>test_llama_3_2_1b_accuracy[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_accuracy[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_accuracy[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_accuracy[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_accuracy[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_determinism[iter0]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_determinism[iter1]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_determinism[iter2]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_determinism[iter3]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b_determinism[iter4]</td><td>✅ 1/1</td><td>n/a</td><td>n/a</td></tr>
    </tbody>
</table>

</details>

