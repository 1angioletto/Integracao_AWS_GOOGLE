import boto3

def download_file_from_s3(bucket_name, object_key, local_file_path):
    # Criando uma sessão boto3 sem as credenciais diretamente no código
    session = boto3.Session(
        region_name="us-east-1"  # Substitua pela sua região, se necessário
    )
    
    # Usando o cliente configurado com as credenciais do AWS CLI
    s3_client = session.client('s3')
    
    # Baixar o arquivo do S3 para o diretório local
    s3_client.download_file(bucket_name, object_key, local_file_path)
    print(f"Arquivo {object_key} do bucket {bucket_name} baixado para {local_file_path}")

# Definir o nome do bucket e o objeto (arquivo) no S3
bucket_name = "teste"  # Nome do seu bucket no S3
object_key = "PEDIDOS.csv"  # Nome do arquivo no S3

# Caminho onde o arquivo será salvo localmente
local_file_path = r'C:\Users\Usuário\OneDrive\Fluxo\dados\pedidos.csv'  # Caminho completo onde o arquivo será salvo

# Chamar a função para fazer o download
download_file_from_s3(bucket_name, object_key, local_file_path)
