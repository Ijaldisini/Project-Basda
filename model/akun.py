from core.Database import curr_db as db

def mlogin(no_hp, nama):
    conn, cur = db()
    
    cur.execute("""SELECT id_akun, nama, role FROM akun
            WHERE no_hp = %s AND nama = %s;
        """, (no_hp, nama))
    
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    return result

def mregister_cek(nama, no_hp):
    conn, cur = db()
    
    cur.execute("SELECT * FROM akun WHERE no_hp = %s", (no_hp,))
    
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    return result

def mregister(nama, no_hp):
    conn, cur = db()
    
    cur.execute("""
        INSERT INTO akun (no_hp, nama, role)
        VALUES (%s, %s, %s) RETURNING id_akun;
    """, (no_hp, nama, "P"))
    id_akun = cur.fetchone()[0]
    
    conn.commit()
    
    conn.close()
    cur.close()
    return id_akun