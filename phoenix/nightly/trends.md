# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1832343.05 µs | 1721283.83 µs | 🟢 -6.06% |
| `embedding_gemma2` | `name_passage` | `Latency` | 5055136.35 µs | 4794891.64 µs | 🟢 -5.15% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 2.40 s | 3.22 s | 🔴 +34.18% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.69 s | 2.13 s | 🔴 +25.65% |

