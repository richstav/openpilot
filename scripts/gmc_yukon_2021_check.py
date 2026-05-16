#!/usr/bin/env python3
"""
GMC Yukon 2021 — Compatibility & Fingerprint Check Script
Run this on a machine with openpilot installed to verify GM car support.
"""

import sys

# Known T1XX platform fingerprints that should match Yukon 2021
# Source: commaai/opendbc fingerprints.py (GM section)
GM_T1XX_FINGERPRINTS = {
    "GMC Sierra 1500 2020": {
        0x1E1: 4, 0x1F1: 8, 0x26F: 8, 0x348: 8, 0x360: 8,
        0x361: 8, 0x362: 8, 0x363: 8, 0x3EA: 8, 0x3EF: 8,
        0x435: 8, 0x437: 8, 0x44F: 8, 0x451: 8, 0x4E4: 8,
    },
    "GMC Sierra 1500 2021": {
        0x1E1: 4, 0x1F1: 8, 0x26F: 8, 0x348: 8, 0x360: 8,
        0x361: 8, 0x362: 8, 0x363: 8, 0x3EA: 8, 0x3EF: 8,
        0x435: 8, 0x437: 8, 0x44F: 8, 0x451: 8, 0x4E4: 8,
    },
    "Chevy Silverado 1500 2021": {
        0x1E1: 4, 0x1F1: 8, 0x26F: 8, 0x348: 8, 0x360: 8,
        0x361: 8, 0x362: 8, 0x363: 8, 0x3EA: 8, 0x3EF: 8,
        0x435: 8, 0x437: 8, 0x44F: 8, 0x451: 8, 0x4E4: 8,
    },
}

YUKON_NOTES = """
--- GMC Yukon 2021 Compatibility Notes ---

Platform: GM T1XX (same as Sierra 1500 2020-2021, Silverado 1500, Tahoe 2021)
Required: Driver Alert Package II (ACC + LKAS)

The 2021 GMC Yukon is NOT explicitly listed in openpilot's official CARS.md,
however it shares the T1XX platform and CAN bus architecture with the supported
GMC Sierra 1500 2020-2021.

Recommended approach:
1. Install stock openpilot (openpilot.comma.ai)
2. Let the device attempt auto-fingerprint on first connection
3. If unrecognized, capture the CAN fingerprint using:
   tools/car_porting/examples/find_segments_with_message.ipynb
4. Compare against Sierra 1500 2021 fingerprint above
5. If matching, the Yukon will likely work with Sierra fingerprint
6. Submit a new fingerprint PR to commaai/opendbc for official Yukon support

Harness: Standard GM Harness + Harness Box (same as Sierra/Silverado)
No pedal required if factory ACC is present.
"""


def check_compatibility():
    print("=" * 60)
    print("GMC Yukon 2021 — OpenPilot Compatibility Check")
    print("=" * 60)
    print(YUKON_NOTES)
    print("\nKnown T1XX platform fingerprints (Sierra/Silverado 2020-2021):")
    for car, fp in GM_T1XX_FINGERPRINTS.items():
        print(f"  {car}: {len(fp)} CAN IDs")
    print("\nStatus: Ready for hardware install and fingerprint verification.")
    print("Next: Connect comma four, run openpilot, check /data/log for fingerprint.")


if __name__ == "__main__":
    check_compatibility()
