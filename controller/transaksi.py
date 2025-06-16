from model.transaksi import get_daftar_panen, insert_transaksi, insert_detail_transaksi, get_riwayat_transaksi
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

    daftar = get_daftar_panen()
    if not daftar:
        print("Belum ada panen yang tersedia untuk dijual.")
        kembali()
        return

    print(tabulate(
        [[i+1, d[0], d[1], d[2]] for i, d in enumerate(daftar)],
        headers=["No", "ID Panen", "Bibit", "Total Panen (gram), "],
        tablefmt="fancy_grid"
    ))

    try:
        pilihan = int(input("\nMasukkan ID Panen yang ingin dijual: "))
        panen_terpilih = next((d for d in daftar if d[0] == pilihan), None)

        if not panen_terpilih:
            print("ID panen tidak ditemukan.")
            kembali()
            return

        jumlah = int(input("Masukkan jumlah (kg) yang ingin dijual: "))
        if jumlah > panen_terpilih[2]:
            print("Jumlah melebihi total hasil panen!")
            kembali()
            return

        harga_perkg = 10000  # jika ingin dinamis, ambil dari bibit_tanaman
        nominal = jumlah * harga_perkg

        id_transaksi = insert_transaksi(id_akun)
        insert_detail_transaksi(jumlah, nominal, id_transaksi, panen_terpilih[0])

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
