# Project: Supercar Liquidity Scanner (Malaysia)

**Status:** Active | **Type:** Market Arbitrage Tool | **Language:** Python

### 📉 The Thesis
The Malaysian high-end automotive market exhibits a decoupling between **Sales Volume** and **Credit Quality**. While registration numbers for luxury vehicles (Porsche, Lamborghini, etc.) are up, household debt data suggests a rising default rate in the sub-prime/shadow financing layer.

This tool was built to scrape, quantify, and visualize that distress signal.

### 🛠 What This Tool Does
1.  **Market Scanning:** Ingests listing data (Price, Model, Description).
2.  **Natural Language Processing (NLP):** Scans for distress keywords indicating financial duress:
    * *"Sambung Bayar"* (Illegal Loan Continuation)
    * *"Lari Bank"* (Absconding/Default Risk)
    * *"Cash Only / Urgent"* (Liquidity Crisis)
3.  **Valuation Engine:**
    * Calculates **Enterprise Value** (Upfront Cash + Remaining Loan Liability).
    * Compares against **Fair Market Value (FMV)** baselines.
    * Generates a **Spread %** (Arbitrage Opportunity).
4.  **Risk Scoring:** Assigns a "Beta" to each asset class to weight the risk of illiquidity (e.g., a McLaren has a higher liquidity risk/beta than a Honda Civic).


## ⚠️ Disclaimer
This tool is for **educational and research purposes only**. It uses synthetic data generation for demonstration to comply with web scraping policies.

"Sambung Bayar" (loan continuation) deals often exist in a legal grey area in Malaysia. This tool scans listing data but does not verify the legality of any specific transaction. Proceed with caution and consult legal counsel before engaging in such deals.

### 📊 Logic Sample
```python
# The "Gamble" Equation
if margin_pct > 25 and risk_score >= 30:
    verdict = "⚠️ HIGH RISK GAMBLE"
# The "Alpha" Equation
elif margin_pct > 15 and risk_score < 15:
    verdict = "💎 PRIME ALPHA"
