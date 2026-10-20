# MediSave

> **A prescription in. A savings sheet out.** Same molecules, visible prices, nearest Jan Aushadhi Kendra.

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

**Status:** `v0` — savings engine, 20-drug map and 5 tests. The ACP agent, cards, PDF and Kendra locator are the next commits.
**Event:** Fetch-A-Thon 3.0 · 24 October 2026 · Presidency University, Bengaluru
**Team:** `fetchathon3.0-1624` — Nikhil (lead), Guvvala Yella Reddy, Dwarak, Dakshath Iyengar

> **Price transparency, not medical advice.** Confirm any change with your doctor or pharmacist.

---

## The 30-second pitch

A family buying three chronic medicines can spend **₹1,850 a month**. The same molecules at Jan Aushadhi prices cost **₹620**.

That gap is not medicine. It is information.

MediSave is an ASI:One agent that turns a prescription into a savings sheet: brand → molecule → indicative price → monthly and annual saving → nearest Kendra → questions for the doctor.

**One chat. One sheet. No app.**

---

## The problem

- The brand is not the medicine. The molecule is.
- Jan Aushadhi exists, but the brand-to-molecule map is invisible.
- Even when people know, they do not know the fair price or the nearest Kendra.
- The result: households overpay every month for the same active ingredient.

---

## The test case

| Brand | Molecule | Brand / month | Jan Aushadhi / month | Saving |
|---|---|---|---|---|
| Telma 40 | Telmisartan 40 mg | ₹700 | ₹240 | ₹460 |
| Atorva 10 | Atorvastatin 10 mg | ₹600 | ₹200 | ₹400 |
| Pan 40 | Pantoprazole 40 mg | ₹550 | ₹180 | ₹370 |
| **Total** | | **₹1,850** | **₹620** | **₹1,230 / month** |

**Annual saving: ₹14,760.** Prices are indicative demo values, not market quotes.

---

## What MediSave does

1. **Read** the prescription — brand, strength, dose.
2. **Map** each brand to its molecule.
3. **Price** it against the Jan Aushadhi indicative price.
4. **Save** — monthly and annual.
5. **Locate** the nearest Kendra by PIN. *(next)*
6. **Document** — a savings-sheet PDF with questions for the doctor. *(next)*

---

## Demo in 30 seconds

No install, no API key, no Agentverse. Standard library only.

```bash
python demo.py "Telma 40, Atorva 10, Pan 40" 1850
```

```text
Brand total: ₹1,850 / month
Jan Aushadhi total: ₹620 / month
Monthly saving: ₹1,230
Annual saving: ₹14,760
```

The engine is deterministic: the saving is computed, not generated.

---

## Architecture

```text
ASI:One chat
   │  Agent Chat Protocol 0.3.0
   ▼
medisave-router (uAgent)
   ├── RxScout      → brand, strength, dose
   ├── PriceMap     → molecule + indicative price
   ├── SavingsSmith → monthly / annual saving
   └── case_file    → savings sheet PDF
```

### Agent roles

Three reasoning agents plus the document renderer.

| Agent | Job | Input | Output | Status |
|---|---|---|---|---|
| **RxScout** | Parse the prescription | Free text or form | Brand, strength, dose | v1 |
| **PriceMap** | Brand → molecule → price | Drug map | Price comparison | Engine in `medicine.py` |
| **SavingsSmith** | Compute and render the saving | Price table + bill | Savings sheet | Engine in `medicine.py` |
| **case_file** | Produce the PDF | Savings sheet | PDF / HTML | v1 |

### Repository layout

```text
medisave/
├─ medicine.py              # savings engine: parse, match, assess, build sheet
├─ demo.py                  # CLI demo, no Agentverse required
├─ data/drugs.json          # 20-drug brand → molecule map
├─ tests/test_medicine.py   # 5 tests
├─ docs/overview.md         # full overview + roadmap
├─ docs/carousel.html       # 5-slide LinkedIn carousel
├─ docs/linkedin-posts.md   # Day 1/2/3 copy
├─ docs/repo-structure.md   # publishing guide
├─ README.md
├─ requirements.txt         # v1 ACP/Agentverse layer
├─ requirements-dev.txt     # pytest
├─ conftest.py
├─ .env.example
├─ .gitignore
└─ LICENSE
```

