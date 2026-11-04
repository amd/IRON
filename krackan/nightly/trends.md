# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.78 s | 1.97 s | 🔴 +10.87% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_13_tokens_1` | `TTFT` | 4.39 s | 4.16 s | 🟢 -5.32% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.49 s | 0.46 s | 🟢 -5.15% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.52 s | 0.49 s | 🟢 -6.53% |

