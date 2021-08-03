x = 1
"""
while x <= 100:
    print(x)
    x += 1
print("Bitti...")
"""
"""
while x <= 100:
    if (x % 2 == 0):
        print(f"Sayı Çift: {x}")
    else:
        print(f"Sayı Tek: {x}")
    x += 1
"""
"""
name = "" # False
while not name:
    name = input("Adınız: ")
print(f"Merhaba, {name}")
"""

name = "" #False
while not name.strip():
    name = input("Adınız: ")
print(f"Merhaba, {name}")