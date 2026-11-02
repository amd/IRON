# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""MkDocs hook: drop a page's leading SPDX comment, so MkDocs titles it by its H1."""

import re

_SPDX_RE = re.compile(
    r"\A\s*<!--(?:(?!-->).)*SPDX-License-Identifier(?:(?!-->).)*-->\s*", re.S
)


def on_page_markdown(markdown, page, config, files):
    """Strip the licence comment that precedes a page's first heading."""
    return _SPDX_RE.sub("", markdown, count=1)
