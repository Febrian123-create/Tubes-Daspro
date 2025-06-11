import csv
import os,time # import os buat clear log, time supaya nambahin delay
from logo import logo

print(logo)
time.sleep(2.5)

def lihatMember():
    os.system("cls")
    print("\n====== Daftar Member ======\n")
    if jumlahMember == 0:
        print("Belum ada member yang terdaftar.")
    else:
        for i in range(jumlahMember):
            print(f"{i+1}. Nama: {members[i][1]}, No. Telp: {members[i][0]}")
    input("\nTekan Enter untuk kembali ke menu admin: ")
    menuAdmin()

def bacacsv(name,ukuran):
    matriks=[None]*100
    for i in range(0,100,1):
        matriks[i]=[None]*ukuran
    with open(name, mode="r") as file:
        reader = csv.reader(file)
        skip=True
        i=0
        for row in reader:
            if (skip==True):
                skip=False
            else:
                for j in range(0,ukuran,1):
                    matriks[i][j]=row[j]
                i+=1
    return matriks
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
    global num
    os.system("cls")
    print("\n====== Menu Admin ======\n")
    print("1. Lihat Transaksi")
    print("2. Lihat Pendapatan Hari Ini")
    print("3. Cari Transaksi Berdasarkan Menu")
    print("4. Lihat Daftar Member")
    print("5. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        lihatTransaksi()
    elif pilihan == "2":
        tampilPendapatan()
    elif pilihan == "3":
        menu = tampilanMenu()
        carimenu = int(input("Menu yang dicari : "))
        if (0 < carimenu <= len(menu)):
            SearchMenu(carimenu, menu)
        else:
            print("Menu tidak ditemukan")
            time.sleep(2)
        time.sleep(5)
        menuAdmin()
    elif pilihan == "4":
        lihatMember()
    elif pilihan =="5":
        main()
    else:
        print("Pilihan tidak valid.")
        time.sleep(1.5)
        menuAdmin()

def SearchMenu(carimenu, layanan):
    file = "Tubes-Daspro/transaksi.csv"
    data = bacacsv(file, 4)
    tampilanMenu()
    found = False
    print("\n====== Hasil Pencarian ======\n")
    i = 0
    while (data[i][0] != None):
        if (transaksi[i][1] == carimenu):
            if (layanan == 1):
                print(f"{i+1}. Takewaya, Menu {transaksi[i][1]}, Jumlah {transaksi[i][2]}, Total Rp {transaksi[i][3]}")
            elif (layanan == 2):    
                print(f"{i+1}. Meja: {transaksi[i][0]}, Menu {transaksi[i][1]}, Jumlah {transaksi[i][2]}, Total Rp {transaksi[i][3]}")
            found = True
        i += 1
    if (found == False):
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
def signup():
    username = str(input("Buat Username anda: "))
    password = str(input("Buat Password anda: "))
    file_path = "Tubes-Daspro/account.csv"
    data=[username,password]
    with open(file_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Akun berhasil dibuat!")
    print("Kembali")
    login()

def login(): # menu login admin/user
    os.system("cls")
    nama='Tubes-Daspro/account.csv'
    maccount=bacacsv(nama,2)
    print("\n====== ADMIN ======\n")
    print("1.Sign Up Account")
    print("2.Log in")
    print("3.Keluar")
    plh=int(input("Pilih: "))
    if(plh==1):
        print("\n====== SignUp Account ======\n")
        signup()
    elif(plh==2):
        print("\n====== Login Admin ======\n")
        username = input("Username: ")
        password = input("Password: ")
        index=0
        status=True
        while(maccount[index][0]!=None):
            for j in range(0,3,1):
                if (maccount[index][0]==username)and(maccount[index][1]==password):
                    print(f"Login berhasil! Selamat datang {maccount[index][0]} !")
                    time.sleep(3)
                    menuAdmin()
                    status=False
            index+=1
            if(status==False):
                print("Login gagal, Username atau Password salah.")
                time.sleep(2)
                ask = str(input("\nApakah mau lanjut login (y/n)")).upper()
                if ask == "N":
                    main()
                else:
                    login()

def kelolaMenu():
    os.system("cls")
    print("\n====== Kelola Menu ======\n")
    print("1.Tambah Menu")
    print("2.Hapus Menu")
    print("3.Edit Menu")
    print("4.Kembali")
    plh=int(input("Pilih Menu: "))
    if (plh == 1):
        tambahMenu()
    elif (plh == 2):
        hapusMenu()
    elif (plh == 3):
        editMenu()
    elif (plh == 4):
        time.sleep(1.5)
        menuAdmin()
    else:
        print("Pilihan tidak valid.")
        time.sleep(1.5)
        kelolaMenu

def tampilanMenu():
    global num
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,2)

    print("\n====== Menu ======\n")
    num = 1
    i = 0 
    while (menu[i][0] != None):
        print(f"{num}. {menu[i][0]} - Rp {menu[i][1]}")
        num += 1
        i +=1
    return menu

def tambahMenu():
    file = "Tubes-Daspro/menu.csv"
    print("\n====== Tambah Menu ======\n")
    tampilanMenu()
    nama = str(input("Masukkan menu baru: "))
    harga = int(input("Harga menu: "))
    with open(file, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nama, harga])
    print("Menu berhasil ditambahkan")
    time.sleep(2)
    kelolaMenu()

