numbers = [1, 3, 5, 7, 9, 12, 19, 21]

# 1-) numbers listesindeki hangi sayılar 3 ün katıdır.

for i in numbers:
    if (i % 3 == 0):
        print(i)        

# 2-) numbers listesindeki sayıların toplamı kaçtır.

total = 0
for i in numbers:
    total += i
print("Total: ",total)

# 3-) numbers listesindelki tek sayıların karesini alınız.

for i in numbers:
    if (i % 2 == 1):
        print(i**2)

cities = ["Bursa", "İstanbul", "Ankara", "İzmir", "Rize"]

# cities listesindeki şehirlerin hangileri en fazla 5 karakterlidir.

for i in cities:
    if (len(i) <= 5):
        print(i)

products = [
    {"name": "Samsung S6", "price": 3000},
    {"name": "Samsung S7", "price": 4000},
    {"name": "Samsung S8", "price": 5000},
    {"name": "Samsung S9", "price": 6000},
    {"name": "Samsung S10", "price": 7000}

]
# 5-) Ürünlerin fiyatları toplamı nedir?

totalPrice = 0
for product in products:
    price = int(product["price"])
    totalPrice += price
print(totalPrice)

# 6-) Ürünlerden fiyatı en fazla 5000 olan ürünleri gösteriniz.
for product in products:
    if (int(product["price"]) <= 5000):
        print(product["name"])