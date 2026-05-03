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

# Facebook Ads MCP â€” Operational Guide

> **Scope**: How to create, manage, update, pause, and document Meta (Facebook/Instagram) ad campaigns using the Facebook Ads MCP. Covers account setup, campaign architecture, targeting, creative, tracking, retargeting, documentation, safety guardrails, and pre-flight questions.

---

## 1. ACCOUNT & BUSINESS SETUP

### Which Ad Account & Business Manager to Use
- **Always operate through Meta Business Manager** (business.facebook.com), never through personal ad accounts. Business accounts have better access controls, billing protection, and can hold multiple assets.
- Identify the correct **Ad Account ID** (`act_XXXXXXXXXX`) before executing any action. Use `ads_get_ad_accounts` to list accessible accounts.
- Identify the correct **Business ID** using `ads_get_pages_for_business` if page-level targeting is needed.
- Each website/brand should have its own dedicated ad account. Never mix sites into one account â€” it muddles reporting and risks cross-contamination if an account is flagged.
- Keep the **billing method verified** before launching. Unverified billing = automatic campaign pause.

### MCP Account Verification Checklist (run before first campaign)
1. `ads_get_ad_accounts` â€” confirm correct account IDs accessible
2. `ads_get_pages_for_business` â€” confirm correct Facebook Page linked
3. `ads_catalog_get_catalogs` â€” check if a product catalog exists (needed for dynamic ads)
4. `ads_get_dataset_details` â€” verify Pixel is installed and receiving events
5. `ads_get_dataset_quality` â€” check Event Match Quality score (target: 7+ out of 10)

---

## 2. CAMPAIGN ARCHITECTURE: THE THREE-TIER HIERARCHY

```
Campaign  (Objective + Budget Strategy)
  â””â”€â”€ Ad Set  (Audience + Placement + Schedule + Budget)
        â””â”€â”€ Ad  (Creative + Copy + CTA + Destination URL)
```

### Campaign Level
- Sets the **objective** â€” the single most important decision. Meta's algorithm optimizes delivery for this goal.
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

