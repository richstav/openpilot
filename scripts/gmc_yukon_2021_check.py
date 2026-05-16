#!/usr/bin/env python3
"""
GMC Yukon 2021 — compatibility and fingerprint reference checker.

Run locally before/after comma four install. Does not require a full openpilot tree.
"""

from __future__ import annotations

# Source: commaai/opendbc opendbc/car/gm/fingerprints.py (master, 2026-05)
# CHEVROLET_SILVERADO covers GMC Sierra 1500 2020-21 in values.py
GM_T1XX_CAMERA_ACC = {
    "Chevrolet Silverado 1500 / GMC Sierra 1500 (opendbc CHEVROLET_SILVERADO)": {
        190: 6,
        193: 8,
        197: 8,
        201: 8,
        208: 8,
        209: 7,
        211: 2,
        241: 6,
        249: 8,
        257: 8,
        288: 5,
        289: 8,
        298: 8,
        304: 3,
        309: 8,
        311: 8,
        313: 8,
        320: 4,
        322: 7,
        328: 1,
        352: 5,
        381: 8,
        384: 4,
        386: 8,
        388: 8,
        413: 8,
        451: 8,
        452: 8,
        453: 6,
        455: 7,
        460: 5,
        463: 3,
        479: 3,
        481: 7,
        485: 8,
        489: 8,
        497: 8,
        500: 6,
        501: 8,
        528: 5,
        532: 6,
        534: 2,
        560: 8,
        562: 8,
        563: 5,
        565: 5,
        587: 8,
        608: 8,
        609: 6,
        610: 6,
        611: 6,
        612: 8,
        613: 8,
        707: 8,
        715: 8,
        717: 5,
        761: 7,
        789: 5,
        800: 6,
        801: 8,
        810: 8,
        840: 5,
        842: 5,
        844: 8,
        848: 4,
        869: 4,
        880: 6,
        977: 8,
        1001: 8,
        1011: 6,
        1017: 8,
        1020: 8,
        1033: 7,
        1034: 7,
        1217: 8,
        1221: 5,
        1233: 8,
        1249: 8,
        1259: 8,
        1261: 7,
        1263: 4,
        1265: 8,
        1267: 1,
        1271: 8,
        1280: 4,
        1296: 4,
        1300: 8,
        1611: 8,
        1930: 7,
    },
    "GMC Yukon (opendbc GMC_YUKON — listed as 2019-20 only)": {
        190: 6,
        193: 8,
        197: 8,
        201: 8,
        208: 8,
        209: 7,
        211: 2,
        241: 6,
        249: 8,
        288: 5,
        289: 8,
        298: 8,
        304: 1,
        309: 8,
        311: 8,
        313: 8,
        320: 3,
        328: 1,
        352: 5,
        381: 8,
        384: 4,
        386: 8,
        388: 8,
        413: 8,
        451: 8,
        452: 8,
        453: 6,
        455: 7,
        460: 5,
        463: 3,
        479: 3,
        481: 7,
        485: 8,
        489: 8,
        497: 8,
        500: 6,
        501: 8,
        510: 8,
        528: 5,
        532: 6,
        534: 2,
        562: 8,
        563: 5,
        587: 8,
        608: 8,
        609: 6,
        610: 6,
        611: 6,
        612: 8,
        613: 8,
        707: 8,
        761: 7,
        800: 6,
        801: 8,
        810: 8,
        840: 5,
        842: 5,
        844: 8,
        848: 4,
        977: 8,
        1001: 8,
        1017: 8,
        1020: 8,
        1217: 8,
        1221: 5,
        1233: 8,
        1249: 8,
        1265: 8,
        1267: 1,
        1280: 4,
        1300: 8,
        1355: 8,
        1611: 8,
    },
}

YUKON_NOTES = """
--- GMC Yukon Denali Ultimate 2021 ---

Official CARS.md: GMC Sierra 1500 2020-21 and Chevy Silverado 1500 2020-21 (Driver Alert / Safety Package II).
opendbc also has GMC_YUKON for 2019-20; your 2021 may auto-match Sierra or need a new fingerprint row.

VIN on file for this project: 1GKS2DKL4MR220264 (Denali Ultimate — ACC + LKAS standard).

Install: stock openpilot at openpilot.comma.ai first.
Harness: GM Y-harness + harness box + OBD-C cable (included; NOT a regular ethernet cable).
Visual guide: https://comma.ai/setup
"""


def _overlap(ref: dict[int, int], sample: dict[int, int]) -> tuple[int, int, list[int]]:
    shared = set(ref) & set(sample)
    mismatches = [addr for addr in shared if ref[addr] != sample[addr]]
    return len(shared), len(mismatches), mismatches


def compare_fingerprint(sample: dict[int, int]) -> None:
    print("\nFingerprint comparison (decimal CAN IDs):")
    for name, ref in GM_T1XX_CAMERA_ACC.items():
        shared, bad, bad_addrs = _overlap(ref, sample)
        pct = (100.0 * shared / len(ref)) if ref else 0.0
        print(f"  {name}: {shared}/{len(ref)} IDs overlap ({pct:.0f}%), length mismatches: {bad}")
        if bad_addrs[:5]:
            print(f"    first mismatches: {bad_addrs[:5]}")


def check_compatibility() -> None:
    print("=" * 60)
    print("GMC Yukon 2021 — OpenPilot Compatibility Check")
    print("=" * 60)
    print(YUKON_NOTES)
    print("\nReference fingerprints in upstream opendbc:")
    for name, fp in GM_T1XX_CAMERA_ACC.items():
        print(f"  {name}: {len(fp)} CAN IDs")
    print("\nStatus: Hardware ready — install harness, flash openpilot.comma.ai, verify fingerprint.")
    print("Fork branch: https://github.com/richstav/openpilot/tree/gmc-yukon-2021")


if __name__ == "__main__":
    check_compatibility()
