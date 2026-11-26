import pandas as pd

REQUIRED_COLUMNS = ["stock_symbol", "date", "open",  "high", "low", "close" , "adj_close", "volume"]

def extract(path):
    df = pd.read_csv(path)

    missing = [col for col in REQUIRED_COLUMNS if col not in df.columns]

    if missing:
        raise ValueError(f"Missing columns: {missing}")

    print(f"Rows read: {len(df)}")
    print(f"Symbols: {sorted(df['stock_symbol'].unique())}")
    return df

if __name__ == "__main__":
    df = extract("data/raw/big_tech_stock_prices.csv")






 


    





