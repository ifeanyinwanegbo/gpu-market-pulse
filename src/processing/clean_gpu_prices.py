import os
import pandas as pd

RAW_PATH = os.path.join("data", "raw", "gpu_prices_raw.csv")
OUT_PATH = os.path.join("data", "processed", "gpu_prices_clean.csv")

EXPECTED_COLS = [
    "date", "brand", "series", "model",
    "msrp_usd", "price_usd", "availability",
    "region", "source"
]

def clean_gpu_prices(df: pd.DataFrame) -> pd.DataFrame:
    # Basic column check
    missing = [c for c in EXPECTED_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing expected columns: {missing}")

    # Standardize text columns
    text_cols = ["brand", "series", "model", "availability", "region", "source"]
    for c in text_cols:
        df[c] = df[c].astype(str).str.strip()

    # Parse date
    df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Numeric cleanup
    for c in ["msrp_usd", "price_usd"]:
        df[c] = pd.to_numeric(df[c], errors="coerce")

    # Normalize availability values
    df["availability"] = (
        df["availability"]
        .str.lower()
        .str.replace(" ", "_", regex=False)
    )

    # Drop rows with critical missing values
    df = df.dropna(subset=["date", "brand", "model", "price_usd"])

    # Remove duplicates (same listing on same day)
    df = df.drop_duplicates(subset=["date", "brand", "model", "region", "source"], keep="last")

    # Add simple engineered feature
    df["markup_pct"] = ((df["price_usd"] - df["msrp_usd"]) / df["msrp_usd"]) * 100

    # Order columns nicely
    df = df[EXPECTED_COLS + ["markup_pct"]]

    return df

def main():
    df = pd.read_csv(RAW_PATH)
    clean = clean_gpu_prices(df)

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    clean.to_csv(OUT_PATH, index=False)

    print("Saved:", OUT_PATH)
    print(clean.head())
    print(f"\nRows: {len(clean)} | Columns: {len(clean.columns)}")

if __name__ == "__main__":
    main()

