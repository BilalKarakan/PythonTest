numbers = [1, 10, 5, 16, 4, 9, 10]
letters = ["a", "g", "s", "b", "y", "a", "s"]

val = min(numbers)          # en küçük sayıyı yazdırır.
val = max(numbers)          # en büyük sayıyı yazdırır.
val = min(letters)          # alfabetik sıraya göre en küçük harfi yazdırır.
val = max(letters)          # alfabetik sıraya göre en büyük harfi yazdırır
 
val = numbers[3:6]          # 3. elemandan başlar sona kadar gider.
val = numbers[:3]           # Baştan başlar 3. elemana kadar gider.
val = numbers[2:]           # 2. elemandan başlar sona kadar gider.

numbers[4] = 55             # istediğimiz elemanı değiştirebiliriz.

numbers.append(20)          # append methodu ile istediğimiz sayıyı diziye ekleyebiliriz.

numbers.insert(3, 28)       # 3. indexden bir önceki elemana bu elemanı ekler.
numbers.insert(-1, 166)

numbers.pop()               # en son elemanı siler.
numbers.pop(0)             # 0.indexdeki elemanı siler. Hangi index numarası verilirse onu siler.

numbers.remove(5)          # girilen elemanı bulur ve siler.

numbers.sort()             # sayısal değer olarak küçükten büyüğe doğru sıralar.
letters.sort()             # alfabetik olarak ilk harften son harfe doğru sıralar.

numbers.reverse()          # Diziyi tersine çevirir. Büyükten küçüğe doğru sıralar.
letters.reverse()          # Diziyi tersine çevirir. Z den A ya doğru sıralar.

print(len(numbers))       # eleman sayısını verir.

print(numbers.count(10))  # Girilen elemandan dizide kaç tane olduğunu yazdırır.

print(numbers.clear())    # Bütün elemanları siler.

print(numbers)
print(val)