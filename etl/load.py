from sqlalchemy import create_engine
from urllib.parse import quote_plus

MYSQL_USER = "root"
import os

MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD")

MYSQL_HOST = "localhost"
MYSQL_PORT = "3306"
MYSQL_DB = "ecommerce_dw"

ENCODED_PASSWORD = quote_plus(MYSQL_PASSWORD)

engine = create_engine(
    f"mysql+mysqldb://{MYSQL_USER}:{ENCODED_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
)

def load_data(customers_dim, products_dim, date_dim, orders_fact):
    customers_dim.to_sql("customers_dim", engine, if_exists="replace", index=False)
    products_dim.to_sql("products_dim", engine, if_exists="replace", index=False)
    date_dim.to_sql("date_dim", engine, if_exists="replace", index=False)
    orders_fact.to_sql("orders_fact", engine, if_exists="replace", index=False)
