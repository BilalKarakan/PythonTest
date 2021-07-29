"""
Daire Alanı = pi*r^2
Daire Çevresi = 2*pi*r

Yarıçapı verilen bir dairenin alnını ve çevresini hesaplayınız.
"""
pi = 3.14
yariCap = input("Yarı Çap: ")
r = float(yariCap)
alan = pi * r**2
# print("Alan: ", alan)
cevre = 2*pi*r
# print("Çevre: ", cevre)
print("Alan: "+ str(alan) +" "+ "Çevre: "+ str(cevre))
