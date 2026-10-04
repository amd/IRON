# Performance trends

**Operators dropped:** `swiglu_prefill_stream`

Benchmarks that moved by at least 5% and by more than 2x the spread the runs measured:

| Operator | Parametrization | Metric | Previous | Current | Change |
|---|---|---|---|---|---|
| `flm/gemm` | `M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even` | `Bandwidth` | 10.69 | 13.68 | 🟢 +28.02% |
| `flm/gemm` | `M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even` | `Latency` | 7668.68 | 5989.32 | 🟢 -21.90% |
| `flm/gemm` | `M_2048-K_2560-N_10240-epilogue_none-clamp_None-rounding_conv_even` | `Throughput` | 14008.65 | 17933.86 | 🟢 +28.02% |

