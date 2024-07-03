import psycopg2
from psycopg2 import OperationalError
import os


def create_connection():
    conn = None
    try:
      
        conn = psycopg2.connect(
            host=os.getenv('localhost'),
            database=os.getenv('postgres'),
            user=os.getenv('postgres'),
            password=os.getenv('12345')
        )
        return conn
    except OperationalError as e:
        print(f"The error '{e}' occurred")

    return conn
