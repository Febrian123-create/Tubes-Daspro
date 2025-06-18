import csv
import os, time  # import os buat clear log, time supaya nambahin delay
from logo import logo

print(logo)
time.sleep(2.5)

def bacacsv(name, ukuran):
    matriks = [None] * 100
    for i in range(0, 100, 1):
        matriks[i] = [None] * ukuran
    with open(name, mode="r") as file:
        reader = csv.reader(file)
        skip = True
        i = 0
        for row in reader:
            if skip:
                skip = False
            else:
                for j in range(0, ukuran, 1):
                    matriks[i][j] = row[j]
                i += 1
    return matriks

def cekcsv(file_path):
    with open(file_path, 'r') as file:
        line_count = 0
        inside_line = False
        stop = False
        while not stop:
            char = file.read(1)
            if char == "":
                stop = True
            else:
                if char != '\n' and not inside_line:
                    inside_line = True
                    line_count += 1
                elif char == '\n':
                    inside_line = False
                if line_count >= 2:
                    stop = True
        if line_count < 2:
            return True
        else:
            return False

def lihatMember():
    os.system("cls")
    nama = 'Tubes-Daspro/member.csv'
    mmember = bacacsv(nama,3)
    print("\n====== Semua Member ======")
    num = 1
    i=0
    while(mmember[i][0] != None):
        print(f"{num}. Nama: {mmember[i][1]} ")
        print(f"Telepon: {mmember[i][0]} ")
        num += 1
        i +=1
    input("Tekan Enter untuk kembali ke menu admin: ")
    menuAdmin()

def lihatTransaksi():
    os.system("cls")
    print("\n====== Tampil Transaksi ======\n")
    print("1.Transaksi Hari Ini")
    print("2.Kembali")
    plh=int(input("Masukkan pilihan: "))
    if plh ==1:
        TransaksiHariIni()
    elif plh ==2:
        menuAdmin()
    else:
        print("Pilihan tidak valid")
        lihatTransaksi()

def TransaksiHariIni():
    os.system("cls")
    nama = 'Tubes-Daspro/transaksi.csv'
    cek=cekcsv(nama)
    if cek == False:
        mtransaksi = bacacsv(nama, 4)
        print("\n====== Semua Transaksi ======")
        num = 1
        i=0
        while(mtransaksi[i][0] != None):
            print(f"{num}. Meja: {mtransaksi[i][0]} | Menu: {mtransaksi[i][1]} x{mtransaksi[i][2]} | Total: Rp {mtransaksi[i][3]}")
            num += 1
            i +=1
        input("Tekan Enter untuk kembali ke menu admin: ")
        lihatTransaksi()
    else:
        print("Belum ada transaksi hari ini")
        input("Tekan Enter untuk kembali ke menu admin: ")
        menuAdmin()


def lihatTransaksiHari():
    os.system("cls")
    tanggal=input("Masukkan tanggal (DDMMYYYY): ")
    nama = f"Tubes-Daspro/transaksi_{tanggal}.csv"
    mtransaksi = bacacsv(nama, 4)
    print(f"\n====== Transaksi Hari {tanggal} ======")
    num = 1
    i=0
    while(mtransaksi[i][0] != None):
        print(f"{num}. Meja: {mtransaksi[i][0]} | Menu: {mtransaksi[i][1]} x{mtransaksi[i][2]} | Total: Rp {mtransaksi[i][3]}")
        num += 1
        i +=1
    input("Tekan Enter untuk kembali ke menu Lihat Transaksi: ")
    lihatTransaksi()

