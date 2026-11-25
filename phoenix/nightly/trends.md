# Performance trends

**Operators added:** `fastflowlm_iron`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1675222.12 µs | 1888281.27 µs | 🔴 +12.72% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 2.06 s | 1.90 s | 🟢 -7.87% |

