# Repo structure and publishing

## What to push tonight

```
medisave/
├─ README.md                  ← the first screen; problem, test case, roadmap
├─ demo.py                    ← run the savings engine without Agentverse
├─ medicine.py                ← parse, match, assess, build the sheet
├─ data/drugs.json            ← 20-drug brand → molecule map
├─ tests/test_medicine.py     ← 5 tests
├─ docs/carousel.html         ← 5 slides, 1080×1350
├─ docs/linkedin-posts.md     ← Day 1/2/3 copy
├─ conftest.py
├─ requirements.txt
├─ requirements-dev.txt
├─ .env.example
├─ .gitignore
└─ LICENSE
```

## Create and push

```bash
cd medisave
git init
git add .
git commit -m "v0: savings engine, 20-drug map, tests"
```

Create a **public** repo on GitHub named `medisave`, then:

```bash
git remote add origin https://github.com/<handle>/medisave.git
git branch -M main
git push -u origin main
```

If you have the GitHub CLI:

```bash
gh repo create medisave --public --source=. --push
```

## Repo settings

- **Description:** “A prescription-to-savings agent for ASI:One. Same molecules, visible prices.”
- **Topics:** `fetchai`, `agentverse`, `asi-one`, `agentic-ai`, `hackathon`, `healthcare`, `medisave`
- **Website:** the LinkedIn post URL (after publishing)
- **Pin the repo** on your profile.

## Commit schedule

**Tonight (3 commits)**

1. `v0: savings engine, 20-drug map, tests`
2. `docs: README, test case, disclaimer`
3. `docs: carousel + LinkedIn copy`

**Tomorrow (3–5 commits)**

4. `feat: add 10 more molecules to the drug map`
5. `feat: savings sheet template`
6. `docs: update README with demo output`
7. `chore: add CI for tests`

Small, frequent commits are a visibility signal.

## README first-screen checklist

- [ ] One-liner with the number: ₹1,850 → ₹620.
- [ ] Status: v0 engine, ACP agent next.
- [ ] Test case table.
- [ ] `python demo.py ...` command.
- [ ] Architecture sketch.
- [ ] Disclaimer: price transparency, not medical advice.
- [ ] Team + event.
- [ ] Innovation Lab and hackathon badges.

## What not to do

- Do not push `.env` or keys.
- Do not claim the ACP agent is built until it is.
- Do not leave the repo named `insaf`.
- Do not publish a README that says “coming soon” with no code; the engine and tests are the proof.
