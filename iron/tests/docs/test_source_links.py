# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0

"""Regression checks for the site's source-link hook."""

import importlib.util
from pathlib import Path
from types import SimpleNamespace

import pytest

pytest.importorskip("mkdocs")
from mkdocs.structure.files import File, Files

ROOT = Path(__file__).resolve().parents[3]


@pytest.fixture
def hook():
    spec = importlib.util.spec_from_file_location(
        "rewrite_source_links", ROOT / "docs/hooks/rewrite_source_links.py"
    )
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


@pytest.mark.parametrize("directory_urls", [True, False])
@pytest.mark.parametrize("quote", ['"', "'"])
def test_html_image_uses_site_asset(hook, directory_urls, quote, tmp_path):
    docs_path = tmp_path / "docs"
    image_path = docs_path / "assets" / "images" / "XDNA2.png"
    image_path.parent.mkdir(parents=True)
    image_path.write_bytes(b"real image")
    source_path = docs_path / "agents.md"
    source_path.write_text("real documentation", encoding="utf-8")
    docs = str(docs_path)
    image = File("assets/images/XDNA2.png", docs, "/tmp/site", directory_urls)
    source = File("agents.md", docs, "/tmp/site", directory_urls)
    page = SimpleNamespace(file=source, url=source.url)
    markdown = (
        f'<img alt="IRON Logo" src={quote}./assets/images/XDNA2.png?raw=1#logo{quote}>'
    )

    rendered = hook.on_page_markdown(
        markdown, page, {"docs_dir": docs}, Files([source, image])
    )

    prefix = "../" if directory_urls else ""
    assert rendered == (
        f'<img alt="IRON Logo" src={quote}'
        f"{prefix}assets/images/XDNA2.png?raw=1#logo{quote}>"
    )


@pytest.mark.parametrize(
    "target",
    ["https://example.com/logo.png", "//example.com/logo.png", "/logo.png", "none.png"],
)
def test_unmapped_html_image_is_unchanged(hook, target):
    docs = str(ROOT / "docs")
    source = File("agents.md", docs, "/tmp/site", True)
    page = SimpleNamespace(file=source, url=source.url)
    markdown = f'<img src="{target}">'

    assert (
        hook.on_page_markdown(markdown, page, {"docs_dir": docs}, Files([source]))
        == markdown
    )
