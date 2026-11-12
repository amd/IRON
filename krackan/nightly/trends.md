# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.79 s | 2.01 s | 🔴 +12.38% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_40` | `TPS` | 1.99 tokens/s | 1.88 tokens/s | 🔴 -5.73% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.80 s | 0.73 s | 🟢 -8.94% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.52 s | 0.49 s | 🟢 -6.47% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.17 s | 1.25 s | 🔴 +7.45% |

