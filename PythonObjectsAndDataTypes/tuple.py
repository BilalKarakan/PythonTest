# list1 = [1, 2, 3]
# list2 = (1, "iki", 3)             # Tuple liste örneği, parantez kullanmasak da olur.

# print(type(list1))
# print(type(list2))

# print(list1[2])
# print(list2[2])

# print(len(list1))
# print(len(list2))

list1 = ["Ali", "Mehmet"]
list2 = ("Damla", "Ayşe")

# list1[0] = "Ahmet"
# list2[1] = "Özge"                 # Tuple listelerde normal listeden farklı olarak değer ataması değiştirilemez.
# Tuple listelere yeni bir liste ekleyebiliriz.
list3 = ("Demet", "Emel", "Sude")
newList = list2 + list3
print(newList)
print(list1, list2)

print(list2.index("Damla"))               # index numarasını verir tuple listelerde.
print(list3.count("Emel"))                # Kaç tane olduğunu söyler.
# Tuple listelerde eleman ekleme, eleman silme, yeni eleman ataması vs. yapamıyoruz.