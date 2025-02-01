from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract_
from transform import transform
from load import load

# Define default arguments for the DAG
default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2025, 1, 1),
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=60),
}

# Define the DAG
dag = DAG(
    'etl_pipeline',
    default_args=default_args,
    description='Job ETL pipeline',
    schedule_interval=timedelta(days=90),
)

# Define the tasks
extract_task = PythonOperator(
    task_id='extract',
    python_callable=extract_,
    provide_context=True,
    dag=dag,
)

transform_task = PythonOperator(
    task_id='transform',
    python_callable=transform,
    provide_context=True,
    dag=dag,
)

load_task = PythonOperator(
    task_id='load',
    python_callable=load,
    provide_context=True,
    dag=dag,
)

# Set the task dependencies
extract_task >> transform_task >> load_task