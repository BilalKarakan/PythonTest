# class
class Person:
    address =  "No information"
    # class attributes

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.birthyear = year
        print("init metodu çalıştı.")
    # methods

# object (instance)
p1 = Person("Bilal", 1998)
p2 = Person("Elif", 2017)
# p1 = Person(name = "Bilal", year = 1998)
# p2 = Person(name = "Elif", year = 2017)

# updating
p1.name = "Ali"
p2.address = "İzmir"

# accessing object attributes
print(f"for p1, name: {p1.name} year: {p1.birthyear} address: {p1.address}")
print(f"for p2, name: {p2.name} year: {p2.birthyear} address: {p2.address}")
# Different Address
print(p1)
print(p2)
print(type(p1))
print(type(p2))
print(p1 == p2)