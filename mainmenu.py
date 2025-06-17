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
        first_line = file.readline()
        if not first_line:
            return True
        second_line = file.readline()
        if not second_line:
            return True
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
    print("2.Transaksi Hari Tertentu")
    print("3.Kembali")
    plh=int(input("Masukkan pilihan: "))
    if plh ==1:
        TransaksiHariIni()
    elif plh ==2:
        lihatTransaksiHari()
    elif plh ==3:
        menuAdmin()

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



# Fungsi untuk membaca semua file transaksi
# data : sumber file
# file_transaksi : list untuk menyimpan nama file transaksi
# count : untuk menghitung jumlah file yang ditemukan
# file : untuk mengecek setiap file dalam folder
# file_valid : list untuk menyimpan nama file yang valid
def baca_semua_transaksi():
    data = 'Tubes-Daspro/'
    file_transaksi = [None] * 100  
    count = 0  
    for file in os.listdir(data):
        if file.startswith('transaksi_') and file.endswith('.csv'):
            if count < 100:  
                file_transaksi[count] = file
                count += 1
    file_valid = [file_transaksi[i] for i in range(count)]
    return file_valid 

# Fungsi untuk mencari transaksi berdasarkan menu
# found : untuk mengecek apakah menu ditemukan
# num : untuk menghitung jumlah transaksi yang ditemukan
# data : untuk menyimpan data dari file transaksi
# i : untuk indeks data
# tanggal : untuk menyimpan tanggal dari nama file
# carimenu : untuk menyimpan pilihan menu yang dicari
# menu : untuk menyimpan daftar menu
def SearchMenu(carimenu, menu):
    file_transaksi = baca_semua_transaksi()
    found = False
    print("\n====== Hasil Pencarian ======\n")
    num = 1
    for file in file_transaksi:
        data = bacacsv(f"Tubes-Daspro/{file}", 4)
        i = 0
        tanggal = file[10:18]
        while True:
            if data[i][0] == None:
                break
            elif (data[i][1] == menu[carimenu-1][0]):   
                print(f"{num}. Tanggal : {tanggal} Meja {data[i][0]}, Menu {data[i][1]}, Jumlah {data[i][2]}, Total Rp {data[i][3]}")
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
        kelolaMenu

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
            print(f"{num}. {menu[i][0]} - Rp {menu[i][1]} (habis)")
        else:    
            print(f"{num}. {menu[i][0]} - Rp {menu[i][1]}")
        num += 1
        i +=1
    return menu
# Fungsi untuk menambahkan menu baru
# file : untuk menyimpan menu.csv
# nama : untuk menginput nama menu baru
# harga : untuk menginput harga menu baru
# writer : untuk menulis data ke dalam file csv
def tambahMenu():
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

# Fungsi untuk menghapus menu yang sudah ada
# file : untuk menyimpan menu.csv
# menu : untuk menyimpan data dari file csv
# hapus : untuk menginput nomor menu yang ingin dihapus
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
    
def cekmember():
    global total
    discount = 0
    loginStatus = False
    nama = 'Tubes-Daspro/member.csv'
    mmember = bacacsv(nama, 3)
    while loginStatus==False:
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
            index += 1
        if status==True:
            print("Member tidak ditemukan mohon masukkan ulang no.telepon dan password")
            time.sleep(2)
            diskon=0
            cekmember()
            loginStatus=False    
    if discount:
        print(f"\nTotal Bayar setelah discount: Rp. {int(total * diskon)}")
        total = int(total * diskon)
    else:
        print(f"\nTotal Bayar: Rp. {total}")
        
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

def prosesUser():
    global jumlahTransaksi,total
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
    pesanan = [[None]*3 for _ in range(100)]
    jumlahPesanan = 0

    while True:
        pilihMakanan = int(input("\nPilih nomor menu (0 jika selesai): "))
        if pilihMakanan == 0:
            break
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
    i_member = str(input("Apakah anda sudah mempunyai member (y/n): ")).upper()
    if i_member == "Y":
        cekmember()
    elif i_member == "N":
        askMember = str(input("Apakah anda mau membuat member (y/n): ")).upper()
        if askMember == "Y":
            buatmember() 
        else:
            print("Total yang harus dibayar:",total)
        
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
    members = [[None]*3 for _ in range(100)]
    jumlahMember = 0
    transaksi = [[None]*4 for _ in range(100)]
    jumlahTransaksi = 0
    main()
