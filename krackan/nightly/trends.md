# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 1.96 s | 1.81 s | 🟢 -7.92% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_40` | `TTFT` | 5.64 s | 5.32 s | 🟢 -5.61% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.73 s | 0.81 s | 🔴 +11.09% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.53 s | 0.50 s | 🟢 -5.55% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.47 s | 0.53 s | 🔴 +11.19% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_1` | `TTFT` | 2.01 s | 2.13 s | 🔴 +5.76% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.10 s | 2.40 s | 🔴 +14.61% |