> âš ï¸ **2026 update**: Detailed interest targeting was deprecated January 2026. Use **Advantage+ Audience** (Meta's AI targeting) or **broad targeting with strong creative** as primary strategy. Interest-based audiences created before October 2025 no longer deliver.

### Ad Set Level
- Contains: **audience**, **placement**, **schedule**, **budget** (if ABO).
- 3â€“5 ad sets per campaign is the recommended range â€” enough to test, not so many the budget fragments.
- Each ad set should target a **distinct, non-overlapping audience segment**.
- Minimum audience size: **50,000+ users** for efficient delivery.
- Budget must allow **~50 optimization events per week** to exit the Learning Phase.

### Ad Level
- Contains: **creative** (image/video), **headline**, **body copy**, **CTA button**, **destination URL**.
- Limit: **3â€“5 ads per ad set** â€” enough for testing, not so many each ad starves for impressions.
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

## 4. BUDGET STRATEGY

### CBO vs ABO
| Scenario | Recommended |
|---|---|
| Total daily budget â‰¥ $50, trust Meta's algorithm | **CBO** â€” Meta allocates to best-performing ad set |
| Small budget, strict testing, need visibility per audience | **ABO** â€” fixed budget per ad set |
| Finding winning creatives in a new account | **ABO** first, then consolidate to CBO at scale |

### Starting Budgets (per site/campaign)
- **Testing phase**: $10â€“$20/day per campaign (ABO) â€” just enough to generate signal
- **Scaling a winner**: $50â€“$200/day CBO, let Meta optimize
- **Learning Phase rule**: Never edit budget by more than 20% at once â€” it resets learning
- **Minimum for a conversion campaign to exit Learning Phase**: ~$50 total spend generating 50+ conversion events

### Budget Guardrails
- Set **Campaign Spending Limits** in Ads Manager as a hard ceiling
- Set **Account Spending Limits** in billing settings
- Review daily spend every morning during launch week
- Never launch a campaign on a Friday without someone monitoring it

---

## 5. AUDIENCE TARGETING

### Full-Funnel Audience Strategy

#### Cold (Prospecting) â€” People who don't know the brand
- **Advantage+ Audience** (recommended 2026): Let Meta find the right people using your pixel data as a signal. Provide broad demographics + let algorithm work.
- **Lookalike Audiences**: Build from website visitors (180-day), purchasers, or email list. Start with 1â€“2% LAL, test 3â€“5% for scale.
- **Broad Targeting**: Age + gender + country only â€” trust Meta's algorithm with strong creative.

#### Warm (Engagement Retargeting) â€” People who know the brand but haven't converted
- Facebook/Instagram page engagers (90 days)
- Video viewers (25%, 50%, 75%)
- Website visitors who didn't convert (30/60/90 days)

#### Hot (Purchase Retargeting) â€” People who showed strong purchase intent
- Website visitors of key pages (product page, pricing page, checkout)
- Add-to-cart but didn't purchase (7â€“14 days)
- Email list upload (Custom Audience from CRM)

### Exclusions (Always Set These)
- Exclude existing customers from prospecting campaigns
- Exclude retargeting pools from cold audiences
- Exclude purchasers from add-to-cart retargeting
- Use Meta's **Audience Overlap tool** to check for cannibalization

### Custom Audiences to Build and Maintain
1. Website visitors (30 / 60 / 90 / 180 days)
2. Video viewers by percentage (25% / 50% / 75%)
3. Page engagers (30 / 90 days)
4. Customer list uploads (email + phone, hashed)
5. Purchasers / converters

---

## 6. AD FORMATS & WHEN TO USE THEM

| Format | Best For | Notes |
|---|---|---|
| **Single Image** | Awareness, traffic, quick tests | Fast to produce, cheap to test, use 1:1 ratio |
| **Single Video** | Cold prospecting, storytelling, UGC | Hook in first 3 seconds, 15â€“60s optimal, add subtitles |
| **Carousel** | Products, features, step-by-step | Each card = one idea; works for e-commerce |
| **Instant Experience** | Immersive mobile landing pages | Full-screen, loads fast, good for high-ticket |
| **Dynamic / Collection** | E-commerce with product catalog | Requires catalog; auto-personalizes |
| **Lead Form** | Lead gen without a landing page | Native to Facebook; frictionless |

### Creative Best Practices (2026)
- **UGC-style videos** (creator talking to camera, holding product) consistently outperform polished ads
- **Real faces with genuine expressions** outperform stock imagery
- **First 3 seconds of video are everything** â€” open with conflict, result, or bold claim
- **Always add subtitles** â€” 80%+ watch with sound off
- **Use 4:5 ratio** for feed (takes more screen space than 1:1)
- **Aspect ratio 9:16** for Stories and Reels placements

---

## 7. AD COPY FRAMEWORK

Use the **existing facebook-ads SKILL** for full copy generation. Quick reference:

| Funnel Stage | Framework | Opening Style |
|---|---|---|
| Cold | AIDA | Attention hook â†’ build interest â†’ desire â†’ action |
| Warm | PAS | Problem â†’ Agitate â†’ Solution |
| Retargeting | BAB | Before â†’ After â†’ Bridge |

**Copy Rules (Non-Negotiable)**:
- Hook is the first sentence â€” rewrite it until it's undeniable
- "You / your" always, never "we / our" in the hook
- Short sentences, line breaks, one idea per paragraph
- For health/wellness: never use "cures", "guarantees", "eliminates" â€” use "helps", "may", "many people find"

---

## 8. ASSET & TEXT GENERATION

### For Image Creatives
- Use the **flux-imagegen skill** to generate ad images with Claude
- Request: 1080Ã—1080 (1:1 feed) or 1080Ã—1350 (4:5 portrait)
- Generate at least 3 visual variations per angle
- Always test: lifestyle image vs. product closeup vs. text-dominant graphic

### For Copy
- Use the **facebook-ads skill** â€” generates full ad packages with 3 copy variations, 3 headlines, CTA button options, and visual concept descriptions
- Always generate multiple variations â€” A/B testing is non-negotiable

### Asset Storage
- Save all approved ad assets in the **Google Drive folder** for that site
- Name files to match the naming convention: `[Site]-[Format]-[Angle]-[Variation]`
- Keep a "creative graveyard" folder for retired but potentially recyclable creatives

---

## 9. PIXEL & TRACKING SETUP

### The Recommended Setup: Pixel + CAPI Together

**Meta Pixel** (browser-side) and **Conversions API / CAPI** (server-side) must both be running. Never rely on Pixel alone â€” Safari/Firefox block third-party cookies by default, and iOS privacy changes cause 40â€“60% data loss in Pixel-only setups.

```
Browser Side:  User action â†’ JavaScript Pixel fires â†’ Meta receives event
Server Side:   User action â†’ Your server â†’ CAPI â†’ Meta receives event
Deduplication: Both send same event_id â†’ Meta counts it once
```

### Priority Events to Track (in order of importance)
1. `Purchase` / `Lead` â€” primary conversion event
2. `InitiateCheckout` / `ViewContent` â€” funnel signals
3. `AddToCart` â€” intent signals
4. `PageView` â€” top-of-funnel presence
5. `CompleteRegistration` â€” for lead-gen sites

### Pixel Installation (WordPress Sites)
- Install via **Meta for WordPress plugin** (official) or **PixelYourSite plugin**
- For CAPI on WordPress: use **PixelYourSite Pro** (has CAPI built in) or custom server-side integration
- Verify in **Events Manager â†’ Test Events** tool after installation
- Check **Event Match Quality (EMQ)** score â€” target 7+/10

### Pixel Verification Checklist
- [ ] Pixel fires on all key pages
- [ ] Purchase / Lead event fires correctly on conversion page
- [ ] CAPI events are sending (check Events Manager â†’ Aggregated Event Measurement)
- [ ] Deduplication is working (no doubled events in Events Manager)
- [ ] EMQ score is 7+/10 (improve by sending email/phone in event parameters)
- [ ] Attribution window set to: 7-day click, 1-day view

---

## 10. RETARGETING CAMPAIGNS

### Retargeting Campaign Architecture

```
Campaign: [Site] | Sales/Leads | Retargeting | [Date]
  Ad Set 1: Hot â€” Checkout abandoners (7 days)
  Ad Set 2: Warm â€” Product page visitors (30 days, excl. purchasers)
  Ad Set 3: Warm â€” Video viewers 75% (60 days)
  Ad Set 4: Warm â€” Page engagers (90 days)
```

### Retargeting Creative Strategy
- Be specific â€” reference what they viewed or did ("Still thinking about [product]?")
- Show social proof â€” testimonials, reviews, trust signals
- Create urgency if truthful â€” limited stock, expiring offer
- Different creative from prospecting â€” they know you already
- Use BAB (Before â†’ After â†’ Bridge) framework

### Retargeting Exclusions (Critical)
- Always exclude purchasers/converters from all retargeting sets
- Set a **frequency cap** â€” max 3â€“5 impressions per person per week to avoid burnout
- Monitor frequency score â€” above 5 = audience is oversaturated, expand or refresh creative

---

## 11. CAMPAIGN MANAGEMENT: CREATING VIA MCP

### Creating a Campaign (Step-by-Step with MCP Tools)

**Step 1**: Gather account info
```
ads_get_ad_accounts â†’ get act_XXXXXXXXXX
ads_get_pages_for_business â†’ get page ID
ads_get_dataset_details â†’ get pixel ID
```

**Step 2**: Create campaign (PAUSED)
```
ads_create_campaign
  - objective: TRAFFIC / OUTCOME_LEADS / OUTCOME_SALES
  - status: PAUSED
  - name: [naming convention]
  - special_ad_categories: [] (or CREDIT/HOUSING/EMPLOYMENT/ISSUES if applicable)
```

**Step 3**: Create ad set (PAUSED)
```
ads_create_ad_set
  - campaign_id: from step 2
  - targeting: audience definition
  - budget: daily_budget (in cents)
  - optimization_goal: LINK_CLICKS / LEAD_GENERATION / CONVERSIONS
  - status: PAUSED
```

**Step 4**: Create ad (PAUSED)
```
ads_create_ad
  - adset_id: from step 3
  - creative: image/video + copy + headline + CTA
  - status: PAUSED
```

**Step 5**: Full review before activation
- Check all levels in Ads Manager UI
- Verify pixel is attached to ad set
- Verify destination URL is correct and loads
- Verify creative and copy look correct in preview

**Step 6**: Activate (set top-level campaign to ACTIVE only after review)

---

## 12. PERFORMANCE TRACKING & KPIs

### Core KPIs by Campaign Objective

| Objective | Primary KPI | Secondary KPIs |
|---|---|---|
| Traffic | CTR (Link), CPC | Reach, Frequency, Landing Page Views |
| Leads | CPL (Cost per Lead) | Lead volume, Lead quality, Form completion rate |
| Sales | ROAS, CPA | Add-to-cart rate, Checkout initiation, Purchase volume |
| Awareness | CPM, Reach | Frequency, Video views, Brand lift |

### Reporting Cadence
- **Daily** (launch week): Check spend, CTR, any disapprovals
- **Weekly**: Full performance review â€” CTR, CPM, CPL/CPA, ROAS, frequency
- **Monthly**: Strategic review â€” winners vs. losers, budget reallocation, new creative planning

### When to Intervene
| Signal | Action |
|---|---|
| CTR < 0.5% on cold campaigns | Test new hook / creative |
| CPM rising week-over-week | Audience fatigued â€” refresh creative or expand audience |
| Frequency > 5 | Expand audience or pause ad set |
| Ad in "Learning Limited" status | Consolidate ad sets or increase budget |
| Spend depleting with zero conversions | Pause immediately, review pixel and landing page |
| ROAS < break-even | Pause ad set, investigate (creative? audience? landing page?) |

### Using MCP for Reporting
```
ads_get_ad_entities â€” pull campaign/ad set/ad performance
ads_insights_performance_trend â€” analyze trends over time
ads_insights_anomaly_signal â€” detect unusual patterns
ads_insights_auction_ranking_benchmarks â€” see how ads perform vs. benchmarks
ads_get_opportunity_score â€” get Meta's recommendations
```

---

## 13. EXTERNAL CAMPAIGN DOCUMENTATION

### Per-Campaign Document (create in Google Drive for each site)

Store in the site's designated Drive folder. Document should include:

**Campaign Brief**
- Campaign name (per naming convention)
- Objective and KPI targets
- Budget (daily, total)
- Start date / end date / ongoing
- Ad Account ID
- Pixel ID

**Audience Definition**
- Cold audience description
- Retargeting audiences and window
- Exclusions applied

**Creative Log**
| Ad Name | Format | Angle | Status | CTR | CPM | Notes |
|---|---|---|---|---|---|---|
| Seraphim-Video-Story-A | Video 4:5 | Origin Story | Active | 1.8% | $8.20 | Top performer |
| Seraphim-Image-Product-B | Image 1:1 | Product Shot | Paused | 0.4% | $12.00 | Low CTR |

**Results Tracker**
- Weekly snapshot of: Spend, Impressions, CTR, CPM, Leads/Sales, CPA/CPL, ROAS
- Notes on what changed each week

**Decisions Log**
- Date / decision / reason
- e.g. "2026-05-10: Paused ad set 2 â€” frequency reached 7, CTR dropped to 0.3%"

**Creative Archive**
- Link to Google Drive folder with all assets
- Retired creatives marked "Archive" â€” never deleted

---

## 14. PRE-CAMPAIGN INTAKE â€” QUESTIONS TO ASK

Before creating any campaign, gather all of the following. Ask these in natural conversation (not all at once).

### Account & Brand
1. Which site/brand is this for? (to select correct ad account)
2. What is the Facebook Page name/ID to use?
3. Is the Pixel installed and verified on this site?
4. Is CAPI (server-side tracking) set up? If not, is this blocking launch?

### Campaign Goal
5. What is the **primary objective**? (traffic / leads / sales / awareness)
6. What is the **specific conversion event** we're optimizing for? (purchase, lead form submission, contact page visit, etc.)
7. What does **success look like in numbers**? (e.g., CPL under $10, ROAS above 3x, 50 leads/month)

### Audience
8. Who is the **target customer**? (demographics, psychographics, pain points)
9. Are we targeting **cold, warm, or retargeting** audiences â€” or all three?
10. What countries/regions/cities?
11. Do we have an **existing customer list** to upload for LAL or exclusions?
12. Are there any audiences to **exclude**? (competitors, existing customers, irrelevant demographics)

### Creative
13. What **product or offer** is being promoted?
14. What is the **main message / hook**? What transformation or benefit do we lead with?
15. Do we have **existing creative assets** (images, videos, UGC)? Or do we need to generate them?
16. Are there any **compliance restrictions**? (health claims, financial claims, regulated categories)
17. What **tone** â€” inspirational / educational / direct response / storytelling?

### Budget & Timeline
18. What is the **daily or monthly budget**?
19. Is there a **hard end date**, or is this ongoing?
20. Is there a **promotional deadline** (sale, event, launch) that affects urgency?

### Landing Page & Funnel
21. What **URL** do ads link to?
22. Is the landing page **optimized for the conversion event**? (fast load, clear CTA, mobile-friendly)
23. Is there a **thank-you page** with a Pixel event firing on it?

---

## 15. SAFETY GUARDRAILS (NON-NEGOTIABLE)

### The Golden Rule: PAUSE, Never Delete

> **Never delete campaigns, ad sets, ads, audiences, or pixels.** Meta's algorithm learns from historical data attached to every object. Deleted objects lose their optimization history forever. Paused objects retain it.

```
CORRECT:  ads_activate_entity(status: PAUSED) on underperforming campaigns/ad sets/ads
INCORRECT: Any delete operation on live or historical campaign entities
```

### Additional Safety Rules

| Rule | Why |
|---|---|
| Always create campaigns in **PAUSED** status | Prevents accidental spend before review |
| Never increase budget by more than **20% at a time** | Larger jumps reset the Learning Phase |
| Never run campaigns without a **verified Pixel** | No conversion data = no optimization |
| Never edit targeting, creative, or budget simultaneously | Isolate variables so you know what changed performance |
| Never touch campaigns in **Learning Phase** (first 7 days / ~50 events) | Edits extend or restart learning |
| Keep **account spending limit** set in billing | Prevents runaway spend from bugs or errors |
| Always **preview ads** before activating | Catches broken URLs, wrong pages, copy errors |
| Never use **personal ad accounts** for business campaigns | No access controls, billing risk |
| **Document every change** in the campaign's Decisions Log | Creates audit trail, enables learning over time |
| For special ad categories (housing, credit, employment, political) â€” **declare them** | Non-declared special categories can cause account suspension |

### Account Health Rules
- Maintain **ad account policy compliance** â€” avoid prohibited con
