# 1-) Girilen iki sayıdan hangisi büyüktür?
"""
number1 = int(input("Enter a number: "))
number2 = int(input("Enter a number: "))
result = (number1 < number2)
print(f"number1: {number1} number2: {number2}'den küçüktür: {result}")
"""
# 2-) Kullanıcıdan vize (%40) ve final (%60) notunu alıp ortalama hesaplayın.
# Eğer ortalama 50 ve üstündeyse "Geçti" değilse "Kaldı" yazdırın.
"""
vize1 = float(input("Sınav notunuzu girin: "))
final = float(input("Sınav notunuzu girin: "))
ortalama = (vize1*0.4) + (final*0.6)

print(f"Birinci Vize: {vize1} Final: {final} Ortalama: {ortalama} ==> {ortalama>=50}")
"""

# 3-) Girilen bir sayının tek mi çift mi olduğunu yazdırın.
"""
number = int(input("Bir sayı girin: "))
result = ((number%2) == 1)
print(f"{number} tek bir sayıdır: {result}")
"""
# 4-) Girilen sayının negatif-pozitif olma durumunu yazdırın.
"""
number = int(input("Sayı: "))
result = (number<0)
print(f"Sayının negatif olma durumu: {result}")
"""

# 5-) Parola ve email bilgisini isteyip doğruluğunu kontrol ediniz.
# email: email@bilalkarakan.com  password: abc123
"""
email = input("Mail adresinizi girin: ")
password = input("Şifrenizi girin: ")
result = (email=="email@bilalkarakan.com") and (password =="abc123")
print(f"Email: {email}  Password: {password} ==> {result}")
"""