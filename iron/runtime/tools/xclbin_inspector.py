# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc.
# SPDX-License-Identifier: Apache-2.0

"""
FastFlowLM .xclbin Inspector

Tool for extracting kernel interfaces from FastFlowLM .xclbin files.
This is part of the Discovery Phase for IRON-Lemonade integration.

Usage:
    python xclbin_inspector.py <xclbin_file> [output.json]
"""

import struct
import json
from pathlib import Path
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict, field

# .xclbin binary format constants
XCLBIN_MAGIC = b"xclbin2\x00"  # 8 bytes
XCLBIN_HEADER_SIZE = 64


@dataclass
class KernelArgument:
    """Represents a single kernel argument"""

    name: str
    address_qualifier: int  # 0=value, 1=pointer to global, 2=pointer to constant
    size: int
    type_name: str
    offset: int
    port: int = 0
    arg_index: int = 0


@dataclass
class KernelInterface:
    """Represents a kernel's interface"""

    name: str
    language: str  # "C", "RTL", etc.
    arguments: List[KernelArgument] = field(default_factory=list)
    work_group_size: List[int] = field(default_factory=lambda: [1, 1, 1])
    compile_options: str = ""
    hw_control_protocols: List[str] = field(default_factory=list)
    memory_connections: List[str] = field(default_factory=list)


@dataclass
class XclbinInfo:
    """Complete .xclbin file information"""

    path: str
    file_size: int
    kernels: List[KernelInterface] = field(default_factory=list)
    sections: Dict[str, int] = field(default_factory=dict)  # section_name -> size
    uuid: str = ""
    version: int = 0
    platform_indicators: List[str] = field(default_factory=list)


