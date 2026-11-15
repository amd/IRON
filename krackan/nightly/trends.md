# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.74 s | 0.79 s | 🔴 +6.85% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.48 s | 0.52 s | 🔴 +9.66% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.58 s | 2.37 s | 🟢 -8.24% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.27 s | 1.18 s | 🟢 -7.58% |

