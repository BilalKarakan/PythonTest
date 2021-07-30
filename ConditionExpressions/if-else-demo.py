# 1-) Kullanıcıdan isim, yaş ve eğitim bilgilerini isteyip ehliyet alabilme durumunu kontrol ediniz.
#     Ehliyet alma koşulu en az 18 yaş ve eğitim durumu lise ya da üniversite olmalıdır.

ad = input("Adınız: ")
yas = int(input("Yaşınız: "))
egitimDurumu = input("Eğitim Durumunuz: ")

if (yas >= 18):
    if ((egitimDurumu == "Üniversite") or (egitimDurumu == "Lise")):
        print("Ehliyet alabilirsiniz.")
    else:
        print("Ehliyrt alamazsınız. Eğitim durumunuz uygun değil.")
else:
    (print("Ehliyet alamazsınız. Yaşınız uygun değil."))


# 2-) Bir öğrencinin iki yazılı ve bir sözlü notunu alıp hesaplanan ortalamaya göre not
#     ağırlığına karşılık gelen not bilgisini yazdırınız.
# 0-24 => 0
# 25-44 => 1
# 45-54 => 2
# 55-69 => 3
# 70-84 => 4
# 85-100 => 5

birinciYazılı = float(input("1.Yazılı Sınavınız: "))
ikinciYazılı = float(input("2. Yazılı Sınavınız: "))
sozlu = float(input("Sözlü Notunuz: "))

ortalama = (birinciYazılı + ikinciYazılı + sozlu)/3

if (0 <= ortalama <= 24):
    print("Notunuz: 0")
elif (25 <= ortalama <= 44):
    print("Notunuz: 1")
elif (45 <= ortalama <= 54):
    print("Notunuz: 2")
elif (55 <= ortalama <= 69):
    print("Notunuz: 3")
elif (70 <= ortalama <= 84):
    print("Notunuz: 4")
elif (85 <= ortalama <= 100):
    print("Notunuz: 5")
else:
    print("Yanlış değer girdiniz.")

# 3-) Trafiğe çıkış tarihi alınan bir aracın servis zamanını aşağıdaki bilgilere göre hesaplayınız.
# 1.Bakım => 1.Yıl
# 2.Bakım => 2.Yıl
# 3.Bakım => 3.Yıl
# ** Süre hesabını alınan gün, ay, yıl bilgisine göre gün bazlı hesaplayınız.

import datetime
tarih = (input("Aracınızın trafiğe çıkış tarihi (2021/07/30): "))
tarih = tarih.split("/")
trafigeCıkıs = datetime.datetime(int(tarih[0]), int(tarih[1]), int(tarih[2]))
simdi = datetime.datetime.now()
fark = simdi - trafigeCıkıs
days = fark.days
print(days)

if (days <= 365):
    print("1. servis bakım aralığı")
elif(365 < days <= 365*2):
    print("2. servis bakım aralığı")
elif (365*2 < days < 365*3):
    print("3. servis bakım aralığı")
else:
    print("Hatalı bilgi girdiniz.")
