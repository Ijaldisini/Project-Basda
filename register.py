import psycopg2
import Database as db
import time
from terminal import clear_terminal, kembali

def register():
    clear_terminal()
    print('\n' + '=' * 20 + ' REGISTRASI AKUN ' + '=' * 20 + '\n')
    nama = input("Nama: ")
    no_hp = input("No HP: ")
    
    conn = db.connect_db()
    cur = conn.cursor()
    
    cur.execute("SELECT * FROM akun WHERE no_hp = %s", (no_hp,))
    no_hp2 = cur.fetchone()
    
    if no_hp2 is not None:
        print("Registrasi gagal: Nomor HP sudah digunakan!!!")
        time.sleep(1)
        kembali()
    
    try:
        if no_hp2 is None:
            # Insert ke tabel akun
            cur.execute("""
                INSERT INTO akun (no_hp, nama, role)
                VALUES (%s, %s, %s) RETURNING id_akun;
            """, (no_hp, nama, "P"))
            id_akun = cur.fetchone()[0]

            conn.commit()
            print("Registrasi berhasil!")
            time.sleep(1)
            kembali()
            
    except psycopg2.IntegrityError:
        conn.rollback()
        input("Registrasi gagal: Nomor HP sudah digunakan atau data tidak valid.")
        time.sleep(1)
        kembali()
        
    except Exception as e:
        conn.rollback()
        input("Terjadi kesalahan:", e)
        time.sleep(1)
        kembali()
        
    finally:
        cur.close()
        conn.close()