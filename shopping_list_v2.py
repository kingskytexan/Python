# Script for creating a simple shopping list when you need food with some added functionality to easliy replace various bits of my app

shopping_list = []


def show_help():
    print("What should we pick up form the store?")
    print("""
    Enter 'DONE' to stop adding items and to print out your list
    Enter 'HELP' for the script's help
    Enter 'SHOW' to see what items you have in your list
    """)

while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    shopping_list.append(new_item)

print("Here's your list: ")

for item in shopping_list:
    print(item)