class XclbinInspector:
    """Parses .xclbin files and extracts kernel information"""

    def __init__(self, xclbin_path: str):
        self.path = Path(xclbin_path)
        if not self.path.exists():
            raise FileNotFoundError(f".xclbin file not found: {self.path}")
        self.data = self.path.read_bytes()
        self.info = XclbinInfo(
            path=str(self.path),
            file_size=len(self.data),
            kernels=[],
            sections={},
            uuid="",
            version=0,
            platform_indicators=[],
        )

    def parse(self) -> XclbinInfo:
        """Parse .xclbin and extract all information"""
        # Verify magic number
        if len(self.data) < 64:
            raise ValueError(
                f"File too small to be valid .xclbin: {len(self.data)} bytes"
            )

        if self.data[:8] != XCLBIN_MAGIC:
            raise ValueError(
                f"Invalid .xclbin magic number: {self.data[:8]}. "
                f"Expected {XCLBIN_MAGIC}"
            )

        # Parse header
        header = self._parse_header()
        self.info.uuid = header["uuid"]
        self.info.version = header["version"]

        # Find and parse sections
        sections = self._find_sections()
        self.info.sections = {s["name"]: s["size"] for s in sections}

        # Parse XML metadata for kernel information
        self._parse_xml_metadata()

        # Detect platform indicators
        self._detect_platform_indicators()

        return self.info

    def _parse_header(self) -> dict:
        """Parse xclbin header (64 bytes)"""
        # struct xclbin2_header:
        # [0:8]   Magic number "xclbin2\x00"
        # [8:24]  UUID (16 bytes)
        # [24:32] Version
        # [32:40] Number of sections
        # [40:48] Header length
        # [48:56] Reserved
        # [56:64] Checksum

        uuid_bytes = self.data[8:24]
        uuid = uuid_bytes.hex()

        version = struct.unpack("<Q", self.data[24:32])[0]
        num_sections = struct.unpack("<Q", self.data[32:40])[0]
        header_len = struct.unpack("<Q", self.data[40:48])[0]
        checksum = struct.unpack("<Q", self.data[48:56])[0]

        return {
            "uuid": uuid,
            "version": version,
            "num_sections": num_sections,
            "header_len": header_len,
            "checksum": checksum,
        }

    def _find_sections(self) -> List[dict]:
        """Find all sections in the file"""
        sections = []
        offset = 64  # After main header

        # Section header structure (approximately 92 bytes)
        # struct xclbin2_section_header:
        # [0:4]   sectionType
        # [4:8]   reserved
        # [8:16]  sectionOffset
        # [16:24] sectionSize
        # [24:28] sectionKind
        # [28:92] sectionName (64 bytes)

        iteration = 0
        while offset + 92 <= len(self.data) and iteration < 100:
            try:
                section_type = struct.unpack("<I", self.data[offset : offset + 4])[0]
                section_offset = struct.unpack(
                    "<Q", self.data[offset + 8 : offset + 16]
                )[0]
                section_size = struct.unpack(
                    "<Q", self.data[offset + 16 : offset + 24]
                )[0]
                section_kind = struct.unpack(
                    "<I", self.data[offset + 24 : offset + 28]
                )[0]

                try:
                    section_name = (
                        self.data[offset + 28 : offset + 92]
                        .rstrip(b"\x00")
                        .decode("ascii")
                    )
                except UnicodeDecodeError:
                    section_name = f"SECTION_{section_kind}"

                if (
                    section_size == 0
                    or section_offset == 0
                    or section_offset >= len(self.data)
                ):
                    break

                sections.append(
                    {
                        "name": section_name or f"UNKNOWN_{section_kind}",
                        "type": section_type,
                        "offset": section_offset,
                        "size": section_size,
                        "kind": section_kind,
                    }
                )

                offset += 92
                iteration += 1
            except struct.error:
                break

        return sections

    def _parse_xml_metadata(self):
        """Parse embedded XML metadata to extract kernel information"""
        # Search for XML start
        xml_start = self.data.find(b"<?xml")
        if xml_start == -1:
            # Try alternative XML markers
            xml_start = self.data.find(b"<xcl:root")
            if xml_start == -1:
                self.info.platform_indicators.append("No XML metadata found")
                return

        # Find XML end
        xml_end_marker = b"</xcl:root>"
        xml_end = self.data.find(xml_end_marker, xml_start)
        if xml_end == -1:
            return
        xml_end += len(xml_end_marker)

        xml_data = self.data[xml_start:xml_end].decode("utf-8", errors="ignore")

        # Parse XML
        try:
            import xml.etree.ElementTree as ET

            root = ET.fromstring(xml_data)

            # Handle namespaces
            namespaces = {}
            if "xcl" in xml_data:
                namespaces["xcl"] = "http://www.xilinx.com"
            if "api" in xml_data:
                namespaces["api"] = "http://www.xilinx.com/api"

            # Use namespace-aware or namespace-agnostic search
            def find_all(elem, tag):
                # Try with namespace
                result = elem.findall(f".//xcl:{tag}", namespaces)
                if not result:
                    # Try without namespace
                    result = elem.findall(f".//{tag}")
                if not result:
                    # Try wildcard namespace
                    result = elem.findall(f".//{{*}}{tag}")
                return result

            # Find kernel entries
            kernel_elems = find_all(root, "kernel")

            for kernel_elem in kernel_elems:
                kernel_info = self._parse_kernel_xml(kernel_elem, find_all)
                if kernel_info:
                    self.info.kernels.append(kernel_info)

        except ET.ParseError as e:
            self.info.platform_indicators.append(f"XML parse error: {str(e)}")
        except Exception as e:
            self.info.platform_indicators.append(f"XML processing error: {str(e)}")

    def _parse_kernel_xml(self, kernel_elem, find_all) -> Optional[KernelInterface]:
        """Parse kernel XML element"""

        def get_attr(elem, attr, default=""):
            """Get attribute with namespace handling"""
            val = elem.get(attr)
            if val is None:
                # Try with namespace prefix variations
                for prefix in ["xcl:", "api:", ""]:
                    val = elem.get(f"{prefix}{attr}")
                    if val is not None:
                        break
            return val if val else default

        name = get_attr(kernel_elem, "name", "unknown")
        if name == "unknown":
            return None  # Skip unnamed kernels

        language = get_attr(kernel_elem, "language", "C")
        compile_options = get_attr(kernel_elem, "compileOptions", "")

        arguments = []
        arg_elems = find_all(kernel_elem, "arg")

        for i, arg_elem in enumerate(arg_elems):
            arg_name = get_attr(arg_elem, "name", f"arg_{i}")
            addr_qual = get_attr(arg_elem, "addressQualifier", "0")
            size = get_attr(arg_elem, "size", "0")
            arg_type = get_attr(arg_elem, "type", "unknown")
            offset = get_attr(arg_elem, "offset", "0")
            port = get_attr(arg_elem, "port", "0")
            arg_index = get_attr(arg_elem, "index", str(i))

            try:
                arg_info = KernelArgument(
                    name=arg_name,
                    address_qualifier=int(addr_qual),
                    size=int(size),
                    type_name=arg_type,
                    offset=int(offset),
                    port=int(port),
                    arg_index=int(arg_index),
                )
                arguments.append(arg_info)
            except ValueError:
                continue

        # Work group size
        work_group_size = [1, 1, 1]
        wg_elems = find_all(kernel_elem, "workGroupSize")
        if wg_elems:
            wg_elem = wg_elems[0]
            for i, dim in enumerate(["dim1", "dim2", "dim3"]):
                val = get_attr(wg_elem, dim)
                if val:
                    try:
                        work_group_size[i] = int(val)
                    except ValueError:
                        pass

        # Hardware control protocols
        hw_protocols = []
        proto_elems = find_all(kernel_elem, "hwControlProtocol")
        for proto_elem in proto_elems:
            protocol = get_attr(proto_elem, "protocol")
            if protocol:
                hw_protocols.append(protocol)

        # Memory connections
        memory_connections = []
        conn_elems = find_all(kernel_elem, "memoryConnection")
        for conn_elem in conn_elems:
            memory = get_attr(conn_elem, "memory")
            if memory:
                memory_connections.append(memory)

        return KernelInterface(
            name=name,
            language=language,
            arguments=arguments,
            work_group_size=work_group_size,
            compile_options=compile_options,
            hw_control_protocols=hw_protocols,
            memory_connections=memory_connections,
        )

    def _detect_platform_indicators(self) -> List[str]:
        """Detect platform-specific indicators in the .xclbin"""
        indicators = []

        # Check for Windows-specific strings
        if b"\\" in self.data[:2000]:
            indicators.append("Windows path separators detected")

        # Check for Linux-specific strings
        if b"/opt/" in self.data or b"/usr/" in self.data or b"/home/" in self.data:
            indicators.append("Linux path references found")

        # Check for xrt references
        if b"xrt" in self.data.lower():
            indicators.append("XRT references detected")

        # Check for xdna references
        if b"xdna" in self.data.lower():
            indicators.append("xDNA references detected")

        # Check for aie references
        if b"aie" in self.data.lower():
            indicators.append("AIE (AI Engine) references detected")

        # Check for target device
        if b"npu" in self.data.lower():
            indicators.append("NPU target detected")
        if b"ryzen" in self.data.lower():
            indicators.append("Ryzen AI target detected")

        self.info.platform_indicators.extend(indicators)
        return indicators

    def export_json(self, output_path: str):
        """Export parsed information as JSON"""
        with open(output_path, "w") as f:
            json.dump(asdict(self.info), f, indent=2, default=str)


