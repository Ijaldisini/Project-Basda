import Database as db
import os
import time
from register import register
from login import login

def clear_terminal():
    os.system('cls')

def kembali ():
    inputan_kembali = input("Tekan Enter untuk kembali ke menu utama...")
    if inputan_kembali == "":
        clear_terminal()

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
            login()

        elif pilihan == "3":
            clear_terminal()
            print('\n' + '=' * 20 + ' ANDA KELUAR DARI APLIKASI ' + '=' * 20 + '\n')
            time.sleep(1)
            clear_terminal()
            break

        else:
            print("Pilihan tidak valid.")
            kembali()
            
main()