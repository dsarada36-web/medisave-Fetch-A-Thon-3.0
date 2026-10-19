# Publish tonight — 19 October

The organizer's message: shortlisting starts now and concludes on 20 October,
with selection emails by 22 October. Visibility is the gate.

## 21:45 — create the repo

- Copy the `medisave/` folder into a new public GitHub repo named `medisave`.
- Set the description and topics from `docs/repo-structure.md`.
- Commit and push.

## 22:00 — verify the engine

```bash
python demo.py "Telma 40, Atorva 10, Pan 40" 1850
pytest -q
```

Expected: the sheet prints ₹1,850 → ₹620, and 5 tests pass.

If Python is not installed, skip this step. Do **not** claim the engine runs in
the post; say “v0 engine is in the repo” and update after it runs.

## 22:15 — README check

- First screen has the one-liner and the test case.
- Status says v0; ACP agent next.
- Disclaimer is visible.
- Badges are present.

## 22:30 — carousel

Open `docs/carousel.html` in Chrome. DevTools → 1080×1350 → capture five slides.
Or print to PDF and crop.

## 22:45 — publish Day 1

Copy the Day 1 post from `docs/linkedin-posts.md`. Attach the carousel. Put the
repo link in the post. Tag 4–5 official pages.

## 23:15 — first-hour engagement

- Ask 5 classmates to comment with a real question.
- Reply to every comment within 10 minutes.
- Do not edit the post.

## 23:30 — optional Loom

Record 45–60 seconds: run `demo.py`, show the sheet. Put the link in the first
comment. If the engine does not run, record a slide walkthrough instead and
label it a prototype.

## Tomorrow 09:30 — Day 2

Publish the Day 2 post with a screenshot or the Loom. Commit 3–5 times during
the day. Shortlisting concludes.

## Do not

- Wait for the ACP agent before posting.
- Leave the repo named Insaf.
- Tag 15 people.
- Claim medical advice or a finished agent.
- Skip the disclaimer.
