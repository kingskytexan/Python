# Script for creating a simple shopping list when you need food with some added functionality to easliy replace various bits of my app
#   

import os

shopping_list = []

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_help():
    clear_screen()
    print("What should we pick up form the store?")
    print("""
    Enter 'DONE' to stop adding items and to print out your list
    Enter 'HELP' for the script's help
    Enter 'SHOW' to see what items you have in your list
    Enter 'REMOVE' to deleate an item form the list
    """)


def add_to_list(item):
    show_list()
    if len(shopping_list):
        position = input("Where should I add {}?\n"
                         "Press ENTER to add to the end of the list\n"
                         "> ",format(item))
    else:
        position = 0
    try:
        position = abs(int(position))
    except ValueError:
        position = None
    if position is not None:
        shopping_list.insert(position-1, item)
    else:
        shopping_list.append(new_item)

    show_list()
    


def show_list():
    clear_screen()
    print("Here's your list: ")
    
    for index, item in enumerate(shopping_list, start=1):
        print("{}. {}".format(index, item))
        
    print("-" * 10)


def remove_from_list():
    show_list()
    want_to_remove = input("What would you like to remove?/n> ")
    try:
       shopping_list.remove(want_to_remove)
    except ValueError:
        pass
    show_list()

show_help()

while True:
    new_item = input("> ")
    
    if new_item.upper() == "DONE" or new_item.upper() == 'QUIT':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == "SHOW":
        show_list()
        continue
    elif new_item.upper() == "REMOVE":
        remove_from_list()
        continue
    else:
        add_to_list(new_item)

show_list()
