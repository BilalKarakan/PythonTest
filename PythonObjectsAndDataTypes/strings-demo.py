
website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sona Python Programlama Rehberiniz (40 saat)"

# 1- 'course' karakter dizisinde kaç karakter bulunmaktadır.
"""
print(len(course))
"""
"""
length = len(course)
print(length)
"""

# 2- 'website' içinden www karakterlerini alın
"""
print(website[7:10])
"""
# 3- 'website' içinden com karakterlerini alın 
"""
result = website[22:25]
print(result)
"""
"""
length = len(website)
result = website[length-3:length]
print(result)
"""
# 4- 'course' içinden ilk 15 ve son 15 karakterlerini alın 
"""
print(course[:15])
print(course[-15:])
"""
"""
length = len(course)
print(course[length-15:length])
"""
# 5- 'course' içindeki karakterleri tersten yazdırın 
"""
result = course[::-1]
print(result)
"""

name, surname, age, job = "Bora", "Yılmaz", 32, "mühendis"

# 6- Yukarıda verilen değişkenler ile ekrana aşağıdaki ifadeyi yazdırın.
# Benim adım Bora Yılmaz, yaşım 32 ve mesleğim mühendis.
"""
result = "Benim adım"+" "+ name + " " + surname + "," + " " "yaşım"+ " " + str(age) + " ve meseleğim"+" "+ job 
print(result)
"""
"""
result = "Benim adım {} {}, yaşım {} ve mesleğim {}".format(name, surname, age, job)
print(result)
"""
"""
result = f"Benim adım {name} {surname}, yaşım {age} ve mesleğim {job}."
print(result)
"""
# 7- "Hello world" ifadesindeki w harfini "W" ile değiştirin
"""
s = "Hello world"
result = s[0:6] + "W" + s[7:]
print(result)
"""
# 8- "abc" ifadesini yan yana 3 defa yazdırın 
print("abc"*3)