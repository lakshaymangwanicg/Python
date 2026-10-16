def format_name(first, last, uppercase=False):
    name = first + " " + last
    if uppercase == True:
        return name.upper()
    return name
print(format_name("lakshay","mangwani",True))