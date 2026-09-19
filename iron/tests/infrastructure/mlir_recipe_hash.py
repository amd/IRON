# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""``PythonGeneratedMLIRArtifact`` keys its own cache validity on a recipe hash.

The DAG's own staleness check (``CompilationArtifact.is_available_in_filesystem``)
only compares mtimes: a file exists, is newer than its source, done. That is
blind to a generator whose *kwargs* changed underneath an unchanged filename --
exactly what ``FusedDispatch`` does when it sets ``func_prefix`` on a shared
operator's MLIR generator (see ``mlir_cache_poisoning.py`` for the on-hardware
regression this used to cause). These tests pin the general mechanism that
closes it, directly and without a device: a mismatched recipe hash makes the
artifact unavailable no matter how fresh its mtime is.

Device-free; nothing here compiles or touches the MLIR bindings.
"""

from pathlib import Path

from iron.common.compilation import DesignGenerator, PythonGeneratedMLIRArtifact

# A real module on disk, not a `-c` snippet: DesignGenerator.source_file falls
# back to inspect.getfile(fn), which has nothing to report for code that was
# never in a file.
import iron.tests.infrastructure._recipe_hash_fixture as _fixture


def _artifact(tmp_path, **kwargs):
    gen = DesignGenerator(fn=_fixture.design, kwargs=kwargs)
    return PythonGeneratedMLIRArtifact(str(tmp_path / "op.mlir"), gen)


def _stamp(artifact):
    """Write the .mlir file and its recipe-hash sidecar, as the compile rule does."""
    Path(artifact.filename).write_text("module {}")
    Path(f"{artifact.filename}.recipe_hash").write_text(artifact.recipe_hash())


def test_same_kwargs_gives_the_same_hash(tmp_path):
    a = _artifact(tmp_path, size=1024)
    b = _artifact(tmp_path, size=1024)
    assert a.recipe_hash() == b.recipe_hash()


def test_func_prefix_changes_the_hash(tmp_path):
    """The kwarg FusedDispatch actually mutates."""
    unprefixed = _artifact(tmp_path, size=1024)
    prefixed = _artifact(tmp_path, size=1024, func_prefix="op0_")
    assert unprefixed.recipe_hash() != prefixed.recipe_hash()


def test_stamped_artifact_with_unchanged_kwargs_is_available(tmp_path):
    artifact = _artifact(tmp_path, size=1024)
    _stamp(artifact)
    assert artifact.is_available_in_filesystem()


def test_mutating_kwargs_after_stamping_makes_it_unavailable(tmp_path):
    """The exact shape of the fused-build bug: mutate generator.kwargs in
    place, on the same artifact, without touching the file or its mtime."""
    artifact = _artifact(tmp_path, size=1024)
    _stamp(artifact)
    assert artifact.is_available_in_filesystem()

    artifact.generator.kwargs["func_prefix"] = "op0_"
    assert not artifact.is_available_in_filesystem(), (
        "mtime alone said this was fine; the recipe hash has to catch what "
        "mtime cannot see"
    )


def test_missing_stamp_is_not_available(tmp_path):
    """A file written before this mechanism existed has no sidecar at all --
    treat that as unknown, not as trivially valid."""
    artifact = _artifact(tmp_path, size=1024)
    Path(artifact.filename).write_text("module {}")
    assert not artifact.is_available_in_filesystem()


def test_device_kwarg_is_hashed_by_identity_not_by_object_repr(tmp_path):
    """A fresh device object of the same arch must not look like a different
    recipe -- default object repr embeds a memory address, which changes on
    every construction even when nothing about the device did."""

    class _FakeDevice:
        arch = "npu2"
        cols = 8
        rows = 6

    a = _artifact(tmp_path, size=1024, dev=_FakeDevice())
    b = _artifact(tmp_path, size=1024, dev=_FakeDevice())
    assert a.recipe_hash() == b.recipe_hash()
