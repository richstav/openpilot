# GMC Yukon 2021 — OpenPilot Build Guide

## Vehicle Overview
- **Make/Model:** GMC Yukon 2021 (also applicable to Yukon XL 2021)
- **Platform:** GM T1XX (shared with Chevy Tahoe, Silverado, Sierra 2020-2021)
- **Required Feature:** Driver Alert Package II (includes Lane Keep Assist + ACC)

---

## Hardware Required

| Component | Notes |
|---|---|
| comma four | $999 @ comma.ai/shop |
| GM Harness + Harness Box | Standard GM harness (2x9 pin box) from BearTech or Comma |
| comma pedal (optional) | Only needed if no ACC — Yukon 2021 should have factory ACC |
| Ethernet cable (11ft+) | Avoid flat/noodle cables |

> **Harness Note:** The 2021 GMC Yukon uses the standard **GM Harness & Harness box** (NOT ASCM, NOT SDGM).  
> Reference: https://docs.innoisle.com/car-make/gm-vehicles

---

## Software / Fork

### Option 1: Official openpilot (Recommended Starting Point)
- Install URL: `openpilot.comma.ai`
- Branch: `release-mici` (comma four) or `release-tizi` (comma 3X)
- The 2021 GMC Sierra 1500 is officially supported; Yukon shares the same T1XX platform/CAN bus fingerprint.

### Option 2: SunnyPilot Fork
- Adds M.A.D.S. (Modified Assistive Driving Safety)
- Independent steering/speed control toggle
- Install: https://smiskol.com/fork/sunnyhaibin/sunnypilot

### Option 3: FrogPilot Fork
- Advanced features, experimental longitudinal
- Install: https://smiskol.com/fork/FrogAi/FrogPilot

---

## Car Fingerprint / CAN Bus

The 2021 GMC Yukon shares the GM T1XX platform with:
- GMC Sierra 1500 2020-2021 (officially supported in openpilot)
- Chevy Silverado 1500 High Country 2020-2021
- Chevy Tahoe 2021

**Key fingerprint files in openpilot (opendbc submodule):**
- `opendbc/car/gm/fingerprints.py` — vehicle fingerprints
- `opendbc/car/gm/values.py` — CAR enum and feature flags
- `opendbc/car/gm/carstate.py` — CAN signal parsing
- `opendbc/car/gm/interface.py` — car interface & limits

---

## Key Requirements for Yukon 2021

1. **Driver Alert Package II** must be equipped (includes LKAS + ACC)
2. Vehicle must have factory **Adaptive Cruise Control (ACC)**
3. **Lane Keep Assist System (LKAS)** must be present
4. The standard **GM OBD-II harness** connects near the rearview mirror

---

## Installation Steps

1. Confirm your Yukon has ACC + LKAS (check window sticker or RPO codes)
2. Order: comma four + GM harness + harness box from comma.ai or BearTech
3. Mount comma four using windshield mount (BearTech Slidemount C4 recommended)
4. Connect harness at rearview mirror housing
5. Power on comma four, enter setup
6. Enter software URL: `openpilot.comma.ai` for stock, or a fork URL
7. Complete calibration drive (highway recommended)

---

## Community Resources

- comma.ai Discord: https://discord.comma.ai (see #gm channel)
- OPGM repo (archived, merged to mainline): https://github.com/opgm/openpilot-1
- BearTech GM Guide: https://docs.innoisle.com/car-make/gm-vehicles
- Comma Wiki for GM: https://github.com/commaai/openpilot/wiki/GM
- commaai/opendbc: https://github.com/commaai/opendbc

---

## TODO / Next Steps

- [ ] Confirm Yukon 2021 fingerprint match vs Sierra 2021 in opendbc
- [ ] Verify RPO codes from VIN for ACC/LKAS presence
- [ ] Test stock openpilot on Yukon 2021 and log fingerprint
- [ ] If not recognized, submit new fingerprint PR to commaai/opendbc
- [ ] Evaluate SunnyPilot M.A.D.S. for preferred UX
