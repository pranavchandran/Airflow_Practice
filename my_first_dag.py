from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime

def start_task():
    print("Hello from task 1")

def end_task():
    print("Hello from task 2")

default_args = {
    'start_date': datetime(2023, 1, 1),
    'catchup': False
}

with DAG('test_dag_ok',
         schedule_interval='@daily',
         default_args=default_args,
         description='Test DAG working fine'
         ) as dag:

    t1 = PythonOperator(
        task_id='start',
        python_callable=start_task
    )

    t2 = PythonOperator(
        task_id='end',
        python_callable=end_task
    )

    t1 >> t2
