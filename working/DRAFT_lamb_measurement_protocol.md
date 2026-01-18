# DRAFT: Lamb Chest Compression Measurement Protocol

**Status:** DRAFT - for discussion only
**Purpose:** Characterize infant-surrogate chest mechanical properties
**Collaborator:** Arjen ten Pas (LUMC)
**Created:** 2026-01-18

---

## Objective

Measure force-displacement characteristics of lamb chest to establish reference data for infant CPR manikin fidelity assessment.

**Target parameters:**
- Stiffness k (N/mm)
- Damping coefficient c (N·s/mm)
- Non-linearity
- Hysteresis

---

## Animal Specifications

| Parameter | Target | Rationale |
|-----------|--------|-----------|
| Species | Lamb | Similar mass to term infant |
| Weight | 3-4 kg | Matches infant manikin target |
| Age | Newborn/perinatal | Chest compliance comparable |

---

## Equipment

### Available (HAN)
- CNC linear actuator (BlackBox X32)
- Load cell DYMH-103 (0-49 N)
- Displacement sensor VL53L4CD
- STM32F405 data acquisition

### To prepare
- Compression plunger (~30 mm diameter, flat or slightly curved)
- Positioning support/jig
- Calipers for chest measurement

---

## Measurements to Record

### Per animal:
| Parameter | Unit | Method |
|-----------|------|--------|
| Weight | kg | Scale |
| Chest AP diameter | mm | Calipers |
| Age | days | Record |
| Post-mortem interval | hours | Record |
| Temperature | °C | Thermometer |

### Per compression test:
| Parameter | Unit | Rate |
|-----------|------|------|
| Force | N | 100 Hz |
| Displacement | mm | 100 Hz |
| Timestamp | ms | Synchronized |

---

## Test Protocol (Draft)

### Preparation
1. Position lamb supine
2. Measure chest AP diameter
3. Calculate target depth: 1/3 × AP diameter
4. Zero sensors

### Test 1: Quasi-static (stiffness)
- Compression rate: 2 mm/s
- Depth: 0 → target → 0
- Cycles: 3
- Rest: 30 s between cycles

### Test 2: Dynamic (damping)
- Compression rate: 100/min (~1.7 Hz)
- Depth: target depth
- Cycles: 10
- Rest: 60 s after

### Test 3: Repeat quasi-static
- Same as Test 1
- Check for tissue fatigue/change

---

## Data Analysis

### Stiffness (from quasi-static):
```
k = ΔF / Δd  (linear fit)
```
Or polynomial fit for non-linearity:
```
F = k₁d + k₂d² + k₃d³
```

### Damping (from dynamic):
```
c = loop_width / (2 × v_max)
```

### Hysteresis:
```
H = (loop_area / loading_area) × 100%
```

---

## Sample Size

| Phase | n | Purpose |
|-------|---|---------|
| Pilot | 2-3 | Verify setup, refine protocol |
| Main study | 8-10 | Reference data with CI |

---

## Considerations

### Ethical
- [ ] Animal research approval required
- [ ] LUMC protocol coverage?

### Practical
- [ ] Fresh tissue timing (<2h post-mortem ideal)
- [ ] Temperature control
- [ ] Equipment transport to LUMC?

### Scientific
- [ ] Live vs post-mortem differences (Arbogast: ~2× stiffer post-mortem)
- [ ] Lamb vs human infant validity

---

## Open Questions

1. Does LUMC have existing ethical approval for lamb mechanical testing?
2. Can we use animals from other studies (opportunistic)?
3. Equipment at LUMC or transport from HAN?
4. Fresh post-mortem or anesthetized?
5. Sample size for statistical validity?

---

## Next Steps (if proceeding)

1. [ ] Discuss feasibility with Arjen ten Pas
2. [ ] Clarify ethical/practical constraints
3. [ ] Pilot test (n=2-3)
4. [ ] Refine protocol based on pilot
5. [ ] Main study (n=8-10)

---

*DRAFT - not for execution without further review*
