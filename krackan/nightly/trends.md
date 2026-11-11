# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 1.83 s | 2.05 s | 🔴 +11.72% |
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.96 s | 1.79 s | 🟢 -8.79% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_40` | `TPS` | 1.89 tokens/s | 1.99 tokens/s | 🟢 +5.19% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.53 s | 0.57 s | 🔴 +6.45% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.75 s | 0.80 s | 🔴 +7.11% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.49 s | 0.52 s | 🔴 +6.96% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.28 s | 1.17 s | 🟢 -9.24% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.15 s | 1.26 s | 🔴 +9.74% |

