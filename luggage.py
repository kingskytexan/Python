# Learning the different aspects of packing and unpacking of dictionaries in
#   relationship to functions

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
