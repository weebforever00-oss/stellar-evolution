#!/usr/bin/env python3
"""Stellar evolution stages from mass."""
import math

def lifetime_Gyr(mass_solar):
    """Main sequence lifetime = 10 Gyr / M^2.5."""
    return 10 / mass_solar**2.5

def final_state(mass_solar):
    """Predict end state based on initial mass."""
    if mass_solar < 0.08: return "Brown dwarf (never ignites)"
    if mass_solar < 8: return "White dwarf"
    if mass_solar < 25: return "Neutron star"
    return "Black hole"

def spectral_class(temp_k):
    classes = [(30000,"O"),(10000,"B"),(7500,"A"),(6000,"F"),(5200,"G"),(3700,"K"),(2400,"M")]
    for t, c in classes:
        if temp_k >= t: return c
    return "L"

if __name__ == "__main__":
    stars = [("0.1 Msun", 0.1), ("0.5 Msun", 0.5), ("1.0 Msun (Sun)", 1.0),
             ("3.0 Msun", 3.0), ("10 Msun", 10.0), ("25 Msun", 25.0), ("50 Msun", 50.0)]
    print("Stellar Evolution")
    for name, m in stars:
        life = lifetime_Gyr(m)
        state = final_state(m)
        print(f"  {name:18s}: life={life:.2f} Gyr -> {state}")\n