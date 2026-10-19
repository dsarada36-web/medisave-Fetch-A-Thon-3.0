"""MediSave savings engine.

Pure Python, no network. The drug map is a curated demo dataset; prices are
indicative and this is not medical advice.
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from pathlib import Path

DATA_PATH = Path(__file__).resolve().parent / "data" / "drugs.json"


def load_drugs() -> list[dict]:
    with DATA_PATH.open(encoding="utf-8") as fh:
        return json.load(fh)["drugs"]


DRUGS = load_drugs()


def normalize(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", str(value).lower()).strip()


def _matches(drug: dict, text: str) -> bool:
    haystack = normalize(text)
    if not haystack:
        return False
    brand = normalize(drug["brand"])
    molecule = normalize(drug["molecule"])
    return bool((brand and brand in haystack) or (molecule and molecule in haystack))


def find_drugs(prescription: str) -> list[dict]:
    found: list[dict] = []
    seen: set[tuple[str, str]] = set()
    for drug in DRUGS:
        if not _matches(drug, prescription):
            continue
        key = (normalize(drug["molecule"]), normalize(drug["strength"]))
        if key in seen:
            continue
        seen.add(key)
        found.append(drug)
    return found


@dataclass
class SavingsItem:
    brand: str
    molecule: str
    strength: str
    brand_price: int
    generic_price: int

    @property
    def saving(self) -> int:
        return max(self.brand_price - self.generic_price, 0)


@dataclass
class Savings:
    items: list[SavingsItem]
    brand_total: int
    generic_total: int
    monthly_saving: int
    annual_saving: int


def assess(prescription: str, bill_total: int | float = 0) -> Savings:
    items = [
        SavingsItem(
            brand=drug["brand"],
            molecule=drug["molecule"],
            strength=drug["strength"],
            brand_price=int(drug["brand_price"]),
            generic_price=int(drug["generic_price"]),
        )
        for drug in find_drugs(prescription)
    ]
    if not items:
        return Savings([], 0, 0, 0, 0)

    brand_sum = sum(item.brand_price for item in items)
    generic_total = sum(item.generic_price for item in items)
    brand_total = int(bill_total) if bill_total and bill_total > 0 else brand_sum
    monthly = max(brand_total - generic_total, 0)
    return Savings(items, brand_total, generic_total, monthly, monthly * 12)


def build_sheet(result: Savings) -> str:
    if not result.items:
        return (
            "MediSave could not match any medicine in that prescription.\n"
            "Try the brand name and strength, for example: Telma 40."
        )

    lines = [
        "MEDISAVE — indicative savings sheet",
        "",
        "| Brand | Molecule | Brand / month | Jan Aushadhi / month | Saving |",
        "|---|---|---|---|---|",
    ]
    for item in result.items:
        lines.append(
            f"| {item.brand} | {item.molecule} {item.strength} | "
            f"₹{item.brand_price:,} | ₹{item.generic_price:,} | ₹{item.saving:,} |"
        )

    lines.extend(
        [
            "",
            f"Brand total: ₹{result.brand_total:,} / month",
            f"Jan Aushadhi total: ₹{result.generic_total:,} / month",
            f"Monthly saving: ₹{result.monthly_saving:,}",
            f"Annual saving: ₹{result.annual_saving:,}",
            "",
            "Prices are indicative demo values, not market quotes.",
            "This is price transparency, not medical advice.",
            "Confirm any change with your doctor or pharmacist before acting.",
        ]
    )
    return "\n".join(lines)
