# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 5.25 s | 6.01 s | 🔴 +14.59% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.82 s | 1.71 s | 🟢 -6.21% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.76 s | 1.57 s | 🟢 -10.84% |

