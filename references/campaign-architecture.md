# Account, Architecture & Naming

# meta-ads-mcp

---
name: meta-ads-mcp
description: >
  Complete operational guide for creating, managing, and documenting Meta (Facebook/Instagram)
  ad campaigns via the Facebook Ads MCP. Use this skill whenever the user mentions: creating
  a Facebook ad, managing a campaign, setting budgets, building audiences, retargeting,
  checking ad performance, installing a pixel, or anything related to Meta Ads across any
  of the managed sites (Seraphim, Pachamama, Onyx-WP, WP Academy, Aguila). Also trigger
  for pre-campaign planning, intake questions, naming conventions, or campaign documentation.
---

# Facebook Ads MCP — Operational Guide

> **Scope**: How to create, manage, update, pause, and document Meta (Facebook/Instagram) ad campaigns using the Facebook Ads MCP. Covers account setup, campaign architecture, targeting, creative, tracking, retargeting, documentation, safety guardrails, and pre-flight questions.

---

## 1. ACCOUNT & BUSINESS SETUP

### Which Ad Account & Business Manager to Use
- **Always operate through Meta Business Manager** (business.facebook.com), never through personal ad accounts. Business accounts have better access controls, billing protection, and can hold multiple assets.
- Identify the correct **Ad Account ID** (`act_XXXXXXXXXX`) before executing any action. Use `ads_get_ad_accounts` to list accessible accounts.
- Identify the correct **Business ID** using `ads_get_pages_for_business` if page-level targeting is needed.
- Each website/brand should have its own dedicated ad account. Never mix sites into one account — it muddles reporting and risks cross-contamination if an account is flagged.
- Keep the **billing method verified** before launching. Unverified billing = automatic campaign pause.

### MCP Account Verification Checklist (run before first campaign)
1. `ads_get_ad_accounts` — confirm correct account IDs accessible
2. `ads_get_pages_for_business` — confirm correct Facebook Page linked
3. `ads_catalog_get_catalogs` — check if a product catalog exists (needed for dynamic ads)
4. `ads_get_dataset_details` — verify Pixel is installed and receiving events
5. `ads_get_dataset_quality` — check Event Match Quality score (target: 7+ out of 10)

---

## 2. CAMPAIGN ARCHITECTURE: THE THREE-TIER HIERARCHY

```
Campaign  (Objective + Budget Strategy)
  └── Ad Set  (Audience + Placement + Schedule + Budget)
        └── Ad  (Creative + Copy + CTA + Destination URL)
```

### Campaign Level
- Sets the **objective** — the single most important decision. Meta's algorithm optimizes delivery for this goal.
- Sets **budget strategy**: CBO (Campaign Budget Optimization) or ABO (Ad Set Budget Optimization).
- One campaign per **product / funnel stage combination**.

| Business Goal | Campaign Objective |
|---|---|
| Drive website visits | Traffic |
| Get form submissions / leads | Leads |
| Sell a product | Sales |
| Grow brand recognition | Awareness |
| Promote content / page engagement | Engagement |
| Promote an app | App Promotion |

> � �? **2026 update**: Detailed interest targeting was deprecated January 2026. Use **Advantage+ Audience** (Meta's AI targeting) or **broad targeting with strong creative** as primary strategy. Interest-based audiences created before October 2025 no longer deliver.

### Ad Set Level
- Contains: **audience**, **placement**, **schedule**, **budget** (if ABO).
- 3–5 ad sets per campaign is the recommended range — enough to test, not so many the budget fragments.
- Each ad set should target a **distinct, non-overlapping audience segment**.
- Minimum audience size: **50,000+ users** for efficient delivery.
- Budget must allow **~50 optimization events per week** to exit the Learning Phase.

### Ad Level
- Contains: **creative** (image/video), **headline**, **body copy**, **CTA button**, **destination URL**.
- Limit: **3–5 ads per ad set** — enough for testing, not so many each ad starves for impressions.
- Name ads consistently for reporting clarity.

---

## 3. NAMING CONVENTIONS (MANDATORY)

Use consistent naming across all three levels. Recommended format:

```
[Site] | [Objective] | [Funnel Stage] | [Audience/Test Variable] | [Date YYYY-MM]

Examples:
Seraphim | Traffic | Cold | Broad-Advantage+ | 2026-05
Pachamama | Leads | Warm | Video-Viewers-LAL | 2026-05
OnyxWP | Sales | Retargeting | Site-Visitors-30d | 2026-05
```

For **Ads**:
```
[Site] | [Format] | [Angle/Hook] | [Variation Letter]

Example:
Seraphim | Video | Incense-Story | A
Pachamama | Image | Testimonial-Sarah | B
```

---
