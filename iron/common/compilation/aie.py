# SPDX-FileCopyrightText: Copyright (C) 2025 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path
import os.path
import importlib.util
from contextlib import nullcontext
from aie.extras.context import mlir_mod_ctx
from .base import (
    CompilationArtifact,
    SourceArtifact,
    CompilationRule,
    ShellCompilationCommand,
    PythonCallbackCompilationCommand,
)

# AIE Artifacts
# ##########################################################################


class FullElfArtifact(CompilationArtifact):
    def __init__(self, filename, mlir_input, dependencies):
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.mlir_input = mlir_input


class XclbinArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        mlir_input,
        dependencies,
        kernel_name="MLIR_AIE",
        extra_flags=None,
        xclbin_input=None,
    ):
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.mlir_input = mlir_input
        self.kernel_name = kernel_name
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.xclbin_input = xclbin_input


class InstsBinArtifact(CompilationArtifact):
    def __init__(self, filename, mlir_input, dependencies, extra_flags=None):
        self.mlir_input = mlir_input
        if mlir_input not in dependencies:
            dependencies = dependencies + [mlir_input]
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []


class KernelObjectArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        dependencies,
        extra_flags=None,
        rename_symbols=None,
        prefix_symbols=None,
    ):
        super().__init__(filename, dependencies)
        self.extra_flags = extra_flags if extra_flags is not None else []
        self.rename_symbols = rename_symbols if rename_symbols is not None else {}
        self.prefix_symbols = prefix_symbols


class KernelArchiveArtifact(CompilationArtifact):
    pass


class PythonGeneratedMLIRArtifact(CompilationArtifact):
    def __init__(
        self,
        filename,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
        uses_kernel_archive=False,
        kernel_archive=None,
    ):
        self.import_path = import_path
        self.callback_fn = callback_fn
        self.callback_args = callback_args if callback_args is not None else []
        self.callback_kwargs = callback_kwargs if callback_kwargs is not None else {}
        self.requires_context = requires_context
        dependencies = [SourceArtifact(import_path)]
        super().__init__(filename, dependencies=dependencies)


# AIE Rules
# ##########################################################################


class GenerateMLIRFromPythonCompilationRule(CompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist(PythonGeneratedMLIRArtifact))

    def compile(self, graph):
        """Generate MLIR from a Python callback that uses the MLIR bindings"""
        commands = []
        worklist = graph.get_worklist(PythonGeneratedMLIRArtifact)
        for artifact in worklist:
            new_artifact = SourceArtifact(artifact.filename)
            # To make Python capture variables in this closure by value, not by reference, use default arguments
            callback = lambda new_artifact=new_artifact, import_path=artifact.import_path, callback_fn=artifact.callback_fn, callback_args=artifact.callback_args, callback_kwargs=artifact.callback_kwargs, requires_context=artifact.requires_context: self.generate_mlir(
                new_artifact,
                import_path,
                callback_fn,
                callback_args,
                callback_kwargs,
                requires_context,
            )
            commands.append(PythonCallbackCompilationCommand(callback))
            new_artifact.available = True
            graph.replace(artifact, new_artifact)
        return commands

    @staticmethod
    def generate_mlir(
        output_artifact,
        import_path,
        callback_fn,
        callback_args=None,
        callback_kwargs=None,
        requires_context=False,
    ):
        # Import the Python source file
        spec = importlib.util.spec_from_file_location(
            Path(import_path).name, import_path
        )
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        # We only initiate an MLIR context if requested; otherwise, it is expected that the callback creates the context
        ctx_callback = lambda: (mlir_mod_ctx() if requires_context else nullcontext())
        with ctx_callback() as ctx:
            callback_function = getattr(module, callback_fn)
            mlir_code = callback_function(*callback_args, **callback_kwargs)
        # Stringify the generated MLIR
        if requires_context:
            mlir_code = str(ctx.module)
        else:
            mlir_code = str(mlir_code)

        with open(output_artifact.filename, "w") as f:
            f.write(mlir_code)


class AieccCompilationRule(CompilationRule):
    def __init__(self, build_dir, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.build_dir = build_dir
        self.aiecc_path = Path(mlir_aie_dir) / "bin" / "aiecc.py"
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)


