# Performance trends

**Operators added:** `embedding_gemma2`, `gemma4`, `gemma4/reference`, `gemma4_flm`, `granite`, `granite/reference`, `granite_hybrid`, `granite_hybrid/reference`, `llama`, `llama/reference`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `granite` | `granite_4_2_3b_prompt_1024_tokens_40` | `TTFT` | 2.88 s | 3.07 s | 🔴 +6.60% |
| `llama` | `llama_3.2_1b-prompt_1024_tokens_40` | `TTFT` | 0.72 s | 0.77 s | 🔴 +6.46% |
| `llama` | `llama_3.2_3b-prompt_13_tokens_1` | `TTFT` | 1.27 s | 1.20 s | 🟢 -5.57% |

