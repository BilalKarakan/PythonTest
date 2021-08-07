# for x in range(10):
#     print(x)

# numbers = [x for x in range(10)]
# print(numbers)

# numbers = []
# for x in range(10):
#     numbers.append(x)
# print(numbers)

# for x in range(10):
#     print(x**2)
# numbers = [x**2 for x in range(10)]
# print(numbers)

# numbers = [x*x for x in range(10) if x%3==0]
# print(numbers)

myString = "Hello"
myList = []

for letter in myString:
    myList.append(letter)
print(myList)

myList = [letter for letter in myString]
print(myList)

years = [1983, 1996, 1952, 2005, 1971]
ages = [2021-age for age in years]
print(ages)

result = [x if x%2==0 else "Tek Sayı" for x in range(1,10)]
print(result)

result = []

for x in range(3):
    for y in range(3):
        result.append((x,y))
print(result)

result = [(x,y) for x in range(3) for y in range(3)]
print(result)