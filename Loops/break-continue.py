
name = "Bilal Karakan"

for letter in name:
    if letter == "K":
        break
    print(letter)
#-----------------------------------
for letter in name:
    if letter == "l":
        continue
    print(letter)
#-----------------------------------
x = 0

while x < 5:
    if x == 3:
        break
    print(x)
    x += 1 
#-----------------------------------
while x < 5:
    x += 1
    if x == 3:
        continue
    print(x)
#----------------------------------
# 1-100 e kadar sayıların toplamı ?

x = 1
total = 0

while x <= 100:
    total = total + x
    x += 1
print(total)
#--------------------------------
x = 0
result = 0
while x <= 100:
    x += 1
    if x % 2 == 0:
        continue
    result += x
print(f"Toplam: {result}")