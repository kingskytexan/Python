# Understanding the use of strings of Python

stuff = "stuff"
print(stuff)

junk = 'junk'
print(junk)

print('He\'s right!')
print("""He's right!""")
print('''He's right!''')

long_string = """Here's a new line:


It's right here!"""
print(long_string)

print(str(7))

print("Hello" + " there!")

name = "Tommy "
name += "Klapheke"
print(name)

print('=' * 40)

status_message = "Hey, we have {} people using the site right now"
print(status_message.format(8))
print(status_message.format(7))

message = "We have {} people with {} kids tonight"
print(message.format(7, 3))