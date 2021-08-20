Hesap1 = {
    'Ad': "Bilal Karakan",
    'HesapNo': 123456789,
    'Bakiye': 2500,
    'EkHesap': 1500,
}

Hesap2 = {
    'Ad': "Bilal Karakan",
    'HesapNo': 123456789,
    'Bakiye': 2500,
    'EkHesap': 1500,
}
def paraCek(hesap, miktar):
    print(f"Merhaba {Hesap1['Ad']}")

    if hesap['Bakiye'] >= miktar:
        hesap['Bakiye'] -= miktar
        print(f"Paranızı alt bölmeden alabilirsiniz.")
        bakiyeSorgula(hesap)
    else:
        total = hesap['Bakiye'] + hesap['EkHesap']
        if total >= miktar:
            ekHesapKullanimi = input("Ek hesap kullanılsın mı? (e/h)")
            if ekHesapKullanimi == "e":
                ekHesapKullanilacakMiktar = miktar - hesap['Bakiye']
                hesap['Bakiye'] = 0
                hesap['EkHesap'] -= ekHesapKullanilacakMiktar 
                print("Paranızı alt bölmeden alabilirsiniz.")
                bakiyeSorgula(hesap)
            else:
                print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} bulunmaktadır.")
        else:
            print("Bakiye yetersiz.")
            bakiyeSorgula(hesap)

def bakiyeSorgula(hesap):
    print(f"{hesap['HesapNo']} nolu hesabınızda {hesap['Bakiye']} TL bulunmaktadır. Ek hesabınızda {hesap['EkHesap']} TL bulunmaktadır.")
paraCek(Hesap1, int(input("Kaç para çekmek istiyorsunuz?  ")))
paraCek(Hesap1, int(input("Kaç para çekmek istiyorsunuz?  ")))
