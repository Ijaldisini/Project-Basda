import psycopg2

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    database="DBBasda",
    user="postgres",
    password="@Raditya14",
    port=5432
    )     
    return conn

def curr_db():
    conn = connect_db()
    cur = conn.cursor()
    return conn, cur