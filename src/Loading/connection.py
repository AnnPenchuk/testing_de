import psycopg2
from dotenv import load_dotenv
#from src.settings import Settings

#from src.settings import Settings_DATABASE

connection = psycopg2.connect(
        host ="127.0.0.1",
        user="admin",    #Settings.user,
        password="password",
        database="de_projects",
        port = "6432"
    )
connection.autocommit=True
