"""
1-100 arasında rastgele üretilecek bir sayıyı aşağı yukarı ifadeleri ile buldurmaya çalışın.
** 100 üzerinden puanlama yapın. Her soru 20 puan.
** Hak bilgisini kullanıcıdan alın ve her soru belirtilen can sayısı üzerinden hesaplansın.
"""

import random

randomNumber = random.randint(1,100)
can = int(input("Kaç hak kullanmak istersiniz: "))
hak = can
sayac = 0
while hak > 0:
    hak -= 1
    sayac +=1
    number = int(input("Bir sayı girin: "))
    if number == randomNumber:
        print(f"Tebrikler {sayac}. hakkınızda doğru tahmin ettiniz. Toplam puanınız: {100 - (can*(sayac-1))}")
        break
    elif number < randomNumber:
        print("YUKARI")
    else:
        print("AŞAĞI")
    if hak == 0:
        print(f"Hakkınız bitti. Tutulan sayı: {randomNumber}")