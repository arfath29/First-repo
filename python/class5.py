# a="hello"
# mystr="welcome \n \"unknown\" "
# print(mystr)
# print(len(a))
# for i in a :
#     print(i,end=" ")

# x=lambda a,b,c:a+b+c
# print(x(20,20,30))

mylist=[10,20,30,40,50,18,13]
# for i in mylist:
#     if i>=18:
#         print("your eligible")
#     else:
#         print("not eligible")

age=filter(lambda x:x>=18,mylist)
for i in age:
    print(i)
    print("eligible")