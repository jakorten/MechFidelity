#!/usr/bin/env python3
"""
Preliminary plots for Mechanical Fidelity paper
Shows expected data visualization for:
- Ventilation: Compliance & Resistance (with human reference from Huang 2016)
- Compression: Stiffness & Damping (descriptive, no human reference for infants)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon

# Set style
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150

# =============================================================================
# VENTILATION DATA (from Huang 2016, n=205)
# =============================================================================

# Age groups (weeks) - midpoints
age_weeks = np.array([12, 36, 60, 84])  # 1-24, 25-48, 49-72, 73-96 weeks
age_labels = ['1-24 wk', '25-48 wk', '49-72 wk', '73-96 wk']

# Compliance (mL/kPa) - mean ± SD from Huang 2016 Table 2
compliance_mean = np.array([77.95, 115.60, 147.50, 170.58])
compliance_sd = np.array([46.16, 48.44, 52.29, 50.14])

# Resistance (kPa/L/s) - median (IQR) from Huang 2016 Table 2
resistance_median = np.array([6.39, 4.90, 4.23, 3.74])
resistance_iqr_low = np.array([4.90, 3.92, 3.33, 3.04])
resistance_iqr_high = np.array([8.63, 6.27, 5.59, 4.90])

# Hypothetical manikin data (to be replaced with real measurements)
manikin_names = ['Manikin A', 'Manikin B', 'Manikin C']
# Compliance values (hypothetical - representing different manikin designs)
manikin_compliance = [85, 120, 65]  # mL/kPa
# Resistance values (hypothetical)
manikin_resistance = [5.5, 4.0, 8.0]  # kPa/L/s

# =============================================================================
# FIGURE 1: VENTILATION - COMPLIANCE
# =============================================================================

fig1, ax1 = plt.subplots(figsize=(8, 5))

# Human reference envelope (mean ± 2SD for ~95% coverage)
upper = compliance_mean + 2*compliance_sd
lower = np.maximum(compliance_mean - 2*compliance_sd, 0)

# Fill envelope
ax1.fill_between(age_weeks, lower, upper, alpha=0.3, color='blue',
                  label='Human reference (mean ± 2SD)')

# Mean line
ax1.plot(age_weeks, compliance_mean, 'b-', linewidth=2, marker='o',
         label='Human mean (Huang 2016, n=205)')

# Hypothetical manikin points (at 12 weeks equivalent - typical infant manikin)
colors = ['red', 'green', 'orange']
for i, (name, c_val) in enumerate(zip(manikin_names, manikin_compliance)):
    ax1.scatter([12], [c_val], s=150, c=colors[i], marker='s',
                edgecolors='black', linewidth=1.5, zorder=5, label=f'{name}: {c_val} mL/kPa')

ax1.set_xlabel('Age (weeks)')
ax1.set_ylabel('Compliance (mL/kPa)')
ax1.set_title('Infant Ventilation: Compliance\nHuman Reference vs Manikin Characterization')
ax1.set_xlim(0, 100)
ax1.set_ylim(0, 300)
ax1.legend(loc='upper left', fontsize=9)
ax1.grid(True, alpha=0.3)

# Add annotation
ax1.annotate('Fidelity assessment:\nManikin within envelope?',
             xy=(50, 250), fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_ventilation_compliance.png')
print("Saved: plot_ventilation_compliance.png")

# =============================================================================
# FIGURE 2: VENTILATION - RESISTANCE
# =============================================================================

fig2, ax2 = plt.subplots(figsize=(8, 5))

# Human reference envelope (using IQR)
ax2.fill_between(age_weeks, resistance_iqr_low, resistance_iqr_high,
                  alpha=0.3, color='blue', label='Human reference (IQR)')

# Median line
ax2.plot(age_weeks, resistance_median, 'b-', linewidth=2, marker='o',
         label='Human median (Huang 2016, n=205)')

# Hypothetical manikin points
for i, (name, r_val) in enumerate(zip(manikin_names, manikin_resistance)):
    ax2.scatter([12], [r_val], s=150, c=colors[i], marker='s',
                edgecolors='black', linewidth=1.5, zorder=5, label=f'{name}: {r_val} kPa/L/s')

ax2.set_xlabel('Age (weeks)')
ax2.set_ylabel('Resistance (kPa/L/s)')
ax2.set_title('Infant Ventilation: Resistance\nHuman Reference vs Manikin Characterization')
ax2.set_xlim(0, 100)
ax2.set_ylim(0, 12)
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

# Add annotation
ax2.annotate('Fidelity assessment:\nManikin within envelope?',
             xy=(50, 10), fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_ventilation_resistance.png')
print("Saved: plot_ventilation_resistance.png")

# =============================================================================
# FIGURE 3: COMPRESSION - FORCE-DISPLACEMENT (STIFFNESS)
# =============================================================================

fig3, ax3 = plt.subplots(figsize=(8, 5))

# Displacement range for infant manikin (0-30 mm typical)
displacement = np.linspace(0, 25, 100)  # mm

# Hypothetical manikin force-displacement curves
# F = k * d (linear) or F = k1*d + k2*d^2 (non-linear)
# Stiffness values (N/mm) - hypothetical for infant manikins
stiffness_values = [1.0, 1.5, 0.8]  # N/mm (linear approximation)
nonlinearity = [0.02, 0.01, 0.03]  # Progressivity factor

for i, (name, k, nl) in enumerate(zip(manikin_names, stiffness_values, nonlinearity)):
    # Non-linear force: F = k*d + nl*d^2
    force = k * displacement + nl * displacement**2
    ax3.plot(displacement, force, linewidth=2, color=colors[i],
             label=f'{name}: k={k} N/mm')

# Add typical compression depth marker (Ikeyama 2024: 2.7 cm for 0-2mo)
ax3.axvline(x=27, color='gray', linestyle='--', alpha=0.7)
ax3.annotate('Target depth\n(27 mm)', xy=(27, 5), xytext=(20, 8),
             fontsize=9, arrowprops=dict(arrowstyle='->', color='gray'))

ax3.set_xlabel('Displacement (mm)')
ax3.set_ylabel('Force (N)')
ax3.set_title('Infant Compression: Force-Displacement (Stiffness)\nDescriptive Characterization (no human reference)')
ax3.set_xlim(0, 30)
ax3.set_ylim(0, 50)
ax3.legend(loc='upper left', fontsize=9)
ax3.grid(True, alpha=0.3)

# Add note about no human reference
ax3.annotate('Note: No human infant\nchest stiffness data exists',
             xy=(18, 40), fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_compression_stiffness.png')
print("Saved: plot_compression_stiffness.png")

# =============================================================================
# FIGURE 4: COMPRESSION - HYSTERESIS (DAMPING)
# =============================================================================

fig4, ax4 = plt.subplots(figsize=(8, 5))

# Compression cycle with hysteresis
displacement_down = np.linspace(0, 25, 50)  # Compression phase
displacement_up = np.linspace(25, 0, 50)    # Release phase

for i, (name, k, nl) in enumerate(zip(manikin_names, stiffness_values, nonlinearity)):
    # Compression (loading)
    force_down = k * displacement_down + nl * displacement_down**2
    # Release (unloading) - with hysteresis (damping effect)
    damping_factor = 0.15  # ~15% energy loss
    force_up = (k * displacement_up + nl * displacement_up**2) * (1 - damping_factor)

    # Plot hysteresis loop
    ax4.plot(displacement_down, force_down, linewidth=2, color=colors[i],
             label=f'{name} (loading)')
    ax4.plot(displacement_up, force_up, linewidth=2, color=colors[i],
             linestyle='--', alpha=0.7)

# Add arrows to show direction
ax4.annotate('', xy=(15, 20), xytext=(10, 12),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax4.annotate('', xy=(10, 8), xytext=(15, 15),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax4.text(8, 18, 'Loading', fontsize=9)
ax4.text(16, 8, 'Unloading', fontsize=9)

ax4.set_xlabel('Displacement (mm)')
ax4.set_ylabel('Force (N)')
ax4.set_title('Infant Compression: Hysteresis Loop (Damping)\nArea = Energy Dissipation')
ax4.set_xlim(0, 30)
ax4.set_ylim(0, 50)
ax4.legend(loc='upper left', fontsize=9)
ax4.grid(True, alpha=0.3)

# Add note about damping
ax4.annotate('Damping coefficient from\nhysteresis loop area',
             xy=(20, 35), fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_compression_damping.png')
print("Saved: plot_compression_damping.png")

# =============================================================================
# FIGURE 5: COMBINED OVERVIEW (2x2)
# =============================================================================

fig5, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Compliance
ax = axes[0, 0]
ax.fill_between(age_weeks, lower, upper, alpha=0.3, color='blue')
ax.plot(age_weeks, compliance_mean, 'b-', linewidth=2, marker='o')
for i, (name, c_val) in enumerate(zip(manikin_names, manikin_compliance)):
    ax.scatter([12], [c_val], s=100, c=colors[i], marker='s', edgecolors='black')
ax.set_xlabel('Age (weeks)')
ax.set_ylabel('Compliance (mL/kPa)')
ax.set_title('A) Ventilation: Compliance')
ax.set_xlim(0, 100)
ax.set_ylim(0, 300)
ax.grid(True, alpha=0.3)

# Top-right: Resistance
ax = axes[0, 1]
ax.fill_between(age_weeks, resistance_iqr_low, resistance_iqr_high, alpha=0.3, color='blue')
ax.plot(age_weeks, resistance_median, 'b-', linewidth=2, marker='o')
for i, (name, r_val) in enumerate(zip(manikin_names, manikin_resistance)):
    ax.scatter([12], [r_val], s=100, c=colors[i], marker='s', edgecolors='black')
ax.set_xlabel('Age (weeks)')
ax.set_ylabel('Resistance (kPa/L/s)')
ax.set_title('B) Ventilation: Resistance')
ax.set_xlim(0, 100)
ax.set_ylim(0, 12)
ax.grid(True, alpha=0.3)

# Bottom-left: Stiffness
ax = axes[1, 0]
for i, (name, k, nl) in enumerate(zip(manikin_names, stiffness_values, nonlinearity)):
    force = k * displacement + nl * displacement**2
    ax.plot(displacement, force, linewidth=2, color=colors[i], label=name)
ax.axvline(x=27, color='gray', linestyle='--', alpha=0.7)
ax.set_xlabel('Displacement (mm)')
ax.set_ylabel('Force (N)')
ax.set_title('C) Compression: Stiffness (no human ref.)')
ax.set_xlim(0, 30)
ax.set_ylim(0, 50)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)

# Bottom-right: Damping
ax = axes[1, 1]
for i, (name, k, nl) in enumerate(zip(manikin_names, stiffness_values, nonlinearity)):
    force_down = k * displacement_down + nl * displacement_down**2
    force_up = (k * displacement_up + nl * displacement_up**2) * 0.85
    ax.plot(displacement_down, force_down, linewidth=2, color=colors[i], label=name)
    ax.plot(displacement_up, force_up, linewidth=2, color=colors[i], linestyle='--', alpha=0.7)
ax.set_xlabel('Displacement (mm)')
ax.set_ylabel('Force (N)')
ax.set_title('D) Compression: Damping (hysteresis)')
ax.set_xlim(0, 30)
ax.set_ylim(0, 50)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle('Mechanical Fidelity of Infant CPR Manikins\nPreliminary Plot Concepts',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_combined_overview.png')
print("Saved: plot_combined_overview.png")

print("\nAll plots generated successfully!")
print("\nLegend:")
print("  - Blue shaded area: Human reference envelope")
print("  - Colored squares: Hypothetical manikin measurements")
print("  - Manikin data is PLACEHOLDER - to be replaced with real measurements")
