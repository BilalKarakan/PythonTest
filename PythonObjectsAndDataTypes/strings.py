name = "Bilal"
surname = "Karakan"
# age = 22    hata alırsın str ile int toplanmaz.
age = "22"
# print("My name is "+ name + " "+ surname + " and I am "+ age + " years old.")
# print("My name is "+ name + " "+ surname + " and I am "+ str(age) + " years old.")
# print("My name is "+ name + " "+ surname + " and\nI am "+ str(age) + " years old.")        #alt satıra almak için \n kullan.
greeting = "My name is "+ name + " "+ surname + " and\nI am "+ str(age) + " years old."
length = len(greeting)
# print(greeting)

#index numarası ile işlem yapılabilir. name değişkeninde 0 B ye -1 l ye karşılık gelir.[] ile index numarası belirtilir.
# print(greeting[-1])
# print(greeting[0])
# print(greeting[2])
# print(greeting[10])
# print(len(greeting))    # len ile bir string ifadenin kaç karakterli olduğunu bulabiliriz.
# print(greeting[length-1])    # son karakteri böyle de bulabiliriz.

# print(greeting[2:5])   # 2. indexden 5. indexe kadar yazdır.
# print(greeting[3:7])
# print(greeting[3:])        3.karakterden başlayıp sonuna kadar gider eğer bit bitiş indexi girmezsek.
# print(greeting[:15])        en baştan başlar, 15. indexe kadar gider.
# print(greeting[2:40:2])        2.indexden başla 40. indexe kadar git ama ikişer ikişer git.