class AieccFullElfCompilationRule(AieccCompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist(FullElfArtifact))

    def compile(self, graph):
        worklist = graph.get_worklist(FullElfArtifact)
        commands = []

        for artifact in worklist:
            compile_cmd = [
                "python",
                str(self.aiecc_path),
                "--no-compile-host",
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
                "--dynamic-objFifos",
                "--expand-load-pdis",
                "--generate-full-elf",
                "--full-elf-name",
                os.path.abspath(artifact.filename),
                os.path.abspath(artifact.mlir_input.filename),
            ]
            commands.append(
                ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))
            )
            artifact.available = True

        return commands


class AieccXclbinInstsCompilationRule(AieccCompilationRule):
    def matches(self, graph):
        return any(graph.get_worklist((XclbinArtifact, InstsBinArtifact)))

    def compile(self, graph):
        # Group artifacts by their unique compilation configuration
        xclbin_configs = {}
        insts_configs = {}
        worklist = graph.get_worklist((XclbinArtifact, InstsBinArtifact))

        for artifact in worklist:
            mlir_dependency = artifact.mlir_input
            if isinstance(artifact, XclbinArtifact):
                key = (
                    mlir_dependency,
                    artifact.kernel_name,
                    tuple(artifact.extra_flags),
                    artifact.xclbin_input,
                )
                xclbin_configs.setdefault(key, []).append(artifact)
            elif isinstance(artifact, InstsBinArtifact):
                key = (mlir_dependency, tuple(artifact.extra_flags))
                insts_configs.setdefault(key, []).append(artifact)

        commands = []
        handled_insts_configs = set()

        # Iterate through XCLBIN configurations
        for xclbin_key, xclbin_artifacts in xclbin_configs.items():
            mlir_source, kernel_name, xclbin_flags, xclbin_input = xclbin_key

            # Try to find a matching InstsBin configuration (same MLIR source)
            matching_insts_key = None
            for insts_key in insts_configs:
                if (
                    insts_key not in handled_insts_configs
                    and insts_key[0] == mlir_source
                ):
                    matching_insts_key = insts_key
                    break

            compile_cmd = [
                "python",
                str(self.aiecc_path),
                "--no-compile-host",
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
                "--dynamic-objFifos",
            ]

            # Add XCLBIN flags
            first_xclbin = xclbin_artifacts[0]
            compile_cmd += list(xclbin_flags) + [
                "--aie-generate-xclbin",
                "--xclbin-name=" + os.path.abspath(first_xclbin.filename),
                "--xclbin-kernel-name=" + kernel_name,
            ]
            if xclbin_input is not None:
                compile_cmd += [
                    "--xclbin-input=" + os.path.abspath(xclbin_input.filename)
                ]

            # Add InstsBin flags if matching config found
            if matching_insts_key:
                handled_insts_configs.add(matching_insts_key)
                insts_artifacts = insts_configs[matching_insts_key]
                first_insts = insts_artifacts[0]
                compile_cmd += list(matching_insts_key[1]) + [
                    "--aie-generate-npu",
                    "--npu-insts-name=" + os.path.abspath(first_insts.filename),
                ]

            compile_cmd += [os.path.abspath(mlir_source.filename)]

            # If the MLIR source depends on a kernel archive, pass it to aiecc.py so it can be linked
            if (
                isinstance(mlir_source, PythonGeneratedMLIRArtifact)
                and "kernel_archive" in mlir_source.callback_kwargs
            ):
                compile_cmd.append(
                    os.path.abspath(
                        os.path.join(
                            self.build_dir,
                            mlir_source.callback_kwargs["kernel_archive"],
                        )
                    )
                )

            commands.append(
                ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))
            )

            # Copy for other XCLBIN artifacts with same config
            if len(xclbin_artifacts) > 1:
                for copy_dest in xclbin_artifacts[1:]:
                    commands.append(
                        ShellCompilationCommand(
                            ["cp", first_xclbin.filename, copy_dest.filename]
                        )
                    )

            # Copy for other InstsBin artifacts with same config (if matched)
            if matching_insts_key:
                insts_artifacts = insts_configs[matching_insts_key]
                if len(insts_artifacts) > 1:
                    first_insts = insts_artifacts[0]
                    for copy_dest in insts_artifacts[1:]:
                        commands.append(
                            ShellCompilationCommand(
                                ["cp", first_insts.filename, copy_dest.filename]
                            )
                        )

        # Handle remaining InstsBin configurations
        for insts_key, insts_artifacts in insts_configs.items():
            if insts_key in handled_insts_configs:
                continue

            mlir_source, insts_flags = insts_key
            first_insts = insts_artifacts[0]

            compile_cmd = [
                "python",
                str(self.aiecc_path),
                "--no-compile-host",
                "--no-xchesscc",
                "--no-xbridge",
                "--peano",
                str(self.peano_dir),
                "--dynamic-objFifos",
                "--no-compile",
            ]

            compile_cmd += list(insts_flags) + [
                "--aie-generate-npu",
                "--npu-insts-name=" + os.path.abspath(first_insts.filename),
            ]

            compile_cmd += [os.path.abspath(mlir_source.filename)]

            # If the MLIR source depends on a kernel archive, pass it to aiecc.py so it can be linked
            if (
                isinstance(mlir_source, PythonGeneratedMLIRArtifact)
                and "kernel_archive" in mlir_source.callback_kwargs
            ):
                compile_cmd.append(
                    os.path.abspath(
                        os.path.join(
                            self.build_dir,
                            mlir_source.callback_kwargs["kernel_archive"],
                        )
                    )
                )

            commands.append(
                ShellCompilationCommand(compile_cmd, cwd=str(self.build_dir))
            )

            # Copy for other InstsBin artifacts with same config
            if len(insts_artifacts) > 1:
                for copy_dest in insts_artifacts[1:]:
                    commands.append(
                        ShellCompilationCommand(
                            ["cp", first_insts.filename, copy_dest.filename]
                        )
                    )

        # Update graph
        for artifact in worklist:
            artifact.available = True

        return commands


