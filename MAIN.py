import mysql.connector
db = mysql.connector.connect(
    host="localhost",
    user="root",
    database="daspro"
)

cursor = db.cursor()
#PROGRAM MANAGEMENT RESTORAN 
def password(username,password):
    query = "SELECT username, password FROM account"
    cursor.execute(query)
    # Ambil hasil query
    result = cursor.fetchone()
    if result:
        db_username, db_password = result
        if (password == db_password):  # Bandingkan dengan hash!
            print("Login berhasil!")
            role=username
        else:
            print("Password salah.")
    else:
        print("Username tidak ditemukan.")
    return role
def admin():
    print
def role():
    if(role=="admin"):
        admin()
    i_user=str(input("Username:"))
    i_password=str(input("Password:"))
    role=password(i_user,i_password)
    if(role=="admin"):
        print
def main():




if __name__ == '__main__':    
    main()   