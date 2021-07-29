# key - value
"""
sehirler = ["Kocaeli", "İstanbul", "İzmir"]
plakalar = [42, 34, 35]

print(plakalar[sehirler.index("İstanbul")])
"""
# Bu kullanımda dizideki elemanların sırası önemlidir o yüzden tercih etmeyiz.

# { key : value}

plakalar = {"Kocaeli" : 41, "İstanbul" : 34, "İzmir" : 35}

print(plakalar["Kocaeli"])
print(plakalar["İstanbul"])

plakalar["Bursa"] = 16                # Yeni bir eleman ekleyebiliriz.
plakalar["Kocaeli"] = "new value"     # Yeni değer atayabiliriz.

print(plakalar)


usersName = {
    "bilalkarakan" : {
        "age" : 22,
        "roles" : ["admin", "user"],
        "email" : "bilal@gmail.com",
        "address" : "İzmir",
        "phone" : "123456789"
    },
    "x1x2x3x4x5" : {
        "age" : 25,
        "email" : "x1x2x3x4x5@gmail.com",
        "address" : "İstanbul",
        "phone" : "987654321"
    }
}

print(usersName["bilalkarakan"])          # Böyle dallanmalar yaparak kullanıcı hakkında bütün bilgileri görüntüleyebiliriz.
print(usersName["bilalkarakan"]["age"])   # Daha alta inerek istediğimiz bilgiyi yazdırabiliriz.
print(usersName["bilalkarakan"]["roles"])  # Dizi tanımlayabiliriz.
print(usersName["bilalkarakan"]["roles"][0])   # Dizinin istediğimiz indexini yazdırabiliriz.