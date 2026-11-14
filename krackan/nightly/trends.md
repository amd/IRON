# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_1` | `TTFT` | 5.10 s | 5.45 s | 🔴 +6.82% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.54 s | 0.57 s | 🔴 +5.24% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.52 s | 0.48 s | 🟢 -8.81% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.49 s | 0.52 s | 🔴 +6.68% |

