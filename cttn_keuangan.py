import json
import os

#Fungsi untuk memuat data
def load_data():
    if os.path.exists("data.json"):
        with open("data.json", "r") as file:
            return json.load(file)
    return []

#Fungsi untuk menyimpan data
def save_data(transaksi):
    with open("data.json", "w") as file:
        json.dump(transaksi, file, indent=4)

#Fungsi tambah pemasukan
def tambah_pemasukan(transaksi):
    jumlah = float(input("Masukkan jumlah pemasukan: "))
    keterangan = input("Keterangan: ")
    transaksi.append({"tipe": "pemasukan", "jumlah": jumlah, "keterangan": keterangan})
    save_data(transaksi)
    print("Pemasukan berhasil ditambahkan.\n")

#Fungsi tambah pengeluaran
def tambah_pengeluaran(transaksi):
    jumlah = float(input("Masukkan jumlah pengeluaran: "))
    keterangan = input("Keterangan: ")
    transaksi.append({"tipe": "pengeluaran", "jumlah": jumlah, "keterangan": keterangan})
    save_data(transaksi)
    print("Pengeluaran berhasil ditambahkan.\n")

#Fungsi menampilkan transaksi
def tampilkan_transaksi(transaksi):
    if not transaksi:
        print("Belum ada catatan transaksi.\n")
        return
    
    print("\n=== DAFTAR TRANSAKSI ===")
    for i, t in enumerate(transaksi, start=1):
        print(f"{i}. {t['tipe'].upper()} - Rp{t['jumlah']} ({t['keterangan']})")
    print()

#Fungsi hitung saldo
def hitung_saldo(transaksi):
    saldo = 0
    for t in transaksi:
        if t["tipe"] == "pemasukan":
            saldo += t["jumlah"]
        else:
            saldo -= t["jumlah"]
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
