from posixpath import split

name = input()

for i in range(len(name)):
    print("\t",name[i],name[len(name)-i-1])

