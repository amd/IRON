# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_1` | `TTFT` | 2.74 s | 2.88 s | 🔴 +5.30% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.56 s | 0.53 s | 🟢 -5.94% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.49 s | 0.53 s | 🔴 +7.28% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.53 s | 0.47 s | 🟢 -9.77% |

