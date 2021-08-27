"""
# class
class Person:
    address =  "No information"
    # class attributes

    # constructor (yapıcı metod)
    def __init__(self, name, year):
        # object attributes
        self.name = name
        self.birthyear = year
        
    # instance methods
    def intro(self):
        print("Hello There I am " + self.name)
    
    def calculateAge(self):
        return 2021 - self.birthyear

# object (instance)
p1 = Person("Bilal", 1998)
p2 = Person("Elif", 2017)

p1.intro()
p2.intro()

print(f"My name is {p1.name} and I am {p1.calculateAge()} years old.")
print(f"My name is {p2.name} and I am {p2.calculateAge()} years old.")
"""

class Circle:
    # class object attribute
    pi = 3.14
    def __init__(self, yaricap = 1):
        self.yaricap = yaricap

    def cevre_hesapla(self):      
        return 2 * self.pi * self.yaricap
    def alan_hesapla(self):
        return self.pi * (self.yaricap**2)
    
c1 = Circle() # yaricap = 1
c2 = Circle(3)

print(f"c1: alan = {c1.alan_hesapla()} çevre = {c1.cevre_hesapla()}")
print(f"c2: alan = {c2.alan_hesapla()} çevre = {c2.cevre_hesapla()}")
