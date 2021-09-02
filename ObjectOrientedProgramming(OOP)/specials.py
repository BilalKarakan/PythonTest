"""
myList = [1, 2, 3]
myString = "My string"

print(len(myList))
print(len(myString))
print(type(myList))
print(type(myString))

class Movie:
    pass

m = Movie()

print(len(m))
print(type(m))
"""

class Movie():
    def __init__(self, title, director, duration):
        self.title = title
        self.director = director
        self.duration = duration
        print("Movie objesi oluşturuldu.")

    def __str__(self):
        return f"{self.title} by {self.director}"

    def __len__(self):
        return self.duration

    def __del__(self):
        print("Film objesi silindi.")

# m = Movie("Film Adı", "Film Yönetmeni", "Film Süresi")
m = Movie("Film Adı", "Film Yönetmeni", 120)


myList = [1, 2, 3]

# print(str(myList))
# print(str(m))
print(len(myList))
print(len(m))
del m
print(m)