import tabulate
from core.Database import curr_db as db

def datastokbibit_full():
    conn, cur = db()
    cur.execute("SELECT * FROM bibit_tanaman")
    data = cur.fetchall()
    cur.close()
    conn.close()
    print(tabulate.tabulate(data,headers=["ID Bibit", "Nama Bibit", "Stok", "Usia Panen", "Harga Perkg", "Harga Bibit", "ID Panen"], tablefmt="fancy_grid"))
    return data