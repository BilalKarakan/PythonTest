# x = 5
# y = 10
# z = 20

#OR

# x, y, z = 5, 16, 20
# print(x, y, z)

#x, y = y, x       # Atamaları değiştirebiliriz

#x += 5     # x = x + 5
#x -= 5     # x = x - 5
#x *= 5     # x = x * 5
#x /= 5     # x = x / 5
#x %= 5     # x = x % 5
#y //= 5    # y = y // 5
#y **= z    # y = y ** z

# print(x, y, z)

# values = 1, 2, 3             # Tuple
#values = 1, 2                  # Hata verir. z'ye değer ataması yapılamadı.
values = 1, 2, 3, 4, 5        # Fazla değer var. Hata verir.
# print(values)
# print(type(values))


x , y, *z = values             # z ye dizi ataması yapılır.

print(x, y, z[0])              # Ancak z nin elemanlarına ulaşılabilir.
