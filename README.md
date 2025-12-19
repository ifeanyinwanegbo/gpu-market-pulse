
# GPU Market Pulse

GPU Market Pulse is an end-to-end data engineering and analytics project that tracks GPU pricing, availability, and market trends across major vendors such as NVIDIA and AMD. The project demonstrates how raw market data can be ingested, cleaned analyzed, and transformed into an automated, insight-driven report using a modular pipeline design similar to real-world analytics systems.

---

## 📌 Project Overview

This project answers practical market questions such as:
- How do GPU prices compare across brands?
- How far are market prices deviating from MSRP?
- What is the current availability of GPUs in the market?
- Can market insights be generated automatically from raw data?

The pipeline is fully script-driven and produces a structured analytics report without manual intervention.

---

## 🏗️ Architecture

The project follows a modular pipeline architecture with clear separation of concerns:

1. **Ingestion Layer**
   - Loads raw GPU pricing data from CSV sources.
   - Handles schema validation and data loading.

2. **Processing Layer**
   - Cleans and standardizes the raw data.
   - Converts prices to numeric format.
   - Calculates price deviation from MSRP.

3. **Analytics Layer**
   - Aggregates pricing and availability metrics.
   - Computes brand-level statistics.
   - Generates a structured market summary.

4. **Reporting Layer**
   - Automatically writes insights to a Markdown report for easy sharing and review.

This structure mirrors production-grade data analytics workflows.

---

## 📁 Project Structure
```text
gpu-market-pulse/
├── data/
│ ├── raw/
│ │ └── gpu_prices_raw.csv
│ └── processed/
│ └── gpu_prices_clean.csv
├── docs/
│ └── market_summary.md
├── src/
│ ├── ingestion/
│ │ └── load_gpu_prices.py
│ ├── processing/
│ │ └── clean_gpu_prices.py
│ └── analytics/
│ └── analyze_gpu_market.py
```
├── notebooks/
├── docker/
├── README.md
└── LICENSE

