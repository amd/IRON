# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1643673.41 µs | 1862443.59 µs | 🔴 +13.31% |
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 5.22 s | 6.16 s | 🔴 +17.99% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TPS` | 3.13 tokens/s | 3.29 tokens/s | 🟢 +5.24% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.76 s | 1.52 s | 🟢 -13.69% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.72 s | 1.90 s | 🔴 +10.90% |
| `long_context` | `gemma4_e2b_each_step-16384` | `TTFT` | 112.16 s | 120.39 s | 🔴 +7.34% |
| `long_context` | `gemma4_e2b_each_step-32768` | `TTFT` | 112.72 s | 120.85 s | 🔴 +7.21% |

