# conditional_nav.py -*- Python -*-
#
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""MkDocs hook: drop the Programming Guide nav section when it isn't present.

``docs/programming_guide`` is a symlink to the repo-root ``programming_guide/``
tree, created at build time (see .github/workflows/publish-pages.yml), not
committed: that tree doesn't exist on every branch yet. A strict build would
otherwise fail on a nav entry pointing at a missing page, so drop the section
here instead of hand-editing mkdocs.yml per branch.
"""

import os
import re

_HAS_GUIDE = "_has_programming_guide"

# The landing page links to the guide from its quick-nav cards; matches the
# single <a class="iron-card" href="programming_guide/" ...>...</a> block.
_GUIDE_CARD_RE = re.compile(
    r'<a class="iron-card" href="programming_guide/".*?</a>\n*', re.S
)


def on_config(config):
    guide_dir = os.path.join(config["docs_dir"], "programming_guide")
    has_guide = os.path.isdir(guide_dir)
    config[_HAS_GUIDE] = has_guide
    if has_guide:
        return config

    config["nav"] = [
        item
        for item in config["nav"]
        if not (isinstance(item, dict) and "Programming Guide" in item)
    ]
    return config


def on_page_markdown(markdown, page, config, files):
    if config.get(_HAS_GUIDE) or page.file.src_path != "index.md":
        return markdown
    return _GUIDE_CARD_RE.sub("", markdown)
