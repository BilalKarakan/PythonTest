message = "Hello There. My name is Bilal Karakan"

# message = message.upper()       Her harfi büyük harf yapar.
# message = message.lower()       Her harfi küçük harf yapar.
# message = message.title()       Her kelimenin baş harfini büyük yapar.
# message = message.capitalize()    Sadece ilk harfi büyük yapar.

# message = message.strip()         Baş ve sondaki boşluk karakterlerini yoksayar.
# message = message.split()          Her bir kelime boşluk karakterlerinden ayrılır ve ayrı bir dizinin elemanı olur.
# message = message.split(".")        Nokta karakterinden itibaren ayırır.
# print(message[0])                   Bir diziye dönüştüğü için 0. index Hello there olur.

# message = message.split()
# message = " ".join(message)          #Ayrılmış ifadeyi araya boşluk koyarak tekrar birleştirir.
# message = ".".join(message)            #Ayrılmış ifadeyi araya nokta koyarak tekrar birleştirir.

# index = message.find("Bilal")          Mevcut string ifadede Bilal kelimesinin olup olmadığını sorgular, başlangıcın index numarasını verir.
# index = message.find("Sadık")            -1 döndürür. Çünkü mevcut ifadede böyle bir karakter dizisi yok.
# print(index)

# isFound = message.startswith("H")       message karakter dizisinin H ile başlayıp başlamadığını  sorgular ve false ve true diye cevap döndürür.
# print(isFound)
 
# isFound = message.endswith("n")           message karakter dizisinin n ile bitip bitmediğini sorgular. True ve false diye cevap dönüdürür.
# print(isFound)

# message = message.replace("Bilal", "Sadık")     message karakter dizisinde Bilal yerine Sadık yazar.
# message = message.replace(" ", "*")
# message = message.replace("ç", "c").replace("ö", "o")     # url gibi yapılarda Türkçe karakterleri gidermek için kullanılabilir.

# message = message.replace("ç", "c")
                #  .replace("ö", "o")      Böylede kullanılabilir.

# message = message.center(50)               message karakter dizisini tam ortaya alacak şekilde 50 karaktere tamamlar. Bir parametre girilmezse boşluk karakterleri ile tamamlar.
# message = message.center(50, "*")          boşlukları * karakterleri ile doldurur.
print(message)

