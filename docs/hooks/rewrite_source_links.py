# rewrite_source_links.py -*- Python -*-
#
# SPDX-FileCopyrightText: Copyright (C) 2026 Advanced Micro Devices, Inc. All rights reserved.
# SPDX-License-Identifier: Apache-2.0
#
"""MkDocs hook: rewrite relative links that point at repo source into GitHub URLs.

Several doc pages are symlinks to files that live elsewhere in the repo
(``docs/installation.md`` -> ``../README.md``, ``docs/programming_guide`` ->
``../programming_guide``, ...), so their relative links -
``[AGENTS.md](AGENTS.md#environment)``, ``[model.py](model.py)`` - stay correct
when the same file is browsed on GitHub. Those links resolve correctly from
the symlink's own position too, as long as the target is itself part of the
doc tree; but a link to something only the repository has (plain source
files, ``iron/``, ...) would 404 on the deployed site, since those aren't
copied into it.

This hook runs at build time (``on_page_markdown``) and rewrites only the
links that escape the doc tree into repo source, into absolute
``github.com`` URLs. Links between doc pages are left untouched so they keep
resolving locally on the site.

HTML images are matched to doc-tree assets, including symlinks, and use
URLs relative to the rendered page.
"""

import os
import re
import urllib.parse

from mkdocs.plugins import log
from mkdocs.utils import get_relative_url

GITHUB_REPO = "amd/IRON"
# publish-pages.yml does not set this, so a deployed site always links to devel.
GITHUB_BRANCH = os.environ.get("DOCS_GITHUB_REF", "devel")

_BLOB_BASE = f"https://github.com/{GITHUB_REPO}/blob/{GITHUB_BRANCH}"
_TREE_BASE = f"https://github.com/{GITHUB_REPO}/tree/{GITHUB_BRANCH}"

# Repo-root files that are themselves symlinked into the doc tree under
# another name. A link to one of these from elsewhere in the docs should land
# on that doc page, not bounce out to GitHub.
_ROOT_DOC_SYMLINKS = {
    "README.md": "installation.md",
    "CONTRIBUTING.md": "contributing.md",
    "AGENTS.md": "agents.md",
}

# Markdown inline link: [text](target)  and  [text](target "title")
_LINK_RE = re.compile(
    r"(?P<label>\[(?:[^\[\]]|\[[^\[\]]*\])*\])"  # [text] (allows one nesting level)
    r"\("
    r"\s*"
    r"(?P<target><[^>]*>|[^\s()]+)"  # <target> or bare target (no spaces/parens)
    r"(?P<title>\s+(?:\"[^\"]*\"|'[^']*'|\([^)]*\)))?"  # optional "title"
    r"\s*"
    r"\)"
)

_HTML_IMAGE_RE = re.compile(
    r"(?P<prefix><img\b[^>]*?\s+src\s*=\s*)"
    r"(?P<quote>[\"'])(?P<target>.*?)(?P=quote)",
    re.IGNORECASE,
)

_SKIP_PREFIXES = ("http://", "https://", "mailto:", "ftp://", "//", "tel:")

_EXTENSIONLESS_FILES = frozenset({"Makefile", "Dockerfile", "LICENSE", "README"})


def _split_suffix(target):
    """Split a link target into (path, suffix), suffix keeping #anchor/?query."""
    idx_hash = target.find("#")
    idx_q = target.find("?")
    cut = min([i for i in (idx_hash, idx_q) if i != -1], default=-1)
    if cut == -1:
        return target, ""
    return target[:cut], target[cut:]


def _looks_like_directory(path):
    """Heuristic: does this repo-relative path point at a directory?"""
    if path.endswith("/"):
        return True
    last = path.rsplit("/", 1)[-1]
    if last in _EXTENSIONLESS_FILES:
        return False
    _, ext = os.path.splitext(last)
    return ext == ""


