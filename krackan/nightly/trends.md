# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 1.81 s | 1.95 s | 🔴 +8.13% |
| `granite_hybrid` | `granite_4_0_h_1b_prompt_1024_tokens_40` | `TTFT` | 5.32 s | 5.65 s | 🔴 +6.20% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.53 s | 0.57 s | 🔴 +6.09% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.81 s | 0.75 s | 🟢 -7.77% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_1` | `TTFT` | 0.50 s | 0.52 s | 🔴 +5.19% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.40 s | 2.55 s | 🔴 +5.99% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.18 s | 1.26 s | 🔴 +6.22% |

