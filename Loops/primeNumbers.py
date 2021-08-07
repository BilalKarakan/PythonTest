number = int(input("Enter a number: "))

isPrime = True

if number == 1:
    print(f"{number} is not a prime number")

if number < 1:
    print("Invalid number")

for i in range(2,number):
    if number % i == 0:
        isPrime = False

if isPrime == True:
    print(f"{number} is a prime number")
else:
    print(f"{number} is not a prime number")