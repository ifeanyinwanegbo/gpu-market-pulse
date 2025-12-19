import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_PATH = BASE_DIR / "data" / "processed" / "gpu_prices_clean.csv"
DOCS_PATH = BASE_DIR / "docs"
DOCS_PATH.mkdir(exist_ok=True)

def analyze_market():
    df = pd.read_csv(DATA_PATH)

    summary = []

    summary.append("# GPU Market Summary\n")
    summary.append(f"Total Listings: {len(df)}\n")

    avg_price = df.groupby("brand")["price_usd"].mean().round(2)
    summary.append("## Average Price by Brand\n")
    summary.append(avg_price.to_string())
    summary.append("\n")

    availability = df["availability"].value_counts()
    summary.append("## Availability Breakdown\n")
    summary.append(availability.to_string())
    summary.append("\n")

    output_file = DOCS_PATH / "market_summary.md"
    output_file.write_text("\n".join(summary))

    print(f"Saved report: {output_file}")

if __name__ == "__main__":
    analyze_market()


