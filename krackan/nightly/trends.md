# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_1` | `TTFT` | 2.89 s | 2.74 s | 🟢 -5.23% |
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 1.89 s | 1.99 s | 🔴 +5.56% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.76 s | 0.72 s | 🟢 -5.43% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.52 s | 0.49 s | 🟢 -6.27% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.25 s | 1.31 s | 🔴 +5.08% |

