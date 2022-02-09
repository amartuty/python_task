string1=input("enter the string1: ")
string2=input("enter the string2: ")

a=len(string1)
b=len(string2)

print(a)
print(string1[1:a+1])
string3=string2[0]+string1[1:a+1]
string4=string1[0]+string2[1:b+1]

print(string3+string4+str(a)+str(b)+string1[2:4])
