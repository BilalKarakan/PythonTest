x = 6

result = 5 < x < 10

# AND
# True, True => True
# True, False => False
# False, True => False
# False, False => False
result = (5 < x) and (x < 10)      
hak = 0
devam = "e"
result = ((hak > 0) and (devam == "e"))
# OR
# True, True => True
# True, False => True
# False, True => True
# False, False => False

result = (x > 0) or (x % 2 == 0)

# NOT
result = (x > 5)  # True
result2 = not(x >5)  # False

# x, 5-10 arasında bir çift sayı mı ? 
result = ((x > 5) and (x < 10)) and (x % 2 == 0)
print(result)
print(result2)
