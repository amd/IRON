
# IRON

Tested on `2026_10_08_02_50_09` at commit `1c1f8e3`.

<details>
<summary>iron/applications/gemma4_flm</summary>

<table>
    <thead>
        <tr><td>Test</td><td>Checks</td><td>TTFT (mean)</td><td>TPS (mean)</td></tr>
    </thead>
    <tbody>
        <tr><td>test_iron_matches_engine[prompt_long_prompt]</td><td>✅ 5/5</td><td>2.31</td><td>26.71</td></tr>
        <tr><td>test_iron_matches_engine[prompt_word_problem]</td><td>✅ 5/5</td><td>0.64</td><td>27.75</td></tr>
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
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_1]</td><td>✅ 5/5</td><td>2.05</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_1024_tokens_40]</td><td>✅ 5/5</td><td>2.08</td><td>7.65</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_1]</td><td>✅ 5/5</td><td>2.02</td><td>n/a</td></tr>
        <tr><td>test_llama_3_2_1b[llama_3.2_1b_prompt_13_tokens_40]</td><td>✅ 5/5</td><td>2.02</td><td>7.59</td></tr>
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

