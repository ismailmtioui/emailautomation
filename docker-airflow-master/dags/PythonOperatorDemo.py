from datetime import datetime

from airflow.models import DAG, Variable
from airflow.operators.python_operator import PythonOperator
from bots.Python_Helper import call  # Assuming this line exists

default_args = {
    'owner': 'Ismailelmtioui',
    'start_date': datetime(2024, 4, 14)
}

with DAG(
    dag_id="PythonOperatorDemo1",
    default_args=default_args,
    schedule_interval=None
) as dag:

    start_dag = PythonOperator(
        task_id='start_dag',
        python_callable=call
    )

    start_dag