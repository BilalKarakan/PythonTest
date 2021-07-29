website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1-) " Hello World " ifadesinin baş ve sonundaki boşluk karakterlerini siliniz.
"""
result = " Hello World ".strip()
result = " Hello World ".lstrip()      # sadece soldaki boşluk karakterini siler.
result = " Hello World ".rstrip()      # sadece sağdaki boşluk karakterini 
result = website.lstrip("/:pth")       # soldan parantez içine girilen karakterleri siler.bir karakteri bir kere yazmak yeterlidir.

print(result)
"""
# 2-) "www.sadikturan.com" içinedeki sadikturan bilgisi dışında bütün karakterleri siliniz.
"""
result = "www.sadikturan.com".strip("w.moc")
print(result)
"""
# 3-) "course" karakter dizisinin tüm karaakterlerini küçük harf yapın.
"""
result =course.lower()
print(result)
"""
# 4-) "website" içinde kaç tane a karakteri vardır. (count("a"))
"""
result = website.count("a")
result = website.count("www")                # çoklu arama yapabiliriz.
result = website.count("www",0,10)           #index nmaralarıyla aralık belirtebiliriz.
print(result)
"""
# 5-) "website" 'www' ile başlayıp 'com' ile bitiyor mu
"""
result = website.startswith("www")
result = website.startswith("http")
result = website.endswith("com")
print(result)
"""
# 6-) "website" içinde ".com" ifadesi var mı
"""
result = website.find(".com")
result = website.find(".com", 0, 10)         # aralık seçebiliriz.
result = course.find("Python")
result = course.rfind("Python")            #sağdan bulmaya çalışır ve index numarasını verir.
result = course.index("Python")             #index numarasını verir.
result = course.rindex("Python")            #sağdan başlar saymaya
result = course.index("comm")              # ifadede olmayan bir karakter veya karakter dizisi aradığımızda hata verir.
print(result)
"""
# 7-) "course" içindeki karakterlerin hepsi alfabetik mi (isalpha, isdigit)
"""
result = course.isalpha()
result = "Hello".isalpha()             #alfabetik
result = course.isdigit()              
result = "75453".isdigit()             #ifadenin içindekiler sayı mı 
print(result)
"""
# 8-) "Contents" ifadesini satırda 50 karakter içerisine ekleyin, sağına ve soluna * ekleyin.
"""
result = "Contents".center(50 , "-")
result = "Contents".rjust(50,"-")      #Contents ifadesini sağa yatırır
result = "Contents".ljust(50,"-")
print(result)
"""
# 9-) "course" karakter dizisindeki tüm boşluk karakterlerini "--" ile değiştirin.
"""
result = course.replace(" ","-")
result = course.replace(" ","-",5)        #ilk 5 karakteri değiştirir
result = course.replace(" ", "")          #tüm boşluk karakterlerini silebilirsiniz.
print(result)
"""
# 10-) "Hello World" karakter dizisinin "World" ifadesini "There ile değiştirin"
"""
result = "Hello World".replace("World", "There")
print(result)
"""
# 11-) "course" karakter dizisini boşluk karakterlerinden ayırın
"""
result = course.split(" ")

# print(result[2])
print(result[5])
"""