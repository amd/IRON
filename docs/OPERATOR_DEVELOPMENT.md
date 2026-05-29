# Operator Development Workflow

This repository uses a structured workflow for developing and landing new operators.

## Canonical Per-Operator Branches

Each new operator lives on its own dedicated feature branch following this naming convention:

- `feature/operator-<name>` (e.g. `feature/operator-reduction`, `feature/operator-conv3d`)

These branches are created from the current `devel` and contain **only** the production code for that single operator:

- `iron/operators/<name>/` (including `cpu_test.py`)
- `aie_kernels/aie2/<name>.cc`
- `aie_kernels/aie2p/<name>.cc`

**No SPEC documents, no extra documentation, and no code for other operators** are allowed in these branches.

## Worktrees

For convenient development, dedicated worktrees are maintained at:

```
~/iron-worktrees/iron-operator-<name>
```

Example:
```bash
cd ~/iron-worktrees/iron-operator-reduction
```

## Recommended Commit Messages

Keep them short and professional:

```
feat: Add <op> production code (SPEC-0xx)

- Production files only for the <op> operator
- Includes cpu_test.py for CPU reference validation
- Part of the operator development workflow using feature/operator-* branches
```

## Per-Operator CI

When changes are pushed to any `feature/operator-*` branch, GitHub Actions automatically runs only the tests relevant to that operator.

## Landing

Once an operator is ready, a pull request is opened from the `feature/operator-<name>` branch into `devel`.

The full GOLD certification context and cross-operator documentation lives in the main integration branch `feature/model-converter-analysis` (and its `GOLD_STATUS.md`).
