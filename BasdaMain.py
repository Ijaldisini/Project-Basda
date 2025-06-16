import time
import tabulate
from controller.register import register
from controller.login import login
from controller.terminal import clear_terminal, kembali
import model.stok as stok
from controller.stok import tambah_stok, kelola_siklus_rak
from controller.penyakit import deteksi_penyakit
from controller.jadwalvit import jadwal_vitamin
from controller.transaksi import transaksi_penjualan, lihat_riwayat

def main():
    while True:
        clear_terminal()
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
                    menu_owner(result[1], result[2])
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
            
def menu_owner(nama, id_akun):
    while True :
        clear_terminal()
        print('\n' + '=' * 20 + f' Halo {nama} selamat datang di Aplikasi Petani!!! ' + '=' * 20 + '\n')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	     MENU OWNER              ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Lihat Stok                  ||')
        print('||                2. Penjualan                   ||')
        print('||                3. Keluar                      ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            clear_terminal()
            menu_stok_owner()
            
        elif pilihan == "2":
            clear_terminal()
            lihat_riwayat(id_akun)
            
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
            menu_stok_petani()
            
        elif pilihan == "2":
            clear_terminal()
            transaksi_penjualan(id_akun)
            
        elif pilihan == "3":
            clear_terminal()
            jadwal_vitamin()
            
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

def menu_stok_owner():
    while True:
        clear_terminal()
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	      MENU PENGELOLAAN STOK          ^^^ ||')
        print('||---------    Silahkan pilih menu       ---------||')
        print('||    1. Tampilkan Stock Bibit                    ||')
        print('||    2. Tampilkan Sayur                          ||')
        print('||    3. Keluar                                   ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        if pilihan == "1" :
            clear_terminal()
            data = stok.datastokbibit_full()
            print (tabulate.tabulate(data,headers=["ID Bibit", "Nama Bibit", "Stok", "Usia Panen","Hasil Panen Per Bibit", "Harga Perkg", "Harga Bibit"], tablefmt="fancy_grid"))
            input("Tekan Enter Untuk Kembali....")
        elif pilihan == "2":
            clear_terminal()
            data = stok.datastoksayur_full()
            print (tabulate.tabulate(data,headers =["ID Rak","Bibit Tanaman","Bibit Per Rak","Tanggal Tanam","Tanggal Panen","Batas Panen","Total Hasil Panen"],tablefmt="fancy_grid"))
            input("Tekan Enter Untuk Kembali....")
            
        elif pilihan == "3":
            break
        
def menu_stok_petani():
    clear_terminal()
    data = stok.datastokbibit_full()
    while True:
        print (tabulate.tabulate(data,headers=["ID Bibit", "Nama Bibit", "Stok", "Usia Panen","Hasil Panen Per Bibit", "Harga Perkg", "Harga Bibit"], tablefmt="fancy_grid"))
        
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	      MENU PENGELOLAAN STOK          ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||              1. Kelola tanaman                ||')
        print('||              2. Tambah bibit                  ||')
        print('||              3. Keluar                        ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()
        
        if pilihan == "1":
            clear_terminal()
            kelola_siklus_rak()
        
        elif pilihan == "2":
            clear_terminal()
            tambah_stok()
            
        elif pilihan == "3":
            break
        
        else:
            print("Pilihan tidak valid.")
            kembali()
            
main()