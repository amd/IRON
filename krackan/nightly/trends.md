# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 2.05 s | 1.87 s | 🟢 -8.76% |
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.95 s | 1.85 s | 🟢 -5.13% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_1` | `TTFT` | 5.11 s | 5.53 s | 🔴 +8.15% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.39 s | 2.51 s | 🔴 +5.06% |

