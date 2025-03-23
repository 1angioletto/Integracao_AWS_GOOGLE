from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from python.download_from_s3 import download_file_from_s3  # Função que baixa o arquivo do S3
from python.load_to_bigquery import load_to_bigquery

# Configuração da DAG
with DAG(
    dag_id="pmweb_integracao",
    start_date=datetime(2023, 3, 25),  # Data de início
    schedule_interval=None,  # Definido como "None" para execução manual
) as dag:
  
    # Tarefa para baixar os dados do S3
    download_from_s3_task = PythonOperator(
        task_id='download_from_s3',
        python_callable=download_file_from_s3,  # Chama a função de download
        op_args=["teste", "CADASTROS.csv", "/path/to/local/cadastro.csv"],  # Adicionar os parâmetros necessários
    )

    # Tarefa para carregar dados no BigQuery
    load_to_bigquery_task = PythonOperator(
        task_id='load_to_bigquery',
        python_callable=load_to_bigquery,  # Chama a função de carregamento para BigQuery
    )

    # Definir a ordem das tarefas
    download_from_s3_task >> load_to_bigquery_task
