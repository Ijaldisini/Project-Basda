from model.jadwalvit import jadwal, tambah_jadwal, nutrisi, bibit
from controller.terminal import clear_terminal
import tabulate

def jadwal_vitamin():
    while True:
        clear_terminal()
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	    MENU JADWAL              ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Lihat jadwal                ||')
        print('||                2. Tambah jadwal               ||')
        print('||                3. Kembali                     ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()

        if pilihan == "1":
            data = jadwal()
            clear_terminal()
            print("=== DAFTAR JADWAL NUTRISI ===")
            if data:
                print(tabulate.tabulate(
                    [[d[0], d[1], d[2], d[3]] for d in data],
                    headers=["ID", "Nutrisi", "Dosis perMinggu", "Bibit"],
                    tablefmt="fancy_grid"
                ))
            else:
                print("Belum ada data jadwal nutrisi.")
            input("\nTekan Enter untuk kembali...")

        elif pilihan == "2":
            clear_terminal()
            nutrisi_list = nutrisi()
            bibit_list = bibit()

            print("\n=== Daftar Nutrisi ===")
            if nutrisi_list:
                print(tabulate.tabulate(
                    [[n[0], n[1]] for n in nutrisi_list],
                    headers=["ID Nutrisi", "Nama Nutrisi"],
                    tablefmt="fancy_grid"
                ))
            else:
                print("Tidak ada data nutrisi.")

            print("\n=== Daftar Bibit ===")
            if bibit_list:
                print(tabulate.tabulate(
                    [[b[0], b[1]] for b in bibit_list],
                    headers=["ID Bibit", "Nama Bibit"],
                    tablefmt="fancy_grid"
                ))
            else:
                print("Tidak ada data bibit.")

            try:
                id_nutrisi = int(input("\nPilih ID Nutrisi: ").strip())
                id_bibit = int(input("Pilih ID Bibit: ").strip())
                dosis = int(input("Masukkan dosis: ").strip())
                tambah_jadwal(id_nutrisi, id_bibit, dosis)
                print("\nJadwal vitamin berhasil ditambahkan.")
                
            except Exception as e:
                print(f"\nTerjadi kesalahan: {e}")

            input("\nTekan Enter untuk kembali...")


        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")
