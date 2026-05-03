---
name: meta-ads-mcp
description: >
  Operational guide for creating, managing, and documenting Meta (Facebook/Instagram)
  ad campaigns via the Facebook Ads MCP. Use whenever the user mentions creating a
  Facebook ad, managing a campaign, setting budgets, building audiences, retargeting,
  checking ad performance, or installing a pixel — across any managed site
  (Seraphim, Pachamama, Onyx-WP, WP Academy, Aguila). Also trigger for pre-campaign
  planning, intake questions, naming conventions, or campaign documentation.
---

# Facebook Ads MCP — Operational Guide

> **Scope**: How to create, manage, update, pause, and document Meta (Facebook/Instagram) ad campaigns using the Facebook Ads MCP. Covers account setup, campaign architecture, targeting, creative, tracking, retargeting, documentation, and safety guardrails.

## How to use this skill

This file is the entrypoint. Detailed playbooks live in `references/`. Load only the file relevant to the current task:

| Task | Reference |
|---|---|
| Picking the right ad account, building campaign hierarchy, naming an entity | [`references/campaign-architecture.md`](references/campaign-architecture.md) |
| Setting budgets (CBO/ABO), choosing cold/warm/hot audiences, exclusions | [`references/budget-and-audience.md`](references/budget-and-audience.md) |
| Choosing ad format, writing copy frameworks, generating images | [`references/creative-and-copy.md`](references/creative-and-copy.md) |
| Pixel + CAPI install, event setup, retargeting structure | [`references/tracking-and-retargeting.md`](references/tracking-and-retargeting.md) |
| Step-by-step MCP creation flow, KPIs, per-campaign documentation | [`references/campaign-operations.md`](references/campaign-operations.md) |
| Pre-campaign intake — what to ask before launching | [`references/intake-questions.md`](references/intake-questions.md) |
| Hard safety rules — never delete, never edit during learning, etc. | [`references/safety-guardrails.md`](references/safety-guardrails.md) |

## Core workflow (always follow this order)

1. **Verify the account** — `ads_get_ad_accounts`, `ads_get_pages_for_business`, `ads_get_dataset_details`. Never proceed with an unverified pixel or unlinked page.
2. **Run intake** — gather goal, audience, creative, budget, timeline, landing page (see `references/intake-questions.md`). Do not invent answers.
3. **Plan structure** — pick objective, decide CBO vs ABO, draft 3–5 ad sets and 3–5 ads per set with consistent names (see `references/campaign-architecture.md`).
4. **Create everything PAUSED** — campaign → ad set → ad, all with `status: PAUSED`. See the step-by-step in `references/campaign-operations.md`.
5. **Preview + verify** — check pixel attachment, destination URL, ad preview, and naming in Ads Manager UI before activation.
6. **Activate** — flip status to ACTIVE only after the full review is signed off.
7. **Document** — log the campaign brief, audiences, creatives, and decisions in the site's Drive folder (see `references/campaign-operations.md` § 13).

## Non-negotiable safety rules

These are summarized here; full list in `references/safety-guardrails.md`.

- **PAUSE, never delete.** Deletes destroy historical learning and cannot be reversed.
- **Always create in PAUSED status.** No exceptions.
- **Never edit budget by more than 20% at once** — larger jumps reset the Learning Phase.
- **Never run a campaign without a verified pixel.**
- **Never touch a campaign in Learning Phase** (first 7 days / ~50 events).
- **Special ad categories must be declared** (housing, credit, employment, political).
- **Detailed interest targeting was deprecated January 2026.** Use Advantage+ Audience or broad targeting + strong creative.

## Key MCP tools (quick reference)

```
Account & assets:
  ads_get_ad_accounts            list accessible ad accounts
  ads_get_pages_for_business     list pages under a Business Manager
  ads_catalog_get_catalogs       check for product catalog (dynamic ads)
  ads_get_dataset_details        verify pixel installation
  ads_get_dataset_quality        check Event Match Quality (target 7+/10)

Creation:
  ads_create_campaign            create campaign (always status: PAUSED)
  ads_create_ad_set              create ad set under a campaign
  ads_create_ad                  create ad under an ad set
  ads_activate_entity            flip status (use PAUSED to disable, never delete)

Reporting:
  ads_get_ad_entities                    pull campaign/ad set/ad performance
  ads_insights_performance_trend         analyze trends over time
  ads_insights_anomaly_signal            detect unusual patterns
  ads_insights_auction_ranking_benchmarks  compare against benchmarks
  ads_get_opportunity_score              Meta's recommendations
```

## Related skills

- **facebook-ads** — full ad copy generation (3 copy variations, 3 headlines, CTA options, visual concept). Use for creative writing.
- **flux-imagegen** — generate ad images (1080×1080 for 1:1, 1080×1350 for 4:5).
