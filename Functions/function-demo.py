# Gönderilen bir kelimeyi belirtilen kez ekranda gösteren fonksiyonu yazın.

message = str(input("Enter a word: "))
index = int(input("Enter a number: "))
k = 0
def display():
    print(message)
while k < index:
    k = k + 1
    display()

# OR

def write(word, piece):
    print(word * piece)
write("Hello World!\n", 10)

# Kendine gönderilen sınırsız sayıdaki parametreyi bir listeye çeviren fonksiyonu yazın.

def createList(*parameters):
    list = []
    for i in parameters:
        list.append(i)
    return list
result = createList(10, 20, 30, 40, 50, "Hello There")
print(result)

# OR

def makeList(*parameters):
    print(parameters)
makeList(10,20,30)

# Gönderilen iki sayı arasındaki tüm asal sayıları bulun

def  findPrimeNumbers(number1, number2):
    for number in range(number1, number2+1):
        if number > 1:
            for i in range(2,number):
                if (number % i == 0):
                    break
            else:
                print(number)
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
findPrimeNumbers(number1, number2)

# OR

number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))


def findNumbers():
    isPrime = True
    for i in range(number1+1, number2):
        for j in range(2,i):
            if i % j == 0:
                isPrime = False
                break
            else:
                isPrime = True
        if isPrime == True:
            print(f"{i} is a prime number.")
findNumbers()        

# Kendisine gönderilen bir sayının tam bölenlerini bir liste şeklinde döndüren fonksiyonu yazın.

number = int(input("Enter a number: "))
list = []
def createList():
    for i in range(1,number+1):
        if number % i == 0:
            list.append(i)
    print(list)
createList()

# OR


def findaliquots(number):
    list = []
    for i in range(1, number+1):
        if (number % i == 0):
            list.append(i)
    return list
print(findaliquots(20))