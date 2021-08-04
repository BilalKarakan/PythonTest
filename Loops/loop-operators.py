# RANGE

for x in range(10):
    print(x)


for x in range(1,10):
    print(x)


for x in range(1,10,2):
    print(x)
print(list(range(1, 10, 2)))

# ENUMERATE

index = 0
greeting = "Hello There"

for letter in greeting:
    print(f"index: {index}  letter: {greeting[index]}")
    index += 1


greeting = "Hello There"

for index, letter in enumerate(greeting):
    print(f"index: {index}  letter: {letter}")


greeting = "Hello There"

for item in enumerate(greeting):
    print(item)


greeting = "Hello There"

for index, item in enumerate(greeting):
    print(f"index: {index} letter: {item}")

# ZIP

list1 = [1, 2, 3, 4, 5]
list2 = ["a", "b", "c", "d", "e"]
list3 = [100, 200, 300, 400, 500]

print(list(zip(list1,list2,list3)))

for item in zip(list1,list2,list3):
    print(item)
for a, b, c in zip(list1, list2, list3):
    print(a, b, c)