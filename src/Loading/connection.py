import logging
import psycopg2
from src.settings import settings


def connection():
     try:
          conn = psycopg2.connect(
          host=settings.host,
          user=settings.user,
          password=settings.password,
          database=settings.db_name,
          port=settings.port
          )
          conn.autocommit = True
          return conn
     except:
         print('не удалось подключиться к базе данных')
         logging.error('не удалось подключиться к базе данных')






