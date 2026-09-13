#!/usr/bin/env python3
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""KernelObjectArtifact.is_available_in_filesystem() must be content-addressed, not
mtime-compared -- see iron/common/cache.py's module docstring and
2026-09-12-compilationartifact-is-a-third-mtime-only-cache-instance for the live bug
(a shared build cache silently linked the wrong SCORES_ROWBATCH arm's compiled object)
this replaces.

Per method-content-addressed-cache-key-discipline: the row-4 self-test below asserts a
mutation (1) changes the content key, (2) misses the cache/manifest, and (3) is not
silently served a stale artifact -- then a fourth test sabotages content_key to a
constant and confirms that mutation test goes RED, proving the guard is not vacuous.

No Peano/aiecc invocation anywhere here: a KernelObjectArtifact's inputs and the
manifest KernelCompilationRule writes are plain files, and this suite manufactures
both by hand, the same way iron/tests/compilation/kernel_object_arch_isolation.py
manufactures a stale leftover object without a real compiler.
"""

import json
from pathlib import Path
from unittest import mock

from iron.common.cache import ContentStore, content_digest, content_key, parse_depfile
from iron.common.compilation import SourceArtifact
from iron.common.compilation.base import KernelObjectArtifact, KernelCompilationRule


def _write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def _built_artifact(tmp_path, *, source_text="int f() { return 1; }\n", extra_flags=()):
    """A KernelObjectArtifact plus a hand-written depfile and manifest, as if
    KernelCompilationRule._record_cache_entry had just run after a real compile."""
    source = tmp_path / "kernel.cc"
    _write(source, source_text)
    header = tmp_path / "shared.h"
    _write(header, "// shared\n")

    obj = tmp_path / "kernel.o"
    _write(obj, "<fake compiled bytes>")
    depfile = tmp_path / "kernel.o.d"
    _write(depfile, f"{obj}: {source} {header}\n")

    artifact = KernelObjectArtifact(
        filename=str(obj),
        dependencies=[SourceArtifact(str(source))],
        extra_flags=list(extra_flags),
    )
    inputs = parse_depfile(str(depfile))
    flags = artifact._content_flags()
    toolchain = "toolchain-v1"
    key = content_key(inputs, flags, toolchain)
    manifest = {"key": key, "inputs": inputs, "flags": flags, "toolchain": toolchain}
    _write(
        Path(f"{obj}.contentkey.json"),
        json.dumps(manifest, sort_keys=True),
    )
    return artifact, source, header, key, toolchain


def _with_fixed_toolchain(toolchain):
    return mock.patch(
        "iron.common.compilation.base._peano_toolchain_fingerprint",
        return_value=toolchain,
    )


# --- content_key / ContentStore / parse_depfile, in isolation ---------------------


def test_content_key_changes_when_an_input_files_bytes_change(tmp_path):
    a = tmp_path / "a.txt"
    a.write_text("v1")
    key1 = content_key([str(a)], {}, "tc")
    a.write_text("v2")
    key2 = content_key([str(a)], {}, "tc")
    assert key1 != key2


def test_content_key_changes_when_a_flag_changes_but_files_do_not(tmp_path):
    a = tmp_path / "a.txt"
    a.write_text("stable")
    key1 = content_key([str(a)], {"rowbatch": 1}, "tc")
    key2 = content_key([str(a)], {"rowbatch": 4}, "tc")
    assert key1 != key2


def test_content_key_is_order_independent_over_inputs_and_flags(tmp_path):
    a, b = tmp_path / "a.txt", tmp_path / "b.txt"
    a.write_text("A")
    b.write_text("B")
    forward = content_key([str(a), str(b)], {"x": 1, "y": 2}, "tc")
    backward = content_key([str(b), str(a)], {"y": 2, "x": 1}, "tc")
    assert forward == backward


def test_content_key_fails_closed_on_an_unreadable_input(tmp_path):
    missing = tmp_path / "does-not-exist.txt"
    present = tmp_path / "present.txt"
    present.write_text("x")
    key_missing = content_key([str(missing)], {}, "tc")
    key_present = content_key([str(present)], {}, "tc")
    # A missing input must not collapse onto a key some OTHER present input
    # could also produce, and must not raise.
    assert key_missing != key_present
    assert "<unreadable:" in content_digest(missing)


def test_content_store_put_then_get_round_trips_and_is_addressed_by_key(tmp_path):
    store = ContentStore(tmp_path / "store")
    src = tmp_path / "artifact.bin"
    src.write_bytes(b"payload")
    key = "deadbeef" * 8
    stored = store.put(key, src)
    assert store.get(key) == stored
    assert stored.read_bytes() == b"payload"
    # Content-addressed: the slot path is a pure function of the key.
    assert stored == store._slot(key)


def test_content_store_get_misses_a_key_never_put(tmp_path):
    store = ContentStore(tmp_path / "store")
    assert store.get("never-put") is None


def test_parse_depfile_handles_line_continuations_and_escaped_spaces(tmp_path):
    depfile = tmp_path / "x.o.d"
    depfile.write_text("x.o: a.cc \\\n  b\\ header.h \\\n  c.h\n")
    assert parse_depfile(str(depfile)) == ["a.cc", "b header.h", "c.h"]


def test_parse_depfile_returns_empty_for_a_missing_file(tmp_path):
    assert parse_depfile(str(tmp_path / "nope.d")) == []


# --- KernelObjectArtifact.is_available_in_filesystem(), the actual migration -------


def test_a_freshly_built_artifact_is_available(tmp_path):
    artifact, *_rest, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()


def test_row_4_self_test_extra_flags_change_misses_and_is_not_served_stale(tmp_path):
    """The mutation self-test method-content-addressed-cache-key-discipline requires:
    (1) the content key changes, (2) the artifact misses (is not "available"), and
    (3) nothing here can silently ride the stale object -- KernelCompilationRule's
    caller sees is_available_in_filesystem() == False and must recompile."""
    artifact, source, header, old_key, toolchain = _built_artifact(
        tmp_path, extra_flags=["-DSCORES_ROWBATCH=1"]
    )
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()  # sanity: the fixture is self-consistent

        # (1) mutate an input that changes what THIS object should contain, the same
        # shape as SCORES_ROWBATCH going from 1 to 4 at one unchanged filename.
        artifact.extra_flags = ["-DSCORES_ROWBATCH=4"]
        new_flags = artifact._content_flags()
        new_key = content_key(parse_depfile(f"{artifact.filename}.d"), new_flags, toolchain)
        assert new_key != old_key, "content key did not change after the flag mutation"

        # (2) the artifact -- whose on-disk manifest still names the OLD key -- must
        # now report unavailable, because its recorded identity no longer matches.
        assert not artifact.is_available_in_filesystem(), (
            "a flag-only mutation was silently served the pre-mutation object"
        )

        # (3) the stale object's own bytes were never touched by this check --
        # confirms rejection is a pure predicate, not an accidental in-place mutation
        # that would itself hide the staleness.
        assert Path(artifact.filename).read_bytes() == b"<fake compiled bytes>"

    _ = source, header  # kept for readability; parse_depfile reads them by path only


def test_a_changed_header_the_depfile_names_also_misses(tmp_path):
    """Same discipline, the OTHER half of content_key's input set: a file the
    depfile names (not the primary source) changing must also miss -- this is
    the "forgot the include closure" bug class content_key is built to close."""
    artifact, source, header, old_key, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        header.write_text("// shared, but different now\n")
        assert not artifact.is_available_in_filesystem(), (
            "an edit to a header the depfile named was not detected"
        )


def test_a_missing_manifest_is_not_available(tmp_path):
    artifact, *_rest = _built_artifact(tmp_path)
    Path(f"{artifact.filename}.contentkey.json").unlink()
    assert not artifact.is_available_in_filesystem()


def test_a_missing_file_is_not_available_even_with_a_valid_manifest(tmp_path):
    artifact, *_rest = _built_artifact(tmp_path)
    Path(artifact.filename).unlink()
    assert not artifact.is_available_in_filesystem()


def test_a_toolchain_change_misses_even_with_unchanged_inputs_and_flags(tmp_path):
    artifact, *_rest, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain + "-rebuilt"):
        assert not artifact.is_available_in_filesystem()


# --- The real recording path, not just a hand-authored fixture --------------------


def test_record_cache_entry_writes_a_manifest_that_is_then_recognized_available(tmp_path):
    """Exercises KernelCompilationRule._record_cache_entry itself (the code that
    runs after a real compile), rather than a hand-authored manifest, to prove the
    fixture above matches what the real migration actually writes."""
    source = tmp_path / "kernel.cc"
    _write(source, "int g() { return 2; }\n")
    obj = tmp_path / "kernel.o"
    _write(obj, "<freshly compiled bytes>")
    _write(Path(f"{obj}.d"), f"{obj}: {source}\n")

    artifact = KernelObjectArtifact(
        filename=str(obj), dependencies=[SourceArtifact(str(source))]
    )
    test_store = ContentStore(tmp_path / "npu-cache")
    with _with_fixed_toolchain("toolchain-v1"), mock.patch(
        "iron.common.compilation.base._kernel_object_store", return_value=test_store
    ):
        assert not artifact.is_available_in_filesystem(), (
            "no manifest exists yet; a fresh compile must not already look available"
        )
        assert KernelCompilationRule._record_cache_entry(artifact) is True
        assert artifact.is_available_in_filesystem(), (
            "_record_cache_entry's own manifest was not recognized by "
            "is_available_in_filesystem() -- the two disagree about the schema"
        )

        # And the store side: a copy landed under the manifest's own key, content-
        # addressed, ready for a second filename with the same identity to reuse.
        manifest = json.loads(Path(f"{obj}.contentkey.json").read_text())
        stored = test_store.get(manifest["key"])
        assert stored is not None and stored.read_bytes() == obj.read_bytes()


# --- Non-vacuity: sabotage the key function and confirm the guard goes red --------


def test_sabotaging_content_key_to_a_constant_makes_the_mutation_guard_go_red(tmp_path):
    """Proves test_a_changed_header_the_depfile_names_also_misses above is not
    vacuous: a content_key that ignores its inputs must fail EXACTLY the assertion
    that test protects, the same way method-content-addressed-cache-key-discipline's
    2026-07-25 sabotage did for the npu-xrt self-test this mirrors.

    Deliberately reuses the HEADER-edit scenario, not a flags edit:
    is_available_in_filesystem() short-circuits on a bare flags-dict mismatch
    before ever calling content_key(), so sabotaging content_key would not touch
    that path at all -- proving nothing about content_key's own correctness. A
    header edit changes no flag; only content_key's file hashing can catch it.
    """
    artifact, source, header, old_key, toolchain = _built_artifact(tmp_path)
    with _with_fixed_toolchain(toolchain):
        assert artifact.is_available_in_filesystem()
        header.write_text("// shared, but different now\n")

        with mock.patch(
            "iron.common.compilation.base.content_key", return_value="constant-key"
        ):
            # Rewrite the manifest under the sabotaged (constant) key, exactly as
            # _record_cache_entry would with the sabotaged function active.
            manifest_path = Path(f"{artifact.filename}.contentkey.json")
            manifest = json.loads(manifest_path.read_text())
            manifest["key"] = "constant-key"
            manifest_path.write_text(json.dumps(manifest))

            # Under the sabotaged key function this INCORRECTLY reports available
            # after the header edit -- a broken key reads green. Assert that
            # failure explicitly, so an accidental future fix of the mock (or of
            # this test) cannot go unnoticed.
            assert artifact.is_available_in_filesystem(), (
                "sabotage did not reproduce the failure -- the guard may already "
                "be vacuous for a different reason, or this test no longer "
                "exercises it"
            )
    _ = source
