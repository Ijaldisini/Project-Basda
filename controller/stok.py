from model import stok
from controller.terminal import clear_terminal, kembali
import tabulate
from datetime import date, timedelta


def tambah_stok():
    clear_terminal()
    print("=== TAMBAH BIBIT TANAMAN BARU ===\n")

    try:
        nama = input("Masukkan nama bibit: ").strip()
        stok_bibit = int(input("Masukkan jumlah stok bibit: "))
        usia_panen = int(input("Masukkan usia panen (dalam hari): "))
        hasil_perbibit = int(input("Masukkan hasil panen per bibit (gram): "))
        harga_perkg = int(input("Masukkan harga per kg (Rp): "))
        harga_bibit = int(input("Masukkan harga bibit (Rp): "))

        stok.insert_bibit(
            nama_bibit=nama,
            stok_bibit=stok_bibit,
            usia_panen=usia_panen,
            hasil_perbibit=hasil_perbibit,
            harga_perkg=harga_perkg,
            harga_bibit=harga_bibit
        )

        print(f"\n✅ Bibit '{nama}' berhasil ditambahkan ke stok.")
    except Exception as e:
        print(f"\n❌ Terjadi kesalahan saat menambah bibit: {e}")

    kembali()

def kelola_siklus_rak():
    clear_terminal()
    print("=== KELOLA SIKLUS RAK ===\n")

    daftar_rak = stok.datastoksayur_full()
    if not daftar_rak:
        print("Tidak ada data rak budidaya.")
        kembali()
        return

    print(tabulate.tabulate(
        [[i + 1, d[0], d[1], d[2], d[3], d[4], d[5], d[6]] for i, d in enumerate(daftar_rak)],
        headers=["No", "ID Rak", "Bibit", "Bibit/Rak", "Tgl Tanam", "Tgl Panen", "Batas Panen", "Total Hasil"],
        tablefmt="fancy_grid"
    ))

    try:
        rak_id = int(input("\nMasukkan ID Rak yang ingin diganti siklusnya: "))
        rak_ada = any(d[0] == rak_id for d in daftar_rak)
        if not rak_ada:
            print("❌ ID Rak tidak ditemukan.")
            kembali()
            return

        bibit_tersedia = stok.datastokbibit_full()
        if not bibit_tersedia:
            print("Belum ada bibit tersedia.")
            kembali()
            return

        print("\n=== PILIH BIBIT UNTUK RAK ===")
        print(tabulate.tabulate(
            [[i + 1, d[0], d[1], d[2], d[3], d[4], d[5], d[6]] for i, d in enumerate(bibit_tersedia)],
            headers=["No", "ID Bibit", "Nama", "Stok", "Usia Panen", "Hasil/Bibit", "Harga/kg", "Harga Bibit"],
            tablefmt="fancy_grid"
        ))

        id_bibit = int(input("Masukkan ID Bibit yang ingin ditanam di rak: "))
        bibit = next((b for b in bibit_tersedia if b[0] == id_bibit), None)
        if not bibit:
            print("❌ ID Bibit tidak valid.")
            kembali()
            return

        usia_panen = bibit[3]
        hasil_perbibit = bibit[4]

        tgl_tanam = date.today()
        tgl_panen = tgl_tanam + timedelta(days=usia_panen)
        batas_panen = tgl_panen + timedelta(days=3)

        total_hasil = hasil_perbibit * 1  # Asumsikan 1 bibit per rak, atau sesuaikan

        # Tambahkan panen baru
        id_panen_baru = stok.insert_panen(
            id_bibit=id_bibit,
            tgl_tanam=tgl_tanam,
            tgl_panen=tgl_panen,
            batas_panen=batas_panen,
            total_hasil=total_hasil
        )

        # Update rak agar pakai panen baru
        stok.update_rak_dengan_panen(rak_id, id_panen_baru)

        print(f"\n✅ Rak {rak_id} berhasil diperbarui dengan siklus panen baru.")

    except Exception as e:
        print(f"\n❌ Terjadi kesalahan: {e}")

    kembali()