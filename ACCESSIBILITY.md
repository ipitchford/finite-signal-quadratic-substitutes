# Accessible reading format

paper.md is generated from the unchanged paper.tex by Pandoc, with a small reproducible formatting helper to preserve title/abstract, named citation markers and separate bibliography entries. Mathematical content is retained as TeX-style mathematical notation in Markdown. This is a text-reading alternative, not a claim of WCAG conformance, tagged PDF, or screen-reader-tested mathematical speech.

The authoritative scientific source remains paper.tex and its matching supplied PDF. Cross-reference and citation presence checks supplement but do not replace full visual and assistive-technology review. A final publication should inspect rendered Markdown, mathematical notation, tables, links and all PDF pages. No manuscript claim is repaired or strengthened by conversion.

Regenerate with: python3 -B tools/build_markdown.py (requires Pandoc). The helper is formatting-only and does not edit paper.tex.
