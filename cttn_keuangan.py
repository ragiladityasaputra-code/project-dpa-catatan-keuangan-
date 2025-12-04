#Fungsi untuk memuat data
def load_data():
    data = []
    try:
        with open("data.txt", "r") as file:
            for line in file:
                line = line.strip()
                if line:
                    parts = line.split("|")
                    if len(parts) == 3:
                        data.append({
                            "Tipe": parts[0],
                            "Jumlah": int(parts[1]),
                            "Keterangan": parts[2]
                        })
    except FileNotFoundError:
        print("File belum ada, data kosong. \n")
    return data

#Fungsi untuk menyimpan data
def save_data(transaksi):
    try:
        with open("data.txt", "w") as file:
            for t in transaksi:
                line = f"{t['Tipe']}|{t['Jumlah']}|{t['Keterangan']}\n"
                file.write(line)
    except KeyError:
        print(f"Error: Terjadi kesalahan transaksi.")

#Fungsi tambah pemasukan
def tambah_pemasukan(transaksi):
    try:
        jumlah = int(input("Masukkan jumlah pemasukan: "))
        keterangan = input("Keterangan: ")
        transaksi.append({"Tipe": "Pemasukan", "Jumlah": jumlah, "Keterangan": keterangan})
        save_data(transaksi)
        print("Pemasukan berhasil ditambahkan.\n")
    except ValueError:
        print("Error: Jumlah pemasukan harus berupa bilangan bulat.\n")

#Fungsi tambah pengeluaran
def tambah_pengeluaran(transaksi):
    try:
        jumlah = int(input("Masukkan jumlah pengeluaran: "))
        keterangan = input("Keterangan: ")
        transaksi.append({"Tipe": "Pengeluaran", "Jumlah": jumlah, "Keterangan": keterangan})
        save_data(transaksi)
        print("Pengeluaran berhasil ditambahkan.\n")
    except ValueError:
        print("Error: Jumlah pengeluaran harus bilangan bulat.\n")

#Fungsi menampilkan transaksi
def tampilkan_transaksi(transaksi):
    if not transaksi:
        print("Belum ada catatan transaksi.\n")
        return
    
    print("\n=== DAFTAR TRANSAKSI ===")
    nomor_urut = 1
    for t in transaksi:
        print(f"{nomor_urut}. {t['Tipe'].upper()} - Rp{t['Jumlah']} ({t['Keterangan']})")
        nomor_urut += 1
    print()

#Fungsi hitung saldo
def hitung_saldo(transaksi):
    saldo = 0
    for t in transaksi:
        if t["Tipe"] == "Pemasukan":
            saldo += t["Jumlah"]
        else:
            saldo -= t["Jumlah"]
    print(f"\nSaldo saat ini: Rp{saldo}\n")

#Menu utama
def menu():
    transaksi = load_data()

    while True:
        print("=== CATATAN KEUANGAN HARIAN ===")
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Tampilkan Semua Transaksi")
        print("4. Hitung Saldo")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tambah_pemasukan(transaksi)
        elif pilihan == "2":
            tambah_pengeluaran(transaksi)
        elif pilihan == "3":
            tampilkan_transaksi(transaksi)
        elif pilihan == "4":
            hitung_saldo(transaksi)
        elif pilihan == "5":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.\n")


menu()  
