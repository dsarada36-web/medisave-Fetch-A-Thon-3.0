"""Run the savings engine without Agentverse.

Usage:
    python demo.py "Telma 40, Atorva 10, Pan 40" 1850
"""

from __future__ import annotations

import sys

from medicine import assess, build_sheet


def main() -> None:
    prescription = sys.argv[1] if len(sys.argv) > 1 else "Telma 40, Atorva 10, Pan 40"
    raw_bill = sys.argv[2] if len(sys.argv) > 2 else "1850"

    try:
        bill = int(float(raw_bill.replace(",", "").replace("₹", "")))
    except ValueError:
        bill = 0

    print(build_sheet(assess(prescription, bill)))


if __name__ == "__main__":
    main()
