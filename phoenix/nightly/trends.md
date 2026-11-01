# Performance trends

**Operators added:** `embedding_gemma2`, `gemma4/reference`, `granite`, `granite/reference`, `granite_hybrid`, `granite_hybrid/reference`, `llama`, `llama/reference`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 5.28 s | 6.34 s | 🔴 +20.03% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_40` | `TTFT` | 1.85 s | 1.63 s | 🟢 -11.74% |

