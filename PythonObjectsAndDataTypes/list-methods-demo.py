names = ["Ali", "Yağmur", "Hakan", "Deniz"]
years = [1999, 2000, 1999, 1992]

# "Cenk" ismini listenin sonuna ekleyin.
"""
names.append("Cenk")
print(names)
names.insert(-1,"Cenk")
print(names)
names.insert(len(names), "Mehmet)
print(names)
"""
# "Sena" değerini listenin başına ekleyin.
"""
names.insert(0,"Sena")
print(names)
"""
# "Deniz" ismini listeden silin.
"""
names.pop(-1)
print(names)
names.remove("Deniz")
print(names)
"""
# "Deniz" isminin indexi nedir?
"""
index = names.index("Deniz")
print(index)
names.pop(index)
print(names)              # Özel durum
"""
# "Ali" listenin bir elemanı mıdır?
"""
result = "Ali" in names
print(names)
var = names.index("Ali")        # Yoksa -1 döndürür, varsa index numarasını verir.
print(names.count("Ali"))
"""
# Liste elemanlarını ters çevirin.
"""
names.reverse()
print(names)
"""
# Liste elemanlarını alfabetik olarak sıralayın.
"""
names.sort()
print(names)
"""
# years listesini rakamsal büyüklüklerine söre sıralayın.
"""
years.sort()
print(years)
"""
# str = "Chevrolet, Dacia" karakater dizisini listeye çevirin.
"""
str = "Chevrolet, Dacia"
result = str.split(",")
print(result)
"""
# years dizisinin en büyük ve en küçük elemanı nedir?
"""
print(min(years))
print(max(years))
"""
# years dizisinde kaç tane 1999 değeri vardır?
"""
print(years.count(1999))
"""
# years dizisinin tüm elemanlarını silin.
"""
years.clear()
print(years)
"""
# Kullanıcıdan alacağınız 3 tane marka bilgisini bir listede saklayınız.
"""
brand1 = input("Enter a brand name: ")
brand2 = input("Enter a brand name: ")
brand3 = input("Enter a brand name: ")

allBrand = [brand1, brand2, brand3]
print(allBrand)

OR
"""
"""
markalar = []

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

marka = input("Marka: ")
markalar.append(marka)

print(markalar)
"""
