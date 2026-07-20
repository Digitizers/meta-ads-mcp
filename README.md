# Meta Ads MCP — Claude Code & OpenClaw Skill

[![CI](https://github.com/Digitizers/meta-ads-mcp/actions/workflows/ci.yml/badge.svg)](https://github.com/Digitizers/meta-ads-mcp/actions/workflows/ci.yml)
![Claude Code Skill](https://img.shields.io/badge/Claude_Code-Skill-d97757)
![OpenClaw Skill](https://img.shields.io/badge/OpenClaw-Skill-purple)
![Meta Ads](https://img.shields.io/badge/Meta-Ads-1877f2)
![License: MIT--0](https://img.shields.io/badge/License-MIT--0-green)
![Version](https://img.shields.io/badge/version-1.1.0-blue)

A practical **Claude Code & OpenClaw skill** for planning, creating, managing, optimizing, and documenting Meta/Facebook/Instagram ad campaigns through the Facebook Ads MCP — with safety-first defaults for real ad accounts and real budgets.

This is not just a tool reference. It is an operational playbook for running Meta Ads responsibly: intake, account checks, campaign structure, budgets, audiences, creative, tracking, retargeting, KPIs, documentation, and non-negotiable safety guardrails.

## Features

- ✅ **MCP campaign workflow** — step-by-step use of Facebook Ads MCP tools for accounts, campaigns, ad sets, ads, reporting, and opportunities.
- ✅ **Safety-first launch process** — campaigns, ad sets, and ads are created `PAUSED` until reviewed and approved.
- ✅ **Account verification checklist** — ad account, page, catalog, Pixel/dataset, and Event Match Quality checks before launch.
- ✅ **Campaign architecture** — objective selection, CBO vs ABO, funnel stages, ad set planning, and naming conventions.
- ✅ **Budget guardrails** — no >20% budget jumps, Learning Phase protection, spend ceilings, and launch-week monitoring.
- ✅ **Audience strategy** — cold, warm, hot, lookalikes, retargeting, exclusions, and 2026 targeting realities.
- ✅ **Creative playbook** — formats, hooks, copy frameworks, UGC/video guidance, and asset generation rules.
- ✅ **Pixel + CAPI tracking** — event priorities, WordPress setup notes, deduplication, and verification checklist.
- ✅ **Retargeting structure** — hot/warm audiences, frequency control, exclusions, and creative direction.
- ✅ **Reporting and KPIs** — CTR, CPC, CPM, CPL, CPA, ROAS, frequency, anomaly signals, and intervention rules.
- ✅ **Documentation discipline** — campaign brief, creative log, results tracker, and decisions log for every campaign.
- ✅ **Public-ready skill packaging** — clean skill payload folder, repo-level marketing docs, CI validation, and explicit file allowlist.

## Package Layout

The actual skill payload lives in:

```text
meta-ads-mcp/
```

Repository-only files such as this README, changelog, license, CI, validation scripts, and package metadata intentionally stay outside the skill directory.

## Version

Current version: **1.1.0**

## Installation

### Via OpenClaw / ClawHub

```bash
openclaw skills install meta-ads-mcp
```

### Manual Installation

```bash
cp -R meta-ads-mcp ~/.openclaw/workspace/skills/meta-ads-mcp
```

### Windows note

The plugin ships its skill through a git **symlink** (`skills/` → the in-repo
source). Cloning with `core.symlinks=false` — the default on many Windows
setups — turns that link into a plain text file and the skill will not load.
Before installing on Windows, enable Developer Mode and run
`git config --global core.symlinks true`, or use WSL. macOS/Linux need nothing.

## What This Skill Helps With

### 1. Pre-Campaign Planning

Use it when you need to answer:

- Which ad account, page, pixel, dataset, or catalog should we use?
- What is the campaign objective?
- What is the conversion event?
- What does success look like numerically?
- Is this cold, warm, retargeting, or full-funnel?
- Do we have assets, or do we need to generate creative?
- Is the landing page ready for traffic?

### 2. Safe Campaign Creation via MCP

Recommended flow:

```text
Verify account → Intake → Plan structure → Create PAUSED → Preview → Approve → Activate → Document
```

Core tools covered:

```text
ads_get_ad_accounts
ads_get_pages_for_business
ads_catalog_get_catalogs
ads_get_dataset_details
ads_get_dataset_quality
ads_create_campaign
ads_create_ad_set
ads_create_ad
ads_activate_entity
ads_get_ad_entities
ads_insights_performance_trend
ads_insights_anomaly_signal
ads_get_opportunity_score
```

### 3. Performance Management

The playbook covers when to intervene:

| Signal | Typical action |
|---|---|
| CTR below target | Test a stronger hook or creative angle |
| CPM rising week-over-week | Refresh creative or expand audience |
| Frequency too high | Expand audience or pause fatigued ad set |
| Learning Limited | Consolidate ad sets or increase budget carefully |
| Spend with zero conversions | Pause, then review Pixel, event, landing page, offer |
| ROAS below break-even | Pause ad set and diagnose creative/audience/funnel |

## Reference Guides

| File | Purpose |
|---|---|
| [`meta-ads-mcp/SKILL.md`](meta-ads-mcp/SKILL.md) | Skill entrypoint and execution rules |
| [`meta-ads-mcp/references/campaign-architecture.md`](meta-ads-mcp/references/campaign-architecture.md) | Account setup, campaign hierarchy, naming conventions |
| [`meta-ads-mcp/references/budget-and-audience.md`](meta-ads-mcp/references/budget-and-audience.md) | CBO/ABO, budgets, cold/warm/hot audiences, exclusions |
| [`meta-ads-mcp/references/creative-and-copy.md`](meta-ads-mcp/references/creative-and-copy.md) | Ad formats, copy frameworks, creative asset guidance |
| [`meta-ads-mcp/references/tracking-and-retargeting.md`](meta-ads-mcp/references/tracking-and-retargeting.md) | Pixel, CAPI, events, retargeting structures |
| [`meta-ads-mcp/references/campaign-operations.md`](meta-ads-mcp/references/campaign-operations.md) | MCP creation flow, KPIs, reporting, documentation |
| [`meta-ads-mcp/references/intake-questions.md`](meta-ads-mcp/references/intake-questions.md) | Pre-campaign intake questions |
| [`meta-ads-mcp/references/safety-guardrails.md`](meta-ads-mcp/references/safety-guardrails.md) | Non-negotiable safety and account health rules |

## Safety Model

- ✅ **Create everything paused** — never launch spend before review.
- ✅ **Pause, never delete** — preserve historical learning and auditability.
- ✅ **Verify Pixel/dataset before campaigns** — no tracking, no optimization.
- ✅ **Declare special ad categories** — housing, credit, employment, political/social issues.
- ✅ **Avoid Learning Phase disruption** — no simultaneous budget, creative, and targeting edits.
- ✅ **Document every meaningful change** — decisions, reasons, results.
- ✅ **Use Business Manager** — avoid personal ad account operations.
- ❌ **Never activate without explicit approval.**
- ❌ **Never bypass account restrictions or policy issues.**

## Use Cases

- Launching a lead generation campaign.
- Planning an e-commerce sales campaign.
- Building retargeting audiences and hot/warm funnel campaigns.
- Auditing Pixel/CAPI readiness before paid traffic.
- Turning a campaign brief into a paused Meta campaign structure.
- Diagnosing weak CTR, high CPM, Learning Limited, or poor ROAS.
- Standardizing campaign naming and documentation across brands.
- Creating a repeatable paid-media operations workflow for agencies.

## Requirements

- OpenClaw with access to the Facebook Ads MCP tools.
- Meta Business Manager access to the relevant assets.
- Verified ad account billing before launch.
- Facebook Page linked to the ad account.
- Pixel/dataset installed and receiving events.
- Application-specific permissions for campaign creation and reporting.

## Development

Validate the skill package locally:

```bash
npm test
npm pack --dry-run
```

The CI checks:

- skill frontmatter
- referenced files exist
- repo-only files stay outside `meta-ads-mcp/`
- obvious encoding corruption
- hardcoded-looking secrets/placeholders
- npm package allowlist

## Links

- **Repository:** https://github.com/Digitizers/meta-ads-mcp
- **OpenClaw:** https://openclaw.ai
- **Meta Ads Manager:** https://business.facebook.com/adsmanager
- **Meta Events Manager:** https://business.facebook.com/events_manager
- **Digitizer:** https://www.digitizer.studio

## License

MIT-0 — see [LICENSE.txt](LICENSE.txt)

---

Built with ❤️ for OpenClaw by [Digitizer](https://www.digitizer.studio)
