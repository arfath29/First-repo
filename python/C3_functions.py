def add(x,y):
    print(x+y)
add(10,20)


def login(username,password):
    if username=="fsa" and password=="1234":
        print("login successful")
    else:
        print("login failed")
login("fsa","1234")

def mul(x,y=10):
    print(x*y)
mul(5)


# list

x=[10,20,91.1,True,"well"]
for i in x:
    print(i)


def test():
    return True
x=test()
if x:
    print("hi")
else:
    print("")