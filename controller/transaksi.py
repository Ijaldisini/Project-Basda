from model.transaksi import insert_transaksi, insert_detail_transaksi, get_riwayat_transaksi, get_harga_perkg, update_hasil_panen, get_riwayat_transaksiowner
from model.stok import sayur_panen
from controller.terminal import clear_terminal, kembali
from tabulate import tabulate
from datetime import datetime

def transaksi_penjualan(id_akun):
    while True:
        clear_terminal()
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        print('|| ^^^ 	     	    MENU PENJUALAN           ^^^ ||')
        print('||---------    Silahkan pilih menu      ---------||')
        print('||                1. Tambah transaksi            ||')
        print('||                2. Riwayat                     ||')
        print('||                3. Kembali                     ||')
        print('+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+:+')
        pilihan = input('Silahkan pilih menu: ').strip()

        if pilihan == "1":
            tambah_transaksi(id_akun)
        elif pilihan == "2":
            lihat_riwayat(id_akun)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid.")
            input("Tekan Enter untuk kembali...")

def tambah_transaksi(id_akun):
    clear_terminal()
    print("=== TAMBAH TRANSAKSI PENJUALAN ===\n")

    daftar = sayur_panen()
    if not daftar:
        print("Belum ada panen yang tersedia untuk dijual.")
        kembali()
        return

    print(tabulate(
        [[i + 1, d[0], d[1], d[2], d[7]] for i, d in enumerate(daftar)],
        headers=["No", "ID Rak", "Bibit", "Bibit/Rak", "Total Hasil (gram)"],
        tablefmt="fancy_grid"
    ))

    try:
        pilihan = int(input("\nMasukkan ID Rak yang ingin dijual: "))
        rak_terpilih = next((d for d in daftar if d[0] == pilihan), None)

        if not rak_terpilih:
            print("ID rak tidak ditemukan.")
            kembali()
            return

        jumlah = int(input("Masukkan jumlah (kg) yang ingin dijual: "))
        if jumlah * 1000 > rak_terpilih[7]:
            print("Jumlah melebihi total hasil panen!")
            kembali()
            return

        id_bibit = rak_terpilih[8]
        harga_perkg = get_harga_perkg(id_bibit)
        nominal = jumlah * harga_perkg

        id_transaksi = insert_transaksi(id_akun)
        id_panen = rak_terpilih[3]
        insert_detail_transaksi(jumlah, nominal, id_transaksi, id_panen)
        update_hasil_panen(id_panen, jumlah * 1000)

        print(f"\n✅ Transaksi berhasil dicatat. Total: Rp{nominal:,}")
        
    except Exception as e:
        print(f"❌ Terjadi kesalahan: {e}")

    kembali()

def lihat_riwayat(id_akun):
    clear_terminal()
    print("=== RIWAYAT PENJUALAN ===\n")
    data = get_riwayat_transaksi(id_akun)
    if data:
        print(tabulate(
            [[d[0], d[1], d[2], d[3], d[4]] for d in data],
            headers=["ID Transaksi", "Tanggal", "Bibit", "Jumlah (kg)", "Total (Rp)"],
            tablefmt="fancy_grid"
        ))
    else:
        print("Belum ada transaksi.")
    kembali()
    
def lihat_riwayatowner():
    clear_terminal()
    print("=== RIWAYAT PENJUALAN ===\n")
    data = get_riwayat_transaksiowner()
    if data:
        print(tabulate(
            [[d[0], d[1], d[2], d[3], d[4]] for d in data],
            headers=["ID Transaksi", "Tanggal", "Bibit", "Jumlah (kg)", "Total (Rp)"],
            tablefmt="fancy_grid"
        ))
    else:
        print("Belum ada transaksi.")
    kembali()