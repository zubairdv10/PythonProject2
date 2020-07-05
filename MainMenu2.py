import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="1234", database="lifechoicesonline")

mycursor = mydb.cursor()

import DiffParts


def userMenu():
    DiffParts.login()
    user_select_option = input("""Please choose an option :
    1)Logout time
    2)exit menu
    option : """)

    try:
        option_selected = int(user_select_option)
        if option_selected == 1:
            DiffParts.logout_time()
            userMenu()
        else:
            exit()
    except ValueError:
        print("incorrect option not valid\n")
