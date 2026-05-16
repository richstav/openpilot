# GMC Yukon Denali 2021 — OpenPilot Build Guide

## Vehicle Profile (Confirmed)
| Field | Value |
|---|---|
| **Owner** | Rishi Srivastava |
| **Vehicle** | 2021 GMC Yukon Denali Ultimate |
| **VIN** | `1GKS2DKL4MR220264` |
| **Platform** | GM T1XX (shared with Sierra 1500, Silverado 1500, Tahoe 2021) |
| **Trim** | Denali Ultimate — Driver Alert Package II **standard** |
| **Engine** | 6.2L EcoTec3 V8 |
| **Assembly** | Arlington, TX |
| **OnStar** | Active — Connected by OnStar Canada |

---

## Hardware Status ✔️

| Component | Status | Notes |
|---|---|---|
| comma four | ✅ **In hand** | Selected GM harness via comma.ai dropdown |
| GM Harness + Harness Box | ✅ **In hand** | Standard 2x9-pin GM harness from comma.ai |
| comma pedal | ❌ Not needed | Denali Ultimate has factory ACC |
| Windshield mount | 🔲 Recommended | BearTech Slidemount C4 or comma.ai mount |

---

## Software Choice

### ✅ Recommended: Start with Official openpilot
- **Install URL:** `openpilot.comma.ai` (enter this on comma four first boot)
- **Why:** GMC Sierra 1500 2020-21 is on [comma.ai/vehicles](https://comma.ai/vehicles); same T1XX platform as your Yukon
- **Expected behavior:** Yukon may auto-fingerprint as **GMC Sierra 1500** or **GMC Yukon** (opendbc has Yukon **2019-20**; 2021 may still match Sierra)
- **If it doesn’t fingerprint:** See CAN fingerprint section below

### Alternative: SunnyPilot (after confirming basic functionality)
- Adds **M.A.D.S.** — independent steering/speed engagement
- Install URL: `https://smiskol.com/fork/sunnyhaibin/sunnypilot`

---

## Physical Installation — Step by Step

> **Before you begin:** Park on level ground, engine OFF, key out. Do NOT turn on ignition during install.
>
> **Official visual guide (use this):** [comma.ai/setup](https://comma.ai/setup) — animated steps for GM harness + comma four.

### What’s in the GM harness kit
| Part | Purpose |
|---|---|
| Y-harness (2× grey connectors) | Inline at the forward camera / LKAS connector behind the mirror |
| Harness box | Small box with USB-C; mounts inside mirror housing |
| Comma power tap | Plugs into harness box (standby power) |
| **OBD-C cable (~1.5 ft)** | Harness box → comma four bottom USB-C (**not** a regular ethernet cable) |

### Step 1 — Remove mirror trim
Pop the plastic shroud at the base of the rearview mirror (plastic pry tool). You’ll see the grey multi-pin LKAS/camera connector.  
Reference: [comma.ai/setup](https://comma.ai/setup) → select **GMC** → harness install animation.

### Step 2 — Unplug factory camera connector
Press the **red safety tab down**, then squeeze the grey release and pull straight out.

### Step 3 — Install Y-harness inline
- One Y leg → camera module  
- Other Y leg → factory harness you unplugged  
- Adhere harness box inside the mirror cavity (adhesive on box)

### Step 4 — Connect OBD-C cable
Plug **USB-C** into the harness box. Route the short OBD-C out the **bottom** of the housing toward the windshield mount (~6″ slack).  
**Do not** route down the A-pillar — the included cable is too short. **Never** use a standard ethernet patch cable.

### Step 5 — Mount comma four
1. Clean windshield with isopropyl alcohol (behind / beside mirror, clear of tint and defrost lines)  
2. Press mount 30–60 seconds  
3. Slide comma four onto mount  
4. Plug OBD-C into the **bottom USB-C** until fully seated

### Step 6 — Reinstall trim
Tuck harness box inside; ensure OBD-C is not pinched. Snap trim back until clips engage.

### Step 7 — First boot & software
1. Ignition ON (engine off OK)  
2. WiFi → software URL: **`openpilot.comma.ai`**  
3. Wait for download (~5–15 min)  
4. Highway drive 15+ min for calibration

### Step 8 — Verify fingerprint
**Settings → Device → Car fingerprint**  
Expected: `GMC Sierra 1500 2020-21` or similar T1XX name.  
Upstream `opendbc` also lists **GMC Yukon 2019-20**; a 2021 may match Sierra or need a new fingerprint — see CAN section below.

### Optional: OBD-II standby cable
A separate **OBD-C** from the OBD-II port to comma four is optional (standby power / updates with engine off). Not required for normal driving if the harness provides power.

---

## CAN Fingerprint — If Yukon Not Recognized

If openpilot doesn’t auto-detect your Yukon, you’ll need to capture the fingerprint.

**Method 1: Force fingerprint via SSH**
```bash
# SSH into comma four (Settings > Developer > Enable SSH)
ssh comma@[device-ip]
cat /data/params/d/CarParams | python3 -c "import sys,json; d=json.load(sys.stdin); print(d.get('carFingerprint','NOT DETECTED'))"
```

**Method 2: Use openpilot tools**
- Run `tools/car_porting/examples/find_segments_with_message.ipynb` from this repo
- Compare against Sierra 1500 Denali 2021 fingerprint in `opendbc/car/gm/fingerprints.py`

**If fingerprint differs from Sierra:**
1. Capture full CAN fingerprint output
2. Submit PR to [commaai/opendbc](https://github.com/commaai/opendbc) adding Yukon Denali 2021
3. Reference PR template from existing GM vehicles

---

## Key opendbc Files for GM
- [`opendbc/car/gm/fingerprints.py`](https://github.com/commaai/opendbc/blob/master/opendbc/car/gm/fingerprints.py) — vehicle fingerprints
- [`opendbc/car/gm/values.py`](https://github.com/commaai/opendbc/blob/master/opendbc/car/gm/values.py) — CAR enum and feature flags
- [`opendbc/car/gm/interface.py`](https://github.com/commaai/opendbc/blob/master/opendbc/car/gm/interface.py) — car interface & speed/steering limits

---

## Community Resources
- comma.ai Discord: https://discord.comma.ai → `#gm` channel
- BearTech GM Vehicle Guide: https://docs.innoisle.com/car-make/gm-vehicles
- commaai/opendbc: https://github.com/commaai/opendbc
- openpilot supported cars: https://docs.comma.ai/CARS/

---

## Build Status

- [x] VIN confirmed: `1GKS2DKL4MR220264`
- [x] Trim confirmed: Denali Ultimate (ACC + LKAS standard)
- [x] Platform confirmed: GM T1XX
- [x] Harness type confirmed: Standard GM Harness + Box
- [x] comma four: **in hand**
- [x] GM harness: **in hand**
- [ ] Physical harness installed in vehicle
- [ ] comma four mounted on windshield
- [ ] First boot completed, software URL entered
- [ ] Calibration drive completed
- [ ] Fingerprint verified
- [ ] (If needed) CAN fingerprint captured + PR submitted to commaai/opendbc
