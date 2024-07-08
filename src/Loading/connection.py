import psycopg2

connection = psycopg2.connect(
        host="127.0.0.1",
        user="admin",
        password="password",
        database="de_projects",
        port = "6432"
    )
connection.autocommit=True
