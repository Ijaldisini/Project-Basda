from model.penyakit import mpenyakit_cek, mgejala, mgejala_semua
from controller.terminal import clear_terminal, kembali
import tabulate

def deteksi_penyakit():
    clear_terminal()

    semua_penyakit = mpenyakit_cek()
    semua_gejala = mgejala_semua()

    if not semua_gejala:
        print("Data gejala tidak tersedia.")
        kembali()
        return

    penyakit_map = {}
    for penyakit in semua_penyakit:
        id_penyakit = penyakit[0]
        gejala_list = mgejala(id_penyakit)
        penyakit_map[id_penyakit] = set(g[0] for g in gejala_list)

    print("=== Daftar Gejala ===")
    print(tabulate.tabulate(
        [[idx, g[0], g[1]] for idx, g in enumerate(semua_gejala, 1)],
        headers=["No", "ID Gejala", "Nama Gejala"],
        tablefmt="fancy_grid"
    ))

    input_user = input("\nMasukkan ID gejala yang Anda alami (pisahkan dengan koma, contoh: 1,3,5): ")
    try:
        id_gejala_user = set(int(i.strip()) for i in input_user.split(',') if i.strip().isdigit())
    except ValueError:
        print("Input tidak valid!")
        kembali()
        return

    if not id_gejala_user:
        print("Tidak ada gejala yang dimasukkan.")
        kembali()
        return

    hasil = []
    for id_penyakit, gejala_penyakit in penyakit_map.items():
        cocok = len(id_gejala_user & gejala_penyakit)
        total = len(gejala_penyakit)
        persentase = cocok / total if total > 0 else 0
        if cocok > 0:
            hasil.append((id_penyakit, cocok, total, persentase))

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
        print("Tidak ditemukan penyakit yang cocok dengan gejala yang Anda masukkan.")

    input("\nTekan Enter untuk kembali...")
