from core.Database import curr_db as db
from datetime import date
from controller.terminal import clear_terminal

def get_daftar_panen():
    conn, cur = db()
    cur.execute("""
        SELECT p.id_panen, b.nama_bibit, p.total_hasil_panen
        FROM panen p
        JOIN bibit_tanaman b ON p.id_bibit = b.id_bibit
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def insert_transaksi(id_akun):
    conn, cur = db()
    cur.execute("""
        INSERT INTO transaksi (tanggal, akun_id_akun)
        VALUES (%s, %s)
        RETURNING id_transaksi
    """, (date.today(), id_akun))
    id_transaksi = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return id_transaksi

def insert_detail_transaksi(jumlah, nominal, id_transaksi, id_panen):
    conn, cur = db()
    cur.execute("""
        INSERT INTO detail_transaksi (jumlah, nominal, transaksi_id_transaksi, panen_id_panen)
        VALUES (%s, %s, %s, %s)
    """, (jumlah, nominal, id_transaksi, id_panen))
    conn.commit()
    cur.close()
    conn.close()
