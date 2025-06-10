import os, time
from logo import logo

print(logo)
time.sleep(2.5)

def lihatTransaksi():
    print("\n====== Semua Transaksi ======") 
    if jumlahTransaksi == 0:
        print("Belum ada transaksi.")
        time.sleep(2)
        menuAdmin()
    else:
        for i in range(jumlahTransaksi):
            print(f"{i+1}. Meja: {transaksi[i][0]} | Menu: {transaksi[i][1]} x{transaksi[i][2]} | Total: Rp {transaksi[i][3]}")
        input("Tekan Enter untuk keluar: ")
    menuAdmin()

def tampilpenjualan():
    os.system("cls")
    print('='*50)
    print("Penjualan Hari Ini")

    if jumlahTransaksi == 0 or jumlahPelanggan == 0:
        print("Belum ada transaksi hari ini.")
        input("\nTekan Enter untuk kembali...")
        menuAdmin()
    else:
        menu = tampilanMenu()
        printmenu(menu)
        jmenu = JumlahPesananPerMenu()
        jumlah = 0
        print('='*50)
        print("Jumlah Pelanggan:", jumlahPelanggan)
        i = 0
        n = 0
        while menu[i][0] != None:
            n += 1
            i += 1
        print('-'*30)
        print("Menu Terjual:")
        for i in range(n):
            if menu[i][0] != None and jmenu[i] > 0:
                print(f"{menu[i][0]} : {jmenu[i]} Order")
        print('-'*30)
        print("Total Penjualan per Produk:")
        for i in range(n):
            if menu[i][0] != None and jmenu[i] > 0:
                total = jmenu[i] * menu[i][1]
                jumlah += total
                print(f"{menu[i][0]} : Rp {total}")
        print('-'*30)
        print("Total pendapatan Hari ini:", jumlah)
        print()
        input("\nTekan Enter untuk kembali...")
        menuAdmin()

def menuAdmin():
    os.system("cls")
    print("\n====== Menu Admin ======\n")
    print("1. Lihat Transaksi")
    print("2. Lihat Penjualan Hari Ini")
    print("3. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        lihatTransaksi()
    elif pilihan == "2":
        tampilpenjualan()
    elif pilihan == "3":
        main()
    else:
        print("Pilihan tidak valid.")
        time.sleep(1.5)
        menuAdmin()

def login():
    os.system("cls")
    users = [["admin1", "admin123", "admin"]]

    print("\n====== Login Admin ======\n")
    username = input("Username: ")
    password = input("Password: ")
    for i in users:
        if i[0] == username and i[1] == password:
            print(f"Login berhasil! Selamat datang {i[0]} !")
            time.sleep(3)
            menuAdmin()
    print("Login gagal, Username atau Password salah.")
    time.sleep(2)
    ask = str(input("\nApakah mau lanjut login (y/n)")).upper()
    if ask == "N":
        main()
    else:
        login()

def tampilanMenu():
    return [
        ["Ayam Geprek", 15000],
        ["Nasi Goreng", 20000],
        ["Indomie Telor", 10000],
        ["Es Teh", 5000],
        ["Kopi Susu", 8000],
        ["Susu Murni", 8000],
        [None, None],
    ]

def printmenu(menu):
    print("\n====== Menu ======\n")
    num = 1
    i = 0
    n = 0
    while menu[i][0] != None:
        n += 1
        i += 1
    for i in range(n):
        if menu[i][0] != None:
            print(f"{num}.{menu[i][0]} - Rp {menu[i][1]}")
        num += 1
    return menu

def JumlahPesananPerMenu():
    menu = tampilanMenu()
    n = 0
    while menu[n][0] != None:
        n += 1
    jmenu = [0] * n
    for item in semuaPesanan:
        if item[0] is not None:
            nama = item[0]
            jumlah = item[1]
            for j in range(n):
                if nama == menu[j][0]:
                    jmenu[j] += jumlah
    return jmenu

def prosesUser():
    global jumlahTransaksi, jumlahPelanggan
    os.system("cls")
    meja = 0
    print("\n====== Layanan Cafe ======\n")
    layanan = int(input("Pilih layanan (1. Takeaway | 2. Dine In): "))
    if layanan == 2:
        meja = input("Masukkan nomor meja: ")
    elif layanan == 1:
        meja = "Takeaway"
    else:
        print("Masukkan 1 atau 2.")
        time.sleep(2.5)
        prosesUser()

    menu = tampilanMenu()
    printmenu(menu)

    pesanan = [[None, 0, 0] for _ in range(100)]
    jumlahPesanan = 0
    n = 0
    while menu[n][0] is not None:
        n += 1

    while True:
        pilihMakanan = int(input("\nPilih nomor menu (0 jika selesai): "))
        if pilihMakanan == 0:
            break
        elif pilihMakanan > n or pilihMakanan < 0:
            print(f"Maaf makanan nomor {pilihMakanan} tidak ada, silakan pilih makanan lain")
        else:
            jumlah = int(input("Masukkan Jumlah: "))
            if jumlah <= 30:
                index = pilihMakanan - 1
                nama = menu[index][0]
                harga = menu[index][1]
                status = False
                for i in range(jumlahPesanan):
                    if pesanan[i][0] == nama:
                        pesanan[i][1] += jumlah
                        status = True
                if status==False:
                    pesanan[jumlahPesanan][0] = nama
                    pesanan[jumlahPesanan][1] = jumlah
                    pesanan[jumlahPesanan][2] = harga
                    jumlahPesanan += 1
            else:
                print("Maaf pesanan tidak bisa melebihi 30 item")

    print("\n====== Struk Pembayaran ======\n")
    total = 0
    for i in range(jumlahPesanan):
        nama, jumlah, harga = pesanan[i]
        subtotal = jumlah * harga
        print(f"{nama} x{jumlah} = Rp {subtotal}")
        total += subtotal
        transaksi[jumlahTransaksi] = [meja, nama, jumlah, subtotal]
        jumlahTransaksi += 1

    print(f"\nTotal Bayar: Rp. {total}")
    bayar = int(input("Masukkan jumlah uang: "))
    while bayar < total:
        print("Uang tidak cukup.")
        bayar = int(input("Masukkan ulang uang: "))
    kembalian = bayar - total
    print(f"Kembalian: Rp {kembalian}")
    time.sleep(3)
    os.system("cls")
    print("Terima kasih! Pesanan Anda sedang diproses.")
    time.sleep(1.5)

    # Simpan semua pesanan ke semuaPesanan
    semuaPesanan.extend(pesanan[:jumlahPesanan])

    jumlahPelanggan += 1
    main()

def main():
    os.system("cls")
    print("="*50)
    print(" Selamat Datang di Program Manajemen Cafe MyCafe!")
    print("="*50)
    print("\n1. Admin\n2. User\n")
    role = int(input("Pilih Jenis Login: "))
    if role == 1:
        login()
    elif role == 2:
        prosesUser()
    else:
        print("Input Tidak Valid. Pilih 1 atau 2")
        time.sleep(2)
        main()

if __name__ == '__main__':
    semuaPesanan = []
    jumlahPelanggan = 0
    transaksi = [None]*100 
    for i in range(0,100,1):
        transaksi[i]=[None]*4
    jumlahTransaksi = 0
    main()