class PeanoCompilationRule(CompilationRule):
    def __init__(self, peano_dir, mlir_aie_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        self.mlir_aie_dir = mlir_aie_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(artifacts.get_worklist(KernelObjectArtifact))

    def compile(self, artifacts):
        clang_path = Path(self.peano_dir) / "bin" / "clang++"
        include_path = Path(self.mlir_aie_dir) / "include"
        worklist = artifacts.get_worklist(KernelObjectArtifact)
        commands = []
        for artifact in worklist:
            if len(artifact.dependencies) != 1:
                raise RuntimeError(
                    "Expected exactly one dependency (the C source code) for KernelObjectArtifact"
                )
            source_file = artifact.dependencies[0]
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
                + ["-c", source_file.filename, "-o", artifact.filename]
            )

            commands.append(ShellCompilationCommand(cmd))
            if artifact.rename_symbols:
                commands.extend(self._rename_symbols(artifact))
            if artifact.prefix_symbols:
                commands.extend(self._prefix_symbols(artifact, artifact.prefix_symbols))
            artifact.available = True

        return commands

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
        cmd += [artifact.filename]
        return [ShellCompilationCommand(cmd)]

    def _prefix_symbols(self, artifact, prefix):
        objcopy_path = "llvm-objcopy-18"
        nm_path = "llvm-nm-18"
        symbol_map_file = artifact.filename + ".symbol_map"

        # Extract defined symbols and create symbol map
        nm_cmd = [
            "sh",
            "-c",
            f"{nm_path} --defined-only --extern-only {artifact.filename} | "
            f"awk '{{print $3 \" {prefix}\" $3}}' > {symbol_map_file}",
        ]

        # Apply the renaming using the symbol map
        objcopy_cmd = [
            objcopy_path,
            "--redefine-syms=" + symbol_map_file,
            artifact.filename,
        ]

        return [ShellCompilationCommand(nm_cmd), ShellCompilationCommand(objcopy_cmd)]


class ArchiveCompilationRule(CompilationRule):
    def __init__(self, peano_dir, *args, **kwargs):
        self.peano_dir = peano_dir
        super().__init__(*args, **kwargs)

    def matches(self, artifacts):
        return any(artifacts.get_worklist(KernelArchiveArtifact))

    def compile(self, artifacts):
        """Create an archive (.a) from compiled object files"""
        worklist = artifacts.get_worklist(KernelArchiveArtifact)
        commands = []
        for artifact in worklist:
            # Get archive filename from method
            archive_path = artifact.filename
            object_files = [
                dep.filename
                for dep in artifact.dependencies
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
            commands.append(ShellCompilationCommand(cmd))

            # Check for duplicate symbol definitions in the archive
            check_cmd = [
                "sh",
                "-c",
                f"nm {archive_path} | grep ' [TDR] ' | awk '{{print $3}}' | sort | uniq -d | "
                f'if read sym; then echo "Error: Duplicate symbol in archive: $sym" >&2; exit 1; fi',
            ]
            commands.append(ShellCompilationCommand(check_cmd))

            artifact.available = True

        return commands
