
def changeName(n):
    n = "Ayşe"
name = "Ahmet"
changeName(name)
print(name)


def change(n):
    n[0] = "istanbul"
cities = ["Ankara", "İzmir"]
change(cities)
print(cities)


def change(n):
    n[0] = "İstanbul"
cities = ["Ankara", "İzmir"]
n = cities[:] #slicing
n[0] = "İstanbul"
print(cities)
print(n)

def change(n):
    n[0] = "İstanbul"
cities = ["Ankara", "İzmir"]
change(cities[:])
print(cities)

def add(a, b, c = 0):
    return sum((a, b, c))
print(add(20, 53))
print(add(20, 53, 22))

def add(*parameters):
    print(parameters)
    print(parameters[1]) # Bir tuple liste oluşturur.
    return sum((parameters))
print(add(29, 33))
print(add(43, 54, 76))
print(add(65, 43, 64, 32, 23))

def add(*parameters):
    sum = 0
    for i in parameters:
        sum = sum + i
    return sum

def displayUser(**args):
    print(type(args))
    for key, value in args.items():
        print("{} is {}".format(key,value))

displayUser(name = "Ayşe", age = 12, city = "Ankara")
displayUser(name = "Ahmet", age = 14, city = "İstanbul", phone = 123123)
displayUser(name = "Ali", age = 16, city = "İzmir", phone = 12341234, email = "ali@gmail.com")

# for tuple "*"
# for dictionary "**"

def myFunc(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
myFunc(20, 30, 45, 55, key1 = "value1", key2 = "value2")
