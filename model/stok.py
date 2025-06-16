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

def sayur_panen():
    conn, cur = db()
    cur.execute("""
        SELECT rb.id_rak, bt.nama_bibit, rb.bibit_per_rak,
               p.id_panen, p.tanggal_tanam, p.tanggal_panen, 
               p.batas_panen, p.total_hasil_panen,
               p.bibit_tanaman_id_bibit  -- tambahkan ini
        FROM rak_budidaya rb 
        JOIN panen p ON rb.panen_id_panen = p.id_panen 
        JOIN bibit_tanaman bt ON p.bibit_tanaman_id_bibit = bt.id_bibit
        WHERE p.batas_panen > CURRENT_DATE AND p.tanggal_panen < CURRENT_DATE
    """)
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def insert_bibit(nama_bibit, stok_bibit, usia_panen, hasil_perbibit, harga_perkg, harga_bibit):
    conn, cur = db()
    cur.execute("""
        INSERT INTO bibit_tanaman (nama_bibit, stok, usia_panen, hasil_panen_perbibit, harga_perkg, harga_bibit)
        VALUES (%s, %s, %s, %s, %s, %s)
    """, (nama_bibit, stok_bibit, usia_panen, hasil_perbibit, harga_perkg, harga_bibit))
    conn.commit()
    cur.close()
    conn.close()

def insert_panen(id_bibit, tgl_tanam, tgl_panen, batas_panen, total_hasil):
    conn, cur = db()
    cur.execute("""
        INSERT INTO panen (
            bibit_tanaman_id_bibit, tanggal_tanam, tanggal_panen, batas_panen, total_hasil_panen
        ) VALUES (%s, %s, %s, %s, %s)
        RETURNING id_panen
    """, (id_bibit, tgl_tanam, tgl_panen, batas_panen, total_hasil))
    
    id_baru = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return id_baru



def update_rak_dengan_panen(id_rak, id_panen_baru):
    conn, cur = db()
    cur.execute("""
        UPDATE rak_budidaya SET panen_id_panen = %s WHERE id_rak = %s
    """, (id_panen_baru, id_rak))
    conn.commit()
    cur.close()
    conn.close()
