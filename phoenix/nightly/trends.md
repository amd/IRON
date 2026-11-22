# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1733833.55 µs | 1832343.05 µs | 🔴 +5.68% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 3.25 s | 2.40 s | 🟢 -26.10% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.92 s | 1.79 s | 🟢 -6.31% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 2.17 s | 1.69 s | 🟢 -22.15% |

