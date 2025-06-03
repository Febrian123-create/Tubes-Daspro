import os,time


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

def menuAdmin():
    os.system("cls")
    print("\n====== Menu Admin ======\n")
    print("1. Lihat Transaksi")
    print("2. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        lihatTransaksi()
    elif pilihan == "2":
        main()
    else:
        print("Pilihan tidak valid.")

def login():
    users = [["admin1","admin123","admin"],["user1","user123","user"]]
    print("\n====== Login ======\n")
    username = input("Username: ")
    password = input("Password: ")
    for i in users:
        if (i[0]==username)and(i[1]==password):
            print(f"Login berhasil! Selamat datang {i[0]} !")
            print(f"Selamat datang di program {i[2]}")
            return i[2]
    print("Login gagal, Username atau Password salah.")
    return None
def tampilanMenu():
    menu = [["Ayam Geprek", 15000],
            ["Nasi Goreng",20000],
            ["Indomie Telor",10000],
            ["Es Teh", 5000],
            ["Kopi Susu", 8000],
            ["Susu Murni", 8000]]
    print("\n====== Menu ======\n")
    num = 1
    for i in menu:
        print(f"{num}. {i[0]} - Rp {i[1]}")
        num+=1
    return menu

def prosesUser():
    global jumlahTransaksi
    os.system("cls")
    meja = 0
    print("\n====== Layanan Cafe ======\n")
    layanan = int(input("Pilih layanan (1. Takeaway | 2. Dine In): "))
    if (layanan == 1) or (layanan==2):
        if layanan == 2:
            meja = input("Masukkan nomor meja (1-10): ")
    else:
        print("Masukkan 1 atau 2.")
        time.sleep(2.5)
        prosesUser()
    
    menu = tampilanMenu()
    
    pesanan = [None]*100 # proses memesan makanan
    jumlahPesanan = 0
    for i in range(0,100,1):
        pesanan[i] = [None]*3
    check = True
    while check == True:
        pilihMakanan = int(input("\nPilih nomor menu (0 jika selesai): "))
        if pilihMakanan == 0:
            check = False
        else:
            jumlah = int(input("Masukkan Jumlah: "))
            if jumlah<=30:
                index = pilihMakanan-1
                nama = menu[index][0]
                harga = menu[index][1]
                pesanan[jumlahPesanan][0] = nama
                pesanan[jumlahPesanan][1] = jumlah
                pesanan[jumlahPesanan][2] = harga

                totalItem = harga * jumlah
                transaksi[jumlahTransaksi][0] = meja
                transaksi[jumlahTransaksi][1] = nama
                transaksi[jumlahTransaksi][2] = jumlah
                transaksi[jumlahTransaksi][3] = totalItem
                
                jumlahTransaksi += 1
                jumlahPesanan += 1
            else:
                print("Maaf pesanan tidak bisa melebihi 30 item")
    
    print("\n====== Struk Pembayaran ======\n")
    total = 0
    for i in range (jumlahPesanan):
        nama = pesanan[i][0]
        jumlah = pesanan[i][1]
        harga = pesanan[i][2]
        subtotal = jumlah * harga
        print(f"{nama} x{jumlah} = Rp {subtotal}")
        total += subtotal

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
    main()

def main():
    os.system("cls")
    print("="*50)
    print(" Selamat Datang di Program Manajemen Cafe MyCafe!")
    print("="*50)
    role = login() 
    if role == "admin":
        time.sleep(3)
        os.system("cls")
        menuAdmin()
    elif role == "user":
        prosesUser()
    elif role == None:
        time.sleep(2)
        main()
if __name__ == '__main__':  
    transaksi = [None]*100
    for i in range (0,100):
        transaksi[i]=[None]*4
    jumlahTransaksi = 0  
    main()   