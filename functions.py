# Learning how functions are created, maintained, can called within Python 

def hows_the_parrot():
    print("He's pining for the fjords.")

hows_the_parrot()



def lumbarjack(name, pronoun):
    print("{}'s a lumberjack and {} OK!".format(name, pronoun))

lumbarjack("Tommy", "he's")
lumbarjack("Amy", "she's")



def average(num1, num2):
    return (num1 + num2) / 2

avg = average(2, 6)
print(avg)
