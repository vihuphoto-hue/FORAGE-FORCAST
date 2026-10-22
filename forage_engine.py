"""Transparent forage-budget calculations. Values are estimates, not veterinary advice."""
from typing import Dict

KG_PER_ACRE = 0.404685642  # hectares per acre; naming kept for readability

def calculate_budget(area_ha: float, standing_forage_kg_ha: float,
                     allowable_use_pct: float, reserve_pct: float,
                     regrowth_kg_ha_day: float, horizon_days: int,
                     weather_factor: float, animals: Dict) -> dict:
    """Compute a simplified forage budget from user-entered dry matter measurements.

    Safe supply = current standing DM * allowable use * reserve retention
                  + forecast regrowth during the period, adjusted by scenario factor.
    Important: this simplified calculation does not model seasonal growth curves,
    species-specific diet selection, inaccessible forage, or pasture quality constraints.
    """
    total_animals = sum(int(v["count"]) for v in animals.values())
    daily_demand = 0.0
    demand_by_species = {}
    for species, data in animals.items():
        # kg DM per animal per day = liveweight * intake fraction
        demand = int(data["count"]) * float(data["weight_kg"]) * float(data["intake_pct"]) / 100.0
        demand_by_species[species] = demand
        daily_demand += demand

    current_total_dm = max(0.0, area_ha * standing_forage_kg_ha)
    usable_fraction = max(0.0, min(1.0, allowable_use_pct / 100.0))
    reserve_fraction = max(0.0, min(1.0, 1.0 - reserve_pct / 100.0))
    regrowth = max(0.0, area_ha * regrowth_kg_ha_day * horizon_days)
    safe_supply = (current_total_dm * usable_fraction * reserve_fraction + regrowth * usable_fraction) * max(0.0, min(1.2, weather_factor))
    period_demand = daily_demand * horizon_days
    balance = safe_supply - period_demand
    coverage_days = safe_supply / daily_demand if daily_demand > 0 else None

    return {
        "total_animals": total_animals,
        "current_total_dm_kg": current_total_dm,
        "estimated_regrowth_kg": regrowth,
        "safe_supply_kg": safe_supply,
        "daily_demand_kg": daily_demand,
        "period_demand_kg": period_demand,
        "balance_kg": balance,
        "coverage_days": coverage_days,
        "demand_by_species_kg_day": demand_by_species,
        "weather_factor": weather_factor,
    }


def make_recommendations(result: dict, vegetation_quality: str, scenario: str,
                         paddocks: int, usable_acres: float, total_animals: int) -> list:
    advice = []
    if total_animals == 0:
        advice.append("Enter livestock numbers to calculate herd demand.")
    if result["balance_kg"] < 0:
        advice.append("Do not assume the planned herd can remain on the land for this period: reduce grazing pressure, shorten the grazing period, provide suitable supplementary feed, or use another verified forage source.")
        advice.append("Recalculate using fresh forage measurements and consider whether the stocking rate is sustainable for the full season.")
    else:
        advice.append("The entered forage budget covers the selected period mathematically; verify ground cover, regrowth, forage quality and animal condition before grazing.")
    if vegetation_quality in ("Very poor", "Poor"):
        advice.append("Forage quality is flagged as poor: obtain local feed/nutrition advice and assess whether supplementary feed is needed.")
    if scenario == "Water access problem":
        advice.append("Water safety lock: confirm reliable, clean water access for every paddock before placing livestock there.")
    if scenario == "Heavy rain / waterlogged soil":
        advice.append("Avoid grazing vulnerable waterlogged soils; inspect compaction, runoff and erosion risk before moving animals.")
    if scenario == "Dry spell stress test":
        advice.append("Drought response: inspect forage more frequently, preserve residual cover, and prepare an early destocking or supplementary-feed contingency.")
    advice.append(f"Initial layout: {paddocks} paddocks averaging {usable_acres / max(1, paddocks):.2f} usable acres each; adjust boundaries to terrain, water, shade, soil and sensitive habitat.")
    advice.append("Move livestock according to measured forage residual and recovery—not a fixed calendar alone. Protect riparian areas and keep an ungrazed recovery reserve where appropriate.")
    return advice


def forecast_budget(initial_supply_kg: float, daily_demand_kg: float, daily_regrowth_kg: float, days: int) -> list:
    """Simple daily supply trajectory for a chart or scenario simulation."""
    remaining = max(0.0, initial_supply_kg)
    rows = []
    for day in range(1, days + 1):
        remaining = max(0.0, remaining + max(0.0, daily_regrowth_kg) - max(0.0, daily_demand_kg))
        rows.append({"day": day, "estimated_remaining_forage_kg": remaining})
    return rows