def akhirihari():
    os.system("cls")
    nama = 'Tubes-Daspro/transaksi.csv'
    mtransaksi = bacacsv(nama, 4)
    print("Hari ini Berakhir!! Sampai Jumpa!")
    count = 0
    while (mtransaksi[count][0]!=None):
        count += 1
    if count > 0:
        tanggal = input("Masukkan tanggal (DDMMYYYY): ")
        i = 0
        n = 0
        jumlah = 0
        while mtransaksi[i][0] != None:
            jumlah += int(mtransaksi[i][3])
            n += 1
            i += 1
        print("Total pendapatan hari ini: Rp.", jumlah)
        print('=' * 30)
        print("Total Pendapatan dari meja:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 0, 3)
        for i in range(n):
            if s_array[i] != None:
                print(f"Meja {s_array[i]} : Rp.{j_array[i]}")
        print('=' * 30)
        print("Total pendapatan/menu:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 1, 3)
        for i in range(n):
            if s_array[i] != None:
                print(f"Menu {s_array[i]} : Rp.{j_array[i]}")
        print('=' * 30)
        print("Jumlah Menu yang laku:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 1, 2)
        for i in range(n):
            if s_array[i] != None:
                print(f"Menu {s_array[i]} : {j_array[i]}")
        print('=' * 30)
        print("Belum ada transaksi")
        input("\nTekan Enter untuk kembali ke menu Admin: ")
        with open(f'Tubes-Daspro/transaksi_{tanggal}.csv', 'w',newline='') as backup:
            writer = csv.writer(backup)
            writer.writerow(["Meja","Menu","Jumlah","Total"])
            for i in range (0,count,1):
                writer.writerow([mtransaksi[i][0],mtransaksi[i][1],mtransaksi[i][2],mtransaksi[i][3]])
            backup.close()
            print(f"Backup dibuat untuk tanggal {tanggal}")
            with open(f'Tubes-Daspro/transaksi.csv', 'w',newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Meja","Menu","Jumlah","Total"])
    else:
        print("Tidak ada transaksi hari ini")
        input("\nTekan Enter untuk kembali ke menu admin: ")
    menuAdmin()

# fungsi menu pilih fitur  untuk admin
#  pilihan = var int input pilih menu

def menuAdmin():
    os.system("cls")
    print("\n====== MENU ADMIN ======")
    print("1. Lihat Transaksi")
    print("2. Lihat Pendapatan")
    print("3. Cari Transaksi Berdasarkan Menu")
    print("4. Lihat Daftar Member")
    print("5. Kelola Menu")
    print("6. Tambah Stok")
    print("7. Akhiri Hari")
    print("8. Keluar")
    pilihan = input("Pilih menu: ")
    if pilihan == "1":
        lihatTransaksi()
    elif pilihan == "2":
        tampilPendapatan()
    elif pilihan == "3":
        tampilanMenu()
        carimenu = int(input("Menu yang dicari : "))
        SearchMenu(carimenu, menu)
    elif pilihan =="4":
        lihatMember()
    elif pilihan == "5":
        kelolaMenu()
    elif pilihan == "6":
        tambahStok()
    elif pilihan =="7":
        akhirihari()
    elif pilihan =="8":
        main()
    else:
        print("Pilihan tidak valid.")
        time.sleep(1.5)
        menuAdmin()

# Fungsi untuk mencari transaksi berdasarkan menu
# found : untuk mengecek apakah menu ditemukan
# num : untuk menghitung jumlah transaksi yang ditemukan
# data : untuk menyimpan data dari file transaksi
# i : untuk indeks data
# tanggal : untuk menyimpan tanggal dari nama file
# carimenu : untuk menyimpan pilihan menu yang dicari
# menu : untuk menyimpan daftar menu
def SearchMenu(carimenu, menu):
    file = "Tubes-Daspro/transaksi.csv" 
    found = False
    print("\n====== Hasil Pencarian ======\n")
    num = 1
    data = bacacsv(file, 4)
    i = 0
    status=True
    while status==True:
        if data[i][0] == None:
            status=False
        elif (data[i][1] == menu[carimenu-1][0]):   
            print(f"{num}. Meja {data[i][0]}, Menu {data[i][1]}, Jumlah {data[i][2]}, Total Rp {data[i][3]}")
            found = True
            num += 1
        i += 1
    if not found:
        print(f"Menu tidak ditemukan dalam transaksi.")
    input("\nTekan Enter untuk kembali ke menu admin: ")
    menuAdmin()

# Fungsi untuk mengelola menu
# plh : untuk menginput pilihan menu
# tambahMenu : untuk menambahkan menu baru
# hapusMenu : untuk menghapus menu yang ada
# editMenu : untuk mengedit menu yang ada      
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
        kelolaMenu()

def campur(mtransaksi,s_array, j_array, n, x, z):
    y = 0
    for i in range(n):
        status = False
        for j in range(y):
            if mtransaksi[i][x] == s_array[j]:
                j_array[j] += int(mtransaksi[i][z])
                status = True
        if not status:
            s_array[y] = mtransaksi[i][x]
            j_array[y] = int(mtransaksi[i][z])
            y += 1

def tampilPendapatan():
    os.system("cls")
    print("\n====== Tampil Pendapatan ======\n")
    print("1.Pendapatan Hari Ini")
    print("2.Pendapatan Hari Tertentu")
    print("3.Kembali")
    plh=int(input("Masukkan pilihan: "))
    if plh ==1:
        PendapatanHariIni()
    elif plh ==2:
        PendapatanHari()
    elif plh ==3:
        menuAdmin()
    else:
        print("Pilihan tidak valid")
        tampilPendapatan()
def PendapatanHariIni():
    os.system("cls")
    nama = 'Tubes-Daspro/transaksi.csv'
    cek=cekcsv(nama)
    if cek == False:
        mtransaksi = bacacsv(nama,4)
        i = 0
        n = 0
        jumlah = 0
        while mtransaksi[i][0] != None:
            jumlah += int(mtransaksi[i][3])
            n += 1
            i += 1
        print("Total pendapatan hari ini: Rp.", jumlah)
        print('=' * 30)
        print("Total Pendapatan dari meja:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 0, 3)
        for i in range(n):
            if s_array[i] != None:
                print(f"Meja {s_array[i]} : Rp.{j_array[i]}")
        print('=' * 30)
        print("Total pendapatan/menu:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 1, 3)
        for i in range(n):
            if s_array[i] != None:
                print(f"Menu {s_array[i]} : Rp.{j_array[i]}")
        print('=' * 30)
        print("Jumlah Menu yang laku:")
        s_array = [None] * 100
        j_array = [0] * 100
        campur(mtransaksi,s_array, j_array, n, 1, 2)
        for i in range(n):
            if s_array[i] != None:
                print(f"Menu {s_array[i]} : {j_array[i]}")
        print('=' * 30)
        input("\nTekan Enter untuk kembali ke menu admin: ")
        tampilPendapatan()
    else:
        print("Belum ada transaksi")
        input("\nTekan Enter untuk kembali ke menu Admin: ")
        menuAdmin()

def PendapatanHari():
    os.system("cls")
    tanggal=input("Masukkan tanggal (DDMMYYYY): ")
    nama = f"Tubes-Daspro/transaksi_{tanggal}.csv"
    mtransaksi = bacacsv(nama,4)
    i = 0
    n = 0
    jumlah = 0
    while mtransaksi[i][0] != None:
        jumlah += int(mtransaksi[i][3])
        n += 1
        i += 1
    print("Total pendapatan hari ini: Rp.", jumlah)
    print('=' * 30)
    print("Total Pendapatan dari meja:")
    s_array = [None] * 100
    j_array = [0] * 100
    campur(mtransaksi,s_array, j_array, n, 0, 3)
    for i in range(n):
        if s_array[i] != None:
            print(f"Meja {s_array[i]} : Rp.{j_array[i]}")
    print('=' * 30)
    print("Total pendapatan/menu:")
    s_array = [None] * 100
    j_array = [0] * 100
    campur(mtransaksi,s_array, j_array, n, 1, 3)
    for i in range(n):
        if s_array[i] != None:
            print(f"Menu {s_array[i]} : Rp.{j_array[i]}")
    print('=' * 30)
    print("Jumlah Menu yang laku:")
    s_array = [None] * 100
    j_array = [0] * 100
    campur(mtransaksi,s_array, j_array, n, 1, 2)
    for i in range(n):
        if s_array[i] != None:
            print(f"Menu {s_array[i]} : {j_array[i]}")
    print('=' * 30)
    input("\nTekan Enter untuk kembali ke menu admin: ")
    tampilPendapatan()

# Fungsi buat akun untuk admin 
# username = var input string buat username
# password = var input string buat password
# file_path = filepath csv
# data = var array simpan username dan password
def signup():
    username = str(input("Buat Username anda: "))
    password = str(input("Buat Password anda: "))
    file_path = "Tubes-Daspro/account.csv"
    data = [username, password]
    with open(file_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Akun berhasil dibuat!")
    print("Kembali")
    login()

# Fungsi login untuk admin 
# nama = filepath csv
# maccount = data login admin 
# plh = var int input pilih jenis 
# username = var input username  
# password = var input password
# index = var iterasi
# status = var boolean
# cstatus = var booleabn
# ask = var input string yes or no
def login():
    os.system("cls")
    nama = 'Tubes-Daspro/account.csv'
    maccount = bacacsv(nama, 2)
    print("\n====== MENU AWAL ======\n")
    print("1.Sign Up Account")
    print("2.Log in")
    print("3.Keluar")
    plh = int(input("Pilih: "))
    if plh == 1:
        print("\n====== SignUp Account ======\n")
        signup()
    elif plh == 2:
        print("\n====== Login Admin ======\n")
        username = input("Username: ")
        password = input("Password: ")
        index = 0
        status = True
        cstatus=False
        while status==True:
            if(maccount[index][0]==None):
                status=False
                cstatus=True
            if maccount[index][0] == username and maccount[index][1] == password:
                print(f"Login berhasil! Selamat datang {maccount[index][0]} !")
                time.sleep(3)
                menuAdmin()
                status = False
            index += 1
        if cstatus==True:
            print("Login gagal, Username atau Password salah.")
            time.sleep(2)
            ask = str(input("\nApakah mau lanjut login (y/n)")).upper()
            if ask == "N":
                main()
            else:
                login()
    elif plh == 3 :
        main()
    else:
        print("Pilihan tidak valid. Silahkan pilih 1, 2, atau 3.")
        time.sleep(2)
        login()

# Fungsi untuk menampilkan loading bar
# i : untuk menghitung jumlah iterasi
# persen : untuk menghitung persentase dari total
# bar : untuk menyimpan string dari loading bar
# j : untuk menghitung jumlah karakter yang sudah diisi
# k : untuk menghitung jumlah karakter yang belum diisi
def loading(total):
    for i in range(total + 1):
        persen = (i * 100) / total  # buat itung persen 
        bar = ''
        for j in range(i):
            bar += '='
        for k in range(total - i):
            bar += ' '
        #\r untuk menghapus baris sebelumnya
        print(f'\r[{bar}] {int(persen)}%', end='')
        time.sleep(0.2)
    return 

def tambahStok():
    os.system("cls")
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file, 3)
    print("\n====== Tambah Stok ======\n")
    tampilanMenu()
    baris = int(input("Pilih nomor menu untuk menambah stok: ")) - 1
    if (baris < 0 or menu[baris][0] == None):
        print("Nomor menu tidak ada")
        time.sleep(2)
        tambahStok()
        return
    else:
        menuAdmin()
    tambah_stok = int(input("Masukkan jumlah stok yang ingin ditambahkan: "))
    menu[baris][2] = int(menu[baris][2]) + tambah_stok  

    with open(file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga", "Stok"])
        i = 0
        while (menu[i][0] != None):
            writer.writerow(menu[i])
            i += 1
    print("Stok berhasil ditambahkan.")
    time.sleep(2)
    menuAdmin()

# Fungsi menampilkan menu yang ada
# file = filepath csv
# menu = data menu yang ada
# num = var nampilin nomor
# i  = var iterasi
# stok = var stok makanan
def tampilanMenu():
    global menu
    global num
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,3)
    print("\n====== Menu ======\n")
    num = 1
    i=0
    while (menu[i][0] != None):
        stok = menu[i][2]
        if stok == "0":
            print(f"{num}. {menu[i][0]} - Rp {menu[i][1]} - Stok:(habis)")
        else:    
            print(f"{num}. {menu[i][0]} - Rp {menu[i][1]} - Stok:{menu[i][2]}")
        num += 1
        i +=1
    return menu
# Fungsi untuk menambahkan menu baru
# file : untuk menyimpan menu.csv
# nama : untuk menginput nama menu baru
# harga : untuk menginput harga menu baru
# writer : untuk menulis data ke dalam file csv
def tambahMenu():
    os.system("cls")
    file = "Tubes-Daspro/menu.csv"
    print("\n====== Tambah Menu ======\n")
    tampilanMenu()
    nama = str(input("Masukkan menu baru: "))
    harga = int(input("Harga menu: "))
    stok = int(input("jumlah stok awal: "))
    with open(file, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([nama, harga, stok])
    print("Menu berhasil ditambahkan")
    time.sleep(2)
    kelolaMenu()

# Fungsi untuk mengedit menu yang sudah ada
# file : untuk menyimpan menu.csv
# menu : untuk menyimpan data dari file csv
# baris : untuk menginput nomor menu yang ingin diedit
# edit_nama : untuk menginput nama baru
# edit_harga : untuk menginput harga baru
# writer : untuk menulis data ke dalam file csv
# i : untuk menghitung jumlah menu yang sudah ada
def editMenu():
    os.system("cls")
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,3)
    print("\n====== Edit Menu ======\n")
    tampilanMenu()
    baris = int(input("Pilih nomor menu yang ingin diedit: ")) - 1
    if (baris < 0 or menu[baris][0] == None):
        print("Nomor menu tidak ada")
        time.sleep(2)
        kelolaMenu()
        return
    else:
        kelolaMenu()
    
    edit_nama = input("Edit nama (kosongkan jika tidak ingin diubah): ")
    edit_harga = input("Edit harga (kosongkan jika tidak ingin diubah): ")
    if edit_nama != "":
        menu[baris][0] = edit_nama
    elif edit_harga != "":
        menu[baris][1] = edit_harga

    with open(file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga","Stok"])
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

# Fungsi untuk menghapus menu yang sudah ada
# file : untuk menyimpan menu.csv
# menu : untuk menyimpan data dari file csv
# hapus : untuk menginput nomor menu yang ingin dihapus
def hapusMenu():
    os.system("cls")
    file = "Tubes-Daspro/menu.csv"
    menu = bacacsv(file,3)
    tampilanMenu()
    hapus = int(input("Masukkan nomor menu yang ingin dihapus: ")) -1
    if (hapus < 0 or menu[hapus][0] == None):
        print("Nomor menu tidak ada")
        time.sleep(2)
        kelolaMenu()
    else:
        kelolaMenu()
    #hapus data dari csv
    menu[hapus][0] = None

    with open(file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga","Stok"])
        for row in menu:
            if (row[0] != None):
                writer.writerow(row)
       
    print("Menu berhasil dihapus.")
    time.sleep(2)
    kelolaMenu()

# Fungsi cek member ada atau tidak
# total = var total yang harus dibayar setelah diskon
# discount = var boolean discount 
# loginStatus = var boolean ada tidaknya member
# telp = var input no telp member
# pw = var input password member
# index = var iterasi
# status = var boolean
# mmember = data member dari csv
# nama = filepath csv
# diskon = var besaran diskon
def cekmember():
    global total
    discount = False
    loginStatus = False
    nama = 'Tubes-Daspro/member.csv'
    mmember = bacacsv(nama, 3)
    while loginStatus==False:
        clogin=True
        telp = input("Masukkan nomor telepon member: ")
        pw = input("Masukkan password member: ")
        index = 0
        status = True
        while status==True:
            if(mmember[index][0]==None):
                status=False
                loginStatus=True
            elif mmember[index][0] == telp and mmember[index][2] == pw:
                print(f"Login berhasil! Selamat datang {mmember[index][1]} !")
                time.sleep(3)
                status = False
                diskon=90/100
                discount=True
                loginStatus=True
                clogin=False
            index += 1
        if clogin==True:
            print("Member tidak ditemukan mohon masukkan ulang no.telepon dan password")
            time.sleep(2)
            diskon=0
            loginStatus=False
    if discount:
        print(f"\nTotal Bayar setelah discount: Rp. {int(total * diskon)}")
        total = int(total * diskon)
    else:
        print(f"\nTotal Bayar: Rp. {total}")

# Fungsi membuat member untuk user 
# telp = var input string no telp
# nama = var input string nama user
# pw = var input string password

def buatmember():
    telp = str(input("Masukkan telp anda: "))
    nama = str(input("Masukkan nama anda: "))
    pw = str(input("Buat password anda: "))
    file_path = "Tubes-Daspro/member.csv"
    data = [telp, nama,pw]
    with open(file_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)
    print("Akun berhasil dibuat!")
    cekmember()

def GiveRating():
    nama=str(input("Masukkan nama anda: "))
    Rating = int(input("Masukkan rating anda (1-10): "))
    deskripsi = str(input("Masukkan pesan anda"))
    file_path = "Tubes-Daspro/rating.csv"
    data=[nama,Rating,deskripsi]
    with open(file_path, mode="a+", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(data)

def tampilrating():
    os.system("cls")
    print("\n====== Rating Cafe ======\n")
    nama = 'Tubes-Daspro/rating.csv'
    mrating = bacacsv(nama, 3)
    i=0
    num=1
    jumlah=0
    while(mrating[i][0]!=None):
        if(mrating[i][0]!=None):
            print("Nama :",mrating[i][0])
            print("Rating :",mrating[i][1])
            print("Deskripsi :",mrating[i][2])
            simpan=int(mrating[i][1])
            jumlah+=simpan
        print()
        num+=1
        i+=1
    rata_rata=jumlah/i
    print("Rata-rata rating cafe:",round(rata_rata,1))
    input("\nTekan Enter untuk kembali ke menu user:")
    usermenu()
    
def usermenu():
    os.system("cls")
    print("\n====== Menu User ======\n")
    print("1.Order")
    print("2.Tampil Rating")
    print("3.Keluar")
    plh=int(input("Pilih fitur: "))
    if plh==1:
        prosesUser()
    elif plh==2:
        tampilrating()
    elif plh ==3:
        main()
    else:
        input("Pilihan tidak ada mohon input ulang (enter)")
        usermenu()

# fungsi pembelian makanan untuk user
# meja = var input milih nomor meja
# layanan = var input pilih takeaway/dine in
# menu = manggil fungsi tampilanMenu() 
# pesanan = array menyimpan nama, jumlah, harga
# jumlahPesanan = var simpan jumlah pesanan yang ada
# cond = var boolean looping while 
# pilihMakanan = var input int pilih menu makanan 
# num = var jumlah menu yang tersedia dari fungsi tampilanMenu()
# index = var iterasi
# stok_makanan = var stok makanan yang tersedia
# jumlah = var jumlah makanan yang dipesan
# menu = array dari fungsi tampilanMenu()
# pesanan = array matriks
# jumlahPesanan = var jumlah pesanan yang dipesan oleh user
# nama = var nama menu yang dipilih
# harga = var harga menu yang dipilih
# totalItem =  total bayar per item yang dipilih dari jumlah * harga
# transaksi = array matriks menyimpan meja, nama, jumlah, totalItem
# jumlahTranskasi = var jumlah transaksi yang dipesan oleh user
# total = harga seluruh barang yang harus dibayar
# subtotal = rincian harga per item
# condPunyaMember = var boolean
# condBuatMember = var boolean
# i_member = var input string punya member atau tidak
# askMember = var input string mau buat member atau tidak
# bayar = var input int bayar
# kembalian = var kembalian dari uang yang dibayar
# i_rating = var input string masukan rating
def prosesUser():
    global jumlahTransaksi,total
    os.system("cls")
    meja = 0
    print("\n====== Layanan Cafe ======\n")
    layanan = int(input("Pilih layanan (1. Takeaway | 2. Dine In |3.Kembali): "))
    if layanan == 2:
        meja = input("Masukkan nomor meja: ")
    elif layanan == 1:
        meja = "Takeaway"
    elif layanan==3:
        main()
    else:
        print("Masukkan 1 atau 2.")
        time.sleep(2.5)
        prosesUser()

    pesanan = [None]*100
    for i in range(0,100,1):
        pesanan[i]=[None]*3
    jumlahPesanan = 0
    menu = tampilanMenu()
    cond = True
    while cond == True:
        pilihMakanan = int(input("\nPilih nomor menu (0 jika selesai): "))
        if pilihMakanan == 0:
            cond = False
            lanjut=str(input("Mau lanjut pesan?[Y/N]: "))
            if lanjut=='Y':
                cond=True
            elif lanjut=='N':
                usermenu()
        elif pilihMakanan >= num:
            print(f"Maaf makanan nomor {pilihMakanan} tidak ada, silahkan pilih makanan lain")
        else:
            index = pilihMakanan - 1
            stok_makanan = int(menu[index][2])
            if stok_makanan == 0:
                print(f"Maaf, {menu[index][0]} sudah habis.")
            else:
                jumlah = int(input("Masukkan Jumlah: "))
                if jumlah <= 30 and int(menu[index][2]) >= jumlah:
                    nama = menu[index][0]
                    harga = int(menu[index][1])
                    pesanan[jumlahPesanan] = [nama, jumlah, harga]
                    totalItem = harga * jumlah
                    transaksi[jumlahTransaksi] = [meja, nama, jumlah, totalItem]
                    jumlahTransaksi += 1
                    jumlahPesanan += 1
                    menu[index][2] = int(menu[index][2]) - jumlah
                else:
                    print("Maaf pesanan tidak bisa melebihi 30 item atau makanan sudah habis.")

    print("\n====== Struk Pembayaran ======\n")
    total = 0
    for i in range(jumlahPesanan):
        nama, jumlah, harga = pesanan[i]
        subtotal = jumlah * harga
        print(f"{nama} x{jumlah} = Rp {subtotal}")
        total += subtotal

    condPunyaMember = False
    while not condPunyaMember:
        i_member = input("Apakah anda sudah mempunyai member (y/n): ").upper()
        if i_member == "Y":
            cekmember()
            condPunyaMember = True
        elif i_member == "N":
            condBuatMember = False
            while not condBuatMember:
                askMember = input("Apakah anda mau membuat member (y/n): ").upper()
                if askMember == "Y":
                    buatmember()
                    condBuatMember = True
                    condPunyaMember = True
                elif askMember == "N":
                    print("Total yang harus dibayar:", total)
                    condBuatMember = True
                    condPunyaMember = True
                else:
                    print("Masukkan hanya 'y' atau 'n'.")
        else:
            print("Masukkan hanya 'y' atau 'n'.")

            
    bayar = int(input("Masukkan jumlah uang: "))
    while bayar < total:
        print("Uang tidak cukup.")
        bayar = int(input("Masukkan ulang uang: "))
    kembalian = bayar - total
    print(f"Kembalian: Rp. {kembalian}")
    time.sleep(3)
    os.system("cls")
    print("Pesanan Anda sedang diproses.")
    loading(30)
    print("\nPesanan Anda telah selesai!")
    time.sleep(1.5)
    i_rating = str(input("Apakah anda mau memberikan rating ke restoran ini? (y/n): ")).upper()
    if i_rating=="Y":
        GiveRating()
    else:
        print("Terimakasih sudah datang ke restoran kami!")
    time.sleep(1.5)
    simpan_transaksi_csv()
    with open("Tubes-Daspro/menu.csv", mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Menu", "Harga", "Stok"])
        for i in range(num - 1):
            if menu[i][0] != None:
                writer.writerow(menu[i])
    main()

def simpan_transaksi_csv():
    path = "Tubes-Daspro/transaksi.csv"
    cek=cekcsv(path)
    if cek == True:
        with open(f'Tubes-Daspro/transaksi.csv', 'w',newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Meja","Menu","Jumlah","Total"])
            for i in range(jumlahTransaksi):
                writer.writerow(transaksi[i])
    else:
        with open(path, mode="a+", newline="") as file:
            writer = csv.writer(file)
            for i in range(jumlahTransaksi):
                writer.writerow(transaksi[i])
    print("Data transaksi telah disimpan ke transaksi.csv")

# Fungsi menu utama
# role = pilih role admin/user
def main():
    os.system("cls")
    print("=" * 50)
    print(" Selamat Datang di Program Manajemen Cafe MyCafe!")
    print("=" * 50)
    print("\n1. Admin\n2. User\n")
    role = int(input("Pilih Jenis Login: "))
    if role == 1:
        login()
    elif role == 2:
        usermenu()
    else:
        print("Input Tidak Valid. Pilih 1 atau 2")
        time.sleep(2)
        main()

if __name__ == '__main__':
    members = [None]*100
    for i in range(0,100,1):
        members[i]=[None]*3
    jumlahMember = 0
    transaksi = [None]*100
    for i in range(0,100,1):
        transaksi[i]=[None]*4
    jumlahTransaksi = 0
    main()
