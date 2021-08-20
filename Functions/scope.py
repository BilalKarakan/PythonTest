"""
# global scope
x = "global x"
def function():
    # local scope
    x = "local x"

function()
print(x)
"""
"""
x = "global x"
def function():
    x = "local x"
    print(x)
function()
print(x)
"""
"""
x = "global x"
def function():
    # x = "local x"
    print(x)
function()
print(x)
"""
"""
# global
name = "Bilal"
def changeName(new_name):
    # local 
    name = new_name
    print(name)
changeName("Elif")
print(name)
"""
"""
name = "global string"
def greeting():
    name = "Bilal"
    def hello():
        print("Hello "+ name)
    hello()
greeting()
"""
"""
name = "global string"
def greeting():
    name = "Bilal"
    def hello():
        name = "Elif"
        print("Hello "+name)
    hello()
greeting()
"""
"""
name = "global string"
def greeting():
    # name = "Bilal"
    def hello():
        # name = "Elif"
        print("Hello "+name)
    hello()
greeting()
"""
"""
x = 50
def function(x):
    print(f"x is {x}")

    x = 100
    print(f"changed x to {x}")
function(50)
print(x)
"""
x = 50
def function():
    global x
    print(f"x is {x}")

    x = 100
    print(f"changed x to {x}")
function()
print(x)