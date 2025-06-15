from Database import curr_db as db
import time
from terminal import clear_terminal, kembali
from M_Akun import mlogin

def login():
    clear_terminal()
    print('\n' + '=' * 20 + ' LOGIN ' + '=' * 20 + '\n')
    no_hp = input("No HP: ")
    nama = input("Nama: ")

    try:
        user = mlogin(no_hp, nama)

        if user:
            id_akun= user[0]
            nama= user[1]
            status = user[2]
            
            if status == "O":
                return("owner", nama)
                
            else : 
                return("petani", id_akun, nama)
            
        else:
            input("Login gagal: Nomor HP atau nama salah!!!")
            time.sleep(1)
            kembali()

    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        time.sleep(1)
        kembali()
        
    finally:
        conn, cur = db()
        cur.close()
        conn.close()