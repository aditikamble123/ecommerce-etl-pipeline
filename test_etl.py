from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_etl():
    print("Starting ETL process...")

    # Extract
    df = extract_data()
    print(f"Extracted {len(df)} rows")

    # Transform
    customers_dim, products_dim, date_dim, orders_fact = transform_data(df)
    print("Transformation completed")

    # Load
    load_data(customers_dim, products_dim, date_dim, orders_fact)
    print("Data loaded into MySQL successfully")


if __name__ == "__main__":
    run_etl()
    print("ETL ran successfully")
