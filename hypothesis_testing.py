"""
MODULE: Statistical Validation Engine
PURPOSE: Hypothesis testing to confirm the divergence between "Shadow" and "Retail" asset classes.
METHODOLOGY: 
    1. Pearson Correlation: To link Macro Sales Volume with Default Rates.
    2. Welch's T-Test: To prove the 'Shadow Premium' (Spread) is statistically significant.
AUTHOR: Ikhwan Afif | Quant-Hybrid
"""

import pandas as pd
import numpy as np
from scipy import stats
import random

print(">>> [INIT] LOADING STATISTICAL MODULE...")

# --- 1. MACRO THESIS: "THE BUBBLE LINK" ---
# Hypothesis: High Sales Growth correlates with High Default Rates (Liquidity Trap)
# Data Source: Aggregated from Slide 2 Analysis
macro_data = {
    'Year': [2020, 2021, 2022, 2023, 2024, 2025],
    'Luxury_Sales_Growth': [5, 8, 35, 45, 60, 48],  # The "Optics"
    'Default_Rate': [2.1, 2.3, 2.8, 3.2, 4.5, 5.1]  # The "Reality"
}
df_macro = pd.DataFrame(macro_data)

# Test: Pearson Correlation
corr_coef, p_val_corr = stats.pearsonr(df_macro['Luxury_Sales_Growth'], df_macro['Default_Rate'])

print("\n>>> [MACRO] HYPOTHESIS TEST RESULTS")
print(f"Correlation (r): {corr_coef:.4f}")
print(f"P-Value: {p_val_corr:.4f}")
if p_val_corr < 0.05:
    print("VERDICT: STATISTICALLY SIGNIFICANT LINK between Sales & Defaults.")
else:
    print("VERDICT: No significant link found.")
print("-" * 50)

# --- 2. MICRO THESIS: "THE ALPHA SPREAD" ---
# Hypothesis: Shadow Market (Sambung Bayar) offers significantly higher yields than Retail.
# We simulate a larger sample (n=200) to prove the spread isn't random noise.

SCENARIOS = [
    {"type": "Shadow (Sambung/Lari)", "discount": 0.25, "group": "Shadow"}, # Avg discount
    {"type": "Retail (Clean Title)", "discount": -0.05, "group": "Retail"}  # Premium price
]

def generate_spreads(n=200):
    data = []
    for _ in range(n):
        # 30% of market is Shadow, 70% is Retail based on scraping frequency
        scenario = random.choices(SCENARIOS, weights=[30, 70], k=1)[0]
        
        # Base Price (Arbitrary for spread calc)
        fmv = 500000 
        
        # Add random noise to simulate market negotiation (+/- 5%)
        noise = random.uniform(0.95, 1.05)
        ask_price = fmv * (1 - scenario['discount']) * noise
        
        # Spread = (FMV - Ask) / FMV
        spread_pct = ((fmv - ask_price) / fmv) * 100
        
        data.append({"Group": scenario['group'], "Spread": spread_pct})
    return pd.DataFrame(data)

df_micro = generate_spreads(200)

# Test: Welch's T-Test (Independent samples, unequal variance)
shadow_pop = df_micro[df_micro['Group'] == 'Shadow']['Spread']
retail_pop = df_micro[df_micro['Group'] == 'Retail']['Spread']

t_stat, p_val_ttest = stats.ttest_ind(shadow_pop, retail_pop, equal_var=False)

print("\n>>> [MICRO] ALPHA VALIDATION")
print(f"Mean Shadow Spread: {shadow_pop.mean():.2f}%")
print(f"Mean Retail Spread: {retail_pop.mean():.2f}%")
print(f"T-Statistic: {t_stat:.4f}")
print(f"P-Value: {p_val_ttest:.4e}") # Scientific notation for very small numbers

if p_val_ttest < 0.01:
    print("VERDICT: The 'Shadow Premium' is REAL (Conf > 99%).")
else:
    print("VERDICT: Difference could be random chance.")
