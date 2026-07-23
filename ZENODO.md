# Zenodo paper release handoff

This checklist prepares the paper for a manual Zenodo Publication / Preprint
record. Publishing the record remains a deliberate manual action.

## Do not use the GitHub integration

Do not use Zenodo's GitHub integration for this deposit. That integration is
for Software records and Software Heritage archival. Create a normal manual
Zenodo upload instead.

## Build and verify the upload files

Run:

```sh
python3 scripts/build_release_artifacts.py
shasum -a 256 -c SHA256SUMS
```

Upload these four files:

1. `dist/semilocal-reflected-packet-oscillation-paper-v1.0.0.pdf`
2. `dist/semilocal-reflected-packet-oscillation-paper-v1.0.0-sources.tar.gz`
3. `dist/semilocal-reflected-packet-oscillation-paper-v1.0.0-reproducibility.tar.gz`
4. `ZENODO_UPLOAD_SHA256SUMS`

Set the PDF as the default preview. The PDF is the primary research object.
The LaTeX source and reproducibility archive are supplementary files.

## Deposit metadata

- Resource type: Publication
- Subtype: Preprint
- Title: Reflected-Packet Interactions in the Semilocal Weil Form: An Exact
  Zero Expansion and Unconditional Infinite Oscillation
- Version: 1.0.0
- Publication date: 2026-07-23
- Creator: LeonardSEO
- Language: English
- Related identifier:
  https://github.com/LeonardSEO/semilocal-reflected-packet-oscillation
  with relation `is supplemented by`
- Keywords:
  - Weil explicit formula
  - Riemann zeta function
  - prime powers
  - oscillation theorem
  - analytic number theory
  - reproducible mathematics

Abstract:

> We freeze one explicit real, even, compactly supported smooth packet and
> compute the interaction of two widely separated reflected translates in the
> complete semilocal Weil preform. The pole and all-prime-power sectors combine
> into a Stieltjes pairing against the Chebyshev-error distribution. A contour
> displacement gives an absolutely convergent expansion over all nontrivial
> and trivial zeros. The archimedean term and the remaining pole term cancel
> the complete trivial-zero series, leaving a zero-only expansion for the full
> reflected cross interaction. An unconditional positive-proportion theorem
> supplies infinitely many visible critical-line poles, and a Laplace-transform
> form of Landau's theorem excludes either eventual sign. Consequently both
> the arithmetic interaction and the even-minus-odd energy splitting take both
> strict signs arbitrarily far out. This is not a proof of the Riemann
> hypothesis, is only a fixed-packet result, and does not determine actual
> semilocal ground-state parity. Numerical computations are diagnostics only.

## DOI

Select **No existing DOI** unless this exact paper already has a DOI. You may
either let Zenodo assign the DOI at publication or reserve it in the draft.
Do not use the DOI of the repository, a software record, or another paper.

If you reserve the DOI before publication and want it printed in the PDF, add
it to the LaTeX paper, rebuild every upload file, regenerate both checksum
manifests, and re-run all validation before publishing.

## Rights and visibility

The source material contains no explicit open-access licensing grant. Do not
leave Zenodo's default CC-BY license selected. Use a custom rights statement
consistent with `NOTICE`:

- Title: No license granted; all rights reserved
- Description: No permission to use, copy, modify, or redistribute is granted
  beyond rights provided by applicable law. See the included NOTICE.

Public file visibility does not itself grant reuse rights. If Zenodo refuses
the custom statement, stop before publication and resolve the paper's licensing
policy explicitly; do not substitute another license without authorization.

## Final pre-publication checks

1. Confirm that the record says Publication / Preprint, not Software.
2. Confirm the creator name and add an ORCID only if it is verified.
3. Confirm paper version `1.0.0` and publication date `2026-07-23`.
4. Confirm the three content files against `ZENODO_UPLOAD_SHA256SUMS`, then
   confirm that manifest itself against the root `SHA256SUMS`.
5. Set the PDF as the default preview.
6. Confirm the scope warnings are visible in the abstract.
7. Preview the record and generated citation.
8. Publish only after Zenodo reports no metadata errors.

After publication, record the assigned version DOI, concept DOI, record URL,
and uploaded-file hashes in a follow-up repository metadata revision. Do not
rewrite the archived paper files.
