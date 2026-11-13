# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 2.01 s | 1.88 s | 🟢 -6.48% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_40` | `TTFT` | 5.50 s | 5.77 s | 🔴 +5.04% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.31 s | 1.24 s | 🟢 -5.67% |

