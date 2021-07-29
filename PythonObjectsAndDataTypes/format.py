name = "Bilal"
# print("My name is {}".format(name))
surname = "Karakan"
# print("My name is {} {}".format(name,surname))
# print("My name is {0} {1}".format(name,surname))      Aynı sonucu verir.Ancak index numaralarını değiştirirsek durum değişir.
# print("My name is {1} {0}".format(name,surname))
# print("My name is {s} {n}".format(n=name,s=surname))
# print("My name is {} {} and I'm {} years old.".format(name,surname,"22"))
age = 22
# print("My name is {} {} and I'm {} years old.".format(name,surname,age))

# result = 200/700
# print("the result is {r:1.4}".format(r=result))       # 1=1 boşluk bırakır, 4=virgülden sonra 4 basamak gider
print(f"My name is {name} {surname} and I'm {age} years old.")        #önüne f koyduğunda süslü parantezlerin içine direkt değişken isimleri yazılabilir.