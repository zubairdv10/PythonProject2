import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",passwd="1234",database="lifechoicesonline")

mycursor = mydb.cursor()
#registering a new user
def registration():
    sql = "Insert into users values (%s, %s, %s, %s, %s, %s)"
    Id = int(input("Please enter your id: "))
    full_name = input("Please enter your full name: ")
    username = input("Please enter username: ")
    password = str(input("Please enter password: "))
    date=input("Please enter the date you came to the premises:")
    time=input("Please enter the time you came: ")
    myrec = [Id, full_name, username, password, date, time]
    try:
        mycursor.execute(sql, myrec)
        mydb.commit()
        print("Successfully added")
    except:
        print("record exist")

#old users can login
def login():
    sql = "SELECT * FROM users WHERE username=%s and password=%s"
    username = input("Please enter username: ")
    password = str(input("Please enter your password: "))
    myrec = username, password
    try:
        mycursor.execute(sql, myrec)
        print("Your password and username match please proceed")
    except:
        print("Your password and username do not match")
        exit()

#the time they exited the building
def logout_time():
    sql = "INSERT INTO logout values (%s, %s)"
    Id = int(input("Please enter your Id: "))
    logoutTime = input("Please enter the time that you have left the premises: ")
    myrec = Id, logoutTime
    try:
        mycursor.execute(sql, myrec)
        mydb.commit()
        print("Have a good day further")
    except:
        print("username does not match")

