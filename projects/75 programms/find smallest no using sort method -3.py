list1 = [20,40,45]
list1.sort()
small = list1[:1]
print("the small number is:",small)

#method2
list1 = [20,40,45]
small = min(list1)
print("the small number is:",small)

#method 3
lst=[]
n=int(input("enter the no of element"))
for i in range(1,n+1):
    int1 = int(input())
    lst.append(int1)
print("the small number is:",min(lst))
