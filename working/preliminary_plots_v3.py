#!/usr/bin/env python3
"""
Preliminary plots for Mechanical Fidelity paper - Version 3
Includes hypothetical LAMB reference for compression (3.5 kg, comparable to newborn infant)
"""

import numpy as np
import matplotlib.pyplot as plt

# Set style
plt.rcParams['font.size'] = 10
plt.rcParams['figure.dpi'] = 150

# =============================================================================
# VENTILATION DATA (from Huang 2016)
# =============================================================================

Vt = 24.5  # mL (7 mL/kg × 3.5 kg)

manikin_names = ['Manikin A', 'Manikin B', 'Manikin C']
colors = ['red', 'green', 'orange']

# Compliance (mL/cmH2O) and Resistance (cmH2O·s/L)
manikin_C = [8.5, 12.0, 6.5]
manikin_R = [55, 40, 80]

# Human reference (Huang 2016)
human_C_mean = 7.8
human_C_sd = 4.6

# =============================================================================
# COMPRESSION DATA
# =============================================================================

# Manikin properties
manikin_k = [1.0, 1.5, 0.8]      # N/mm
manikin_nl = [0.02, 0.01, 0.03]  # Non-linearity
manikin_damping = [0.15, 0.10, 0.20]

target_depth = 27  # mm

# HYPOTHETICAL LAMB REFERENCE (3.5 kg, newborn equivalent)
# These are placeholder values - to be replaced with actual lamb data
# Based on general neonatal biomechanics literature estimates
lamb_k_mean = 1.2      # N/mm (hypothetical mean stiffness)
lamb_k_sd = 0.3        # N/mm (hypothetical SD)
lamb_damping_mean = 0.12  # 12% energy loss (hypothetical)
lamb_damping_sd = 0.04

# =============================================================================
# FIGURE: SIDE-BY-SIDE WITH LAMB REFERENCE
# =============================================================================

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

t = np.linspace(0, 2*np.pi, 100)
d_down = np.linspace(0, target_depth, 50)
d_up = np.linspace(target_depth, 0, 50)

# --- LEFT: Ventilation P-V loop ---
V_ref = np.linspace(0, Vt, 50)
P_ref_low = V_ref / (human_C_mean + human_C_sd)
P_ref_high = V_ref / (human_C_mean - human_C_sd)
P_ref_high = np.clip(P_ref_high, 0, 20)

ax1.fill_betweenx(V_ref, P_ref_low, P_ref_high, alpha=0.25, color='blue',
                   label='Human envelope (Huang 2016)')

for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    V = (Vt/2) * (1 - np.cos(t))
    flow = (Vt/2) * np.sin(t) * (1/0.5)
    flow_Lps = flow / 1000
    P_total = V / C + R * flow_Lps
    ax1.plot(P_total, V, linewidth=2.5, color=colors[i], label=f'{name}')

ax1.set_xlabel('Airway Pressure, Paw (cmH₂O)', fontsize=11)
ax1.set_ylabel('Volume, V (mL)', fontsize=11)
ax1.set_title('VENTILATION\nP-V Loop (Human Reference)', fontsize=12, fontweight='bold')
ax1.set_xlim(-2, 15)
ax1.set_ylim(0, 30)
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, alpha=0.3)

