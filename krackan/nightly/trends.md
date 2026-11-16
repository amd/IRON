# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_1` | `TTFT` | 5.19 s | 5.46 s | 🔴 +5.06% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.57 s | 0.52 s | 🟢 -7.46% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.79 s | 0.73 s | 🟢 -8.05% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.52 s | 0.47 s | 🟢 -9.53% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_1` | `TTFT` | 2.15 s | 2.01 s | 🟢 -6.58% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.37 s | 2.10 s | 🟢 -11.63% |

