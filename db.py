from dotenv import load_dotenv
import psycopg2
import os

load_dotenv()

class db:
    def __enter__(self):
      conn = psycopg2.connect(os.environ["DATABASE_URL"])
      return conn

    def __exit__(self ,type, value, traceback):
      print('ok')
      return False