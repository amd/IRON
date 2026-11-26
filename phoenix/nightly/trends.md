# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1888281.27 µs | 1723473.19 µs | 🟢 -8.73% |
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 6.28 s | 5.57 s | 🟢 -11.34% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.65 s | 1.43 s | 🟢 -12.79% |