def editMenu():
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,2)
    print("\n====== Edit Menu ======\n")
    tampilanMenu()
    baris = int(input("Pilih nomor menu yang ingin diedit: ")) - 1
    if (baris < 0 or menu[baris][0] == None):
        print("Nomor menu tidak ada")
        time.sleep(2)
        kelolaMenu()
        return
    
    edit_nama = input("Edit nama (kosongkan jika tidak ingin diubah): ")
    edit_harga = input("Edit harga (kosongkan jika tidak ingin diubah): ")
    if edit_nama != "":
        menu[baris][0] = edit_nama
    elif edit_harga != "":
        menu[baris][1] = edit_harga

    with open(file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga"])
        i = 0
        while (menu[i][0] != None):
            writer.writerow(menu[i])
            i += 1
    if (edit_nama == "" and edit_harga == ""):
        print("Tidak ada menu yang diubah")
    else:
        print("Menu berhasil diubah.")
    time.sleep(2)
    kelolaMenu()

def hapusMenu():
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,2)
    tampilanMenu()
    hapus = int(input("Masukkan nomor menu yang ingin dihapus: ")) -1
    if (hapus < 0 or menu[hapus][0] == None):
        print("Nomor menu tidak ada")
        time.sleep(2)
        kelolaMenu()

    #hapus data dari csv
    del menu[hapus]

    with open(file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga"])
        for row in menu:
            if (row[0] != None):
                writer.writerow(row)
       
    print("Menu berhasil dihapus.")
    time.sleep(2)
    kelolaMenu()

def prosesUser():
    global jumlahTransaksi, jumlahMember
    discount = 0
    loginStatus = False
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
                harga = int(menu[index][1])
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

    while loginStatus == False:
        member = str(input("Apakah anda sudah mempunyai member (y/n): ")).upper()
        if member == "Y":
            telp = input("Masukkan nomor telepon member: ")
            pw = input("Masukkan password member: ")
            for i in range(jumlahMember):
                if members[i][0] == telp and members[i][2] == pw:
                    print(f"Selamat datang kembali, {members[i][1]} (Member)!")
                    loginStatus = True
                    discount = 90/100
            if loginStatus == False:
                print("Data member tidak ditemukan atau salah.")
                time.sleep(2)
        elif member == "N":
            askMember = str(input("Apakah anda mau membuat member (y/n): ")).upper()
            if askMember == "Y":
                telp = input("Masukkan nomor telepon: ")
                nama = input("Masukkan nama: ")
                pw = input("Buat password: ")
                members[jumlahMember][0] = telp
                members[jumlahMember][1] = nama
                members[jumlahMember][2] = pw
                jumlahMember += 1
                print(f"Member berhasil dibuat. Selamat datang {nama}!")
                loginStatus = True  # Member baru langsung login bos
                time.sleep(2)
            else:
                loginStatus = True
    
    if discount != 0: # proses bayar
        print(f"\nTotal Bayar setelah discount: Rp. {total*discount}")
    else:
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
    simpan_transaksi_csv()
    main()

def simpan_transaksi_csv():
    path="Tubes-Daspro/transaksi.csv"
    with open(path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        for i in range(jumlahTransaksi):
            writer.writerow(transaksi[i])
    print("Data transaksi telah disimpan ke transaksi.csv")

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
    members = [None]*100  # format: [no_telp, nama, password]
    for i in range (0,100):
        members[i]=[None]*3
    jumlahMember = 0

    transaksi = [None]*100 # var global kita
    for i in range (0,100):
        transaksi[i]=[None]*4
    jumlahTransaksi = 0  
    main()   