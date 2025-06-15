import time
from register import register
from login import login
from terminal import clear_terminal, kembali

def main():
    clear_terminal()
    while True:
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	        MENU                 ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Register                    ||')
        print('||                2. Login                       ||')
        print('||                3. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()

        if pilihan == "1":
            clear_terminal()
            register()

        elif pilihan == "2":
            clear_terminal()
            result = login()
            if result:
                if result[0] == "owner":
                    menu_owner(result[1])
                else:
                    menu_petani(result[1], result[2])

        elif pilihan == "3":
            clear_terminal()
            print('\n' + '=' * 20 + ' ANDA KELUAR DARI APLIKASI ' + '=' * 20 + '\n')
            time.sleep(1)
            clear_terminal()
            break

        else:
            print("Pilihan tidak valid!!")
            kembali()
            
def menu_owner(nama):
    while True :
        clear_terminal()
        print('\n' + '=' * 20 + f' Halo {nama} selamat datang di Aplikasi Petani!!! ' + '=' * 20 + '\n')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	     MENU OWNER              ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Penjualan Hasil Tani        ||')
        print('||                2. Rute Pengiriman             ||')
        print('||                3. Pencatatan Transaksi        ||')
        print('||                4. Pengelolaan Stok            ||')
        print('||                5. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            print("kau")
            
        elif pilihan == "2":
            print("an")
            
        elif pilihan == "3":
            print("coba")
        
        elif pilihan == "4":
            print("lagi")
        
        elif pilihan == "5":
            clear_terminal()
            print('\n' + '=' * 20 + ' TERIMA KASIH TELAH MENGGUNAKAN APLIKASI TANI ' + '=' * 20 + '\n')
            time.sleep(1)
            clear_terminal()
            break
        
        else:
            print("Pilihan tidak valid.")
            kembali()
        
def menu_petani(id_akun, nama):
    while True :
        clear_terminal()
        print('\n' + '=' * 20 + f' Halo {nama} selamat datang di Aplikasi Petani!!! ' + '=' * 20 + '\n')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	    MENU PETANI              ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Beli Hasil Tani             ||')
        print('||                2. Riwayat Pembelian           ||')
        print('||                3. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            print("id_akun")
            
        elif pilihan == "2":
            print("id_akun")
            
        elif pilihan == "3":
            print("Terima kasih telah menggunakan aplikasi ini.")
            clear_terminal()
            break
        
        else:
            print("Pilihan tidak valid.")
            
main()