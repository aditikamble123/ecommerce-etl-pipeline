import pandas as pd

def extract_data():
    df = pd.read_csv("data/ecommerce_orders_10k_updated.csv")
    return df
