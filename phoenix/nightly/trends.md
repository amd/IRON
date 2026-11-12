# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1796268.40 µs | 1656369.78 µs | 🟢 -7.79% |
| `granite` | `granite_4_2_3b_prompt_1024_tokens_1` | `TTFT` | 5.77 s | 5.30 s | 🟢 -8.18% |
| `llama` | `llama_3.2_3b-prompt_1024_tokens_40` | `TTFT` | 3.26 s | 3.09 s | 🟢 -5.41% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.71 s | 1.92 s | 🔴 +12.26% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.62 s | 1.79 s | 🔴 +10.17% |

