from core.Database import curr_db as db

def mlogin(no_hp, password):
    conn, cur = db()
    
    cur.execute("""SELECT id_akun, nama, role FROM akun
            WHERE no_hp = %s AND password = %s;
        """, (no_hp, password))
    
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    return result

def mregister_cek(no_hp):
    conn, cur = db()
    
    cur.execute("SELECT * FROM akun WHERE no_hp = %s", (no_hp,))
    
    result = cur.fetchone()
    
    cur.close()
    conn.close()
    return result

def mregister(nama, no_hp, password):
    conn, cur = db()
    
    cur.execute("""
        INSERT INTO akun (nama,no_hp,role,password)
        VALUES (%s, %s, %s, %s) RETURNING id_akun;
    """, (no_hp, nama, "P",password))
    id_akun = cur.fetchone()[0]
    
    conn.commit()
    
    conn.close()
    cur.close()
    return id_akun