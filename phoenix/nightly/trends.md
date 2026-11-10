# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1851967.80 µs | 1706418.58 µs | 🟢 -7.86% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 3.18 s | 3.35 s | 🔴 +5.35% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.68 s | 1.83 s | 🔴 +8.65% |
| `long_context` | `llama_3.2_1b_each_step-16384` | `TTFT` | 18.66 s | 17.58 s | 🟢 -5.76% |
| `long_context` | `llama_3.2_1b_each_step-32768` | `TTFT` | 18.74 s | 17.48 s | 🟢 -6.73% |
| `long_context` | `llama_3.2_1b_each_step-65536` | `TTFT` | 18.71 s | 17.51 s | 🟢 -6.42% |
| `long_context` | `llama_3.2_1b_each_step-whole` | `TTFT` | 18.70 s | 17.47 s | 🟢 -6.56% |
| `long_context` | `llama_3.2_3b_each_step-16384` | `TTFT` | 67.76 s | 41.51 s | 🟢 -38.73% |
| `long_context` | `llama_3.2_3b_each_step-32768` | `TTFT` | 67.87 s | 41.42 s | 🟢 -38.96% |
| `long_context` | `llama_3.2_3b_each_step-65536` | `TTFT` | 67.73 s | 41.34 s | 🟢 -38.97% |
| `long_context` | `llama_3.2_3b_each_step-whole` | `TTFT` | 67.76 s | 41.44 s | 🟢 -38.84% |

