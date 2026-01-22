#!/usr/bin/env python3
"""
Preliminary plots for Mechanical Fidelity paper - Version 2
Shows hysteresis loops for BOTH ventilation and compression

Ventilation: Pressure-Volume loops (compliance from slope, resistance from hysteresis)
Compression: Force-Displacement loops (stiffness from slope, damping from hysteresis)
"""

import numpy as np
import matplotlib.pyplot as plt

# Set style
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150

# =============================================================================
# VENTILATION DATA
# =============================================================================

# Target tidal volume for 3.5 kg infant manikin
Vt = 24.5  # mL (7 mL/kg × 3.5 kg)

# Human reference from Huang 2016 (1-24 weeks, youngest group)
# Compliance: 77.95 ± 46.16 mL/kPa
# Resistance: 6.39 kPa/L/s (median)

# Convert to convenient units for plotting
# C = 78 mL/kPa = 7.8 mL/cmH2O (since 1 kPa ≈ 10 cmH2O)
# R = 6.4 kPa/L/s = 64 cmH2O·s/L

# Hypothetical manikin properties
manikin_names = ['Manikin A', 'Manikin B', 'Manikin C']
colors = ['red', 'green', 'orange']

# Compliance (mL/cmH2O) and Resistance (cmH2O·s/L)
manikin_C = [8.5, 12.0, 6.5]   # mL/cmH2O
manikin_R = [55, 40, 80]       # cmH2O·s/L

# Human reference envelope (from Huang 2016, converted)
human_C_mean = 7.8   # mL/cmH2O
human_C_sd = 4.6     # mL/cmH2O
human_R_median = 64  # cmH2O·s/L
human_R_iqr = [49, 86]  # cmH2O·s/L

# =============================================================================
# COMPRESSION DATA
# =============================================================================

# Hypothetical manikin compression properties
# Stiffness (N/mm) and damping coefficient
manikin_k = [1.0, 1.5, 0.8]      # N/mm (linear stiffness)
manikin_nl = [0.02, 0.01, 0.03]  # Non-linearity factor
manikin_damping = [0.15, 0.10, 0.20]  # Energy loss fraction

# Target compression depth (Ikeyama 2024: 2.7 cm for 0-2 mo infants)
target_depth = 27  # mm

# =============================================================================
# FIGURE 1: VENTILATION P-V LOOP (COMPLIANCE + HYSTERESIS)
# =============================================================================

fig1, ax1 = plt.subplots(figsize=(8, 6))

# Time points for one breath cycle
t = np.linspace(0, 2*np.pi, 100)

# Generate P-V loops for each manikin
for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    # Volume waveform (sinusoidal inspiration/expiration)
    V = (Vt/2) * (1 - np.cos(t))  # 0 to Vt mL

    # Flow = dV/dt (derivative of volume)
    # For sinusoidal: flow peaks at Vt/2 per half-cycle
    # Approximate peak flow: Vt / (inspiration time) ≈ 24.5 mL / 0.5 s = 49 mL/s = 0.049 L/s
    flow = (Vt/2) * np.sin(t) * (1/0.5)  # mL/s, scaled for ~0.5s inspiration
    flow_Lps = flow / 1000  # Convert to L/s

    # Pressure = V/C + R*flow (equation of motion)
    # P_elastic = V / C
    # P_resistive = R * flow
    P_elastic = V / C  # cmH2O
    P_resistive = R * flow_Lps  # cmH2O
    P_total = P_elastic + P_resistive

    # Plot P-V loop
    ax1.plot(P_total, V, linewidth=2, color=colors[i], label=f'{name}: C={C} mL/cmH₂O, R={R} cmH₂O·s/L')

# Add human reference envelope (simplified as a band)
V_ref = np.linspace(0, Vt, 50)
P_ref_low = V_ref / (human_C_mean + human_C_sd)  # High compliance = low pressure
P_ref_high = V_ref / (human_C_mean - human_C_sd)  # Low compliance = high pressure
P_ref_high = np.clip(P_ref_high, 0, 20)  # Clip to reasonable range

ax1.fill_betweenx(V_ref, P_ref_low, P_ref_high, alpha=0.2, color='blue',
                   label=f'Human reference (C={human_C_mean}±{human_C_sd} mL/cmH₂O)')

