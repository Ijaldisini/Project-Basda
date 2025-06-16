import tabulate
from core.Database import curr_db as db

def mpenyakit_cek():
    conn, cur = db()
    cur.execute("SELECT id_penyakit, nama_penyakit, penanganan FROM penyakit")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def mgejala(id_penyakit):
    conn, cur = db()
    cur.execute("""
        SELECT g.id_gejala, g.gejala 
        FROM gejala g
        JOIN detail_penyakit dp ON g.id_gejala = dp.gejala_id_gejala
        WHERE dp.penyakit_id_penyakit = %s
    """, (id_penyakit,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def mgejala_semua():
    conn, cur = db()
    cur.execute("SELECT id_gejala, gejala FROM gejala")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data
