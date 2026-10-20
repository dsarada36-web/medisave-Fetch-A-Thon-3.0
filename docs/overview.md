# MediSave — total overview

## In one line

**A prescription in. A savings sheet out. Same molecules, visible prices.**

## For friends — 30 seconds

A family buying three chronic medicines can spend ₹1,850 a month. The same molecules at Jan Aushadhi prices cost ₹620. Most people never see that gap because the brand hides the molecule.

MediSave is an AI agent on ASI:One. You describe the prescription; it maps each brand to its molecule, shows the indicative Jan Aushadhi price, computes the monthly and annual saving, finds the nearest Kendra, and produces a savings sheet you can take to your doctor.

It is **price transparency, not medical advice**.

## The problem

- The brand is not the medicine. The molecule is.
- Jan Aushadhi stores exist, but people do not know which brand maps to which molecule.
- Even when they know, they do not know the fair price, the nearest Kendra, or what to ask the doctor.
- The result: households overpay every month for the same active ingredient.

## What MediSave does

1. **Reads the prescription** — brand, strength, dose.
2. **Maps brand → molecule** — a curated drug map.
3. **Shows the indicative price** — brand vs Jan Aushadhi.
4. **Computes the saving** — monthly and annual.
5. **Finds the nearest Kendra** — by PIN code.
6. **Produces a savings sheet** — with questions for the doctor and a visible disclaimer.

## How it works

```
ASI:One chat
   │  Agent Chat Protocol 0.3.0
   ▼
MediSave router
   ├── RxScout       → parses the prescription
   ├── PriceMap      → brand → molecule → price
   ├── SavingsSmith  → monthly / annual saving
   └── KendraScout   → nearest Jan Aushadhi Kendra
                        ↓
                 savings sheet PDF
```

- **Agentverse** for discovery and the mailbox.
- **ASI:One Interactive Cards** for the form, the savings table and the review.
- **ASI1** for extracting facts from a messy prescription.
- **Deterministic code** for the arithmetic: the saving is computed, not generated.

## Why it matters

| Way it helps | What it changes |
|---|---|
| Money | A family sees the monthly and annual gap before the next refill. |
| Access | The nearest Kendra, not just a generic price. |
| Agency | Three questions to ask the doctor, instead of blind switching. |
| Trust | Transparent prices and a “not medical advice” boundary. |
| Reach | The same agent can serve a household, a clinic, or an ASHA worker. |

## What is built today

- v0 savings engine (`medicine.py`) with a 20-drug brand → molecule map.
- Five tests.
- A `demo.py` that prints the savings sheet.
- The ACP agent, cards, PDF and Kendra locator are the next commits.

## Feature roadmap

### Hackathon build (24 October)

| Feature | Why |
|---|---|
| Prescription form card | The only input the user needs |
| Savings card | The number that wins the demo |
| Review card | Confirm before the sheet |
| Savings-sheet PDF | The artifact judges remember |
| Kendra locator | Turns a price into an action |
| Doctor questions | Safe, useful, differentiated |

### Next 30 days

| Feature | Why |
|---|---|
| 100-drug map + state price variations | Coverage beyond the demo |
| Family profiles | Household savings, not one prescription |
| Refill reminders | The saving repeats every month |
| Hindi / Kannada / Tamil | Reach beyond English |
| Prescription photo / OCR | Remove typing |
| “Share with doctor” on WhatsApp | The sheet leaves the app |

### Next 90 days

| Feature | Why |
|---|---|
| ASHA / health-worker mode | One worker, many households |
| PM-JAY / state scheme integration | Coverage alongside savings |
| Jan Aushadhi stock and availability | “Near” is not enough if it is out of stock |
| Pharmacy price comparison | More than one benchmark |
| Doctor/pharmacist review tier | Human confirmation, paid |
| Clinic / NGO API | B2B distribution |

## What we will not build

- A symptom checker or diagnosis.
- “Switch this medicine” or “stop this drug.”
- A drug-interaction checker without a clinical corpus.
- Insurance claim processing in v1.
- A pharmacy marketplace.

The boundary is the product: **price transparency, not medical advice.**

## Team

Fetch-A-Thon 3.0 · team `fetchathon3.0-1624` · Presidency University, Bengaluru · 24 October 2026.
