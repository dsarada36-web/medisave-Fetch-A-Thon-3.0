# MediSave — 60-second demo

**Loom:** [paste the link here]

## Run

```bash
python demo.py "Telma 40, Atorva 10, Pan 40" 1850
```

## Output

```text
MEDISAVE — indicative savings sheet

| Brand | Molecule | Brand / month | Jan Aushadhi / month | Saving |
...
Brand total: ₹1,850 / month
Jan Aushadhi total: ₹620 / month
Monthly saving: ₹1,230
Annual saving: ₹14,760
```

## What the video shows

| Time | Show | Say |
|---|---|---|
| 0:00 | Title card | “Three medicines, ₹1,850 a month. Same molecules: ₹620.” |
| 0:08 | Terminal | “This is the v0 engine — standard library only.” |
| 0:15 | Run the command | “One command, no API key, no Agentverse.” |
| 0:25 | Output totals | “₹1,230 a month, ₹14,760 a year.” |
| 0:40 | Tests | “Five tests: parser, saving, no-match, bill override, dedupe.” |
| 0:52 | README | “Price transparency, not medical advice. Repo in the description.” |

## What it proves

- The engine runs on a clean machine.
- The number is computed, not generated.
- The tests pass.
- The safety boundary is visible.
