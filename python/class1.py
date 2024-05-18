'''
a=int(input(print("enter the first number")))
b=int(input(print("enter the second number")))
c=int(input(print("enter the first number")))
if a>b and a>c:
    print("a is greater than",b,"and",c)
elif b>a and b>c:
        print("b is greater than",a,"and",c)
else:
      print("c is greater than",a,"and",b)'''




a=int(input(print("enter the first number")))
operator=input(print("enter arithmetic operator +,-,/,%,*"))
b=int(input(print("enter the second number")))

if operator =="+":
    print(a+b)
elif operator=="*":
    print(a*b)
elif operator=="-":
    print(a-b)
elif operator=="/":
    print(a/b)
elif operator=="%":
    print(a%b)
else:
    print("error")


