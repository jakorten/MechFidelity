#!/usr/bin/env python3
"""
Ventilation Mechanics Analysis for Mechanical Fidelity Paper

Calculates respiratory compliance and resistance from pressure/flow data
collected by the existing TIM ventilation apparatus.

Author: Generated for Mechanical Fidelity Paper
Date: January 2026
"""

import numpy as np
from typing import Tuple, Dict, Optional
from dataclasses import dataclass


@dataclass
class VentilationMechanics:
    """Container for ventilation mechanics parameters."""
    compliance_mL_cmH2O: float
    compliance_mL_kPa: float
    resistance_cmH2O_L_s: float
    resistance_kPa_L_s: float
    peak_pressure_cmH2O: float
    peak_flow_L_s: float
    tidal_volume_mL: float

    def to_dict(self) -> Dict:
        return {
            'compliance_mL_cmH2O': self.compliance_mL_cmH2O,
            'compliance_mL_kPa': self.compliance_mL_kPa,
            'resistance_cmH2O_L_s': self.resistance_cmH2O_L_s,
            'resistance_kPa_L_s': self.resistance_kPa_L_s,
            'peak_pressure_cmH2O': self.peak_pressure_cmH2O,
            'peak_flow_L_s': self.peak_flow_L_s,
            'tidal_volume_mL': self.tidal_volume_mL,
        }


# =============================================================================
# Unit Conversion Functions
# =============================================================================

def cmH2O_to_kPa(pressure_cmH2O: float) -> float:
    """Convert pressure from cmH2O to kPa.

    1 kPa = 10.197 cmH2O
    """
    return pressure_cmH2O / 10.197


def kPa_to_cmH2O(pressure_kPa: float) -> float:
    """Convert pressure from kPa to cmH2O."""
    return pressure_kPa * 10.197


def compliance_cmH2O_to_kPa(C_cmH2O: float) -> float:
    """Convert compliance from mL/cmH2O to mL/kPa.

    C [mL/kPa] = C [mL/cmH2O] × 10.197
    """
    return C_cmH2O * 10.197


def resistance_cmH2O_to_kPa(R_cmH2O: float) -> float:
    """Convert resistance from cmH2O/L/s to kPa/L/s.

    R [kPa/L/s] = R [cmH2O/L/s] / 10.197
    """
    return R_cmH2O / 10.197


# =============================================================================
# Core Mechanics Calculations
# =============================================================================

def calculate_compliance(
    volume_mL: np.ndarray,
    pressure_cmH2O: np.ndarray,
    baseline_pressure: Optional[float] = None
) -> float:
    """
    Calculate respiratory system compliance.

    C_rs = ΔV / ΔP [mL/cmH2O]

    Parameters
    ----------
    volume_mL : array
        Volume timeseries in mL
    pressure_cmH2O : array
        Pressure timeseries in cmH2O
    baseline_pressure : float, optional
        Baseline pressure. If None, uses minimum pressure.

    Returns
    -------
    float
        Compliance in mL/cmH2O
    """
    if baseline_pressure is None:
        baseline_pressure = np.min(pressure_cmH2O)

    delta_V = np.max(volume_mL) - np.min(volume_mL)
    delta_P = np.max(pressure_cmH2O) - baseline_pressure

    if delta_P <= 0:
        raise ValueError("Pressure change must be positive")

    return delta_V / delta_P


def calculate_resistance(
    pressure_cmH2O: np.ndarray,
    flow_L_s: np.ndarray,
    method: str = 'peak'
) -> float:
    """
    Calculate respiratory system resistance.

    R_rs = ΔP / V̇ [cmH2O·s/L]

    Parameters
    ----------
    pressure_cmH2O : array
        Pressure timeseries in cmH2O
    flow_L_s : array
        Flow timeseries in L/s
    method : str
        'peak' - use peak flow and corresponding pressure
        'mean' - use mean values during inspiration

    Returns
    -------
    float
        Resistance in cmH2O·s/L (equivalent to cmH2O/L/s)
    """
    if method == 'peak':
        # Find peak inspiratory flow (positive flow = inspiration)
        peak_flow_idx = np.argmax(flow_L_s)
        peak_flow = flow_L_s[peak_flow_idx]

        if peak_flow <= 0:
            raise ValueError("No positive (inspiratory) flow detected")

        # Pressure at peak flow
        pressure_at_peak = pressure_cmH2O[peak_flow_idx]

        return pressure_at_peak / peak_flow

    elif method == 'mean':
        # Use mean values during inspiration (flow > 0)
        insp_mask = flow_L_s > 0
        if not np.any(insp_mask):
            raise ValueError("No inspiratory phase detected")

        mean_pressure = np.mean(pressure_cmH2O[insp_mask])
        mean_flow = np.mean(flow_L_s[insp_mask])

        return mean_pressure / mean_flow

    else:
        raise ValueError(f"Unknown method: {method}")


