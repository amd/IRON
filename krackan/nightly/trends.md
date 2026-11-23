# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.96 s | 1.76 s | 🟢 -10.47% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.53 s | 0.57 s | 🔴 +6.82% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.73 s | 0.79 s | 🔴 +8.65% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.47 s | 0.50 s | 🔴 +5.94% |

