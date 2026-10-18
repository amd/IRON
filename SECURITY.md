<!--
SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
SPDX-License-Identifier: Apache-2.0
-->

# Security Policy

## Reporting a Vulnerability

If you believe you have found a security vulnerability in IRON, please report
it privately rather than opening a public issue.

Use GitHub's [private vulnerability reporting](https://github.com/amd/IRON/security/advisories/new).
This opens a private advisory visible only to the maintainers. We will
acknowledge reports as soon as we are able.

Please include, where possible:
- A description of the vulnerability and its potential impact.
- Steps to reproduce, or a minimal proof of concept.
- The commit hash or release tag the issue was observed against.
- Any suggested mitigation.

## Supported Versions

IRON tracks the tip of `devel`. Security fixes are applied there as soon as
feasible; prior releases are not patched in place.

## Scope

In scope: code in this repository, including its CI workflows, and how it
loads model weights and downloads files. Vulnerabilities in mlir-aie, Peano or
XRT belong to those projects.
