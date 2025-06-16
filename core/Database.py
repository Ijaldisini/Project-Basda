import psycopg2

def connect_db():
    conn = psycopg2.connect(
    host="localhost",
    database="Basda",
    user="postgres",
    password="syadid1306",
    port=5432
    )     
    return conn

def curr_db():
    conn = connect_db()
    cur = conn.cursor()
    return conn, cur