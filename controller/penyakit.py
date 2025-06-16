from model.penyakit import mpenyakit_cek, mgejala, mgejala_semua
from controller.terminal import clear_terminal, kembali
import tabulate

def deteksi_penyakit():
    clear_terminal()

    # Ambil semua data penyakit dan gejala
    semua_penyakit = mpenyakit_cek()
    semua_gejala = mgejala_semua()

    if not semua_gejala:
        print("Data gejala tidak tersedia.")
        kembali()
        return

    # Tampilkan semua gejala
    print("=== Daftar Gejala ===")
    print(tabulate.tabulate(
        [[idx, g[0], g[1]] for idx, g in enumerate(semua_gejala, 1)],
        headers=["No", "ID Gejala", "Nama Gejala"],
        tablefmt="fancy_grid"
    ))

    # Input satu ID gejala dari user
    input_user = input("\nMasukkan ID gejala yang Anda alami: ").strip()
    if not input_user.isdigit():
        print("Input harus berupa angka ID gejala!")
        kembali()
        return

    id_gejala_user = int(input_user)

    # Pastikan gejala tersebut valid
    id_gejala_valid = [g[0] for g in semua_gejala]
    if id_gejala_user not in id_gejala_valid:
        print("ID gejala tidak ditemukan!")
        kembali()
        return

    # Cari penyakit yang memiliki gejala tersebut
    hasil = []
    for penyakit in semua_penyakit:
        id_penyakit = penyakit[0]
        gejala_penyakit = [g[0] for g in mgejala(id_penyakit)]
        if id_gejala_user in gejala_penyakit:
            total = len(gejala_penyakit)
            cocok = 1
            persentase = cocok / total if total > 0 else 0
            hasil.append((id_penyakit, cocok, total, persentase))

    # Tampilkan hasil
    clear_terminal()
    print("=== HASIL DIAGNOSA ===")
    if hasil:
        hasil.sort(key=lambda x: x[3], reverse=True)
        for h in hasil:
            penyakit = next(p for p in semua_penyakit if p[0] == h[0])
            print(f"\nPenyakit: {penyakit[1]}")
            print(f"Kecocokan gejala: {h[1]}/{h[2]} ({round(h[3]*100)}%)")
            if h[3] >= 0.5:
                print(f"Penanganan: {penyakit[2]}")
            else:
                print("Gejala tidak cukup spesifik untuk diagnosis yang akurat.")
    else:
        print("Tidak ditemukan penyakit yang memiliki gejala tersebut.")

    input("\nTekan Enter untuk kembali...")