def analyze_ventilation_cycle(
    time_s: np.ndarray,
    volume_mL: np.ndarray,
    pressure_cmH2O: np.ndarray,
    flow_L_s: Optional[np.ndarray] = None
) -> VentilationMechanics:
    """
    Complete analysis of a single ventilation cycle.

    Parameters
    ----------
    time_s : array
        Time in seconds
    volume_mL : array
        Volume in mL
    pressure_cmH2O : array
        Pressure in cmH2O
    flow_L_s : array, optional
        Flow in L/s. If None, derived from volume.

    Returns
    -------
    VentilationMechanics
        Dataclass with all calculated parameters
    """
    # Derive flow from volume if not provided
    if flow_L_s is None:
        dt = np.diff(time_s)
        dV = np.diff(volume_mL)
        flow_L_s = np.zeros_like(volume_mL)
        flow_L_s[1:] = (dV / dt) / 1000  # mL/s to L/s

    # Calculate compliance
    compliance_cmH2O = calculate_compliance(volume_mL, pressure_cmH2O)
    compliance_kPa = compliance_cmH2O_to_kPa(compliance_cmH2O)

    # Calculate resistance
    resistance_cmH2O = calculate_resistance(pressure_cmH2O, flow_L_s)
    resistance_kPa = resistance_cmH2O_to_kPa(resistance_cmH2O)

    # Extract other parameters
    peak_pressure = np.max(pressure_cmH2O)
    peak_flow = np.max(flow_L_s)
    tidal_volume = np.max(volume_mL) - np.min(volume_mL)

    return VentilationMechanics(
        compliance_mL_cmH2O=compliance_cmH2O,
        compliance_mL_kPa=compliance_kPa,
        resistance_cmH2O_L_s=resistance_cmH2O,
        resistance_kPa_L_s=resistance_kPa,
        peak_pressure_cmH2O=peak_pressure,
        peak_flow_L_s=peak_flow,
        tidal_volume_mL=tidal_volume,
    )


# =============================================================================
# Reference Envelope Comparison
# =============================================================================

# Human reference values from Huang et al. 2016 (infants 1-96 weeks)
HUANG_REFERENCE = {
    'compliance_mL_kPa': {'min': 78, 'max': 171, 'mean': 119.52},
    'resistance_kPa_L_s': {'min': 3.74, 'max': 6.39, 'median': 5.04},
}

# Age-stratified reference (Huang 2016)
HUANG_AGE_STRATIFIED = {
    '1-24_weeks': {'compliance_mL_kPa': 77.95, 'resistance_kPa_L_s': 6.39},
    '25-48_weeks': {'compliance_mL_kPa': 123.51, 'resistance_kPa_L_s': 5.11},
    '49-72_weeks': {'compliance_mL_kPa': 141.17, 'resistance_kPa_L_s': 4.20},
    '73-96_weeks': {'compliance_mL_kPa': 170.58, 'resistance_kPa_L_s': 3.74},
}


def compare_to_reference(
    mechanics: VentilationMechanics,
    reference: Dict = HUANG_REFERENCE
) -> Dict:
    """
    Compare measured mechanics to human reference envelope.

    Returns
    -------
    dict
        Comparison results with 'within_envelope' flags and deviations
    """
    results = {}

    # Compliance comparison
    C = mechanics.compliance_mL_kPa
    C_ref = reference['compliance_mL_kPa']
    results['compliance'] = {
        'measured': C,
        'reference_min': C_ref['min'],
        'reference_max': C_ref['max'],
        'within_envelope': C_ref['min'] <= C <= C_ref['max'],
        'deviation_from_mean_pct': (C - C_ref['mean']) / C_ref['mean'] * 100,
    }

    # Resistance comparison
    R = mechanics.resistance_kPa_L_s
    R_ref = reference['resistance_kPa_L_s']
    results['resistance'] = {
        'measured': R,
        'reference_min': R_ref['min'],
        'reference_max': R_ref['max'],
        'within_envelope': R_ref['min'] <= R <= R_ref['max'],
        'deviation_from_median_pct': (R - R_ref['median']) / R_ref['median'] * 100,
    }

    return results


def calculate_ventilation_fidelity_score(
    mechanics: VentilationMechanics,
    reference: Dict = HUANG_REFERENCE
) -> float:
    """
    Calculate Ventilation Fidelity Score (VFS) for Mechanical Fidelity Index.

    VFS = 1 - mean(|deviation from reference|)

    Score of 1.0 = perfect match to reference center
    Score of 0.0 = deviation equals full envelope width

    Returns
    -------
    float
        VFS between 0 and 1
    """
    # Compliance deviation (normalized to envelope width)
    C = mechanics.compliance_mL_kPa
    C_ref = reference['compliance_mL_kPa']
    C_center = (C_ref['min'] + C_ref['max']) / 2
    C_width = C_ref['max'] - C_ref['min']
    C_deviation = abs(C - C_center) / (C_width / 2)

    # Resistance deviation (normalized to envelope width)
    R = mechanics.resistance_kPa_L_s
    R_ref = reference['resistance_kPa_L_s']
    R_center = (R_ref['min'] + R_ref['max']) / 2
    R_width = R_ref['max'] - R_ref['min']
    R_deviation = abs(R - R_center) / (R_width / 2)

    # Combined score (clamped to [0, 1])
    mean_deviation = (C_deviation + R_deviation) / 2
    VFS = max(0, 1 - mean_deviation)

    return VFS


