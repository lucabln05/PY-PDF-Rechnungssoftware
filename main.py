from pdf_create_script import pdf_creator
from database_connector import *
from win_main import main_window as main_gui


def menu():
    print('''

    1. Add Client
    2. Delete Client
    3. Update Client
    4. Search Client
    5. Create PDF
    6. Start GUI
    7. Exit  

    by lucabln05
        ''')

    while True:
    
        try:
            # ask the user what he wants to do
            user_input = int(input("What do you want to do? "))
            if user_input == 1:
                add_client()
            elif user_input == 2:
                delete_client()
            elif user_input == 3:
                update_client()
            elif user_input == 4:
                search_client()
            elif user_input == 5:
                pdf_creator()
            elif user_input == 6:
                main_gui()
            elif user_input == 7:
                exit()
            else:
                print("Please enter a valid number")
        except Exception as error:
            print(error)

menu()





