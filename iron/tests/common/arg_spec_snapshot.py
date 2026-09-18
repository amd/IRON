#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Pin every operator's arg spec, so a refactor cannot change one by accident.

``get_arg_spec()`` is moving out of each ``op.py`` and onto a shape function
declared with the operator itself. That is a pure refactor: the specs it
produces must be identical before and after, for every operator and every
configuration. "Identical" is not something a reviewer can check by eye across
22 classes, so it is recorded here instead -- ``arg_spec_snapshot.json`` is the
pre-refactor truth, generated on ``devel`` and committed alongside it.

The snapshot covers both device generations because a spec may depend on the
device: an operator reads the ShimDMA column limit at construction, and a shape
that silently differed between npu1 and npu2 would otherwise land as a
correctness bug on whichever one CI does not run.

Device-free: this sets a device *description* (``from_name``), never a live
one, so it runs anywhere. Regenerate deliberately with::

    python -m iron.tests.common.arg_spec_snapshot --write

Never regenerate to make a failure go away. A diff here means either the
refactor changed behaviour, or a spec genuinely changed and the commit that
changes it should say why.
"""

import argparse
import importlib
import json
from pathlib import Path

import aie.utils as aie_utils
import pytest
from aie.iron.device import from_name

from iron.tests.common.arg_spec_cases import CASES, dtype_name

SNAPSHOT_PATH = Path(__file__).with_name("arg_spec_snapshot.json")

# Four columns is the widest both generations support here, and column count
# feeds the ShimDMA limit that several operators validate against.
DEVICES = ("npu1", "npu2")
N_COLS = 4

# Operators that need an optional third-party package to construct. These are
# skipped on both sides of the comparison when the package is absent, rather
# than dropped from the matrix: a snapshot generated without ``stream`` must
# not read as "case added" on a machine that has it, and vice versa.
OPTIONAL_REQUIREMENTS = {"_SwiGLUStreamGroup": "stream"}


def _unavailable_classes():
    """Class names whose optional requirement is not importable here."""
    unavailable = set()
    for class_name, module_name in OPTIONAL_REQUIREMENTS.items():
        try:
            importlib.import_module(module_name)
        except ImportError:
            unavailable.add(class_name)
    return unavailable


def _drop_unavailable(recorded):
    """Remove entries for operators whose optional requirement is missing."""
    skipped = _unavailable_classes()
    return {
        key: value
        for key, value in recorded.items()
        if key.split("(", 1)[0] not in skipped
    }


def _record_specs(device_name):
    """Return ``{case_key: [[direction, shape, dtype], ...]}`` for one device."""
    previous = aie_utils.get_current_device()
    aie_utils.set_current_device(from_name(device_name, n_cols=N_COLS))
    try:
        recorded = {}
        skipped = _unavailable_classes()
        for module_name, class_name, cases in CASES:
            if class_name in skipped:
                continue
            module = importlib.import_module(f"iron.operators.{module_name}.op")
            operator_class = getattr(module, class_name)
            for kwargs in cases:
                # The kwargs are part of the key, so a case that is edited
                # shows up as an added/removed entry rather than a silently
                # changed value.
                key = f"{class_name}({json.dumps(kwargs, sort_keys=True, default=str)})"
                specs = operator_class(**kwargs).get_arg_spec()
                recorded[key] = [
                    [spec.direction, list(spec.shape), dtype_name(spec.dtype)]
                    for spec in specs
                ]
        return recorded
    finally:
        aie_utils.set_current_device(previous)


def current_snapshot():
    """Derive the full snapshot from the operators as they are right now."""
    return {device: _record_specs(device) for device in DEVICES}


def test_snapshot_exists():
    assert SNAPSHOT_PATH.exists(), (
        f"{SNAPSHOT_PATH.name} is missing. Generate it with "
        "`python -m iron.tests.common.arg_spec_snapshot --write`."
    )


@pytest.mark.parametrize("device_name", DEVICES)
def test_arg_specs_match_snapshot(device_name):
    """Every operator's spec still matches what was recorded."""
    expected = _drop_unavailable(json.loads(SNAPSHOT_PATH.read_text())[device_name])
    actual = _record_specs(device_name)

    missing = sorted(set(expected) - set(actual))
    added = sorted(set(actual) - set(expected))
    assert not missing, f"[{device_name}] cases dropped from the matrix: {missing}"
    assert (
        not added
    ), f"[{device_name}] cases added without regenerating the snapshot: {added}"

    changed = {
        key: {"recorded": expected[key], "now": actual[key]}
        for key in expected
        if expected[key] != actual[key]
    }
    assert not changed, f"[{device_name}] arg specs changed:\n" + json.dumps(
        changed, indent=2, sort_keys=True
    )


def test_every_operator_with_a_spec_is_covered():
    """The matrix must not quietly stop covering an operator.

    A refactor that dropped an operator from CASES would still pass the
    comparison above -- it would just check less. This fails instead.
    """
    from iron.common.sequence import OperatorSequence

    covered = {class_name for _, class_name, _ in CASES}
    operators_dir = Path(__file__).resolve().parents[2] / "operators"
    declared = set()
    for op_path in sorted(operators_dir.glob("*/op.py")):
        module = importlib.import_module(f"iron.operators.{op_path.parent.name}.op")
        for name, obj in vars(module).items():
            if not (
                isinstance(obj, type)
                and getattr(obj, "__module__", None) == module.__name__
                and hasattr(obj, "get_arg_spec")
            ):
                continue
            # Every class inherits the attribute, so its presence proves
            # nothing. OperatorSequence subclasses are composites built from a
            # runlist and raise from get_arg_spec() on purpose -- they have no
            # unified spec to pin, only per-buffer layouts.
            if issubclass(obj, OperatorSequence):
                continue
            declared.add(name)
    assert (
        declared <= covered
    ), f"operators missing from CASES: {sorted(declared - covered)}"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--write",
        action="store_true",
        help="regenerate the snapshot from the current operators",
    )
    args = parser.parse_args()
    if not args.write:
        parser.error("nothing to do without --write; run under pytest to check")
    SNAPSHOT_PATH.write_text(
        json.dumps(current_snapshot(), indent=2, sort_keys=True) + "\n"
    )
    print(f"wrote {SNAPSHOT_PATH}")


if __name__ == "__main__":
    main()