def _rewrite_target(target, page_dir_link, page_dir_real, docs_dir, repo_root):
    """Return the rewritten URL for ``target``, or None to leave it unchanged.

    Two directories for the page are needed because a doc page may be a
    symlink (``docs/programming_guide/...`` -> the real
    ``<repo>/programming_guide/...``): ``page_dir_link`` is the page's
    directory as MkDocs sees it (under ``docs/``), used for doc-page
    detection; ``page_dir_real`` is the symlink-resolved directory, used to
    compute the real repo-root-relative path for the GitHub URL.
    """
    stripped = target.strip()
    if stripped.startswith("<") and stripped.endswith(">"):
        stripped = stripped[1:-1].strip()
    if not stripped:
        return None
    if stripped.lower().startswith(_SKIP_PREFIXES):
        return None
    if stripped.startswith("#") or stripped.startswith("?"):
        return None
    if stripped.startswith("/"):
        return None

    path_part, suffix = _split_suffix(stripped)
    if not path_part:
        return None

    decoded_path = urllib.parse.unquote(path_part)

    # --- Doc-page detection (MkDocs / symlink view) --------------------------
    # Resolve the link lexically against the page's docs-relative directory,
    # exactly as MkDocs does. If that lands on an existing path under docs/,
    # it's a doc page or asset and must stay a working relative link.
    doc_candidate = os.path.normpath(os.path.join(page_dir_link, decoded_path))
    in_docs_lexically = doc_candidate == docs_dir or doc_candidate.startswith(
        docs_dir + os.sep
    )
    if (
        in_docs_lexically
        and os.path.exists(doc_candidate)
        and page_dir_real != repo_root
    ):
        return None

    # --- Repo-source resolution (real-filesystem / GitHub view) --------------
    resolved = os.path.realpath(os.path.join(page_dir_real, decoded_path))
    real_docs = os.path.realpath(docs_dir)

    # --- Symlinked repo-root page (docs/installation.md -> ../README.md) -----
    # The page is served from inside docs/, but its own links are repo-root-
    # relative. Map a link back to one of the known doc tree targets.
    if page_dir_real == repo_root:
        lexical = os.path.normpath(os.path.join(page_dir_real, decoded_path))
        if (
            lexical == docs_dir or lexical.startswith(docs_dir + os.sep)
        ) and os.path.exists(lexical):
            return os.path.relpath(lexical, docs_dir).replace(os.sep, "/") + suffix
        root_name = os.path.basename(resolved)
        if (
            os.path.dirname(resolved) == repo_root
            and root_name in _ROOT_DOC_SYMLINKS
            and os.path.exists(resolved)
        ):
            return _ROOT_DOC_SYMLINKS[root_name] + suffix

    # A link that resolves into the docs tree proper from a page whose source
    # lives outside it: emit the path relative to the page's docs-view
    # directory and let MkDocs convert the .md target to the final page URL.
    if resolved == real_docs or resolved.startswith(real_docs + os.sep):
        rel_doc = os.path.relpath(resolved, page_dir_link).replace(os.sep, "/")
        if not rel_doc.startswith(".."):
            rel_doc = "./" + rel_doc
        return rel_doc + suffix

    # A repo-root file that is itself symlinked into the doc tree under
    # another name - map it to that doc page instead of bouncing to GitHub.
    if (
        os.path.dirname(resolved) == repo_root
        and os.path.basename(resolved) in _ROOT_DOC_SYMLINKS
    ):
        target_page = _ROOT_DOC_SYMLINKS[os.path.basename(resolved)]
        return (
            os.path.relpath(
                os.path.join(real_docs, target_page), page_dir_link
            ).replace(os.sep, "/")
            + suffix
        )

    if not (resolved == repo_root or resolved.startswith(repo_root + os.sep)):
        return None

    rel = os.path.relpath(resolved, repo_root)
    if rel.startswith(".."):
        return None
    rel = rel.replace(os.sep, "/")

    is_dir = _looks_like_directory(path_part)
    base = _TREE_BASE if is_dir else _BLOB_BASE
    encoded_rel = "/".join(urllib.parse.quote(seg) for seg in rel.split("/"))

    return f"{base}/{encoded_rel}{suffix}"


def on_page_markdown(markdown, page, config, files):
    """MkDocs event: rewrite repo-source links to GitHub URLs at build time."""
    abs_src = page.file.abs_src_path
    if not abs_src:
        return markdown

    page_dir_link = os.path.dirname(os.path.abspath(abs_src))
    page_dir_real = os.path.dirname(os.path.realpath(abs_src))
    docs_dir = os.path.abspath(config["docs_dir"])
    repo_root = os.path.dirname(os.path.realpath(docs_dir))

    # installation.md's source is README.md, whose H1 is the project name -
    # correct on GitHub, but on the site it duplicates the Home page's H1.
    if os.path.realpath(abs_src) == os.path.join(repo_root, "README.md"):
        markdown = re.sub(
            r"^#[ \t]+.*$", "# Installation", markdown, count=1, flags=re.MULTILINE
        )

    def _sub(match):
        target = match.group("target")
        new_target = _rewrite_target(
            target, page_dir_link, page_dir_real, docs_dir, repo_root
        )
        if new_target is None:
            return match.group(0)
        log.debug("rewrite_source_links: %s -> %s", target, new_target)
        label = match.group("label")
        title = match.group("title") or ""
        return f"{label}({new_target}{title})"

    def _sub_image(match):
        target = match.group("target")
        if target.lower().startswith(_SKIP_PREFIXES) or target.startswith(("/", "#")):
            return match.group(0)
        path, suffix = _split_suffix(target)
        resolved = os.path.realpath(
            os.path.join(page_dir_real, urllib.parse.unquote(path))
        )
        for file in files:
            if file.abs_src_path and os.path.realpath(file.abs_src_path) == resolved:
                url = get_relative_url(file.url, page.url) + suffix
                quote = match.group("quote")
                return f"{match.group('prefix')}{quote}{url}{quote}"
        return match.group(0)

    markdown = _LINK_RE.sub(_sub, markdown)
    return _HTML_IMAGE_RE.sub(_sub_image, markdown)
