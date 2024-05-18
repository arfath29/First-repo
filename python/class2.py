i=1
'''
while i<=10:
    print("*")
    i=i+1

for i in range(1,10,1): #last parameter for the increment number
    print("hello")      # without 1st parameter it takes 0 as default value
else:
    print("end")
str="hi"
for i in str:
    print("welcome")


      # multiplication
x=2
for i in range(1,11,1):
    print(x,"x",i,"=",x*1) #output 2x1=2


for k in range(2,6,1):
    for i in range (1,11,1):
        print(k,"x",i,"=",k*1) '''


         # prime number
flag=True
x=int(input("enter the number"))
for i in range(2,x,1):
    if x%2==0:
        print(i)
        flag=False
        break

if flag==True:
    print("prime number")
else:
    print("not prime")


     # ignoring the 5
'''for y in  range(1,10,1):
    if y==5:
        continue
    print(y,end=" ")'''