# Add arrows to show direction
ax1.annotate('', xy=(6, 20), xytext=(4, 12),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.annotate('', xy=(2, 8), xytext=(4, 16),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax1.text(2, 20, 'Inspiration', fontsize=9, fontweight='bold')
ax1.text(5, 5, 'Expiration', fontsize=9, fontweight='bold')

ax1.set_xlabel('Airway Pressure (cmH₂O)')
ax1.set_ylabel('Volume (mL)')
ax1.set_title('Infant Ventilation: Pressure-Volume Loop\nSlope = Compliance, Loop Area = Resistance Work')
ax1.set_xlim(-2, 15)
ax1.set_ylim(0, 30)
ax1.legend(loc='lower right', fontsize=8)
ax1.grid(True, alpha=0.3)
ax1.axhline(y=Vt, color='gray', linestyle=':', alpha=0.5)
ax1.text(12, Vt+1, f'Vt={Vt} mL', fontsize=8, color='gray')

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v2_ventilation_PV_loop.png')
print("Saved: plot_v2_ventilation_PV_loop.png")

# =============================================================================
# FIGURE 2: COMPRESSION FORCE-DISPLACEMENT LOOP (STIFFNESS + DAMPING)
# =============================================================================

fig2, ax2 = plt.subplots(figsize=(8, 6))

# Displacement cycle
d_down = np.linspace(0, target_depth, 50)  # Compression
d_up = np.linspace(target_depth, 0, 50)    # Release

for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    # Loading curve: F = k*d + nl*d^2 (non-linear spring)
    F_down = k * d_down + nl * d_down**2

    # Unloading curve: reduced by damping factor (energy loss)
    F_up = (k * d_up + nl * d_up**2) * (1 - damp)

    # Plot hysteresis loop
    ax2.plot(d_down, F_down, linewidth=2, color=colors[i],
             label=f'{name}: k={k} N/mm, {int(damp*100)}% damping')
    ax2.plot(d_up, F_up, linewidth=2, color=colors[i], linestyle='--', alpha=0.7)

    # Fill the hysteresis area (energy dissipation)
    d_full = np.concatenate([d_down, d_up])
    F_full = np.concatenate([F_down, F_up])
    ax2.fill(d_full, F_full, alpha=0.1, color=colors[i])

# Add arrows for direction
ax2.annotate('', xy=(20, 28), xytext=(10, 14),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax2.annotate('', xy=(8, 8), xytext=(18, 20),
             arrowprops=dict(arrowstyle='->', color='black', lw=1.5))
ax2.text(5, 25, 'Compression', fontsize=9, fontweight='bold')
ax2.text(18, 8, 'Release', fontsize=9, fontweight='bold')

# Target depth line
ax2.axvline(x=target_depth, color='gray', linestyle=':', alpha=0.7)
ax2.text(target_depth+0.5, 5, f'Target\n{target_depth} mm', fontsize=8, color='gray')

ax2.set_xlabel('Displacement (mm)')
ax2.set_ylabel('Force (N)')
ax2.set_title('Infant Compression: Force-Displacement Loop\nSlope = Stiffness, Loop Area = Energy Dissipation (Damping)')
ax2.set_xlim(0, 32)
ax2.set_ylim(0, 50)
ax2.legend(loc='upper left', fontsize=8)
ax2.grid(True, alpha=0.3)

# Note about no human reference
ax2.annotate('Note: No human infant\nchest stiffness data exists\n(descriptive only)',
             xy=(22, 40), fontsize=9, style='italic',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v2_compression_FD_loop.png')
print("Saved: plot_v2_compression_FD_loop.png")

# =============================================================================
# FIGURE 3: COMBINED 2x2 - HYSTERESIS COMPARISON
# =============================================================================

fig3, axes = plt.subplots(2, 2, figsize=(12, 10))

# Top-left: Ventilation P-V loop
ax = axes[0, 0]
for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    V = (Vt/2) * (1 - np.cos(t))
    flow = (Vt/2) * np.sin(t) * (1/0.5)
    flow_Lps = flow / 1000
    P_total = V / C + R * flow_Lps
    ax.plot(P_total, V, linewidth=2, color=colors[i], label=name)
ax.fill_betweenx(V_ref, P_ref_low, P_ref_high, alpha=0.2, color='blue', label='Human ref.')
ax.set_xlabel('Pressure (cmH₂O)')
ax.set_ylabel('Volume (mL)')
ax.set_title('A) Ventilation: P-V Loop')
ax.set_xlim(-2, 15)
ax.set_ylim(0, 30)
ax.legend(loc='lower right', fontsize=8)
ax.grid(True, alpha=0.3)

# Top-right: Ventilation time waveforms
ax = axes[0, 1]
t_sec = np.linspace(0, 2, 100)  # 2 seconds
for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    V = (Vt/2) * (1 - np.cos(np.pi * t_sec))  # One breath in 2 sec
    flow = (Vt/2) * np.pi * np.sin(np.pi * t_sec)  # mL/s
    flow_Lps = flow / 1000
    P_total = V / C + R * flow_Lps
    ax.plot(t_sec, P_total, linewidth=2, color=colors[i], label=name)
ax.axhline(y=0, color='gray', linestyle='-', alpha=0.3)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Pressure (cmH₂O)')
ax.set_title('B) Ventilation: Pressure Waveform')
ax.set_xlim(0, 2)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

# Bottom-left: Compression F-D loop
ax = axes[1, 0]
for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    F_down = k * d_down + nl * d_down**2
    F_up = (k * d_up + nl * d_up**2) * (1 - damp)
    ax.plot(d_down, F_down, linewidth=2, color=colors[i], label=name)
    ax.plot(d_up, F_up, linewidth=2, color=colors[i], linestyle='--', alpha=0.7)
ax.axvline(x=target_depth, color='gray', linestyle=':', alpha=0.7)
ax.set_xlabel('Displacement (mm)')
ax.set_ylabel('Force (N)')
ax.set_title('C) Compression: F-D Loop (no human ref.)')
ax.set_xlim(0, 32)
ax.set_ylim(0, 50)
ax.legend(loc='upper left', fontsize=8)
ax.grid(True, alpha=0.3)

# Bottom-right: Compression time waveforms
ax = axes[1, 1]
t_comp = np.linspace(0, 1, 100)  # 1 second compression cycle (100 bpm = ~0.6s, but showing slower)
d_t = (target_depth/2) * (1 - np.cos(2*np.pi * t_comp))  # Sinusoidal displacement
for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    # Force follows displacement with some phase shift due to damping
    F_t = k * d_t + nl * d_t**2
    ax.plot(t_comp, F_t, linewidth=2, color=colors[i], label=name)
ax.set_xlabel('Time (s)')
ax.set_ylabel('Force (N)')
ax.set_title('D) Compression: Force Waveform')
ax.set_xlim(0, 1)
ax.legend(loc='upper right', fontsize=8)
ax.grid(True, alpha=0.3)

plt.suptitle('Mechanical Fidelity: Hysteresis Loops\nVentilation (with human ref.) vs Compression (descriptive)',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v2_combined_hysteresis.png')
print("Saved: plot_v2_combined_hysteresis.png")

# =============================================================================
# FIGURE 4: SIDE-BY-SIDE COMPARISON (Ventilation vs Compression loops)
# =============================================================================

fig4, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# Left: Ventilation P-V loop
for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    V = (Vt/2) * (1 - np.cos(t))
    flow = (Vt/2) * np.sin(t) * (1/0.5)
    flow_Lps = flow / 1000
    P_total = V / C + R * flow_Lps
    ax1.plot(P_total, V, linewidth=2.5, color=colors[i], label=f'{name}')

ax1.fill_betweenx(V_ref, P_ref_low, P_ref_high, alpha=0.25, color='blue',
                   label='Human envelope')
ax1.set_xlabel('Airway Pressure, Paw (cmH₂O)', fontsize=11)
ax1.set_ylabel('Volume, V (mL)', fontsize=11)
ax1.set_title('VENTILATION\nP-V Loop (Compliance & Resistance)', fontsize=12, fontweight='bold')
ax1.set_xlim(-2, 15)
ax1.set_ylim(0, 30)
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, alpha=0.3)

# Annotations
ax1.annotate('Slope = C\n(compliance)', xy=(2, 15), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax1.annotate('Loop width = R\n(resistance)', xy=(8, 8), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Right: Compression F-D loop
for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    F_down = k * d_down + nl * d_down**2
    F_up = (k * d_up + nl * d_up**2) * (1 - damp)
    d_full = np.concatenate([d_down, d_up])
    F_full = np.concatenate([F_down, F_up])
    ax2.fill(d_full, F_full, alpha=0.15, color=colors[i])
    ax2.plot(d_down, F_down, linewidth=2.5, color=colors[i], label=f'{name}')
    ax2.plot(d_up, F_up, linewidth=2.5, color=colors[i], linestyle='--', alpha=0.7)

ax2.axvline(x=target_depth, color='gray', linestyle=':', alpha=0.7, linewidth=2)
ax2.set_xlabel('Displacement, d (mm)', fontsize=11)
ax2.set_ylabel('Force, F (N)', fontsize=11)
ax2.set_title('COMPRESSION\nF-D Loop (Stiffness & Damping)', fontsize=12, fontweight='bold')
ax2.set_xlim(0, 32)
ax2.set_ylim(0, 50)
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)

# Annotations
ax2.annotate('Slope = k\n(stiffness)', xy=(5, 35), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax2.annotate('Loop area = \nenergy loss\n(damping)', xy=(15, 15), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax2.annotate('No human\nreference', xy=(22, 42), fontsize=9, style='italic', color='red',
             bbox=dict(boxstyle='round', facecolor='lightyellow', alpha=0.8))

plt.suptitle('Mechanical Fidelity of Infant CPR Manikins: Hysteresis Analysis',
             fontsize=14, fontweight='bold', y=1.02)
plt.tight_layout()
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v2_sidebyside_loops.png')
print("Saved: plot_v2_sidebyside_loops.png")

print("\nAll v2 plots generated successfully!")
print("\nKey insight: Both ventilation and compression show hysteresis:")
print("  - Ventilation: P-V loop width indicates resistance effects")
print("  - Compression: F-D loop area indicates energy dissipation (damping)")
