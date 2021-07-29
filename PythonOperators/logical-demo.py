# 1-) Girilen sayının 0-100 arasında olup olmadığını kontrol ediniz.
"""
x = int(input("Enter a number: "))
result = (x > 0) and (x < 100)
print(f"{x}, 0 ve 100 arasında mı: ",result)
"""
# 2-) Girilen sayının pozitif çift sayı olup olmadığını kontrol ediniz.
"""
number = int(input("Enter a number: "))
result = (number > 0) and (number%2 == 0)
print(f"{number}, pozitif çift tamsayı mı: {result}")
"""
# 3-) Email ve password bilgileri ile giriş kontrolü yapınız.
"""
email = "email@bilalkarakan.com"
password = "123abc"
variable1 = input("Email adresi girin: ")
variable2 = input("Şifrenizi girin: ")
result = (email == variable1) and (password == variable2)
print(f"Giriş başarılı mı: {result}")
"""
# 4-) Girilen üç sayıyı büyüklüklerine göre karşılaştırınız.
"""
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
number3 = int(input("Enter a number: "))

result1 = (number1 > number2) and (number1 > number3)
print(f"En büyük sayı {number1}: {result1}")

result2 = (number2 > number1) and (number2 > number3)
print(f"En büyük sayı {number2}: {result2}")

result3 = (number3 > number1) and (number3 > number2)
print(f"En büyük sayı {number3}: {result3}")
"""
# 5-) Kullanıcıdan bir vize sınavı (%40) ve bir final sınavı (%60) noto alıp ortalama hesaplayınız.
#     Eğer ortalama 50 ve üzerindeyse "geçti" değilse "kaldı" yazdırın. 
#     a-) Ortalama 50 olsa bile final notu en az 50 olmalı.
#     b-) Finalden 70 alındığında vizenin bir önemi olmasın
"""
vize = float(input("Vize sınav notunuz: "))
final = float(input("Final sınav notunuz: "))
ortalama = (vize*0.4) + (final*0.6)
# result = (ortalama >= 50) and (final >=50)
result = (ortalama >= 50) or (final >=70)

print(f"Ders geçme durumu: {result}")
"""
# 6-) Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayınız.
#     Formül: (Kilo / Boy uzunluğu)**2
#     Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#     0-18.4      => Zayıf
#     18.5-24.9   => Normal
#     25.0-29.9   => Fazla Kilolu
#     30.0-34-9   => Şişman (Obez)

isim = input("Adınız: ")
kilo = float(input("Kilonuz: "))
boy = float(input("Boyunuz: "))
kiloIndeks = (kilo)/(boy**2)

result1 = (0 <= kiloIndeks <= 18.4)
result2 = (18.5 < kiloIndeks <= 24.9)
result3 = (25.0 < kiloIndeks <= 29.9)
result4 = (30.0 < kiloIndeks <= 34.9)

print(f"Ad: {isim} Kilo: {kilo} Boy: {boy}Kilo indeksi: {kiloIndeks} ===> Zayıf: {result1}")

print(f"Ad: {isim} Kilo: {kilo} Boy: {boy}Kilo indeksi: {kiloIndeks} ===> Normal: {result2}")

print(f"Ad: {isim} Kilo: {kilo} Boy: {boy}Kilo indeksi: {kiloIndeks} ===> Fazla Kilolu: {result3}")

print(f"Ad: {isim} Kilo: {kilo} Boy: {boy}Kilo indeksi: {kiloIndeks} ===> Şişman (Obez): {result4}")
