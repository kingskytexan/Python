# Script for creating a simple shopping list when you need food with some added functionality to easliy replace various bits of my app

shopping_list = []


def show_help():
    print("What should we pick up form the store?")
    print("""
    Enter 'DONE' to stop adding items and to print out your list
    Enter 'HELP' for the script's help
    Enter 'SHOW' to see what items you have in your list
    """)

def show_list():
    print("Here's your list: ")

    for item in shopping_list:
        print(item)

def add_to_list(new_item):
    shopping_list.append(new_item)
    print("Added {}. List now has {} items.".format(new_item, len(shopping_list)))

show_help()

while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    elif new_item == 'HELP':
        show_help()
        continue
    elif new_item == "SHOW":
        show_list()
        continue
    add_to_list(new_item)

show_list()

