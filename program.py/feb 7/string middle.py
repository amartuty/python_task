a=input("Enter the string")
length=len(a)
print(length)
index=length//2
print(index)
middle=a[index]
print(middle)
print(f"The middle part of the string {a} is {a[index]}")
print(middle)
print("The middle part of the string {} is {}".format(a,middle))
print("The middle part of the string {0} is {1}".format(a,middle))
