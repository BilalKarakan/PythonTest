# Yöntem 1

# import math
#import math as islem

# value = dir(math)
# value = help(math)
# value = help(math.cosh)
# value = math.sqrt(49)
# value = math.factorial(6)
# value = math.floor(5.9)
# value = math.ceil(5.9)

# value = islem.factorial(5)

# Yöntem 2

# from math import * #(İlgili modüldeki bütün fonksiyonları import eder.)

# value = factorial(5)
# value = sqrt(16)

#from math import factorial, sqrt, ceil #(Sadece ilgili fonksiyonları import eder.)

# value = factorial(5)
# value = sqrt(25)
# value = ceil(6.2)

# def sqrt(x):
#     print("x: " + str(x))

# from math import factorial,sqrt,ceil
 #==> 3.0
 # def sqrt(x):
#     print("x: " + str(x))

# from math import factorial,sqrt,ceil
# ==> x: 9
# (En son tanımlanan çalışır.)

value = sqrt(9)
print(value)