from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data

with DAG(
    "ecommerce_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@daily",
    catchup=False
) as dag:

    extract = PythonOperator(
        task_id="extract",
        python_callable=extract_data
    )

    transform = PythonOperator(
        task_id="transform",
        python_callable=transform_data
    )

    load = PythonOperator(
        task_id="load",
        python_callable=load_data
    )

    extract >> transform >> load
