import time
from controller.register import register
from controller.login import login
from controller.terminal import clear_terminal, kembali
from model.stok import data_full
from controller.penyakit import deteksi_penyakit

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
        print('||                1. Stok                        ||')
        print('||                2. Penjualan                   ||')
        print('||                3. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            clear_terminal()
            menu_stok()
            
        elif pilihan == "2":
            print("penjualan")
            
        elif pilihan == "3":
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
        print('||                1. Stok                        ||')
        print('||                2. Penjualan                   ||')
        print('||                3. Jadwal vitamin              ||')
        print('||                4. Deteksi penyakit            ||')
        print('||                5. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            clear_terminal()
            menu_stok()
            
        elif pilihan == "2":
            print("penjualan")
            
        elif pilihan == "3":
            print("jadwal vitamin")
            
        elif pilihan == "4":
            clear_terminal()
            deteksi_penyakit()
            
        elif pilihan == "5":
            print("Terima kasih telah menggunakan aplikasi ini.")
            kembali()
            clear_terminal()
            break
        
        else:
            print("Pilihan tidak valid.")

def menu_stok():
    data = data_full()
    while True:
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	      MENU PENGELOLAAN STOK          ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||    1. Tampilkan Sayur Berdasar Stok           ||')
        print('||    2. Tampilkan Sayur Berdasarkan Urutan Nama ||')
        print('||    3. Cari Sayur dan Ganti Harga              ||')
        print('||    4. Tambah Sayur                            ||')
        print('||    5. Hapus Sayur                             ||')
        print('||    6. Tambah Stock                            ||')
        print('||    7. Kembali                                 ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
main()