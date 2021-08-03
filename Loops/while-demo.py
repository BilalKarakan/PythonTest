numbers = [1, 2, 3, 5, 7, 9, 12, 19, 21]

# 1-) numbers listesindeki sayıları while ile ekrana yazdırın.

i = 0
while i < len(numbers):
    print(numbers[i])
    i += 1


# 2-) Başlangıç ve bitiş değerlerini kullanıcıdan alıp aradaki tüm tek sayıları ekrana yazdırın.

number1 = int(input("Başlangıç Sayısı: "))
number2 = int(input("Bitiş Sayısı: "))
x = number1 + 1
while x < number2:
    if (x % 2 == 1):
        print(x)
    x += 1

# 3-) 1-100 arasındaki sayıları azalan şekilde yazdırın.

x = 100
while x > 0:
    print(x)
    x -= 1

# 4-) Kullanıcıdan alacağınız 5 sayıyı sıralı bir şekilde ekrana yazdırın.

numbers = []

i = 0

while i < 5:
    number = int(input("Bir sayı girin: "))
    numbers.append(number)
    i += 1
numbers.sort()
print(numbers)


# 5-) Kullanıcıdan alacağınız sınırsız ürün bilgisini ürünler listesi içinde saklayınız.
#     Ürün sayısını kullanıcıya sorun.
#     Dictionary listesi yapısı (name, price) şeklinde olsun.
#     Ürün ekleme işlemi bittiğinde ürünleri ekrana while ile yazdırın.

products = []

piece = int(input("Kaç tane ürün eklemek istiyorsunuz: "))
i = 0
while i < piece:
    name = input("Ürün adı: ")  
    price = int(input("Ürün fiyatı: "))
    products.append({
        "name": name,
        "price": price
    })
    i += 1
for product in products:
    print(f"Ürün Adı: {product['name']} Ürün fiyatı: {product['price']}")
