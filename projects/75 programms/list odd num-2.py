#prg30
#method1
#list odd num
list1 = [10,30,44,55,77]
for i in list1:
    if i%2==1:
        print(i,end=" ")

#31
#method2
list1= [10,21,4,45,66,93]
odd1 =[num for num in list1 if num%2==1]
print(odd1)
[21, 45, 93]
