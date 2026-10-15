# Component license map

| Component | License | Boundary |
|---|---|---|
| Original paper.tex, paper.pdf, paper.md, project prose and claims | CC0-1.0 | See LICENSE and PUBLIC_DOMAIN.md |
| Constructed tables, example.json and original replay records | CC0-1.0 | Mathematical observations; no personal data |
| Original Python programs, formatting helper and CI configuration | MIT | See LICENSE-CODE |
| Cited research works and any quoted excerpts | Upstream terms / NOASSERTION | Citations do not transfer ownership; full third-party works are not bundled |
| PDF embedded Latin Modern fonts | GUST Font License | Embedded subsets, not relicensed by this package |
| PDF embedded AMS MSBM10 | SIL Open Font License | Embedded subset, not relicensed by this package |

No external human review is included. The house licenses apply only to original materials and rights actually held; they do not claim copyright where applicable law provides none.

Fresh `pdffonts paper.pdf` inspection of the DOI-bound PDF found only Latin Modern and AMS MSBM10 fonts: all 16 entries are embedded subsets with Unicode maps. The [Latin Modern distribution](https://www.ctan.org/tex-archive/fonts/lm) expressly permits use and distribution under the GUST Font License; the [AMS Fonts distribution](https://ctan.org/tex-archive/fonts/amsfonts?lang=en) identifies its SIL Open Font License. These upstream font rights remain separate from the document’s CC0 dedication. No standalone font files are redistributed. See METADATA_BINDING_QA.json for the actual font inventory. Source check: 2026-10-15; direct GUST URL was unavailable and AMS website returned 403, so the upstream distributions on CTAN supplied the license evidence.
