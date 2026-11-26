# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 2.01 s | 1.84 s | 🟢 -8.63% |
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.96 s | 1.82 s | 🟢 -7.07% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.48 s | 0.52 s | 🔴 +9.30% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.51 s | 2.38 s | 🟢 -5.41% |

