### Example script for a DAG
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator

default_args = {
    'owner': 'your_name',
    'start_date': datetime(2023, 6, 23),
    'retries': 1,
    'retry_delay': timedelta(minutes=5)
}

def task1():
    # Your task logic goes here
    print("Executing Task 1")

def task2():
    # Your task logic goes here
    print("Executing Task 2")

def task3():
    # Your task logic goes here
    print("Executing Task 3")

with DAG('sample_dag', default_args=default_args, schedule_interval=timedelta(days=1)) as dag:
    t1 = PythonOperator(
        task_id='task1',
        python_callable=task1
    )

    t2 = PythonOperator(
        task_id='task2',
        python_callable=task2
    )

    t3 = PythonOperator(
        task_id='task3',
        python_callable=task3
    )

    t1 >> t2 >> t3  # Define the task dependencies