def format_argument(arg: KernelArgument) -> str:
    """Format kernel argument for display"""
    ptr = "*" if arg.address_qualifier == 1 else ""
    const = "const " if arg.address_qualifier == 2 else ""
    return f"{const}{arg.type_name}{ptr} {arg.name}"


def main():
    import sys

    if len(sys.argv) < 2:
        print("FastFlowLM .xclbin Inspector")
        print("=" * 40)
        print("\nUsage: python xclbin_inspector.py <xclbin_file> [output.json]")
        print("\nExtracts kernel interface information from .xclbin files.")
        sys.exit(1)

    xclbin_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    try:
        inspector = XclbinInspector(xclbin_path)
        info = inspector.parse()

        print(f"\n{'=' * 60}")
        print(f"=== .xclbin Kernel Inspector Report")
        print(f"{'=' * 60}")
        print(f"\nFile: {info.path}")
        print(f"Size: {info.file_size:,} bytes ({info.file_size / 1024 / 1024:.2f} MB)")
        print(f"UUID: {info.uuid}")
        print(f"Version: {info.version}")

        print(f"\n--- Sections ({len(info.sections)}) ---")
        for name, size in info.sections.items():
            size_str = (
                f"{size:,} bytes"
                if size < 1024 * 1024
                else f"{size / 1024 / 1024:.2f} MB"
            )
            print(f"  {name}: {size_str}")

        print(f"\n--- Platform Indicators ---")
        for indicator in info.platform_indicators:
            print(f"  - {indicator}")

        print(f"\n--- Kernels ({len(info.kernels)}) ---")
        for i, kernel in enumerate(info.kernels):
            print(f"\n  [{i}] Kernel: {kernel.name}")
            print(f"      Language: {kernel.language}")
            print(f"      Work group size: {kernel.work_group_size}")
            if kernel.compile_options:
                print(f"      Compile options: {kernel.compile_options}")

            if kernel.arguments:
                print(f"      Arguments ({len(kernel.arguments)}):")
                for arg in kernel.arguments:
                    arg_str = format_argument(arg)
                    print(f"        [{arg.arg_index}] {arg_str}")
                    print(
                        f"            offset={arg.offset}, size={arg.size}, addr_qual={arg.address_qual}"
                    )

            if kernel.hw_control_protocols:
                print(f"      HW protocols: {', '.join(kernel.hw_control_protocols)}")
            if kernel.memory_connections:
                print(
                    f"      Memory connections: {', '.join(kernel.memory_connections)}"
                )

        if not info.kernels:
            print("\n  No kernels found in .xclbin file.")
            print("  This may indicate:")
            print("    - File is not a valid .xclbin")
            print("    - Kernel metadata is in non-standard format")
            print("    - XML metadata section is missing or corrupted")

        if output_path:
            inspector.export_json(output_path)
            print(f"\n{'=' * 60}")
            print(f"Exported to: {output_path}")

        print(f"\n{'=' * 60}")

    except FileNotFoundError as e:
        print(f"Error: {e}")
        sys.exit(1)
    except ValueError as e:
        print(f"Error parsing .xclbin: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback

        traceback.print_exc()
        sys.exit(1)


if __name__ == "__main__":
    main()
