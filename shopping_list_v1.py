# Script for creating a simple shopping list when you need food

shopping_list = []

print("What should we pick up form the store?")
print("Enter 'DONE' to stop adding items and to print out your list")

while True:
    new_item = input("> ")
    if new_item == "DONE":
        break
    shopping_list.append(new_item)

print("Here's your list: ")

for item in shopping_list:
    print(item)
