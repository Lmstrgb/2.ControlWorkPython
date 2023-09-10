
from Note import *
import view
from main import *


def menu():
    global data
    data = load_notes()
    while True:
        action = view.show_menu()
        # action = input(
        # "Введите 'n' чтобы сделать новую заметку, 'r' чтобы прочитать, 'u' чтобы обновить, 'l' чтобы вывести список заметок, 'd' чтобы удалить,  'q' чтобы выйти: ")
        if action == "n":
            create_note(data)
        elif action == "r":
            read_note(data)
        elif action == "u":
            update_note(data)
        elif action == "d":
            delete_note(data)
        elif action == "l":
            list_notes(data)
        elif action == "q":
            break
        else:
            print("Неправильное действие")
