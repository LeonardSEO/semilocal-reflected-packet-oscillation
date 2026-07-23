# Zenodo release handoff

This checklist prepares version 1.0.2 for preservation as a Zenodo Software
record. Publishing the Zenodo record remains a deliberate manual action.

## Preferred route: GitHub integration

1. Sign in to Zenodo and link the GitHub account that owns
   `LeonardSEO/semilocal-reflected-packet-oscillation`.
2. Open the Zenodo GitHub page, synchronize repositories, and enable this
   repository **before** creating the GitHub `v1.0.2` release.
3. Create the GitHub `v1.0.2` release from the commit containing this file.
4. Wait for Zenodo to process the release, inspect the draft/record metadata,
   and publish only after the checks below pass.

The repository intentionally uses `CITATION.cff` as its single
machine-readable creator and citation metadata source. There is no
`.zenodo.json`: when both files are present, Zenodo ignores `CITATION.cff`.

## Manual route

Run:

```sh
python3 scripts/build_release_artifacts.py
shasum -a 256 -c SHA256SUMS
```

Upload exactly one compressed file:

`dist/semilocal-reflected-packet-oscillation-v1.0.2-zenodo.zip`

Using one source ZIP allows Zenodo to submit the Software record for Software
Heritage archival. The ZIP contains an internal `ZENODO_SHA256SUMS` manifest
covering every deposited file.

## Deposit metadata

- Resource type: Software
- Title: Semilocal Reflected-Packet Oscillation
- Version: 1.0.2
- Publication date: 2026-07-23
- Creator: LeonardSEO
- Language: English
- Repository: https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation
- Keywords:
  - Weil explicit formula
  - Riemann zeta function
  - prime powers
  - oscillation theorem
  - reproducible mathematics

Version `1.0.2` identifies the reproducibility software bundle. The included
mathematical paper remains the unchanged paper version `1.0.0`; no analytic
claim was revised by the packaging and documentation releases.

Description:

> A standalone proof and reproducibility package for an exact zero expansion
> and unconditional infinite sign changes of one fixed reflected-packet
> interaction in the complete semilocal Weil preform. This is not a proof of
> the Riemann hypothesis, is only a fixed-packet result, and does not determine
> actual semilocal ground-state parity. Numerical calculations are diagnostics
> and are separate from the load-bearing analytic proof.

## DOI

Select **No existing DOI** and let Zenodo assign a DOI at publication. Do not
insert a placeholder or the DOI of a different object. After publication, add
the assigned version DOI and concept DOI to a later repository metadata
revision; do not rewrite the archived `v1.0.2` files.

## Rights and visibility

The source material contains no explicit open-source licensing grant. Do not
leave Zenodo's default CC-BY license selected and do not select an OSI license.
Use a custom rights statement consistent with `NOTICE`:

- Title: No license granted; all rights reserved
- Description: No permission to use, copy, modify, or redistribute is granted
  beyond rights provided by applicable law. See the included NOTICE.

Public file visibility does not itself grant reuse rights. If Zenodo refuses
the custom statement for the selected workflow, stop before publication and
resolve the licensing policy explicitly; do not substitute another license.

## Final pre-publication checks

1. Confirm the creator name and add an ORCID only if it is verified.
2. Confirm version `1.0.2` and publication date `2026-07-23`.
3. Confirm that the record contains one ZIP for a manual Software deposit.
4. Confirm that the ZIP SHA-256 matches the corresponding `SHA256SUMS` entry.
5. Confirm the scope warnings are visible in the description.
6. Preview the record and citation.
7. Publish only after the metadata validation has no errors.

After publication, record the Zenodo version DOI, concept DOI, record URL, and
the deposited ZIP SHA-256 in a follow-up repository release.
