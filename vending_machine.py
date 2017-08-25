sodas = ['Pepsi', 'Cheery Coke', 'Ale8']
chips = ['Cheetos', 'Doritos']
candy = ['Three Muskters', 'M&Ms', 'Snickers']

while True:
    choice = input("Would you like a soda, some chips, and or some candy? ").lower()

    try:
        if choice == 'soda':
            snack = sodas.pop()
        elif choice == 'chips':
            snack = chips.pop()
        elif choice == 'candy':
            snack =candy.pop()
        else:
            print("I'm sorry I did not understand that!")
            continue
        
    except IndexError:
        print("We're all out of {}! Sorry!".format(choice))
        
    else:
        print("Here's your {}: {}".format(choice, snack))
    
