# Development of a Test Protocol to Evaluate Infant CPR Training Manikins

**Authors:** Babic N, Baddour N, Fenech M (University of Ottawa)
**Venue:** IEEE MeMeA 2017
**DOI:** 10.1109/MeMeA.2017.7985839

---

## Abstract

The authors created a cross-platform LabVIEW program and test protocol using a Universal Testing Machine (UTM) to evaluate infant CPR manikin performance. They assessed thoracic force-displacement response and feedback mechanisms through root-mean-square error (RMSE) calculations, reporting compression scores of ±17 N, decompression of ±83 N, and final scores of ±50 N for their prototype.

---

## Key Quotes (for claim verification)

### Gap in infant data (supports C5):
> "Little research has been performed to evaluate the force required in younger infants"

> "the absence of well-documented test protocols for the evaluation of CPR manikins"

### Source of reference curves:
- Cite Maltese et al. (2008) for pediatric thoracic force-deflection — but this covers **8-22 year olds**, not infants
- For infants (<12 months), they used **scaling methods** from older child data

---

## Methods Summary

### Test Equipment
- Hydraulic Instron Model 1332 UTM
- Dynamic force capacity: minimum 500 N
- Calibrated load cells and stroke position sensors

### Data Acquisition
- LabVIEW-based
- 10 kHz sampling rate
- 50 data points/second/channel

### Protocol
1. Thoracic force-displacement evaluation via RMSE
2. Feedback mechanism calibration (visual/audio cues)
3. Scoring: compare experimental vs "theoretical" curves

### RMSE Formula
$$RMSE = \sqrt{\frac{\sum_{i=1}^{n}(\hat{y}_i - y_i)^2}{n}}$$

---

## Results

**Prototype manikin:** 7-month-old anthropometrics, ~12 cm max chest depth

**Performance:**
| Phase | RMSE Score |
|-------|------------|
| Compression | ±17 N |
| Decompression | ±83 N |
| Final | ±50 N |

- Force for 40 mm compression: **~190 N**
- Decompression showed "major deviation" due to excessive hysteresis

---

## Relevance to MST Paper

### Supports claim C5:
Babic explicitly acknowledges the absence of infant biomechanical reference data. Their "theoretically desired curves" are scaled from older child data, not measured from human infants.

### Comparison to Thielen 2017:

| Aspect | Babic 2017 | Thielen 2017 |
|--------|------------|--------------|
| Focus | Test protocol | Manikin design |
| Reference data | Scaled from 8-22y | None (anatomical approach) |
| Force at ~40mm | 190 N (prototype) | "Considerably lower" than human |
| Human infant validation | ❌ No | ❌ No |

### Your paper's contribution:
- Babic provides test *methodology* but lacks human infant reference envelope
- Your MFI framework provides what's missing: systematic comparison against reference model
- Even Babic's scaled curves are approximations — your ventilation data (Huang 2016) provides actual infant reference

---

## References Cited (relevant)

- Maltese et al. (2008): Pediatric thoracic force-deflection (8-22 years)
- Park et al. (2014): Manikin-integrated measurement systems
- Stanley et al. (2012): Programmable pneumatic damping

---

*Retrieved: 2026-01-15*
*Source: ResearchGate / IEEE Xplore*
