import pandas as pd
from pathlib import Path


def load_gpu_prices():
    """
    Load raw GPU price data from CSV.
    """
    data_path = Path("data/raw/gpu_prices_raw.csv")

    if not data_path.exists():
        raise FileNotFoundError(f"Data file not found at {data_path}")

    df = pd.read_csv(data_path)

    return df


if __name__ == "__main__":
    df = load_gpu_prices()
    print("GPU Prices Raw Data Preview:")
    print(df.head())
    print(f"\nRows: {len(df)} | Columns: {len(df.columns)}")

