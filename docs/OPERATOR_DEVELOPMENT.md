# Operator Development Workflow

This repository uses a structured, production-oriented workflow for developing and integrating new NPU operators. Each operator's production code is isolated on dedicated branches to enable focused review, automated per-operator CI, and strict adherence to hygiene standards.

## Integration Branch and Table Branches

- **Integration branch**: `feature/model-converter-analysis`

  This branch serves as the primary workspace for model analysis, operator specifications, GOLD certification records (`GOLD_STATUS.md`), planning artifacts, and full project context.

- **Per-operator table branches** (`feature/operator-*`):

  These are the exact branches enumerated in the inventory table of [docs/MASTER-SPEC.md](MASTER-SPEC.md). Examples include `feature/operator-reduction`, `feature/operator-conv2d`, `feature/operator-maxpool`, `feature/operator-avgpool`, `feature/operator-conv3d`, `feature/operator-infrastructure`, and similar branches for other operators and fixes.

  Each such branch is the authoritative source for a single operator's contribution.

## Production-Code-Only Rule

`feature/operator-<name>` branches contain **exclusively** the production code for one operator:

- `iron/operators/<name>/` (all required Python modules, including `op.py`, `design.py`, `reference.py`, `test.py`, and `cpu_test.py` where present for CPU reference validation)
- `aie_kernels/aie2/<name>.cc`
- `aie_kernels/aie2p/<name>.cc` (as applicable)

**Prohibited** on these branches (enforced by the Hygiene agent):

- Any `SPEC-*.md` files or supplementary documentation
- Production code, tests, or changes for any other operator
- Unrelated modifications to build configuration, scripts, or infrastructure (except on dedicated infrastructure branches)

All broader documentation, specifications, and cross-operator analysis remain exclusively on the integration branch.

## Dedicated Worktrees

Dedicated git worktrees provide isolated development environments for each per-operator branch without affecting the primary clone:

Recommended path: `~/iron-worktrees/iron-operator-<name>`

**Setup examples** (executed from a checkout of the integration branch):

```bash
# Attach worktree to an existing per-operator branch
git worktree add ~/iron-worktrees/iron-operator-reduction feature/operator-reduction

# Create and attach a new per-operator branch
git worktree add -b feature/operator-newop ~/iron-worktrees/iron-operator-newop
```

All development, testing, and formatting occur inside the worktree. This approach supports concurrent work on multiple operators and maintains a clean primary working directory.

## Per-Operator CI

Pushes and pull requests targeting any `feature/operator-*` branch trigger the dedicated workflow defined in `.github/workflows/operator-ci.yml`:

- The operator name is derived automatically from the branch.
- CPU reference validation is executed (`pytest` with `-k "cpu or reference"` selectors) together with test collection (`--collectonly`).
- No NPU hardware or XRT is required; the workflow validates pure-CPU paths in `reference.py` and `cpu_test.py` (including `generate_golden_reference` and direct `*_cpu` functions).
- The repository-wide lint workflow (`.github/workflows/ci-lint.yml`) also executes on relevant events, enforcing REUSE license headers, Black formatting for Python, and clang-format for C++.

Hardware-accelerated NPU tests are run manually by developers with access to Ryzen AI devices, typically under the `iron314` conda environment.

## Development Process

1. **Analysis and Specification**  
   On the integration branch, use `iron.model_analysis` tooling to identify gaps and generate specifications. All SPEC documents and updates to tracking files (MASTER-SPEC.md, GOLD_STATUS.md, etc.) are made here only.

2. **Branch Creation and Hygiene Coordination**  
   Coordinate with the Hygiene agent to initialize a `feature/operator-<name>` branch containing precisely the allowed production files. The branch must pass production-code-only validation before development proceeds.

3. **Worktree Activation**  
   Create or attach the dedicated worktree and perform all edits there.

4. **Implementation and Local Checks**  
   - Build out or refine the operator, preserving clear separation between CPU reference implementations and NPU execution paths.
   - Validate CPU references extensively:
     ```
     python -m pytest iron/operators/<name>/ -q -k "cpu or reference or cpu_only" --tb=short
     ```
   - Run collection-only checks and exercise `get_params` / import safety (no XRT dependency at import time).
   - Apply code hygiene: invoke `scripts/hooks/pre-push` (or equivalent black / clang-format-wrapper.py / reuse commands) before every push.

5. **Automated Gates**  
   Push to the per-operator branch to invoke CI. All per-operator tests and lint checks must pass. Engage the CI agent if operator-specific test markers or workflow extensions are required.

6. **Certification and Pull Request**  
   Upon achieving production readiness (CPU/Torch parity, kernel correctness, full hygiene compliance), reference the GOLD certification process documented on the integration branch.  
   Create a pull request from `feature/operator-<name>` to `devel` (targeting amd/iron). PR descriptions must cite the relevant SPEC, this workflow document, and the integration branch for full context.

7. **Post-Landing Maintenance**  
   Update references and status on the integration branch after merge. Retain per-operator branches for audit history as needed.

## Commit Message Conventions

Use concise, professional messages:

```
feat(operator): Add conv3d production code (SPEC-015)

- Production files only for conv3d operator per production-code-only rule
- iron/operators/conv3d/ + AIE2/AIE2P kernels
- cpu_test.py with golden reference generation and direct CPU validation
- Per feature/operator-conv3d branch and worktree workflow
```

## Agent Coordination

- **Hygiene Agent**: Owns branch purity checks, file filtering for per-operator branches, pre-push hook maintenance, and enforcement of the production-code-only rule.
- **CI Agent**: Maintains operator-ci.yml, ci-lint.yml, pytest configuration, and test selection logic to ensure reliable isolated validation of each operator.
- Documentation for this workflow (including updates to this file and the corresponding section of README.md) is maintained solely on the integration branch.

This model enables high-quality, independently verifiable operator additions while retaining complete analytical and historical context on the integration branch.

## References

- Per-operator CI definition: `.github/workflows/operator-ci.yml`
- Linting CI: `.github/workflows/ci-lint.yml`
- Pre-push hygiene hook: `scripts/hooks/pre-push`
- Branch inventory: `docs/MASTER-SPEC.md`
- Certification status: `GOLD_STATUS.md`
- Main README operator section

---

**Maintained by:** Anthony Mikinka
