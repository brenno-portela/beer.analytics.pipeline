from airflow import DAG
from airflow.providers.papermill.operators.papermill import PapermillOperator
from datetime import datetime

with DAG(
    dag_id='executar_notebook_cerveja',
    start_date=datetime(2024, 1, 1),
    schedule_interval=None, 
    catchup=False
) as dag:

    rodar_analise = PapermillOperator(
        task_id="rodar_main_notebook",
        input_nb="/opt/airflow/dags/main.ipynb",
        output_nb="/opt/airflow/dags/resultado_main.ipynb",
        parameters={"execucao": "via_airflow"}
    )