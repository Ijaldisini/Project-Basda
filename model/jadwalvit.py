from core.Database import curr_db as db
from controller.terminal import clear_terminal, kembali


def jadwal():
    clear_terminal()
    
    conn, cur = db()
    cur.execute("""
        SELECT dn.id_detail_nutrisi, n.nama_nutrisi, dn.dosis, b.nama_bibit
        FROM detail_nutrisi dn
        JOIN nutrisi n ON dn.nutrisi_id_nutrisi = n.id_nutrisi
        JOIN bibit_tanaman b ON dn.bibit_tanaman_id_bibit = b.id_bibit
        ORDER BY dn.id_detail_nutrisi ASC
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def tambah_jadwal(nutrisi_id, bibit_id, dosis):
    conn, cur = db()
    cur.execute("""
        INSERT INTO detail_nutrisi (nutrisi_id_nutrisi, bibit_tanaman_id_bibit, dosis)
        VALUES (%s, %s, %s)
    """, (nutrisi_id, bibit_id, dosis))
    conn.commit()
    cur.close()
    conn.close()

def nutrisi():
    conn, cur = db()
    cur.execute("SELECT id_nutrisi, nama_nutrisi FROM nutrisi")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def bibit():
    conn, cur = db()
    cur.execute("SELECT id_bibit, nama_bibit FROM bibit_tanaman")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
