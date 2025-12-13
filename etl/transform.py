import pandas as pd

def transform_data(df):
    df = df.drop_duplicates()

    # Convert date
    df["order_date"] = pd.to_datetime(df["order_date"], dayfirst=True)

    # Data quality checks
    df = df[df["price"] >= 0]
    df = df[df["qty"] > 0]

    # Dimensions
    customers_dim = df[["user_id", "country", "customer_segment"]].drop_duplicates()
    products_dim = df[["product_id", "category", "price"]].drop_duplicates()

    date_dim = df[["order_date"]].drop_duplicates()
    date_dim["date_id"] = date_dim["order_date"].dt.strftime("%Y%m%d").astype(int)
    date_dim["year"] = date_dim["order_date"].dt.year
    date_dim["month"] = date_dim["order_date"].dt.month
    date_dim["day"] = date_dim["order_date"].dt.day

    # Fact table
    orders_fact = df.merge(date_dim, on="order_date")[[
        "order_id", "user_id", "product_id", "date_id", "qty", "total_price"
    ]]

    return customers_dim, products_dim, date_dim, orders_fact
