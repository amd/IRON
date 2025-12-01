# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""
This file implements a simple Python-based build system. You specify what you
want to compile (*artifacts*) through subclasses of `CompilationArtifact`.
Each artifact can have a list of depenencies of other artifacts that it relies
on. Each artifact corresponds to exactly one file. If a file with a matching
name already exists, and all its dependencies are built and older than the file,
then the existing file will be reused.

For each file name, artifacts are singletons. You create artifacts by calling
the `new` class method of the appropriate class. This ensures that artifact
objects are uniqued, i.e., calling `new` twice with the same file name will
return the same object.

There is a special artifact for source files that do not need to get generated,
`SourceArtifact`. It is likely that in your compilation dependency graph,
the leaf nodes will be `SourceArtifact`s.

You specify how to generate (compile) an artifact through *rules*, which are
expressed as subclasses of `CompilationRule`. This class requires you to
implement two methods: `matches` and `compile`. During compilation, we will
call `matches` on the set of remaining artifacts to see if the given rule is
able to produce any of the artifacts not available yet. If this function
returns `True`, we will call `compile` on the rule to generate the artifact.
`compile` returns a new list of artifacts, which may be the same one as
before; however, if `matches()==True`, at least one of the artifacts in the
list must be made available after calling `compile()`.
"""

from abc import ABC, abstractmethod
from pathlib import Path
import os.path
import zlib
import logging
import subprocess
import importlib.util
from contextlib import nullcontext
from aie.extras.context import mlir_mod_ctx


# Compilation Artifacts
# --------------------------------------------------------------------------


class CompilationArtifact(ABC):
    _instances = {}

    @classmethod
    def new(cls, path, *args, **kwargs):
        """Uniques artifacts based on absolute file path; any two artifacts with the same absolute path will be represented by the same object."""
        path = Path(path)
        abs_path = path.absolute()
        if abs_path not in cls._instances:
            cls._instances[abs_path] = None
            instance = cls(path, *args, **kwargs)
            cls._instances[abs_path] = instance
        else:
            assert (
                type(cls._instances[abs_path]) == cls
            ), f"Artifact with path {abs_path} is already registered with a different type"
        return cls._instances[abs_path]

    def __init__(self, path, depends=None):
        abs_path = path.absolute()
        assert (
            abs_path in self._instances
        ), "do not construct artifact objects directly; call the get() class method instead for uniquing"
        self.path: Path = path
        self.depends: list[CompilationArtifact] = depends if depends is not None else []
        self.users: list[CompilationArtifact] = (
            []
        )  # List of ancestor artifacts that depend on this artifact
        for dependency in self.depends:
            dependency.users.append(self)

    def __repr__(self):
        return f"{self.__class__.__name__}(path={self.path}, depends={self.depends})"

    def set_path(self, new_path):
        old_abs_path = self.path.absolute()
        new_path = Path(new_path)
        abs_path = new_path.absolute()
        self.path = new_path
        del CompilationArtifact._instances[old_abs_path]
        CompilationArtifact._instances[abs_path] = self

    def is_available(self):
        if not self.path.exists():
            return False
        for dependency in self.depends:
            # If any of our dependencies' dependencies are outdated, this artifact is also outdated
            if not dependency.is_available():
                return False
            # If any of our direct dependencies are newer than this artifact, this artifact is invalid
            if dependency.is_newer_than(os.path.getmtime(str(self.path))):
                return False
        return True

    def is_newer_than(self, time):
        return os.path.getmtime(str(self.path)) > time

    def delete(self):
        for user in self.users:
            user.depends.remove(self)
        del self._instances[self.path.absolute()]
        return self.users


class SourceArtifact(CompilationArtifact):
    pass


class XclbinArtifact(CompilationArtifact):
    def __init__(
        self, path, depends, kernel_name="MLIR_AIE", extra_flags=None, xclbin_input=None
    ):
        super().__init__(path, depends)
        self.kernel_name = kernel_name
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.xclbin_input = xclbin_input


class InstsBinArtifact(CompilationArtifact):
    def __init__(self, path, depends, extra_flags=None):
        super().__init__(path, depends)
        self.extra_flags = extra_flags if extra_flags is not None else []


class KernelObjectArtifact(CompilationArtifact):
    def __init__(self, path, depends, extra_flags=None, rename_symbols=None):
        super().__init__(path, depends)
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.rename_symbols = rename_symbols if rename_symbols is not None else {}


class KernelArchiveArtifact(CompilationArtifact):
    pass


class PythonGeneratedMLIRArtifact(CompilationArtifact):
    def __init__(
        self,
        path,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
    ):
        self.import_path = import_path
        self.callback_fn = callback_fn
        self.callback_args = callback_args if callback_args is not None else []
        self.callback_kwargs = callback_kwargs if callback_kwargs is not None else {}
        self.requires_context = requires_context
        super().__init__(path)

    def is_available(self):
        is_available = super().is_available()
        if is_available:
            # Force regeneration if the Python source is changed
            return os.path.getmtime(str(self.path)) >= os.path.getmtime(
                self.import_path
            )
        return is_available


# Compilation Rules
# --------------------------------------------------------------------------


class CompilationRule(ABC):
    @abstractmethod
    def matches(self, artifact: list[CompilationArtifact]) -> bool:
        pass

    @abstractmethod
    def compile(
        self, artifacts: list[CompilationArtifact]
    ) -> list[CompilationArtifact]:
        pass


class GenerateMLIRFromPythonCompilationRule(CompilationRule):
    def matches(self, artifacts):
        return any(
            isinstance(artifact, PythonGeneratedMLIRArtifact)
            and len(artifact.depends) == 0
            for artifact in artifacts
        )

    def compile(self, artifacts):
        """Generate MLIR from a Python callback that uses the MLIR bindings"""
        for i, artifact in enumerate(artifacts):
            if not isinstance(artifact, PythonGeneratedMLIRArtifact):
                continue
            if not all(dependency.is_available() for dependency in artifact.depends):
                continue

            # Import the Python source file
            spec = importlib.util.spec_from_file_location(
                Path(artifact.import_path).name, artifact.import_path
            )
            module = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(module)
            # We only initiate an MLIR context if requested; otherwise, it is expected that the callback creates the context
            ctx_callback = lambda: (
                mlir_mod_ctx() if artifact.requires_context else nullcontext()
            )
            with ctx_callback() as ctx:
                callback_function = getattr(module, artifact.callback_fn)
                mlir_code = callback_function(
                    *artifact.callback_args, **artifact.callback_kwargs
                )
                # Stringify the generated MLIR
                if artifact.requires_context:
                    mlir_code = str(ctx.module)
                else:
                    mlir_code = str(mlir_code)

            with open(artifact.path, "w") as f:
                f.write(mlir_code)

            # Now that the artifact is generated, replace this artifact with the MLIR source code file
            old_users = artifact.delete()
            new_artifact = SourceArtifact.new(artifact.path)
            for user in old_users:
                user.depends.append(new_artifact)
            artifacts[i] = new_artifact
            logging.debug(f"Created MLIR source string for {artifact.path.name}")

        return artifacts



class AieccCompilationRule(CompilationRule):
    def __init__(self, build_dir, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.build_dir = build_dir
        self.aiecc_path = Path(mlir_aie_dir) / "bin" / "aiecc.py"
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(
            isinstance(artifact, (XclbinArtifact, InstsBinArtifact))
            and all(dependency.is_available() for dependency in artifact.depends)
            for artifact in artifacts
        )

    def compile(self, artifacts):
        # If there are both xclbin and insts.bin targets based on the same source MLIR code, we can combine them into one single `aiecc.py` invocation.
        mlir_sources = set()
        mlir_sources_to_xclbins = {}
        mlir_sources_to_insts_bins = {}
        for artifact in artifacts:
            if not isinstance(artifact, (XclbinArtifact, InstsBinArtifact)):
                continue
            if not all(dependency.is_available() for dependency in artifact.depends):
                continue
            mlir_dependencies = [
                d
                for d in artifact.depends
                if isinstance(d, (SourceArtifact, PythonGeneratedMLIRArtifact))
            ]
            if len(mlir_dependencies) != 1:
                raise RuntimeError(
                    f"Expected exactly one dependency of {artifact.path} to be SourceArtifact or PythonGeneratedMLIRArtifact, got: {', '.join(str(dep.path) for dep in artifact.depends)}"
                )
            mlir_dependency = mlir_dependencies[0]
            mlir_sources.add(mlir_dependency)
            if isinstance(artifact, XclbinArtifact):
                mlir_sources_to_xclbins.setdefault(mlir_dependency, []).append(artifact)
            elif isinstance(artifact, InstsBinArtifact):
                mlir_sources_to_insts_bins.setdefault(mlir_dependency, []).append(
                    artifact
                )

        # Now we know for each mlir source if we need to generate an xclbin, an insts.bin or both for it
        for mlir_source in mlir_sources:
            # Build aiecc command using Peano
            compile_cmd = [
                "python",
                str(self.aiecc_path),
                "--no-compile-host",
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
            ]
            do_compile_xclbin = mlir_source in mlir_sources_to_xclbins
            do_compile_insts_bin = mlir_source in mlir_sources_to_insts_bins
            if do_compile_xclbin:
                first_xclbin = mlir_sources_to_xclbins[mlir_source][
                    0
                ]  # FIXME: this does not handle the case of multiple xclbins with different kernel names or flags from the same MLIR
                compile_cmd += first_xclbin.extra_flags + [
                    "--aie-generate-xclbin",
                    "--xclbin-name=" + str(first_xclbin.path),
                    "--xclbin-kernel-name=" + first_xclbin.kernel_name,
                ]
                if first_xclbin.xclbin_input is not None:
                    compile_cmd += [
                        "--xclbin-input=" + str(first_xclbin.xclbin_input.path)
                    ]
            if do_compile_insts_bin:
                first_insts_bin = mlir_sources_to_insts_bins[mlir_source][
                    0
                ]  # FIXME: this does not handle the case of multiple insts.bins with different flags from the same MLIR
                if not do_compile_xclbin:
                    compile_cmd += ["--no-compile"]
                compile_cmd += first_insts_bin.extra_flags + [
                    "--aie-generate-npu",
                    "--npu-insts-name=" + str(first_insts_bin.path),
                ]
            compile_cmd += [str(mlir_source.path)]

            env = os.environ.copy()
            logging.debug(f"Compiling MLIR with command: {' '.join(compile_cmd)}")
            result = subprocess.run(
                compile_cmd,
                cwd=str(self.build_dir),
                capture_output=True,
                text=True,
                timeout=300,
                env=env,
            )
            if result.returncode == 0:
                logging.debug(
                    f"Successfully compiled {mlir_source.path} to {', '.join([str(first_xclbin.path)] if do_compile_xclbin else [] + [str(first_insts_bin.path)] if do_compile_insts_bin else [])}"
                )
            else:
                raise RuntimeError(
                    f"MLIR compilation for {mlir_source.path} failed: {result.stderr}"
                )

            # There may be multiple targets that require an xclbin/insts.bin from the same MLIR with different names; copy them
            for sources_to in [mlir_sources_to_xclbins, mlir_sources_to_insts_bins]:
                if sources_to.get(mlir_source, [])[1:]:
                    copy_src = sources_to[mlir_source][0]
                    for copy_dest in sources_to[mlir_source][1:]:
                        shutil.copy(copy_src.path, copy_dest.path)

        # With the newly generated files, is_available() should now return True on the Xclbin and InstsBin targets
        return artifacts


class PeanoCompilationRule(CompilationRule):
    def __init__(self, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(
            isinstance(artifact, KernelObjectArtifact)
            and all(
                isinstance(dependency, SourceArtifact) and dependency.is_available()
                for dependency in artifact.depends
            )
            for artifact in artifacts
        )

    def compile(self, artifacts):
        clang_path = Path(self.peano_dir) / "bin" / "clang++"
        include_path = Path(self.mlir_aie_dir) / "include"

        for artifact in artifacts:
            if not isinstance(artifact, KernelObjectArtifact):
                continue

            if len(artifact.depends) != 1:
                raise RuntimeError(
                    "Expected exactly one dependency (the C source code) for KernelObjectArtifact"
                )
            source_file = artifact.depends[0]
            if not isinstance(source_file, SourceArtifact):
                raise RuntimeError(
                    "Expected KernelObject dependency to be a C source file"
                )

            cmd = (
                [
                    str(clang_path),
                    "-O2",
                    "-std=c++20",
                    "--target=aie2p-none-unknown-elf",
                    "-Wno-parentheses",
                    "-Wno-attributes",
                    "-Wno-macro-redefined",
                    "-Wno-empty-body",
                    "-Wno-missing-template-arg-list-after-template-kw",
                    f"-I{str(include_path)}",
                ]
                + artifact.extra_flags
                + ["-c", str(source_file.path), "-o", str(artifact.path)]
            )
            logging.debug(f"Running compilation command: {' '.join(cmd)}")
            result = subprocess.run(cmd, capture_output=True, text=True)
            if result.returncode != 0:
                raise RuntimeError(f"Compilation failed: {result.stderr}")
            logging.debug(f"Successfully compiled: {artifact.path.name}")

            if artifact.rename_symbols:
                self._rename_symbols(artifact)

        return artifacts

    def _rename_symbols(self, artifact):
        objcopy_path = "llvm-objcopy-18"
        cmd = [
            objcopy_path,
        ]
        for old_sym, new_sym in artifact.rename_symbols.items():
            cmd += [
                "--redefine-sym",
                f"{old_sym}={new_sym}",
            ]
        cmd += [str(artifact.path)]

        logging.debug(f"Running renaming command: {' '.join(cmd)}")
        result = subprocess.run(cmd, capture_output=True, text=True)

        if result.returncode == 0:
            logging.debug(f"Successfully renamed symbols in: {artifact.path.name}")
        else:
            raise RuntimeError(f"Symbol renaming failed: {result.stderr}")


class ArchiveCompilationRule(CompilationRule):
    def __init__(self, peano_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(
            isinstance(artifact, KernelArchiveArtifact) and len(artifact.depends) > 0
            for artifact in artifacts
        )

    def compile(self, artifacts):
        """Create an archive (.a) from compiled object files"""
        for artifact in artifacts:
            if not isinstance(artifact, KernelArchiveArtifact):
                continue

            # Get archive filename from method
            archive_path = str(artifact.path)
            object_files = [
                str(dep.path)
                for dep in artifact.depends
                if isinstance(dep, KernelObjectArtifact)
            ]

            # Try to find ar tool from PEANO, then system
            ar_path = None

            if self.peano_dir:
                # Peano has llvm-ar for archiving
                peano_ar = Path(self.peano_dir) / "bin" / "llvm-ar"
                if os.path.exists(peano_ar):
                    ar_path = peano_ar

            if ar_path is None:
                raise RuntimeError(
                    "Could not find 'ar' tool in PEANO installation or system PATH"
                )

            cmd = [str(ar_path), "rcs", archive_path] + object_files

            result = subprocess.run(cmd, capture_output=True, text=True)

            if result.returncode == 0:
                logging.debug(
                    f"Successfully created archive: {Path(archive_path).name}"
                )
            else:
                raise RuntimeError(f"Archive creation failed: {result.stderr}")

        return artifacts


# Global Functions
# --------------------------------------------------------------------------


def apply_rules(rules, artifacts):
    for rule in rules:
        if rule.matches(artifacts):
            logging.debug(f"Applying rule: {rule.__class__.__name__}")
            artifacts = rule.compile(artifacts)
            break
    else:
        # None of the rules matched
        return False, artifacts

    return True, artifacts


def compile(rules, artifacts):
    # While some artifacts remain to be compiled (not all are available)
    while not all(artifact.is_available() for artifact in artifacts):
        remaining = [artifact for artifact in artifacts if not artifact.is_available()]
        success, artifacts = apply_rules(rules, remaining)
        if not success:
            raise RuntimeError(
                f"No matching rule to compile target(s): {', '.join(str(artifact.path.name) for artifact in artifacts if not artifact.is_available())}"
            )
    return artifacts


def get_work_list(artifacts):
    """
    Return a flattened artifact creation worklist in reverse topological order from dependencies.
    The returned list will start with leaf nodes (artifacts with no dependencies), and any following artifacts will only contain artifacts from earlier in the list.
    """
    work_list = []
    todo = list(artifacts)
    visited = set()

    def dfs_visit(artifact):
        if artifact in visited:
            # Thanks to uniquing of artifact objects, this avoids duplicate creation of the same artifacts
            return
        visited.add(artifact)
        # First visit all dependencies, so put leaves first (post-order) ...
        for dep in artifact.depends:
            dfs_visit(dep)
        #  ... then put parent
        if not artifact.is_available():
            work_list.append(artifact)

    for artifact in todo:
        dfs_visit(artifact)

    return work_list
