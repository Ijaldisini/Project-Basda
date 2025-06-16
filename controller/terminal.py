import os

def clear_terminal():
    os.system('cls')

def kembali ():
    inputan_kembali = input("Tekan Enter untuk kembali ke menu utama...")
    if inputan_kembali == "":
        clear_terminal()