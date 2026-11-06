# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1847325.78 µs | 1717426.55 µs | 🟢 -7.03% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TPS` | 3.24 tokens/s | 3.40 tokens/s | 🟢 +5.03% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.85 s | 1.97 s | 🔴 +6.37% |

