#prg36
#find positive numbers method1
list1 = [10,-11,12,-13]
for i in list1:
    if i>=0:
        print(i,end=' ')


#method2
i =0
list1 = [10,-11,12,-13]
n = len(list1)
while i<n:
    if list1[i]>=0:
        print(list1[i],end=' ')
    i+=1


#38
#method3
list1 = [10,-11,12,-13]

pos_nos = [num for num in list1 if num >= 0]
  
print("Positive numbers in the list: ", pos_nos)
