# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `name_extended` | `Latency` | 5082747.32 µs | 4814750.03 µs | 🟢 -5.27% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.72 s | 1.92 s | 🔴 +11.61% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.87 s | 2.17 s | 🔴 +16.31% |

