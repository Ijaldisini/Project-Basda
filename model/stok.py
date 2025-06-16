from core.Database import curr_db as db

def datastokbibit_full():
    conn, cur = db()
    cur.execute("SELECT * FROM bibit_tanaman")
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def datastoksayur_full():
    conn, cur = db()
    cur.execute("""SELECT rb.id_rak, bt.nama_bibit, rb.bibit_per_rak ,p.tanggal_tanam, p.tanggal_panen, p.batas_panen, p.total_hasil_panen 
                FROM rak_budidaya rb 
                join panen p on (rb.panen_id_panen=p.id_panen) 
                join bibit_tanaman bt on (p.bibit_tanaman_id_bibit=bt.id_bibit)
                """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data