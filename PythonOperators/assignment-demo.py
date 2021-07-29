x, y, z = 2, 5, 10
numbers = 1, 5, 7, 10, 6

# 1-) Kullanıcıdan aldığınız 2 sayının çarpımı ile x, y, z toplamının farkı nedir?
"""
value1 = input("Enter a number: ")
value2 = input("Enter a number: ")
value1 = int(value1)
value2 = int(value2)
print((value1*value2) - (x+y+z))
"""
# 2-) y'nin x'e kalansız bölümünü hesaplayınız.
"""
result = y//x
print(result)
"""
# 3-) (x, y,z) toplamının mod 3'ü nedir ? 
"""
result = ((x+y+z) % 3)
print(result)
"""
# 4-) y'nin x. kuvveti nedir?
"""
y = y**x
print(y)
"""
# 5-) (x, *y, z) = numbers işlemine göre z'nin küpü kaçtır?
"""
x, *y, z = numbers
print(z**3)
"""
# 6-) (x, *y, z) = numbers işlemine göre y'nin değerleri toplamı kaçtır?
x, *y, z = numbers
result = y[0]+ y[1]+ y[2]
print(result) 