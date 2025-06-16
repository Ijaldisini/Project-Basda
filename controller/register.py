import psycopg2
from core.Database import curr_db as db
import time
from controller.terminal import clear_terminal, kembali
from model.akun import mregister_cek, mregister

def register():
    clear_terminal()
    print('\n' + '=' * 20 + ' REGISTRASI AKUN ' + '=' * 20 + '\n')
    nama = input("Nama : ")
    no_hp = input("No HP: ")
    password = input("Password: ")
    
    cek = mregister_cek(no_hp)
    conn, cur = db()
    
    if cek is not None:
        print("Registrasi gagal: Nomor HP sudah digunakan!!!")
        time.sleep(1)
        kembali()
    
    try:
        if cek is None:
            mregister(nama, no_hp,password)
            
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