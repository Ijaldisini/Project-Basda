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

def get_riwayat_transaksi(id_akun):
    conn, cur = db()
    cur.execute("""
        SELECT t.id_transaksi, t.tanggal, b.nama_bibit, dt.jumlah, dt.nominal
        FROM transaksi t
        JOIN detail_transaksi dt ON dt.transaksi_id_transaksi = t.id_transaksi
        JOIN panen p ON dt.panen_id_panen = p.id_panen
        JOIN bibit_tanaman b ON p.bibit_tanaman_id_bibit = b.id_bibit
        WHERE t.akun_id_akun = %s
        ORDER BY t.tanggal DESC
    """, (id_akun,))
    data = cur.fetchall()
    cur.close()
    conn.close()
    return data

def get_harga_perkg(id_bibit):
    conn, cur = db()
    cur.execute("SELECT harga_perkg FROM bibit_tanaman WHERE id_bibit = %s", (id_bibit,))
    hasil = cur.fetchone()
    cur.close()
    conn.close()
    return hasil[0] if hasil else 0

def update_hasil_panen(id_panen, jumlah_gram):
    conn, cur = db()
    cur.execute("""
        UPDATE panen
        SET total_hasil_panen = total_hasil_panen - %s
        WHERE id_panen = %s
    """, (jumlah_gram, id_panen))
    conn.commit()
    cur.close()
    conn.close()