# 1-) Girilen bir sayının 0-100 arasında olup olmadığını kontrol ediniz.

number = int(input("Bir Sayı Girin: "))
if (0 < number < 100):
    print(f"{number}, 0-100 arasında bir sayıdır.")
else:
    print(f"{number}, 0-100 arasında bir sayı değildir.")

# 2-) Girilen bir sayının pozitif çift tamsayı olup olmadığını kontrol ediniz.

number = int(input("Bir Sayı Girin: "))
if (number > 0):
    if (number % 2 == 0):
        print(f"{number}, pozitif çift tamsayıdır.")
    else:
        print(f"{number}, pozitif ancak çift değildir.")
else:
    print(f"{number}, pozitif bir sayı değildir.")

# 3-) Email ve parola bilgileri ile giriş kontrolü yapınız.

email = input("Email adresinizi girin: ")
password = input("Parolanızı girin: ")

if (email == "email@bilalkarakan.com"):
    if (password == "abc123"):
        print("Giriş Başarılı")
    else:
        print("Parola yanlış")
else:
    print("Email adresiniz yanlış")

# 4-) Girilen üç sayıyı büyüklük olarak karşılaştırınız.

number1 = int(input("Bir Sayı Giriniz: "))
number2 = int(input("Bir Sayı Giriniz: "))
number3 = int(input("Bir Sayı Giriniz: "))
enBuyuk = number1
if (enBuyuk < number2):
    enBuyuk = number2
if (enBuyuk < number3):
    enBuyuk = number3
print(f"En büyük sayı {enBuyuk}'dır.")

# 5-) Kullanıcıdan iki vize sınavı (%60) ve bir final sınavı (%40) notunu alıp ortalama hesaplayınız.
#     Eğer ortalama 50 ve üzerindeyse "Geçti" değilse "Kaldı" yazdırın.
#     a-) Ortalama 50 olsa bile final notu en az 50 olmalı.
#     b-) Finalden 70 alındığında ortalamanın bir önemi olmasın.

vize1 = float(input("1.Vize Sınavı: "))
vize2 = float(input("2.Vize Sınavı: "))
final = float(input("Final Sınavı: "))
ortalama = (((vize1 + vize2)/2)*0.6) + (final * 0.4)
print("Ortalamanız: ", ortalama)
if (final >= 50):
    if (final >= 70):
        print("Final notunuz 70 den yüksek olduğu için geçtiniz.")
    else:
        if (ortalama >= 50):
            print("Ortalama notunuz 50 den yüksek olduğu için geçtiniz.")
        else:
            print("Ortalama notunuz 50 den düşük olduğu için kaldınız.")
else:
    print("Final notunuz 50 den düşük olduğu için kaldınız.")

    
# 6-) Kişinin ad, yaş ve kilo bilgilerini alıp kilo indekslerini hesaplayınız.
#     Formül: (Kilo / Boy uzunluğunun karesi)
#     Aşağıdaki tabloya göre kişi hangi gruba girmektedir.
#     0-18.4 => Zayıf
#     18.5-24.9 => Normal
#     25.0-29.9 => Fazla Kilolu
#     30.0-34.9 => Şişman(Obez)

ad = input("Adınız: ")
boy = float(input("Boyunuz: "))
kilo = float(input("Kilonuz: "))
kiloIndeksi = kilo / ((boy)**2)
if (0 <= kiloIndeksi <= 18.4):
    print(f"Kilo indeksiniz : {kiloIndeksi} ==> Zayıf")
elif (18.5 <= kiloIndeksi <= 24.9):
    print(f"Kilo indeksiniz : {kiloIndeksi} ==> Normal")
elif (25.0 <= kiloIndeksi <= 29.9):
    print(f"Kilo indeksiniz : {kiloIndeksi} ==> Fazla Kilolu")
elif (30.0 <= kiloIndeksi <= 34.9):
    print(f"Kilo indeksiniz : {kiloIndeksi} ==> Şişman(Obez)")
else:
    print("Girilen bilgiler değerlendirme dışında.")
