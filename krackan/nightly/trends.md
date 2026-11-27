# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_1` | `TTFT` | 4.14 s | 4.39 s | 🔴 +6.06% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_40` | `TTFT` | 4.46 s | 4.20 s | 🟢 -5.72% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.79 s | 0.71 s | 🟢 -9.87% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.28 s | 1.16 s | 🟢 -9.37% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.29 s | 1.15 s | 🟢 -10.51% |

