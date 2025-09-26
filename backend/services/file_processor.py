import pandas as pd
def validate_df(df, required):
    missing = [c for c in required if c not in df.columns]
    return missing
def process_hosts_df(df):
    # basic normalization
    df = df.rename(columns=lambda c: c.strip())
    return df
