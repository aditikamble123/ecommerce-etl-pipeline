🛒 E-Commerce ETL Pipeline (Python + MySQL)
📌 Overview

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline for e-commerce order data.

Raw CSV data is ingested, cleaned, transformed, and loaded into a MySQL data warehouse designed using a star schema to support analytical queries.

The pipeline is modular, production-oriented, and Airflow-ready for orchestration in a Linux environment.

🏗️ Architecture
CSV File
   ↓
Extract (Python)
   ↓
Transform (Cleaning, Validation, Normalization)
   ↓
Load (MySQL Data Warehouse)
   ↓
Analytics Queries

🛠️ Tech Stack

Python

Pandas

MySQL

SQLAlchemy

Apache Airflow (design-level orchestration)

Git & GitHub

📂 Project Structure
ecommerce-etl-pipeline/
│
├── etl/
│   ├── extract.py          # Data extraction logic
│   ├── transform.py        # Data cleaning & transformation
│   └── load.py             # Load data into MySQL
│
├── data/
│   └── ecommerce_orders_10k_updated.csv
│
├── sql/
│   └── create_tables.sql
│
├── dags/
│   └── etl_pipeline.py     # Airflow DAG (design-level)
│
├── test_etl.py             # Run ETL without Airflow
├── requirements.txt
├── .gitignore
└── README.md

🧠 Business Problem

E-commerce order data arrives as raw CSV files that may contain:

Duplicates

Inconsistent formats

Redundant fields

Business teams need clean, structured, and query-optimized data to analyze:

Revenue trends

Customer segments

Country-wise sales

Product performance

This project automates the conversion of raw data into analytics-ready tables.

🗄️ Data Warehouse Design (Star Schema)
Dimension Tables

customers_dim

user_id

country

customer_segment

products_dim

product_id

category

price

date_dim

date_id

order_date

year

month

day

Fact Table

orders_fact

order_id

user_id

product_id

date_id

qty

total_price

🔄 ETL Workflow
1️⃣ Extract

Reads raw CSV data using Pandas

2️⃣ Transform

Removes duplicates

Handles missing and invalid values

Converts date formats

Creates dimension and fact tables

Applies data quality validations

3️⃣ Load

Loads transformed data into MySQL

Uses chunked inserts for reliability (Windows-friendly)

Designed for safe re-runs during development

▶️ How to Run the Project
1️⃣ Create virtual environment
python -m venv venv

2️⃣ Activate virtual environment
# Windows
venv\Scripts\activate

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set MySQL password (environment variable)
set MYSQL_PASSWORD=your_mysql_password

5️⃣ Run ETL pipeline
python test_etl.py

✅ Expected Output
Starting ETL process...
Extracted 10000 rows
Transformation completed
Loading customers_dim...
Loading products_dim...
Loading date_dim...
Loading orders_fact...
Load step completed
ETL ran successfully

🔍 Verify Data in MySQL
USE ecommerce_dw;

SELECT COUNT(*) FROM orders_fact;
SELECT * FROM customers_dim LIMIT 5;

📊 Sample Analytics Query
SELECT
    country,
    SUM(total_price) AS total_revenue
FROM orders_fact o
JOIN customers_dim c
    ON o.user_id = c.user_id
GROUP BY country
ORDER BY total_revenue DESC;

⏰ Airflow Orchestration

An Apache Airflow DAG is included for scheduling and orchestration.

Due to Windows limitations, the DAG is design-level only, but it is fully compatible with Linux / WSL-based Airflow deployments.

🚀 Key Learnings

Built modular ETL pipelines using Python

Designed a star-schema data warehouse

Handled real-world dependency and driver issues

Implemented chunked bulk loading for MySQL

Designed Airflow-ready orchestration
