if 3==3:
    print("Hello World")

if True:
    print("Hello World")

if False:
    print("Hello World")

isLoggedin = True
if isLoggedin:
    print("Hello World")

username = "bilalkarakan"
password = 1234

# isLoggedin = (username == "bilalkarakan") and (password == 1234)

if (username == "bilalkarakan") and (password == 1234):
    print("Hello World")


if (username == "bilalkarakan") and (password == 12345):
    print("Hello World")
else:
    print("Kullanıcı Adı ya da parola yanlış")

username = input("Kullanıcı adınızı girin: ")
password = input("Şifrenizi girin: ")
if (username == "bilalkarakan"):
    if (password == "1234"):
        print("Hello World")
    else:
        print("Parola yanlış")
else:
    print("Kullanıcı Adı yanlış")