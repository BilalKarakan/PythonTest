# Error Handling => Hata Yönetimi

"""
x = int(input("x: "))
y = int(input("y: "))

print(x/y)
"""

"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except ZeroDivisionError:
    print("y = 0 olamaz.")
except ValueError:
    print("x ve y için sayısal değer girmelisiniz.")
"""

"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except (ZeroDivisionError,ValueError) as error: # Hata kaynağı kullanıcıya bildirilir.
    print("Hatalı değer girdiniz.")
    print(error)
"""

"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except:
    print("Hatalı değer girdiniz.") # Bu kullanımda hata kaynağına ulaşamayız.
"""

"""
try:
    x = int(input("x: "))
    y = int(input("y: "))
    print(x/y)
except:
    print("Hatalı değer girdiniz.")
else:
    print("Her şey yolunda")
"""

while True:
    try:
        x = int(input("x: "))
        y = int(input("y: "))
        print(x/y)
    except Exception as ex:
        print("Hatalı değer girdiniz:",ex)
    else:    # except bloğu çalışmazsa else çalışır.
        break
    finally:  # Her zaman çalışır.
        print("try-except sonlandı.")