### v1 target

```text
agent.py          # ACP router + state machine
cards.py          # form / savings / review cards
docgen.py         # PDF renderer
data/kendras.json # PIN → nearest Jan Aushadhi Kendra
```

---

## What works today

| Layer | Status |
|---|---|
| Savings engine | ✅ |
| 20-drug brand → molecule map | ✅ |
| Monthly / annual saving | ✅ |
| 5 tests | ✅ |
| CLI demo | ✅ |
| ACP agent on Agentverse | 🔜 next |
| Form / savings / review cards | 🔜 next |
| Savings-sheet PDF | 🔜 next |
| Jan Aushadhi Kendra locator | 🔜 next |
| ASI1 extraction from free text | 🔜 next |

---

## Why an agent, not a calculator

A price calculator is a form. MediSave has to:

- parse a messy prescription,
- map a brand to a molecule,
- compute the gap,
- find a Kendra,
- produce a document.

The workflow is the product. The conversation is the interface.

---

## Fetch.ai stack

| Component | Use | Status |
|---|---|---|
| **Agentverse** | Registration, mailbox, discovery | Next |
| **Agent Chat Protocol 0.3.0** | ASI:One compatibility | Next |
| **ASI1** | Extract facts from free text | Next |
| **ASI:One Interactive Cards** | Form, savings, review | Next |
| **Payment Protocol** | Paid document pack / review | Roadmap |

---

## Impact

| Way it helps | What changes |
|---|---|
| **Money** | ₹14,760 a year in the test case. |
| **Access** | The nearest Kendra, not just a generic price. |
| **Agency** | Questions to ask the doctor, not blind switching. |
| **Trust** | Transparent prices and a visible disclaimer. |
| **Reach** | The same agent can serve a household, a clinic or an ASHA worker. |

---

## Safety boundary

MediSave is a **price-transparency tool**, not a doctor.

It does **not** diagnose, prescribe, recommend switching, check drug interactions, process insurance claims, or replace a pharmacist. Prices are indicative and may vary by city, pack size and date.

Every sheet ends with: **confirm with your doctor or pharmacist before acting.**

---

## Roadmap

### Hackathon build — 24 October

- ACP agent on Agentverse.
- Form / savings / review cards.
- Savings-sheet PDF.
- Kendra locator by PIN.
- One end-to-end demo in ASI:One.

### Next 30 days

- 100-drug map and state price variations.
- Family profiles — one household, multiple prescriptions.
- Refill reminders and price alerts.
- Hindi / Kannada / Tamil.
- Prescription photo / OCR.
- “Share with doctor” on WhatsApp.

### Next 90 days

- ASHA / health-worker mode.
- PM-JAY / state scheme integration.
- Jan Aushadhi stock and availability.
- Pharmacy price comparison.
- Doctor / pharmacist review tier.
- Clinic / NGO API.

---

## Tests

```bash
pip install -r requirements-dev.txt
pytest -q
```

```text
5 passed
```

| Test | What it proves |
|---|---|
| `test_find_three_brands` | The parser recognises brand names. |
| `test_savings_for_test_case` | ₹1,850 → ₹620; ₹1,230/month; ₹14,760/year. |
| `test_no_match_returns_zero` | No false positives. |
| `test_bill_total_overrides_dataset_sum` | Uses the user’s actual bill. |
| `test_same_molecule_is_deduped` | No double counting. |

---

## Judge highlights

- **On-brief:** ACP, Agentverse, ASI:One and Interactive Cards are the design.
- **A real artifact:** the build delivers a savings-sheet PDF, not a chat reply.
- **Deterministic core:** the saving is computed; the model cannot invent arithmetic.
- **A safety boundary:** price transparency, not medical advice.
- **Proof:** 20-drug map, 5 tests, a 30-second demo.

---

## Team

Built at **Fetch-A-Thon 3.0** by team `fetchathon3.0-1624`.

Nikhil · Guvvala · Dwarak · Dakshath

Presidency University, Bengaluru · 24 October 2026.

---

## License

MIT — see [LICENSE](LICENSE).
