mytuple=("a","b","c","d")
for i in mytuple:
    print(i)

# sets
myset={1,2,3,4,5,6,4,2,3,5}
print(myset) #you may get same order in output
myset1={"google",3,"random","linux","commands"}
myset.union(myset1) # print uncommon

myset2=myset.intersection(myset1)