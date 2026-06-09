# Changelog

## 1.1.0 — 2026-06-05

Security/compliance documentation hardening (ClawHub audit, additive docs only):

- Added a Privacy & compliance section for Custom Audiences / CAPI PII (lawful basis, consent, SHA-256 hashing, minimization, suppression, DPA/residency).
- Added a Scope & external dependencies disclosure (Google Drive, facebook-ads, flux-imagegen).
- Tightened invocation triggers ("ad budgets/spend", "ad audiences") to reduce generic-marketing activation.
- Added a Data & privacy section to the safety guardrails.

## 1.0.0 - 2026-05-05

Initial public-ready OpenClaw skill package for Meta Ads MCP operations.

- Moved publishable skill payload into `meta-ads-mcp/`.
- Added polished root README as a marketing/usage overview.
- Added MIT-0 license and package metadata.
- Added CI validation for skill structure, references, packaging, and obvious scanner-risk patterns.
- Cleaned campaign architecture reference: removed duplicated frontmatter and fixed encoding corruption.
- Added explicit safety-first workflow: create paused, preview, approve, activate, document.
