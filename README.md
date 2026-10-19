# MediSave

> A prescription in. A savings sheet out. Same molecules, visible prices, nearest Jan Aushadhi Kendra.

![tag:innovationlab](https://img.shields.io/badge/innovationlab-3D8BD3)
![tag:hackathon](https://img.shields.io/badge/hackathon-5F43F1)

**Status:** v0 — savings engine, 20-drug dataset and tests. The ACP agent, ASI:One cards and PDF are the next commits.
**Event:** Fetch-A-Thon 3.0 · 24 Oct 2026 · Presidency University, Bengaluru
**Team:** `fetchathon3.0-1624` — Nikhil (lead), Guvvala Yella Reddy, Dwarak, Dakshath Iyengar

> This is price transparency, **not medical advice**. Confirm any change with your doctor or pharmacist.

## The problem

A family buying three chronic medicines can spend ₹1,850 a month on brands whose generic equivalents cost ₹620. The molecule is the medicine; the brand is the packaging. Jan Aushadhi stores exist, but most people do not know which brand maps to which molecule, what the fair price is, or where the nearest Kendra is.

MediSave turns a prescription into that missing sheet.

## The test case

| Brand | Molecule | Brand / month | Jan Aushadhi / month | Saving |
|---|---|---|---|---|
| Telma 40 | Telmisartan 40 mg | ₹700 | ₹240 | ₹460 |
| Atorva 10 | Atorvastatin 10 mg | ₹600 | ₹200 | ₹400 |
| Pan 40 | Pantoprazole 40 mg | ₹550 | ₹180 | ₹370 |
| **Total** | | **₹1,850** | **₹620** | **₹1,230 / month** |

Annual saving: **₹14,760**. Prices are indicative demo values, not market quotes.

## What it does

1. Parses a prescription into brand, molecule and strength.
2. Matches each brand to its molecule in a curated 20-drug map.
3. Shows the brand price, the Jan Aushadhi indicative price and the saving.
4. Computes monthly and annual savings.
5. (Next) Finds the nearest Jan Aushadhi Kendra by PIN code.
6. (Next) Produces a savings-sheet PDF with questions for the doctor.

## Try it

The v0 engine uses only the Python standard library:

```bash
python demo.py "Telma 40, Atorva 10, Pan 40" 1850
```

```bash
pip install -r requirements-dev.txt
pytest -q
```

Expected: 5 tests passing.

`requirements.txt` lists the ACP/Agentverse layer for v1; it is not needed to run the v0 engine.

## Architecture (v1)

```
ASI:One chat
   │  Agent Chat Protocol 0.3.0
   ▼
medisave-router (uAgent)
   ├── prescription card  → brand, strength, monthly bill, PIN
   ├── drug_map           → brand → molecule → generic price
   ├── savings card       → monthly / annual saving
   ├── review card
   └── savings sheet PDF + nearest Jan Aushadhi Kendra
```

## Stack

- Python 3.10+
- v1: uAgents, Agentverse, Agent Chat Protocol 0.3.0, ASI:One Interactive Cards, ASI1 for extraction, ReportLab for the PDF
- Data: NPPA ceiling prices, the Jan Aushadhi product list, and a curated brand-to-molecule map

## Roadmap

- [x] 20-drug brand → molecule map
- [x] Savings engine
- [x] Tests
- [ ] ACP agent on Agentverse
- [ ] Form / savings / review cards
- [ ] Jan Aushadhi Kendra locator
- [ ] Savings-sheet PDF
- [ ] ASI1 extraction from free-text prescriptions

## Why an agent

A price calculator is a form. MediSave has to parse a messy prescription, match brands to molecules, compute the saving, find a Kendra, and produce a document — in one ASI:One conversation. The workflow is the product.

## Disclaimer

MediSave is a price-transparency tool. It does not diagnose, prescribe, recommend switching, or replace a doctor or pharmacist. Prices are indicative and may vary by city, pack size and date. Verify before acting.

## Team

Built at Fetch-A-Thon 3.0 by team `fetchathon3.0-1624`.

## License

MIT — see [LICENSE](LICENSE).
