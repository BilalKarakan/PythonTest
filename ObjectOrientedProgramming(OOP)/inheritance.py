# Inheritance (Kalıtım): Classların birbirinden özellik alması

# Person ==> Firsname, Lastname, age, job, eat(), run(), drink()
# Student(Person), Teacher(Person)

# Animal ==> Dog(Animal), Cat(Animal)
"""
class Person():
    def __init__(self):
        print("Person Created")

class Student(Person):
    def __init__(self):
        Person.__init__(self)
        print("Student Created")    # Sadece Student classının sahip olduğu özellikleri alır.
        #Personın özelliklerinin kaybolmaması için ._init kullanmak zorundayız.

p1 = Person()
s1 = Student()
"""

"""
class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname):
        Person.__init__(self, fname, lname)
        print("Student Created")    # Sadece Student classının sahip olduğu özellikleri alır.
        #Personın özelliklerinin kaybolmaması için ._init kullanmak zorundayız.

    # Override
    def who_am_i(self):
        print("I am a student")    # Person classını böyle ezebiliriz.

p1 = Person("Elif", "Delen")
s1 = Student("Bilal", "Karakan")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName)

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
"""

class Person():
    def __init__(self, fname, lname):
        self.firstName = fname
        self.lastName = lname
        print("Person Created")

    def who_am_i(self):
        print("I am a person")

    def eat(self):
        print("I am eating")

class Student(Person):
    def __init__(self, fname, lname, number):
        Person.__init__(self, fname, lname)
        print("Student Created")    # Sadece Student classının sahip olduğu özellikleri alır.
        #Personın özelliklerinin kaybolmaması için ._init kullanmak zorundayız.
        self.studentNumber = number

    # Override
    def who_am_i(self):
        print("I am a student")    # Person classını böyle ezebiliriz.
    
    def sayHello(self):
        print("Hello I am a student")

class Teacher(Person):
    def __init__(self, fname, lname, branch):
        super().__init__(fname, lname)   # Student classında kullandığımıza alternatif
        self.branch = branch

    def who_am_i(self):
        print(f"I am a {self.branch} teacher")
        

p1 = Person("Elif", "Delen")
s1 = Student("Bilal", "Karakan", 111)
t1 = Teacher("Emine", "Albaş", "Linear Algebra")

print(p1.firstName + " " + p1.lastName)
print(s1.firstName + " " + s1.lastName + " " + str(s1.studentNumber))

p1.who_am_i()
s1.who_am_i()
p1.eat()
s1.eat()
s1.sayHello()
t1.who_am_i()