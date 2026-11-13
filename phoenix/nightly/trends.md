# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_1` | `TTFT` | 5.30 s | 5.81 s | 🔴 +9.66% |
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 6.05 s | 5.22 s | 🟢 -13.62% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 3.09 s | 3.28 s | 🔴 +6.18% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.92 s | 1.76 s | 🟢 -8.29% |
| `long_context` | `gemma4_e2b_each_step-16384` | `TTFT` | 120.40 s | 112.16 s | 🟢 -6.85% |
| `long_context` | `gemma4_e2b_each_step-32768` | `TTFT` | 120.39 s | 112.72 s | 🟢 -6.37% |

