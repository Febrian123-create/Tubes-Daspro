import os,time # import os buat clear log, time supaya nambahin delay
from logo import logo

print(logo)
time.sleep(2.5)
def lihatTransaksi(): # fungsi liat daftar transaksi
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

def menuAdmin(): # menu admin kalo udah berhasil masukin username sama pass
    os.system("cls")
    print("\n====== Menu Admin ======\n")
    print("1. Lihat Transaksi")
    print("2. Lihat Pendapatan Hari Ini")
    print("3. Cari Transaksi Berdasarkan Menu")
    print("4. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        lihatTransaksi()
    elif pilihan == "2":
        tampilPendapatan()
    elif pilihan == "3":
        tampilanMenu()
        carimenu = str(input("Menu yang dicari : "))
        SearchMenu(carimenu)
        time.sleep(5)
        menuAdmin()
    elif pilihan =="4":
        main()
    else:
        print("Pilihan tidak valid.")
        time.sleep(1.5)
        menuAdmin()

def SearchMenu(carimenu):
    global jumlahTransaksi, transaksi
    transaksi[jumlahTransaksi] = carimenu
    i = 0
    while (transaksi[i][1] != carimenu):
        i += 1
    for j in range(0,100,1):
        if (i < jumlahTransaksi):
            print(f"Transaksi ditemukan: Meja {transaksi[i][0]}, Menu {transaksi[i][1]}, Jumlah {transaksi[i][2]}, Total Rp {transaksi[i][3]}")
        else:
            print("Transaksi tidak ditemukan")


def campur(s_array,j_array,n,x,z):
    y = 0
    for i in range(n):
        status = False
        for j in range(y):
            if transaksi[i][x] == s_array[j]:
                j_array[j] += transaksi[i][z]
                status = True
        if status==False:
            s_array[y] = transaksi[i][x]
            j_array[y] = transaksi[i][z]
            y += 1
            
def tampilPendapatan():
    i = 0
    n = 0
    jumlah = 0
    while transaksi[i][0] != None:
        jumlah += transaksi[i][3]
        n += 1
        i += 1
    print("Total pendapatan hari ini: Rp.",jumlah)
    print("Total Pendapatan dari meja:")
    s_array=[None]*100
    j_array=[0]*100
    print('='*30)
    campur(s_array,j_array,n,0,3)
    for i in range(0,n,1):
        if(s_array[i]!=None):
            print(f"Meja {s_array[i]} : Rp.{j_array[i]}")
    print("Total pendapatan/menu:")
    s_array=[None]*100
    j_array=[0]*100
    print('='*30)
    campur(s_array,j_array,n,1,3)
    for i in range(0,n,1):
        if(s_array[i]!=None):
            print(f"Menu {s_array[i]} : Rp.{j_array[i]}")
    print("Jumlah Menu yang laku:")
    s_array=[None]*100
    j_array=[0]*100
    print('='*30)
    campur(s_array,j_array,n,1,2)
    for i in range(0,n,1):
        if(s_array[i]!=None):
            print(f"Menu {s_array[i]} : {j_array[i]}")


def login(): # menu login admin/user
    os.system("cls")
    users = [["admin1","admin123","admin"]] # index 0 = username, index 1 = password

    print("\n====== Login Admin ======\n")
    username = input("Username: ")
    password = input("Password: ")
    for i in users:
        if (i[0]==username)and(i[1]==password):
            print(f"Login berhasil! Selamat datang {i[0]} !")
            time.sleep(3)
            menuAdmin()
        else:
            print("Login gagal, Username atau Password salah.")
            time.sleep(2)
            ask = str(input("\nApakah mau lanjut login (y/n)")).upper()
            if ask == "N":
                main()
            else:
                login()
  
def tampilanMenu():
    global num
    menu = [["Ayam Geprek", 15000], # list menu sementara
            ["Nasi Goreng",20000],
            ["Indomie Telor",10000],
            ["Es Teh", 5000],
            ["Kopi Susu", 8000],
            ["Susu Murni", 8000]]
    print("\n====== Menu ======\n")
    num = 1
    for i in menu: # print menu
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
            meja = input("Masukkan nomor meja: ")
        else:
            meja = "Takeaway"
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
        elif pilihMakanan >= num:
            print(f"Maaf makanan nomor {pilihMakanan} tidak ada, silahkan pilih makanan lain")
        else:
            jumlah = int(input("Masukkan Jumlah: "))
            if jumlah<=30: # proses masukin makanan ke pesanan sama daftar transaksi
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
    
    print("\n====== Struk Pembayaran ======\n") # cetak struk
    total = 0
    for i in range (jumlahPesanan):
        nama = pesanan[i][0]
        jumlah = pesanan[i][1]
        harga = pesanan[i][2]
        subtotal = jumlah * harga
        print(f"{nama} x{jumlah} = Rp {subtotal}")
        total += subtotal

    print(f"\nTotal Bayar: Rp. {total}") # proses bayar
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

def main(): # notes: os.system("cls") buat clear log, time.sleep(<detik>) buat kasih efek delay second
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
    transaksi = [None]*100 # var global kita
    for i in range (0,100):
        transaksi[i]=[None]*4
    jumlahTransaksi = 0  
    main()   