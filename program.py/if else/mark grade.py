#Task 5:


mark1=float(input("tamil mark is:" ))
mark2=float(input("english mark is:" ))
mark3=float(input("maths mark is:" ))
n=int(input("total no of subjects:" ))

total=(mark1+mark2+mark3)
average= total/n

print(average)

if average>=90 and average<=100:
    print("grade A")
elif average>=75 and average<90:
    print("grade B")
elif average>=50 and average<75:
    print("grade C")
else:    
    print("grade D")
