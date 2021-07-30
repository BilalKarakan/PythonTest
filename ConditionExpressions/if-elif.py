"""
x = int(input("x: "))
y = int(input("y: "))

if (x>y):
    print("x y'den büyüktür.")
elif (x == y):
    print("x ve y eşittir.")
else:
       print("y x'den büyüktür.") 
"""

number = int(input("Enter a number: "))

if (number > 0):
    print(f"{number} is greater than zero")
elif (number < 0):
    print(f"{number} is less than zero")
else:
    print(f"{number} is equal to zero")