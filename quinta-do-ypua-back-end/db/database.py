# conexão com o banco de dados

import psycopg2
from psycopg2 import OperationalError
import os


def create_connection():
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        # use variáveis de ambiente para as credenciais
        conn = psycopg2.connect(
            host=os.getenv('DB_HOST'),
            database=os.getenv('quinta_do_ypua'),
            user=os.getenv('postgress'),
            password=os.getenv('postgress')
        )
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    return conn
