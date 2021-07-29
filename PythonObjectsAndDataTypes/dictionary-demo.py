"""
students = {
    "120" : {
        "Name" : "Dorothea",
        "Surname" : "Brooke",
        "Phone" : "532 000 00 01"
    },
    "125" : {
        "Name" : "Edward",
        "Surname" : "Casaubon",
        "Phone" : "532 000 00 02"
    },
    "128" : {
        "Name" : "Will",
        "Surname" : "Ladislaw",
        "Phone" : "532 000 00 03",
    }
}
"""
# 1-) Bilgileri verilen öğrencileri kullanıcıdan aldığınız bilgilerle dictionary içinde saklayınız.

students = {}

number = input("Enter a student number: ")
name = input("Enter a student name: ")
surname = input("Enter a student surname: ")
phone = input("Enter a student phone number: ")

# students[number] = {
#     "name" : name,
#     "surname" : surname,
#     "phone" : phone,
# }

#OR

students.update({
    number : {
        "name" : name,
        "surname" : surname,
        "phone" : phone
    }
})    

print(students)

# 2-) Öğrenci numaraasını kullanıcıdan alıp ilgili öğrenci bilgisini gösterin.

# stdNo = input("Student No: ")
# student = students[stdNo]
# print(student)

print("*"*50)
stdNo = input("Student No: ")
student = students[stdNo]

print(f"Aradığınız {stdNo} nolu öğrencinin adı: {student[name]} soyadı: {student[surname]} ve telefonu ise {student[phone]}")
