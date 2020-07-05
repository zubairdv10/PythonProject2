import DiffParts
import MainMenu2

def mainMenu():
    user_select = input("""WELCOME TO LIFE_CHOICES_ONLINE
    Please select a option :
    1.Register(If you are new here)
    2.Login
    3.exit
    option : """)
    try:
        option_selected = int(user_select)
        if option_selected == 1:
            DiffParts.registration()
            print("You have been registered successfully")
        elif option_selected == 2:
            MainMenu2.userMenu()
        else:
            print("Thank you for your time , please come again soon")
            exit()
    except ValueError:
        print("incorrect option not valid\n")
        mainMenu()
mainMenu()
exit()