# =============================================================================
# Batch Processing
# =============================================================================

def analyze_multiple_cycles(
    cycles_data: list,
    reference: Dict = HUANG_REFERENCE
) -> Dict:
    """
    Analyze multiple ventilation cycles and compute statistics.

    Parameters
    ----------
    cycles_data : list of dict
        Each dict contains 'time_s', 'volume_mL', 'pressure_cmH2O',
        and optionally 'flow_L_s'
    reference : dict
        Reference envelope for comparison

    Returns
    -------
    dict
        Aggregated results with mean, std, and fidelity scores
    """
    results = []

    for cycle in cycles_data:
        mechanics = analyze_ventilation_cycle(
            time_s=cycle['time_s'],
            volume_mL=cycle['volume_mL'],
            pressure_cmH2O=cycle['pressure_cmH2O'],
            flow_L_s=cycle.get('flow_L_s'),
        )
        results.append(mechanics)

    # Aggregate statistics
    compliance_values = [r.compliance_mL_kPa for r in results]
    resistance_values = [r.resistance_kPa_L_s for r in results]

    summary = {
        'n_cycles': len(results),
        'compliance_mL_kPa': {
            'mean': np.mean(compliance_values),
            'std': np.std(compliance_values),
            'cv_pct': np.std(compliance_values) / np.mean(compliance_values) * 100,
        },
        'resistance_kPa_L_s': {
            'mean': np.mean(resistance_values),
            'std': np.std(resistance_values),
            'cv_pct': np.std(resistance_values) / np.mean(resistance_values) * 100,
        },
        'individual_cycles': [r.to_dict() for r in results],
    }

    # Calculate VFS for mean values
    mean_mechanics = VentilationMechanics(
        compliance_mL_cmH2O=np.mean([r.compliance_mL_cmH2O for r in results]),
        compliance_mL_kPa=np.mean(compliance_values),
        resistance_cmH2O_L_s=np.mean([r.resistance_cmH2O_L_s for r in results]),
        resistance_kPa_L_s=np.mean(resistance_values),
        peak_pressure_cmH2O=np.mean([r.peak_pressure_cmH2O for r in results]),
        peak_flow_L_s=np.mean([r.peak_flow_L_s for r in results]),
        tidal_volume_mL=np.mean([r.tidal_volume_mL for r in results]),
    )

    summary['ventilation_fidelity_score'] = calculate_ventilation_fidelity_score(
        mean_mechanics, reference
    )
    summary['reference_comparison'] = compare_to_reference(mean_mechanics, reference)

    return summary


# =============================================================================
# Example Usage
# =============================================================================

if __name__ == '__main__':
    # Example with synthetic data
    print("Ventilation Mechanics Analysis Module")
    print("=" * 50)

    # Simulate a ventilation cycle
    t = np.linspace(0, 2, 200)  # 2 seconds
    volume = 25 * np.sin(np.pi * t) ** 2  # 0-25 mL tidal volume
    pressure = 15 * np.sin(np.pi * t) ** 2  # 0-15 cmH2O
    flow = np.gradient(volume, t) / 1000  # L/s

    # Analyze
    mechanics = analyze_ventilation_cycle(t, volume, pressure, flow)

    print(f"\nMeasured Parameters:")
    print(f"  Compliance: {mechanics.compliance_mL_cmH2O:.2f} mL/cmH2O")
    print(f"             ({mechanics.compliance_mL_kPa:.2f} mL/kPa)")
    print(f"  Resistance: {mechanics.resistance_cmH2O_L_s:.2f} cmH2O·s/L")
    print(f"             ({mechanics.resistance_kPa_L_s:.2f} kPa/L/s)")
    print(f"  Tidal Volume: {mechanics.tidal_volume_mL:.1f} mL")
    print(f"  Peak Pressure: {mechanics.peak_pressure_cmH2O:.1f} cmH2O")

    # Compare to reference
    comparison = compare_to_reference(mechanics)
    print(f"\nReference Comparison (Huang 2016):")
    print(f"  Compliance within envelope: {comparison['compliance']['within_envelope']}")
    print(f"  Resistance within envelope: {comparison['resistance']['within_envelope']}")

    # Calculate VFS
    vfs = calculate_ventilation_fidelity_score(mechanics)
    print(f"\nVentilation Fidelity Score: {vfs:.3f}")
