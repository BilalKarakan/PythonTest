# 1-) "Bmw", "Mercedes", "Opel", "Mazda", elemanlarına sahip bir liste oluşturunuz.
carsList = ["Bmw", "Mercedes", "Opel", "Mazda"]
"""
carsList = ["Bmw", "Mercedes", "Opel", "Mazda"]
print(carsList)
"""
# 2-) Liste kaç elemanlıdır.
"""
print(len(carsList))
"""
# 3-) Listenin ilk ve son elemanı nedir?
"""
print(carsList[0])
print(carsList[3])
"""
# 4-) Mazda değerini Toyota ile değiştirin.
"""
carsList[-1] = "Toyota"
print(carsList)
"""
# 5-) Mercedes listenin bir elemanı mıdır?
"""
isThere = "Mercedes" in carsList
print(isThere)
"""
# 6-) Listenin -2 indexindeki değer nedir?
"""
print(carsList[-2])
"""
# 7-) Listenin ilk 3 elemanını alın.
"""
print(carsList[:3])
"""
# 8-) Listenin son iki elmanı yerine "Toyota" ve "Renault" değerlerini ekleyin.
"""
carsList[:-2] = ["Toyota", "Renault"] 
print(carsList)
"""
# 9-) Listenin üzerine "Audi" ve "Nissan" değerlerini ekleyin.
"""
newList = ["Audi", "Nissan"]
carsList = carsList + newList
print(carsList)
"""
# 10-) Listenin son elemanını silin.
"""
del carsList[-1]
print(carsList)
"""
# 11-) Liste elemanlarını tersten yazın.
"""
print(carsList[::-1])
"""
# 12-) Aşağıdaki verileri bir liste içinde saklayınız.

#  studentA: Yiğit Bilgi 2010, (70,60,70)
#  studentB: Sena Turan 2009, (80,80,70)
#  studentC: Ahmet Turan 2008, (80,70,90)

studentA = ["Yiğit", "Bilgi", 2010, [70,60,70]]
studentB = ["Sena", "Turan", 2009, [80,80,70]]
studentC = ["Ahmet", "Turan", 2008, [80,70,90]]


# 13-) Liste elemanlarını ekrana yazdırın.

print(studentA[0])
print(studentB[1])
print(studentC[3])

print(f"{studentA[0]} {studentA[1]} is {2021-studentA[2]} years old and his grade average {(studentA[3][0]+studentA[3][1]+studentA[3][2])/3}")