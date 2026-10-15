space = "                         "

def main_menu():

    print(space)
    print("MAIN MENU")
    print(space)
    print("1. Add a run")
    print("2. View saved runs")
    print("3. Exit")
    print(space)

    return input("Please select a number from the Menu. ")

def user_menu_input(menu_input):

    if menu_input == "1":
        print("This is where the add a run feature would link from runs.py")
    elif menu_input == "2":
        print("This is where the view saved runs feature would link from runs.py")
    elif menu_input == "3":
        print("This is where the user would exit")
    else:
        print("sod off")


choice = main_menu()
user_menu_input(choice)