ax1.annotate('Slope = C', xy=(2, 15), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax1.annotate('Loop width ∝ R', xy=(7, 8), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# --- RIGHT: Compression F-D loop WITH LAMB REFERENCE ---

# Lamb reference envelope (hypothetical)
k_low = lamb_k_mean - lamb_k_sd
k_high = lamb_k_mean + lamb_k_sd

# Generate envelope curves
F_env_low = k_low * d_down + 0.015 * d_down**2  # Lower bound (softer)
F_env_high = k_high * d_down + 0.025 * d_down**2  # Upper bound (stiffer)

# Fill lamb reference envelope
ax2.fill_between(d_down, F_env_low, F_env_high, alpha=0.25, color='purple',
                  label='Lamb envelope (3.5 kg, hypothetical)')

# Manikin loops
for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    F_down = k * d_down + nl * d_down**2
    F_up = (k * d_up + nl * d_up**2) * (1 - damp)
    d_full = np.concatenate([d_down, d_up])
    F_full = np.concatenate([F_down, F_up])
    ax2.fill(d_full, F_full, alpha=0.1, color=colors[i])
    ax2.plot(d_down, F_down, linewidth=2.5, color=colors[i], label=f'{name}')
    ax2.plot(d_up, F_up, linewidth=2.5, color=colors[i], linestyle='--', alpha=0.7)

ax2.axvline(x=target_depth, color='gray', linestyle=':', alpha=0.7, linewidth=2)

ax2.set_xlabel('Displacement, d (mm)', fontsize=11)
ax2.set_ylabel('Force, F (N)', fontsize=11)
ax2.set_title('COMPRESSION\nF-D Loop (Lamb Reference)', fontsize=12, fontweight='bold')
ax2.set_xlim(0, 32)
ax2.set_ylim(0, 50)
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)

ax2.annotate('Slope = k', xy=(5, 38), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
ax2.annotate('Loop area =\ndamping', xy=(15, 12), fontsize=9,
             bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))

# Note about lamb data being hypothetical
ax2.annotate('⚠ Lamb data TBD\n(values hypothetical)',
             xy=(22, 5), fontsize=8, style='italic', color='purple',
             bbox=dict(boxstyle='round', facecolor='lavender', alpha=0.9))

plt.suptitle('Mechanical Fidelity of Infant CPR Manikins\nVentilation (Human ref.) + Compression (Lamb ref.)',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v3_with_lamb_reference.png')
print("Saved: plot_v3_with_lamb_reference.png")

# =============================================================================
# FIGURE 2: FIDELITY ASSESSMENT CONCEPT
# =============================================================================

fig2, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Ventilation Fidelity ---
ax1.fill_betweenx(V_ref, P_ref_low, P_ref_high, alpha=0.3, color='blue',
                   label='Human reference')

# Show which manikins are within/outside envelope
for i, (name, C, R) in enumerate(zip(manikin_names, manikin_C, manikin_R)):
    V = (Vt/2) * (1 - np.cos(t))
    flow = (Vt/2) * np.sin(t) * (1/0.5)
    flow_Lps = flow / 1000
    P_total = V / C + R * flow_Lps

    # Check if within envelope (simplified: check at Vt)
    P_at_Vt = Vt / C
    within = P_ref_low[-1] <= P_at_Vt <= P_ref_high[-1]

    linestyle = '-' if within else '-'
    marker = '✓' if within else '✗'
    status = 'IN' if within else 'OUT'

    ax1.plot(P_total, V, linewidth=2.5, color=colors[i],
             label=f'{name} [{status}]')

ax1.set_xlabel('Pressure (cmH₂O)', fontsize=11)
ax1.set_ylabel('Volume (mL)', fontsize=11)
ax1.set_title('VENTILATION FIDELITY\nManikin vs Human Reference', fontsize=12, fontweight='bold')
ax1.set_xlim(-2, 15)
ax1.set_ylim(0, 30)
ax1.legend(loc='lower right', fontsize=9)
ax1.grid(True, alpha=0.3)

# --- Compression Fidelity ---
ax2.fill_between(d_down, F_env_low, F_env_high, alpha=0.3, color='purple',
                  label='Lamb reference')

for i, (name, k, nl, damp) in enumerate(zip(manikin_names, manikin_k, manikin_nl, manikin_damping)):
    F_down = k * d_down + nl * d_down**2
    F_up = (k * d_up + nl * d_up**2) * (1 - damp)

    # Check if within envelope (at target depth)
    F_at_target = k * target_depth + nl * target_depth**2
    F_low_target = k_low * target_depth + 0.015 * target_depth**2
    F_high_target = k_high * target_depth + 0.025 * target_depth**2
    within = F_low_target <= F_at_target <= F_high_target

    status = 'IN' if within else 'OUT'

    ax2.plot(d_down, F_down, linewidth=2.5, color=colors[i], label=f'{name} [{status}]')
    ax2.plot(d_up, F_up, linewidth=2.5, color=colors[i], linestyle='--', alpha=0.7)

ax2.axvline(x=target_depth, color='gray', linestyle=':', alpha=0.7)
ax2.set_xlabel('Displacement (mm)', fontsize=11)
ax2.set_ylabel('Force (N)', fontsize=11)
ax2.set_title('COMPRESSION FIDELITY\nManikin vs Lamb Reference', fontsize=12, fontweight='bold')
ax2.set_xlim(0, 32)
ax2.set_ylim(0, 50)
ax2.legend(loc='upper left', fontsize=9)
ax2.grid(True, alpha=0.3)

plt.suptitle('Mechanical Fidelity Assessment\nWhich Manikins Fall Within Reference Envelope?',
             fontsize=14, fontweight='bold')
plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig('/Users/jakorten/research/Paper3 - MechanicalFidelity/working/plot_v3_fidelity_assessment.png')
print("Saved: plot_v3_fidelity_assessment.png")

# =============================================================================
# SUMMARY TABLE
# =============================================================================

print("\n" + "="*70)
print("REFERENCE DATA SUMMARY")
print("="*70)
print("\nVENTILATION (Human, Huang 2016, n=205, 1-24 weeks):")
print(f"  Compliance: {human_C_mean} ± {human_C_sd} mL/cmH₂O")
print(f"  (equivalent: ~78 ± 46 mL/kPa)")
print()
print("COMPRESSION (Lamb, 3.5 kg, HYPOTHETICAL - TBD):")
print(f"  Stiffness: {lamb_k_mean} ± {lamb_k_sd} N/mm")
print(f"  Damping: {lamb_damping_mean*100:.0f} ± {lamb_damping_sd*100:.0f}% energy loss")
print()
print("⚠ Lamb values are PLACEHOLDERS - replace with actual data when available")
print("="*70)
