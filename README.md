🛒 E-Commerce ETL Pipeline (Python + MySQL)

📌 Overview



This project implements an end-to-end ETL (Extract, Transform, Load) pipeline for e-commerce order data.

Raw CSV data is ingested, cleaned, transformed, and loaded into a MySQL data warehouse designed using a star schema to support analytical queries.



The pipeline is modular, production-oriented, and Airflow-ready for orchestration in a Linux environment.



🏗️ Architecture

CSV File

&nbsp;  ↓

Extract (Python)

&nbsp;  ↓

Transform (Cleaning, Validation, Normalization)

&nbsp;  ↓

Load (MySQL Data Warehouse)

&nbsp;  ↓

Analytics Queries



🛠️ Tech Stack



Python



Pandas



MySQL



SQLAlchemy



Apache Airflow (design-level orchestration)



Git \& GitHub



📂 Project Structure

ecommerce-etl-pipeline/

│

├── etl/

│   ├── extract.py      # Data extraction logic

│   ├── transform.py    # Data cleaning \& transformation

│   └── load.py         # Load data into MySQL

│

├── data/

│   └── ecommerce\_orders\_10k\_updated.csv

│

├── sql/

│   └── create\_tables.sql

│

├── dags/

│   └── etl\_pipeline.py   # Airflow DAG (design-level)

│

├── test\_etl.py           # Run ETL without Airflow

├── requirements.txt

├── .gitignore

└── README.md



🧠 Business Problem



E-commerce order data arrives as raw CSV files that may contain duplicates, inconsistent formats, and redundant fields.

Business teams require clean, structured, and query-optimized data to analyze:



Revenue trends



Customer segments



Country-wise sales



Product performance



This project automates the process of converting raw data into analytics-ready tables.



🗄️ Data Warehouse Design (Star Schema)

Dimension Tables



customers\_dim

(user\_id, country, customer\_segment)



products\_dim

(product\_id, category, price)



date\_dim

(date\_id, order\_date, year, month, day)



Fact Table



orders\_fact

(order\_id, user\_id, product\_id, date\_id, qty, total\_price)



🔄 ETL Workflow

1️⃣ Extract



Reads raw CSV data using Pandas



2️⃣ Transform



Removes duplicates



Handles missing/invalid values



Converts date formats



Creates dimension and fact tables



Applies data quality validations



3️⃣ Load



Loads transformed data into MySQL



Uses chunked inserts for reliability on Windows



Designed for re-runs during development



▶️ How to Run the Project

1️⃣ Create virtual environment

python -m venv venv



2️⃣ Activate virtual environment

\# Windows

venv\\Scripts\\activate



3️⃣ Install dependencies

pip install -r requirements.txt



4️⃣ Set MySQL password (environment variable)

set MYSQL\_PASSWORD=your\_mysql\_password



5️⃣ Run ETL

python test\_etl.py



✅ Expected Output

Starting ETL process...

Extracted 10000 rows

Transformation completed

Loading customers\_dim...

Loading products\_dim...

Loading date\_dim...

Loading orders\_fact...

Load step completed

ETL ran successfully



🔍 Verify Data in MySQL

USE ecommerce\_dw;



SELECT COUNT(\*) FROM orders\_fact;

SELECT \* FROM customers\_dim LIMIT 5;



📊 Sample Analytics Query

SELECT

&nbsp; country,

&nbsp; SUM(total\_price) AS total\_revenue

FROM orders\_fact o

JOIN customers\_dim c

&nbsp; ON o.user\_id = c.user\_id

GROUP BY country

ORDER BY total\_revenue DESC;



⏰ Airflow Orchestration



An Apache Airflow DAG is included for scheduling and orchestration.

Due to Windows limitations, the DAG is design-level, but fully compatible with Linux/WSL-based Airflow deployments.



🚀 Key Learnings



Built modular ETL pipelines using Python



Designed a star-schema data warehouse



Handled real-world dependency and driver issues



Implemented chunked bulk loading for MySQL



Designed Airflow-ready orchestration

