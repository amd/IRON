# Operator Enablement Status - 5 New Operators

**Date**: 2026-05-28

**Integration branch**: `feature/model-converter-analysis`

**Canonical per-operator branches** (exact names per SPEC table and `docs/OPERATOR_DEVELOPMENT.md`):

- `feature/operator-reduction` (SPEC-011)
- `feature/operator-conv2d` (SPEC-012)
- `feature/operator-maxpool` (SPEC-013)
- `feature/operator-avgpool` (SPEC-014)
- `feature/operator-conv3d` (SPEC-015)

(Note: `feature/operator-types-runtime` (SPEC-010) is the related types and runtime foundation branch.)

## Summary

Production code for five new operators (Reduction, Conv2D, MaxPool, AvgPool, Conv3D) has been delivered on dedicated branches.

Each branch follows the strict per-operator workflow:

- Contains **only** the production files for that operator (no SPEC-*.md, no docs, no other operators).
- Includes `cpu_test.py` for pure-CPU golden reference validation.
- AIE2 and AIE2P bf16 kernels in `aie_kernels/`.
- Primary datatype: bfloat16.

## Validation

- CPU reference: `generate_golden_reference` + direct `*_cpu` + Torch parity under iron314 (no XRT required for reference paths).
- Pre-push: black, clang-format-wrapper, reuse checks passed on operator files and kernels.
- AGENTS.md compliant.

## Per-Operator Status

| Operator  | Branch                          | Spec    | cpu_test.py | Kernels (AIE2/AIE2P) | Notes |
|-----------|---------------------------------|---------|-------------|----------------------|-------|
| reduction | `feature/operator-reduction`   | SPEC-011 | ✅         | ✅                  | Sum, mean, max, min; 2048-tile cases |
| conv2d    | `feature/operator-conv2d`      | SPEC-012 | ✅         | ✅                  | Full config families |
| maxpool   | `feature/operator-maxpool`     | SPEC-013 | ✅         | ✅                  | k2/s2/p0 + extensive cases |
| avgpool   | `feature/operator-avgpool`     | SPEC-014 | ✅         | ✅                  | Reference paths clean |
| conv3d    | `feature/operator-conv3d`      | SPEC-015 | ✅         | ✅                  | 3D golden + dim helpers |

## Documentation Coordination

Full details and any certification evidence are maintained in this integration branch under `docs/`.

- See `docs/OPERATOR_DEVELOPMENT.md` for the canonical branch workflow and recommended commit template.
- See `docs/MASTER-SPEC.md` and `docs/PR-TRACKER.md` for inventory.
- Gold-certified variant branches (e.g. `feature/*-gold-certified`) are not part of the primary flow. Use the exact `feature/operator-*` names listed above per the SPEC table.

**Status**: Production code complete on canonical branches. Ready for review and landing to `devel`.

*Updated for commit message & GitHub output hygiene (exact table names, professional style).*
