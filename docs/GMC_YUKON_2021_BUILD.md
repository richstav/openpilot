# GMC Yukon Denali 2021 — OpenPilot Build Guide

## Vehicle Profile (Confirmed)
| Field | Value |
|---|---|
| **Owner** | Rishi Srivastava |
| **Vehicle** | 2021 GMC Yukon Denali Ultimate |
| **VIN** | `1GKS2DKL4MR220264` |
| **Platform** | GM T1XX (shared with Sierra 1500, Silverado 1500, Tahoe 2021) |
| **Trim** | Denali Ultimate (top trim — includes Driver Alert Package II standard) |
| **OnStar** | Active — Connected by OnStar Canada |

### VIN Decode — `1GKS2DKL4MR220264`
| Position | Value | Meaning |
|---|---|---|
| 1 | `1` | USA-manufactured |
| 2–3 | `GK` | General Motors (GMC) |
| 4 | `S` | SUV / Multipurpose |
| 5 | `2` | Yukon |
| 6 | `D` | Denali |
| 7 | `K` | Engine: 6.2L EcoTec3 V8 |
| 8 | `L` | GVWR Class |
| 9 | `4` | Check digit |
| 10 | `M` | Model year: **2021** |
| 11 | `R` | Assembly plant: Arlington, TX |
| 12–17 | `220264` | Sequential serial number |

> **Key confirmation:** Denali Ultimate trim includes **Driver Alert Package II** as standard equipment, which bundles **ACC (Adaptive Cruise Control)** and **LKAS (Lane Keep Assist System)** — both required for openpilot.

---

## Hardware Required

| Component | Notes |
|---|---|
| comma four | $999 @ comma.ai/shop |
| GM Harness + Harness Box | Standard GM harness (2x9 pin box) from BearTech or Comma |
| comma pedal | **NOT required** — Denali Ultimate has factory ACC |
| Ethernet cable (11ft+) | Avoid flat/noodle cables |
| BearTech Slidemount C4 | Windshield mount for comma four |

> **Harness Note:** 2021 GMC Yukon Denali uses the **standard GM Harness & Harness Box** (NOT ASCM, NOT SDGM).
> Reference: https://docs.innoisle.com/car-make/gm-vehicles

---

## Software Recommendation

### ✅ Option 1: Official openpilot (Best Starting Point)
- Install URL: `openpilot.comma.ai`
- Branch: `release-mici` (comma four)
- 2021 GMC Sierra 1500 Denali is officially supported; Yukon Denali shares identical T1XX CAN bus
- **Prediction:** The Yukon will auto-fingerprint as Sierra 1500 Denali 2021 on first boot

### Option 2: SunnyPilot Fork
- Adds M.A.D.S. (Modified Assistive Driving Safety)
- Independent steering/speed toggle — steering stays on when you adjust speed
- Install: https://smiskol.com/fork/sunnyhaibin/sunnypilot
- **Recommended if** you want more control over when openpilot engages

### Option 3: FrogPilot Fork
- Advanced features, experimental longitudinal control
- Install: https://smiskol.com/fork/FrogAi/FrogPilot

---

## CAN Bus / Fingerprint

The 2021 GMC Yukon Denali shares the GM T1XX platform with:
- GMC Sierra 1500 Denali 2020–2021 ✅ (officially supported)
- Chevy Silverado 1500 High Country 2020–2021 ✅ (officially supported)
- Chevy Tahoe/Suburban 2021 ✅ (same platform)

**Key fingerprint files in openpilot (opendbc submodule):**
- `opendbc/car/gm/fingerprints.py` — vehicle fingerprints
- `opendbc/car/gm/values.py` — CAR enum and feature flags
- `opendbc/car/gm/carstate.py` — CAN signal parsing
- `opendbc/car/gm/interface.py` — car interface & speed/steering limits

---

## Installation Steps

1. ✅ VIN confirmed — Denali Ultimate has ACC + LKAS standard
2. Order: **comma four** + **GM harness** + **harness box** from [comma.ai](https://comma.ai/shop) or [BearTech](https://docs.innoisle.com)
3. Mount comma four on windshield (BearTech Slidemount C4 recommended for clean install)
4. Plug harness into rearview mirror housing connector
5. Power on comma four → enter setup → enter software URL
6. Use `openpilot.comma.ai` for stock OR a fork URL for enhanced features
7. Complete calibration drive (highway preferred, >15 mins)
8. Check `/data/log` for fingerprint match if vehicle not auto-recognized

---

## Community Resources

- comma.ai Discord: https://discord.comma.ai → `#gm` channel
- OPGM repo (archived, merged to mainline): https://github.com/opgm/openpilot-1
- BearTech GM Vehicle Guide: https://docs.innoisle.com/car-make/gm-vehicles
- commaai/opendbc (fingerprints): https://github.com/commaai/opendbc
- openpilot supported cars: https://docs.comma.ai/CARS/

---

## Status

- [x] VIN confirmed: `1GKS2DKL4MR220264`
- [x] Trim confirmed: Denali Ultimate (ACC + LKAS standard)
- [x] Platform confirmed: GM T1XX
- [x] Harness type confirmed: Standard GM Harness + Box
- [ ] Hardware ordered
- [ ] comma four installed
- [ ] First boot fingerprint test
- [ ] If unrecognized: capture CAN fingerprint and compare vs Sierra 1500 Denali 2021
- [ ] If fingerprint differs: submit PR to commaai/opendbc for official Yukon Denali 2021 support
