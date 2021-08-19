def square(num): return num ** 2

result = square(int(input("Enter a number: ")))
print(result)


numbers = [1, 3, 4, 6, 7, 9]

result = list(map(square, numbers))
print(result)
#-------------------------------------------
numbers = [1, 3, 4, 5, 6, 7, 9]

lambda num: num ** 2
result = list(map(lambda num: num ** 2, numbers))
print(result)
#---------------------------------------------
square = lambda num: num ** 2
print(list(map(square, numbers)))

result = square(3)
print(result)
#-----------------------------------------------
def check_even(num):
    return num % 2 == 0
result = list(filter(check_even, numbers))
print(result)
#----------------------------------------------
lambda num: num % 2 == 0
result = list(filter(lambda num: num % 2 == 0, numbers))
print(result)
#------------------------------------------------
check_even = lambda num: num % 2 == 0
result = list(filter(check_even, numbers))
print(result)