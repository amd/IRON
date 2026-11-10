# Performance trends

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `gemma4` | `gemma4-long-40` | `TTFT` | 5.85 s | 5.52 s | 🟢 -5.65% |
| `gemma4` | `gemma4-short-1` | `TTFT` | 5.45 s | 5.15 s | 🟢 -5.51% |
| `granite` | `granite_4_2_3b_prompt_13_tokens_1` | `TTFT` | 1.97 s | 1.83 s | 🟢 -6.84% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_1` | `TTFT` | 0.56 s | 0.53 s | 🟢 -5.65% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.47 s | 0.35 s | 🟢 -25.07% |
| `llama` | `llama_3.2_1b-prompt_13_tokens_40` | `TTFT` | 0.52 s | 0.49 s | 🟢 -6.07% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.27 s | 1.15 s | 🟢 -9.66% |

