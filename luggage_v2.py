# Learning the different aspects of packing and unpacking of dictionaries in
#   relationship to functions along with the understanding of packing and
#   unpacking of tuples

def packer(name = None, **kwargs):
    print(kwargs)

def unpacker(first_name = None, last_name = None):
    if first_name and last_name:
        print("Hi, {} {}!".format(first_name, last_name))
    else:
        print("Hi no name!")

packer(
    name = 'Tommy',
    num = 49,
    spanish_inquistion = None
    )

unpacker(
    **{"last_name": "Klapheke",
       "first_name": "Jeffery"
       }
    )

course_minutes = {
    "Python Basics": 232,
    "Django Basics": 237,
    "Flask Basics": 189,
    "Java Basics": 133
    }

for course, minutes in course_minutes.items():
    print("{} is {} minutes long".format(course, minutes))
