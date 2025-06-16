from model.transaksi import get_daftar_panen, insert_transaksi, insert_detail_transaksi
from controller.terminal import clear_terminal, kembali
from tabulate import tabulate

def transaksi_penjualan(id_akun):
    clear_terminal()
    print("=== MENU TRANSAKSI PENJUALAN ===\n")

    daftar = get_daftar_panen()
    if not daftar:
        print("Belum ada panen yang tersedia untuk dijual.")
        kembali()
        return

    print(tabulate(
        [[i+1, d[0], d[1], d[2]] for i, d in enumerate(daftar)],
        headers=["No", "ID Panen", "Bibit", "Total Panen (kg)"],
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

        harga_perkg = 10000  # bisa juga ambil dari bibit_tanaman jika perlu
        nominal = jumlah * harga_perkg

        id_transaksi = insert_transaksi(id_akun)
        insert_detail_transaksi(jumlah, nominal, id_transaksi, panen_terpilih[0])

        print(f"\nTransaksi berhasil dicatat. Total: Rp{nominal:,}")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

    kembali()
