from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta

def print_exec_date(**context):
    execution_date = context['execution_date']
    print(f"Execution date: {execution_date}")
    
default_args = {
    'owner': 'Pranav C',
    'start_date': datetime(2025, 4, 10),
    'retries': 0,
}

with DAG(
    dag_id='print_execution_date_dag',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True,
    tags=['Final test'],
    description='Test DAG working fine'
) as dag:
    # Define the task
    print_task = PythonOperator(
        task_id='print_execution_date',
        python_callable=print_exec_date,
        provide_context=True
    )
