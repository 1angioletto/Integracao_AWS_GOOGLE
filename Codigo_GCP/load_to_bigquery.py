from google.cloud import bigquery
import os
import pandas as pd

def read_and_write_to_bigquery(credentials_path, local_file_path, project_id, dataset_id, destination_table_id):
    # Verifica se o arquivo de credenciais existe
    if not os.path.exists(credentials_path):
        raise FileNotFoundError(f"O arquivo de credenciais não foi encontrado no caminho: {credentials_path}")
    
    # Configurar as credenciais do Google Cloud
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

    # Criação do cliente BigQuery
    client = bigquery.Client(project=project_id)

    # Verificar se o arquivo local existe
    if not os.path.exists(local_file_path):
        raise FileNotFoundError(f"O arquivo local não foi encontrado no caminho: {local_file_path}")

    # Carregar os dados do CSV para um DataFrame com codificação para evitar erros de leitura
    try:
        df = pd.read_csv(local_file_path, encoding='ISO-8859-1', delimiter=';', on_bad_lines='skip')  # 'skip' ignora linhas ruins
    except UnicodeDecodeError:
        raise ValueError(f"Erro de codificação ao ler o arquivo {local_file_path}. Verifique o formato do arquivo.")

    # Verificar se o DataFrame não está vazio
    if df.empty:
        raise ValueError(f"O arquivo {local_file_path} está vazio.")

    # Referência da tabela de destino no BigQuery
    destination_table_ref = client.dataset(dataset_id).table(destination_table_id)

    # Configuração do job para carregar os dados para o BigQuery
    job_config = bigquery.LoadJobConfig(
        write_disposition="WRITE_APPEND",  # Mudar para "WRITE_TRUNCATE" se quiser substituir a tabela
        source_format=bigquery.SourceFormat.CSV,
        skip_leading_rows=1,  # Caso o CSV tenha cabeçalho
        autodetect=True,  # Detectar automaticamente o esquema do CSV
    )

    try:
        # Carregar os dados para a tabela de destino
        load_job = client.load_table_from_dataframe(df, destination_table_ref, job_config=job_config)

        # Aguardar a conclusão do job de carga
        load_job.result()

        print(f"Carregamento de {local_file_path} para {destination_table_id} concluído!")

    except Exception as e:
        print(f"Ocorreu um erro ao carregar no BigQuery: {str(e)}")
        raise

# Caminho para o arquivo de credenciais do Google Cloud no container
credentials_path = r'C:\GCP\credenciais.json'  # Caminho no container

# Caminho local para o arquivo CSV que foi baixado do S3
local_file_path = r'C:\Users\Usuário\pedidos.csv'

# Detalhes do projeto e tabela do BigQuery
project_id = 'decent-trail-433100-t8'
dataset_id = 'pm_web'
destination_table_id = 'pm_web_pedidos'

# Chamar a função para carregar os dados no BigQuery
read_and_write_to_bigquery(credentials_path, local_file_path, project_id, dataset_id, destination_table_id)
