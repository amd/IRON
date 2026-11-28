# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_40` | `TTFT` | 1.83 s | 2.00 s | 🔴 +9.38% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.54 s | 0.57 s | 🔴 +5.37% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.52 s | 0.49 s | 🟢 -5.90% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.16 s | 1.26 s | 🔴 +8.65% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.15 s | 1.29 s | 🔴 +11.77% |

