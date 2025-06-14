import psycopg2
import Database as db
import time

def login():
    print('\n' + '=' * 20 + ' LOGIN ' + '=' * 20 + '\n')
    no_hp = input("No HP: ")
    nama = input("Nama: ")

    try:
        conn = db.connect_db()
        cur = conn.cursor()

        cur.execute("""
            SELECT id_akun, nama, role FROM akun
            WHERE no_hp = %s AND nama = %s;
        """, (no_hp, nama))
        user = cur.fetchone()

        if user:
            id_akun= user[0]
            nama= user[1]
            status = user[2]
            
            if status == "O":
                print("Anda owner")
                
            else : 
                print("Anda petani")
            
        else:
            input("Login gagal: Nomor HP atau nama salah!!!")
            time.sleep(1)
            login()

    except Exception as e:
        print("Terjadi kesalahan saat login:", e)
        
    finally:
        cur.close()
        conn.close()