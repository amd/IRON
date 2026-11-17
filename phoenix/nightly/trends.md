# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `embedding_gemma2` | `long_document` | `Latency` | 1645737.76 µs | 1795615.88 µs | 🔴 +9.11% |
| `embedding_gemma2` | `name_living_room` | `Latency` | 1594848.44 µs | 1499559.41 µs | 🟢 -5.97% |
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 6.41 s | 6.06 s | 🟢 -5.47% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.75 s | 1.95 s | 🔴 +11.32% |

