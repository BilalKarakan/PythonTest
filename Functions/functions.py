
def sayHello():
    print("Hello There")
sayHello()
#----------------------------

def sayHello(name = "User"):
    print("Hello "+ name)
sayHello("Ali")
sayHello("Ayşe")
sayHello()
#---------------------------

def sayHello(name = "User"):
    return "Hello "+ name

message = sayHello("Ali")
print(message)
#---------------------------

def total(num1, num2):
    return num1 + num2
result = total(20, 30)
print(result)
#-----------------------------
def yasHesapla(dogumYili):
    return 2021 - dogumYili
ageAli = yasHesapla(2004)
ageAyse = yasHesapla(1993)
ageAhmet = yasHesapla(1981)
print(ageAli, ageAyse, ageAhmet)

def emekliligeKacYilKaldi(dogumYili, isim):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi.
    INPUT: Dogum yili
    OUTPUT: Hesaplanan yil bilgisi
    """
    yas = yasHesapla(dogumYili)
    emeklilik = 65 - yas

    if emeklilik > 0:
        print(f"Emekliliğinize {emeklilik} yıl kaldı.")
    else:
        print("Zaten emekli oldunuz.")
emekliligeKacYilKaldi(1983, "Ali")
emekliligeKacYilKaldi(1952, "Ayşe")
emekliligeKacYilKaldi(1978, "Ahmet")

print(help(emekliligeKacYilKaldi))

#--------------------------------------------
list = [1, 2, 3]
print(help(list.append))