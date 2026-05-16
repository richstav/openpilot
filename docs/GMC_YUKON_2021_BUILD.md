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
- **Why:** Sierra 1500 Denali 2021 (same T1XX platform) is officially supported
- **Expected behavior:** Yukon will auto-fingerprint as Sierra 1500 Denali on first boot
- **If it doesn’t fingerprint:** See CAN fingerprint section below

### Alternative: SunnyPilot (after confirming basic functionality)
- Adds **M.A.D.S.** — independent steering/speed engagement
- Install URL: `https://smiskol.com/fork/sunnyhaibin/sunnypilot`

---

## Physical Installation — Step by Step

> **Before you begin:** Park on level ground, engine OFF, key out. Do NOT turn on ignition during install.

### Step 1 — Locate Harness Connector
- Open the driver’s door and look at the **rearview mirror housing** at the top of the windshield
- The GM harness connects to the **mirror bracket connector** (grey plug, near the headliner)
- On the Yukon Denali, the connector is typically behind a small trim piece that pops off with a plastic pry tool

### Step 2 — Connect the GM Harness
1. **Disconnect** the existing mirror connector (squeeze tabs and pull firmly)
2. **Plug** the harness inline — one end to the car's connector, one end back to the mirror
3. The harness only connects one way — you cannot plug it in wrong
4. Route the **white ethernet cable** down toward the dash (tuck behind headliner trim)

### Step 3 — Route the Ethernet Cable
1. Gently pull the **A-pillar trim** (driver side) — it pops off with light pressure
2. Route the ethernet cable down the A-pillar, tucking it behind the trim
3. Feed cable under the dash toward the center windshield mount area
4. Leave ~12 inches of slack near the windshield for the comma four connection
5. Reinstall A-pillar trim (press back firmly until clips snap)

### Step 4 — Mount the comma four
1. Clean windshield with isopropyl alcohol where you’ll mount
2. Position the mount **behind the rearview mirror**, centered on the windshield
   - Must be in the forward-facing camera’s clear zone (no tint, no defrost lines)
3. Press mount firmly for 30+ seconds
4. Attach comma four to the mount
5. Connect the **ethernet cable** to the comma four (port on the bottom)

### Step 5 — First Boot & Software Setup
1. Turn ignition ON (engine off is fine)
2. comma four powers on automatically via the harness
3. Follow on-screen setup:
   - Connect to WiFi
   - Enter software URL: **`openpilot.comma.ai`**
   - Wait for download (~500MB, takes 5–10 min on good WiFi)
4. Device will reboot into openpilot
5. It will prompt you to **drive for calibration** — do a 15+ min highway drive

### Step 6 — Verify Fingerprint
- After first drive, check: **Settings → Device → Car fingerprint**
- Expected: `GMC Sierra 1500 Limited Denali 2021` or similar T1XX variant
- If unrecognized: see CAN Fingerprint section below

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
