# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 2.03 s | 1.85 s | 🟢 -9.14% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_40` | `TPS` | 2.00 tokens/s | 1.88 tokens/s | 🔴 -5.79% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.75 s | 0.80 s | 🔴 +6.64% |

