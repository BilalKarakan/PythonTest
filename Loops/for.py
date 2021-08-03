numbers = [1, 2, 3, 4, 5]

for i in numbers:
    print(i)

names = ["Dorothea", "Edward", "Will"]

for name in names:
    print(f"My name is {name}")

name = "Dorothea Brooks"

for i in name:
    print(i)

tuple = [(1, 2), (3, 2), (4, 5), (6, 7)]

for t in tuple:
    print(t)

for a, b in tuple:
    print(a)

dictionary = {"N1": "Dorothea", "N2": "Edward", "N3": "Will"}

for item in dictionary:
    print(item)

for item in dictionary.items():
    print(item)

for key, value in dictionary.items():
    print(key, value)