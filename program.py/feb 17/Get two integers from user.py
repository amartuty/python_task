#TASK4

list1 = []
x = int(input("enter the number 1:"))
y = int(input("enter the number 2:"))
for i in range(x,y):
    if (i%8==0):
        list1.append(i)
print("multiple of 8 is:",list1)
