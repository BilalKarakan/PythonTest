x = 3
if (x > 5):
    raise Exception ("The number you enter cannot be greater than 5.")
else:
    print(f"The number you enter {x}.")


def check_password(psw):
    import re
    if len(psw) < 15:
        raise Exception ("The password must be at least 14 characters!")
    elif not re.search("[a-z]",psw):
        raise Exception ("The password must contain lowercase letters.")
    elif not re.search("[A-Z]",psw):
        raise Exception ("The password must contain uppercase letters.")
    elif not re.search("[0-9]",psw):
        raise Exception ("The password must contain numbers")
    elif not re.search("[_@$#£]",psw):
        raise Exception ("The password must contain alpha numeric characters")
    elif re.search("[\s]",psw):
        raise Exception ("The password mustn't contain a space character")
    else:
        print("Everything is okay")
    

password = "1231432235352352345werwerJHIBI#@"

try:
    check_password(password)
except Exception as ex:
    print(ex)
else:
    print("Everything is okay.")
finally:
    print("The validation completed!")


class Person:
    def __init__(self,name,year):
        if len(name) > 10:
            raise Exception ("The name field cannot contain more than 10 characters")
        else:
            self.name = name

p = Person("Bilallllllll",1998)