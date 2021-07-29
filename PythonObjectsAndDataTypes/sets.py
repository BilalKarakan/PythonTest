fruits = { 'Orange', 'Apple', 'Banana' }
# print(fruits[0])               indekslenemez ve sıralanamaz(a-z ye veya z-a ya gibi) bir listedir.
"""
for x in fruits:           # elemanlarına böyle ulaşabiliriz.
    print(x)    
"""

"""
fruits.add("Cherry")        # add ile yeni bir eleman ekleyebiliriz.
print(fruits)
"""

"""
fruits.update(["Mango", "Graphe"])    # update ile bir den fazla eleman ekleyebilriz.
print(fruits)
"""

"""
fruits.update(["Mango", "Graphe", "Apple"])     # Sets de bir elemandan yalnızca bir tane bulunur. 
print(fruits)
"""

"""
myList = [1,2,2,4,5,4,3]
print(myList)
print(set(myList))             # Set constructor çalıştırılırsa aynı elemanlar yazılmaz.
"""

# fruits.remove("Apple")        # İlgili elemanı setden siler.
# fruits.discard("Banana")      # İlgili elemanı setden siler.
#fruits.pop()                   # Dizide en son elemanı silerdi. Set sıralanmadığı için burda rastgele bir eleman siler.
fruits.clear()                  # Bütün elemanlar silinir.
print(fruits)