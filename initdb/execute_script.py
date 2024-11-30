import pandas as pd
import mysql.connector

# Configuração do banco de dados
db_config = {
    'host': 'sql.freedb.tech',
    'user': 'freedb_Teste',
    'password': 'Bnp2cMErZ*38p4&',
    'database': 'freedb_teste_teste'
}

# Função para carregar dados do Excel para o banco
def load_excel_to_db(file_path, table_name):
    try:
        # Carregando o arquivo Excel
        df = pd.read_csv(file_path, sep="|")

        # Conexão com o banco
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

       

        # Preparando o INSERT
        columns = ", ".join(df.columns)  # Usa os nomes das colunas diretamente do DataFrame
        placeholders = ", ".join(["%s"] * len(df.columns))
        sql_insert = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"

       # Inserindo os dados
        for _, row in df.iterrows():
            values = tuple(row)
            print(values)
            cursor.execute(sql_insert, values)

        # Commit das alterações
        connection.commit()
        print(f"{cursor.rowcount} registros inseridos na tabela {table_name}!")

    except Exception as err:
        print(f"Erro: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

# Arquivos e tabelas
files_and_tables = [
    {
        "file_path": "escolas.csv",
        "table_name": "escola",
    },
    # {
    #     "file_path": "C:\\caminho\\para\\alunos.xlsx",
    #     "table_name": "alunos",
    # }
]

# Executando para cada arquivo
for file_info in files_and_tables:
    load_excel_to_db(
        file_info["file_path"],
        file_info["table_name"],
    )
